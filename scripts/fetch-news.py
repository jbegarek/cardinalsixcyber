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
    ("NVD", "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml"),
    ("CVE Feed", "https://cvefeed.io/rssfeed/severity/high.xml"),
    ("CVE Newsroom", "https://cvefeed.io/rssfeed/newsroom.xml"),
]

USER_AGENT = "C6Cyber-NewsBot/1.0"
TIMEOUT = 15
MAX_ARTICLES = 200
SUMMARY_LENGTH = 200
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "news.json"

# Atom namespace
ATOM_NS = "http://www.w3.org/2005/Atom"
# RSS 1.0 (RDF) namespaces
RSS1_NS = "http://purl.org/rss/1.0/"
DC_NS = "http://purl.org/dc/elements/1.1/"


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

    # Try RSS 1.0 (RDF) — used by NVD
    if not articles:
        for item in root.iter(f"{{{RSS1_NS}}}item"):
            title_el = item.find(f"{{{RSS1_NS}}}title")
            link_el = item.find(f"{{{RSS1_NS}}}link")
            desc_el = item.find(f"{{{RSS1_NS}}}description")
            date_el = item.find(f"{{{DC_NS}}}date")

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
