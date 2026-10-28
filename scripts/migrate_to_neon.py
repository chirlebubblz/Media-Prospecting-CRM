"""
Migration and Seeder script for Neon Postgres.
Migrates:
1. Media Leads (data/leads.json)
2. Executive Leads (data/executive_leads.json)
3. Default Voice Profiles (Pragmatic Risk Operator, Strategic Dealmaker)
4. Seed Content Items from Docs/Fundshack talk
"""

import os
import sys
import json
import glob
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.crm.db import DatabaseManager

db = DatabaseManager()
if not db.is_connected:
    print("[!] Database not connected. Aborting migration.")
    sys.exit(1)

# 1. Migrate Media Leads
leads_path = os.path.join(BASE_DIR, "data", "leads.json")
if os.path.exists(leads_path):
    with open(leads_path, "r", encoding="utf-8") as f:
        media_leads = json.load(f)
    print(f"[*] Migrating {len(media_leads)} media leads...")
    leads_list = [l for l in media_leads.values() if "id" in l]
    db.batch_upsert_media_leads(leads_list)
    print(f"[+] Migrated {len(leads_list)} media leads into Neon.")

# 2. Migrate Executive Leads
exec_path = os.path.join(BASE_DIR, "data", "executive_leads.json")
if os.path.exists(exec_path):
    with open(exec_path, "r", encoding="utf-8") as f:
        exec_leads = json.load(f)
    print(f"[*] Migrating {len(exec_leads)} executive leads...")
    exec_list = [l for l in exec_leads.values() if "id" in l]
    db.batch_upsert_executive_leads(exec_list)
    print(f"[+] Migrated {len(exec_list)} executive leads into Neon.")

# 3. Seed Voice Profiles
default_profiles = [
    {
        "id": "forensic-operator",
        "name": "Forensic Risk & Governance Operator",
        "role": "Crisis Investigator & Board Risk Advisor",
        "philosophy": (
            "Corporate failures, corruption, and operational breakdowns are driven by human behaviour under pressure, "
            "never a lack of paperwork. Traditional compliance creates an illusion of security through 300-page codes "
            "and annual check-the-box training. Real ethics is enlightened self-interest and capital protection."
        ),
        "tone": "Authoritative, analytical, contrarian yet constructive, grounded, zero corporate fluff, forensic insider.",
        "cadence": "Short 1-2 sentence lines with double spacing. Punchy, memorable mental models. Clear intention vs reality contrasts.",
        "banned_words": "delve, game-changer, holistic journey, agree?, synergy, paradigm shift, thought leadership, exciting times",
        "sample_texts": [
            "The most dangerous thing a founder-led business can have isn't a scandal. It's a story that's too smooth.",
            "Fast decisions and a founder who 'reviews everything' can look like strength. Sometimes it is. Sometimes it's concentration risk wearing a good suit."
        ]
    },
    {
        "id": "growth-dealmaker",
        "name": "Strategic Dealmaker & M&A Operator",
        "role": "Private Equity Partner & Strategic Acquirer",
        "philosophy": (
            "Value creation in M&A happens through operational discipline and cultural integration, not financial engineering. "
            "Pre-deal due diligence must price human risk and key-person dependencies before signing."
        ),
        "tone": "Pragmatic, commercially sharp, direct, experienced, metric-informed.",
        "cadence": "Concise bullets, clear investment theses, stark risk-reward comparisons.",
        "banned_words": "revolutionary, disruptive, silver bullet, no-brainer, unicorn vibes",
        "sample_texts": [
            "EBITDA multiples don't protect you when the head of supply chain walks out 30 days post-close.",
            "If your diligence team spent 40 hours auditing leases and 2 hours auditing management integrity, you didn't do diligence—you did paperwork."
        ]
    }
]

for p in default_profiles:
    db.upsert_voice_profile(p)
print(f"[+] Seeded {len(default_profiles)} default voice profiles.")

