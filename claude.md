# Cardinal Six Cybersecurity — Website Project

## DO THIS FIRST
**Invoke 'frontend-design' skill before generating any code.** Do it every
time you want to code front-end. In every session. Never skip this step.

---

## Brand Identity

**Company:** Cardinal Six Cyber LLC (also branded as C6 Cyber)
**Parent Company:** Begarek Enterprises LLC
**Industry:** Cybersecurity consulting — CMMC readiness, RMF/NIST compliance, STIG compliance, vulnerability management, risk management
**Target Audience:** Small/mid defense contractors, healthcare organizations, federal agencies, critical infrastructure
**Brand Personality:** Commanding, premium, military authority, personal legacy, deeply credible
**Owner:** Justin T. Begarek — GS-13 IT Cybersecurity Specialist (INFOSEC), Military Sealift Command, TS/SCI clearance, PhD candidate in Cybersecurity

### Brand Story
"Cardinal" honors the founder's late grandfather — the cardinal bird represents family legacy and watchful protection. "Six" is military radio terminology for the commanding officer. Together, Cardinal Six represents leadership, protection, and personal mission. The brand shorthand is "C6 Cyber."

### Brand Tagline Options
- "Command Your Defense."
- "Eyes Forward. Shields Up."
- "Leading From the Front."

---

## Visual References

- The folder `@web_design_references` contains visual references I want you to use when creating web pages
- If you see images in this folder: match layout structure, colors, spacing, typography choices from the provided examples when coding our web page.
- If no reference images are provided: design from scratch, following the rules provided below in the 'Anti-Generic Design Guardrails' section
- When you finish coding the page, capture a page screenshot of the page you've generated and compare it against the references provided in the folder `@web_design_references`. Find and fix any mismatches. Do at least two rounds of comparison and fix. Keep all screenshots you capture in the folder `@screenshots`

### Reference Sites
Study these for layout patterns, motion design, and premium cybersecurity aesthetic:

- **https://arcticwolf.com/** — Premium cybersecurity brand. Study their hero sections, dark backgrounds with selective color pops, sophisticated navigation patterns, and how they balance authority with approachability. Note their use of gradient overlays and layered depth.
- **https://www.behance.net/gallery/243353425/Cybersecurity-Dashboard-UI-UX** — Dashboard UI/UX reference. Study the dark-themed card layouts, data visualization patterns, subtle glow effects, and how they use accent colors sparingly against deep backgrounds.
- **https://www.behance.net/gallery/244133503/NexGuard-Cybersecurity-Branding-for-Tech-Startup** — Cybersecurity startup branding. Study their brand identity system, how they integrate geometric shapes with the brand mark, and their approach to dark/light contrast with accent colors.

When you finish coding the page, capture page screenshot of the page you've generated and compare it against references provided in the folder `@web_design_references`. Find and fix any mismatches. Do at least two rounds of comparison and fix. Keep all screenshots you capture in png format in the folder `@screenshots`

---

## Design System — Cardinal Six Cyber

### Color Palette

Extracted from the current Coming Soon page and expanded for full site use.

#### Core Colors
```
--c6-black:           #0a0a0a;     /* Primary background — near-black, deep, tactical */
--c6-black-elevated:  #111111;     /* Slightly elevated surfaces — cards, nav */
--c6-black-surface:   #1a1a1a;     /* Secondary surfaces — sections, modals */
--c6-charcoal:        #1A1A2E;     /* Deep charcoal with blue undertone — alternate dark */
```

#### Cardinal Red System
```
--c6-red:             #c0392b;     /* Primary brand red — from current site, links, dividers, CTAs */
--c6-red-bright:      #C41E3A;     /* Cardinal red — slightly more vivid for hero elements */
--c6-red-dark:        #8B1A1A;     /* Darkened red — for pressed/active states */
--c6-red-glow:        rgba(192, 57, 43, 0.15);  /* Red glow for hover halos and ambient effects */
--c6-red-gradient:    linear-gradient(135deg, #C41E3A 0%, #c0392b 50%, #8B1A1A 100%);
```

#### Gold Accent System
```
--c6-gold:            #C9A84C;     /* Military insignia gold — premium accent */
--c6-gold-light:      #D4B96A;     /* Lighter gold for hover states */
--c6-gold-dark:       #A8893A;     /* Darker gold for active states */
--c6-gold-glow:       rgba(201, 168, 76, 0.12);  /* Gold ambient glow */
```

