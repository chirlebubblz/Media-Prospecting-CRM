import sys
from src.discovery.podcast_crawler import search_podcasts
from src.discovery.rss_extractor import enrich_from_rss

queries = [
    "productivity operations business",
    "uk founders podcast",
    "private equity diligence podcast",
    "business leader scaling podcast"
]

results = []
for q in queries:
    shows = search_podcasts(q, limit=5)
    for s in shows:
        feed = s["feed_url"]
        enriched = enrich_from_rss(feed)
        s.update(enriched)
        results.append(s)

print(f"Total found: {len(results)}")
for r in results[:10]:
    print(f"TITLE: {r['name']}")
    print(f"HOST: {r['host']}")
    print(f"EMAIL: {r.get('contact_email')}")
    print(f"WEBSITE: {r.get('website')}")
    print(f"EPISODES: {r.get('track_count')}")
    print(f"RECENT EP: {r.get('recent_episodes', [{}])[0].get('title', 'N/A') if r.get('recent_episodes') else 'N/A'}")
    print("-" * 60)