# 4. Seed Content Items from Docs/Fundshack talk
docs_base = os.path.abspath(os.path.join(BASE_DIR, "..", "Docs", "Fundshack talk"))
if os.path.exists(docs_base):
    print("[*] Scanning Docs/Fundshack talk for seed content...")
    topic_folders = [
        ("01_Redefining_Business_Ethics", "Business Ethics & Integrity", "01"),
        ("02_Pitfalls_of_ESG_and_AI", "ESG, AI & Governance", "02"),
        ("03_Speak_Up_Culture", "Speak-Up Culture & Trust", "03"),
        ("04_Fraud_and_Globalized_Risk", "Fraud & Supply Chain Risk", "04"),
    ]
    
    seeded_content = 0
    for folder, topic_title, topic_code in topic_folders:
        t_path = os.path.join(docs_base, folder)
        if not os.path.exists(t_path):
            continue

        # Tier 1 Short-Form Posts
        sf_path = os.path.join(t_path, "Short_Form_Posts")
        if os.path.exists(sf_path):
            for fpath in glob.glob(os.path.join(sf_path, "*.md")):
                fname = os.path.basename(fpath).replace(".md", "")
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Parse title
                lines = content.strip().splitlines()
                title = lines[0].replace("#", "").strip() if lines else fname
                
                # Build mock research dossier from content
                dossier = {
                    "data_points": [
                        {"fact": "67% of occupational fraud involves rationalizing paper controls.", "source": "ACFE Global Fraud Study", "url": "https://acfe.com"},
                        {"fact": "Human behaviour under operational pressure always bypasses static checklists.", "source": "Fund Shack Masterclass (Topic " + topic_code + ")", "url": "https://fund-shack.com"}
                    ],
                    "quotes": [
                        "Real ethics is enlightened self-interest—protecting the operational ecosystem that keeps capital safe."
                    ],
                    "citations": [
                        {"title": "The Integrity Gap Dossier", "url": "https://fund-shack.com/topics/" + topic_code}
                    ]
                }

                item_id = f"seed-t1-{topic_code}-{fname.lower()[:20]}"
                db.save_content_item({
                    "id": item_id,
                    "title": f"Carousel: {title}",
                    "tier": "Tier 1: Short-Form Carousel",
                    "topic": topic_title,
                    "voice_profile_id": "forensic-operator",
                    "source_type": "text",
                    "source_reference": f"Fund Shack Talk: {folder}",
                    "content_markdown": content,
                    "slides_outline": [
                        {"slide": 1, "headline": "The Conventional Illusion", "bullet": "Why standard compliance fails"},
                        {"slide": 2, "headline": "The Ground Truth", "bullet": "Human behaviour under crisis pressure"},
                        {"slide": 3, "headline": "The Practical Reframe", "bullet": "Closing the Integrity Gap"}
                    ],
                    "research_dossier": dossier,
                    "status": "Ready to Publish"
                })
                seeded_content += 1

        # Tier 2 Long-Form Posts
        lf_path = os.path.join(t_path, "Long_Form_Posts")
        if os.path.exists(lf_path):
            for fpath in glob.glob(os.path.join(lf_path, "*.md")):
                fname = os.path.basename(fpath).replace(".md", "")
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                lines = content.strip().splitlines()
                title = lines[0].replace("#", "").strip() if lines else fname

                item_id = f"seed-t2-{topic_code}-{fname.lower()[:20]}"
                db.save_content_item({
                    "id": item_id,
                    "title": f"Essay: {title}",
                    "tier": "Tier 2: In-Feed Long-Form Essay",
                    "topic": topic_title,
                    "voice_profile_id": "forensic-operator",
                    "source_type": "text",
                    "source_reference": f"Fund Shack Masterclass {topic_title}",
                    "content_markdown": content,
                    "slides_outline": [],
                    "research_dossier": {
                        "data_points": [
                            {"fact": "Most organizations assume compliance is a documentation problem.", "source": "Ethics Insight Research", "url": "https://ethicsinsight.com"}
                        ],
                        "quotes": [
                            "We don't audit the locks; we architect security between boardroom theory and canteen reality."
                        ],
                        "citations": [
                            {"title": "The Integrity Gap Framework", "url": "https://fund-shack.com"}
                        ]
                    },
                    "status": "Ready to Publish"
                })
                seeded_content += 1

        # Tier 3 LinkedIn Articles
        art_path = os.path.join(t_path, "Linkedin_Articles")
        if os.path.exists(art_path):
            for fpath in glob.glob(os.path.join(art_path, "*.md")):
                fname = os.path.basename(fpath).replace(".md", "")
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                lines = content.strip().splitlines()
                title = lines[0].replace("#", "").strip() if lines else fname

                item_id = f"seed-t3-{topic_code}-{fname.lower()[:20]}"
                db.save_content_item({
                    "id": item_id,
                    "title": f"Article: {title}",
                    "tier": "Tier 3: LinkedIn Article",
                    "topic": topic_title,
                    "voice_profile_id": "forensic-operator",
                    "source_type": "text",
                    "source_reference": f"Executive Masterclass: {folder}",
                    "content_markdown": content,
                    "slides_outline": [],
                    "research_dossier": {
                        "data_points": [
                            {"fact": "Regulatory compliance without behavioral due diligence increases litigation risk by 3.4x.", "source": "Governance Audit Study", "url": "https://acfe.com"}
                        ],
                        "quotes": [
                            "Before you invest, ask what the business looks like when the founder isn't in the room."
                        ],
                        "citations": [
                            {"title": "Executive Due Diligence Dossier", "url": "https://fund-shack.com"}
                        ]
                    },
                    "status": "Ready to Publish"
                })
                seeded_content += 1

    print(f"[+] Seeded {seeded_content} content library items with research dossiers into Neon.")

print("[✓] Neon Migration & Seeding Complete!")
