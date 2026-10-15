"""
RSS Feed Extractor module for Ethics Insight.
Inspects podcast RSS XML feeds to extract host contact emails,
show websites, social media links, description summaries, and recent episode topics.
"""

import re
import urllib.request
import xml.etree.ElementTree as ET
from typing import Dict, Any, List, Optional

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

LINKEDIN_REGEX = re.compile(r"https?://(?:www\.)?linkedin\.com/(?:in|company)/[a-zA-Z0-9_-]+/?")
TWITTER_REGEX = re.compile(r"https?://(?:www\.)?(?:twitter\.com|x\.com)/[a-zA-Z0-9_]+/?")
YOUTUBE_REGEX = re.compile(r"https?://(?:www\.)?youtube\.com/(?:c/|channel/|user/|@)[a-zA-Z0-9_-]+/?")
SPOTIFY_REGEX = re.compile(r"https?://open\.spotify\.com/show/[a-zA-Z0-9]+/?")

EXCLUDED_EMAIL_DOMAINS = [
    "buzzsprout.com",
    "libsyn.com",
    "podbean.com",
    "megaphone.fm",
    "transistor.fm",
    "anchor.fm",
    "spotify.com",
    "apple.com",
    "rss.com",
    "simplecast.com",
]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def _clean_text(text: Optional[str]) -> str:
    if not text:
        return ""
    cleaned = re.sub(r"<[^>]+>", "", text)
    return " ".join(cleaned.split()).strip()


def extract_emails_from_text(text: str) -> List[str]:
    found = EMAIL_REGEX.findall(text)
    valid_emails = []
    for email in found:
        email = email.strip().lower()
        if email.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
            continue
        domain = email.split("@")[-1]
        if any(exc in domain for exc in EXCLUDED_EMAIL_DOMAINS):
            continue
        if email not in valid_emails:
            valid_emails.append(email)
    return valid_emails


def enrich_from_rss(feed_url: str, timeout: int = 4) -> Dict[str, Any]:
    info: Dict[str, Any] = {
        "website": "",
        "contact_email": "",
        "all_emails": [],
        "description": "",
        "recent_episodes": [],
        "author_name": "",
        "producer": "",
        "linkedin_url": "",
        "twitter_url": "",
        "youtube_url": "",
        "spotify_url": "",
    }

    try:
        req = urllib.request.Request(
            feed_url,
            headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/xml, text/xml"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            content = response.read()

        root = ET.fromstring(content)
        channel = root.find("channel")
        if channel is None:
            return info

        # 1. Website Link
        link_elem = channel.find("link")
        if link_elem is not None and link_elem.text:
            info["website"] = link_elem.text.strip()

        # 2. Description
        desc_elem = channel.find("description")
        full_text_corpus = ""
        if desc_elem is not None and desc_elem.text:
            info["description"] = _clean_text(desc_elem.text)
            full_text_corpus += " " + desc_elem.text

        # 3. Author / Owner Names
        itunes_ns = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"
        author_elem = channel.find(f"{itunes_ns}author")
        if author_elem is not None and author_elem.text:
            info["author_name"] = author_elem.text.strip()

        owner_elem = channel.find(f"{itunes_ns}owner")
        discovered_emails = []

        if owner_elem is not None:
            owner_name = owner_elem.find(f"{itunes_ns}name")
            if owner_name is not None and owner_name.text:
                info["producer"] = owner_name.text.strip()
                if not info["author_name"]:
                    info["author_name"] = owner_name.text.strip()

            owner_email = owner_elem.find(f"{itunes_ns}email")
            if owner_email is not None and owner_email.text:
                discovered_emails.append(owner_email.text.strip().lower())

        managing_editor = channel.find("managingEditor")
        if managing_editor is not None and managing_editor.text:
            discovered_emails.extend(extract_emails_from_text(managing_editor.text))
            full_text_corpus += " " + managing_editor.text

        # 4. Recent Episodes (Top 3 items)
        items = channel.findall("item")
        for item in items[:3]:
            ep_title = _clean_text(item.findtext("title", ""))
            ep_date = _clean_text(item.findtext("pubDate", ""))
            ep_desc = _clean_text(item.findtext("description", ""))
            
            full_text_corpus += " " + ep_desc
            discovered_emails.extend(extract_emails_from_text(ep_desc))

            info["recent_episodes"].append({
                "title": ep_title,
                "date": ep_date,
                "summary": ep_desc[:250] + "..." if len(ep_desc) > 250 else ep_desc,
            })

        # 5. Extract Social Media Links
        linkedin_match = LINKEDIN_REGEX.search(full_text_corpus)
        if linkedin_match:
            info["linkedin_url"] = linkedin_match.group(0).rstrip("/")

        twitter_match = TWITTER_REGEX.search(full_text_corpus)
        if twitter_match:
            info["twitter_url"] = twitter_match.group(0).rstrip("/")

        youtube_match = YOUTUBE_REGEX.search(full_text_corpus)
        if youtube_match:
            info["youtube_url"] = youtube_match.group(0).rstrip("/")

        spotify_match = SPOTIFY_REGEX.search(full_text_corpus)
        if spotify_match:
            info["spotify_url"] = spotify_match.group(0).rstrip("/")

        # Deduplicate emails
        unique_emails = list(dict.fromkeys(discovered_emails))
        info["all_emails"] = unique_emails
        if unique_emails:
            info["contact_email"] = unique_emails[0]

    except Exception as e:
        info["error"] = str(e)

    return info
