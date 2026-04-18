# Programmatic SEO Pages — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate ~220 static compliance reference pages (110 CMMC practices + ~110 NIST 800-171 requirements) with cross-linking, structured data, and context-aware CTAs.

**Architecture:** JSON data files in `data/` are read by Astro dynamic routes at build time via `getStaticPaths()`. A shared `ComplianceDetail.astro` component renders both CMMC and 800-171 detail pages. Index pages render all items at build time with client-side JS filtering. No content collections — direct JSON imports.

**Tech Stack:** Astro (static), Python 3 (data seeding), vanilla JS (index filtering), existing nginx/Docker deploy

**Spec:** `docs/superpowers/specs/2026-03-31-programmatic-seo-design.md`

---

## File Map

### New Files
| File | Responsibility |
|------|---------------|
| `scripts/seed-compliance-data.py` | One-time script: fetch NIST OSCAL 800-171 data, apply hardcoded CMMC mapping, output two JSON files |
| `data/cmmc-practices.json` | All 110 CMMC practices with IDs, descriptions, mappings, assessment objectives |
| `data/nist-800-171.json` | All ~110 NIST 800-171 requirements with IDs, descriptions, mappings |
| `src/components/ComplianceDetail.astro` | Shared detail page template (header, cross-refs, objectives, notes, CTA, related) |
| `src/components/ComplianceCTA.astro` | Context-aware CTA block (Level 1 → Overwatch, Level 2 → consultation) |
| `src/pages/cmmc/[id].astro` | Dynamic route: generates one page per CMMC practice |
| `src/pages/cmmc/index.astro` | CMMC index page with domain grouping + filter/search |
| `src/pages/nist-800-171/[id].astro` | Dynamic route: generates one page per 800-171 requirement |
| `src/pages/nist-800-171/index.astro` | NIST 800-171 index page with family grouping + filter/search |

### Modified Files
| File | Change |
|------|--------|
| `src/components/Footer.astro` | Add "Resources" column with links to `/cmmc/` and `/nist-800-171/` |
| `src/components/Nav.astro` | Add "Resources" link to nav and mobile overlay |
| `src/styles/global.css` | Update footer grid to 5 columns including responsive breakpoints |
| `src/pages/index.astro` | Add links from services section to `/cmmc/` and `/nist-800-171/` |

---

### Task 1: Data Seeding Script — CMMC Mapping Table

**Files:**
- Create: `scripts/seed-compliance-data.py` (partial — mapping table only)

- [ ] **Step 1: Create the script file with the CMMC mapping dict**

Create `scripts/seed-compliance-data.py` containing the `CMMC_MAPPING` dictionary — a Python dict mapping all 110 NIST 800-171 requirement IDs to their CMMC practice metadata (practiceId, domain, domainCode, level). The 17 Level 1 practices have `level: 1`. All others have `level: 2`.

Source: CMMC Model v2.0 document. The mapping is 1:1 — each 800-171 requirement maps to exactly one CMMC practice.

```python
#!/usr/bin/env python3
"""Seed compliance data from NIST OSCAL + CMMC mapping."""
import json
import urllib.request
import os

# CMMC 2.0 practice-to-800-171 mapping (hand-curated from CMMC Model v2.0)
# Key = NIST 800-171 requirement ID (dotted), Value = CMMC practice metadata
CMMC_MAPPING = {
    # Access Control (AC) — Level 1
    "3.1.1": {"practiceId": "AC.L1-3.1.1", "domain": "Access Control", "domainCode": "AC", "level": 1},
    "3.1.2": {"practiceId": "AC.L1-3.1.2", "domain": "Access Control", "domainCode": "AC", "level": 1},
    "3.1.20": {"practiceId": "AC.L1-3.1.20", "domain": "Access Control", "domainCode": "AC", "level": 1},
    "3.1.22": {"practiceId": "AC.L1-3.1.22", "domain": "Access Control", "domainCode": "AC", "level": 1},
    # Access Control (AC) — Level 2
    "3.1.3": {"practiceId": "AC.L2-3.1.3", "domain": "Access Control", "domainCode": "AC", "level": 2},
    # ... (complete all 110 entries)
    # Populate the full mapping from the CMMC Model v2.0 document
}
```

