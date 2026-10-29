"""
Database abstraction layer for Media & Outreach CRM.
Supports dual-mode:
1. Cloud Mode: Neon PostgreSQL (when DATABASE_URL is set)
2. Local Mode: JSON fallback (when DATABASE_URL is empty or unavailable)
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional

try:
    import psycopg2
    from psycopg2.extras import RealDictCursor, execute_values
    PSYCOPG2_AVAILABLE = True
except ImportError:
    PSYCOPG2_AVAILABLE = False


DEFAULT_NEON_URL = "postgresql://neondb_owner:npg_TBCo68znmxJw@ep-rough-art-arc2qxnf-pooler.c-4.us-west-2.aws.neon.tech/neondb?sslmode=require"


def get_db_url() -> Optional[str]:
    """Returns the PostgreSQL connection string if available."""
    url = os.environ.get("DATABASE_URL") or os.environ.get("NEON_DATABASE_URL")
    if url:
        return url
    # Use default Neon project provisioned for this workspace
    return DEFAULT_NEON_URL


class DatabaseManager:
    """Manages connections and queries to Neon Postgres with automatic fallback."""

    def __init__(self, db_url: Optional[str] = None):
        self.db_url = db_url or get_db_url()
        self.is_connected = False
        if PSYCOPG2_AVAILABLE and self.db_url:
            self._init_schema()

    def get_connection(self):
        if not PSYCOPG2_AVAILABLE or not self.db_url:
            return None
        return psycopg2.connect(self.db_url, connect_timeout=3)

    def _init_schema(self):
        """Initializes tables in Neon Postgres if they do not exist."""
        try:
            conn = self.get_connection()
            if not conn:
                self.is_connected = False
                return
            with conn:
                with conn.cursor() as cur:
                    # Media Leads table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS media_leads (
                            id VARCHAR(255) PRIMARY KEY,
                            data JSONB NOT NULL,
                            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    # Executive Leads table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS executive_leads (
                            id VARCHAR(255) PRIMARY KEY,
                            data JSONB NOT NULL,
                            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    # Voice Profiles table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS voice_profiles (
                            id VARCHAR(255) PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            role VARCHAR(255),
                            philosophy TEXT,
                            tone TEXT,
                            cadence TEXT,
                            banned_words TEXT,
                            sample_texts JSONB,
                            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    # Content Items table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS content_items (
                            id VARCHAR(255) PRIMARY KEY,
                            title VARCHAR(500) NOT NULL,
                            tier VARCHAR(100) NOT NULL,
                            topic VARCHAR(255),
                            voice_profile_id VARCHAR(255),
                            source_type VARCHAR(100),
                            source_reference TEXT,
                            content_markdown TEXT NOT NULL,
                            slides_outline JSONB,
                            research_dossier JSONB,
                            status VARCHAR(100) DEFAULT 'Draft',
                            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    conn.commit()
            self.is_connected = True
            print("[+] Neon Postgres schema initialized successfully.")
        except Exception as e:
            print(f"[!] Warning: Could not initialize Neon Postgres: {e}")
            self.is_connected = False

    # ------------------ Media Leads ------------------
    def get_all_media_leads(self) -> Optional[List[Dict[str, Any]]]:
        if not self.is_connected:
            return None
        try:
            with self.get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute("SELECT data FROM media_leads ORDER BY updated_at DESC;")
                    rows = cur.fetchall()
                    return [r["data"] for r in rows]
        except Exception as e:
            print(f"[!] Error reading media_leads from Postgres: {e}")
            return None

    def upsert_media_lead(self, lead: Dict[str, Any]) -> bool:
        if not self.is_connected:
            return False
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        INSERT INTO media_leads (id, data, updated_at)
                        VALUES (%s, %s, CURRENT_TIMESTAMP)
                        ON CONFLICT (id) DO UPDATE
                        SET data = EXCLUDED.data, updated_at = CURRENT_TIMESTAMP;
                    """, (lead["id"], json.dumps(lead)))
                    conn.commit()
            return True
        except Exception as e:
            print(f"[!] Error upserting media lead to Postgres: {e}")
            return False

    def batch_upsert_media_leads(self, leads: List[Dict[str, Any]]) -> bool:
        if not self.is_connected or not leads:
            return False
        try:
            records = [(l["id"], json.dumps(l)) for l in leads if "id" in l]
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    execute_values(cur, """
                        INSERT INTO media_leads (id, data, updated_at)
                        VALUES %s
                        ON CONFLICT (id) DO UPDATE
                        SET data = EXCLUDED.data, updated_at = CURRENT_TIMESTAMP;
                    """, records, template="(%s, %s, CURRENT_TIMESTAMP)")
                    conn.commit()
            return True
        except Exception as e:
            print(f"[!] Error batch upserting media leads to Postgres: {e}")
            return False

    def delete_media_lead(self, lead_id: str) -> bool:
        if not self.is_connected:
            return False
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM media_leads WHERE id = %s;", (lead_id,))
                    conn.commit()
            return True
        except Exception as e:
            print(f"[!] Error deleting media lead from Postgres: {e}")
            return False

    # ------------------ Executive Leads ------------------
    def get_all_executive_leads(self) -> Optional[List[Dict[str, Any]]]:
        if not self.is_connected:
            return None
        try:
            with self.get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute("SELECT data FROM executive_leads ORDER BY updated_at DESC;")
                    rows = cur.fetchall()
                    return [r["data"] for r in rows]
        except Exception as e:
            print(f"[!] Error reading executive_leads from Postgres: {e}")
            return None

    def upsert_executive_lead(self, lead: Dict[str, Any]) -> bool:
        if not self.is_connected:
            return False
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        INSERT INTO executive_leads (id, data, updated_at)
                        VALUES (%s, %s, CURRENT_TIMESTAMP)
                        ON CONFLICT (id) DO UPDATE
                        SET data = EXCLUDED.data, updated_at = CURRENT_TIMESTAMP;
                    """, (lead["id"], json.dumps(lead)))
                    conn.commit()
            return True
        except Exception as e:
            print(f"[!] Error upserting exec lead to Postgres: {e}")
            return False

    def batch_upsert_executive_leads(self, leads: List[Dict[str, Any]]) -> bool:
        if not self.is_connected or not leads:
            return False
        try:
            records = [(l["id"], json.dumps(l)) for l in leads if "id" in l]
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    execute_values(cur, """
                        INSERT INTO executive_leads (id, data, updated_at)
                        VALUES %s
                        ON CONFLICT (id) DO UPDATE
                        SET data = EXCLUDED.data, updated_at = CURRENT_TIMESTAMP;
                    """, records, template="(%s, %s, CURRENT_TIMESTAMP)")
                    conn.commit()
            return True
        except Exception as e:
            print(f"[!] Error batch upserting exec leads to Postgres: {e}")
            return False

    def delete_executive_lead(self, lead_id: str) -> bool:
        if not self.is_connected:
            return False
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM executive_leads WHERE id = %s;", (lead_id,))
                    conn.commit()
            return True
        except Exception as e:
            print(f"[!] Error deleting exec lead from Postgres: {e}")
            return False

    # ------------------ Voice Profiles ------------------
    def get_voice_profiles(self) -> List[Dict[str, Any]]:
        if not self.is_connected:
            return []
        try:
            with self.get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute("SELECT * FROM voice_profiles ORDER BY name ASC;")
                    rows = cur.fetchall()
                    profiles = []
                    for r in rows:
                        p = dict(r)
                        if isinstance(p.get("updated_at"), datetime):
                            p["updated_at"] = p["updated_at"].isoformat()
                        profiles.append(p)
                    return profiles
        except Exception as e:
            print(f"[!] Error fetching voice profiles: {e}")
            return []

    def upsert_voice_profile(self, profile: Dict[str, Any]) -> bool:
        if not self.is_connected:
            return False
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        INSERT INTO voice_profiles (id, name, role, philosophy, tone, cadence, banned_words, sample_texts, updated_at)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
                        ON CONFLICT (id) DO UPDATE SET
                            name = EXCLUDED.name,
                            role = EXCLUDED.role,
                            philosophy = EXCLUDED.philosophy,
                            tone = EXCLUDED.tone,
                            cadence = EXCLUDED.cadence,
                            banned_words = EXCLUDED.banned_words,
                            sample_texts = EXCLUDED.sample_texts,
                            updated_at = CURRENT_TIMESTAMP;
                    """, (
                        profile["id"],
                        profile["name"],
                        profile.get("role", ""),
                        profile.get("philosophy", ""),
                        profile.get("tone", ""),
                        profile.get("cadence", ""),
                        profile.get("banned_words", ""),
                        json.dumps(profile.get("sample_texts", []))
                    ))
                    conn.commit()
            return True
        except Exception as e:
            print(f"[!] Error saving voice profile: {e}")
            return False

    # ------------------ Content Items ------------------
    def get_content_items(self) -> List[Dict[str, Any]]:
        if not self.is_connected:
            return []
        try:
            with self.get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute("SELECT * FROM content_items ORDER BY created_at DESC;")
                    rows = cur.fetchall()
                    items = []
                    for r in rows:
                        item = dict(r)
                        if isinstance(item.get("created_at"), datetime):
                            item["created_at"] = item["created_at"].isoformat()
                        if isinstance(item.get("updated_at"), datetime):
                            item["updated_at"] = item["updated_at"].isoformat()
                        items.append(item)
                    return items
        except Exception as e:
            print(f"[!] Error fetching content items: {e}")
            return []

    def save_content_item(self, item: Dict[str, Any]) -> bool:
        if not self.is_connected:
            return False
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        INSERT INTO content_items (
                            id, title, tier, topic, voice_profile_id, source_type,
                            source_reference, content_markdown, slides_outline,
                            research_dossier, status, updated_at
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
                        ON CONFLICT (id) DO UPDATE SET
                            title = EXCLUDED.title,
                            tier = EXCLUDED.tier,
                            topic = EXCLUDED.topic,
                            voice_profile_id = EXCLUDED.voice_profile_id,
                            source_type = EXCLUDED.source_type,
                            source_reference = EXCLUDED.source_reference,
                            content_markdown = EXCLUDED.content_markdown,
                            slides_outline = EXCLUDED.slides_outline,
                            research_dossier = EXCLUDED.research_dossier,
                            status = EXCLUDED.status,
                            updated_at = CURRENT_TIMESTAMP;
                    """, (
                        item["id"],
                        item["title"],
                        item.get("tier", "Tier 1: Short-Form Carousel"),
                        item.get("topic", "General"),
                        item.get("voice_profile_id", "default"),
                        item.get("source_type", "text"),
                        item.get("source_reference", ""),
                        item.get("content_markdown", ""),
                        json.dumps(item.get("slides_outline", [])),
                        json.dumps(item.get("research_dossier", {})),
                        item.get("status", "Draft")
                    ))
                    conn.commit()
            return True
        except Exception as e:
            print(f"[!] Error saving content item: {e}")
            return False

    def delete_content_item(self, item_id: str) -> bool:
        if not self.is_connected:
            return False
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM content_items WHERE id = %s;", (item_id,))
                    conn.commit()
            return True
        except Exception as e:
            print(f"[!] Error deleting content item: {e}")
            return False
