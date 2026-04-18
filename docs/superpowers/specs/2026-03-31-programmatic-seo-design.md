# Programmatic SEO Pages — Design Spec

**Date:** 2026-03-31
**Status:** Approved
**Scope:** CMMC Practice Pages + NIST 800-171 Requirement Pages

## Overview

Build ~220 programmatic SEO pages for cardinalsixcyber.com: 110 CMMC 2.0 practices (17 of which are Level 1, all 110 are Level 2 — Level 1 is a subset of Level 2) and ~110 NIST 800-171 requirements. One page per practice — not separate pages per level. These pages serve as a compliance reference hub that drives organic search traffic from defense contractors and federal agencies.

**Business model:** Level 1 practice pages funnel visitors to C6 Overwatch (overwatch.cardinalsixcyber.com) for free self-assessment. Level 2 practice pages funnel visitors to paid consultation with Cardinal Six Cyber.

## Content Architecture

### Content Types

| Type | Count | URL Pattern | Index Page |
|------|-------|-------------|------------|
| CMMC Practices | 110 | `/cmmc/{practice-id}` | `/cmmc/` |
| NIST 800-171 Requirements | ~110 | `/nist-800-171/{requirement-id}` | `/nist-800-171/` |

One page per practice/requirement. The 17 Level 1 practices are a subset of the 110 — they get a "Level 1" badge on their page and a different CTA, not a separate page.

### Cross-Linking

- Every CMMC practice page links to its mapped NIST 800-171 requirement(s)
- Every NIST 800-171 page links back to the CMMC practice(s) referencing it
- Both link to relevant NIST 800-53 controls as text references (not full pages yet)
- Every page links to 3-4 related practices/requirements in the same domain/family
- Index pages link to all practices/requirements
- Homepage services section links to both index pages
- Footer gets a new "Resources" column linking to both indexes

### Data Files

Two curated JSON files in `data/`, alongside the existing `data/news.json`:

**`data/cmmc-practices.json`**
```json
{
  "practices": [
    {
      "id": "ac-l2-3-1-1",
      "displayId": "AC.L2-3.1.1",
      "title": "Authorized Access Control",
      "domain": "Access Control",
      "domainCode": "AC",
      "level": 2,
      "description": "Limit system access to authorized users...",
      "assessmentObjectives": [
        "Authorized users are identified",
        "Processes acting on behalf of authorized users are identified"
      ],
      "nist800171": ["3-1-1"],
      "nist80053": ["AC-2", "AC-3"],
      "notes": null
    }
  ]
}
```

**`data/nist-800-171.json`**
```json
{
  "requirements": [
    {
      "id": "3-1-1",
      "displayId": "3.1.1",
      "title": "Authorized Access",
      "family": "Access Control",
      "familyCode": "03.01",
      "description": "Limit system access to authorized users...",
      "assessmentObjectives": ["..."],
      "nist80053": ["AC-2", "AC-3"],
      "cmmcPractices": ["ac-l2-3-1-1"],
      "notes": null
    }
  ]
}
```

Key schema decisions:
- `id` is the URL slug (lowercase, hyphens)
- `displayId` is the human-readable format shown in headings/breadcrumbs (e.g., `AC.L2-3.1.1`)
- `nist800171` is an array (some practices map to multiple requirements)
- `nist80053` is an array of control IDs (text references only)
- `notes` is null by default, populated with markdown string when practitioner commentary is added

### Data Seeding

