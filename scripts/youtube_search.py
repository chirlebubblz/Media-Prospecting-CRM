"""
YouTube Video Podcast & Channel Discovery Script (Zero API Key)
Part of the Media Discovery & Outreach Skill.
Extracts video podcasts, interviews, and channels matching compliance, risk, and finance queries.
"""

import re
import json
import urllib.parse
import urllib.request
from typing import List, Dict, Any, Optional

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def search_youtube(query: str, limit: int = 15) -> List[Dict[str, Any]]:
    """
    Searches YouTube for video podcasts and channels without needing a Google API key.
    """
    search_term = query if "podcast" in query.lower() else f"{query} podcast"
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(search_term)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"})

    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            html = response.read().decode("utf-8")
    except Exception as e:
        print(f"[!] Error fetching YouTube search for '{query}': {e}")
        return []

    match = re.search(r"ytInitialData = ({.*?});", html)
    if not match:
        match = re.search(r"var ytInitialData = ({.*?});</script>", html)

    if not match:
        return []

    try:
        data = json.loads(match.group(1))
    except Exception:
        return []

    results: List[Dict[str, Any]] = []

    try:
        sections = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"]
        for sec in sections:
            item_sec = sec.get("itemSectionRenderer", {}).get("contents", [])
            for it in item_sec:
                if len(results) >= limit:
                    break

                # 1. Video Podcast Episode
                if "videoRenderer" in it:
                    vr = it["videoRenderer"]
                    title = vr.get("title", {}).get("runs", [{}])[0].get("text", "")
                    channel = vr.get("ownerText", {}).get("runs", [{}])[0].get("text", "")
                    vid = vr.get("videoId", "")
                    desc_snippets = vr.get("detailedMetadataSnippets", [])
                    desc = ""
                    if desc_snippets:
                        desc = "".join([r.get("text", "") for r in desc_snippets[0].get("snippetText", {}).get("runs", [])])
                    published = vr.get("publishedTimeText", {}).get("simpleText", "")
                    views = vr.get("viewCountText", {}).get("simpleText", "")
                    thumb = vr.get("thumbnail", {}).get("thumbnails", [{}])[-1].get("url", "")

                    results.append({
                        "id": f"yt_{vid}",
                        "name": f"{channel}: \"{title}\"",
                        "show_name": channel,
                        "episode_title": title,
                        "content_type": "episode",
                        "host": channel,
                        "media_type": "YouTube Video Podcast",
                        "genre": "Video Podcast / Talk Show",
                        "website": f"https://www.youtube.com/watch?v={vid}",
                        "apple_url": "",
                        "feed_url": "",
                        "contact_email": "",
                        "description": desc,
                        "published_date": published,
                        "views": views,
                        "artwork_url": thumb,
                        "search_query": query,
                        "recent_episodes": [{"title": title, "date": published, "summary": desc[:250]}],
                        "status": "Researching"
                    })

                # 2. Dedicated Channel
                elif "channelRenderer" in it:
                    cr = it["channelRenderer"]
                    title = cr.get("title", {}).get("simpleText", "")
                    cid = cr.get("channelId", "")
                    desc_runs = cr.get("descriptionSnippet", {}).get("runs", [])
                    desc = "".join([r.get("text", "") for r in desc_runs])
                    video_count = cr.get("videoCountText", {}).get("runs", [{}])[0].get("text", "")
                    thumb = cr.get("thumbnail", {}).get("thumbnails", [{}])[-1].get("url", "")

                    results.append({
                        "id": f"yt_ch_{cid}",
                        "name": title,
                        "host": title,
                        "media_type": "YouTube Channel",
                        "genre": "YouTube Show",
                        "website": f"https://www.youtube.com/channel/{cid}",
                        "apple_url": "",
                        "feed_url": "",
                        "contact_email": "",
                        "description": desc,
                        "published_date": "",
                        "views": video_count,
                        "artwork_url": thumb,
                        "search_query": query,
                        "recent_episodes": [],
                        "status": "Researching"
                    })
    except Exception as e:
        print(f"[!] Parsing error on YouTube results: {e}")

    return results


if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else "corporate compliance podcast"
    res = search_youtube(q, limit=5)
    print(f"Discovered {len(res)} results for '{q}':")
    for r in res:
        print(f" - [{r['media_type']}] {r['name']} ({r['host']}) -> {r['website']}")
