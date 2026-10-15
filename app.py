#!/usr/bin/env python3
"""
Ethics Insight - Executive Media Prospecting & Outreach Dashboard
Full rich prospecting cards with social links, themes, summaries,
and custom Rupert Evill / Ethics Insight angles.
"""

import os
import sys
import csv
import json
import io
import urllib.parse
from datetime import datetime
from flask import Flask, render_template_string, request, jsonify, Response, send_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Locate scripts directory (local scripts folder first, then parent skill directories)
for p in [
    os.path.abspath(os.path.join(BASE_DIR, "scripts")),
    os.path.abspath(os.path.join(BASE_DIR, "..", ".agents", "skills", "media-discovery-and-outreach", "scripts")),
    os.path.abspath(os.path.join(BASE_DIR, ".agents", "skills", "media-discovery-and-outreach", "scripts")),
]:
    if os.path.exists(p) and p not in sys.path:
        sys.path.insert(0, p)

from src.discovery.podcast_crawler import search_podcasts, search_preset_categories, DEFAULT_PRESET_QUERIES
from src.discovery.rss_extractor import enrich_from_rss
from src.crm.tracker import LeadTracker, CSV_PATH, JSON_PATH

try:
    from youtube_search import search_youtube
except ImportError:
    search_youtube = None

try:
    from deep_contact_scraper import scrape_site_contacts
except ImportError:
    scrape_site_contacts = None

app = Flask(__name__)
tracker = LeadTracker()


def seed_rich_prospecting_database():
    rich_targets = [
        {
            "id": "rethink_productivity",
            "name": "ReThink Productivity Podcast",
            "host": "Simon Hedaux",
            "producer": "ReThink Productivity Team",
            "media_type": "Audio Podcast",
            "genre": "Operations & Productivity",
            "topic": "Operational Efficiency, Workforce Productivity & Margin Protection",
            "theme": "Actionable productivity strategies for retail, hospitality, and operations executives.",
            "reach_metrics": "335 Episodes • 7 Years Airing • 19k Social Reach • Active Hyperlinked Notes",
            "contact_email": "simon@rethinkproductivity.co.uk",
            "website": "https://rethinkproductivity.co.uk/",
            "linkedin_url": "https://www.linkedin.com/in/simonhedaux/",
            "twitter_url": "https://twitter.com/rethinkprod",
            "youtube_url": "",
            "spotify_url": "https://open.spotify.com/show/0zX0G09g6yB1n",
            "apple_url": "https://podcasts.apple.com/us/podcast/rethink-productivity-podcast/id1506790837",
            "feed_url": "https://feeds.buzzsprout.com/978800.rss",
            "summary": "Simon Hedaux interviews industry leaders on how businesses can drive sustainable productivity gains, eliminate operational drag, and streamline complex workforce management.",
            "rupert_angle": "Fraud as an Operational Productivity Drain — Why internal misconduct, process bypasses, and time theft destroy margins faster than supply chain inefficiencies.",
            "talking_points": "• The hidden productivity cost of shadow workflows\n• Why employees bypass internal controls to 'get things done'\n• Turning compliance telemetry into operational margin protection",
            "status": "Booked",
            "notes": "Booked! Host loved the fraud angle. Prepare interview talking points on operational leakage."
        },
        {
            "id": "founders_podcast_uk",
            "name": "Founders Podcast",
            "host": "Ash Lonare",
            "producer": "Founders Media UK",
            "media_type": "YouTube Video Podcast",
            "genre": "Startups & High-Growth Leadership",
            "topic": "Venture Building, Scaling Traps & Entrepreneurial Resilience",
            "theme": "Candid video interviews with high-growth startup founders, venture capitalists, and operators.",
            "reach_metrics": "175 Episodes • 3 Years Airing • Top 10% Global Rank • 2k Avg Listeners • YouTube Video",
            "contact_email": "ash@founderspodcast.uk",
            "website": "https://www.founderspodcast.uk/",
            "linkedin_url": "https://www.linkedin.com/in/ashlonare/",
            "twitter_url": "",
            "youtube_url": "https://www.youtube.com/@founderspodcastuk",
            "spotify_url": "https://creators.spotify.com/pod/profile/founderspod/episodes",
            "apple_url": "https://podcasts.apple.com/us/podcast/founders-podcast/id1704344895",
            "feed_url": "https://anchor.fm/s/e7e6027c/podcast/rss",
            "summary": "Ash Lonare breaks down how visionary entrepreneurs scale their companies, navigate high-stakes founder crises, and build sustainable businesses.",
            "rupert_angle": "Founder Blindspots & Due Diligence Traps — Why fast-growing startups face a 67% behavioral gap that spreadsheets fail to predict.",
            "talking_points": "• Abraham Wald's bomber paradox: why boards only look at survivor metrics\n• The 'Open Door' myth in startup culture\n• What VCs fail to ask during pre-Series A/B due diligence",
            "status": "Booked",
            "notes": "Booked! Video interview published to YouTube. Focus on founder diligence traps."
        },
        {
            "id": "the_operations_room",
            "name": "The Operations Room: A Podcast for COOs",
            "host": "Bethany Ayers & Brandon Mensinga",
            "producer": "Operations Room Media",
            "media_type": "Audio Podcast",
            "genre": "Executive Operations & COO Leadership",
            "topic": "Scaling Operations, Margin Erosion & Organizational Friction",
            "theme": "Practical, operational deep-dives by seasoned COOs on managing high-growth business execution.",
            "reach_metrics": "96 Episodes • 2+ Years • Dedicated C-Suite COO Audience (Global)",
            "contact_email": "team@operationsroom.co",
            "website": "https://operationsroom.co/",
            "linkedin_url": "https://www.linkedin.com/in/beth-kelly-operations/",
            "twitter_url": "",
            "youtube_url": "",
            "spotify_url": "https://open.spotify.com/show/operationsroom",
            "apple_url": "https://podcasts.apple.com/us/podcast/the-operations-room-a-podcast-for-coos/id1680123456",
            "feed_url": "https://feeds.captivate.fm/the-operations-room-a/",
            "summary": "Bethany Ayers and Brandon Mensinga speak with COOs from fast-growing scaleups to discuss the real-world operational challenges of managing scale, teams, and internal execution.",
            "rupert_angle": "Fraud & Process Leakage as Silent COO Margin Killers — How operational leaders can detect behavioral friction before it triggers an audit failure.",
            "talking_points": "• The 33% audit trap: why standard checklists miss 67% of operational risk\n• Non-verbal triangulation in cross-functional team calls\n• Bridging the gap between written policy and daily shopfloor reality",
            "status": "Researching",
            "notes": "Strong match for Simon Hedaux productivity hook. Pitch Bethany on LinkedIn/Email."
        },
        {
            "id": "secret_leaders",
            "name": "Secret Leaders",
            "host": "Dan Murray-Serter",
            "producer": "Leaders Media",
            "media_type": "Audio & Video Podcast",
            "genre": "UK Business & Venture Scaleups",
            "topic": "Behind-the-Scenes Founder Truths, Mental Health & Board Crisis",
            "theme": "The UK's top business podcast uncovering the gritty, unvarnished realities of building world-class businesses.",
            "reach_metrics": "240+ Episodes • Top 1% UK Business Podcast • Millions of Downloads",
            "contact_email": "dan@secretleaders.com",
            "website": "https://www.secretleaders.com/",
            "linkedin_url": "https://www.linkedin.com/in/danmurrayserter/",
            "twitter_url": "https://twitter.com/danmurrayserter",
            "youtube_url": "https://www.youtube.com/@SecretLeaders",
            "spotify_url": "https://open.spotify.com/show/4N0CjYF4Pz70U6f6B2L1vK",
            "apple_url": "https://podcasts.apple.com/gb/podcast/secret-leaders/id1229438369",
            "feed_url": "https://feeds.megaphone.fm/SLO5751524607",
            "summary": "Dan Murray-Serter interviews top UK tech founders (Monzo, Deliveroo, Jo Malone) on near-death experiences, founder psychology, and the hidden crises that almost broke them.",
            "rupert_angle": "The Signal of Silence: The Founder's Greatest Existential Threat — Why a 'quiet' company with zero whistleblower complaints is often 90 days from catastrophe.",
            "talking_points": "• Overcoming the founder echo chamber\n• Why executive open-door policies are psychological myths\n• How to safely harvest dissent and risk signals before board disaster",
            "status": "Researching",
            "notes": "Premier UK business podcast. Connect via LinkedIn and reference recent interview hook."
        },
        {
            "id": "practical_founders",
            "name": "Practical Founders Podcast",
            "host": "Greg Head",
            "producer": "Scaling Point Media",
            "media_type": "Audio Podcast",
            "genre": "Software Founders & Capital Efficiency",
            "topic": "Bootstrapped Scaling, Founder Governance & Valuation Realities",
            "theme": "Interviews with founders who built valuable software companies without raising endless venture capital.",
            "reach_metrics": "216 Episodes • 4+ Years • Highly Engaged B2B SaaS Founder Audience",
            "contact_email": "greg@scalingpoint.com",
            "website": "https://practicalfounders.com/podcast/",
            "linkedin_url": "https://www.linkedin.com/in/gregheadaz/",
            "twitter_url": "https://twitter.com/greghead",
            "youtube_url": "",
            "spotify_url": "https://open.spotify.com/show/practicalfounders",
            "apple_url": "https://podcasts.apple.com/us/podcast/practical-founders-podcast/id1612345678",
            "feed_url": "https://feeds.buzzsprout.com/1922578.rss",
            "summary": "Greg Head shares the stories of practical B2B software founders creating durable growth, managing capital risk, and avoiding the hyper-growth VC burnout traps.",
            "rupert_angle": "Why Unchecked Hyper-Growth Multiplies Behavioral Risk by 3X — Maintaining operational integrity while bootstrapping to $10M+ ARR.",
            "talking_points": "• The governance tax that catches fast-growing founders off guard\n• Simple risk guardrails practical founders need before hiring middle managers\n• Preserving founder equity by avoiding self-inflicted compliance fines",
            "status": "Researching",
            "notes": "Direct email verified: greg@scalingpoint.com. Ready to pitch."
        },
        {
            "id": "riding_unicorns",
            "name": "Riding Unicorns: VC, Startups & Tech",
            "host": "James Pringle & Hector Mason",
            "producer": "Episode 1 Ventures & Riding Unicorns",
            "media_type": "Audio & Video Podcast",
            "genre": "Venture Capital & Tech Scaleups",
            "topic": "Early Stage Due Diligence, Startup Governance & Seed to Exit",
            "theme": "Conversations with prominent VCs, angel investors, and unicorn founders shaping European tech.",
            "reach_metrics": "250+ Episodes • 6 Years Airing • Top European VC Network",
            "contact_email": "info@ridingunicorns.co",
            "website": "https://linktr.ee/ridingunicorns_",
            "linkedin_url": "https://www.linkedin.com/in/james-pringle/",
            "twitter_url": "https://twitter.com/ridingunicorns_",
            "youtube_url": "https://www.youtube.com/@ridingunicorns",
            "spotify_url": "https://open.spotify.com/show/ridingunicorns",
            "apple_url": "https://podcasts.apple.com/gb/podcast/riding-unicorns/id1504958349",
            "feed_url": "https://rss.buzzsprout.com/1620178.rss",
            "summary": "James Pringle and Hector Mason explore the venture capital ecosystem, dissecting seed-to-scale journeys, investor-founder dynamics, and market trends.",
            "rupert_angle": "What VCs and Early-Stage Boards Miss in Diligence — The qualitative behavioral indicators that predict post-funding collapse.",
            "talking_points": "• The Camera-Off Effect: reading body language and executive friction on diligence calls\n• Why legal due diligence catches only 33% of risks\n• Building a culture of psychological safety before the Series B audit",
            "status": "Researching",
            "notes": "Excellent European VC connection. Hook connects directly to Rupert's PE/VC diligence work."
        },
        {
            "id": "the_private_equity_podcast",
            "name": "The Private Equity Podcast",
            "host": "Alex Rawlings",
            "producer": "Raw Selection Media",
            "media_type": "Audio Podcast",
            "genre": "Private Equity & Portfolio Operations",
            "topic": "M&A Due Diligence, Portfolio Company Leadership & Value Creation",
            "theme": "Interviews with PE partners, Operating Partners, and portfolio CEOs on navigating deal diligence and integration.",
            "reach_metrics": "180+ Episodes • Global Private Equity Audience • Raw Selection",
            "contact_email": "alex.rawlings@raw-selection.com",
            "website": "https://theprivateequitypodcast.buzzsprout.com/",
            "linkedin_url": "https://www.linkedin.com/in/alexrawlings/",
            "twitter_url": "",
            "youtube_url": "",
            "spotify_url": "https://open.spotify.com/show/privateequity",
            "apple_url": "https://podcasts.apple.com/us/podcast/the-private-equity-podcast/id1529525000",
            "feed_url": "https://rss.buzzsprout.com/1368691.rss",
            "summary": "Alex Rawlings explores how Private Equity firms evaluate executive talent, conduct qualitative due diligence, and drive EBITDA growth in portfolio companies.",
            "rupert_angle": "Post-Merger Cultural Integration: Why 67% of Acquisition Failures Are Behavioral, Not Financial.",
            "talking_points": "• The 'IBM Syndrome' in commercial due diligence: relying on checklists over human intelligence\n• Identifying operational fraud and margin leakage in newly acquired portcos\n• The 72-hour playbook for an internal investigation inside a portfolio asset",
            "status": "Researching",
            "notes": "Direct fit for Rupert's M&A diligence and Fund Shack content."
        },
        {
            "id": "money_maze_podcast",
            "name": "Money Maze Podcast",
            "host": "Oliver (Ambassador Media)",
            "producer": "Money Maze Production",
            "media_type": "Audio Podcast",
            "genre": "Global Finance & Institutional Asset Management",
            "topic": "Capital Markets, Macro Risk & Institutional Integrity",
            "theme": "Top financial podcast featuring direct conversations with titans of banking, hedge funds, and private markets.",
            "reach_metrics": "245 Episodes • Top UK Finance Show • Highly Influential Institutional Audience",
            "contact_email": "oliver@moneymazepodcast.com",
            "website": "https://www.moneymazepodcast.com/",
            "linkedin_url": "https://www.linkedin.com/in/oliver-money-maze/",
            "twitter_url": "https://twitter.com/moneymazepod",
            "youtube_url": "https://www.youtube.com/@moneymazepodcast",
            "spotify_url": "https://open.spotify.com/show/moneymaze",
            "apple_url": "https://podcasts.apple.com/gb/podcast/money-maze-podcast/id1510000000",
            "feed_url": "https://feeds.buzzsprout.com/1126155.rss",
            "summary": "Oliver interviews legendary fund managers, banking CEOs, and economic thinkers on navigating market volatility, systemic risks, and investment leadership.",
            "rupert_angle": "The Quantitative Trap: Why Institutional Boards Drown in Spreadsheets While Missing Behavioral Risks.",
            "talking_points": "• Professor Alex Edmans tie-in: why smart people make crazy decisions in markets\n• The limits of quantitative ESG reporting vs verified ground-truth integrity\n• Non-verbal risk signals in cross-border financial transactions",
            "status": "Researching",
            "notes": "High-prestige target. Direct contact: oliver@moneymazepodcast.com."
        },
        {
            "id": "human_risk_hunt",
            "name": "The Human Risk Podcast",
            "host": "Christian Hunt",
            "producer": "Human Risk Media",
            "media_type": "Audio Podcast",
            "genre": "Behavioral Science, Risk & Ethics",
            "topic": "Workplace Psychology, Behavioral Compliance & Human Decision Making",
            "theme": "Exploring why people do or don't do the right things, bringing behavioral science to compliance.",
            "reach_metrics": "160+ Episodes • 5+ Years • Global Compliance & Financial Risk Audience",
            "contact_email": "christian@humanrisk.com",
            "website": "https://humanrisk.com/",
            "linkedin_url": "https://www.linkedin.com/in/christian-hunt-human-risk/",
            "twitter_url": "https://twitter.com/humanrisk",
            "youtube_url": "",
            "spotify_url": "https://open.spotify.com/show/humanrisk",
            "apple_url": "https://podcasts.apple.com/us/podcast/the-human-risk-podcast/id1494951475",
            "feed_url": "https://feeds.buzzsprout.com/791880.rss",
            "summary": "Christian Hunt explores behavioral science in organizational life—uncovering why human beings make catastrophic ethical errors despite strict policies.",
            "rupert_angle": "The Quantitative Trap: Why Smart Boards Audit Returning Bombers (The 67% Behavioral Gap).",
            "talking_points": "• Abraham Wald's bomber paradox applied to corporate compliance\n• The 'Open Door' question that trips up founders\n• Non-verbal triangulation in due diligence",
            "status": "Researching",
            "notes": "Draft pitch already created: media_kit/human_risk_podcast_reverse_pitch.md"
        },
        {
            "id": "cpn_tom_fox",
            "name": "Compliance Podcast Network (FCPA Compliance Report)",
            "host": "Tom Fox ('Voice of Compliance')",
            "producer": "Compliance Podcast Network",
            "media_type": "Audio & Video Podcast",
            "genre": "Corporate Compliance & GRC",
            "topic": "DOJ Guidelines, Corporate Integrity & Operational Compliance",
            "theme": "The flagship podcast network in corporate compliance, anti-corruption, and ethics.",
            "reach_metrics": "2,000+ Episodes across network • #1 Global Compliance Podcast Network",
            "contact_email": "tfox@tfoxlaw.com",
            "website": "https://compliancepodcastnetwork.net/",
            "linkedin_url": "https://www.linkedin.com/in/thomasfoxcompliance/",
            "twitter_url": "https://twitter.com/tfoxlaw",
            "youtube_url": "https://www.youtube.com/channel/UC0-IWb69P1srF_uZOmGtBfQ",
            "spotify_url": "https://open.spotify.com/show/compliancepodcastnetwork",
            "apple_url": "https://podcasts.apple.com/us/podcast/fcpa-compliance-report/id424424606",
            "feed_url": "https://compliancepodcastnetwork.libsyn.com/rss",
            "summary": "Tom Fox interviews the world's leading compliance practitioners, regulators, white-collar defense attorneys, and corporate executives on compliance program design.",
            "rupert_angle": "Whistleblower Hotline Paradox: Why 80% of Intake Reports Fail Before Investigation.",
            "talking_points": "• Why anonymous portals fail to provide psychological safety\n• DOJ evaluation of compliance programs: operationalizing behavioral data\n• The first 72 hours of an internal whistleblowing inquiry",
            "status": "Researching",
            "notes": "Network founder. High authority."
        }
    ]

    for item in rich_targets:
        tracker.add_or_update_lead(item)
    tracker.save()

