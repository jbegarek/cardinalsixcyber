# Glossary & NIST 800-53 Pages — Design Spec

**Date:** 2026-04-01
**Status:** Approved
**Scope:** NIST 800-53 Rev 5 Control Pages + Cybersecurity Glossary

## Overview

Add ~1,400 new pages to cardinalsixcyber.com: ~1,100 NIST 800-53 Rev 5 security control pages and 200-300 cybersecurity glossary term pages. All pages cross-link bidirectionally with existing CMMC and NIST 800-171 content. Every page gets practitioner notes written for non-technical business owners with two concrete examples.

## Content Architecture

### Content Types

| Type | Count | URL Pattern | Index Page |
|------|-------|-------------|------------|
| NIST 800-53 Controls | ~1,100 | `/nist-800-53/{control-id}` | `/nist-800-53/` |
| Glossary Terms | 200-300 | `/glossary/{term-slug}` | `/glossary/` |

### Cross-Linking (all bidirectional, live links)

- 800-53 pages link to CMMC practices where mapping exists (via existing `nist80053` field on practices)
- 800-53 pages link to 800-171 requirements where mapping exists
- 800-53 pages link to related 800-53 controls (800-53 has extensive inter-control references)
- Existing CMMC practice pages updated: `nist80053` text badges become links to `/nist-800-53/{id}`
- Existing 800-171 requirement pages updated: same change — `nist80053` becomes links
- Glossary term pages link to relevant CMMC/800-171/800-53 pages where the term is related
- All cross-links render as live `<a>` tags pointing to existing pages

### Data Files

Three files alongside existing `data/cmmc-practices.json`, `data/nist-800-171.json`, `data/news.json`:

**`data/nist-800-53.json`**
```json
{
  "controls": [
    {
      "id": "ac-2",
      "displayId": "AC-2",
      "title": "Account Management",
      "family": "Access Control",
      "familyCode": "AC",
      "description": "...",
      "supplementalGuidance": "...",
      "relatedControls": ["ac-3", "ac-5", "ac-6"],
      "nist800171": ["3-1-1", "3-1-2"],
      "cmmcPractices": ["ac-l2-3-1-1", "ac-l1-3-1-2"],
      "notes": "<p>...</p>"
    }
  ]
}
```

**`data/glossary.json`**
```json
{
  "terms": [
    {
      "id": "ato",
      "term": "Authority to Operate (ATO)",
      "definition": "<p>...</p>",
      "whyItMatters": "<p>...</p>",
      "relatedResources": [
        { "label": "CMMC: AC.L2-3.1.3", "url": "/cmmc/ac-l2-3-1-3" },
        { "label": "NIST 800-53: CA-6", "url": "/nist-800-53/ca-6" }
      ]
    }
  ]
}
```

Key schema decisions:
- `id` is the URL slug (lowercase, hyphens): `AC-2` → `ac-2`, `AC-2(1)` → `ac-2-1`, `AC-21` → `ac-21`. These are unambiguous because base control numbers are never split by hyphens (AC-21 stays `ac-21`), while enhancements always introduce a new hyphen after the base (`ac-2-1`). 800-53 enhancements are single-depth parenthetical only (no nested enhancements).
- `displayId` is human-readable for 800-53 (e.g., `AC-2`, `AC-2(1)`)
- `relatedControls` is an array of 800-53 control slugs (can reference any family, not just same-family)
- `nist800171` and `cmmcPractices` are arrays of slugs linking to existing content
- Glossary `relatedResources` is a pre-computed array of label+url pairs, built at seed time by matching the term name (case-insensitive) against titles and domain/family names in the CMMC, 800-171, and 800-53 data files. Maximum 8 related resources per term.
- `notes` is HTML string with practitioner commentary
- When `supplementalGuidance` is null or empty, the section is hidden on the detail page
- When glossary `relatedResources` is empty, the section is hidden

### Data Seeding

**NIST 800-53 seed script** (`scripts/seed-800-53-data.py`):
- Fetches NIST OSCAL 800-53 Rev 5 catalog from `https://github.com/usnistgov/oscal-content` (public JSON)
- Extracts all controls: id, title, family, description, supplemental guidance, related controls
- Cross-references with existing `data/cmmc-practices.json` and `data/nist-800-171.json` to build the `nist800171` and `cmmcPractices` arrays
- Slug generation: `AC-2` → `ac-2`, `AC-2(1)` → `ac-2-1` (control enhancements use parens in NIST, convert to hyphens)
- Outputs `data/nist-800-53.json`
- Run once, commit, then manually maintained

**Glossary seed script** (`scripts/seed-glossary-data.py`):
- No external API — generates a curated JSON of 200-300 terms
- Terms cover: CMMC terminology, RMF process terms, NIST framework terms, DoD-specific terms, general cybersecurity concepts
- `relatedResources` computed by scanning existing data files for term relevance
- Outputs `data/glossary.json`
- Run once, commit, then manually maintained

## Page Templates

### NIST 800-53 Detail Page

Does NOT reuse `ComplianceDetail.astro` — uses a new `ControlDetail.astro` component. Reason: 800-53 has different data shape (supplemental guidance instead of assessment objectives, no level concept, 3-column cross-refs, related controls from any family). Forcing it into ComplianceDetail would require too many conditional branches.

