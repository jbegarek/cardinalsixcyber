# Cyber News Page — Design Spec

## Overview

Add a cybersecurity news aggregation page to the Cardinal Six Cyber website. A Python script fetches articles from 7 RSS feeds, generates a static JSON file, and a GitHub Actions cron job keeps it fresh every 2 hours. The news page renders articles client-side with a featured/list hybrid layout and source filtering.

## Components

### 1. RSS Fetcher — `scripts/fetch-news.py`

**Purpose:** Fetch, parse, and normalize cybersecurity news from RSS feeds into a single JSON file.

**Runtime:** Python 3.10+ standard library only (no pip dependencies). Uses `urllib.request` for HTTP and `xml.etree.ElementTree` for XML parsing.

**RSS Sources:**

| Source | Feed URL |
|--------|----------|
| The Hacker News | `https://feeds.feedburner.com/TheHackersNews` |
| BleepingComputer | `https://www.bleepingcomputer.com/feed/` |
| Krebs on Security | `https://krebsonsecurity.com/feed/` |
| Dark Reading | `https://www.darkreading.com/rss.xml` |
| SecurityWeek | `https://www.securityweek.com/feed/` |
| CISA Alerts | `https://www.cisa.gov/cybersecurity-advisories/all.xml` |
| The Record | `https://therecord.media/feed` |

**Behavior:**
- Sets User-Agent header `C6Cyber-NewsBot/1.0` on all HTTP requests (many feeds block Python's default UA)
- Per-request timeout of 15 seconds
- Fetches all feeds concurrently (using `concurrent.futures.ThreadPoolExecutor`)
- Handles both RSS 2.0 (`<item>`, `<description>`, `<pubDate>`) and Atom (`<entry>`, `<content>`/`<summary>`, `<updated>`) feed formats — required because CISA may serve Atom XML
- Parses each feed's XML, extracting: title, link, description/summary, publication date, source name
- Strips HTML tags from descriptions, truncates summaries to ~200 characters
- Normalizes all dates to ISO 8601 UTC
- Deduplicates by URL
- Sorts by publication date (newest first)
- Keeps the latest 50 articles
- Writes output to `data/news.json`
- Exits with code 0 on success, non-zero on failure
- Gracefully handles individual feed failures (logs warning, continues with remaining feeds)

**Output format — `data/news.json`:**
```json
{
  "last_updated": "2026-03-27T14:00:00Z",
  "articles": [
    {
      "title": "Article Title",
      "link": "https://example.com/article",
      "summary": "First ~200 characters of the article description...",
      "source": "The Hacker News",
      "published": "2026-03-27T12:00:00Z"
    }
  ]
}
```

### 2. News Page — `news.html`

**Purpose:** Display aggregated cybersecurity news articles with filtering.

**Design system:** Matches the existing C6 design system exactly — same CSS variables, typography, navigation, footer, scan lines overlay, and reveal animations as `index.html`.

**Page structure (top to bottom):**

1. **Navigation** — Identical to `index.html` with "Cyber News" added as a nav link (between "Frameworks" and "Get in Touch"). On `news.html`, nav links to homepage sections use fully qualified relative paths: `index.html#services`, `index.html#why-c6`, `index.html#frameworks`, `index.html#contact`.
2. **Scan lines overlay** — Same as index
3. **Page header** — Eyebrow "Intelligence Feed" + h1 "CYBER NEWS" + red divider + subtitle "Aggregated cybersecurity intelligence from trusted sources, updated every two hours."
4. **Filter bar** — Horizontally scrollable row of pill buttons: "All" (active by default) + one pill per source. Active pill has red background. Clicking a pill filters the article list to that source only.
5. **Article feed:**
   - **Featured article** (first/newest): Elevated card with red top-border accent, gold "Latest" badge, source pill, relative timestamp, full title, full summary (~200 chars), "Read Article" link
   - **Remaining articles**: Compact list rows with subtle bottom border. Each row: source badge, relative timestamp, title, one-line summary, external link arrow icon. Hover state: subtle red glow on left border.
6. **Last updated** — Muted timestamp showing when the feed was last refreshed
7. **Footer** — Identical to `index.html`

**Client-side behavior:**
- Fetches `data/news.json` on page load
- Renders articles into the DOM
- Filter pills toggle a CSS class or re-render the filtered list
- Shows a loading skeleton state while fetching
- Shows an error state if fetch fails ("Unable to load news feed")
- Relative timestamps calculated client-side ("2 hours ago", "yesterday", etc.)
- Reveal-on-scroll animations matching index.html

**Responsive:**
- Filter pills scroll horizontally on mobile
- Featured card stacks vertically on mobile
- Compact list rows remain full-width
- Same mobile nav overlay behavior as index.html

### 3. GitHub Actions Workflow — `.github/workflows/fetch-news.yml`

**Purpose:** Automatically refresh news data every 2 hours.

**Trigger:** `schedule: cron: '0 */2 * * *'` (every 2 hours) + `workflow_dispatch` (manual trigger)

**Steps:**
1. Checkout repo
2. Set up Python 3.12
3. Run `python scripts/fetch-news.py`
4. Check if `data/news.json` changed (`git diff --quiet`)
5. If changed: commit and push with message "chore: update cyber news feed"
6. If unchanged: skip commit

**Permissions:** `contents: write` for pushing commits.

**Timeout:** 5 minutes max for the entire workflow.

### 4. Bootstrap / Seed Data

A seed `data/news.json` must be committed to the repo so the first Docker build succeeds before the GitHub Actions workflow has ever run:

```json
{"last_updated": null, "articles": []}
```

The news page handles this gracefully by showing an empty state message.

### 5. Infrastructure Changes

**`nginx/default.conf`:**
- Add `location = /news.html` serving the news page — place **before** the catch-all `location /` block
- Add `location /data/` serving JSON files from `/usr/share/nginx/html/data/` with `Cache-Control: public, max-age=3600` (1-hour cache, data refreshes every 2 hours) — place **before** the catch-all `location /` block
- CSP header: no changes needed (same-origin JSON fetch, `connect-src 'self'` already present)

**`Dockerfile`:**
- Add `COPY news.html /usr/share/nginx/html/news.html`
- Add `COPY data/ /usr/share/nginx/html/data/`

**`index.html`:**
- Add `<li><a href="news.html">Cyber News</a></li>` to desktop nav links (between "Frameworks" and "Get in Touch")
- Add `<a href="news.html" class="mobile-link">Cyber News</a>` to mobile overlay (between "Frameworks" and "Get in Touch")

## Out of Scope

- Search/full-text filtering within articles
- Saving/bookmarking articles
- Light mode
- Server-side rendering
- Article thumbnails/images
- RSS feed configuration UI
