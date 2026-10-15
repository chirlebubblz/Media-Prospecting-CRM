"""
Deep Website & Masthead Contact Scraper
Part of the Media Discovery & Outreach Skill.
Crawls a podcast or publication website to discover contact emails,
host profiles, and editorial submission forms.
"""

import re
import urllib.parse
from typing import List, Dict, Any, Set
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

EMAIL_REGEX = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,10}\b")

EXCLUDED_DOMAINS = [
    "sentry.io",
    "wixpress.com",
    "wordpress.org",
    "cloudflare.com",
    "google.com",
    "example.com",
    "schema.org",
    "apple.com",
    "spotify.com",
    "buzzsprout.com",
    "libsyn.com",
    "w3.org",
    "github.com",
    "doubleclick.net",
    "googletagmanager.com",
]

EXCLUDED_KEYWORDS = [
    "gsap",
    "alpine",
    "swiper",
    "jquery",
    "vue",
    "react",
    "bootstrap",
    "font",
    "wght",
    "core-js",
    "node_modules",
    "cdn",
    "jsdelivr",
    "unpkg",
    "cdnjs",
    "webpack",
    "npm",
    "polyfill",
    "babel",
    "bundle",
    "min.js",
]

CONTACT_LINK_KEYWORDS = [
    "contact",
    "about",
    "team",
    "editorial",
    "masthead",
    "write-for-us",
    "contribute",
    "guest",
    "press",
    "staff",
    "pitch",
]


def extract_emails_from_html(html: str) -> List[str]:
    """Finds all clean email addresses in raw HTML or text with strict validation."""
    found = EMAIL_REGEX.findall(html)
    valid: List[str] = []
    for email in found:
        email = email.strip().lower()
        if any(email.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".js", ".css", ".woff", ".woff2", ".ttf"]):
            continue
        if any(bad in email for bad in EXCLUDED_KEYWORDS):
            continue
        if ".." in email or len(email) < 6:
            continue

        parts = email.split("@")
        if len(parts) != 2:
            continue
        user_part, domain_part = parts

        # Domain must have at least one dot, and TLD must be purely alphabetical
        domain_labels = domain_part.split(".")
        if len(domain_labels) < 2:
            continue
        tld = domain_labels[-1]
        if not tld.isalpha() or len(tld) < 2 or len(tld) > 10:
            continue
        # Check if domain label starts with or is purely digits (e.g. 3.15)
        if domain_labels[0].isdigit():
            continue

        if any(exc in domain_part for exc in EXCLUDED_DOMAINS):
            continue

        if email not in valid:
            valid.append(email)
    return valid