Ensure all 14 CMMC domains are represented: Access Control (AC), Awareness & Training (AT), Audit & Accountability (AU), Configuration Management (CM), Identification & Authentication (IA), Incident Response (IR), Maintenance (MA), Media Protection (MP), Personnel Security (PS), Physical Protection (PE), Risk Assessment (RA), Security Assessment (CA), System & Communications Protection (SC), System & Information Integrity (SI).

- [ ] **Step 2: Verify mapping count**

```bash
python -c "exec(open('scripts/seed-compliance-data.py').read()); print(f'{len(CMMC_MAPPING)} mappings'); l1=[v for v in CMMC_MAPPING.values() if v['level']==1]; print(f'{len(l1)} Level 1')"
```
Expected: `110 mappings` and `17 Level 1`

- [ ] **Step 3: Commit**

```bash
git add scripts/seed-compliance-data.py
git commit -m "feat: add CMMC-to-800-171 mapping table"
```

---

### Task 2: Data Seeding Script — OSCAL Fetch & JSON Output

**Files:**
- Modify: `scripts/seed-compliance-data.py`
- Create: `data/cmmc-practices.json`
- Create: `data/nist-800-171.json`

- [ ] **Step 1: Add OSCAL fetch and parse logic**

Add functions to `scripts/seed-compliance-data.py`:
- `fetch_oscal()` — downloads the NIST OSCAL 800-171 Rev 2 catalog JSON from `https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-171/rev2/json/NIST_SP-800-171_rev2_catalog.json`
- `parse_requirements(catalog)` — extracts each control from the OSCAL catalog: id, title, family, description text, assessment objective parts, related 800-53 props
- `build_output(requirements)` — cross-references with `CMMC_MAPPING` to produce both JSON output files

ID slug generation:
- 800-171: `3.1.1` → `3-1-1` (replace dots with hyphens)
- CMMC: `AC.L2-3.1.1` → `ac-l2-3-1-1` (lowercase, replace dots with hyphens)

- [ ] **Step 2: Add main function and JSON output**

Add the `main()` function that orchestrates fetch → parse → build → write. Ensure the `data/` directory exists (`os.makedirs('data', exist_ok=True)`). Write both JSON files with `indent=2` for readability.

- [ ] **Step 3: Run the seed script**

```bash
python scripts/seed-compliance-data.py
```
Expected: Two JSON files in `data/`. Verify:
```bash
python -c "import json; d=json.load(open('data/cmmc-practices.json')); print(f'{len(d[\"practices\"])} practices'); l1=[p for p in d['practices'] if p['level']==1]; print(f'{len(l1)} Level 1')"
```
Expected: `110 practices` and `17 Level 1`

- [ ] **Step 4: Verify cross-references**

```bash
python -c "
import json
cmmc = json.load(open('data/cmmc-practices.json'))['practices']
nist = json.load(open('data/nist-800-171.json'))['requirements']
for p in cmmc:
    for ref in p['nist800171']:
        assert any(r['id'] == ref for r in nist), f'CMMC {p[\"id\"]} refs missing 800-171 {ref}'
for r in nist:
    for ref in r['cmmcPractices']:
        assert any(p['id'] == ref for p in cmmc), f'800-171 {r[\"id\"]} refs missing CMMC {ref}'
print('All cross-references valid')
"
```

- [ ] **Step 5: Commit**

```bash
git add scripts/seed-compliance-data.py data/cmmc-practices.json data/nist-800-171.json
git commit -m "feat: seed compliance data from NIST OSCAL"
```

---

### Task 3: CTA Component

**Files:**
- Create: `src/components/ComplianceCTA.astro`

- [ ] **Step 1: Create the CTA component**

Write `src/components/ComplianceCTA.astro`:

Props interface:
```typescript
interface Props {
    level: number;        // 1 or 2 (800-171 pages pass 2)
    groupName: string;    // domain name (CMMC) or family name (800-171)
    groupIndexUrl: string; // e.g., /cmmc#ac or /nist-800-171#03-01
}
```

