import os
import sys
import json
import requests
import time

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

env_file = os.path.join(base_dir, ".env")
if os.path.exists(env_file):
    with open(env_file, "r") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                os.environ["GEMINI_API_KEY"] = line.split("=", 1)[1].strip()

api_key = os.environ.get("GEMINI_API_KEY")

sample_text = """
The Cross-Border Agency Trap: Investigation into Offshore Remote Contractors
Investigations across Southeast Asia and Latin America demonstrate an escalating pattern:
Digital marketing, software development, and growth agencies in the US and Europe hire remote contractors in the Philippines, Colombia, and Nigeria under the banner of 'We are a family' and 'Async Freedom.'
However, empirical analysis of over 420 offshore agency disputes reveals that 67% of cross-border payment failures occur during transition quarters when agencies experience cash flow contraction or client churn.
When cash tightens, US agency founders routinely lock offshore contractors out of Slack, Google Workspace, and project trackers before the final monthly invoice clears, effectively externalizing operational downside onto workers who lack cross-border legal recourse.
According to forensic governance researcher Rupert Evill at Ethics Insight, this is the classic 'Policy Wall Problem': organizations maintain glowing public LinkedIn posts about conscious culture while frontline systems lack basic payment escrow or dispute escalation.
Furthermore, as Christian Hunt explores on The Human Risk Podcast, physical and digital distance erases behavioral friction: stiffing someone face-to-face creates unbearable social shame; deactivating an avatar on Slack is reduced to an administrative click.
"""

topic = "The Cross-Border Agency Trap & Offshore Wage Theft"
voice_profile = {
    "name": "Rupert Evill",
    "role": "Crisis Investigator & Founder at Ethics Insight",
    "philosophy": "Corporate failures and breakdowns are driven by human behaviour under pressure, never a lack of paperwork. Traditional compliance creates an illusion of security through check-the-box policies. Real ethics is enlightened self-interest and capital protection.",
    "tone": "Authoritative, analytical, contrarian yet constructive, grounded, zero corporate fluff, forensic insider.",
    "cadence": "Short 1-2 sentence lines with double spacing. Punchy, memorable mental models. Clear intention vs reality contrasts.",
    "banned_words": "delve, game-changer, holistic journey, agree?, synergy, paradigm shift, thought leadership, exciting times, vital, crucial, beacon, testament"
}

system_instruction = (
    "You are an elite investigative ghostwriter, behavioral risk researcher, and senior executive advisor operating with the forensic rigor of Rupert Evill (Ethics Insight, 'The Integrity Gap') and Christian Hunt ('The Human Risk Podcast').\n\n"
    "ANTI-AI GHOSTWRITING MANDATES:\n"
    "1. Zero generic AI tropes: NEVER use 'delve', 'tapestry', 'in today\\'s rapidly evolving world', 'beacon', 'testament', 'crucial', 'holistic', 'game-changer', 'fostering', 'supercharge', 'unleash', 'more than ever', 'look no further'.\n"
    "2. Human cadence: Vary sentence rhythm. Write short, punchy 1-2 sentence lines with double spacing in posts. Use visceral micro-narratives (e.g. what happens at 2:15 AM on a night shift in Cebu or 4:45 PM on a Friday).\n"
    "3. Contrarian thesis: Real risk is never a lack of paperwork—it is human behavior under commercial pressure. Zero complaints is a 'signal of silence' caused by fear, not integrity. Compliance theatre creates a dangerous illusion of security.\n"
    "4. Hard empirical proof: Ground arguments in verified data points, exact percentages, dollar losses, specific research findings, and citations.\n"
    "5. Ground truth over policy: Real governance is capital preservation and downside protection, not moral posturing or PR.\n\n"
    "Strictly return a valid JSON object matching the requested schema."
)