def scrape_site_contacts(base_url: str, max_subpages: int = 3, timeout: int = 8) -> Dict[str, Any]:
    """
    Crawls a target website and looks for contact information across key pages,
    including separate host LinkedIn, company LinkedIn, Facebook, Instagram, Twitter/X, and emails.
    """
    if not base_url or not base_url.startswith("http"):
        return {
            "primary_email": "",
            "all_emails": [],
            "contact_form_url": "",
            "host_linkedin": "",
            "company_linkedin": "",
            "twitter_url": "",
            "youtube_url": "",
            "facebook_url": "",
            "instagram_url": "",
        }

    parsed_base = urllib.parse.urlparse(base_url)
    root_domain = parsed_base.netloc.lower()

    discovered_emails: Set[str] = set()
    discovered_host_li: str = ""
    discovered_comp_li: str = ""
    discovered_twitter: str = ""
    discovered_youtube: str = ""
    discovered_facebook: str = ""
    discovered_instagram: str = ""
    contact_form_url = ""
    visited_urls: Set[str] = set()
    pages_to_crawl = [base_url]

    def inspect_links_for_socials(soup: BeautifulSoup):
        nonlocal discovered_host_li, discovered_comp_li, discovered_twitter, discovered_youtube, discovered_facebook, discovered_instagram, contact_form_url
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            if href.startswith("mailto:"):
                clean_mail = href.replace("mailto:", "").split("?")[0].strip().lower()
                clean_list = extract_emails_from_html(clean_mail)
                if clean_list:
                    discovered_emails.add(clean_list[0])
                continue

            h_lower = href.lower()
            # Personal LinkedIn
            if "linkedin.com/in/" in h_lower and not discovered_host_li:
                discovered_host_li = href
            # Company LinkedIn
            elif ("linkedin.com/company/" in h_lower or "linkedin.com/school/" in h_lower) and not discovered_comp_li:
                discovered_comp_li = href
            # Twitter / X
            elif ("twitter.com/" in h_lower or "x.com/" in h_lower) and not discovered_twitter:
                if not any(bad in h_lower for bad in ["intent", "share", "widgets", "hashtag"]):
                    discovered_twitter = href
            # YouTube
            elif ("youtube.com/@" in h_lower or "youtube.com/c/" in h_lower or "youtube.com/channel/" in h_lower or "youtube.com/user/" in h_lower) and not discovered_youtube:
                discovered_youtube = href
            # Facebook
            elif ("facebook.com/" in h_lower) and not discovered_facebook:
                if not any(bad in h_lower for bad in ["sharer", "share.php", "dialog", "policies", "help", "tr?"]):
                    discovered_facebook = href
            # Instagram
            elif ("instagram.com/" in h_lower) and not discovered_instagram:
                if not any(bad in h_lower for bad in ["/p/", "/reel/", "/stories/", "/explore/", "/legal/"]):
                    discovered_instagram = href

    # Fetch Homepage first
    try:
        resp = requests.get(base_url, headers=HEADERS, timeout=timeout)
        if resp.status_code == 200:
            content = resp.text
            visited_urls.add(base_url)
            discovered_emails.update(extract_emails_from_html(content))

            soup = BeautifulSoup(content, "html.parser")
            inspect_links_for_socials(soup)

            for a in soup.find_all("a", href=True):
                href = a["href"].strip()
                if href.startswith("mailto:"):
                    continue

                full_url = urllib.parse.urljoin(base_url, href)
                parsed_sub = urllib.parse.urlparse(full_url)

                if parsed_sub.netloc.lower() == root_domain:
                    path_lower = parsed_sub.path.lower()
                    if any(kw in path_lower for kw in CONTACT_LINK_KEYWORDS):
                        if "contact" in path_lower and not contact_form_url:
                            contact_form_url = full_url
                        if full_url not in pages_to_crawl and full_url not in visited_urls:
                            pages_to_crawl.append(full_url)
    except Exception:
        pass

    # Crawl discovered contact subpages
    for sub_url in pages_to_crawl[1 : 1 + max_subpages]:
        if sub_url in visited_urls:
            continue
        try:
            resp = requests.get(sub_url, headers=HEADERS, timeout=timeout)
            if resp.status_code == 200:
                sub_content = resp.text
                visited_urls.add(sub_url)
                discovered_emails.update(extract_emails_from_html(sub_content))

                sub_soup = BeautifulSoup(sub_content, "html.parser")
                inspect_links_for_socials(sub_soup)
        except Exception:
            continue

    clean_email_list = [e for e in discovered_emails if not any(bad in e for bad in EXCLUDED_KEYWORDS)]
    primary = clean_email_list[0] if clean_email_list else ""

    return {
        "primary_email": primary,
        "all_emails": clean_email_list,
        "contact_form_url": contact_form_url,
        "host_linkedin": discovered_host_li,
        "company_linkedin": discovered_comp_li,
        "linkedin_url": discovered_host_li or discovered_comp_li,
        "twitter_url": discovered_twitter,
        "youtube_url": discovered_youtube,
        "facebook_url": discovered_facebook,
        "instagram_url": discovered_instagram,
    }


if __name__ == "__main__":
    import sys
    test_url = sys.argv[1] if len(sys.argv) > 1 else "https://compliancepodcastnetwork.net/"
    print(f"Scraping contact info from: {test_url}")
    res = scrape_site_contacts(test_url)
    print("Result:", res)
