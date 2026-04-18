# Cyber News Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a cybersecurity news aggregation page with automated RSS feed collection, source filtering, and a hybrid featured/list layout matching the C6 design system.

**Architecture:** Python stdlib script fetches 7 RSS feeds (RSS 2.0 + Atom), outputs `data/news.json`. Static `news.html` loads JSON client-side, renders a featured card + compact list with filter pills. GitHub Actions cron refreshes data every 2 hours.

**Tech Stack:** Python 3.10+ (stdlib only), HTML/CSS/JS (vanilla, no frameworks), GitHub Actions, nginx

**Spec:** `docs/superpowers/specs/2026-03-27-cyber-news-page-design.md`

---

### Task 1: Seed data file

**Files:**
- Create: `data/news.json`

- [ ] **Step 1: Create seed `data/news.json`**

```json
{"last_updated": null, "articles": []}
```

This empty seed ensures Docker builds and the news page work before the first real fetch.

- [ ] **Step 2: Commit**

```bash
git add data/news.json
git commit -m "chore: add seed news.json for cyber news page"
```

---

### Task 2: RSS fetcher script

**Files:**
- Create: `scripts/fetch-news.py`

- [ ] **Step 1: Create `scripts/fetch-news.py`**

The script must:
- Use only Python stdlib (`urllib.request`, `xml.etree.ElementTree`, `concurrent.futures`, `json`, `re`, `html`, `datetime`, `email.utils`)
- Set `User-Agent: C6Cyber-NewsBot/1.0` on all requests
- 15-second per-request timeout
- Fetch all 7 feeds concurrently via `ThreadPoolExecutor`
- Handle both RSS 2.0 and Atom feed formats
- Strip HTML tags from descriptions using `re.sub(r'<[^>]+>', '', text)` and `html.unescape()`
- Truncate summaries to ~200 characters at a word boundary
- Parse dates from multiple formats: RFC 822 (`pubDate` via `email.utils.parsedate_to_datetime`), ISO 8601 (`updated`/`published` in Atom)
- Normalize all dates to ISO 8601 UTC strings
- Deduplicate articles by URL
- Sort by published date (newest first)
- Keep top 50 articles
- Write to `data/news.json` atomically (write to temp file, then rename)
- Log warnings for individual feed failures, continue with remaining feeds
- Exit 0 on success (even if some feeds fail), exit 1 only if ALL feeds fail

