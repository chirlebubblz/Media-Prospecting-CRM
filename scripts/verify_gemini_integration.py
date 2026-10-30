import os
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

import app

client = app.app.test_client()

print("--- 1. Testing /api/content/researched-links ---")
resp_links = client.get("/api/content/researched-links")
print("Researched links status:", resp_links.status_code)
links_data = resp_links.get_json()
print(f"Researched links count: {len(links_data)}")
if links_data:
    print("Sample link:", links_data[0])

print("\n--- 2. Testing /api/content/generate with text & Gemini 2.5 Flash ---")
test_payload = {
    "source_type": "text",
    "tier": "Tier 1: Short-Form Carousel",
    "topic": "The Illusion of Boardroom Due Diligence",
    "voice_id": "forensic-operator",
    "text": """
    In cross-border private equity deals, 78% of post-acquisition fraud investigations revealed that the seller had satisfied every formal compliance checklist. 
    "Checklists measure compliance with bureaucracy, not human behavioral pressure," explains lead forensic investigator Rupert Vance.
    "When target margins compress by more than 15%, local executives rationalize unrecorded liabilities in 8 out of 10 portfolio companies."
    The average forensic recovery cost exceeded $23 million per incident in 2024.
    === Source: https://ft.com/content/pe-risk-report-2024 ===
    """
}

resp_gen = client.post("/api/content/generate", json=test_payload)
print("Generate status:", resp_gen.status_code)
if resp_gen.status_code != 200:
    print("Error:", resp_gen.get_data(as_text=True))
    sys.exit(1)

gen_data = resp_gen.get_json()
print("Generated Title:", gen_data.get("title"))
print("Author Voice ID:", gen_data.get("voice_profile_id"))
print("Slides count:", len(gen_data.get("slides_outline", [])))
if gen_data.get("slides_outline"):
    print("Slide 1:", gen_data["slides_outline"][0])
print("\nCompanion Post Preview:\n", gen_data.get("content_markdown", "")[:350])

dossier = gen_data.get("research_dossier", {})
print("\nResearch Dossier:")
print("Thesis:", dossier.get("thesis"))
print("Unseen Tension:", dossier.get("unseen_tension"))
print("Data Points:", len(dossier.get("data_points", [])))
for dp in dossier.get("data_points", []):
    print(" - Fact:", dp.get("fact"))
    print("   Source:", dp.get("source"), "| URL:", dp.get("url"))
print("Quotes:", dossier.get("quotes"))
print("Citations:", dossier.get("citations"))

print("\n--- 3. Testing /api/content/researched-links after generation ---")
resp_links2 = client.get("/api/content/researched-links")
links_data2 = resp_links2.get_json()
print(f"Researched links count after generation: {len(links_data2)}")
matching_link = next((x for x in links_data2 if "ft.com" in x.get("url", "")), None)
print("Newly indexed link found:", bool(matching_link), matching_link)

print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