#### Text Hierarchy
```
--c6-text-primary:    #ffffff;     /* White — headings, primary content */
--c6-text-secondary:  #cccccc;     /* Light gray — from current h1 color, subheadings */
--c6-text-body:       #888888;     /* Mid gray — from current paragraph color, body text */
--c6-text-muted:      #666666;     /* Dark gray — from current contact text, captions, metadata */
--c6-text-dim:        #444444;     /* Dimmest text — disabled states, fine print */
```

#### Functional Colors
```
--c6-border:          rgba(255, 255, 255, 0.06);  /* Subtle divider lines */
--c6-border-accent:   rgba(192, 57, 43, 0.3);     /* Red-tinted borders for emphasis */
--c6-overlay:         rgba(10, 10, 10, 0.85);      /* Modal/overlay backdrop */
--c6-success:         #2ECC71;     /* Success states */
--c6-warning:         #F39C12;     /* Warning states */
--c6-error:           #E74C3C;     /* Error states (distinct from brand red) */
```

#### Gradient Definitions
```
/* Hero background — deep layered depth */
--c6-gradient-hero:       linear-gradient(180deg, #0a0a0a 0%, #111111 40%, #0a0a0a 100%);

/* Section alternation — subtle depth shift */
--c6-gradient-section:    linear-gradient(180deg, #0a0a0a 0%, #0f0f0f 50%, #0a0a0a 100%);

/* Red accent gradient — for CTAs, dividers, highlights */
--c6-gradient-accent:     linear-gradient(90deg, #C41E3A 0%, #c0392b 100%);

/* Gold accent gradient — for premium elements */
--c6-gradient-gold:       linear-gradient(90deg, #A8893A 0%, #C9A84C 50%, #D4B96A 100%);

/* Subtle radial glow — for background ambient effects */
--c6-glow-red:            radial-gradient(ellipse at center, rgba(192, 57, 43, 0.08) 0%, transparent 70%);
--c6-glow-gold:           radial-gradient(ellipse at center, rgba(201, 168, 76, 0.06) 0%, transparent 70%);

/* Card hover glow */
--c6-gradient-card-hover: linear-gradient(135deg, rgba(192, 57, 43, 0.05) 0%, rgba(26, 26, 46, 0.8) 100%);
```

### Typography

#### Font Stack
```
/* Display / Headings — commanding, tight, uppercase-friendly */
--font-display: 'Rajdhani', 'Exo 2', 'Segoe UI', sans-serif;

/* Body / Paragraphs — clean, readable, professional */
--font-body: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

/* Mono / Technical — for code, data, technical specs */
--font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
```

Google Fonts import:
```
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
```

#### Type Scale
```
/* Hero title */
font-family: var(--font-display);
font-size: clamp(2.5rem, 5vw, 4.5rem);
font-weight: 700;
letter-spacing: 0.05em;
text-transform: uppercase;
line-height: 1.1;

/* Section headings (h2) */
font-family: var(--font-display);
font-size: clamp(1.8rem, 3vw, 3rem);
font-weight: 600;
letter-spacing: 0.04em;
text-transform: uppercase;
line-height: 1.2;

/* Subheadings (h3) */
font-family: var(--font-display);
font-size: clamp(1.2rem, 2vw, 1.8rem);
font-weight: 500;
letter-spacing: 0.03em;
line-height: 1.3;

/* Body text */
font-family: var(--font-body);
font-size: 1rem;  /* 16px base */
font-weight: 400;
letter-spacing: 0.01em;
line-height: 1.7;
color: var(--c6-text-body);

/* Small / Caption text */
font-family: var(--font-body);
font-size: 0.875rem;
font-weight: 400;
letter-spacing: 0.02em;
line-height: 1.5;
color: var(--c6-text-muted);

/* Eyebrow / Label text (like "Coming Soon" on current site) */
font-family: var(--font-display);
font-size: 1rem;
font-weight: 300;
letter-spacing: 0.3em;
text-transform: uppercase;
color: var(--c6-text-secondary);
```

### Shadows

Never use default Tailwind shadows. Use these layered, color-tinted custom shadows:

```
/* Subtle card elevation */
--shadow-card:        0 1px 3px rgba(0, 0, 0, 0.4), 0 4px 12px rgba(0, 0, 0, 0.3);

/* Elevated card on hover */
--shadow-card-hover:  0 2px 8px rgba(0, 0, 0, 0.5), 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 40px var(--c6-red-glow);

/* Red-tinted CTA button shadow */
--shadow-cta:         0 2px 8px rgba(192, 57, 43, 0.3), 0 4px 16px rgba(192, 57, 43, 0.15);

/* Gold-tinted premium element shadow */
--shadow-gold:        0 2px 8px rgba(201, 168, 76, 0.2), 0 4px 16px rgba(201, 168, 76, 0.1);

/* Navigation bar shadow */
--shadow-nav:         0 1px 0 var(--c6-border), 0 4px 12px rgba(0, 0, 0, 0.5);

/* Inner glow for focused inputs */
--shadow-input-focus: inset 0 0 0 1px var(--c6-red), 0 0 12px var(--c6-red-glow);
```