```python
#!/usr/bin/env python3
"""Fetch cybersecurity news from RSS/Atom feeds and write data/news.json."""

import concurrent.futures
import html
import json
import logging
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

FEEDS = [
    ("The Hacker News", "https://feeds.feedburner.com/TheHackersNews"),
    ("BleepingComputer", "https://www.bleepingcomputer.com/feed/"),
    ("Krebs on Security", "https://krebsonsecurity.com/feed/"),
    ("Dark Reading", "https://www.darkreading.com/rss.xml"),
    ("SecurityWeek", "https://www.securityweek.com/feed/"),
    ("CISA Alerts", "https://www.cisa.gov/cybersecurity-advisories/all.xml"),
    ("The Record", "https://therecord.media/feed"),
]

USER_AGENT = "C6Cyber-NewsBot/1.0"
TIMEOUT = 15
MAX_ARTICLES = 50
SUMMARY_LENGTH = 200
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "news.json"

# Atom namespace
ATOM_NS = "http://www.w3.org/2005/Atom"


def strip_html(text: str) -> str:
    """Remove HTML tags and decode entities."""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def truncate(text: str, length: int = SUMMARY_LENGTH) -> str:
    """Truncate text to approximately `length` chars at a word boundary."""
    if len(text) <= length:
        return text
    truncated = text[:length]
    last_space = truncated.rfind(" ")
    if last_space > length // 2:
        truncated = truncated[:last_space]
    return truncated.rstrip(".,;:!? ") + "..."


def parse_date(date_str: str | None) -> datetime | None:
    """Parse RFC 822 or ISO 8601 date strings into UTC datetime."""
    if not date_str:
        return None
    date_str = date_str.strip()

    # Try RFC 822 (RSS pubDate)
    try:
        dt = parsedate_to_datetime(date_str)
        return dt.astimezone(timezone.utc)
    except (ValueError, TypeError):
        pass

    # Try ISO 8601 variants (Atom)
    for fmt in (
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d",
    ):
        try:
            dt = datetime.strptime(date_str, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except ValueError:
            continue

    return None


def fetch_feed(source_name: str, url: str) -> list[dict]:
    """Fetch and parse a single RSS/Atom feed. Returns list of article dicts."""
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=TIMEOUT) as resp:
            data = resp.read()
    except Exception as e:
        log.warning("Failed to fetch %s (%s): %s", source_name, url, e)
        return []

    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        log.warning("Failed to parse XML from %s: %s", source_name, e)
        return []

    articles = []

    # Try RSS 2.0: <channel><item>
    for item in root.iter("item"):
        title_el = item.find("title")
        link_el = item.find("link")
        desc_el = item.find("description")
        date_el = item.find("pubDate")

        title = title_el.text.strip() if title_el is not None and title_el.text else None
        link = link_el.text.strip() if link_el is not None and link_el.text else None
        desc = desc_el.text.strip() if desc_el is not None and desc_el.text else ""
        pub_date = parse_date(date_el.text if date_el is not None else None)

        if title and link:
            articles.append({
                "title": strip_html(title),
                "link": link,
                "summary": truncate(strip_html(desc)),
                "source": source_name,
                "published": pub_date.isoformat() if pub_date else None,
                "_sort_date": pub_date,
            })

    # Try Atom: <entry> (only if no RSS items found)
    if not articles:
        for entry in root.iter(f"{{{ATOM_NS}}}entry"):
            title_el = entry.find(f"{{{ATOM_NS}}}title")
            link_el = entry.find(f"{{{ATOM_NS}}}link")
            summary_el = entry.find(f"{{{ATOM_NS}}}summary")
            content_el = entry.find(f"{{{ATOM_NS}}}content")
            updated_el = entry.find(f"{{{ATOM_NS}}}updated")
            published_el = entry.find(f"{{{ATOM_NS}}}published")

            title = title_el.text.strip() if title_el is not None and title_el.text else None
            link = link_el.get("href", "").strip() if link_el is not None else None
            desc = ""
            if summary_el is not None and summary_el.text:
                desc = summary_el.text.strip()
            elif content_el is not None and content_el.text:
                desc = content_el.text.strip()
            date_str = None
            if published_el is not None and published_el.text:
                date_str = published_el.text
            elif updated_el is not None and updated_el.text:
                date_str = updated_el.text
            pub_date = parse_date(date_str)

            if title and link:
                articles.append({
                    "title": strip_html(title),
                    "link": link,
                    "summary": truncate(strip_html(desc)),
                    "source": source_name,
                    "published": pub_date.isoformat() if pub_date else None,
                    "_sort_date": pub_date,
                })

        # Also try Atom entries without namespace prefix
        if not articles:
            for entry in root.iter("entry"):
                title_el = entry.find("title")
                link_el = entry.find("link")
                summary_el = entry.find("summary")
                content_el = entry.find("content")
                updated_el = entry.find("updated")
                published_el = entry.find("published")

                title = title_el.text.strip() if title_el is not None and title_el.text else None
                link = link_el.get("href", "").strip() if link_el is not None else None
                desc = ""
                if summary_el is not None and summary_el.text:
                    desc = summary_el.text.strip()
                elif content_el is not None and content_el.text:
                    desc = content_el.text.strip()
                date_str = None
                if published_el is not None and published_el.text:
                    date_str = published_el.text
                elif updated_el is not None and updated_el.text:
                    date_str = updated_el.text
                pub_date = parse_date(date_str)

                if title and link:
                    articles.append({
                        "title": strip_html(title),
                        "link": link,
                        "summary": truncate(strip_html(desc)),
                        "source": source_name,
                        "published": pub_date.isoformat() if pub_date else None,
                        "_sort_date": pub_date,
                    })

    log.info("Fetched %d articles from %s", len(articles), source_name)
    return articles


def main() -> int:
    all_articles: list[dict] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
        futures = {
            executor.submit(fetch_feed, name, url): name
            for name, url in FEEDS
        }
        for future in concurrent.futures.as_completed(futures):
            source = futures[future]
            try:
                articles = future.result()
                all_articles.extend(articles)
            except Exception as e:
                log.warning("Unexpected error fetching %s: %s", source, e)

    if not all_articles:
        log.error("All feeds failed — no articles fetched")
        return 1

    # Deduplicate by link
    seen_links: set[str] = set()
    unique: list[dict] = []
    for article in all_articles:
        if article["link"] not in seen_links:
            seen_links.add(article["link"])
            unique.append(article)

    # Sort by date (newest first), articles without dates go to the end
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    unique.sort(key=lambda a: a.get("_sort_date") or epoch, reverse=True)

    # Keep top N
    unique = unique[:MAX_ARTICLES]

    # Remove internal sort key
    for article in unique:
        article.pop("_sort_date", None)

    output = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "articles": unique,
    }

    # Write atomically
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(
        dir=OUTPUT_PATH.parent, suffix=".tmp", prefix="news-"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, OUTPUT_PATH)
    except Exception:
        os.unlink(tmp_path)
        raise

    log.info(
        "Wrote %d articles to %s", len(unique), OUTPUT_PATH
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run the fetcher to verify it works and populate real data**

```bash
python scripts/fetch-news.py
```

Expected: `INFO: Wrote N articles to .../data/news.json` with N > 0. Some feeds may warn but the script should succeed.

- [ ] **Step 3: Verify `data/news.json` contains valid data**

Open `data/news.json` and confirm it has `last_updated` set and `articles` array with entries containing `title`, `link`, `summary`, `source`, `published`.

- [ ] **Step 4: Commit**

```bash
git add scripts/fetch-news.py data/news.json
git commit -m "feat: add RSS fetcher script for cyber news aggregation"
```

---

### Task 3: News page HTML/CSS/JS

**Files:**
- Create: `news.html`

This is the largest task. The page must replicate the exact design system from `index.html` — same CSS variables, typography, navigation, footer, scan lines, reveal animations. It adds news-specific styles for filter pills, featured card, and compact article rows.

**Key design references from `index.html`:**
- CSS variables: lines 12-86 (copy entire `:root` block)
- Reset & base: lines 88-113
- Utility classes (`.container`, `.eyebrow`, `.divider`, `.section-heading`): lines 115-173
- Scan lines: lines 175-188
- Navigation (`.nav`, `.nav-inner`, `.nav-links`, `.nav-cta`, `.nav-toggle`, `.nav-overlay`): lines 190-353
- Button styles (`.btn-primary`, `.btn-secondary`): lines 477-540
- Footer (`.footer` through `.footer-legal`): lines 1093-1208
- Animations (`@keyframes fade-up`, `.reveal`): lines 1210-1240
- Responsive breakpoints: 1024px, 768px, 480px (lines 1242-1385)

- [ ] **Step 1: Create `news.html`**

Build the complete page with:

**`<head>`:** Same meta, fonts, title "Cardinal Six Cyber | Cyber News"

**`<style>`:** Copy these CSS sections from `index.html`:
- All design tokens (`:root` block, lines 12-86)
- Reset & base (lines 88-113)
- Utility classes: `.container`, `.eyebrow`, `.divider`, `.divider-wide`, `.divider-gold`, `.section-heading`, `.section-sub` (lines 115-173)
- Scan lines (lines 175-188)
- Full navigation CSS: `.nav`, `.nav.scrolled`, `.nav-inner`, `.nav-logo`, `.nav-links`, `.nav-links a`, `.nav-links a::after`, `.nav-links a:hover`, `.nav-links a:hover::after`, `.nav-links a:focus-visible`, `.nav-cta`, `.nav-cta:hover`, `.nav-cta:active`, `.nav-cta:focus-visible`, `.nav-cta::after`, `.nav-toggle`, `.nav-toggle span`, `.nav-toggle.active span`, `.nav-overlay`, `.nav-overlay.open`, `.nav-overlay a`, `.nav-overlay a:hover` (lines 190-353)
- Button styles: `.btn-primary` and `.btn-secondary` with all states (lines 477-540)
- Full footer CSS (lines 1093-1208)
- Animation keyframes and `.reveal` classes (lines 1210-1240)
- Responsive rules for nav, footer at 1024px, 768px, 480px breakpoints

Then add these **new CSS sections** for the news page:

```css
/* ===== NEWS PAGE HEADER ===== */
.news-header {
    padding: calc(80px + var(--space-16)) 0 var(--space-12);
    background: var(--c6-gradient-hero);
    text-align: center;
    position: relative;
}

