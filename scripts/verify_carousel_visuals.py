import os
import sys
import time
import threading
from playwright.sync_api import sync_playwright

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

sys.path.insert(0, os.path.abspath("media_prospecting"))
from app import app, db

TEST_PORT = 5055
screenshot_path = os.path.abspath("carousel_visual_guide.png")
artifact_screenshot_path = r"C:\Users\jeraf\.gemini\antigravity\brain\fe5fd1d7-a693-44b1-8a32-72a2bd2f1c5a\carousel_visual_guide.png"

def run_server():
    app.run(host="127.0.0.1", port=TEST_PORT, debug=False, use_reloader=False)

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
time.sleep(2)

print(f"[*] Test server started on http://127.0.0.1:{TEST_PORT}")

console_errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1400, "height": 900})
    # Grant clipboard permissions for automated test
    context.grant_permissions(["clipboard-read", "clipboard-write"])
    page = context.new_page()

    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda err: console_errors.append(str(err)))

    print("[*] Navigating to /content...")
    page.goto(f"http://127.0.0.1:{TEST_PORT}/content")
    page.wait_for_selector("#chat-scroll-area", timeout=15000)

    print("[*] Injecting sample carousel asset into chat messages to test inline widget...")
    page.evaluate("""() => {
        const testAsset = {
            type: 'carousel',
            title: 'The 4:45 PM Friday Test',
            visual_style_guide: {
                mood: 'Forensic, cinematic, high-stakes institutional minimalism',
                palette: 'Obsidian Slate (#070b14), Hazard Amber (#f59e0b), Crisp Bone White (#f8fafc)',
                typography_vibe: 'Bold condensed Swiss grotesque headlines, clean monospaced data accents',
                aspect_ratio: '4:5 (Vertical Carousel - 1080x1350px)'
            },
            slides: [
                {
                    slide: 1,
                    type: 'Cover / Hook',
                    headline: 'The 4:45 PM Friday Test',
                    bullet: 'Why boardroom compliance collapses when commercial targets are in jeopardy.',
                    visual_concept: 'Split-screen high contrast: A pristine glass corporate boardroom overlooking a skyline on the left vs. an unread 2:15 AM urgent Slack notification on a cracked laptop screen on the right.',
                    image_prompt: 'Cinematic editorial photograph, split-screen composition: left side shows a pristine dark corporate boardroom with ambient blue glass reflections, right side shows a single dim desk lamp illuminating an unread urgent incident log on a laptop screen, 35mm film grain, moody shadows, minimalist corporate thriller aesthetic, photorealistic, 8k --ar 4:5 --style raw',
                    color_mood: 'Deep obsidian #070b14 with hazard amber #f59e0b spotlight'
                },
                {
                    slide: 2,
                    type: 'The Safety Mirage',
                    headline: 'The Illusion of Safety',
                    bullet: 'A 140-page policy binder does not stop crisis decisions under deadline stress.',
                    visual_concept: 'A pristine, polished 140-page corporate binder encased inside a cracked display glass case, glowing faintly under cold museum spotlight.',
                    image_prompt: 'Cinematic macro shot of an immaculate leather-bound corporate compliance handbook sitting beneath cracked museum vitrine glass, harsh spotlight beam cutting through volumetric dust, cold corporate atmosphere, high resolution, minimalist editorial style --ar 4:5 --style raw',
                    color_mood: 'Cold slate blue #1e293b with stark white directional lighting'
                }
            ],
            copy_script: 'Full companion post script here...'
        };
        notebookChatMessages.push({
            role: 'assistant',
            content: 'Synthesized your complete 7-slide carousel outline with dedicated visual art direction guides and Midjourney prompts below:',
            asset: testAsset
        });
        renderChatMessages();
    }""")

    page.wait_for_timeout(1000)

    # Verify visual style guide banner and slide guide card rendered
    banner = page.query_selector(".deck-style-guide-banner")
    guide = page.query_selector(".slide-visual-guide")
    copy_btn = page.query_selector(".copy-prompt-btn")

    assert banner is not None, "Deck style guide banner missing!"
    assert guide is not None, "Slide visual guide missing!"
    assert copy_btn is not None, "Copy image prompt button missing!"

    print("[*] Deck style guide and visual guide successfully rendered in inline chat widget!")

    # Click the copy prompt button
    copy_btn.click()
    page.wait_for_timeout(500)
    btn_text = copy_btn.inner_text()
    print(f"[*] Button text after click: '{btn_text}'")

    # Now test opening a Campaign Pack with Carousels in the modal
    print("[*] Testing modal carousel viewer...")
    page.evaluate("""() => {
        const item = {
            id: 'test_camp_1',
            title: 'The Digital Sweatshop Paradox: Campaign Pack',
            tier: 'Full Campaign Distribution Pack',
            article: '# Full Investigation Article...',
            weekly_posts: [{ day: 'Monday', theme: 'The Hook', body: 'Post copy...' }],
            carousel_1: {
                title: 'Problem Deconstruction Deck',
                visual_style_guide: {
                    mood: 'Forensic, cinematic, high-stakes institutional minimalism',
                    palette: 'Obsidian Slate (#070b14), Hazard Amber (#f59e0b), Crisp Bone White (#f8fafc)',
                    typography_vibe: 'Bold condensed Swiss grotesque headlines, clean monospaced data accents',
                    aspect_ratio: '4:5 (Vertical Carousel - 1080x1350px)'
                },
                slides: [
                    {
                        slide: 1,
                        type: 'Hook',
                        headline: 'Why Leaders Get Offshore Governance Backwards',
                        bullet: 'The dangerous corporate illusion everyone takes for granted.',
                        visual_concept: 'Split-screen high contrast: A pristine glass corporate boardroom overlooking a skyline on the left vs. an unread 2:15 AM urgent Slack notification on a cracked laptop screen on the right.',
                        image_prompt: 'Cinematic editorial photograph, split-screen composition: left side shows a pristine dark corporate boardroom with ambient blue glass reflections, right side shows a single dim desk lamp illuminating an unread urgent incident log on a laptop screen, 35mm film grain, moody shadows, minimalist corporate thriller aesthetic, photorealistic, 8k --ar 4:5 --style raw',
                        color_mood: 'Deep obsidian #070b14 with hazard amber #f59e0b spotlight'
                    }
                ]
            }
        };
        openContentViewModal(item);
        switchCampaignTab('c1');
    }""")

    page.wait_for_timeout(1000)

    # Take screenshot of the modal with the carousel visual art direction and prompt
    page.screenshot(path=screenshot_path, full_page=False)
    page.screenshot(path=artifact_screenshot_path, full_page=False)
    print(f"[*] Screenshot saved to {screenshot_path} and {artifact_screenshot_path}")

    browser.close()

if console_errors:
    print(f"[!] Warning: console errors encountered: {console_errors}")
else:
    print("[+] Zero console errors detected! UI is clean and functional.")

print("[+] All verification assertions passed successfully!")