One-time Python script (`scripts/seed-compliance-data.py`):
- Fetches NIST OSCAL 800-171 Rev 2 catalog (publicly available JSON from https://github.com/usnistgov/oscal-content)
- CMMC-to-800-171 mapping is hand-curated from the CMMC 2.0 model document (no official machine-readable API exists) — the seed script includes a hardcoded mapping table derived from the CMMC model PDF
- Transforms into the two JSON formats above
- Run once, commit files, then manually maintained going forward

## Page Templates

### Practice/Requirement Detail Page

Top-to-bottom structure:

1. **Breadcrumb bar** — `Home → CMMC → Access Control → AC.L2-3.1.1`
2. **Header block** — Eyebrow (framework, level, domain), title with displayId, red divider, description paragraph
3. **Cross-reference cards** — 2-column grid: NIST 800-171 mapping (linked) + NIST 800-53 controls (text)
4. **Assessment objectives** — Checklist-style list (decorative checkboxes, not interactive)
5. **Practitioner notes** — Initially empty placeholder with "Coming soon" state. Renders from `notes` field in JSON when populated.
6. **Context-aware CTA**
   - Level 1 practices: "Track your Level 1 progress in C6 Overwatch" → links to `https://overwatch.cardinalsixcyber.com`
   - Level 2-only practices: "Level 2 requires third-party assessment. Start your readiness engagement." → links to `mailto:info@cardinalsixcyber.com` (same consultation flow as homepage CTA)
   - Both include secondary "Explore [domain] practices →" link
7. **Related practices** — 3-4 links to other practices in the same domain

### Index Pages

**`/cmmc/` index:**
- Hero header with "CMMC 2.0 Practices" title
- Sticky filter bar with client-side vanilla JS: domain filter pills + text search input + level toggle (All / Level 1 / Level 2)
- Practices grouped by domain, each group with heading + practice count badge
- Each practice as clickable row: displayId, title, level badge (L1/L2)
- All practices rendered in HTML at build time; JS shows/hides based on active filters

**`/nist-800-171/` index:**
- Same structure, grouped by family
- No level toggle
- Each row shows CMMC practice mapping inline

Both indexes get `CollectionPage` + `BreadcrumbList` JSON-LD and are included in the auto-generated sitemap.

## Technical Implementation

### Astro Setup

- **No content collections** — JSON files live in `data/` and are imported directly in page files using `import` or `fs.readFileSync`, matching the existing `data/news.json` pattern
- Dynamic routes: `src/pages/cmmc/[id].astro` and `src/pages/nist-800-171/[id].astro` using `getStaticPaths()` to generate pages from the JSON data
- Shared detail page component (`src/components/ComplianceDetail.astro`) used by both CMMC and 800-171 detail pages
- Index pages: `src/pages/cmmc/index.astro` and `src/pages/nist-800-171/index.astro`
- `@astrojs/sitemap` auto-discovers all generated pages (~220 new URLs)

### URL Resolution

The existing `build.format: 'file'` in `astro.config.mjs` generates files like `cmmc/ac-l2-3-1-1.html`. Clean URLs (`/cmmc/ac-l2-3-1-1`) are handled by the nginx config which already has `try_files $uri $uri.html $uri/ =404` in the catch-all location block. No Astro config change needed.

### Build Flow

1. `npm run build` → Astro reads JSON data → generates ~220 static HTML pages + 2 indexes
2. Docker multi-stage build (Node builds Astro, nginx serves output)
3. Same SCP + SSH deploy workflow as current

### SEO per Page

- **JSON-LD:** `TechArticle` schema (name, description, datePublished, author) + `BreadcrumbList`
- **Title:** `{displayId} — {Title} | CMMC 2.0 | Cardinal Six Cyber`
- **Meta description:** Generated from practice description, truncated to 155 chars
- **Canonical URL, OG tags, Twitter cards** via BaseLayout (already set up)

### Adding Practitioner Notes

- Edit the `notes` field in the JSON data file for any practice
- Rebuild and deploy
- Template renders notes automatically — no code changes needed

## Design Constraints

- All pages use the existing C6 Cyber design system (dark theme, cardinal red, gold accents, Rajdhani/Inter fonts)
- Page-specific CSS uses `<style is:global>` for any JS-generated content, scoped `<style>` otherwise
- Same accessibility standards (skip link, aria-labels, focus-visible, prefers-reduced-motion)
- Same performance optimizations (WebP images, self-hosted fonts, gzip, cache headers)
- Index page filtering is client-side vanilla JavaScript on a single static page (all items rendered in HTML, JS toggles visibility)

## Out of Scope

- Interactive self-assessment (handled by C6 Overwatch)
- NIST 800-53 control pages (future phase)
- STIG guides hub (future phase)
- Cybersecurity glossary (future phase)
- Blog content (separate effort)
