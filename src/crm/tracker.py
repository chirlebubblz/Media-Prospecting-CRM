"""
CRM and Lead Tracker module for Ethics Insight.
Stores rich podcast prospecting data, social media links, editorial summaries,
and custom Rupert Evill / Ethics Insight angles in local CSV and JSON.
"""

import csv
import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))
JSON_PATH = os.path.join(DATA_DIR, "leads.json")
CSV_PATH = os.path.join(DATA_DIR, "leads.csv")

CSV_COLUMNS = [
    "id",
    "name",
    "show_name",
    "content_type",
    "episode_title",
    "host",
    "host_topics",
    "producer",
    "genre",
    "topic",
    "theme",
    "listeners",
    "followers",
    "subscribers",
    "posts_per_month",
    "global_rank",
    "reviews_rating",
    "reach_metrics",
    "show_email",
    "host_email",
    "contact_email",
    "website",
    "company_linkedin",
    "host_linkedin",
    "linkedin_url",
    "twitter_url",
    "host_twitter",
    "facebook_url",
    "instagram_url",
    "tiktok_url",
    "youtube_url",
    "spotify_url",
    "apple_url",
    "feed_url",
    "summary",
    "rupert_angle",
    "talking_points",
    "status",
    "date_added",
    "date_pitched",
    "recent_episode_sample",
    "notes"
]


class LeadTracker:
    def __init__(self, json_path: str = JSON_PATH, csv_path: str = CSV_PATH):
        self.json_path = json_path
        self.csv_path = csv_path
        os.makedirs(os.path.dirname(self.json_path), exist_ok=True)
        self.leads: Dict[str, Dict[str, Any]] = self._load_leads()

    def _load_leads(self) -> Dict[str, Dict[str, Any]]:
        if os.path.exists(self.json_path):
            try:
                with open(self.json_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[!] Warning reading {self.json_path}: {e}")
        return {}

    def save(self):
        """Saves current leads to both JSON and CSV files."""
        # 1. Save JSON
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(self.leads, f, indent=2, ensure_ascii=False)

        # 2. Save CSV
        with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            writer.writeheader()
            for lead_id, item in self.leads.items():
                recent_sample = ""
                recent_eps = item.get("recent_episodes", [])
                if recent_eps and isinstance(recent_eps, list):
                    recent_sample = recent_eps[0].get("title", "")

                row = {col: item.get(col, "") for col in CSV_COLUMNS}
                if recent_sample and not row.get("recent_episode_sample"):
                    row["recent_episode_sample"] = recent_sample
                writer.writerow(row)

    def add_or_update_lead(self, lead_data: Dict[str, Any]) -> bool:
        """
        Adds a new lead or updates existing. Keyed by feed_url or ID.
        Returns True if newly added, False if updated.
        """
        key = lead_data.get("id") or lead_data.get("feed_url") or lead_data.get("name")
        if not key:
            return False

        is_new = key not in self.leads
        now_str = datetime.now().strftime("%Y-%m-%d")

        if is_new:
            entry = {
                "id": key,
                "name": lead_data.get("name", ""),
                "host": lead_data.get("host", "") or lead_data.get("author_name", ""),
                "producer": lead_data.get("producer", ""),
                "media_type": lead_data.get("media_type", "Audio Podcast"),
                "genre": lead_data.get("genre", ""),
                "topic": lead_data.get("topic", lead_data.get("genre", "")),
                "theme": lead_data.get("theme", ""),
                "reach_metrics": lead_data.get("reach_metrics", ""),
                "contact_email": lead_data.get("contact_email", ""),
                "all_emails": lead_data.get("all_emails", []),
                "website": lead_data.get("website", ""),
                "linkedin_url": lead_data.get("linkedin_url", ""),
                "twitter_url": lead_data.get("twitter_url", ""),
                "youtube_url": lead_data.get("youtube_url", ""),
                "spotify_url": lead_data.get("spotify_url", ""),
                "apple_url": lead_data.get("apple_url", ""),
                "feed_url": lead_data.get("feed_url", ""),
                "summary": lead_data.get("summary", lead_data.get("description", "")),
                "rupert_angle": lead_data.get("rupert_angle", lead_data.get("pitch_angle", "")),
                "talking_points": lead_data.get("talking_points", ""),
                "recent_episodes": lead_data.get("recent_episodes", []),
                "status": lead_data.get("status", "Researching"),
                "date_added": now_str,
                "date_pitched": lead_data.get("date_pitched", ""),
                "notes": lead_data.get("notes", ""),
            }
            self.leads[key] = entry
        else:
            existing = self.leads[key]
            for field in [
                "name", "host", "producer", "genre", "topic", "theme", "reach_metrics",
                "contact_email", "website", "linkedin_url", "twitter_url", "youtube_url",
                "spotify_url", "apple_url", "summary", "rupert_angle", "talking_points",
                "status", "notes"
            ]:
                val = lead_data.get(field)
                if val:
                    existing[field] = val
            if lead_data.get("recent_episodes") and not existing.get("recent_episodes"):
                existing["recent_episodes"] = lead_data["recent_episodes"]
            if lead_data.get("all_emails"):
                merged = list(dict.fromkeys(existing.get("all_emails", []) + lead_data["all_emails"]))
                existing["all_emails"] = merged

        return is_new

    def get_leads(self, status_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        self.leads = self._load_leads()
        leads_list = list(self.leads.values())
        if status_filter:
            leads_list = [l for l in leads_list if l.get("status", "").lower() == status_filter.lower()]
        return leads_list

    def update_status(self, key_or_name: str, status: str, notes: str = "", pitch_angle: str = "") -> bool:
        for key, lead in self.leads.items():
            if key == key_or_name or lead.get("name", "").lower() == key_or_name.lower():
                lead["status"] = status
                if notes:
                    lead["notes"] = notes
                if pitch_angle:
                    lead["rupert_angle"] = pitch_angle
                    lead["pitch_angle"] = pitch_angle
                if status.lower() == "pitched" and not lead.get("date_pitched"):
                    lead["date_pitched"] = datetime.now().strftime("%Y-%m-%d")
                self.save()
                return True
        return False