### Spacing Scale

Use a consistent 4px base grid:
```
--space-1:  0.25rem;   /* 4px */
--space-2:  0.5rem;    /* 8px */
--space-3:  0.75rem;   /* 12px */
--space-4:  1rem;      /* 16px */
--space-6:  1.5rem;    /* 24px */
--space-8:  2rem;      /* 32px */
--space-10: 2.5rem;    /* 40px */
--space-12: 3rem;      /* 48px */
--space-16: 4rem;      /* 64px */
--space-20: 5rem;      /* 80px */
--space-24: 6rem;      /* 96px */
--space-32: 8rem;      /* 128px */
```

### Border Radius
```
--radius-sm:  4px;     /* Buttons, badges */
--radius-md:  8px;     /* Cards, inputs */
--radius-lg:  12px;    /* Modal, larger cards */
--radius-xl:  16px;    /* Feature sections */
--radius-full: 9999px; /* Pills, avatars */
```

### The Divider Element
From the current site — the signature red divider line. Use this as a recurring design motif throughout the site:
```css
.divider {
    width: 80px;
    height: 2px;
    background: var(--c6-red);
    margin: 1.5rem auto;
}

/* Expanded variant for section breaks */
.divider-wide {
    width: 120px;
    height: 2px;
    background: var(--c6-gradient-accent);
    margin: 2rem auto;
}

/* Gold variant for premium sections */
.divider-gold {
    width: 80px;
    height: 2px;
    background: var(--c6-gradient-gold);
    margin: 1.5rem auto;
}
```

---

## Anti-Generic Design Guardrails

- **Colors:** Never use default Tailwind palette (`blue-500`, `indigo-600`, etc.). Always define and use custom design tokens from the color system above (e.g. `var(--c6-red)`, `var(--c6-black)`). Avoid raw hex values in JSX — reference the design tokens.
- **Typography:** Never use a single font (`font-sans`) everywhere. Use `var(--font-display)` for headings and `var(--font-body)` for text. Apply tight tracking (`tracking-[-0.03em]` or `letter-spacing: 0.03em`) for headings and generous line-height (`leading-[1.7]` or `line-height: 1.7`) for body text. Headings should feel commanding and uppercase. Body text should feel clean and readable.
- **Shadows:** Never use default utilities like `shadow-md` or `shadow-lg`. Use the layered, color-tinted shadows defined above (`--shadow-card`, `--shadow-cta`, etc.).
- **Gradients & backgrounds:** Avoid flat fills (`bg-white`, `bg-gray-100`). The site is dark-first. Use the layered gradient system (`--c6-gradient-hero`, `--c6-gradient-section`). Add subtle radial glows (`--c6-glow-red`) for depth and ambiance. Every section should have visual depth, never a flat single-color background.
- **Animations:** Never use `transition-all`. Only animate `transform` and `opacity`. Use explicit utilities (`transition-transform`, `transition-opacity`) and controlled durations (200-400ms). Prefer spring-like motion when using animation libraries. Subtle is better than flashy — this is a cybersecurity firm, not a startup landing page.
- **Component styling:** Avoid long, unstructured className strings in JSX. Extract reusable components and variants. Use composition patterns (`clsx`, `cva`) instead of duplicating styles.
- **Interactive states:** Every interactive element must include `hover`, `focus-visible`, and `active` states. No exceptions. Hover states should use the red glow (`--c6-red-glow`) or subtle border shifts. Focus states must be accessible and visible.
- **Images:** Never use raw images without treatment. Always add overlays (e.g. gradient), blending, or color tint to integrate them into the dark design. Images should feel like they belong in the dark environment, not pasted on top.
- **Spacing & layout:** Avoid inconsistent spacing. Use the spacing scale defined above. Prefer CSS Grid for page layouts and Flexbox for component-level layouts. Maintain generous whitespace (this is a premium brand, not a cluttered dashboard).
- **Anti-patterns:** Avoid generic UI patterns like `bg-white + shadow-md + rounded-lg`, default Tailwind look, missing states, or flat, depth-less layouts. This site should never look like a Tailwind template.