.news-header::before {
    content: '';
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translateX(-50%);
    width: 800px;
    height: 600px;
    background: radial-gradient(ellipse at center, rgba(192, 57, 43, 0.06) 0%, transparent 70%);
    pointer-events: none;
}

.news-title {
    font-family: var(--font-display);
    font-size: clamp(2.2rem, 4vw, 3.5rem);
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    line-height: 1.1;
    color: var(--c6-text-primary);
}

/* ===== FILTER PILLS ===== */
.filter-bar {
    padding: var(--space-6) 0;
    background: var(--c6-black);
    border-bottom: 1px solid var(--c6-border);
    position: sticky;
    top: 64px;
    z-index: 100;
}

.filter-pills {
    display: flex;
    gap: var(--space-2);
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    padding-bottom: var(--space-1);
}

.filter-pills::-webkit-scrollbar { display: none; }

.filter-pill {
    font-family: var(--font-display);
    font-size: 0.8rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--c6-text-muted);
    background: var(--c6-black-elevated);
    border: 1px solid var(--c6-border);
    padding: var(--space-2) var(--space-4);
    border-radius: var(--radius-full);
    cursor: pointer;
    white-space: nowrap;
    transition: color 0.2s ease, background 0.2s ease, border-color 0.2s ease;
}

.filter-pill:hover {
    color: var(--c6-text-secondary);
    border-color: var(--c6-border-accent);
}