Renders:
- Level 1: heading "Track Your Level 1 Progress", text about C6 Overwatch, primary button linking to `https://overwatch.cardinalsixcyber.com`, secondary explore link
- Level 2: heading "Level 2 Requires Assessment", text about practitioner-led readiness, primary button `mailto:info@cardinalsixcyber.com`, secondary explore link

Scoped CSS using C6 design tokens: dark card background (`--c6-black-elevated`), `--c6-border`, red divider, proper spacing.

- [ ] **Step 2: Commit**

```bash
git add src/components/ComplianceCTA.astro
git commit -m "feat: add context-aware compliance CTA component"
```

---

### Task 4: Detail Component — Skeleton & Header Sections

**Files:**
- Create: `src/components/ComplianceDetail.astro`

- [ ] **Step 1: Create the component with props and sections 1-3**

Write `src/components/ComplianceDetail.astro` with this props interface:

```typescript
interface Props {
    framework: 'cmmc' | 'nist-800-171';
    id: string;
    displayId: string;
    title: string;
    groupName: string;      // domain (CMMC) or family (800-171)
    groupCode: string;       // domainCode or familyCode
    level: number;           // CMMC level (1 or 2); 800-171 passes 2
    description: string;
    assessmentObjectives: string[];
    crossRefs: { label: string; items: { id: string; displayId: string; url: string }[] }[];
    nist80053: string[];
    notes: string | null;
    relatedItems: { id: string; displayId: string; title: string; url: string }[];
}
```

Implement sections 1-3:
1. Breadcrumb bar — linked: Home → {Framework label} → {groupName} → {displayId}
2. Header block — eyebrow text, h1 with displayId + title, red divider, description paragraph
3. Cross-reference cards — 2-column grid with gold labels

Scoped CSS using C6 design tokens.

- [ ] **Step 2: Commit**

```bash
git add src/components/ComplianceDetail.astro
git commit -m "feat: add ComplianceDetail component (breadcrumb, header, cross-refs)"
```

---

### Task 5: Detail Component — Objectives, Notes, CTA, Related

**Files:**
- Modify: `src/components/ComplianceDetail.astro`

- [ ] **Step 1: Add sections 4-7**

Add to `ComplianceDetail.astro`:

4. Assessment objectives — styled list with decorative checkbox SVGs (not interactive)
5. Practitioner notes — renders `notes` as HTML if populated, shows a styled placeholder ("Practitioner commentary coming soon") if null
6. `<ComplianceCTA>` — import and render with `level`, `groupName`, and `groupIndexUrl` props
7. Related items — grid of 3-4 linked cards showing displayId and title

Add remaining scoped CSS.

- [ ] **Step 2: Verify component renders**

Create `src/pages/_test.astro` with hardcoded sample data for one CMMC practice. Run `npm run build` and check `dist/_test.html` renders correctly. Delete the test page.

- [ ] **Step 3: Commit**

```bash
git add src/components/ComplianceDetail.astro
git commit -m "feat: complete ComplianceDetail with objectives, notes, CTA, related"
```

---

### Task 6: CMMC Dynamic Route

**Files:**
- Create: `src/pages/cmmc/[id].astro`

- [ ] **Step 1: Create the dynamic route**

Write `src/pages/cmmc/[id].astro`:
- Import `BaseLayout`, `ComplianceDetail`, and both JSON data files
- `getStaticPaths()` maps over `cmmcData.practices`, returning `params: { id }` and `props: { practice }`
- Build cross-refs: map `practice.nist800171` IDs to `{ id, displayId, url }` objects by looking up in `nistData.requirements`
- Build related items: same domain, excluding self, max 4
- Pass `activePage="resources"` to BaseLayout
- Pass `ogTitle={practice.displayId + ' — ' + practice.title}` to BaseLayout for clean social sharing
- JSON-LD: `TechArticle` schema with `datePublished: "2026-03-31"` + `BreadcrumbList`
- Page title: `{displayId} — {title} | CMMC 2.0 | Cardinal Six Cyber`
- Meta description: `practice.description.slice(0, 155)`

- [ ] **Step 2: Build and verify**

```bash
npm run build 2>&1 | tail -20
```
Expected: 110 `/cmmc/*.html` pages generated, no errors.

