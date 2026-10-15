from src.discovery.podcast_crawler import search_podcasts
from src.discovery.rss_extractor import enrich_from_rss

shows_to_check = [
    "The Operations Room a podcast for COOs",
    "Secret Leaders",
    "The Modern COO",
    "Riding Unicorns",
    "Scale Up Valley podcast",
    "The Private Equity Podcast",
    "Founder Focus",
    "Operational Excellence Show"
]

found = []
for q in shows_to_check:
    res = search_podcasts(q, limit=1)
    if res:
        s = res[0]
        enriched = enrich_from_rss(s["feed_url"])
        s.update(enriched)
        found.append(s)

print(f"Verified {len(found)} top-tier targets:")
for s in found:
    ep = s.get("recent_episodes", [{}])[0].get("title", "N/A") if s.get("recent_episodes") else "N/A"
    print(f"TITLE: {s['name']}")
    print(f"HOST: {s['host']}")
    print(f"WEBSITE: {s.get('website')}")
    print(f"FEED: {s.get('feed_url')}")
    print(f"RECENT EPISODE: {ep}")
    print("-" * 50)
