"""
Listen Notes API Client
Part of the Media Discovery & Outreach Skill.
Queries the Listen Notes database (3M+ podcasts & episode transcripts)
and retrieves Listen Score popularity rankings.
"""

import os
import json
import urllib.parse
import urllib.request
from typing import List, Dict, Any, Optional


def search_listen_notes(query: str, api_key: Optional[str] = None, limit: int = 15) -> List[Dict[str, Any]]:
    """
    Queries the Listen Notes API.
    Free API keys available at https://www.listennotes.com/api/
    """
    key = api_key or os.environ.get("LISTEN_NOTES_API_KEY")

    if not key:
        print("[!] Listen Notes API key not provided. (Get free key at https://www.listennotes.com/api/)")
        return []

    url = f"https://listen-api.listennotes.com/api/v2/search?q={urllib.parse.quote_plus(query)}&type=podcast&page_size={limit}"
    req = urllib.request.Request(url, headers={"X-ListenAPI-Key": key, "User-Agent": "EthicsInsight-MediaSkill/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        results = data.get("results", [])
        cleaned = []
        for r in results:
            cleaned.append({
                "id": f"ln_{r.get('id')}",
                "name": r.get("title_original", "").strip(),
                "host": r.get("publisher_original", "").strip(),
                "media_type": "Audio Podcast",
                "genre": "Business & Finance",
                "listen_score": r.get("listen_score", "N/A"),
                "listen_score_global_rank": r.get("listen_score_global_rank", "N/A"),
                "feed_url": r.get("rss", ""),
                "website": r.get("website", ""),
                "apple_url": r.get("itunes_id", ""),
                "description": r.get("description_original", ""),
                "artwork_url": r.get("image", ""),
                "total_episodes": r.get("total_episodes", 0),
                "search_query": query,
                "status": "Researching"
            })
        return cleaned
    except Exception as e:
        print(f"[!] Listen Notes API error: {e}")
        return []


if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else "compliance"
    res = search_listen_notes(q)
    print(f"Results: {len(res)}")
