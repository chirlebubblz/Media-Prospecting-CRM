#!/usr/bin/env python3
"""
Ethics Insight - Executive Outreach & Media CRM
Dual-Pipeline CRM:
1. Podcast & Media Pipeline (P4 - Target Shows & Enriched Media)
2. Executive & Dealmaker Pipeline (Master Leads & Outreach - PE/VC/DFI Partners)
"""

import os
import sys
import csv
import json
import io
import re
import urllib.parse
from datetime import datetime
from flask import Flask, render_template_string, request, jsonify, Response, send_file
import openpyxl

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Locate scripts directory (local scripts first, then parent skill directories)
for p in [
    os.path.abspath(os.path.join(BASE_DIR, "scripts")),
    os.path.abspath(os.path.join(BASE_DIR, "..", ".agents", "skills", "media-discovery-and-outreach", "scripts")),
    os.path.abspath(os.path.join(BASE_DIR, ".agents", "skills", "media-discovery-and-outreach", "scripts")),
]:
    if os.path.exists(p) and p not in sys.path:
        sys.path.insert(0, p)

from src.discovery.podcast_crawler import search_podcasts, search_preset_categories, DEFAULT_PRESET_QUERIES
from src.discovery.rss_extractor import enrich_from_rss
from src.crm.tracker import LeadTracker, ExecutiveTracker, CSV_PATH, JSON_PATH, EXEC_JSON_PATH

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
exec_tracker = ExecutiveTracker()


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ethics Insight | Executive Outreach & Media CRM</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #070b14;
      --bg-surface: #0e1626;
      --card-bg: #121d33;
      --card-hover: #172540;
      --border: #1e2c47;
      --border-accent: #2c426b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --accent: #10b981;
      --gold: #f59e0b;
      --purple: #a855f7;
      --rose: #f43f5e;
      --tag-bg: #18233a;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 90px;
      overflow-x: hidden;
    }

    /* Top Navigation Bar */
    .top-navbar {
      background: rgba(14, 22, 38, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }
    .brand-section {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }
    .brand-logo {
      width: 36px;
      height: 36px;
      border-radius: 9px;
      background: linear-gradient(135deg, #0ea5e9, #a855f7);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      box-shadow: 0 4px 14px rgba(14, 165, 233, 0.35);
    }
    .brand-title {
      font-size: 17px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .brand-badge {
      font-size: 10px;
      font-weight: 700;
      background: rgba(56, 189, 248, 0.15);
      color: var(--primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 2px 7px;
      border-radius: 5px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .brand-sub {
      font-size: 11px;
      color: var(--text-muted);
    }

    /* Central Pipeline Switcher */
    .pipeline-switcher {
      display: flex;
      background: rgba(7, 11, 20, 0.8);
      border: 1px solid var(--border);
      padding: 3px;
      border-radius: 10px;
      gap: 4px;
    }
    .pipeline-tab {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 7px 18px;
      border-radius: 7px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .pipeline-tab:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.05);
    }
    .pipeline-tab.active {
      background: #1e293b;
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }
    .pipeline-tab.active.tab-media {
      background: linear-gradient(135deg, rgba(14, 165, 233, 0.25), rgba(56, 189, 248, 0.1));
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
    }
    .pipeline-tab.active.tab-exec {
      background: linear-gradient(135deg, rgba(168, 85, 247, 0.25), rgba(192, 132, 252, 0.1));
      border: 1px solid rgba(168, 85, 247, 0.4);
      color: #c084fc;
    }
    .tab-counter {
      font-size: 11px;
      padding: 1px 7px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.1);
      color: inherit;
    }

    /* Top Right Controls */
    .top-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      font-size: 12.5px;
      font-weight: 600;
      border-radius: 7px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      cursor: pointer;
      text-decoration: none;
      transition: all 0.15s ease;
      white-space: nowrap;
    }
    .btn:hover {
      background: var(--card-hover);
      border-color: var(--border-accent);
      color: #ffffff;
    }
    .btn-primary {
      background: var(--primary);
      color: #070b14;
      border-color: var(--primary);
      font-weight: 700;
    }
    .btn-primary:hover {
      background: var(--primary-hover);
      border-color: var(--primary-hover);
      color: #070b14;
    }
    .btn-success {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.4);
    }
    .btn-success:hover {
      background: rgba(16, 185, 129, 0.3);
      border-color: #34d399;
      color: #ffffff;
    }
    .view-toggle-group {
      display: flex;
      background: rgba(7, 11, 20, 0.8);
      border: 1px solid var(--border);
      padding: 2px;
      border-radius: 8px;
    }
    .view-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 5px 10px;
      font-size: 12px;
      font-weight: 600;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s;
    }
    .view-btn.active {
      background: #1e293b;
      color: #38bdf8;
    }

    /* Main Container */
    .container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 24px 28px;
    }

    /* KPI Summary Ribbon */
    .kpi-ribbon {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-bottom: 24px;
    }
    .kpi-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 12px 16px;
      display: flex;
      flex-direction: column;
      gap: 3px;
      transition: transform 0.15s, border-color 0.15s;
    }
    .kpi-card:hover {
      border-color: var(--border-accent);
      transform: translateY(-1px);
    }
    .kpi-label {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .kpi-val {
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      font-family: 'JetBrains Mono', monospace;
    }
    .kpi-val.sky { color: #38bdf8; }
    .kpi-val.emerald { color: #34d399; }
    .kpi-val.purple { color: #c084fc; }
    .kpi-val.amber { color: #fbbf24; }

    /* Filter & Search Bar */
    .filter-toolbar {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 14px 18px;
      margin-bottom: 24px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
      justify-content: space-between;
    }
    .search-input-wrap {
      flex: 1;
      min-width: 280px;
      position: relative;
    }
    .search-input {
      width: 100%;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 9px 12px 9px 36px;
      color: #ffffff;
      font-size: 13.5px;
      outline: none;
      transition: border-color 0.15s;
    }
    .search-input:focus {
      border-color: var(--primary);
    }
    .search-icon {
      position: absolute;
      left: 11px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 14px;
      color: var(--text-muted);
    }
    .filter-controls {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .select-filter {
      background: var(--bg);
      border: 1px solid var(--border);
      color: #e2e8f0;
      font-size: 12.5px;
      padding: 8px 12px;
      border-radius: 8px;
      outline: none;
      cursor: pointer;
    }
    .select-filter:focus {
      border-color: var(--primary);
    }

    /* Cards Grid View */
    .leads-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(430px, 1fr));
      gap: 18px;
    }
    @media (max-width: 500px) {
      .leads-grid { grid-template-columns: 1fr; }
    }

    /* Lead Card */
    .lead-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      transition: all 0.2s ease;
      position: relative;
    }
    .lead-card:hover {
      border-color: var(--border-accent);
      background: var(--card-hover);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    .card-top {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
    }
    .card-title-group {
      flex: 1;
      min-width: 0;
    }
    .card-title {
      font-size: 16px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.3;
      margin-bottom: 4px;
      word-break: break-word;
    }
    .card-subtitle {
      font-size: 12px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
    }
    .pill-badge {
      display: inline-flex;
      align-items: center;
      font-size: 10.5px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 5px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .badge-media { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .badge-exec { background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }
    .badge-p1 { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-p2 { background: rgba(96, 165, 250, 0.15); color: #93c5fd; border: 1px solid rgba(96, 165, 250, 0.3); }
    .badge-group { background: rgba(255, 255, 255, 0.06); color: #cbd5e1; border: 1px solid rgba(255, 255, 255, 0.1); }

    /* Interactive Status Selector */
    .status-select {
      background: var(--bg);
      border: 1px solid var(--border);
      color: #f1f5f9;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 6px;
      cursor: pointer;
      outline: none;
      transition: all 0.15s;
    }
    .status-select.status-active { border-color: #10b981; color: #34d399; }
    .status-select.status-booked { border-color: #38bdf8; color: #38bdf8; }
    .status-select.status-sent { border-color: #fbbf24; color: #fbbf24; }
    .status-select.status-watch { border-color: #f43f5e; color: #fb7185; }

    /* Contact Details Block */
    .contact-box {
      background: rgba(7, 11, 20, 0.6);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .contact-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      font-size: 12px;
    }
    .contact-target {
      font-weight: 600;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .contact-email-val {
      font-family: 'JetBrains Mono', monospace;
      color: #38bdf8;
      font-size: 11.5px;
      word-break: break-all;
    }

    /* Links & Socials Toolbar */
    .links-toolbar {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
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
    .link-pill.pill-yt { border-color: rgba(244, 63, 94, 0.3); color: #fb7185; }
    .link-pill.pill-yt:hover { border-color: #f43f5e; color: #ffffff; background: rgba(244, 63, 94, 0.2); }
    .link-pill.pill-video-comment {
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.4);
      color: #fda4af;
      font-weight: 700;
    }
    .link-pill.pill-video-comment:hover {
      background: rgba(244, 63, 94, 0.3);
      color: #ffffff;
      border-color: #f43f5e;
    }

    /* Multi-Host Subcards */
    .host-subcards-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .host-subcard {
      background: rgba(14, 22, 38, 0.7);
      border: 1px solid rgba(168, 85, 247, 0.25);
      border-left: 3px solid #c084fc;
      border-radius: 6px;
      padding: 8px 10px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .host-subcard-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 6px;
    }
    .host-subcard-name {
      font-size: 12.5px;
      font-weight: 700;
      color: #ffffff;
    }
    .host-subcard-role {
      font-size: 11px;
      color: #d8b4fe;
    }

    /* Angle / Hook Accent Box */
    .hook-box {
      background: rgba(56, 189, 248, 0.05);
      border-left: 3px solid var(--primary);
      border-radius: 0 8px 8px 0;
      padding: 10px 12px;
      font-size: 12px;
      line-height: 1.5;
      color: #e2e8f0;
    }
    .hook-box.hook-exec {
      background: rgba(168, 85, 247, 0.05);
      border-left-color: var(--purple);
    }
    .hook-label {
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--primary);
      margin-bottom: 3px;
    }
    .hook-label.label-exec { color: #c084fc; }

    /* Current Activity & Notes Field */
    .notes-section {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .notes-label {
      font-size: 10.5px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .notes-input {
      width: 100%;
      background: rgba(7, 11, 20, 0.7);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 6px 10px;
      font-size: 11.5px;
      color: #cbd5e1;
      font-family: inherit;
      resize: vertical;
      min-height: 48px;
    }
    .notes-input:focus {
      outline: none;
      border-color: var(--primary);
    }

    /* Compact CRM Table View */
    .table-container {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow-x: auto;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    .crm-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 12.5px;
    }
    .crm-table th {
      background: rgba(7, 11, 20, 0.95);
      padding: 12px 14px;
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      border-bottom: 1px solid var(--border);
      white-space: nowrap;
    }
    .crm-table td {
      padding: 12px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: #cbd5e1;
      vertical-align: middle;
    }
    .crm-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
      color: #ffffff;
    }
    .td-title {
      font-weight: 700;
      color: #ffffff;
    }

    /* Toast Notification */
    #toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #1e293b;
      color: #ffffff;
      border: 1px solid var(--border-accent);
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
      z-index: 1000;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s, transform 0.2s;
      transform: translateY(10px);
    }
    #toast.show {
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }

    /* Modal Styling */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(4px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 200;
      padding: 20px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s;
    }
    .modal-overlay.active {
      opacity: 1;
      pointer-events: auto;
    }
    .modal-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-accent);
      border-radius: 14px;
      width: 100%;
      max-width: 580px;
      padding: 24px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .modal-title {
      font-size: 18px;
      font-weight: 800;
      color: #ffffff;
    }
    .close-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 20px;
      cursor: pointer;
    }
    .form-group {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    .form-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
    }
    .form-input {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 7px;
      padding: 8px 12px;
      color: #ffffff;
      font-size: 13px;
    }
    .form-input:focus {
      outline: none;
      border-color: var(--primary);
    }

    /* Helper Utilities */
    .btn-xs {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border);
      color: #cbd5e1;
      padding: 3px 7px;
      border-radius: 4px;
      font-size: 11px;
      cursor: pointer;
    }
    .btn-xs:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
    }
  </style>
</head>
<body>

  <!-- Top Navigation Bar -->
  <header class="top-navbar">
    <div class="brand-section">
      <div class="brand-logo">🛡️</div>
      <div>
        <div class="brand-title">
          Ethics Insight
          <span class="brand-badge">Executive CRM</span>
        </div>
        <div class="brand-sub">Behavioral Due Diligence & Media Outreach</div>
      </div>
    </div>

    <!-- Pipeline Switcher Tabs -->
    <div class="pipeline-switcher">
      <button class="pipeline-tab tab-media active" id="tab-pipeline-media" onclick="switchPipeline('media')">
        <span>🎙️ Podcast & Media</span>
        <span class="tab-counter" id="badge-media-count">0</span>
      </button>
      <button class="pipeline-tab tab-exec" id="tab-pipeline-exec" onclick="switchPipeline('exec')">
        <span>💼 Executive & Dealmakers</span>
        <span class="tab-counter" id="badge-exec-count">0</span>
      </button>
    </div>

    <!-- Top Action Buttons -->
    <div class="top-actions">
      <div class="view-toggle-group">
        <button class="view-btn active" id="view-cards-btn" onclick="setViewMode('cards')">🗂️ Cards</button>
        <button class="view-btn" id="view-table-btn" onclick="setViewMode('table')">📋 Table</button>
      </div>

      <a href="/api/export/excel" class="btn btn-success" title="Download Excel Progress Sheet matching your format">
        <span>📥 Export Excel</span>
      </a>

      <button class="btn btn-primary" onclick="openAddLeadModal()">
        <span>➕ Add Lead</span>
      </button>
    </div>
  </header>

  <!-- Main App Container -->
  <main class="container">

    <!-- KPI Summary Ribbon -->
    <div class="kpi-ribbon" id="kpi-ribbon">
      <!-- Injected via JavaScript -->
    </div>

    <!-- Filter & Search Toolbar -->
    <div class="filter-toolbar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="global-search-input" class="search-input" placeholder="Search by name, company, show, host, topic, hook, or notes..." oninput="handleSearchInput()">
      </div>

      <div class="filter-controls">
        <select id="status-filter-select" class="select-filter" onchange="handleFilterChange()">
          <option value="ALL">All Statuses</option>
          <!-- Injected dynamically based on active pipeline -->
        </select>

        <select id="category-filter-select" class="select-filter" onchange="handleFilterChange()">
          <option value="ALL">All Categories / Groups</option>
          <!-- Injected dynamically based on active pipeline -->
        </select>

        <select id="sort-order-select" class="select-filter" onchange="handleSortChange()">
          <option value="default">Sort: Default Order</option>
          <option value="alpha">Sort: Name (A-Z)</option>
          <option value="status">Sort: Status Priority</option>
        </select>
      </div>
    </div>

    <!-- Leads Display Container (Cards View) -->
    <div class="leads-grid" id="leads-cards-container">
      <!-- Injected via JavaScript -->
    </div>

    <!-- Leads Display Container (Table View) -->
    <div class="table-container" id="leads-table-container" style="display: none;">
      <table class="crm-table">
        <thead id="crm-table-head">
          <!-- Injected via JavaScript -->
        </thead>
        <tbody id="crm-table-body">
          <!-- Injected via JavaScript -->
        </tbody>
      </table>
    </div>

  </main>

  <!-- Add Lead Modal -->
  <div class="modal-overlay" id="add-lead-modal">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-title" id="modal-title-text">➕ Add New Lead</div>
        <button class="close-btn" onclick="closeAddLeadModal()">&times;</button>
      </div>

      <div class="form-group">
        <label class="form-label">Pipeline Type</label>
        <select id="new-lead-type" class="form-input" onchange="toggleModalFields()">
          <option value="media">🎙️ Podcast & Media Show</option>
          <option value="exec">💼 Executive & Dealmaker</option>
        </select>
      </div>

      <!-- Media Specific Fields -->
      <div id="modal-media-fields">
        <div class="form-group" style="margin-bottom: 10px;">
          <label class="form-label">Podcast Name *</label>
          <input type="text" id="new-show-name" class="form-input" placeholder="e.g. M&A Science, Venture Capital Today">
        </div>
        <div class="form-group" style="margin-bottom: 10px;">
          <label class="form-label">Host / Producer Contact</label>
          <input type="text" id="new-show-host" class="form-input" placeholder="e.g. Kison Patel">
        </div>
        <div class="form-group" style="margin-bottom: 10px;">
          <label class="form-label">Direct Contact Email</label>
          <input type="email" id="new-show-email" class="form-input" placeholder="e.g. bookings@show.com">
        </div>
      </div>

      <!-- Exec Specific Fields -->
      <div id="modal-exec-fields" style="display: none;">
        <div class="form-group" style="margin-bottom: 10px;">
          <label class="form-label">Executive Name *</label>
          <input type="text" id="new-exec-name" class="form-input" placeholder="e.g. Jason Godwin">
        </div>
        <div class="form-group" style="margin-bottom: 10px;">
          <label class="form-label">Entity / Company *</label>
          <input type="text" id="new-exec-company" class="form-input" placeholder="e.g. FBX, Norfund, tbh Ventures">
        </div>
        <div class="form-group" style="margin-bottom: 10px;">
          <label class="form-label">Priority & Strategic Group</label>
          <div style="display: flex; gap: 8px;">
            <select id="new-exec-priority" class="form-input" style="flex: 1;">
              <option value="P1">P1 - High Priority</option>
              <option value="P2">P2 - Secondary</option>
            </select>
            <select id="new-exec-group" class="form-input" style="flex: 2;">
              <option value="Group 1">Group 1: Co-investors</option>
              <option value="Group 2">Group 2: Operating Partners</option>
              <option value="Group 3">Group 3: Family Offices</option>
              <option value="Group 4">Group 4: Founders</option>
            </select>
          </div>
        </div>
        <div class="form-group" style="margin-bottom: 10px;">
          <label class="form-label">LinkedIn Profile URL</label>
          <input type="url" id="new-exec-linkedin" class="form-input" placeholder="https://www.linkedin.com/in/...">
        </div>
      </div>

      <div class="form-group" style="margin-bottom: 10px;">
        <label class="form-label">Engagement Hook / Angle</label>
        <textarea id="new-lead-hook" class="form-input" rows="2" placeholder="e.g. Behavioral due diligence, 93% implementation rate..."></textarea>
      </div>

      <div style="display: flex; justify-content: flex-end; gap: 10px; margin-top: 8px;">
        <button class="btn" onclick="closeAddLeadModal()">Cancel</button>
        <button class="btn btn-primary" onclick="submitNewLead()">Save Lead</button>
      </div>
    </div>
  </div>

  <!-- Toast Element -->
  <div id="toast">Changes saved</div>

  <!-- Client JavaScript -->
  <script>
    let activePipeline = 'media'; // 'media' or 'exec'
    let viewMode = 'cards'; // 'cards' or 'table'
    let mediaLeads = [];
    let execLeads = [];
    let searchQuery = '';
    let statusFilter = 'ALL';
    let categoryFilter = 'ALL';
    let sortOrder = 'default';

    const STATUS_OPTIONS_MEDIA = [
      'Identified',
      'Watch & Comment active',
      'Referral Outreach Sent',
      'Connection Message sent',
      'In a conversation with him',
      'Booked',
      'Researching'
    ];

    const STATUS_OPTIONS_EXEC = [
      'Identified',
      'Connected on Linkedin',
      'Active Conversation',
      'Connection Sent',
      'Connect on Linkedin, Message Sent',
      'Handshake Sent',
      'Pivot to Referral',
      'Linkedin Connection Accepted',
      'Email Sent',
      'Monitoring'
    ];

    // Load initial data
    async function loadAllData() {
      try {
        const [resMedia, resExec] = await Promise.all([
          fetch('/api/leads'),
          fetch('/api/executives')
        ]);
        mediaLeads = await resMedia.json();
        execLeads = await resExec.json();

        document.getElementById('badge-media-count').innerText = mediaLeads.length;
        document.getElementById('badge-exec-count').innerText = execLeads.length;

        updateFilterDropdowns();
        renderKPIs();
        renderLeads();
      } catch (err) {
        console.error('Error loading CRM leads:', err);
        showToast('Error loading CRM data');
      }
    }

    function switchPipeline(type) {
      activePipeline = type;
      document.querySelectorAll('.pipeline-tab').forEach(t => t.classList.remove('active'));
      if (type === 'media') {
        document.getElementById('tab-pipeline-media').classList.add('active');
      } else {
        document.getElementById('tab-pipeline-exec').classList.add('active');
      }
      statusFilter = 'ALL';
      categoryFilter = 'ALL';
      updateFilterDropdowns();
      renderKPIs();
      renderLeads();
    }

    function setViewMode(mode) {
      viewMode = mode;
      document.getElementById('view-cards-btn').classList.toggle('active', mode === 'cards');
      document.getElementById('view-table-btn').classList.toggle('active', mode === 'table');
      document.getElementById('leads-cards-container').style.display = mode === 'cards' ? 'grid' : 'none';
      document.getElementById('leads-table-container').style.display = mode === 'table' ? 'block' : 'none';
      renderLeads();
    }

    function updateFilterDropdowns() {
      const statusSelect = document.getElementById('status-filter-select');
      const catSelect = document.getElementById('category-filter-select');

      const statuses = activePipeline === 'media' ? STATUS_OPTIONS_MEDIA : STATUS_OPTIONS_EXEC;
      statusSelect.innerHTML = '<option value="ALL">All Statuses</option>' +
        statuses.map(s => `<option value="${escapeHtml(s)}">${escapeHtml(s)}</option>`).join('');

      if (activePipeline === 'media') {
        catSelect.innerHTML = `
          <option value="ALL">All Categories & Verticals</option>
          <option value="Operations">Operations & Productivity</option>
          <option value="Founder">Founder Psychology & Blindspots</option>
          <option value="Venture">Venture Capital & Scaleups</option>
          <option value="M&A">Private Equity & M&A Diligence</option>
          <option value="Governance">Compliance, Ethics & Fraud</option>
        `;
      } else {
        catSelect.innerHTML = `
          <option value="ALL">All Strategic Groups</option>
          <option value="Group 1">Group 1: Co-investors (ARCH, AIIM, Leapfrog)</option>
          <option value="Group 2">Group 2: Operating Partners (Atradius, IFU, Norfund)</option>
          <option value="Group 3">Group 3: Family Offices</option>
          <option value="Group 4">Group 4: Founders & Portco Execs</option>
        `;
      }
    }

    function renderKPIs() {
      const ribbon = document.getElementById('kpi-ribbon');
      if (activePipeline === 'media') {
        const total = mediaLeads.length;
        const activeConversations = mediaLeads.filter(l => (l.status || '').toLowerCase().includes('conversation') || (l.status || '').toLowerCase().includes('comment')).length;
        const outreachSent = mediaLeads.filter(l => (l.status || '').toLowerCase().includes('sent')).length;
        const booked = mediaLeads.filter(l => (l.status || '').toLowerCase().includes('booked')).length;
        const verifiedEmails = mediaLeads.filter(l => l.contact_email && l.contact_email.includes('@')).length;

        ribbon.innerHTML = `
          <div class="kpi-card">
            <span class="kpi-label">Target Media Shows</span>
            <span class="kpi-val sky">${total}</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Active Watch & Comments</span>
            <span class="kpi-val emerald">${activeConversations}</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Outreach & Referrals Sent</span>
            <span class="kpi-val amber">${outreachSent}</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Confirmed Booked</span>
            <span class="kpi-val purple">${booked}</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Direct Verified Emails</span>
            <span class="kpi-val sky">${verifiedEmails}</span>
          </div>
        `;
      } else {
        const total = execLeads.length;
        const p1Count = execLeads.filter(l => (l.priority || '').toUpperCase() === 'P1').length;
        const activeConversations = execLeads.filter(l => (l.status || '').toLowerCase().includes('conversation')).length;
        const connectedLinkedIn = execLeads.filter(l => (l.status || '').toLowerCase().includes('connected')).length;
        const sentOutreach = execLeads.filter(l => (l.status || '').toLowerCase().includes('sent')).length;

        ribbon.innerHTML = `
          <div class="kpi-card">
            <span class="kpi-label">Total Executive Leads</span>
            <span class="kpi-val purple">${total}</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">P1 Priority Targets</span>
            <span class="kpi-val amber">${p1Count}</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Active Conversations</span>
            <span class="kpi-val emerald">${activeConversations}</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Connected on LinkedIn</span>
            <span class="kpi-val sky">${connectedLinkedIn}</span>
          </div>
          <div class="kpi-card">
            <span class="kpi-label">Handshake / Pitch Sent</span>
            <span class="kpi-val amber">${sentOutreach}</span>
          </div>
        `;
      }
    }

    function handleSearchInput() {
      searchQuery = (document.getElementById('global-search-input').value || '').toLowerCase().trim();
      renderLeads();
    }

    function handleFilterChange() {
      statusFilter = document.getElementById('status-filter-select').value;
      categoryFilter = document.getElementById('category-filter-select').value;
      renderLeads();
    }

    function handleSortChange() {
      sortOrder = document.getElementById('sort-order-select').value;
      renderLeads();
    }

    function getFilteredLeads() {
      const rawLeads = activePipeline === 'media' ? mediaLeads : execLeads;
      return rawLeads.filter(lead => {
        // Status filter
        if (statusFilter !== 'ALL') {
          if ((lead.status || '').toLowerCase() !== statusFilter.toLowerCase()) return false;
        }

        // Category / Group filter
        if (categoryFilter !== 'ALL') {
          if (activePipeline === 'media') {
            const topicStr = ((lead.topic || '') + ' ' + (lead.genre || '') + ' ' + (lead.theme || '')).toLowerCase();
            if (!topicStr.includes(categoryFilter.toLowerCase())) return false;
          } else {
            const groupStr = (lead.group || '').toLowerCase();
            if (!groupStr.includes(categoryFilter.toLowerCase())) return false;
          }
        }

        // Search Query
        if (searchQuery) {
          const hay = Object.values(lead).map(v => typeof v === 'string' ? v : JSON.stringify(v)).join(' ').toLowerCase();
          if (!hay.includes(searchQuery)) return false;
        }

        return true;
      }).sort((a, b) => {
        if (sortOrder === 'alpha') {
          return (a.name || '').localeCompare(b.name || '');
        }
        if (sortOrder === 'status') {
          return (a.status || '').localeCompare(b.status || '');
        }
        return 0;
      });
    }

    function renderLeads() {
      const filtered = getFilteredLeads();
      if (viewMode === 'cards') {
        renderCardsView(filtered);
      } else {
        renderTableView(filtered);
      }
    }

    /* Cards View Rendering */
    function renderCardsView(leads) {
      const container = document.getElementById('leads-cards-container');
      if (leads.length === 0) {
        container.innerHTML = `<div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: var(--text-muted); background: var(--bg-surface); border-radius: 12px; border: 1px dashed var(--border);">No leads matching current search & filters.</div>`;
        return;
      }

      if (activePipeline === 'media') {
        container.innerHTML = leads.map(l => renderPodcastCard(l)).join('');
      } else {
        container.innerHTML = leads.map(l => renderExecutiveCard(l)).join('');
      }
    }

    function renderPodcastCard(lead) {
      const hasMultipleHosts = lead.hosts && lead.hosts.length > 1;
      const statusClass = (lead.status || '').toLowerCase().includes('booked') ? 'status-booked' :
                          (lead.status || '').toLowerCase().includes('conversation') ? 'status-active' :
                          (lead.status || '').toLowerCase().includes('comment') ? 'status-watch' :
                          (lead.status || '').toLowerCase().includes('sent') ? 'status-sent' : '';

      return `
        <div class="lead-card" id="card-${escapeHtml(lead.id)}">
          <div class="card-top">
            <div class="card-title-group">
              <div class="card-title">${escapeHtml(lead.name || 'Untitled Show')}</div>
              <div class="card-subtitle">
                <span class="pill-badge badge-media">${escapeHtml(lead.genre || lead.topic || 'Media')}</span>
                ${lead.reach_metrics ? `<span style="font-size: 11px; color: var(--text-muted);">• ${escapeHtml(lead.reach_metrics)}</span>` : ''}
              </div>
            </div>
            <div>
              <select class="status-select ${statusClass}" onchange="updatePodcastStatus('${escapeHtml(lead.id)}', this.value)">
                ${STATUS_OPTIONS_MEDIA.map(opt => `<option value="${escapeHtml(opt)}" ${lead.status === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join('')}
              </select>
            </div>
          </div>

          <!-- Verified Contacts & Co-Hosts -->
          ${hasMultipleHosts ? `
            <div class="host-subcards-list">
              <div style="font-size: 11px; font-weight: 700; color: #c084fc; text-transform: uppercase;">Co-Hosts (${lead.hosts.length}):</div>
              ${lead.hosts.map(h => `
                <div class="host-subcard">
                  <div class="host-subcard-header">
                    <div>
                      <div class="host-subcard-name">${escapeHtml(h.name)}</div>
                      <div class="host-subcard-role">${escapeHtml(h.role || '')}</div>
                    </div>
                    <div style="display: flex; gap: 4px;">
                      ${h.email ? `<button class="btn-xs" onclick="copyText('${escapeHtml(h.email)}')">Copy Email</button>` : ''}
                      ${h.linkedin_url ? `<a href="${h.linkedin_url}" target="_blank" class="btn-xs" style="text-decoration:none; color:#c084fc;">InMail</a>` : ''}
                    </div>
                  </div>
                  ${h.email ? `<div style="font-size: 11px; font-family: monospace; color: #38bdf8;">✉️ ${escapeHtml(h.email)}</div>` : ''}
                </div>
              `).join('')}
            </div>
          ` : `
            <div class="contact-box">
              <div class="contact-row">
                <div class="contact-target">
                  <span>🎙️ Host / Contact:</span>
                  <span style="color: #ffffff;">${escapeHtml(lead.host || 'Host')}</span>
                </div>
                ${lead.contact_email ? `
                  <div style="display: flex; gap: 4px;">
                    <button class="btn-xs" onclick="copyText('${escapeHtml(lead.contact_email)}')">Copy</button>
                    <a href="mailto:${escapeHtml(lead.contact_email)}" class="btn-xs" style="text-decoration:none;">Email</a>
                  </div>
                ` : ''}
              </div>
              <div class="contact-email-val">
                ${lead.contact_email ? `✉️ ${escapeHtml(lead.contact_email)}` : `<span style="color: var(--text-muted); font-size: 11px;">⚠️ Direct email not publicly listed</span>`}
              </div>
            </div>
          `}

          <!-- Video Watch & Comment Callout -->
          ${lead.video_url ? `
            <div>
              <a href="${lead.video_url}" target="_blank" class="link-pill pill-video-comment">
                <span>▶️ Active Commented YouTube Video (Open)</span>
              </a>
            </div>
          ` : ''}

          <!-- Show Links Toolbar -->
          <div class="links-toolbar">
            ${lead.website ? `<a href="${lead.website}" target="_blank" class="link-pill">🌐 Website</a>` : ''}
            ${lead.youtube_url ? `<a href="${lead.youtube_url}" target="_blank" class="link-pill pill-yt">▶️ YouTube</a>` : ''}
            ${lead.linkedin_url ? `<a href="${lead.linkedin_url}" target="_blank" class="link-pill pill-li">💼 LinkedIn</a>` : ''}
            ${lead.apple_url ? `<a href="${lead.apple_url}" target="_blank" class="link-pill">🍏 Apple</a>` : ''}
            ${lead.spotify_url ? `<a href="${lead.spotify_url}" target="_blank" class="link-pill">🎧 Spotify</a>` : ''}
          </div>

          <!-- Engagement Hook / Rupert Angle -->
          <div class="hook-box">
            <div class="hook-label">🎙️ Engagement Hook / Topic:</div>
            <div>${escapeHtml(lead.rupert_angle || lead.pitch_angle || lead.theme || 'Behavioral due diligence, people risk, and organizational fraud controls.')}</div>
          </div>

          <!-- Notes & Current Activity Field -->
          <div class="notes-section">
            <div class="notes-label">
              <span>Activity / Notes:</span>
              <button class="btn-xs" onclick="savePodcastNotes('${escapeHtml(lead.id)}')">Save Notes</button>
            </div>
            <textarea id="notes-${escapeHtml(lead.id)}" class="notes-input" placeholder="Add interaction notes, outreach history...">${escapeHtml(lead.current_activity || lead.notes || '')}</textarea>
          </div>
        </div>
      `;
    }

    function renderExecutiveCard(lead) {
      const statusClass = (lead.status || '').toLowerCase().includes('conversation') ? 'status-active' :
                          (lead.status || '').toLowerCase().includes('connected') ? 'status-booked' :
                          (lead.status || '').toLowerCase().includes('sent') ? 'status-sent' : '';

      return `
        <div class="lead-card" id="card-${escapeHtml(lead.id)}">
          <div class="card-top">
            <div class="card-title-group">
              <div class="card-title">${escapeHtml(lead.name || 'Unnamed Contact')}</div>
              <div class="card-subtitle">
                <span class="pill-badge badge-exec">${escapeHtml(lead.company || 'Enterprise')}</span>
                ${lead.priority ? `<span class="pill-badge badge-p1">${escapeHtml(lead.priority)}</span>` : ''}
                ${lead.group ? `<span class="pill-badge badge-group">${escapeHtml(lead.group)}</span>` : ''}
              </div>
            </div>
            <div>
              <select class="status-select ${statusClass}" onchange="updateExecutiveStatus('${escapeHtml(lead.id)}', this.value)">
                ${STATUS_OPTIONS_EXEC.map(opt => `<option value="${escapeHtml(opt)}" ${lead.status === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join('')}
              </select>
            </div>
          </div>

          <!-- Role / Title & Organization -->
          ${lead.title ? `<div style="font-size: 12px; color: #cbd5e1; font-weight: 500;">👔 ${escapeHtml(lead.title)}</div>` : ''}

          <!-- Contact Toolbar -->
          <div class="links-toolbar">
            ${lead.linkedin_url ? `<a href="${lead.linkedin_url}" target="_blank" class="link-pill pill-li">💼 View LinkedIn Profile</a>` : `<span style="font-size: 11px; color: var(--text-muted);">LinkedIn URL not mapped</span>`}
            ${lead.email ? `<a href="mailto:${lead.email}" class="link-pill">✉️ ${escapeHtml(lead.email)}</a>` : ''}
          </div>

          <!-- Strategic Hook / Dealmaker Angle -->
          <div class="hook-box hook-exec">
            <div class="hook-label label-exec">💼 Strategic Angle / Hook:</div>
            <div>${escapeHtml(lead.hook || 'Pre-deal people risk, behavioral due diligence, and cultural integration.')}</div>
          </div>

          <!-- Current Activity & Next Move -->
          <div class="notes-section">
            <div class="notes-label">
              <span>Pipeline Activity & Next Move:</span>
              <button class="btn-xs" onclick="saveExecutiveNotes('${escapeHtml(lead.id)}')">Save Activity</button>
            </div>
            <textarea id="notes-${escapeHtml(lead.id)}" class="notes-input" placeholder="Current activity, curiosity follow-ups, next steps...">${escapeHtml(lead.current_activity || lead.next_move || lead.notes || '')}</textarea>
          </div>
        </div>
      `;
    }

    /* Table View Rendering */
    function renderTableView(leads) {
      const thead = document.getElementById('crm-table-head');
      const tbody = document.getElementById('crm-table-body');

      if (activePipeline === 'media') {
        thead.innerHTML = `
          <tr>
            <th>Status</th>
            <th>Show Name</th>
            <th>Contact / Host</th>
            <th>Email</th>
            <th>Links</th>
            <th>Activity / Video</th>
            <th>Engagement Hook</th>
          </tr>
        `;

        if (leads.length === 0) {
          tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 30px; color: var(--text-muted);">No records found.</td></tr>`;
          return;
        }

        tbody.innerHTML = leads.map(l => `
          <tr>
            <td>
              <select class="status-select" onchange="updatePodcastStatus('${escapeHtml(l.id)}', this.value)">
                ${STATUS_OPTIONS_MEDIA.map(opt => `<option value="${escapeHtml(opt)}" ${l.status === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join('')}
              </select>
            </td>
            <td class="td-title">
              <div>${escapeHtml(l.name)}</div>
              <div style="font-size: 10px; color: var(--text-muted); font-weight: normal;">${escapeHtml(l.genre || l.topic || '')}</div>
            </td>
            <td>${escapeHtml(l.host || 'Host')}</td>
            <td>
              ${l.contact_email ? `
                <div style="display: flex; align-items: center; gap: 6px;">
                  <span style="font-family: monospace; color: #38bdf8;">${escapeHtml(l.contact_email)}</span>
                  <button class="btn-xs" onclick="copyText('${escapeHtml(l.contact_email)}')">Copy</button>
                </div>
              ` : '<span style="color: var(--text-muted);">-</span>'}
            </td>
            <td>
              <div style="display: flex; gap: 4px;">
                ${l.website ? `<a href="${l.website}" target="_blank" class="btn-xs">🌐</a>` : ''}
                ${l.youtube_url ? `<a href="${l.youtube_url}" target="_blank" class="btn-xs" style="color: #f43f5e;">▶️</a>` : ''}
                ${l.linkedin_url ? `<a href="${l.linkedin_url}" target="_blank" class="btn-xs" style="color: #38bdf8;">💼</a>` : ''}
              </div>
            </td>
            <td>
              ${l.video_url ? `<a href="${l.video_url}" target="_blank" class="btn-xs" style="color: #fda4af;">▶️ Watch Video</a>` : ''}
              <div style="font-size: 11px; color: var(--text-muted);">${escapeHtml(l.current_activity || '')}</div>
            </td>
            <td style="max-width: 320px; font-size: 11.5px; line-height: 1.4;">${escapeHtml(l.rupert_angle || l.pitch_angle || '')}</td>
          </tr>
        `).join('');
      } else {
        thead.innerHTML = `
          <tr>
            <th>Status</th>
            <th>Executive Name</th>
            <th>Entity / Company</th>
            <th>Priority & Group</th>
            <th>Activity</th>
            <th>Strategic Hook</th>
            <th>LinkedIn</th>
          </tr>
        `;

        if (leads.length === 0) {
          tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 30px; color: var(--text-muted);">No records found.</td></tr>`;
          return;
        }

        tbody.innerHTML = leads.map(l => `
          <tr>
            <td>
              <select class="status-select" onchange="updateExecutiveStatus('${escapeHtml(l.id)}', this.value)">
                ${STATUS_OPTIONS_EXEC.map(opt => `<option value="${escapeHtml(opt)}" ${l.status === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join('')}
              </select>
            </td>
            <td class="td-title">${escapeHtml(l.name)}</td>
            <td>
              <span class="pill-badge badge-exec">${escapeHtml(l.company)}</span>
            </td>
            <td>
              ${l.priority ? `<span class="pill-badge badge-p1">${escapeHtml(l.priority)}</span> ` : ''}
              <span style="font-size: 11px; color: var(--text-muted);">${escapeHtml(l.group || '')}</span>
            </td>
            <td style="font-size: 11px; max-width: 220px;">${escapeHtml(l.current_activity || '')}</td>
            <td style="max-width: 300px; font-size: 11.5px; line-height: 1.4;">${escapeHtml(l.hook || '')}</td>
            <td>
              ${l.linkedin_url ? `<a href="${l.linkedin_url}" target="_blank" class="btn-xs" style="color: #38bdf8;">💼 Profile</a>` : '<span style="color: var(--text-muted);">-</span>'}
            </td>
          </tr>
        `).join('');
      }
    }

    /* Inline Status Updates */
    async function updatePodcastStatus(id, newStatus) {
      const target = mediaLeads.find(l => l.id === id);
      if (target) target.status = newStatus;
      await fetch('/api/leads/update', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: id, status: newStatus })
      });
      renderKPIs();
      showToast(`Status updated to: ${newStatus}`);
    }

    async function updateExecutiveStatus(id, newStatus) {
      const target = execLeads.find(l => l.id === id);
      if (target) target.status = newStatus;
      await fetch('/api/executives/update', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: id, updates: { status: newStatus } })
      });
      renderKPIs();
      showToast(`Status updated to: ${newStatus}`);
    }

    /* Inline Notes Updates */
    async function savePodcastNotes(id) {
      const text = document.getElementById(`notes-${id}`)?.value || '';
      const target = mediaLeads.find(l => l.id === id);
      if (target) target.current_activity = text;
      await fetch('/api/leads/update', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: id, notes: text, current_activity: text })
      });
      showToast('Activity notes saved');
    }

    async function saveExecutiveNotes(id) {
      const text = document.getElementById(`notes-${id}`)?.value || '';
      const target = execLeads.find(l => l.id === id);
      if (target) target.current_activity = text;
      await fetch('/api/executives/update', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: id, updates: { current_activity: text } })
      });
      showToast('Executive activity saved');
    }

    /* Add Lead Modal Logic */
    function openAddLeadModal() {
      document.getElementById('add-lead-modal').classList.add('active');
    }
    function closeAddLeadModal() {
      document.getElementById('add-lead-modal').classList.remove('active');
    }
    function toggleModalFields() {
      const type = document.getElementById('new-lead-type').value;
      document.getElementById('modal-media-fields').style.display = type === 'media' ? 'block' : 'none';
      document.getElementById('modal-exec-fields').style.display = type === 'exec' ? 'block' : 'none';
    }

    async function submitNewLead() {
      const type = document.getElementById('new-lead-type').value;
      const hook = document.getElementById('new-lead-hook').value;

      if (type === 'media') {
        const name = document.getElementById('new-show-name').value.trim();
        if (!name) return alert('Podcast name is required');
        const host = document.getElementById('new-show-host').value.trim();
        const email = document.getElementById('new-show-email').value.trim();

        const newShow = {
          name: name,
          host: host,
          contact_email: email,
          rupert_angle: hook,
          status: 'Identified',
          media_type: 'Audio Podcast'
        };

        const res = await fetch('/api/leads/add', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newShow)
        });
        const created = await res.json();
        mediaLeads.unshift(created);
        showToast('Podcast added to directory');
      } else {
        const name = document.getElementById('new-exec-name').value.trim();
        const company = document.getElementById('new-exec-company').value.trim();
        if (!name || !company) return alert('Executive name and company are required');
        const priority = document.getElementById('new-exec-priority').value;
        const group = document.getElementById('new-exec-group').value;
        const li = document.getElementById('new-exec-linkedin').value.trim();

        const newExec = {
          name: name,
          company: company,
          priority: priority,
          group: group,
          linkedin_url: li,
          hook: hook,
          status: 'Identified'
        };

        const res = await fetch('/api/executives/add', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newExec)
        });
        const created = await res.json();
        execLeads.unshift(created);
        showToast('Executive lead saved');
      }

      closeAddLeadModal();
      document.getElementById('badge-media-count').innerText = mediaLeads.length;
      document.getElementById('badge-exec-count').innerText = execLeads.length;
      renderKPIs();
      renderLeads();
    }

    /* Clipboard Copy Utility */
    function copyText(str) {
      if (!str) return;
      navigator.clipboard.writeText(str).then(() => {
        showToast(`Copied to clipboard: ${str}`);
      }).catch(() => {
        showToast(`Copied: ${str}`);
      });
    }

    /* Toast Utility */
    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2500);
    }

    /* HTML Sanitizer */
    function escapeHtml(str) {
      if (!str) return '';
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // Initialize
    loadAllData();
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


@app.route("/api/leads/update", methods=["POST"])
def update_lead():
    data = request.get_json() or {}
    lead_id = data.get("id")
    status = data.get("status")
    notes = data.get("notes", "")
    angle = data.get("pitch_angle", "")
    current_activity = data.get("current_activity", "")

    tracker.update_status(lead_id, status=status, notes=notes, pitch_angle=angle)
    if current_activity and lead_id in tracker.leads:
        tracker.leads[lead_id]["current_activity"] = current_activity
        tracker.save()
    return jsonify({"success": True})


@app.route("/api/leads/add", methods=["POST"])
def add_lead():
    data = request.get_json() or {}
    lead_id = re.sub(r'[\W_]+', '_', data.get("name", "show").lower()).strip('_')
    data["id"] = lead_id
    tracker.add_or_update_lead(data)
    tracker.save()
    return jsonify(tracker.leads[lead_id])


@app.route("/api/executives")
def get_executives():
    return jsonify(exec_tracker.get_leads())


@app.route("/api/executives/update", methods=["POST"])
def update_executive():
    data = request.get_json() or {}
    lead_id = data.get("id")
    updates = data.get("updates", {})
    success = exec_tracker.update_lead(lead_id, updates)
    return jsonify({"success": success})


@app.route("/api/executives/add", methods=["POST"])
def add_executive():
    data = request.get_json() or {}
    lead_id = exec_tracker.add_lead(data)
    return jsonify(exec_tracker.leads[lead_id])


@app.route("/api/export/excel")
def export_excel():
    """Generates a dynamic multi-tab Excel workbook matching the Progress Sheet structure."""
    podcasts = tracker.get_leads()
    execs = exec_tracker.get_leads()

    wb = openpyxl.Workbook()

    # Tab 1: P4 - Podcast Prospects
    ws_p4 = wb.active
    ws_p4.title = "P4 - Podcast Prospects"
    ws_p4.append([
        "Podcast Name",
        "Target Contact",
        "Contact Details",
        "Website",
        "Status",
        "Current Activity",
        "Engagement Hook"
    ])

    for p in podcasts:
        ws_p4.append([
            p.get("name", ""),
            p.get("host", ""),
            p.get("contact_email", ""),
            p.get("website", ""),
            p.get("status", "Identified"),
            p.get("current_activity", ""),
            p.get("rupert_angle", "") or p.get("pitch_angle", "")
        ])

    # Tab 2: Master Leads & Outreach
    ws_mlo = wb.create_sheet("Master Leads & Outreach")
    ws_mlo.append([
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
    ])

    for e in execs:
        ws_mlo.append([
            e.get("name", ""),
            e.get("company", ""),
            e.get("type", "Cold"),
            e.get("priority", "P1"),
            e.get("group", ""),
            e.get("status", "Identified"),
            e.get("current_activity", ""),
            e.get("hook", ""),
            e.get("title", ""),
            e.get("next_move", ""),
            e.get("persona", ""),
            e.get("linkedin_url", "")
        ])

    buf = io.BytesIO()
    wb.save(buf)
    buf.seek(0)

    filename = f"Ethics_Insight_Progress_Sheet_{datetime.now().strftime('%Y%m%d')}.xlsx"
    return send_file(
        buf,
        as_attachment=True,
        download_name=filename,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


@app.route("/api/export/tsv")
def export_tsv():
    """Returns tab-separated values ready for instant pasting into Google Sheets (12 columns)."""
    leads = tracker.get_leads()
    output = io.StringIO()
    writer = csv.writer(output, delimiter="\t")
    
    headers = [
        "Name", "Entity / Company", "Type", "P-Category", "Group",
        "Status", "Current Activity", "Hook", "Title", "Next Move", "Persona", "Linkedin"
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

    return Response(output.getvalue(), mimetype="text/tab-separated-values")


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

    if engine in ["podcast", "all"]:
        podcast_results = search_podcasts(query=query, limit=limit)
        for show in podcast_results:
            show["media_type"] = "Audio Podcast"
            if enrich:
                rss_info = enrich_from_rss(show["feed_url"])
                show.update(rss_info)
            discovered.append(show)

    if engine in ["youtube", "all"] and search_youtube:
        yt_results = search_youtube(query=query, limit=limit)
        discovered.extend(yt_results)

    for show in discovered:
        tracker.add_or_update_lead(show)

    tracker.save()
    return jsonify(tracker.get_leads())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    host = os.environ.get("HOST", "0.0.0.0")
    print(f"[*] Starting Ethics Insight Media Dashboard on http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