Spot-check:
```bash
grep "AC.L2-3.1.1" dist/cmmc/ac-l2-3-1-1.html | head -3
```

- [ ] **Step 3: Commit**

```bash
git add src/pages/cmmc/
git commit -m "feat: add CMMC practice detail pages (110 pages)"
```

---

### Task 7: NIST 800-171 Dynamic Route

**Files:**
- Create: `src/pages/nist-800-171/[id].astro`

- [ ] **Step 1: Create the dynamic route**

Same pattern as CMMC route but:
- Imports from `nist-800-171.json`
- Cross-refs point to CMMC practice pages (reverse direction): map `req.cmmcPractices` to `{ id, displayId, url }` from CMMC data
- Pass `groupName={req.family}`, `groupCode={req.familyCode}` to ComplianceDetail
- Pass `level={2}` (all 800-171 requirements are Level 2 equivalent for CTA purposes)
- Pass `activePage="resources"` to BaseLayout
- Title: `{displayId} — {title} | NIST 800-171 | Cardinal Six Cyber`
- Breadcrumb: Home → NIST 800-171 → {family} → {displayId}
- JSON-LD: TechArticle with `datePublished: "2026-03-31"` + BreadcrumbList

- [ ] **Step 2: Build and verify**

```bash
npm run build 2>&1 | tail -20
```
Expected: ~110 `/nist-800-171/*.html` pages generated.

- [ ] **Step 3: Commit**

```bash
git add src/pages/nist-800-171/
git commit -m "feat: add NIST 800-171 requirement detail pages (~110 pages)"
```

---

### Task 8: CMMC Index Page

**Files:**
- Create: `src/pages/cmmc/index.astro`

- [ ] **Step 1: Create the index page**

Write `src/pages/cmmc/index.astro`:
- Import `BaseLayout` and `cmmc-practices.json`
- Pass `activePage="resources"`, `navFixed={false}` to BaseLayout
- Hero header: eyebrow "Compliance Reference", h1 "CMMC 2.0 Practices", red divider, subtitle
- Build domain groups from data at build time: `Object.groupBy` or manual reduce
- Render all practices in HTML grouped by domain, each row with `data-domain`, `data-level`, and searchable text attributes
- Sticky filter bar with:
  - Domain filter pills (each shows count)
  - Text search input
  - Level toggle: All / Level 1 / Level 2 buttons
- Client-side vanilla JS in a `<script>` tag: reads filter state, toggles `display:none` on rows. Use `<style is:global>` for any JS-generated elements.
- JSON-LD: `CollectionPage` + `BreadcrumbList` (Home → CMMC)
- Each domain section gets an `id` attribute matching `domainCode.toLowerCase()` for anchor linking from breadcrumbs

- [ ] **Step 2: Build and verify**

```bash
npm run build && grep -c "practice-row" dist/cmmc/index.html
```
Expected: 110 practice rows in the output.

- [ ] **Step 3: Commit**

```bash
git add src/pages/cmmc/index.astro
git commit -m "feat: add CMMC practices index page with filtering"
```

---

### Task 9: NIST 800-171 Index Page

**Files:**
- Create: `src/pages/nist-800-171/index.astro`

- [ ] **Step 1: Create the index page**

Same pattern as CMMC index but:
- Grouped by family instead of domain
- No level toggle
- Each row shows CMMC practice mapping inline (e.g., "→ AC.L2-3.1.1")
- Title: "NIST 800-171 Requirements | Cardinal Six Cyber"
- Breadcrumb: Home → NIST 800-171

- [ ] **Step 2: Build and verify**

```bash
npm run build && grep -c "requirement-row" dist/nist-800-171/index.html
```

- [ ] **Step 3: Commit**

```bash
git add src/pages/nist-800-171/index.astro
git commit -m "feat: add NIST 800-171 requirements index page with filtering"
```

---

### Task 10: Navigation, Footer & Homepage Updates

**Files:**
- Modify: `src/components/Footer.astro`
- Modify: `src/components/Nav.astro`
- Modify: `src/styles/global.css`
- Modify: `src/pages/index.astro`

