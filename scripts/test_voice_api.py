# -*- coding: utf-8 -*-
import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import app, db, VOICES_JSON_PATH

def test_voices_api():
    client = app.test_client()

    print("[*] 1. Testing GET /api/voices...")
    res = client.get("/api/voices")
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    voices = res.get_json()
    print(f"    Returned {len(voices)} voices:")
    for v in voices:
        print(f"    - {v.get('id')}: {v.get('name')}")

    # Check presets
    preset_ids = [v.get("id") for v in voices]
    assert "forensic-operator" in preset_ids, "Missing forensic-operator"
    assert "christian-hunt" in preset_ids, "Missing christian-hunt"
    assert "jordan-sabalo" in preset_ids, "Missing jordan-sabalo"
    assert "growth-dealmaker" in preset_ids, "Missing growth-dealmaker"
    print("[+] All 4 preset voices found in GET /api/voices response!")

    print("[*] 2. Testing POST /api/voices to clone / create a custom voice...")
    test_custom_voice = {
        "id": "test-cloned-investigator",
        "name": "Alex Vance / Forensic Special Situations",
        "role": "Operating Partner & Risk Investigator",
        "philosophy": "When incentives are misaligned, controls are just suggestions.",
        "tone": "Sharp, skeptical, surgical.",
        "cadence": "Pithy, staccato, concrete examples.",
        "banned_words": "paradigm, synergy, holistic",
        "sample_texts": [
            "You cannot audit what employees are actively hiding on unmonitored WhatsApp channels.",
            "Culture is what happens when the founder is asleep."
        ],
        "sample_writing": "You cannot audit what employees are actively hiding on unmonitored WhatsApp channels.\n\nCulture is what happens when the founder is asleep."
    }

    res_post = client.post("/api/voices", json=test_custom_voice)
    assert res_post.status_code == 200, f"Expected 200, got {res_post.status_code}"
    saved_data = res_post.get_json()
    assert saved_data.get("id") == "test-cloned-investigator", "ID mismatch"
    assert saved_data.get("name") == test_custom_voice["name"], "Name mismatch"
    print(f"[+] POST /api/voices successfully saved: {saved_data.get('name')} (id: {saved_data.get('id')})")

    print("[*] 3. Testing GET /api/voices persistence...")
    res_get2 = client.get("/api/voices")
    voices2 = res_get2.get_json()
    found = any(v.get("id") == "test-cloned-investigator" for v in voices2)
    assert found, "Created custom voice was not returned by GET /api/voices"
    print("[+] Custom voice verified in GET /api/voices!")

    # Verify JSON file persistence
    with open(VOICES_JSON_PATH, "r", encoding="utf-8") as f:
        file_voices = json.load(f)
    assert any(v.get("id") == "test-cloned-investigator" for v in file_voices), "Not found in voice_profiles.json"
    print("[+] Verified persistence in voice_profiles.json!")

    # Clean up test voice from json and DB
    print("[*] Cleaning up test voice...")
    file_voices = [v for v in file_voices if v.get("id") != "test-cloned-investigator"]
    with open(VOICES_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(file_voices, f, indent=2, default=str)
    
    if db.is_connected:
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM voice_profiles WHERE id = 'test-cloned-investigator';")
                    conn.commit()
            print("[+] Cleaned up test voice from Neon DB.")
        except Exception as e:
            print(f"[!] Note: cleanup error {e}")

    print("[SUCCESS] All Voice API & Persistence Tests Passed!")

if __name__ == "__main__":
    test_voices_api()