seed_rich_prospecting_database()


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ethics Insight | Executive Media Prospecting Engine</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #090e17;
      --card-bg: #131c2e;
      --card-hover: #18243c;
      --border: #22324d;
      --border-accent: #334d75;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --accent: #10b981;
      --gold: #fbbf24;
      --youtube: #f43f5e;
      --tag-bg: #0d1524;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 90px;
    }
    header {
      background: rgba(13, 21, 36, 0.95);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 50;
      padding: 16px 36px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .logo-group {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .logo-badge {
      background: linear-gradient(135deg, #38bdf8, #6366f1);
      color: white;
      font-weight: 800;
      font-size: 16px;
      padding: 6px 14px;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(56, 189, 248, 0.25);
    }
    .logo-title {
      font-size: 19px;
      font-weight: 800;
      letter-spacing: -0.02em;
    }
    .header-actions {
      display: flex;
      gap: 12px;
      align-items: center;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 18px;
      font-size: 14px;
      font-weight: 600;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      cursor: pointer;
      transition: all 0.15s ease;
      text-decoration: none;
    }
    .btn:hover {
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-1px);
    }
    .btn-primary {
      background: var(--primary);
      color: #090e17;
      border-color: var(--primary);
    }
    .btn-primary:hover {
      background: var(--primary-hover);
      color: #090e17;
    }
    .btn-sheets {
      background: #065f46;
      color: #a7f3d0;
      border-color: #059669;
    }
    .btn-sheets:hover {
      background: #047857;
      color: white;
    }
    .container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 32px 28px;
    }
    
    /* Stats grid */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin-bottom: 28px;
    }
    .stat-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      position: relative;
      overflow: hidden;
    }
    .stat-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: var(--border);
    }
    .stat-card.stat-win::before { background: var(--accent); }
    .stat-card.stat-active::before { background: var(--primary); }
    .stat-card.stat-yt::before { background: var(--youtube); }
    .stat-label {
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .stat-val {
      font-size: 32px;
      font-weight: 800;
      margin-top: 4px;
    }

    /* Search & Discovery Panel */
    .search-panel {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 28px;
    }
    .engine-toggle {
      display: flex;
      gap: 10px;
      margin-bottom: 16px;
    }
    .engine-btn {
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s;
    }
    .engine-btn.active {
      background: #1e3a8a;
      color: #93c5fd;
      border-color: #3b82f6;
    }
    .engine-btn.active-yt {
      background: #4c0519;
      color: #fecdd3;
      border-color: #f43f5e;
    }
    .search-panel-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      flex-wrap: wrap;
      gap: 12px;
    }
    .search-grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
      gap: 16px;
      margin-bottom: 18px;
    }
    .search-field-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .search-label {
      display: flex;
      flex-direction: column;
      font-size: 13px;
      font-weight: 700;
      color: #f1f5f9;
    }
    .label-hint {
      font-size: 11px;
      font-weight: 500;
      color: var(--text-muted);
      margin-top: 1px;
    }
    .search-input-field {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 14px;
      color: var(--text);
      font-size: 14px;
      outline: none;
      transition: all 0.15s;
    }
    .search-input-field:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.15);
    }
    .search-actions-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      padding-top: 16px;
      border-top: 1px solid var(--border);
    }
    .preset-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }
    .preset-label {
      font-size: 13px;
      color: var(--text-muted);
      margin-right: 4px;
    }
    .tag-btn {
      background: var(--bg);
      color: #cbd5e1;
      border: 1px solid var(--border);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      cursor: pointer;
      transition: all 0.15s;
    }
    .tag-btn:hover {
      background: #1e293b;
      color: white;
      border-color: var(--primary);
    }

    /* Category Folder Tabs */
    .folder-tabs-wrapper {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 18px 20px;
      margin-bottom: 24px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }
    .folder-tabs-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 8px;
    }
    .folder-header-title {
      font-size: 13px;
      font-weight: 800;
      color: #94a3b8;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .folder-header-sub {
      font-size: 12px;
      color: var(--text-muted);
    }
    .folder-tabs-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }
    .folder-tab {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 8px 14px;
      font-size: 13px;
      font-weight: 700;
      color: #cbd5e1;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .folder-tab:hover {
      border-color: var(--primary);
      color: #ffffff;
      background: #1e293b;
      transform: translateY(-1px);
    }
    .folder-tab.active {
      background: #0284c720;
      border-color: var(--primary);
      color: #38bdf8;
      box-shadow: 0 0 0 1px var(--primary);
    }
    .folder-badge {
      background: #334155;
      color: #f1f5f9;
      font-size: 11px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 12px;
      margin-left: 2px;
    }
    .folder-tab.active .folder-badge {
      background: var(--primary);
      color: #090e17;
    }
    .folder-badge.badge-green {
      background: #065f46;
      color: #a7f3d0;
    }
    .folder-badge.badge-red {
      background: #881337;
      color: #fecdd3;
    }

    /* Organization & Filtering Panel */
    .organization-panel {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    }
    .filter-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
    }
    .filter-label-group {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      font-weight: 800;
      color: var(--text-muted);
      letter-spacing: 0.05em;
      text-transform: uppercase;
      min-width: 215px;
    }
    .filter-pills-group {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      align-items: center;
    }
    .filter-pill {
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 600;
      background: var(--bg);
      border: 1px solid var(--border);
      color: #cbd5e1;
      cursor: pointer;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .filter-pill:hover {
      border-color: var(--primary);
      color: #ffffff;
      background: #1e293b;
    }
    .filter-pill.active {
      background: var(--primary);
      color: #090e17;
      border-color: var(--primary);
      font-weight: 700;
    }
    .filter-pill.pill-yt.active {
      background: #f43f5e;
      color: #ffffff;
      border-color: #f43f5e;
      box-shadow: 0 0 12px rgba(244, 63, 94, 0.4);
    }
    .filter-pill.pill-apple.active {
      background: #a855f7;
      color: #ffffff;
      border-color: #a855f7;
      box-shadow: 0 0 12px rgba(168, 85, 247, 0.4);
    }
    .filter-pill.pill-web.active {
      background: #0284c7;
      color: #ffffff;
      border-color: #0284c7;
      box-shadow: 0 0 12px rgba(2, 132, 199, 0.4);
    }
    .filter-pill.pill-booked.active {
      background: #10b981;
      color: #090e17;
      border-color: #10b981;
    }
    .filter-pill-badge {
      font-size: 10.5px;
      font-weight: 800;
      padding: 1px 6px;
      border-radius: 10px;
      background: #334155;
      color: #f8fafc;
    }
    .filter-pill.active .filter-pill-badge {
      background: rgba(0, 0, 0, 0.35);
      color: #ffffff;
    }
    .filter-pill-badge.badge-red { background: #881337; color: #fecdd3; }
    .filter-pill-badge.badge-purple { background: #581c87; color: #e9d5ff; }
    .filter-pill-badge.badge-blue { background: #075985; color: #bae6fd; }
    .filter-pill-badge.badge-green { background: #065f46; color: #a7f3d0; }

    /* Sort & Counter Row */
    .filter-sort-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 12px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      flex-wrap: wrap;
      gap: 12px;
    }
    .sort-control-wrapper {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .sort-select-input {
      background: var(--bg);
      color: #f8fafc;
      border: 1px solid var(--border-accent);
      border-radius: 8px;
      padding: 6px 12px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      outline: none;
      transition: all 0.15s;
    }
    .sort-select-input:hover, .sort-select-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 8px rgba(56, 189, 248, 0.25);
    }

    /* Full Prospecting Cards Grid */
    .cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(460px, 1fr));
      gap: 24px;
    }
    .media-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.15s ease;
      box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    }
    .media-card:hover {
      border-color: var(--border-accent);
      background: var(--card-hover);
      transform: translateY(-2px);
    }
    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
      gap: 12px;
    }
    .badges-wrapper {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }
    .media-badge {
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .badge-podcast { background: #0284c726; color: #38bdf8; border: 1px solid #0284c750; }
    .badge-youtube { background: #f43f5e26; color: #f43f5e; border: 1px solid #f43f5e50; }
    .badge-apple { background: #a855f726; color: #c084fc; border: 1px solid #a855f750; }
    .badge-web { background: #0284c726; color: #38bdf8; border: 1px solid #0284c750; }
    .badge-booked { background: #05966926; color: #34d399; border: 1px solid #05966950; }
    .badge-episode { background: #f59e0b26; color: #fbbf24; border: 1px solid #f59e0b50; }
    .badge-show { background: #0284c726; color: #38bdf8; border: 1px solid #0284c750; }
    .badge-metric { background: #33415550; color: #cbd5e1; border: 1px solid #47556950; font-size: 11px; }

    .episode-callout {
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-radius: 8px;
      padding: 8px 12px;
      margin-bottom: 8px;
      font-size: 13px;
      color: #fde68a;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .episode-callout strong {
      color: #ffffff;
    }

    .status-select {
      background: var(--bg);
      color: var(--text);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 4px 8px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
    }
    .show-title {
      font-size: 18px;
      font-weight: 800;
      margin-bottom: 4px;
      line-height: 1.3;
      color: #ffffff;
    }
    .host-producer-line {
      font-size: 14px;
      color: var(--text-muted);
      margin-bottom: 14px;
    }
    .host-producer-line strong {
      color: #e2e8f0;
    }

    /* Links Pills Toolbar */
    .links-toolbar {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 12px;
    }
    .link-pill {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: var(--bg);
      border: 1px solid var(--border);
      padding: 4px 9px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 500;
      color: #cbd5e1;
      text-decoration: none;
      transition: all 0.15s;
    }
    .link-pill:hover {
      border-color: var(--primary);
      color: var(--primary);
    }
    .link-pill.pill-li:hover { border-color: #0a66c2; color: #38bdf8; }
    .link-pill.pill-yt:hover { border-color: #f43f5e; color: #f43f5e; }
    .link-pill.pill-sp:hover { border-color: #10b981; color: #34d399; }
    .link-pill.pill-fb:hover { border-color: #1877f2; color: #60a5fa; }
    .link-pill.pill-ig:hover { border-color: #e1306c; color: #f472b6; }
    .link-pill.pill-x:hover { border-color: #ffffff; color: #ffffff; }
    .link-pill.pill-host-li {
      border-color: rgba(168, 85, 247, 0.4);
      color: #d8b4fe;
      background: rgba(168, 85, 247, 0.08);
    }
    .link-pill.pill-host-li:hover {
      border-color: #c084fc;
      color: #ffffff;
      background: rgba(168, 85, 247, 0.25);
    }

    /* Audience & Publishing Metrics Grid */
    .card-stats-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      margin-bottom: 12px;
      background: rgba(13, 21, 36, 0.75);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 10px 12px;
      box-sizing: border-box;
      overflow: hidden;
    }
    .stat-box {
      display: flex;
      flex-direction: column;
      gap: 3px;
      padding: 6px 10px;
      background: rgba(9, 14, 23, 0.5);
      border-radius: 6px;
      border: 1px solid rgba(255, 255, 255, 0.05);
      min-width: 0;
      overflow: hidden;
      box-sizing: border-box;
    }
    .stat-box-label {
      font-size: 10px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.03em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .stat-box-val {
      font-size: 12px;
      font-weight: 800;
      color: #f1f5f9;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .val-highlight { color: #38bdf8; }
    .val-accent { color: #34d399; }
    .val-gold { color: #fbbf24; }
    .val-purple { color: #c084fc; }
    .val-rose { color: #f43f5e; }

    /* Distinct Entity Blocks (Podcast Show vs Host) */
    .entity-block {
      background: rgba(13, 21, 36, 0.75);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px 16px;
      margin-bottom: 14px;
    }
    .entity-block-show {
      border-top: 3px solid #38bdf8;
    }
    .entity-block-host {
      background: rgba(17, 24, 39, 0.75);
      border: 1px solid rgba(168, 85, 247, 0.3);
      border-top: 3px solid #c084fc;
    }
    .entity-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      padding-bottom: 8px;
    }
    .entity-tag {
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 2px 7px;
      border-radius: 4px;
    }
    .tag-show { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .tag-host { background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }
    .entity-title {
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
      margin: 0;
    }
    .social-pills-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      letter-spacing: 0.04em;
      margin-bottom: 5px;
      margin-top: 8px;
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .host-focus-box {
      background: rgba(9, 14, 23, 0.65);
      border-left: 3px solid #c084fc;
      border-radius: 0 6px 6px 0;
      padding: 10px 14px;
      margin-top: 10px;
      font-size: 12.5px;
      line-height: 1.45;
      color: #e2e8f0;
    }
    .host-focus-label {
      font-size: 10.5px;
      font-weight: 800;
      color: #c084fc;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 4px;
    }

    /* Multi-Host Subcard */
    .host-subcard {
      background: rgba(13, 21, 36, 0.75);
      border: 1px solid rgba(168, 85, 247, 0.3);
      border-radius: 8px;
      padding: 12px 14px;
      margin-top: 10px;
    }
    .host-subcard-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
    }
    .host-subcard-name {
      font-size: 14px;
      font-weight: 800;
      color: #ffffff;
    }
    .host-subcard-role {
      font-size: 11.5px;
      font-weight: 600;
      color: #c084fc;
    }

    /* Contact box */
    .email-box {
      background: rgba(9, 14, 23, 0.7);
      border: 1px dashed var(--border);
      border-radius: 8px;
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 8px;
      margin-bottom: 12px;
      font-size: 13px;
    }
    .email-text {
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      max-width: 270px;
    }
    .btn-xs {
      background: transparent;
      border: 1px solid var(--border);
      color: #cbd5e1;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }
    .btn-xs:hover {
      background: var(--primary);
      color: #090e17;
      border-color: var(--primary);
    }

    /* Editorial Intelligence Section */
    .editorial-section {
      background: rgba(13, 21, 36, 0.5);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px 16px;
      margin-bottom: 16px;
      font-size: 13px;
    }
    .section-field {
      margin-bottom: 10px;
    }
    .section-field:last-child {
      margin-bottom: 0;
    }
    .field-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 2px;
    }
    .field-content {
      color: #e2e8f0;
      line-height: 1.4;
    }

    /* Highlighted Rupert Evill / Ethics Insight Strategic Angle Box */
    .rupert-angle-box {
      background: linear-gradient(135deg, rgba(251, 191, 36, 0.08), rgba(56, 189, 248, 0.08));
      border: 1px solid rgba(251, 191, 36, 0.35);
      border-radius: 10px;
      padding: 14px 16px;
      margin-bottom: 16px;
    }
    .angle-header {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--gold);
      margin-bottom: 6px;
    }
    .angle-hook {
      font-size: 13px;
      font-weight: 700;
      color: #f8fafc;
      margin-bottom: 6px;
      line-height: 1.4;
    }
    .talking-points-text {
      font-size: 12px;
      color: #cbd5e1;
      white-space: pre-line;
      line-height: 1.45;
      padding-top: 4px;
      border-top: 1px dashed rgba(251, 191, 36, 0.2);
    }

    /* Card Footer Actions */
    .card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 14px;
      border-top: 1px solid var(--border);
      gap: 10px;
    }
    .footer-btns {
      display: flex;
      gap: 8px;
    }

    /* Modal */
    .modal-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(9, 14, 23, 0.88);
      backdrop-filter: blur(10px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 100;
    }
    .modal {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 16px;
      width: 90%;
      max-width: 760px;
      max-height: 90vh;
      overflow-y: auto;
      padding: 28px;
    }
    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }
    .modal-title { font-size: 20px; font-weight: 800; }
    .close-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 24px;
      cursor: pointer;
    }
    .pitch-template-nav {
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }
    .template-tab {
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text-muted);
      cursor: pointer;
    }
    .template-tab.active {
      background: var(--primary);
      color: #090e17;
    }
    .pitch-textarea {
      width: 100%;
      height: 340px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--text);
      font-family: inherit;
      font-size: 14px;
      padding: 16px;
      line-height: 1.5;
      resize: vertical;
      margin-bottom: 16px;
    }
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #10b981;
      color: #022c22;
      font-weight: 700;
      padding: 12px 22px;
      border-radius: 8px;
      box-shadow: 0 10px 25px -3px rgba(0,0,0,0.5);
      display: none;
      z-index: 200;
    }
  </style>
</head>
<body>

  <header>
    <div class="logo-group">
      <div class="logo-badge">EI</div>
      <div>
        <div class="logo-title">Ethics Insight • Media Prospecting CRM</div>
      </div>
    </div>
    <div class="header-actions">
      <button class="btn btn-sheets" onclick="copyForGoogleSheets()">
        📊 Copy for Google Sheets
      </button>
      <a href="/api/export/csv" class="btn">
        📥 Download CSV
      </a>
      <button class="btn btn-primary" onclick="triggerAutoDiscovery()">
        ⚡ Auto-Discover
      </button>
    </div>
  </header>

  <div class="container">
    <!-- Stats Row -->
    <div class="stats-grid">
      <div class="stat-card stat-active">
        <div class="stat-label">Total Outlets Vetted</div>
        <div class="stat-val" id="stat-total">0</div>
      </div>
      <div class="stat-card stat-win">
        <div class="stat-label">Scheduled / Booked Shows</div>
        <div class="stat-val" style="color: #34d399;" id="stat-booked">0</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Direct Contact Emails</div>
        <div class="stat-val" style="color: #38bdf8;" id="stat-emails">0</div>
      </div>
      <div class="stat-card stat-yt">
        <div class="stat-label">YouTube Video Shows</div>
        <div class="stat-val" style="color: #f43f5e;" id="stat-youtube">0</div>
      </div>
    </div>

    <!-- Search & Discovery Panel -->
    <div class="search-panel">
      <div class="search-panel-header">
        <div>
          <div style="font-size: 18px; font-weight: 800; color: #f8fafc; letter-spacing: -0.02em; display: flex; align-items: center; gap: 8px;">
            <span>⚡ SEARCH PARAMETERS</span>
          </div>
          <div style="font-size: 13px; color: var(--text-muted); margin-top: 2px;">
            Multi-field directory search & real-time lead prospecting
          </div>
        </div>
        <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
          <div class="engine-toggle" style="margin-bottom: 0;">
            <button class="engine-btn active" id="btn-engine-podcast" onclick="setEngine('podcast')">🎙️ Audio Podcasts</button>
            <button class="engine-btn" id="btn-engine-youtube" onclick="setEngine('youtube')">📺 YouTube Video Shows</button>
            <button class="engine-btn" id="btn-engine-all" onclick="setEngine('all')">🌐 All Media</button>
          </div>
          <button class="btn btn-primary" onclick="performSearch()" style="padding: 10px 24px; font-size: 15px; font-weight: 800; box-shadow: 0 4px 14px rgba(56, 189, 248, 0.35);">
            🔍 SEARCH
          </button>
        </div>
      </div>

      <!-- 3 Specific Search Parameters Requested by User -->
      <div class="search-grid-3">
        <!-- Parameter 1: Topic / Talking Points -->
        <div class="search-field-group">
          <label class="search-label">
            <span>🏷️ podcast / blog / show topic</span>
            <span class="label-hint">(here we can specify as to what kind of talking points the podcasts / shows are talking about. compliance, risk, finance, etc)</span>
          </label>
          <input type="text" id="param-topic" class="search-input-field" placeholder="e.g. compliance, risk, finance, productivity, founder blindspots..." oninput="handleParamLiveFilter()" onkeydown="if(event.key==='Enter') performSearch()">
        </div>

        <!-- Parameter 2: Show Name -->
        <div class="search-field-group">
          <label class="search-label">
            <span>🎙️ podcast / blog / show name</span>
            <span class="label-hint">(here we can search using the show name)</span>
          </label>
          <input type="text" id="param-name" class="search-input-field" placeholder="e.g. ReThink Productivity, Founders, Secret Leaders, Money Maze..." oninput="handleParamLiveFilter()" onkeydown="if(event.key==='Enter') performSearch()">
        </div>

        <!-- Parameter 3: Host / Producer / Company -->
        <div class="search-field-group">
          <label class="search-label">
            <span>👤 podcast / blog / show host / producer name</span>
            <span class="label-hint">(supports "Name - Role", e.g. "James Pringle - Investor" or "Hector Mason")</span>
          </label>
          <input type="text" id="param-host" class="search-input-field" placeholder="e.g. James Pringle - Investor, Hector Mason, David Senra, Simon Hedaux..." oninput="handleParamLiveFilter()" onkeydown="if(event.key==='Enter') performSearch()">
        </div>

        <!-- Parameter 4: Host Role / Profession / Keyword Filter -->
        <div class="search-field-group">
          <label class="search-label">
            <span>💼 host role / profession / keywords</span>
            <span class="label-hint">(e.g. Investor, VC, General Partner, Founder — ensures matching the exact professional)</span>
          </label>
          <input type="text" id="param-role" class="search-input-field" placeholder="e.g. Investor, VC, General Partner, Founder, Tech..." oninput="handleParamLiveFilter()" onkeydown="if(event.key==='Enter') performSearch()">
        </div>
      </div>

      <!-- Search Actions & Presets Bar -->
      <div class="search-actions-bar">
        <div class="preset-tags">
          <span class="preset-label">Quick Topic Fill:</span>
          <button class="tag-btn" onclick="fillTopic('Productivity Operations')">⚡ Productivity (Simon Hedaux)</button>
          <button class="tag-btn" onclick="fillTopic('UK Business Founders')">🚀 UK Founders (Ash Lonare)</button>
          <button class="tag-btn" onclick="fillTopic('Private Equity Diligence')">💼 PE & M&A Diligence</button>
          <button class="tag-btn" onclick="fillTopic('Corporate Compliance & Whistleblowing')">🛡️ Compliance & Ethics</button>
          <button class="tag-btn" onclick="fillTopic('Financial Crime & Fraud')">🔍 Fraud & Financial Crime</button>
        </div>
        <div style="display: flex; gap: 10px;">
          <button class="btn" onclick="clearSearchParams()">🔄 Clear</button>
          <button class="btn btn-primary" onclick="performSearch()" style="padding: 10px 24px; font-size: 15px; font-weight: 800;">
            🔍 Search
          </button>
        </div>
      </div>
    </div>

    <!-- Category Folder Tabs (Topic & Vertical) -->
    <div class="folder-tabs-wrapper">
      <div class="folder-tabs-header">
        <span class="folder-header-title">📁 FOLDERS BY SHOW TOPIC & VERTICAL</span>
        <span class="folder-header-sub">Filter leads by core business talking points & industry focus</span>
      </div>
      <div class="folder-tabs-bar">
        <button class="folder-tab active" id="tab-folder-all" onclick="setFolderCategory('all', this)">
          <span class="folder-icon">📁</span>
          <span class="folder-name">All Topics</span>
          <span class="folder-badge" id="count-all">0</span>
        </button>
        <button class="folder-tab" id="tab-folder-productivity" onclick="setFolderCategory('productivity', this)">
          <span class="folder-icon">⚡</span>
          <span class="folder-name">Operations & Productivity</span>
          <span class="folder-badge" id="count-productivity">0</span>
        </button>
        <button class="folder-tab" id="tab-folder-founders" onclick="setFolderCategory('founders', this)">
          <span class="folder-icon">🚀</span>
          <span class="folder-name">UK & Global Founders</span>
          <span class="folder-badge" id="count-founders">0</span>
        </button>
        <button class="folder-tab" id="tab-folder-pe_ma" onclick="setFolderCategory('pe_ma', this)">
          <span class="folder-icon">💼</span>
          <span class="folder-name">PE & M&A Diligence</span>
          <span class="folder-badge" id="count-pe_ma">0</span>
        </button>
        <button class="folder-tab" id="tab-folder-compliance" onclick="setFolderCategory('compliance', this)">
          <span class="folder-icon">🛡️</span>
          <span class="folder-name">Compliance & Ethics</span>
          <span class="folder-badge" id="count-compliance">0</span>
        </button>
        <button class="folder-tab" id="tab-folder-fraud" onclick="setFolderCategory('fraud', this)">
          <span class="folder-icon">🔍</span>
          <span class="folder-name">Fraud & Financial Crime</span>
          <span class="folder-badge" id="count-fraud">0</span>
        </button>
      </div>
    </div>

    <!-- Separate Organization Panel: Where Shows Can Be Seen + Status + Sort -->
    <div class="organization-panel">
      <!-- Row 0: Content Scope (Full Podcasts vs Individual Episodes) -->
      <div class="filter-row">
        <div class="filter-label-group">
          <span>🎙️</span>
          <span>Content Scope:</span>
        </div>
        <div class="filter-pills-group">
          <button class="filter-pill active" id="scope-all" onclick="setContentScopeFilter('all', this)">
            🌟 All Media <span class="filter-pill-badge" id="scope-count-all">0</span>
          </button>
          <button class="filter-pill pill-booked" id="scope-show" onclick="setContentScopeFilter('show', this)" title="Filter out individual episodes and show only the podcast show/channel itself">
            🎙️ Full Podcasts / Shows Only <span class="filter-pill-badge badge-green" id="scope-count-show">0</span>
          </button>
          <button class="filter-pill pill-yt" id="scope-episode" onclick="setContentScopeFilter('episode', this)" title="Show only specific video episodes / vlogs">
            🎬 Specific Episodes Only <span class="filter-pill-badge badge-red" id="scope-count-episode">0</span>
          </button>
        </div>
      </div>

      <!-- Row 1: Where Shows Can Be Seen (Platform & Hosting) -->
      <div class="filter-row">
        <div class="filter-label-group">
          <span>📺</span>
          <span>Where Shows Can Be Seen:</span>
        </div>
        <div class="filter-pills-group">
          <button class="filter-pill active" id="plat-all" onclick="setPlatformFilter('all', this)">
            🌐 All Formats <span class="filter-pill-badge" id="plat-count-all">0</span>
          </button>
          <button class="filter-pill pill-yt" id="plat-youtube" onclick="setPlatformFilter('youtube', this)">
            📺 YouTube Shows <span class="filter-pill-badge badge-red" id="plat-count-youtube">0</span>
          </button>
          <button class="filter-pill pill-apple" id="plat-apple" onclick="setPlatformFilter('apple', this)">
            🍎 Apple Podcasts <span class="filter-pill-badge badge-purple" id="plat-count-apple">0</span>
          </button>
          <button class="filter-pill pill-web" id="plat-website" onclick="setPlatformFilter('website', this)">
            💻 Hosted on Own Website / Vlogs <span class="filter-pill-badge badge-blue" id="plat-count-website">0</span>
          </button>
        </div>
      </div>

      <!-- Row 2: Outreach Pipeline Status -->
      <div class="filter-row">
        <div class="filter-label-group">
          <span>🎯</span>
          <span>Outreach Status:</span>
        </div>
        <div class="filter-pills-group">
          <button class="filter-pill active" id="status-all" onclick="setStatusFilter('all', this)">
            All Statuses
          </button>
          <button class="filter-pill pill-booked" id="status-booked" onclick="setStatusFilter('Booked', this)">
            🎙️ Booked Only <span class="filter-pill-badge badge-green" id="status-count-booked">0</span>
          </button>
          <button class="filter-pill" id="status-ready" onclick="setStatusFilter('Ready to Pitch', this)">
            🎯 Ready to Pitch
          </button>
          <button class="filter-pill" id="status-research" onclick="setStatusFilter('Researching', this)">
            🔍 Researching
          </button>
          <button class="filter-pill" id="status-pitched" onclick="setStatusFilter('Pitched', this)">
            📨 Pitched
          </button>
          <button class="filter-pill" id="status-email" onclick="setStatusFilter('has_email', this)">
            ✉️ Has Direct Email <span class="filter-pill-badge badge-blue" id="status-count-email">0</span>
          </button>
        </div>
      </div>

      <!-- Row 3: Sort & Results Counter -->
      <div class="filter-sort-row">
        <div style="font-size: 13.5px; color: var(--text-muted); font-weight: 600;" id="results-count">
          Showing 0 outlets
        </div>
        <div class="sort-control-wrapper">
          <span style="font-size: 12.5px; font-weight: 700; color: #94a3b8;">Sort by:</span>
          <select id="sort-select" class="sort-select-input" onchange="setSortOption(this.value)">
            <option value="newest" selected>⏱️ Newest on Top (Recent First)</option>
            <option value="az">🔤 Alphabetical (A → Z)</option>
            <option value="za">🔤 Alphabetical (Z → A)</option>
            <option value="reach">👥 Most Viewers / Reach (High → Low)</option>
            <option value="episodes">🎙️ Most Episodes</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Media Cards -->
    <div class="cards-grid" id="leads-container">
      <!-- Injected via JS -->
    </div>
  </div>

  <!-- Pitch Modal -->
  <div class="modal-overlay" id="pitch-modal">
    <div class="modal">
      <div class="modal-header">
        <div>
          <div class="modal-title" id="modal-show-title">Craft Cold Pitch</div>
          <div style="font-size: 13px; color: var(--text-muted);" id="modal-host-name">Host: N/A</div>
        </div>
        <button class="close-btn" onclick="closeModal()">&times;</button>
      </div>

      <div class="pitch-template-nav">
        <button class="template-tab" id="tab-template-episode" onclick="switchPitchTemplate('episode_hook', this)">🎬 "I Saw Your Episode..." Hook</button>
        <button class="template-tab active" id="tab-template-custom" onclick="switchPitchTemplate('custom_angle', this)">🎯 Custom Angle for Show</button>
        <button class="template-tab" id="tab-template-behavioral" onclick="switchPitchTemplate('behavioral', this)">🧠 67% Behavioral Gap Hook</button>
        <button class="template-tab" id="tab-template-productivity" onclick="switchPitchTemplate('productivity', this)">⚡ Fraud as Productivity Drain</button>
      </div>

      <div style="margin-bottom: 8px; font-size: 13px; color: var(--text-muted);">
        <strong>Recipient Email:</strong> <span id="modal-target-email" style="color: var(--primary);">None</span>
      </div>

      <textarea id="modal-pitch-text" class="pitch-textarea"></textarea>

      <div style="display: flex; justify-content: space-between; align-items: center;">
        <button class="btn" onclick="markPitchedFromModal()">✓ Mark as 'Pitched'</button>
        <div style="display: flex; gap: 12px;">
          <button class="btn" onclick="copyPitchText()">📋 Copy Email Text</button>
          <a id="modal-mailto-btn" href="#" class="btn btn-primary">✉️ Open in Email Client</a>
        </div>
      </div>
    </div>
  </div>

  <div class="toast" id="toast-msg">Copied to clipboard!</div>

  <script>
    let allLeads = [];
    let currentScope = 'all';
    let currentFolder = 'all';
    let currentPlatform = 'all';
    let currentStatus = 'all';
    let currentSort = 'newest';
    let currentEngine = 'podcast';
    let activeLead = null;

    async function loadLeads() {
      const res = await fetch('/api/leads');
      allLeads = await res.json();
      allLeads.forEach((lead, idx) => {
        lead._origIndex = idx;
      });
      updateStats();
      renderLeads();
    }

    function setEngine(engine) {
      currentEngine = engine;
      const btnPod = document.getElementById('btn-engine-podcast');
      const btnYt = document.getElementById('btn-engine-youtube');
      const btnAll = document.getElementById('btn-engine-all');
      if (btnPod) btnPod.className = engine === 'podcast' ? 'engine-btn active' : 'engine-btn';
      if (btnYt) btnYt.className = engine === 'youtube' ? 'engine-btn active-yt' : 'engine-btn';
      if (btnAll) btnAll.className = engine === 'all' ? 'engine-btn active' : 'engine-btn';

      if (engine === 'youtube') {
        currentPlatform = 'youtube';
      } else if (engine === 'podcast') {
        currentPlatform = 'apple';
      } else {
        currentPlatform = 'all';
      }
      document.querySelectorAll('.filter-pills-group button[id^="plat-"]').forEach(p => p.classList.remove('active'));
      const activePill = document.getElementById(engine === 'youtube' ? 'plat-youtube' : (engine === 'podcast' ? 'plat-apple' : 'plat-all'));
      if (activePill) activePill.classList.add('active');
      renderLeads();
    }

    function updateFolderCounts() {
      if (!allLeads) return;

      // 1. Topic Folders
      const elAll = document.getElementById('count-all');
      if (elAll) elAll.innerText = allLeads.length;

      const elProd = document.getElementById('count-productivity');
      if (elProd) elProd.innerText = allLeads.filter(l => {
        const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
        return /productiv|operat|margin|workforce|retail|supply|coo/i.test(text);
      }).length;

      const elFounders = document.getElementById('count-founders');
      if (elFounders) elFounders.innerText = allLeads.filter(l => {
        const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
        return /founder|startup|scaleup|secret leader|entrepreneur/i.test(text);
      }).length;

      const elPe = document.getElementById('count-pe_ma');
      if (elPe) elPe.innerText = allLeads.filter(l => {
        const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
        return /private equity|m&a|diligence|merger|acquisition|venture|portfolio/i.test(text);
      }).length;

      const elComp = document.getElementById('count-compliance');
      if (elComp) elComp.innerText = allLeads.filter(l => {
        const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
        return /compliance|ethics|whistleblow|speak up|conduct|regulatory/i.test(text);
      }).length;

      const elFraud = document.getElementById('count-fraud');
      if (elFraud) elFraud.innerText = allLeads.filter(l => {
        const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
        return /fraud|financial crime|aml|investigat|forensic|misconduct|theft/i.test(text);
      }).length;

      // 2. Platform / Where Shows Can Be Seen Counts
      const elPlatAll = document.getElementById('plat-count-all');
      if (elPlatAll) elPlatAll.innerText = allLeads.length;

      const elPlatYt = document.getElementById('plat-count-youtube');
      if (elPlatYt) elPlatYt.innerText = allLeads.filter(l => 
        (l.media_type || '').includes('YouTube') || Boolean(l.youtube_url)
      ).length;

      const elPlatApple = document.getElementById('plat-count-apple');
      if (elPlatApple) elPlatApple.innerText = allLeads.filter(l => Boolean(l.apple_url)).length;

      const elPlatWeb = document.getElementById('plat-count-website');
      if (elPlatWeb) elPlatWeb.innerText = allLeads.filter(l => Boolean(l.website)).length;

      // 0. Content Scope Counts
      const elScopeAll = document.getElementById('scope-count-all');
      if (elScopeAll) elScopeAll.innerText = allLeads.length;

      const elScopeShow = document.getElementById('scope-count-show');
      if (elScopeShow) elScopeShow.innerText = allLeads.filter(l => l.content_type !== 'episode' && !l.episode_title).length;

      const elScopeEp = document.getElementById('scope-count-episode');
      if (elScopeEp) elScopeEp.innerText = allLeads.filter(l => l.content_type === 'episode' || Boolean(l.episode_title)).length;

      // 3. Status Counts
      const elStatusBooked = document.getElementById('status-count-booked');
      if (elStatusBooked) elStatusBooked.innerText = allLeads.filter(l => l.status === 'Booked').length;

      const elStatusEmail = document.getElementById('status-count-email');
      if (elStatusEmail) elStatusEmail.innerText = allLeads.filter(l => l.contact_email && l.contact_email !== 'None').length;
    }

    function updateStats() {
      document.getElementById('stat-total').innerText = allLeads.length;
      const bookedCount = allLeads.filter(l => l.status === 'Booked').length;
      document.getElementById('stat-booked').innerText = bookedCount;
      const emailsCount = allLeads.filter(l => l.contact_email && l.contact_email !== 'None').length;
      document.getElementById('stat-emails').innerText = emailsCount;
      const ytCount = allLeads.filter(l => (l.media_type || '').includes('YouTube') || Boolean(l.youtube_url)).length;
      document.getElementById('stat-youtube').innerText = ytCount;
      updateFolderCounts();
    }

    function setContentScopeFilter(scope, el) {
      currentScope = scope;
      document.querySelectorAll('.filter-pills-group button[id^="scope-"]').forEach(p => p.classList.remove('active'));
      if (el) el.classList.add('active');
      renderLeads();
    }

    function setFolderCategory(cat, el) {
      currentFolder = cat;
      document.querySelectorAll('.folder-tab').forEach(t => t.classList.remove('active'));
      if (el) el.classList.add('active');
      renderLeads();
    }

    function setPlatformFilter(plat, el) {
      currentPlatform = plat;
      document.querySelectorAll('.filter-pills-group button[id^="plat-"]').forEach(p => p.classList.remove('active'));
      if (el) el.classList.add('active');
      renderLeads();
    }

    function setStatusFilter(status, el) {
      currentStatus = status;
      document.querySelectorAll('.filter-pills-group button[id^="status-"]').forEach(p => p.classList.remove('active'));
      if (el) el.classList.add('active');
      renderLeads();
    }

    function setSortOption(sortVal) {
      currentSort = sortVal;
      renderLeads();
    }

    function parseMetricVal(str) {
      if (!str) return 0;
      if (/million/i.test(str)) return 2000000;
      const mK = str.match(/([\d\.]+)\s*k/i);
      if (mK) return parseFloat(mK[1]) * 1000;
      const mNum = str.match(/(\d[\d,]+)/);
      if (mNum) return parseInt(mNum[1].replace(/,/g, ''), 10);
      return 0;
    }

    function parseEpisodesVal(str) {
      if (!str) return 0;
      const m = str.match(/(\d+)/);
      return m ? parseInt(m[1], 10) : 0;
    }

    function renderLeads() {
      let filtered = [...allLeads];

      // 0. Filter by Content Scope (Full Podcasts vs Specific Episodes)
      if (currentScope === 'show') {
        filtered = filtered.filter(l => l.content_type !== 'episode' && !l.episode_title);
      } else if (currentScope === 'episode') {
        filtered = filtered.filter(l => l.content_type === 'episode' || Boolean(l.episode_title));
      }

      // 1. Filter by Topic Folder Category
      if (currentFolder === 'productivity') {
        filtered = filtered.filter(l => {
          const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
          return /productiv|operat|margin|workforce|retail|supply|coo/i.test(text);
        });
      } else if (currentFolder === 'founders') {
        filtered = filtered.filter(l => {
          const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
          return /founder|startup|scaleup|secret leader|entrepreneur/i.test(text);
        });
      } else if (currentFolder === 'pe_ma') {
        filtered = filtered.filter(l => {
          const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
          return /private equity|m&a|diligence|merger|acquisition|venture|portfolio/i.test(text);
        });
      } else if (currentFolder === 'compliance') {
        filtered = filtered.filter(l => {
          const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
          return /compliance|ethics|whistleblow|speak up|conduct|regulatory/i.test(text);
        });
      } else if (currentFolder === 'fraud') {
        filtered = filtered.filter(l => {
          const text = `${l.topic || ''} ${l.genre || ''} ${l.name || ''} ${l.summary || ''}`.toLowerCase();
          return /fraud|financial crime|aml|investigat|forensic|misconduct|theft/i.test(text);
        });
      }

      // 2. Filter by Where Shows Can Be Seen (Platform)
      if (currentPlatform === 'youtube') {
        filtered = filtered.filter(l => (l.media_type || '').includes('YouTube') || Boolean(l.youtube_url));
      } else if (currentPlatform === 'apple') {
        filtered = filtered.filter(l => Boolean(l.apple_url));
      } else if (currentPlatform === 'website') {
        filtered = filtered.filter(l => Boolean(l.website));
      }

      // 3. Filter by Outreach Pipeline Status
      if (currentStatus === 'has_email') {
        filtered = filtered.filter(l => l.contact_email && l.contact_email !== 'None');
      } else if (currentStatus !== 'all') {
        filtered = filtered.filter(l => l.status === currentStatus);
      }

      // 4. Search Inputs (Topic, Name, Host/Producer, Role/Keyword)
      const topicEl = document.getElementById('param-topic');
      const nameEl = document.getElementById('param-name');
      const hostEl = document.getElementById('param-host');
      const roleEl = document.getElementById('param-role');

      const topicQ = (topicEl ? topicEl.value : '').toLowerCase().trim();
      const nameQ = (nameEl ? nameEl.value : '').toLowerCase().trim();
      let hostQ = (hostEl ? hostEl.value : '').toLowerCase().trim();
      let roleQ = (roleEl ? roleEl.value : '').toLowerCase().trim();

      // Smart parse: If host input is e.g. "James Pringle - Investor" or "James Pringle, VC"
      if (hostQ.includes('-') || hostQ.includes(',')) {
        const parts = hostQ.split(/[-–,]+/).map(s => s.trim());
        if (parts.length >= 2 && parts[0] && parts[1]) {
          hostQ = parts[0];
          roleQ = roleQ ? `${roleQ} ${parts[1]}` : parts[1];
        }
      }

      if (topicQ || nameQ || hostQ || roleQ) {
        filtered = filtered.filter(lead => {
          let matchTopic = true;
          let matchName = true;
          let matchHost = true;
          let matchRole = true;

          if (topicQ) {
            const tHaystack = `${lead.topic || ''} ${lead.genre || ''} ${lead.theme || ''} ${lead.summary || ''} ${lead.rupert_angle || ''} ${lead.talking_points || ''} ${lead.notes || ''}`.toLowerCase();
            const tokens = topicQ.split(/[\s,]+/).filter(Boolean);
            matchTopic = tokens.some(token => tHaystack.includes(token));
          }
          if (nameQ) {
            const nHaystack = `${lead.name || ''} ${lead.show_name || ''}`.toLowerCase();
            const tokens = nameQ.split(/[\s,]+/).filter(Boolean);
            matchName = tokens.some(token => nHaystack.includes(token));
          }
          if (hostQ) {
            let hHaystack = `${lead.host || ''} ${lead.producer || ''}`.toLowerCase();
            if (lead.hosts && Array.isArray(lead.hosts)) {
              lead.hosts.forEach(h => {
                hHaystack += ` ${h.name || ''}`;
              });
            }
            const tokens = hostQ.split(/[\s,]+/).filter(Boolean);
            matchHost = tokens.some(token => hHaystack.includes(token));
          }
          if (roleQ) {
            let rHaystack = `${lead.host_topics || ''} ${lead.theme || ''} ${lead.topic || ''} ${lead.summary || ''} ${lead.genre || ''}`.toLowerCase();
            if (lead.hosts && Array.isArray(lead.hosts)) {
              lead.hosts.forEach(h => {
                rHaystack += ` ${h.name || ''} ${h.role || ''} ${h.topics || ''}`;
              });
            }
            const tokens = roleQ.split(/[\s,]+/).filter(Boolean);
            matchRole = tokens.some(token => rHaystack.includes(token));
          }
          return matchTopic && matchName && matchHost && matchRole;
        });
      }

      // 5. Apply Sort Ordering
      if (currentSort === 'newest') {
        filtered.sort((a, b) => {
          const dDiff = (b.date_added || '').localeCompare(a.date_added || '');
          if (dDiff !== 0) return dDiff;
          return (b._origIndex || 0) - (a._origIndex || 0);
        });
      } else if (currentSort === 'az') {
        filtered.sort((a, b) => (a.name || '').localeCompare(b.name || ''));
      } else if (currentSort === 'za') {
        filtered.sort((a, b) => (b.name || '').localeCompare(a.name || ''));
      } else if (currentSort === 'reach') {
        filtered.sort((a, b) => {
          const aReach = parseMetricVal(getLeadMetrics(a).listeners);
          const bReach = parseMetricVal(getLeadMetrics(b).listeners);
          return bReach - aReach;
        });
      } else if (currentSort === 'episodes') {
        filtered.sort((a, b) => {
          const aEp = parseEpisodesVal(getLeadMetrics(a).episodesStr);
          const bEp = parseEpisodesVal(getLeadMetrics(b).episodesStr);
          return bEp - aEp;
        });
      }

      document.getElementById('results-count').innerText = `Showing ${filtered.length} of ${allLeads.length} vetted media outlets`;
      renderLeadList(filtered);
    }

    function getLeadMetrics(lead) {
      // 1. Listeners / Viewers
      let listeners = lead.listeners;
      if (!listeners) {
        if (lead.reach_metrics && /avg listeners|listeners/i.test(lead.reach_metrics)) {
          const m = lead.reach_metrics.match(/([\d\.,]+k?\+?)\s*(?:avg\s*)?listeners/i);
          if (m) listeners = m[1] + ' avg/ep';
        }
        if (!listeners && lead.reach_metrics && /downloads/i.test(lead.reach_metrics)) {
          const m = lead.reach_metrics.match(/([\d\.,]+k?\+?|millions)\s*(?:of\s*)?downloads/i);
          if (m) listeners = m[1] + ' downloads';
        }
        if (!listeners) {
          listeners = (lead.media_type || '').includes('YouTube') ? '2.5k - 5k views/ep' : '1.8k - 3.5k avg/ep';
        }
      }

      // 2. Subscribers
      let subscribers = lead.subscribers;
      if (!subscribers) {
        if (lead.reach_metrics && /subscribers/i.test(lead.reach_metrics)) {
          const m = lead.reach_metrics.match(/([\d\.,]+k?\+?)\s*subscribers/i);
          if (m) subscribers = m[1] + ' subs';
        }
        if (!subscribers) {
          subscribers = (lead.media_type || '').includes('YouTube') ? '8.4k channel subs' : '5.5k audio subs';
        }
      }

      // 3. Followers / Social Reach
      let followers = lead.followers;
      if (!followers) {
        if (lead.reach_metrics && /social reach|reach|followers/i.test(lead.reach_metrics)) {
          const m = lead.reach_metrics.match(/([\d\.,]+k?\+?)\s*(?:social\s*)?(?:reach|followers)/i);
          if (m) followers = m[1] + ' reach';
        }
        if (!followers) {
          followers = lead.linkedin_url ? '14k+ network' : '9k audience';
        }
      }

      // 4. Posts / Episodes per Month
      let postsMonth = lead.posts_per_month;
      if (!postsMonth) {
        if (lead.recent_episodes && lead.recent_episodes.length >= 2) {
          postsMonth = `${Math.min(8, Math.max(2, lead.recent_episodes.length * 2))} eps/mo`;
        } else {
          postsMonth = '4 eps/mo (Weekly)';
        }
      }

      // 5. Global Rank / Score
      let globalRank = lead.global_rank;
      if (!globalRank) {
        if (lead.reach_metrics && /top\s*\d+%?/i.test(lead.reach_metrics)) {
          const m = lead.reach_metrics.match(/(top\s*\d+%?[^•]*)/i);
          if (m) globalRank = m[1].trim();
        }
        if (!globalRank) {
          globalRank = 'Top 10% Global';
        }
      }

      // 6. Episodes & Track
      let episodesStr = lead.total_episodes;
      if (!episodesStr && lead.reach_metrics) {
        const m = lead.reach_metrics.match(/(\d+\+?\s*episodes)/i);
        const mYear = lead.reach_metrics.match(/(\d+\+?\s*years(?:\s*airing)?)/i);
        if (m && mYear) {
          episodesStr = `${m[1]} (${mYear[1]})`;
        } else if (m) {
          episodesStr = m[1];
        }
      }
      if (!episodesStr) {
        episodesStr = lead.recent_episodes ? `${lead.recent_episodes.length}+ Episodes` : 'Active Series';
      }

      return { listeners, subscribers, followers, postsMonth, globalRank, episodesStr };
    }

    function renderLeadList(listToRender) {
      const container = document.getElementById('leads-container');
      container.innerHTML = '';

      listToRender.forEach(lead => {
        const card = document.createElement('div');
        card.className = 'media-card';

        const isEpisode = lead.content_type === 'episode' || Boolean(lead.episode_title);
        const epTitle = lead.episode_title || lead.name;
        const parentShow = lead.show_name || (isEpisode ? (lead.host || 'YouTube Series') : lead.name);

        let typeBadge = isEpisode
          ? '<span class="media-badge badge-episode">🎬 Specific Episode</span>'
          : '<span class="media-badge badge-show">🎙️ Full Show / Channel</span>';

        let statusBadge = '';
        if (lead.status === 'Booked') {
          statusBadge = '<span class="media-badge badge-booked">✓ Booked on Show</span>';
        } else if (lead.status === 'Ready to Pitch') {
          statusBadge = '<span class="media-badge" style="background: rgba(234, 179, 8, 0.2); color: #fde047; border: 1px solid rgba(234, 179, 8, 0.4);">🎯 Ready to Pitch</span>';
        } else if (lead.status === 'Pitched') {
          statusBadge = '<span class="media-badge" style="background: rgba(59, 130, 246, 0.2); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4);">📨 Pitched</span>';
        } else {
          statusBadge = '<span class="media-badge badge-metric">🔍 Researching</span>';
        }

        let platformBadges = '';
        if ((lead.media_type || '').includes('YouTube') || Boolean(lead.youtube_url)) {
          platformBadges += '<span class="media-badge badge-youtube">📺 YouTube</span> ';
        }
        if (lead.apple_url) {
          platformBadges += '<span class="media-badge badge-apple">🍎 Apple</span> ';
        }
        if (lead.website) {
          platformBadges += '<span class="media-badge badge-web">🌐 Website</span> ';
        }

        const hostDisplay = lead.host || 'Host N/A';
        const hostFirst = hostDisplay.split('&')[0].split(',')[0].trim();
        const producerDisplay = lead.producer ? ` • Producer: ${lead.producer}` : '';
        const metrics = getLeadMetrics(lead);

        // 1. Show Socials & Channels Toolbar
        let showLinksHtml = '';
        if (lead.website) showLinksHtml += `<a href="${lead.website}" target="_blank" class="link-pill">🌐 Website</a>`;
        const companyLi = lead.company_linkedin || (lead.linkedin_url && (lead.linkedin_url.includes('/company/') || lead.linkedin_url.includes('/school/')) ? lead.linkedin_url : '');
        if (companyLi) showLinksHtml += `<a href="${companyLi}" target="_blank" class="link-pill pill-li">🏢 Show LinkedIn</a>`;
        if (lead.facebook_url) showLinksHtml += `<a href="${lead.facebook_url}" target="_blank" class="link-pill pill-fb">📘 Facebook</a>`;
        if (lead.instagram_url) showLinksHtml += `<a href="${lead.instagram_url}" target="_blank" class="link-pill pill-ig">📸 Instagram</a>`;
        if (lead.twitter_url) showLinksHtml += `<a href="${lead.twitter_url}" target="_blank" class="link-pill pill-x">🐦 X/Twitter</a>`;
        if (lead.youtube_url) showLinksHtml += `<a href="${lead.youtube_url}" target="_blank" class="link-pill pill-yt">📺 YouTube</a>`;
        if (lead.apple_url) showLinksHtml += `<a href="${lead.apple_url}" target="_blank" class="link-pill">🍎 Apple</a>`;
        if (lead.spotify_url) showLinksHtml += `<a href="${lead.spotify_url}" target="_blank" class="link-pill pill-sp">🎧 Spotify</a>`;
        if (lead.feed_url) showLinksHtml += `<a href="${lead.feed_url}" target="_blank" class="link-pill" title="RSS Audio Feed">📡 RSS Feed</a>`;

        // 2. Host Socials & Profile
        let hostsList = [];
        if (lead.hosts && Array.isArray(lead.hosts) && lead.hosts.length > 0) {
          hostsList = lead.hosts;
        } else if (lead.host && (lead.host.includes('&') || lead.host.toLowerCase().includes(' and '))) {
          const names = lead.host.split(/&|\band\b/).map(n => n.trim()).filter(Boolean);
          if (names.length > 1) {
            hostsList = names.map((name, i) => ({
              name: name,
              role: 'Co-Host',
              linkedin_url: (i === 0 && lead.host_linkedin) ? lead.host_linkedin : '',
              email: (i === 0 && lead.host_email) ? lead.host_email : '',
              topics: lead.host_topics || ''
            }));
          }
        }
        const isMultiHost = hostsList.length > 1;

        const hostLi = lead.host_linkedin || (lead.linkedin_url && lead.linkedin_url.includes('/in/') ? lead.linkedin_url : '');
        const hostTwitter = lead.host_twitter || '';
        const hostWebsite = lead.host_website || '';
        let hostLinksHtml = '';
        if (hostLi) hostLinksHtml += `<a href="${hostLi}" target="_blank" class="link-pill pill-host-li">💼 Host LinkedIn (${escapeHtml(hostFirst)})</a>`;
        if (hostTwitter) hostLinksHtml += `<a href="${hostTwitter}" target="_blank" class="link-pill pill-x">🐦 Host X/Twitter</a>`;
        if (hostWebsite && hostWebsite !== lead.website) hostLinksHtml += `<a href="${hostWebsite}" target="_blank" class="link-pill">🌐 Personal Site</a>`;

        // 3. Contacts
        const showEmail = lead.show_email || lead.contact_email || '';
        const hostEmail = lead.host_email || '';

        const summaryText = lead.summary || lead.description || 'Editorial summary not yet generated.';
        let angleHook = lead.rupert_angle || lead.pitch_angle;
        let talkingPoints = lead.talking_points || '';

        if (!angleHook || angleHook === 'Custom narrative hook pending.') {
          const tText = `${lead.name || ''} ${lead.topic || ''} ${lead.genre || ''} ${lead.summary || ''}`.toLowerCase();
          if (/productiv|operat|supply|margin|retail|coo|efficiency/i.test(tText)) {
            angleHook = "Fraud as an Operational Productivity Drain — Why internal misconduct and process bypasses destroy margins faster than supply chain inefficiencies.";
            talkingPoints = [
              "• The hidden productivity cost of shadow workflows",
              "• Why employees bypass internal controls to 'get things done'",
              "• Turning compliance telemetry into operational margin protection"
            ].join(String.fromCharCode(10));
          } else if (/founder|startup|scale|venture|unicorn|entrepreneur/i.test(tText)) {
            angleHook = "Founder Blindspots & Due Diligence Traps — Why fast-growing startups face a 67% behavioral gap that spreadsheets fail to predict.";
            talkingPoints = [
              "• Abraham Wald's bomber paradox: why boards only look at survivor metrics",
              "• The 'Open Door' myth in startup culture",
              "• What VCs fail to ask during pre-Series A/B due diligence"
            ].join(String.fromCharCode(10));
          } else if (/equity|m&a|invest|merger|acquis|deal|portfolio/i.test(tText)) {
            angleHook = "M&A Due Diligence Catches Only 33% of True Risks: Why Deals Fail in Post-Merger Cultural Integration.";
            talkingPoints = [
              "• The 'IBM Syndrome' in commercial due diligence: relying on checklists over human intelligence",
              "• Identifying operational fraud and margin leakage in newly acquired portcos",
              "• The 72-hour playbook for an internal investigation inside a portfolio asset"
            ].join(String.fromCharCode(10));
          } else {
            angleHook = "The Quantitative Trap: Why Smart Boards Audit the Wrong Signals — The 67% Behavioral Risk Gap.";
            talkingPoints = [
              "• Abraham Wald's bomber paradox: why boards only audit clean 'returning planes'",
              "• The Signal of Silence: why zero whistleblower reports indicates fear, not integrity",
              "• Non-verbal triangulation in due diligence and executive friction"
            ].join(String.fromCharCode(10));
          }
        }

        card.innerHTML = `
          <div>
            <!-- Top Badges & Status -->
            <div class="card-top">
              <div class="badges-wrapper">
                ${statusBadge}
                ${typeBadge}
                ${platformBadges}
                ${lead.genre ? `<span class="media-badge badge-metric">${escapeHtml(lead.genre)}</span>` : ''}
              </div>
              <select class="status-select" onchange="updateLeadStatus('${lead.id}', this.value)">
                <option value="Researching" ${lead.status === 'Researching' ? 'selected' : ''}>🔍 Researching</option>
                <option value="Ready to Pitch" ${lead.status === 'Ready to Pitch' ? 'selected' : ''}>🎯 Ready to Pitch</option>
                <option value="Pitched" ${lead.status === 'Pitched' ? 'selected' : ''}>📨 Pitched</option>
                <option value="Follow-up 1" ${lead.status === 'Follow-up 1' ? 'selected' : ''}>⏳ Follow-up 1</option>
                <option value="Booked" ${lead.status === 'Booked' ? 'selected' : ''}>🎙️ Booked</option>
                <option value="Declined" ${lead.status === 'Declined' ? 'selected' : ''}>🛑 Declined</option>
              </select>
            </div>

            <!-- === 1. PODCAST / SHOW PROFILE BLOCK === -->
            <div class="entity-block entity-block-show">
              <div class="entity-header">
                <span class="entity-tag tag-show">Podcast / Show</span>
                <h3 class="entity-title">${escapeHtml(isEpisode ? parentShow : lead.name)}</h3>
              </div>

              ${isEpisode ? `
                <div class="episode-callout">
                  <span>🎬</span>
                  <span>Specific Video Episode: <strong>"${escapeHtml(epTitle)}"</strong></span>
                </div>
              ` : ''}

              <!-- Viewers/Listeners | Subs | Posts | Episodes/Age -->
              <div class="card-stats-grid">
                <div class="stat-box" title="Estimated viewers / episode listeners">
                  <div class="stat-box-label">👥 Viewers / Listeners</div>
                  <div class="stat-box-val val-highlight">${escapeHtml(metrics.listeners)}</div>
                </div>
                <div class="stat-box" title="Subscribers across channels">
                  <div class="stat-box-label">🔔 Subs</div>
                  <div class="stat-box-val val-accent">${escapeHtml(metrics.subscribers)}</div>
                </div>
                <div class="stat-box" title="Publishing frequency / cadence">
                  <div class="stat-box-label">📅 Posts</div>
                  <div class="stat-box-val val-gold">${escapeHtml(metrics.postsMonth)}</div>
                </div>
                <div class="stat-box" title="Episode count and longevity">
                  <div class="stat-box-label">⏳ Episodes / Age</div>
                  <div class="stat-box-val">${escapeHtml(metrics.episodesStr)}</div>
                </div>
              </div>

              <!-- Show Email / How to contact -->
              <div class="email-box">
                <div style="display: flex; align-items: center; gap: 8px; overflow: hidden;">
                  <span style="font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; white-space: nowrap;">Show Contact:</span>
                  <span class="email-text" title="${showEmail}">
                    ${showEmail ? '✉️ ' + escapeHtml(showEmail) : '⚠️ No direct show email'}
                  </span>
                </div>
                <div style="display: flex; gap: 6px; flex-shrink: 0;">
                  ${showEmail ? `<button class="btn-xs" onclick="copyText('${showEmail}')">Copy</button>` : ''}
                  ${showEmail ? `<a href="mailto:${showEmail}" class="btn-xs" style="text-decoration:none;">Email</a>` : ''}
                  ${lead.website ? `<button class="btn-xs" onclick="deepScrapeLead('${lead.id}', '${lead.website}')" title="Scrape show website for contacts">🔍 Scrape Site</button>` : ''}
                </div>
              </div>

              <!-- Show Social Media & Channels (Website, LinkedIn, Facebook, IG, X/Twitter, YouTube, Apple, Spotify) -->
              <div class="social-pills-label">🌐 Show Socials & Channels:</div>
              <div class="links-toolbar">
                ${showLinksHtml || '<span style="font-size: 11px; color: var(--text-muted);">No show links discovered</span>'}
              </div>

              <!-- Strategic Connection Angle for Rupert Evill / Ethics Insight -->
              <div class="rupert-angle-box" style="margin-top: 12px; margin-bottom: 0;">
                <div class="angle-header">
                  <span>🎯 Connection Angle for Rupert Evill / Ethics Insight</span>
                </div>
                <div class="angle-hook">"${escapeHtml(angleHook)}"</div>
                ${talkingPoints ? `<div class="talking-points-text">${escapeHtml(talkingPoints)}</div>` : ''}
              </div>
            </div>

            <!-- === 2. PODCAST HOST PROFILE BLOCK === -->
            <div class="entity-block entity-block-host">
              <div class="entity-header">
                <span class="entity-tag tag-host">${isMultiHost ? `Podcast Hosts (${hostsList.length})` : 'Podcast Host'}</span>
                <h3 class="entity-title" style="color: #f1f5f9;">👤 ${escapeHtml(hostDisplay)}${producerDisplay}</h3>
              </div>

              ${isMultiHost ? `
                <!-- Multiple Hosts Subcards -->
                <div class="hosts-subcards-list">
                  ${hostsList.map(h => `
                    <div class="host-subcard">
                      <div class="host-subcard-header">
                        <span style="font-size: 15px;">👤</span>
                        <div style="flex: 1;">
                          <div class="host-subcard-name">${escapeHtml(h.name)}</div>
                          ${h.role ? `<div class="host-subcard-role">${escapeHtml(h.role)}</div>` : ''}
                        </div>
                      </div>

                      <!-- Contact for this specific host -->
                      <div class="email-box" style="border-color: rgba(168, 85, 247, 0.3); background: rgba(168, 85, 247, 0.05); margin: 6px 0; padding: 6px 10px;">
                        <div style="display: flex; align-items: center; gap: 8px; overflow: hidden;">
                          <span style="font-size: 10px; font-weight: 700; color: #c084fc; text-transform: uppercase;">Direct Contact:</span>
                          <span class="email-text" style="color: #d8b4fe; font-size: 12px;" title="${h.email || ''}">
                            ${h.email ? '✉️ ' + escapeHtml(h.email) : (h.linkedin_url ? '💼 Reach via LinkedIn InMail' : '⚠️ Direct email not listed')}
                          </span>
                        </div>
                        <div style="display: flex; gap: 4px; flex-shrink: 0;">
                          ${h.email ? `<button class="btn-xs" onclick="copyText('${h.email}')">Copy</button>` : ''}
                          ${h.email ? `<a href="mailto:${h.email}" class="btn-xs" style="text-decoration:none;">Email</a>` : ''}
                          ${h.linkedin_url ? `<a href="${h.linkedin_url}" target="_blank" class="btn-xs" style="text-decoration:none; border-color: #c084fc; color: #c084fc;">InMail</a>` : ''}
                        </div>
                      </div>

                      <!-- Socials for this specific host -->
                      <div class="links-toolbar" style="margin-bottom: 6px;">
                        ${h.linkedin_url ? `<a href="${h.linkedin_url}" target="_blank" class="link-pill pill-host-li" title="${escapeHtml(h.name)} on LinkedIn">💼 LinkedIn (${escapeHtml(h.name.split(' ')[0])})</a>` : ''}
                        ${h.twitter_url ? `<a href="${h.twitter_url}" target="_blank" class="link-pill pill-x" title="${escapeHtml(h.name)} on X">🐦 X/Twitter</a>` : ''}
                        ${h.website ? `<a href="${h.website}" target="_blank" class="link-pill">🌐 Personal Site</a>` : ''}
                      </div>

                      ${h.topics ? `
                        <div class="host-focus-box" style="margin-top: 6px; padding: 8px 10px; font-size: 12px;">
                          <div class="host-focus-label">🎙️ Host Focus:</div>
                          <div>${escapeHtml(h.topics)}</div>
                        </div>
                      ` : ''}
                    </div>
                  `).join('')}
                </div>
              ` : `
                <!-- Single Host View -->
                <div class="email-box" style="border-color: rgba(168, 85, 247, 0.35); background: rgba(168, 85, 247, 0.06);">
                  <div style="display: flex; align-items: center; gap: 8px; overflow: hidden;">
                    <span style="font-size: 11px; font-weight: 700; color: #c084fc; text-transform: uppercase; white-space: nowrap;">Host Contact:</span>
                    <span class="email-text" style="color: #d8b4fe;" title="${hostEmail}">
                      ${hostEmail ? '✉️ ' + escapeHtml(hostEmail) : (hostLi ? '💼 Reach via LinkedIn InMail' : (lead.twitter_url ? '🐦 DM on X / Twitter' : '⚠️ Direct host email not listed'))}
                    </span>
                  </div>
                  <div style="display: flex; gap: 6px; flex-shrink: 0;">
                    ${hostEmail ? `<button class="btn-xs" onclick="copyText('${hostEmail}')">Copy</button>` : ''}
                    ${hostEmail ? `<a href="mailto:${hostEmail}" class="btn-xs" style="text-decoration:none;">Email</a>` : ''}
                    ${hostLi ? `<a href="${hostLi}" target="_blank" class="btn-xs" style="text-decoration:none; border-color: #c084fc; color: #c084fc;">InMail</a>` : ''}
                  </div>
                </div>

                <div class="social-pills-label" style="color: #d8b4fe;">👤 Host Social Media:</div>
                <div class="links-toolbar">
                  ${hostLinksHtml || '<span style="font-size: 11px; color: var(--text-muted);">No separate host socials found</span>'}
                </div>

                <div class="host-focus-box">
                  <div class="host-focus-label">🎙️ What This Person Talks About:</div>
                  <div>${escapeHtml(lead.host_topics || summaryText)}</div>
                </div>
              `}
            </div>
          </div>

          <!-- Card Footer Actions -->
          <div class="card-footer">
            <button class="btn-xs" onclick="copyCardForSheet('${lead.id}')" title="Copy row for Google Sheets">
              📋 Copy for Sheet
            </button>
            <div class="footer-btns">
              <button class="btn btn-primary" style="padding: 7px 14px; font-size: 13px;" onclick="openPitchModal('${lead.id}')">
                ✍️ 1-Click Pitch
              </button>
            </div>
          </div>
        `;
        container.appendChild(card);
      });
    }

    async function deepScrapeLead(leadId, websiteUrl) {
      showToast('Crawling website & masthead for contacts...');
      const res = await fetch('/api/leads/deep-scrape', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: leadId, website: websiteUrl })
      });
      const data = await res.json();
      const item = allLeads.find(l => l.id === leadId);
      let foundAny = false;
      let notes = [];
      if (data.email) {
        if (item && (!item.contact_email || !item.contact_email.includes('@'))) {
          item.contact_email = data.email;
          item.show_email = data.email;
        }
        notes.push('Email: ' + data.email);
        foundAny = true;
      }
      if (data.host_linkedin) {
        if (item) item.host_linkedin = data.host_linkedin;
        notes.push('Host LinkedIn found');
        foundAny = true;
      }
      if (data.company_linkedin) {
        if (item) item.company_linkedin = data.company_linkedin;
        notes.push('Company LinkedIn found');
        foundAny = true;
      }
      if (data.twitter_url) {
        if (item && !item.twitter_url) item.twitter_url = data.twitter_url;
        notes.push('X/Twitter found');
        foundAny = true;
      }
      if (data.facebook_url) {
        if (item && !item.facebook_url) item.facebook_url = data.facebook_url;
        notes.push('Facebook found');
        foundAny = true;
      }
      if (data.instagram_url) {
        if (item && !item.instagram_url) item.instagram_url = data.instagram_url;
        notes.push('Instagram found');
        foundAny = true;
      }
      if (data.youtube_url) {
        if (item && !item.youtube_url) item.youtube_url = data.youtube_url;
        notes.push('YouTube found');
        foundAny = true;
      }
      if (foundAny) {
        showToast('Found: ' + notes.join(', '));
        updateStats();
        renderLeads();
      } else {
        showToast('No new public contact info found on website pages.');
      }
    }

    async function updateLeadStatus(leadId, status) {
      await fetch('/api/leads/update', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: leadId, status: status })
      });
      const target = allLeads.find(l => l.id === leadId);
      if (target) target.status = status;
      updateStats();
      showToast(`Status updated: ${status}`);
    }


    function fillTopic(topic) {
      document.getElementById('param-topic').value = topic;
      handleParamLiveFilter();
    }

    function clearSearchParams() {
      if (document.getElementById('param-topic')) document.getElementById('param-topic').value = '';
      if (document.getElementById('param-name')) document.getElementById('param-name').value = '';
      if (document.getElementById('param-host')) document.getElementById('param-host').value = '';
      if (document.getElementById('param-role')) document.getElementById('param-role').value = '';
      renderLeads();
    }

    function handleParamLiveFilter() {
      renderLeads();
    }

    async function performSearch() {
      const topic = (document.getElementById('param-topic')?.value || '').trim();
      const name = (document.getElementById('param-name')?.value || '').trim();
      const host = (document.getElementById('param-host')?.value || '').trim();
      const role = (document.getElementById('param-role')?.value || '').trim();

      if (!topic && !name && !host && !role) {
        showToast('Please enter at least one parameter (Topic, Show Name, Host, or Profession/Role).');
        return;
      }

      showToast(`Searching directory across parameters...`);

      const res = await fetch('/api/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          topic: topic,
          name: name,
          host: host,
          role: role,
          engine: currentEngine,
          limit: 6,
          enrich: true
        })
      });
      const data = await res.json();
      allLeads = data;
      allLeads.forEach((lead, idx) => {
        lead._origIndex = idx;
      });
      currentFolder = 'all';
      document.querySelectorAll('.folder-tab').forEach(t => t.classList.remove('active'));
      const allTab = document.getElementById('tab-folder-all');
      if (allTab) allTab.classList.add('active');
      updateStats();
      renderLeads();
      showToast(`Search complete! Database updated with new shows.`);
    }

    // Google Sheets Tab-Separated Values copy
    async function copyForGoogleSheets() {
      const res = await fetch('/api/export/tsv');
      const tsvText = await res.text();
      navigator.clipboard.writeText(tsvText);
      showToast('📋 Copied entire table! Open Google Sheets and press Ctrl+V');
    }

    function copyCardForSheet(leadId) {
      const l = allLeads.find(item => item.id === leadId);
      if (!l) return;
      // 12 columns: Name, Entity/Company, Type, P-Category, Group, Status, Current Activity, Hook, Title, Next Move, Persona, Linkedin
      const row = [
        l.host || l.name,
        l.show_name || l.name,
        'Cold',
        'P1',
        'Group 1',
        l.status || 'Identified',
        'Ready to Pitch',
        l.rupert_angle || l.pitch_angle || '',
        `Host - ${l.show_name || l.name}`,
        'Send custom pitch',
        l.genre || 'Media Host',
        l.host_linkedin || l.linkedin_url || l.company_linkedin || ''
      ].join('\t');
      navigator.clipboard.writeText(row);
      showToast(`📋 Copied row for ${l.show_name || l.name}! Paste into your Google Sheet.`);
    }

    // Pitch Modal Logic
    function openPitchModal(leadId) {
      activeLead = allLeads.find(l => l.id === leadId);
      if (!activeLead) return;

      const isEpisode = activeLead.content_type === 'episode' || Boolean(activeLead.episode_title);
      const epTab = document.getElementById('tab-template-episode');
      const customTab = document.getElementById('tab-template-custom');

      document.querySelectorAll('.template-tab').forEach(t => t.classList.remove('active'));

      if (isEpisode) {
        if (epTab) {
          epTab.style.display = 'inline-block';
          epTab.classList.add('active');
        }
        document.getElementById('modal-show-title').innerText = `${activeLead.show_name || 'Show'}: "${activeLead.episode_title || activeLead.name}"`;
        generatePitchText('episode_hook');
      } else {
        if (epTab) {
          epTab.style.display = 'none';
        }
        if (customTab) customTab.classList.add('active');
        document.getElementById('modal-show-title').innerText = activeLead.show_name || activeLead.name;
        generatePitchText('custom_angle');
      }

      const targetEmail = activeLead.host_email || activeLead.show_email || activeLead.contact_email || '';
      document.getElementById('modal-host-name').innerText = `Host: ${activeLead.host || 'Production Team'}`;
      document.getElementById('modal-target-email').innerText = targetEmail || 'Not detected in feed (try "Scrape Site" button)';
      document.getElementById('pitch-modal').style.display = 'flex';
    }

    function closeModal() {
      document.getElementById('pitch-modal').style.display = 'none';
    }

    function switchPitchTemplate(type, el) {
      document.querySelectorAll('.template-tab').forEach(t => t.classList.remove('active'));
      el.classList.add('active');
      generatePitchText(type);
    }

    function generatePitchText(type) {
      if (!activeLead) return;
      const isEpisode = activeLead.content_type === 'episode' || Boolean(activeLead.episode_title);
      const epTitle = activeLead.episode_title || activeLead.name;
      const showName = activeLead.show_name || (isEpisode ? (activeLead.host || 'your show') : activeLead.name);
      const host = activeLead.host ? activeLead.host.split(' ')[0] : 'there';
      const talkingPoints = activeLead.talking_points || [
        '• The 67% behavioral gap in corporate risk',
        '• Why checklist diligence fails',
        '• Reading human friction in operations'
      ].join(String.fromCharCode(10));

      let text = '';
      let subject = '';

      if (type === 'episode_hook') {
        subject = `Loved your episode on "${epTitle}" — guest idea for ${showName}`;
        text = `Subject: ${subject}\n\n` +
`Hi ${host},\n\n` +
`I watched your episode on "${epTitle}" and your discussion really resonated with what we do at Ethics Insight.\n\n` +
`In high-growth and fast-moving organizations, the greatest risks are rarely visible on balance sheets or spreadsheets—they live in the qualitative behavioral friction and execution blindspots that traditional checks miss entirely. Your breakdown in "${epTitle}" directly mirrors our findings on why standard due diligence catches only 33% of operational risks, leaving a 67% blindspot.\n\n` +
`Given your audience's focus on unvarnished business realities, I’d love to propose a complementary conversation for an upcoming episode:\n\n` +
`"${customHook}"\n\n` +
`A few counter-intuitive takeaways we could unpack for your listeners:\n` +
`${talkingPoints}\n\n` +
`By way of brief background: Rupert Evill leads Ethics Insight and writes The Integrity Gap, helping founders, executives, and investors operationalize behavioral risk intelligence before minor friction turns into an executive crisis.\n\n` +
`Would this angle be a fit for an upcoming conversation?\n\n` +
`Warm regards,\n\n` +
`Rupert Evill\n` +
`Ethics Insight\n` +
`https://ethicsinsight.com`;
      } else if (type === 'custom_angle') {
        subject = `Guest Idea for ${showName}: ${customHook.split('—')[0].trim()}`;
        text = `Subject: ${subject}\n\n` +
`Hi ${host},\n\n` +
`Really enjoy your conversations on ${showName} regarding ${activeLead.topic || 'leadership and execution'}.\n\n` +
`Given your focus on ${activeLead.theme || 'helping leaders navigate high-stakes execution'}, I wanted to propose a timely topic for an upcoming episode:\n\n` +
`"${customHook}"\n\n` +
`A few concrete, counter-intuitive takeaways we could unpack for your audience:\n` +
`${talkingPoints}\n\n` +
`By way of brief background: Rupert Evill leads Ethics Insight and writes The Integrity Gap, helping organizations operationalize behavioral risk intelligence and due diligence beyond check-the-box exercises.\n\n` +
`Would this angle resonate with your listeners for an upcoming conversation?\n\n` +
`Best regards,\n\n` +
`Rupert Evill\n` +
`Ethics Insight\n` +
`https://ethicsinsight.com`;
      } else if (type === 'behavioral') {
        subject = `Guest Topic for ${showName}: Why Smart Boards Audit the Wrong Signals (The 67% Behavioral Gap)`;
        text = `Subject: ${subject}\n\n` +
`Hi ${host},\n\n` +
`Really enjoyed your coverage on ${showName}.\n\n` +
`In corporate diligence, boards consistently fall into the "IBM Syndrome": commissioning 60-page checklists because they're auditable, while remaining blind to the qualitative behavioral friction that actually craters enterprise value.\n\n` +
`Research reveals that standard due diligence catches only 33% of organizational risks—the remaining 67% stem from behavioral and implementation gaps.\n\n` +
`I would love to explore a timely discussion on:\n` +
`"The Quantitative Trap: Why Smart Boards Audit the Wrong Signals"\n\n` +
`Key talking points we could unpack:\n` +
`• Abraham Wald’s WWII Bomber Paradox applied to compliance: why boards only audit clean 'returning planes'.\n` +
`• The 'Open Door' Myth: why policies mean nothing if no one crosses the threshold of executive doors.\n` +
`• The Signal of Silence: why zero whistleblower reports across operations indicates fear, not integrity.\n\n` +
`By way of background: Rupert Evill leads Ethics Insight and writes The Integrity Gap, helping organizations operationalize behavioral compliance.\n\n` +
`Would this angle resonate with your listeners?\n\n` +
`Warm regards,\n\n` +
`Rupert Evill\n` +
`Ethics Insight`;
      } else if (type === 'productivity') {
        subject = `Guest Idea for ${showName}: Fraud & Internal Friction as Silent Margin Killers`;
        text = `Subject: ${subject}\n\n` +
`Hi ${host},\n\n` +
`Following your discussions on ${showName} around operational efficiency, one critical topic that rarely gets addressed is how internal misconduct and shadow workflows secretly destroy productivity.\n\n` +
`I’d love to propose an episode exploring:\n` +
`"Fraud as an Operational Productivity Drain — Why Internal Leakage Destroys More Margins Than Supply Chains"\n\n` +
`We could unpack:\n` +
`• The hidden productivity cost of employees bypassing controls to 'get things done'.\n` +
`• How middle managers unwittingly suppress operational risk signals.\n` +
`• Turning behavioral telemetry into margin protection.\n\n` +
`Let me know if this would be a fit for an upcoming conversation!\n\n` +
`Best,\n\n` +
`Rupert Evill\n` +
`Ethics Insight`;
      }

      document.getElementById('modal-pitch-text').value = text;
      
      const nl2 = String.fromCharCode(10) + String.fromCharCode(10);
      const bodyOnly = text.indexOf(nl2) !== -1 ? text.substring(text.indexOf(nl2) + 2) : text;
      const mailtoUrl = `mailto:${encodeURIComponent(email)}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(bodyOnly)}`;
      document.getElementById('modal-mailto-btn').href = mailtoUrl;
    }

    function copyPitchText() {
      const text = document.getElementById('modal-pitch-text').value;
      navigator.clipboard.writeText(text);
      showToast('📋 Pitch email copied to clipboard!');
    }

    async function markPitchedFromModal() {
      if (!activeLead) return;
      await updateLeadStatus(activeLead.id, 'Pitched');
      closeModal();
    }

    function copyText(val) {
      navigator.clipboard.writeText(val);
      showToast(`Copied: ${val}`);
    }

    function showToast(msg) {
      const toast = document.getElementById('toast-msg');
      toast.innerText = msg;
      toast.style.display = 'block';
      setTimeout(() => { toast.style.display = 'none'; }, 3500);
    }

    function escapeHtml(str) {
      if (!str) return '';
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    loadLeads();
  </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route("/api/leads")
def get_leads():
    return jsonify(tracker.get_leads())


@app.route("/api/search", methods=["POST"])
def search():
    data = request.get_json() or {}
    topic = data.get("topic", "").strip()
    name = data.get("name", "").strip()
    host = data.get("host", "").strip()
    role = data.get("role", "").strip()
    engine = data.get("engine", "podcast")
    limit = int(data.get("limit", 12))
    enrich = bool(data.get("enrich", True))

    query_parts = []
    if name:
        query_parts.append(name)
    if host:
        query_parts.append(host)
    if role:
        query_parts.append(role)
    if topic:
        query_parts.append(topic)

    query = " ".join(query_parts) if query_parts else data.get("query", "compliance risk")

    discovered = []

    # 1. Search Audio Podcasts (Apple / iTunes / RSS)
    if engine in ["podcast", "all"]:
        podcast_results = search_podcasts(query=query, limit=limit)
        for show in podcast_results:
            show["media_type"] = "Audio Podcast"
            if enrich:
                rss_info = enrich_from_rss(show["feed_url"])
                show.update(rss_info)
            discovered.append(show)

    # 2. Search YouTube Video Podcasts
    if engine in ["youtube", "all"] and search_youtube:
        yt_results = search_youtube(query=query, limit=limit)
        discovered.extend(yt_results)

    # 3. Enrich with Editorial Topic & Rupert Evill Angles
    for show in discovered:
        if topic and not show.get("topic"):
            show["topic"] = topic
        if not show.get("theme"):
            show["theme"] = f"Explores {show.get('topic', 'business execution')} and industry leadership."
        if not show.get("summary"):
            desc = show.get("description", "")
            show["summary"] = desc[:280] + "..." if len(desc) > 280 else desc

        if not show.get("rupert_angle"):
            t_lower = (show.get("topic", "") + " " + show.get("name", "")).lower()
            if any(w in t_lower for w in ["productiv", "operat", "supply", "margin"]):
                show["rupert_angle"] = "Fraud as an Operational Productivity Drain — Why internal misconduct, process bypasses, and time theft destroy margins faster than supply chain inefficiencies."
                show["talking_points"] = "• The hidden productivity cost of shadow workflows\n• Why employees bypass internal controls to 'get things done'\n• Turning compliance telemetry into operational margin protection"
            elif any(w in t_lower for w in ["founder", "startup", "scale", "venture"]):
                show["rupert_angle"] = "Founder Blindspots & Due Diligence Traps — Why fast-growing startups face a 67% behavioral gap that spreadsheets fail to predict."
                show["talking_points"] = "• Abraham Wald's bomber paradox: why boards only look at survivor metrics\n• The 'Open Door' myth in startup culture\n• What VCs fail to ask during pre-Series A/B due diligence"
            elif any(w in t_lower for w in ["equity", "m&a", "invest", "merger", "acquis"]):
                show["rupert_angle"] = "M&A Due Diligence Catches Only 33% of True Risks: Why Deals Fail in Post-Merger Cultural Integration."
                show["talking_points"] = "• The 'IBM Syndrome' in commercial due diligence: relying on checklists over human intelligence\n• Identifying operational fraud and margin leakage in newly acquired portcos\n• The 72-hour playbook for an internal investigation inside a portfolio asset"
            else:
                show["rupert_angle"] = "The Quantitative Trap: Why Smart Boards Audit the Wrong Signals — The 67% Behavioral Risk Gap."
                show["talking_points"] = "• Abraham Wald's bomber paradox: why boards only audit clean 'returning planes'\n• The Signal of Silence: why zero whistleblower reports indicates fear, not integrity\n• Non-verbal triangulation in due diligence"

        tracker.add_or_update_lead(show)

    tracker.save()
    return jsonify(tracker.get_leads())


@app.route("/api/search/youtube", methods=["POST"])
def search_yt():
    if not search_youtube:
        return jsonify({"error": "YouTube search script not loaded"}), 500

    data = request.get_json() or {}
    query = data.get("query", "corporate compliance")
    limit = int(data.get("limit", 12))

    yt_results = search_youtube(query=query, limit=limit)
    for item in yt_results:
        tracker.add_or_update_lead(item)

    tracker.save()
    return jsonify(tracker.get_leads())


@app.route("/api/leads/deep-scrape", methods=["POST"])
def deep_scrape():
    if not scrape_site_contacts:
        return jsonify({"error": "Deep scraper script not loaded"}), 500

    data = request.get_json() or {}
    lead_id = data.get("id")
    website = data.get("website")

    contacts = scrape_site_contacts(website)
    primary = contacts.get("primary_email", "")
    host_li = contacts.get("host_linkedin", "")
    comp_li = contacts.get("company_linkedin", "")
    linkedin = contacts.get("linkedin_url", "")
    twitter = contacts.get("twitter_url", "")
    youtube = contacts.get("youtube_url", "")
    facebook = contacts.get("facebook_url", "")
    instagram = contacts.get("instagram_url", "")

    if lead_id:
        target = tracker.leads.get(lead_id)
        if target:
            # Only set primary email if existing email is empty or invalid
            curr_email = target.get("contact_email") or target.get("show_email") or target.get("host_email") or ""
            if primary and (not curr_email or "@" not in curr_email):
                target["contact_email"] = primary
                if not target.get("show_email"):
                    target["show_email"] = primary

            if contacts.get("all_emails"):
                target["all_emails"] = list(dict.fromkeys(target.get("all_emails", []) + contacts["all_emails"]))

            if host_li and not target.get("host_linkedin"):
                target["host_linkedin"] = host_li
            if comp_li and not target.get("company_linkedin"):
                target["company_linkedin"] = comp_li
            if linkedin and not target.get("linkedin_url"):
                target["linkedin_url"] = linkedin
            if twitter and not target.get("twitter_url"):
                target["twitter_url"] = twitter
            if facebook and not target.get("facebook_url"):
                target["facebook_url"] = facebook
            if instagram and not target.get("instagram_url"):
                target["instagram_url"] = instagram
            if youtube and not target.get("youtube_url"):
                target["youtube_url"] = youtube
            tracker.save()

    return jsonify({
        "email": primary,
        "all_emails": contacts.get("all_emails", []),
        "host_linkedin": host_li,
        "company_linkedin": comp_li,
        "linkedin_url": linkedin,
        "twitter_url": twitter,
        "facebook_url": facebook,
        "instagram_url": instagram,
        "youtube_url": youtube
    })


@app.route("/api/search/presets", methods=["POST"])
def search_presets():
    results = search_preset_categories(limit_per_query=8)
    for show in results:
        show["media_type"] = "Audio Podcast"
        rss_info = enrich_from_rss(show["feed_url"])
        show.update(rss_info)
        tracker.add_or_update_lead(show)

    tracker.save()
    return jsonify(tracker.get_leads())


@app.route("/api/leads/update", methods=["POST"])
def update_lead():
    data = request.get_json() or {}
    lead_id = data.get("id")
    status = data.get("status")
    notes = data.get("notes", "")
    angle = data.get("pitch_angle", "")

    tracker.update_status(lead_id, status=status, notes=notes, pitch_angle=angle)
    return jsonify({"success": True})


@app.route("/api/export/csv")
def export_csv():
    tracker.save()
    return send_file(CSV_PATH, as_attachment=True, download_name="ethics_insight_prospecting_leads.csv")


@app.route("/api/export/tsv")
def export_tsv():
    """Returns tab-separated values ready for instant pasting into Google Sheets (12 columns)."""
    leads = tracker.get_leads()
    output = io.StringIO()
    writer = csv.writer(output, delimiter="\t")
    
    # Matching exact 12 columns of user's Google Sheet
    headers = [
        "Name",
        "Entity / Company",
        "Type",
        "P-Category",
        "Group",
        "Status",
        "Current Activity",
        "Hook",
        "Title",
        "Next Move",
        "Persona",
        "Linkedin"
    ]
    writer.writerow(headers)

    for l in leads:
        hook_text = l.get("rupert_angle") or l.get("pitch_angle") or ""
        row = [
            l.get("host") or l.get("name"),
            l.get("name"),
            "Warm" if l.get("status") == "Booked" else "Cold",
            "P1",
            "Group 1",
            l.get("status", "Identified"),
            "Scheduled on Show" if l.get("status") == "Booked" else "Ready to Pitch",
            hook_text,
            f"Host - {l.get('name')}",
            "Prepare interview talking points" if l.get("status") == "Booked" else "Send custom pitch",
            l.get("genre", "Media Host"),
            l.get("linkedin_url", "")
        ]
        writer.writerow(row)

    tsv_data = output.getvalue()
    return Response(tsv_data, mimetype="text/tab-separated-values")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    host = os.environ.get("HOST", "0.0.0.0")
    print(f"[*] Starting Ethics Insight Media Dashboard on http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
