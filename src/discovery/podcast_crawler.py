"""
Podcast Crawler module.
Queries public podcast directories (Apple Podcasts / iTunes Search API)
to discover podcasts matching executive, leadership, strategy, and business keywords.
"""

import json
import urllib.parse
import urllib.request
from typing import List, Dict, Any, Optional

DEFAULT_PRESET_QUERIES = [
    "leadership",
    "business strategy",
    "operations",
    "private equity",
    "venture capital",
    "corporate governance",
    "technology",
    "investing",
]

USER_AGENT = "MediaOutreach-CRM/1.0"


def search_podcasts(query: str, limit: int = 25) -> List[Dict[str, Any]]:
    """
    Searches the Apple Podcasts directory via the iTunes Search API.
    Does not require an API key.
    """
    base_url = "https://itunes.apple.com/search"
    params = {
        "term": query,
        "media": "podcast",
        "limit": limit,
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
            results = data.get("results", [])
            
            cleaned = []
            for r in results:
                feed_url = r.get("feedUrl")
                # Filter out shows without RSS feeds
                if not feed_url:
                    continue

                cleaned.append({
                    "id": str(r.get("collectionId", "")),
                    "name": r.get("collectionName", "").strip(),
                    "host": r.get("artistName", "").strip(),
                    "feed_url": feed_url.strip(),
                    "apple_url": r.get("collectionViewUrl", ""),
                    "genre": r.get("primaryGenreName", ""),
                    "genres": r.get("genres", []),
                    "track_count": r.get("trackCount", 0),
                    "artwork_url": r.get("artworkUrl600", r.get("artworkUrl100", "")),
                    "search_query": query,
                })
            return cleaned
    except Exception as e:
        print(f"[!] Error searching iTunes API for '{query}': {e}")
        return []


def search_preset_categories(limit_per_query: int = 15) -> List[Dict[str, Any]]:
    """
    Searches across all preset industry queries and deduplicates results by feed URL.
    """
    aggregated: Dict[str, Dict[str, Any]] = {}

    for query in DEFAULT_PRESET_QUERIES:
        print(f"[*] Searching directory for: '{query}'...")
        shows = search_podcasts(query, limit=limit_per_query)
        for show in shows:
            feed = show["feed_url"]
            if feed not in aggregated:
                aggregated[feed] = show
            else:
                # Merge query tag
                existing_queries = aggregated[feed]["search_query"].split(", ")
                if query not in existing_queries:
                    aggregated[feed]["search_query"] += f", {query}"

    print(f"[+] Found {len(aggregated)} unique shows across {len(DEFAULT_PRESET_QUERIES)} keywords.")
    return list(aggregated.values())
