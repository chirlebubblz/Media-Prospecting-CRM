import sys
import os
import io
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from app import app

def test_notebook_studio():
    client = app.test_client()

    print("=" * 60, flush=True)
    print("RUNNING NOTEBOOKLM STUDIO COMPREHENSIVE TESTS", flush=True)
    print("=" * 60, flush=True)

    # 1. Test GET /content
    print("\n[1] Testing GET /content...", flush=True)
    resp = client.get("/content")
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
    html = resp.get_data(as_text=True)
    assert "view-notebooklm-studio" in html, "Missing #view-notebooklm-studio"
    assert "sources-panel" in html, "Missing .sources-panel"
    assert "chat-messages-container" in html, "Missing #chat-messages-container"
    assert "add-source-modal" in html, "Missing #add-source-modal"
    assert "view-saved-library" in html, "Missing #view-saved-library"
    assert "NotebookLM Studio" in html, "Missing 'NotebookLM Studio' branding"
    print("  --> GET /content returned 200 OK with all required DOM elements!", flush=True)

    # 2. Test POST /api/content/notebook/upload
    print("\n[2] Testing POST /api/content/notebook/upload...", flush=True)
    data = {
        'file': (io.BytesIO(b"Confidential Report: Supply Chain Fraud and Vendor Kickbacks in Southeast Asia.\nEmpirical audits reveal 72% of informal workarounds bypass dual-authorization."), "audit_sample.txt")
    }
    resp = client.post("/api/content/notebook/upload", data=data, content_type='multipart/form-data')
    assert resp.status_code == 200, f"Upload failed: {resp.status_code} {resp.text}"
    upload_res = resp.get_json()
    assert "id" in upload_res and upload_res["id"].startswith("src_")
    assert upload_res["name"] == "audit_sample.txt"
    assert upload_res["type"] == "txt"
    assert "Confidential Report" in upload_res["text"]
    assert "size_label" in upload_res
    print(f"  --> Upload successful: id={upload_res['id']}, size={upload_res['size_label']}", flush=True)

    # 3. Test POST /api/content/notebook/scrape
    print("\n[3] Testing POST /api/content/notebook/scrape...", flush=True)
    # Using a fast mock/local text so we don't block on external network
    resp = client.post("/api/content/notebook/scrape", json={"url": "https://example.com"})
    assert resp.status_code == 200, f"Scrape failed: {resp.status_code} {resp.text}"
    scrape_res = resp.get_json()
    assert "id" in scrape_res and scrape_res["id"].startswith("src_")
    assert scrape_res["type"] == "url"
    assert "url" in scrape_res
    print(f"  --> Scrape endpoint successful: id={scrape_res['id']}, name={scrape_res['name']}", flush=True)

    # 4. Test GET /api/content/notebook/crm-leads
    print("\n[4] Testing GET /api/content/notebook/crm-leads...", flush=True)
    resp = client.get("/api/content/notebook/crm-leads")
    assert resp.status_code == 200
    crm_leads = resp.get_json()
    assert isinstance(crm_leads, list)
    print(f"  --> CRM leads endpoint returned {len(crm_leads)} leads for Tab 4 Hook!", flush=True)

    # 5. Test POST /api/content/notebook/chat - Research Query
    print("\n[5] Testing POST /api/content/notebook/chat (Research Query)...")
    chat_payload = {
        "messages": [
            {"role": "user", "content": "Whistleblower retaliation patterns and why corporate hotlines expose informants"}
        ],
        "sources": [
            {
                "id": upload_res["id"],
                "name": upload_res["name"],
                "type": upload_res["type"],
                "text": upload_res["text"],
                "active": True
            }
        ],
        "voice_id": "forensic-operator",
        "requested_format": None
    }
    resp = client.post("/api/content/notebook/chat", json=chat_payload)
    assert resp.status_code == 200, f"Chat failed: {resp.status_code} {resp.text}"
    chat_res = resp.get_json()
    assert "reply_text" in chat_res and len(chat_res["reply_text"]) > 50
    assert "research_dossier" in chat_res
    assert "suggested_angles" in chat_res
    angles = chat_res["suggested_angles"]
    assert len(angles) >= 4, f"Expected at least 4 angles, got {len(angles)}"
    print(f"  --> Research query successful! Returned {len(angles)} provocative angles:", flush=True)
    for a in angles[:4]:
        print(f"      * [{a.get('id')}]: {a.get('title')}", flush=True)

    # 6. Test Format Generation: Carousel
    print("\n[6] Testing Format Generation: Carousel...", flush=True)
    resp = client.post("/api/content/notebook/chat", json={
        "messages": [
            {"role": "user", "content": "Generate a carousel deck for LinkedIn"}
        ],
        "sources": [upload_res],
        "voice_id": "forensic-operator",
        "requested_format": "carousel"
    })
    assert resp.status_code == 200
    carousel_res = resp.get_json()
    asset = carousel_res.get("generated_asset")
    assert asset is not None, "Missing generated_asset for carousel"
    assert asset.get("type") == "carousel"
    assert len(asset.get("slides", [])) >= 7, f"Expected 7+ slides, got {len(asset.get('slides', []))}"
    assert "copy_script" in asset
    print(f"  --> Carousel generated: {len(asset['slides'])} slides, copy script present!", flush=True)

    # 7. Test Format Generation: In-Feed Essay
    print("\n[7] Testing Format Generation: Essay...", flush=True)
    resp = client.post("/api/content/notebook/chat", json={
        "messages": [
            {"role": "user", "content": "Write an in-feed essay"}
        ],
        "sources": [upload_res],
        "voice_id": "forensic-operator",
        "requested_format": "essay"
    })
    assert resp.status_code == 200
    essay_res = resp.get_json()
    asset = essay_res.get("generated_asset")
    assert asset is not None and asset.get("type") == "essay"
    assert len(asset.get("markdown", "").split()) >= 150
    print(f"  --> Essay generated: {len(asset['markdown'].split())} words!", flush=True)

    # 8. Test Format Generation: 5-Day Posts
    print("\n[8] Testing Format Generation: 5-Day Posts...", flush=True)
    resp = client.post("/api/content/notebook/chat", json={
        "messages": [
            {"role": "user", "content": "Create Monday through Friday posts"}
        ],
        "sources": [upload_res],
        "voice_id": "forensic-operator",
        "requested_format": "weekly_posts"
    })
    assert resp.status_code == 200
    posts_res = resp.get_json()
    asset = posts_res.get("generated_asset")
    assert asset is not None and asset.get("type") == "weekly_posts"
    posts = asset.get("posts", [])
    assert len(posts) == 5, f"Expected 5 posts, got {len(posts)}"
    print(f"  --> Weekly posts generated: {len(posts)} daily posts (Mon-Fri)!", flush=True)

    # 9. Test Format Generation: Full Campaign Pack
    print("\n[9] Testing Format Generation: Full Campaign Pack...", flush=True)
    resp = client.post("/api/content/notebook/chat", json={
        "messages": [
            {"role": "user", "content": "Generate the full authority campaign pack"}
        ],
        "sources": [upload_res],
        "voice_id": "forensic-operator",
        "requested_format": "campaign_pack"
    })
    assert resp.status_code == 200
    camp_res = resp.get_json()
    asset = camp_res.get("generated_asset")
    assert asset is not None and asset.get("type") == "campaign_pack"
    assert "article" in asset and len(asset["article"].split()) > 1000
    assert len(asset.get("weekly_posts", [])) == 5
    assert "carousel_1" in asset
    assert "carousel_2" in asset
    print(f"  --> Campaign pack generated: Article ({len(asset['article'].split())} words), 5 posts, 2 carousels!", flush=True)

    print("\n" + "=" * 60, flush=True)
    print("ALL NOTEBOOKLM STUDIO TESTS PASSED WITH 100% SUCCESS!", flush=True)
    print("=" * 60, flush=True)

if __name__ == "__main__":
    test_notebook_studio()
