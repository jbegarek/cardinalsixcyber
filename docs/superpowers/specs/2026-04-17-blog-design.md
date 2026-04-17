# Cardinal Six Cyber Blog — Design Spec

**Date:** 2026-04-17
**Status:** Approved
**Scope:** Blog architecture, content model, publishing workflow, and reader experience

## Overview

Add a first-party blog to cardinalsixcyber.com that supports two explicit content lanes:

- **Practical** for SMB-friendly cybersecurity and CMMC guidance
- **Research** for longer-form essays, academic analysis, citation-heavy writing, and diagram-led pieces

The blog should primarily build trust and authority while also supporting search traffic growth and creating soft pathways into consultation and existing framework/reference pages. The publishing workflow should be lightweight and repo-based so new posts can be published when there is something worth saying, without introducing CMS overhead or requiring a fixed cadence.

## Business Goals

1. Establish Cardinal Six Cyber as a credible voice for SMB cybersecurity and CMMC-related work
2. Create search-visible evergreen content that compounds over time
3. Support existing framework and reference pages through internal linking
4. Preserve room for academic and research-oriented writing without confusing the primary SMB audience
5. Keep conversion pressure low on-page while still making contact paths available

## Primary Audience

### Primary

- Small and mid-sized businesses needing practical cybersecurity help
- Organizations with a special interest in CMMC readiness and defense-contractor adjacent compliance needs

### Secondary

- More technical readers who may value deep research, long-form analysis, or academic framing

### Audience Constraint

The practical lane is the default reader expectation. Research content is allowed and useful, but it must be clearly marked so the site does not drift into an academic journal experience for readers who primarily want operational guidance.

## Information Architecture

### Core Structure

- One top-level destination: **`/blog`**
- One shared index page with explicit filters:
  - `All`
  - `Practical`
  - `Research`
- Individual post pages at **`/blog/{slug}`**

### Navigation

- Add `Blog` as a primary navigation item
- Do **not** add a separate `Research` nav item in the first version
- Keep research discoverable through lane filters, tags, and related-post modules inside the blog

### Rationale

This keeps the blog SEO surface consolidated while still creating a visible distinction between two editorial modes. It avoids the overhead and fragmentation of maintaining two separate content destinations before volume justifies it.

## Content Lanes

### Practical Lane

**Purpose:** Help SMB readers understand what to do, why it matters, and what to prioritize.

**Typical content:**

- CMMC explainers
- SMB cybersecurity checklists
- decision-support articles
- implementation guidance
- plain-language compliance translations
- commentary tied to practical business action

**Editorial rules:**

- Write for clarity first
- Prefer strong headings, scannable sections, and plain language
- Keep jargon controlled and explained
- End with related resources or a soft consultation path

### Research Lane

**Purpose:** Publish deeper analysis, academic work, long-form essays, and evidence-backed argumentation without forcing that style on every reader.

**Typical content:**

- adapted academic work
- long-form essays
- citation-heavy analysis
- model or framework critiques
- diagram-led explainers
- evidence synthesis

**Editorial rules:**

- Signal depth up front
- Support long-form reading with citations, figures, and footnotes
- Translate why the analysis matters for operators or buyers
- Keep the CTA softer than in practical posts

### Lane Relationship

The two lanes share one blog identity but should feel editorially distinct. Practical posts should not read like stripped-down research papers, and research posts should not pretend to be short service-page blog content.

## Publishing Workflow

### Authoring Model

Use **Markdown/MDX in the repo** as the source of truth for blog posts.

### Why

- Fits the desired "publish when I have something" workflow
- Keeps operational complexity low
- Supports version control and future editorial cleanup
- Allows strong formatting without requiring a browser CMS

### Content Technology Direction

Use Astro content collections or an equivalent typed content directory under a path such as:

`src/content/blog/`

Use:

- `.md` for standard posts
- `.mdx` for posts needing richer embedded content, diagrams, or custom components

### Future Compatibility

The initial design should not block a future CMS, but a CMS is explicitly out of scope for version one.

## Content Model

Each post should support the following frontmatter/schema fields:

| Field | Type | Required | Purpose |
|------|------|----------|---------|
| `title` | string | yes | Article title |
| `description` | string | yes | Meta description and index summary |
| `publishDate` | date | yes | Primary publish date |
| `updatedDate` | date | no | Last substantive update |
| `author` | string | yes | Byline |
| `lane` | enum (`practical` \| `research`) | yes | Lane filter and styling logic |
| `topics` | string[] | yes | Tags/topics for filtering and related content |
| `featured` | boolean | no | Optional homepage/blog index feature flag |
| `draft` | boolean | yes | Draft exclusion |
| `heroStyle` | string | no | Visual variant for article hero treatment |
| `heroImage` | string | no | Optional featured image |
| `citations` | boolean | no | Enables citation affordances in layout |
| `diagrams` | boolean | no | Enables figure/diagram affordances in layout |
| `canonicalUrl` | string | no | For syndicated/adapted material if needed |

### Optional Research-Specific Enhancements

- `paperSource`
- `originalContext`
- `readingTimeOverride`

These are optional and should only be added if they provide a real reader-facing benefit.

## Blog Index Experience