.filter-pill:focus-visible {
    outline: 2px solid var(--c6-red);
    outline-offset: 2px;
}

.filter-pill.active {
    color: var(--c6-text-primary);
    background: var(--c6-red);
    border-color: var(--c6-red);
}

/* ===== ARTICLE FEED ===== */
.news-feed {
    padding: var(--space-12) 0;
    background: var(--c6-gradient-section);
    min-height: 50vh;
}

/* Featured article card */
.featured-article {
    background: var(--c6-black-elevated);
    border: 1px solid var(--c6-border);
    border-radius: var(--radius-md);
    padding: var(--space-8);
    margin-bottom: var(--space-10);
    position: relative;
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.featured-article::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--c6-gradient-accent);
}

.featured-article:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-card-hover);
}

.featured-meta {
    display: flex;
    align-items: center;
    gap: var(--space-3);
    margin-bottom: var(--space-4);
    flex-wrap: wrap;
}

.badge-latest {
    font-family: var(--font-display);
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--c6-gold);
    background: rgba(201, 168, 76, 0.12);
    padding: var(--space-1) var(--space-3);
    border-radius: var(--radius-sm);
}

.badge-source {
    font-family: var(--font-display);
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--c6-red);
    background: rgba(192, 57, 43, 0.12);
    padding: var(--space-1) var(--space-3);
    border-radius: var(--radius-sm);
}

.badge-time {
    font-family: var(--font-body);
    font-size: 0.75rem;
    color: var(--c6-text-dim);
}

.featured-title {
    font-family: var(--font-display);
    font-size: clamp(1.2rem, 2vw, 1.6rem);
    font-weight: 700;
    color: var(--c6-text-primary);
    line-height: 1.3;
    margin-bottom: var(--space-3);
}

.featured-title a {
    color: inherit;
    text-decoration: none;
    transition: color 0.2s ease;
}

.featured-title a:hover { color: var(--c6-red-bright); }

.featured-summary {
    font-family: var(--font-body);
    font-size: 0.95rem;
    color: var(--c6-text-body);
    line-height: 1.7;
    margin-bottom: var(--space-6);
}

.featured-link {
    font-family: var(--font-display);
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--c6-red);
    text-decoration: none;
    transition: color 0.2s ease;
}

