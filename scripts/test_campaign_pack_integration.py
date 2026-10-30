import os
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

env_file = os.path.join(base_dir, ".env")
if os.path.exists(env_file):
    with open(env_file, "r") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                os.environ["GEMINI_API_KEY"] = line.split("=", 1)[1].strip()

from src.content.engine import ResearchSynthesizer
from app import app, load_local_content

print("[1] Testing ResearchSynthesizer fallback generation...")
synth_offline = ResearchSynthesizer(api_key="invalid_or_none")
fallback_pack = synth_offline.generate_content(
    raw_text="The 4:45 PM shipping failure in Singapore and Houston caused 67% of cross-border vendor disputes in 2026. 'Informal workarounds rule the canteen floor,' notes lead auditor.",
    voice_profile={"name": "Rupert Evill", "role": "Crisis Investigator"},
    source_title="Singapore Houston Supply Chain Disruption",
    tier="Full Campaign Distribution Pack"
)

assert fallback_pack.get("tier") == "Full Campaign Distribution Pack", "Tier should be Full Campaign Distribution Pack"
assert "article" in fallback_pack, "Article must be present in fallback pack"
assert len(fallback_pack.get("weekly_posts", [])) == 5, "5 weekly posts must be generated"
assert len(fallback_pack.get("carousel_1", {}).get("slides", [])) >= 7, "Carousel 1 must have at least 7 slides"
assert len(fallback_pack.get("carousel_2", {}).get("slides", [])) >= 7, "Carousel 2 must have at least 7 slides"
assert "research_dossier" in fallback_pack, "Research dossier must be present"
print(f"[+] Fallback pack successfully validated! Article words: {len(fallback_pack['article'].split())}, Weekly posts: {len(fallback_pack['weekly_posts'])}")

print("\n[2] Testing Flask /api/content/generate endpoint via Test Client...")
client = app.test_client()

resp = client.post("/api/content/generate", json={
    "source_type": "text",
    "text": "Cross-border remote work has created systemic wage theft where 67% of contracts fail during cash crunches. Founders ghost workers on Slack.",
    "tier": "Full Campaign Distribution Pack",
    "voice_id": "forensic-operator",
    "topic": "The Offshore Remote Contractor Disconnect"
})

assert resp.status_code == 200, f"Expected 200, got {resp.status_code}: {resp.data}"
item = resp.get_json()
print("[+] Created Campaign Pack item ID:", item.get("id"))
print("[+] Title:", item.get("title"))
print("[+] Tier:", item.get("tier"))
assert item.get("tier") == "Full Campaign Distribution Pack"
assert "article" in item or "content_markdown" in item
assert "weekly_posts" in item and len(item["weekly_posts"]) == 5
assert "carousel_1" in item and len(item["carousel_1"]["slides"]) >= 7
assert "carousel_2" in item and len(item["carousel_2"]["slides"]) >= 7

print("\n[3] Testing Flask /api/content GET endpoint...")
get_resp = client.get("/api/content")
assert get_resp.status_code == 200
items = get_resp.get_json()
campaign_items = [x for x in items if "campaign" in (x.get("tier") or "").lower() or x.get("campaign_pack")]
print(f"[+] Total items: {len(items)}, Campaign Pack items: {len(campaign_items)}")
assert len(campaign_items) > 0, "At least one campaign pack item should exist"
latest = campaign_items[0]
assert "weekly_posts" in latest, "weekly_posts must be restored"
assert "carousel_1" in latest, "carousel_1 must be restored"
assert "carousel_2" in latest, "carousel_2 must be restored"

print("\n[✔] ALL TESTS PASSED SUCCESSFULLY!")