---

## Design Motifs & Patterns

These recurring visual elements should appear throughout the site to maintain brand cohesion:

1. **The Red Divider Line** — Thin 2px red line (`--c6-red`) used as section separators, under headings, and as a visual rhythm element. This is the signature motif from the Coming Soon page.
2. **Subtle Grid/Scan Lines** — Very faint grid lines or scan-line texture overlaid on dark backgrounds, suggesting surveillance, monitoring, and tactical awareness. Opacity should be extremely low (0.02-0.05).
3. **Red Ambient Glow** — Soft radial gradients of cardinal red at very low opacity, used behind hero sections, key cards, or CTAs to create warmth and depth in the dark environment.
4. **Gold Accents for Premium Elements** — Use gold sparingly for testimonials, certifications, trust badges, or "premium" callouts. Gold should feel earned, not sprinkled everywhere.
5. **Geometric Cardinal Shapes** — Angular, faceted shapes inspired by the geometric cardinal bird logo. Use as background design elements, section dividers, or decorative accents.
6. **Military-Precision Alignment** — Content should feel precisely placed, with strong grid alignment, consistent gutters, and intentional negative space. Nothing should look accidental.

---

## Page Structure Guidelines

### Navigation
- Fixed top navigation, transparent over hero, solid `--c6-black-elevated` on scroll
- Logo left, nav links center or right, CTA button right
- Red accent on active/hover states
- Mobile: full-screen overlay menu with dark background

### Hero Section
- Full viewport height or near-full
- Dark layered gradient background with optional subtle particle/grid animation
- Logo mark or wordmark prominently featured
- Eyebrow text (uppercase, letter-spaced, light weight) above main heading
- Main heading in display font, large, uppercase
- Red divider below heading
- Subtext in body font, muted gray
- Primary CTA button with red gradient background and shadow

### Content Sections
- Alternate between `--c6-black` and `--c6-black-surface` backgrounds
- Each section should have its own ambient glow or gradient for depth
- Section headings centered with red divider beneath
- Card-based layouts for services, features, capabilities
- Cards: `--c6-black-elevated` background, `--c6-border` border, hover glow effect

### Footer
- Dark `--c6-black` background
- Muted text (`--c6-text-muted`)
- Red divider above footer content
- Logo, contact info, quick links
- "© 2026 Cardinal Six Cyber LLC. All rights reserved."

---

## Visual Style

When you need the company logo for the web page, use `@"C:\working\cardinalsixcyber\brand\logo.png"`

### Logo Usage Rules
- Always use the official logo file — never recreate or approximate
- Minimum clear space around logo: equal to the height of the "C" in the wordmark
- On dark backgrounds: use full-color or white version
- Never place the logo on busy backgrounds without a solid or gradient backing
- Minimum display size: 120px wide for web

---

## Content Tone

- Professional, clear, and direct. No fluff or buzzword padding.
- Confident but not arrogant. Practitioner voice, not salesman voice.
- Mirror the current Coming Soon page tone: "We're building something powerful." — understated confidence.
- Avoid clichés like "in today's ever-evolving threat landscape" or "cutting-edge solutions."
- Write like a DoD cybersecurity professional, not a marketing agency.
- Use current DoD terminology: CORA (not CCRI), ESS/Trellix (not HBSS), Helix (not BMC Remedy).

---

## Technical Notes

- Site should be fully responsive (mobile-first)
- Target performance: Lighthouse score 90+ across all categories
- Accessibility: WCAG 2.1 AA compliant minimum
- Dark theme only (no light mode toggle needed)
- Prefer static site generation (Next.js, Astro) or simple HTML/CSS/JS for initial build
- All fonts loaded via Google Fonts with `display=swap` for performance
- Lazy load images, optimize all assets
- SSL/HTTPS required (handled by Cloudflare)

## Deployment Notes

- The Docker server lives at `justin@192.168.0.240:/home/justin/deploy/cardinalsixcyber`
- Deployable site changes are not live on the server until the Docker image is rebuilt there
- Any commit, push, or pull that changes deployable inputs (`src/`, `public/`, `data/`, `nginx/`, `package*.json`, `astro.config.mjs`, `tsconfig.json`, `Dockerfile`, `compose.yaml`, `.dockerignore`) requires a Docker rebuild and container recreate on the server
- Preferred deploy path: run `scripts/deploy-docker-server.ps1` instead of ad hoc `scp`/`docker compose build` commands
- Use `-SourceDir` when deploying from a worktree so the server is rebuilt from the correct tree