.featured-link:hover { color: var(--c6-red-bright); }
.featured-link:focus-visible {
    outline: 2px solid var(--c6-red);
    outline-offset: 3px;
    border-radius: 2px;
}

/* Compact article rows */
.article-list {
    display: flex;
    flex-direction: column;
}

.article-row {
    display: flex;
    align-items: flex-start;
    gap: var(--space-4);
    padding: var(--space-6) 0;
    border-bottom: 1px solid var(--c6-border);
    position: relative;
    transition: background 0.2s ease;
}

.article-row::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2px;
    background: transparent;
    transition: background 0.2s ease;
}

.article-row:hover {
    background: rgba(192, 57, 43, 0.02);
}

.article-row:hover::before {
    background: var(--c6-red);
}

.article-row:last-child {
    border-bottom: none;
}

.article-body {
    flex: 1;
    min-width: 0;
}

.article-meta {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    margin-bottom: var(--space-1);
    flex-wrap: wrap;
}

.article-title {
    font-family: var(--font-display);
    font-size: 1rem;
    font-weight: 600;
    color: var(--c6-text-primary);
    line-height: 1.4;
    margin-bottom: var(--space-1);
}

.article-title a {
    color: inherit;
    text-decoration: none;
    transition: color 0.2s ease;
}

.article-title a:hover { color: var(--c6-red-bright); }
.article-title a:focus-visible {
    outline: 2px solid var(--c6-red);
    outline-offset: 2px;
    border-radius: 2px;
}

