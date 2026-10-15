"""
PodcastIndex.org API Client
Part of the Media Discovery & Outreach Skill.
Queries the decentralized, open PodcastIndex directory (4M+ podcasts)
using cryptographic auth headers.
"""

import os
import time
import hashlib
import json
import urllib.parse
import urllib.request
from typing import List, Dict, Any, Optional


def search_podcast_index(query: str, api_key: Optional[str] = None, api_secret: Optional[str] = None, limit: int = 15) -> List[Dict[str, Any]]:
    """
    Queries PodcastIndex.org.
    API Key and Secret can be obtained free at https://podcastindex.org/.
    """
    key = api_key or os.environ.get("PODCAST_INDEX_API_KEY")
    secret = api_secret or os.environ.get("PODCAST_INDEX_API_SECRET")

    if not key or not secret:
        print("[!] PodcastIndex API Key/Secret not provided. (Get free keys at https://podcastindex.org/)")
        return []

    epoch_time = str(int(time.time()))
    data_to_hash = key + secret + epoch_time
    sha_1 = hashlib.sha1(data_to_hash.encode("utf-8")).hexdigest()

    headers = {
        "User-Agent": "EthicsInsight-MediaSkill/1.0",
        "X-Auth-Date": epoch_time,
        "X-Auth-Key": key,
        "Authorization": sha_1,
    }

    url = f"https://api.podcastindex.org/api/1.0/search/byterm?q={urllib.parse.quote_plus(query)}&max={limit}"

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        feeds = data.get("feeds", [])
        cleaned = []
        for f in feeds:
            cleaned.append({
                "id": f"pi_{f.get('id')}",
                "name": f.get("title", "").strip(),
                "host": f.get("author", "").strip(),
                "media_type": "Audio Podcast",
                "genre": f.get("categories", {}).get("1", "Business"),
                "feed_url": f.get("url", ""),
                "website": f.get("link", ""),
                "apple_url": f"https://podcasts.apple.com/podcast/id{f.get('itunesId')}" if f.get("itunesId") else "",
                "description": f.get("description", ""),
                "artwork_url": f.get("image", ""),
                "language": f.get("language", ""),
                "episode_count": f.get("episodeCount", 0),
                "search_query": query,
                "status": "Researching"
            })
        return cleaned
    except Exception as e:
        print(f"[!] PodcastIndex API error: {e}")
        return []


if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else "risk management"
    res = search_podcast_index(q)
    print(f"Results: {len(res)}")