- [ ] **Step 1: Add Resources column to Footer**

In `src/components/Footer.astro`, add a new `footer-col` between "Company" and "Contact":
```html
<div class="footer-col">
    <p class="footer-heading">Resources</p>
    <ul>
        <li><a href="/cmmc">CMMC Practices</a></li>
        <li><a href="/nist-800-171">NIST 800-171</a></li>
    </ul>
</div>
```

- [ ] **Step 2: Update footer grid in global.css**

Update the footer grid to 5 columns. In `src/styles/global.css`:
- Desktop: change `grid-template-columns: 2fr 1fr 1fr 1.5fr` to `2fr 1fr 1fr 1fr 1.5fr`
- 1024px breakpoint: keep `grid-template-columns: 1fr 1fr` (wraps naturally)
- 768px breakpoint: keep `grid-template-columns: 1fr` (stacks)

- [ ] **Step 3: Add Resources link to Nav**

In `src/components/Nav.astro`, add a nav link between "Frameworks" and "Cyber News":
```html
<li><a href="/cmmc" class={activePage === 'resources' ? 'nav-active' : ''}>Resources</a></li>
```

Also add to the mobile overlay:
```html
<a href="/cmmc" class="mobile-link">Resources</a>
```

- [ ] **Step 4: Add compliance links to homepage services section**

In `src/pages/index.astro`, after the services grid closing `</div>`, add a small "Explore our compliance reference" link block:
```html
<div class="services-cta reveal reveal-delay-3" style="text-align:center; margin-top:var(--space-10);">
    <a href="/cmmc" class="btn-secondary" style="margin-right:var(--space-4);">CMMC Practices</a>
    <a href="/nist-800-171" class="btn-secondary">NIST 800-171</a>
</div>
```

- [ ] **Step 5: Build and verify**

```bash
npm run build
```
Verify footer has 5 columns, nav has Resources link, and homepage has compliance links.

- [ ] **Step 6: Commit**

```bash
git add src/components/Footer.astro src/components/Nav.astro src/styles/global.css src/pages/index.astro
git commit -m "feat: add Resources links to nav, footer, and homepage"
```

---

### Task 11: Full Build, Verify & Deploy

**Files:** None (integration verification)

- [ ] **Step 1: Clean build**

```bash
rm -rf dist && npm run build
```
Expected: ~225+ pages built, no errors.

- [ ] **Step 2: Verify sitemap**

```bash
grep -c "<loc>" dist/sitemap-0.xml
```
Expected: 225+ URLs

- [ ] **Step 3: Spot-check pages**

Level 1 practice has Overwatch CTA:
```bash
grep -l "C6 Overwatch" dist/cmmc/*.html | head -3
```

Level 2 practice has consultation CTA:
```bash
grep -l "Request Consultation" dist/cmmc/*.html | head -3
```

Cross-linking works (CMMC → 800-171):
```bash
grep "nist-800-171" dist/cmmc/ac-l2-3-1-1.html | head -2
```

Reverse cross-linking (800-171 → CMMC):
```bash
grep "/cmmc/" dist/nist-800-171/3-1-1.html | head -2
```

- [ ] **Step 4: Deploy**

```bash
scp -r src/ public/ data/ astro.config.mjs package.json package-lock.json Dockerfile nginx/ justin@192.168.0.240:/home/justin/deploy/cardinalsixcyber/
ssh justin@192.168.0.240 "cd /home/justin/deploy/cardinalsixcyber && docker compose build && docker compose up -d"
```

- [ ] **Step 5: Verify live**

```bash
ssh justin@192.168.0.240 'for p in /cmmc /cmmc/ac-l2-3-1-1 /nist-800-171 /nist-800-171/3-1-1; do CODE=$(docker exec cardinalsixcyber wget -q -O /dev/null -S "http://127.0.0.1$p" 2>&1 | grep "HTTP/" | awk "{print \$2}"); echo "$p -> $CODE"; done'
```
Expected: All return `200`

- [ ] **Step 6: Commit**

```bash
git add src/ data/ scripts/ public/
git commit -m "feat: deploy programmatic SEO — 220+ compliance reference pages"
```