### Required Elements

1. Hero/header introducing the blog as a trust-building resource
2. Featured post area
3. Lane filters: `All`, `Practical`, `Research`
4. Topic/tag support
5. Post feed with strong card hierarchy
6. Soft internal links to relevant reference pages

### Visual Behavior

- Practical posts should look more direct and operational
- Research posts should carry stronger visual cues for depth, such as a lane badge, reading-time emphasis, or a more editorial card treatment
- Filtering should be immediate and obvious

### Feed Behavior

The index should support mixed display by default while making the lane distinction obvious. A user landing on `/blog` should understand within a few seconds that:

- there is one blog
- there are two kinds of posts
- practical guidance is still the default business-facing mode

## Article Page Experience

### Shared Requirements

- Use the same site shell as the rest of the Astro site
- Strong reading ergonomics
- Better text measure than the framework/reference pages
- Clear heading rhythm
- readable body copy for long-form work
- strong internal linking support

### Practical Post Page

Priorities:

- quick orientation
- skimmability
- obvious next steps
- links into CMMC and reference content

Recommended sections:

- hero/title area
- problem framing
- actionable guidance
- related resources
- soft CTA

### Research Post Page

Priorities:

- support depth without visual clutter
- citations, notes, figures, and diagrams
- clear explanation of why the piece matters for real-world operators

Recommended sections:

- hero/title area
- abstract or framing note
- long-form body
- figures/diagrams
- citations/footnotes
- short “why this matters” or “operator takeaway” block
- soft CTA or related resources

## CTA Strategy

### Primary Principle

The blog is **trust-first**, not hard-sell.

### Practical Lane CTA Pattern

- Related framework/resource links first
- Light consultation prompt second
- Contact paths should feel available, not forced

Examples:

- "Need help operationalizing this?"
- "Explore the related CMMC controls"
- "Talk with Cardinal Six Cyber"

### Research Lane CTA Pattern

- Softest CTA posture on the site
- Prefer related resources, author note, or optional contact path
- Avoid undermining serious long-form work with aggressive conversion framing

## Internal Linking Strategy

The blog should actively support the rest of the site.

### Required Linking Behaviors

- Practical posts link into `/cmmc`, `/nist-800-171`, `/nist-800-53`, `/resources`, or other relevant pages when useful
- Research posts include operator-facing or framework-facing links where appropriate
- Related-post modules should favor same-lane content first, then adjacent useful content
- Topic pages or tag archives can be deferred, but the schema should anticipate them

## SEO Strategy

### Goals

- Build evergreen search visibility
- avoid thin generic blog pages
- let research pieces earn authority while practical pieces target more commercial or informational intent

### Requirements

- Strong titles and meta descriptions
- canonical handling in layout
- article structured data where appropriate
- lane-aware summaries on the blog index
- good heading structure
- clean slugs
- RSS-ready architecture if added later

### Editorial Constraint

Do not produce filler content just to fill a calendar. The architecture should support quality-over-frequency publishing.

## Technical Implementation Direction

### Recommended Approach

- Astro content collections
- Markdown/MDX source files in repo
- shared blog layout components
- typed frontmatter schema
- reusable components for:
  - lane badge
  - article hero
  - citations/footnotes
  - figure or diagram blocks
  - related posts
  - soft CTA blocks

### Expected New Areas

- `src/content/blog/`
- `src/pages/blog/index.astro`
- `src/pages/blog/[slug].astro`
- blog-specific layout/components under `src/components/` or `src/layouts/`

### Likely Dependency Additions During Implementation

- Astro content collection schema support
- MDX integration for richer posts if not already present
- remark/rehype plugins only if they materially improve citations or long-form readability

## First Delivery Slice

The first implementation slice should prove the model without overbuilding.

### Version 1 Deliverables

1. Blog index page
2. Single post template
3. Lane filtering for `Practical` and `Research`
4. Markdown/MDX authoring support
5. One practical sample post
6. One research sample post
7. Navigation entry to `Blog`

### Deliberately Deferred

- browser CMS
- full topic archive system
- author archive pages
- newsletter system
- comments
- search
- multi-author editorial workflow

## Design Constraints

- Must fit the existing Cardinal Six Astro site, not create a parallel product aesthetic
- Must preserve the premium dark visual language already established in `BaseLayout`, `Nav`, `Footer`, `news`, and `resources`
- Must make long-form content visually readable without flattening the site’s brand
- Must support both light-touch business content and serious citation-heavy writing

## Risks And Mitigations

### Risk: Research content confuses SMB readers

**Mitigation:** Explicit lane labels, filter controls, and distinct card/page treatment

### Risk: Blog becomes a dumping ground for academic work

**Mitigation:** Require research posts to include an operator-facing framing note or takeaway

### Risk: Publishing workflow becomes too heavy

**Mitigation:** Keep version one repo-based, Markdown-first, and schema-driven

### Risk: Practical content starts sounding generic

**Mitigation:** Tie editorial guidance to Cardinal Six’s practitioner voice and existing framework resources

## Out Of Scope

- Full CMS in v1
- forced publishing cadence
- separate `/research` section in v1
- newsletter capture flows
- comments/community features
- analytics-specific editorial automation