.article-summary {
    font-family: var(--font-body);
    font-size: 0.85rem;
    color: var(--c6-text-muted);
    line-height: 1.5;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.article-arrow {
    flex-shrink: 0;
    margin-top: var(--space-2);
    color: var(--c6-text-dim);
    transition: color 0.2s ease;
}

.article-row:hover .article-arrow {
    color: var(--c6-red);
}

/* Loading skeleton */
.skeleton {
    background: linear-gradient(90deg, var(--c6-black-elevated) 25%, var(--c6-black-surface) 50%, var(--c6-black-elevated) 75%);
    background-size: 200% 100%;
    animation: skeleton-shimmer 1.5s ease-in-out infinite;
    border-radius: var(--radius-sm);
}

@keyframes skeleton-shimmer {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

.skeleton-featured {
    height: 200px;
    margin-bottom: var(--space-10);
    border-radius: var(--radius-md);
}

.skeleton-row {
    height: 72px;
    margin-bottom: var(--space-4);
}

/* Empty / error states */
.news-empty {
    text-align: center;
    padding: var(--space-16) 0;
}

.news-empty-icon {
    width: 48px;
    height: 48px;
    stroke: var(--c6-text-dim);
    stroke-width: 1.5;
    fill: none;
    margin: 0 auto var(--space-6);
}

.news-empty h3 {
    font-family: var(--font-display);
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--c6-text-secondary);
    margin-bottom: var(--space-2);
}

.news-empty p {
    font-size: 0.9rem;
    color: var(--c6-text-muted);
}

/* Last updated footer */
.news-updated {
    text-align: center;
    padding: var(--space-8) 0 0;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    color: var(--c6-text-dim);
    letter-spacing: 0.05em;
}
```

**Navigation HTML** (note `index.html#` prefixed hrefs):
```html
<nav class="nav scrolled" role="navigation" aria-label="Primary navigation">
    <div class="container nav-inner">
        <a href="index.html" aria-label="Cardinal Six Cyber — Home">
            <img src="brand/logo.png" alt="Cardinal Six Cyber" class="nav-logo">
        </a>
        <ul class="nav-links">
            <li><a href="index.html#services">Services</a></li>
            <li><a href="index.html#why-c6">Why C6</a></li>
            <li><a href="index.html#frameworks">Frameworks</a></li>
            <li><a href="news.html" style="color: var(--c6-text-primary);">Cyber News</a></li>
            <li><a href="index.html#contact" class="nav-cta">Get in Touch</a></li>
        </ul>
        <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
            <span></span><span></span><span></span>
        </button>
    </div>
</nav>
```

The nav on the news page should always have the `scrolled` class (solid background) since there is no full-height hero.

**Page header HTML:**
```html
<section class="news-header">
    <div class="container">
        <span class="eyebrow reveal">Intelligence Feed</span>
        <h1 class="news-title reveal reveal-delay-1">Cyber News</h1>
        <div class="divider reveal reveal-delay-2"></div>
        <p class="section-sub reveal reveal-delay-2">
            Aggregated cybersecurity intelligence from trusted sources, updated every two hours.
        </p>
    </div>
</section>
```

**Filter bar HTML:**
```html
<div class="filter-bar">
    <div class="container">
        <div class="filter-pills" id="filterPills" role="tablist" aria-label="Filter by source">
            <!-- Pills injected by JS -->
        </div>
    </div>
</div>
```

**News feed HTML (container for JS-rendered content):**
```html
<section class="news-feed">
    <div class="container">
        <div id="newsFeed">
            <!-- Loading skeleton shown initially -->
            <div class="skeleton skeleton-featured"></div>
            <div class="skeleton skeleton-row"></div>
            <div class="skeleton skeleton-row"></div>
            <div class="skeleton skeleton-row"></div>
            <div class="skeleton skeleton-row"></div>
            <div class="skeleton skeleton-row"></div>
        </div>
        <div class="news-updated" id="newsUpdated"></div>
    </div>
</section>
```

**Footer HTML:** Copy the exact footer from `index.html` (lines 1723-1773), updating href anchors to `index.html#services`, `index.html#why-c6`, etc. Add a "Cyber News" link in the Company footer column.

**Mobile overlay HTML:**
```html
<div class="nav-overlay" id="navOverlay" role="dialog" aria-label="Mobile navigation">
    <a href="index.html#services" class="mobile-link">Services</a>
    <a href="index.html#why-c6" class="mobile-link">Why C6</a>
    <a href="index.html#frameworks" class="mobile-link">Frameworks</a>
    <a href="news.html" class="mobile-link">Cyber News</a>
    <a href="index.html#contact" class="mobile-link">Get in Touch</a>
</div>
```

**JavaScript:** Include all three JS blocks from `index.html` (nav scroll — but simplified since nav is always `scrolled`, mobile toggle, reveal observer). Then add the news-specific JS:

```javascript
/* News feed loader */
(function() {
    var SOURCES = [
        'The Hacker News', 'BleepingComputer', 'Krebs on Security',
        'Dark Reading', 'SecurityWeek', 'CISA Alerts', 'The Record'
    ];
    var allArticles = [];
    var activeFilter = 'all';

    function timeAgo(dateStr) {
        if (!dateStr) return '';
        var now = new Date();
        var date = new Date(dateStr);
        var seconds = Math.floor((now - date) / 1000);
        if (seconds < 60) return 'just now';
        var minutes = Math.floor(seconds / 60);
        if (minutes < 60) return minutes + 'm ago';
        var hours = Math.floor(minutes / 60);
        if (hours < 24) return hours + 'h ago';
        var days = Math.floor(hours / 24);
        if (days === 1) return 'yesterday';
        if (days < 30) return days + 'd ago';
        return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    }

    function escapeHtml(str) {
        var div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    }

    function renderPills() {
        var container = document.getElementById('filterPills');
        var html = '<button class="filter-pill active" data-source="all" role="tab" aria-selected="true">All</button>';
        SOURCES.forEach(function(source) {
            html += '<button class="filter-pill" data-source="' + escapeHtml(source) +
                '" role="tab" aria-selected="false">' + escapeHtml(source) + '</button>';
        });
        container.innerHTML = html;

        container.addEventListener('click', function(e) {
            var pill = e.target.closest('.filter-pill');
            if (!pill) return;
            activeFilter = pill.dataset.source;
            container.querySelectorAll('.filter-pill').forEach(function(p) {
                var isActive = p.dataset.source === activeFilter;
                p.classList.toggle('active', isActive);
                p.setAttribute('aria-selected', isActive);
            });
            renderArticles();
        });
    }

    function renderArticles() {
        var feed = document.getElementById('newsFeed');
        var filtered = activeFilter === 'all'
            ? allArticles
            : allArticles.filter(function(a) { return a.source === activeFilter; });

        if (filtered.length === 0) {
            feed.innerHTML =
                '<div class="news-empty">' +
                    '<svg class="news-empty-icon" viewBox="0 0 24 24"><path d="M13 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V9z"/><polyline points="13 2 13 9 20 9"/></svg>' +
                    '<h3>No articles found</h3>' +
                    '<p>' + (activeFilter === 'all' ? 'News feed is updating. Check back shortly.' : 'No recent articles from this source.') + '</p>' +
                '</div>';
            return;
        }

        var html = '';
        var featured = filtered[0];

        // Featured card
        html += '<a href="' + escapeHtml(featured.link) + '" target="_blank" rel="noopener noreferrer" class="featured-article" style="display:block;text-decoration:none;">';
        html += '<div class="featured-meta">';
        html += '<span class="badge-latest">Latest</span>';
        html += '<span class="badge-source">' + escapeHtml(featured.source) + '</span>';
        html += '<span class="badge-time">' + timeAgo(featured.published) + '</span>';
        html += '</div>';
        html += '<h2 class="featured-title">' + escapeHtml(featured.title) + '</h2>';
        html += '<p class="featured-summary">' + escapeHtml(featured.summary) + '</p>';
        html += '<span class="featured-link">Read Article &rarr;</span>';
        html += '</a>';

        // Compact rows
        html += '<div class="article-list">';
        for (var i = 1; i < filtered.length; i++) {
            var a = filtered[i];
            html += '<div class="article-row">';
            html += '<div class="article-body">';
            html += '<div class="article-meta">';
            html += '<span class="badge-source">' + escapeHtml(a.source) + '</span>';
            html += '<span class="badge-time">' + timeAgo(a.published) + '</span>';
            html += '</div>';
            html += '<h3 class="article-title"><a href="' + escapeHtml(a.link) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(a.title) + '</a></h3>';
            if (a.summary) {
                html += '<p class="article-summary">' + escapeHtml(a.summary) + '</p>';
            }
            html += '</div>';
            html += '<svg class="article-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M17 7H7M17 7v10"/></svg>';
            html += '</div>';
        }
        html += '</div>';

        feed.innerHTML = html;
    }

    function showError() {
        document.getElementById('newsFeed').innerHTML =
            '<div class="news-empty">' +
                '<svg class="news-empty-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>' +
                '<h3>Unable to load news feed</h3>' +
                '<p>Please try again later.</p>' +
            '</div>';
    }

    renderPills();

    fetch('data/news.json')
        .then(function(res) {
            if (!res.ok) throw new Error('HTTP ' + res.status);
            return res.json();
        })
        .then(function(data) {
            allArticles = data.articles || [];
            renderArticles();
            if (data.last_updated) {
                var updated = new Date(data.last_updated);
                document.getElementById('newsUpdated').textContent =
                    'Last updated: ' + updated.toLocaleString('en-US', {
                        month: 'short', day: 'numeric', year: 'numeric',
                        hour: '2-digit', minute: '2-digit', timeZoneName: 'short'
                    });
            }
        })
        .catch(showError);
})();
```

- [ ] **Step 2: Open `news.html` in a browser and verify**

Check:
- Nav renders with solid background, "Cyber News" link is highlighted
- Page header shows with eyebrow, title, divider, subtitle
- Filter pills appear (All + 7 sources)
- Featured article card renders with gold "Latest" badge, red top border, full summary
- Remaining articles render as compact rows with source badges and timestamps
- Clicking a filter pill filters the list
- Clicking "All" shows everything again
- Article links open in new tabs
- Hover states work (red left border on rows, card lift on featured)
- Mobile responsive: pills scroll, nav shows hamburger at 768px
- Footer renders correctly with links pointing to `index.html#...`

- [ ] **Step 3: Commit**

```bash
git add news.html
git commit -m "feat: add cyber news page with hybrid layout and source filtering"
```

---

### Task 4: Update `index.html` navigation

**Files:**
- Modify: `index.html:1399-1403` (desktop nav)
- Modify: `index.html:1411-1417` (mobile overlay)

- [ ] **Step 1: Add "Cyber News" to desktop nav**

In `index.html`, find the nav links `<ul>` and add the Cyber News link between Frameworks and Get in Touch:

```html
<!-- Before: -->
<li><a href="#frameworks">Frameworks</a></li>
<li><a href="#contact" class="nav-cta">Get in Touch</a></li>

<!-- After: -->
<li><a href="#frameworks">Frameworks</a></li>
<li><a href="news.html">Cyber News</a></li>
<li><a href="#contact" class="nav-cta">Get in Touch</a></li>
```

- [ ] **Step 2: Add "Cyber News" to mobile overlay**

Find the mobile overlay `<div>` and add the link:

```html
<!-- Before: -->
<a href="#frameworks" class="mobile-link">Frameworks</a>
<a href="#contact" class="mobile-link">Get in Touch</a>

<!-- After: -->
<a href="#frameworks" class="mobile-link">Frameworks</a>
<a href="news.html" class="mobile-link">Cyber News</a>
<a href="#contact" class="mobile-link">Get in Touch</a>
```

- [ ] **Step 3: Verify index.html nav still works**

Open `index.html` in browser, confirm "Cyber News" link appears and navigates to `news.html`.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add Cyber News link to site navigation"
```

---

### Task 5: Update nginx config

**Files:**
- Modify: `nginx/default.conf`

- [ ] **Step 1: Add location blocks for news page and data**

Add these two location blocks **before** the catch-all `location / { return 404; }` block:

```nginx
location = /news.html {
    try_files /news.html =404;
}

location /data/ {
    add_header Cache-Control "public, max-age=3600" always;
    try_files $uri =404;
}
```

The final config should have locations in this order:
1. `location = /healthz`
2. `location = /`
3. `location = /news.html`
4. `location /brand/`
5. `location /data/`
6. `location /` (catch-all 404)

- [ ] **Step 2: Commit**

```bash
git add nginx/default.conf
git commit -m "feat: add nginx routes for news page and data endpoint"
```

---

### Task 6: Update Dockerfile

**Files:**
- Modify: `Dockerfile`

- [ ] **Step 1: Add COPY directives for news.html and data/**

Add after the existing `COPY brand/` line:

```dockerfile
COPY news.html /usr/share/nginx/html/news.html
COPY data/ /usr/share/nginx/html/data/
```

- [ ] **Step 2: Verify Docker build succeeds**

```bash
docker build -t c6cyber-test .
```

Expected: Build completes without errors.

- [ ] **Step 3: Commit**

```bash
git add Dockerfile
git commit -m "feat: include news page and data in Docker image"
```

---

### Task 7: GitHub Actions workflow

**Files:**
- Create: `.github/workflows/fetch-news.yml`

- [ ] **Step 1: Create the workflow file**

```yaml
name: Fetch Cyber News

on:
  schedule:
    - cron: '0 */2 * * *'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  fetch-news:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Fetch news feeds
        run: python scripts/fetch-news.py

      - name: Commit if changed
        run: |
          git diff --quiet data/news.json && exit 0
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/news.json
          git commit -m "chore: update cyber news feed"
          git push
```

- [ ] **Step 2: Create `.github/workflows/` directory**

```bash
mkdir -p .github/workflows
```

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/fetch-news.yml
git commit -m "ci: add GitHub Actions workflow for automated news feed updates"
```

---

### Task 8: End-to-end verification

- [ ] **Step 1: Run the fetch script to ensure data is fresh**

```bash
python scripts/fetch-news.py
```

- [ ] **Step 2: Build and run the Docker container**

```bash
docker build -t c6cyber-test . && docker run --rm -p 8080:80 c6cyber-test
```

- [ ] **Step 3: Verify in browser**

Open `http://localhost:8080` and check:
- Homepage loads, "Cyber News" link visible in nav
- Click "Cyber News" — news page loads at `/news.html`
- Articles display with featured card and list rows
- Filter pills work
- All external links open correctly
- Mobile responsive at 768px and 480px breakpoints
- Return to homepage via nav links works

- [ ] **Step 4: Stop container and clean up**

```bash
docker stop $(docker ps -q --filter ancestor=c6cyber-test)
```