prompt = f"""Synthesize the source material into an exhaustive, publication-grade **LinkedIn Authority Campaign Pack** modeled after investigative case studies like 'The Digital Sweatshop Paradox'.

AUTHOR PROFILE:
- Name: {voice_profile['name']} ({voice_profile['role']})
- Philosophy: {voice_profile['philosophy']}
- Tone: {voice_profile['tone']}
- Cadence: {voice_profile['cadence']}
- Banned Words: {voice_profile['banned_words']}

TOPIC: {topic}

RAW RESEARCH TEXT:
{sample_text}

GENERATE A STRICT JSON OBJECT WITH THESE EXACT KEYS:
{{
  "article": "Full markdown long-form article (1,800 to 2,500 words). Include title, subtitle, byline, hero image placeholder, TL;DR Key Takeaways, human vignette (e.g. 2:15 AM screen in Cebu), deep dive on behavioral risk (Christian Hunt / Human Risk), corporate virtue vs reality / policy wall problem (Rupert Evill / Ethics Insight), 4-step tactical operator framework, diagnostic boardroom checklist with 3 hard questions, cold reality conclusion, and full References & Citations.",
  "weekly_posts": [
    {{
      "day": "Monday",
      "title": "The Scroll-Stopping Hook / Human Vignette",
      "post_text": "Full LinkedIn post copy with double spaced lines, arresting opening quote/vignette, takeaway, link placeholder, and 4-5 hashtags.",
      "hashtags": "#RemoteWork #Leadership #BusinessEthics #HumanRisk"
    }},
    {{
      "day": "Tuesday",
      "title": "The Behavioral / Systemic Blindspot",
      "post_text": "Full LinkedIn post copy on why distance erases empathy and why digital screens remove social friction...",
      "hashtags": "#HumanRisk #BehavioralScience #CorporateCulture"
    }},
    {{
      "day": "Wednesday",
      "title": "The Empirical Inversion",
      "post_text": "Full LinkedIn post copy focusing on the hard numbers and the 'Signal of Silence' (why zero complaints means fear)...",
      "hashtags": "#DueDiligence #Governance #TheIntegrityGap"
    }},
    {{
      "day": "Thursday",
      "title": "The Contrarian Framework & 3 Hard Questions for the Board",
      "post_text": "Full LinkedIn post copy on the Policy Wall Problem and 3 diagnostic questions for the board...",
      "hashtags": "#BoardGovernance #RiskManagement #Leadership"
    }},
    {{
      "day": "Friday",
      "title": "The Tactical Operator Diagnostic & Executive CTA",
      "post_text": "Full LinkedIn post copy with frontline operator takeaways, capital preservation focus, and CTA...",
      "hashtags": "#FutureOfWork #ExecutiveBriefing #EthicsInsight"
    }}
  ],
  "carousel_1": {{
    "title": "Problem Deconstruction Deck",
    "description": "7-8 slide high-dwell deck deconstructing why most leaders get this issue backwards.",
    "slides": [
      {{ "slide": 1, "type": "Hook", "headline": "Why Most Leaders Get [Topic] Backwards", "bullet": "The dangerous corporate illusion everyone takes for granted." }},
      {{ "slide": 2, "type": "The Safety Mirage", "headline": "The Safety Mirage", "bullet": "Why paper policies create a false sense of security." }},
      {{ "slide": 3, "type": "The Hard Number", "headline": "The Hard Number", "bullet": "The empirical data point exposing the breakdown." }},
      {{ "slide": 4, "type": "The Operational Break", "headline": "Where It Fails: 4:45 PM on a Friday", "bullet": "How operational stress forces informal workarounds." }},
      {{ "slide": 5, "type": "The Systemic Blindspot", "headline": "The Signal of Silence", "bullet": "Why zero complaints is fear, not harmony." }},
      {{ "slide": 6, "type": "Board Questions", "headline": "3 Questions for the Board", "bullet": "1. What does it look like without the founder?\\n2. Where are the unlogged workarounds?\\n3. Are controls real or theatre?" }},
      {{ "slide": 7, "type": "The Resolution & CTA", "headline": "The Operator Reframe", "bullet": "How to replace paper theatre with decision hygiene. Read the full investigation." }}
    ]
  }},
  "carousel_2": {{
    "title": "Tactical Operator Framework Deck",
    "description": "7-8 slide high-dwell deck detailing the step-by-step diagnostic framework.",
    "slides": [
      {{ "slide": 1, "type": "Hook", "headline": "The [Topic] Operator Framework", "bullet": "4 steps to de-risk frontline decisions before capital is lost." }},
      {{ "slide": 2, "type": "Step 1", "headline": "Step 1: Audit the Ground Truth", "bullet": "Stop auditing what policies exist. Audit the informal workarounds on the floor." }},
      {{ "slide": 3, "type": "Step 2", "headline": "Step 2: Price the Friction Pre-Commitment", "bullet": "Measure human fatigue and key-person dependencies before signing." }},
      {{ "slide": 4, "type": "Step 3", "headline": "Step 3: Remove Key-Person Bottlenecks", "bullet": "If everything routes through one charismatic leader, it's concentration risk." }},
      {{ "slide": 5, "type": "Step 4", "headline": "Step 4: Continuous Verification Over Paper Policies", "bullet": "Replace annual sign-offs with live operational receipts." }},
      {{ "slide": 6, "type": "Diagnostic Checklist", "headline": "The Frontline Diagnostic", "bullet": "Key questions to test your organization's resilience today." }},
      {{ "slide": 7, "type": "Summary & Link", "headline": "Enlightened Self-Interest", "bullet": "Integrity is capital protection. Full guide and case study linked in bio." }}
    ]
  }},
  "research_dossier": {{
    "thesis": "The core investigative thesis",
    "unseen_tension": "Where theory breaks on reality",
    "data_points": [
      {{ "fact": "...", "source": "...", "url": "..." }}
    ],
    "quotes": ["..."],
    "citations": [
      {{ "title": "...", "url": "..." }}
    ]
  }}
}}
"""

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
payload = {
    "systemInstruction": {"parts": [{"text": system_instruction}]},
    "contents": [{"parts": [{"text": prompt}]}],
    "generationConfig": {
        "responseMimeType": "application/json",
        "temperature": 0.3,
        "maxOutputTokens": 8192
    }
}

print("[*] Dispatching request to gemini-2.5-flash...")
start_t = time.time()
resp = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=120)
dur = time.time() - start_t
print(f"[*] Response received in {dur:.2f}s with status {resp.status_code}")

if resp.status_code == 200:
    data_str = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
    parsed = json.loads(data_str)
    print("\nKeys in result:", list(parsed.keys()))
    article = parsed.get("article", "")
    words = len(article.split())
    print(f"Article word count: {words} words")
    print("Weekly posts count:", len(parsed.get("weekly_posts", [])))
    print("Carousel 1 slides count:", len(parsed.get("carousel_1", {}).get("slides", [])))
    print("Carousel 2 slides count:", len(parsed.get("carousel_2", {}).get("slides", [])))
    print("\nPreview of Article (first 300 chars):")
    print(article[:300])
else:
    print("[!] Error:", resp.text)