1. **Breadcrumb:** Home → NIST 800-53 → {Family} → {displayId}
2. **Header:** Eyebrow "NIST 800-53 REV 5 • {FAMILY}" (no level — 800-53 doesn't have CMMC levels), h1 "{displayId} — {title}", divider, description
3. **Cross-reference cards (3-column grid):**
   - Column 1: CMMC Practice mapping (linked if exists, "No direct CMMC mapping" text if not)
   - Column 2: NIST 800-171 mapping (linked if exists, "No direct 800-171 mapping" text if not)
   - Column 3: Related 800-53 controls (all linked — these are inter-control references from any family, from the `relatedControls` array)
4. **Supplemental guidance** section (NIST's own guidance text, in a styled block — hidden when null/empty)
5. **Practitioner notes** with two examples (same format as CMMC notes — hidden when null with placeholder)
6. **CTA:** Consultation CTA (same Level 2 pattern — `mailto:info@cardinalsixcyber.com`)
7. **Same-family controls:** 3-4 links to other controls in the same family for continued browsing (distinct from Section 3's `relatedControls` which are cross-family NIST references)

**JSON-LD:** `TechArticle` + `BreadcrumbList`

### NIST 800-53 Index Page

- Hero: "NIST 800-53 Rev 5 Controls"
- Grouped by family (20 families: AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR)
- Sticky filter bar: family filter pills + text search
- Each row: displayId, title, linked
- JSON-LD: `CollectionPage` + `BreadcrumbList`

### Glossary Entry Page

Does NOT reuse `ComplianceDetail` — uses a new lightweight `GlossaryEntry.astro` component:

1. **Breadcrumb:** Home → Glossary → {Term}
2. **h1:** Term name (e.g., "Authority to Operate (ATO)")
3. **Red divider**
4. **Definition:** 2-3 paragraphs, plain language
5. **"Why It Matters":** 1-2 sentences connecting to compliance journey
6. **Related Resources:** Auto-generated list of linked CMMC/800-171/800-53 pages
7. **Prev/Next navigation:** Alphabetical navigation to adjacent terms

**JSON-LD:** `DefinedTerm` + `BreadcrumbList`

### Glossary Index Page

- Hero: "Cybersecurity Glossary"
- Alphabetical letter bar (A-Z, sticky)
- All terms listed alphabetically: term + one-line summary
- Search bar for filtering
- No domain grouping (alphabetical is natural for a glossary)
- JSON-LD: `CollectionPage` + `BreadcrumbList`

## Technical Implementation

### Astro Setup

Same pattern as existing CMMC/800-171 pages:
- Direct JSON imports from `data/` (no content collections)
- Dynamic routes: `src/pages/nist-800-53/[id].astro`, `src/pages/glossary/[id].astro`
- `getStaticPaths()` generates pages from JSON data
- New component: `src/components/GlossaryEntry.astro` (lightweight, glossary-specific)
- New component: `src/components/ControlDetail.astro` (800-53 detail page — separate from ComplianceDetail due to different data shape)
- Existing `ComplianceDetail.astro` updated: `nist80053` text badges become links to `/nist-800-53/{slug}`

### Updating Existing Pages

- `src/pages/cmmc/[id].astro` — update to render `nist80053` as links to `/nist-800-53/{slug}`. The existing data stores display IDs (e.g., `"AC-2"`); convert to slugs at render time with `.toLowerCase()` (e.g., `ac-2`). This is a behavioral change from text badges to links — now that 800-53 pages exist.
- `src/pages/nist-800-171/[id].astro` — same update
- `src/components/ComplianceDetail.astro` — update the `nist80053` rendering section: instead of `<span>` text badges, render `<a href="/nist-800-53/{slug}">` links. The slug is derived from the display ID by lowercasing. No structural changes to the component's props — the `nist80053` array keeps its current format (display IDs), the template handles the conversion.
- `src/components/Footer.astro` — add Glossary and NIST 800-53 to Resources column

### URL Resolution

Same `build.format: 'file'` + nginx `try_files $uri $uri.html $uri/ =404` pattern. No config changes needed.

### Build Flow

1. `npm run build` → generates ~1,600+ total pages (existing 227 + ~1,100 800-53 + ~250 glossary + 2 indexes)
2. Same Docker multi-stage build
3. Same SCP + SSH deploy

### SEO per Page

- 800-53 pages: `TechArticle` + `BreadcrumbList` schema, title "{displayId} — {title} | NIST 800-53 | Cardinal Six Cyber"
- Glossary pages: `DefinedTerm` + `BreadcrumbList` schema, title "{Term} | Cybersecurity Glossary | Cardinal Six Cyber"
- All pages get canonical URLs, OG tags, Twitter cards via BaseLayout

## Practitioner Notes

**NIST 800-53 (~1,100 controls):**
- Plain-language explanation + two concrete examples (GPO, M365, firewall, tool settings)
- For controls mapping to existing CMMC practices: expand with additional examples from a different angle
- For unmapped controls: fresh notes with relevant practical guidance
- Generated in batches by family (20 families) via parallel agents

**Glossary (200-300 terms):**
- 2-3 paragraph definition for non-technical business owners
- "Why it matters" paragraph connecting to their compliance journey
- Generated in alphabetical batches via parallel agents

## Design Constraints

- Same C6 Cyber design system (dark theme, design tokens, fonts)
- Same accessibility standards (skip link, aria-labels, focus-visible, prefers-reduced-motion)
- `<style is:global>` for JS-generated filter elements on index pages, scoped elsewhere
- Glossary pages use scoped styles only (no JS-generated content)

## Out of Scope

- STIG guides hub (future phase)
- Blog content (separate effort)
- Interactive features (handled by C6 Overwatch)
