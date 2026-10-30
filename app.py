CRM_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Media & Executive Outreach CRM</title>
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
      padding: 9px 34px 9px 36px;
      color: #ffffff;
      font-size: 13.5px;
      outline: none;
      transition: border-color 0.15s;
    }
    .search-input:focus {
      border-color: var(--primary);
    }
    .search-clear-btn {
      position: absolute;
      right: 10px;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: var(--text-muted);
      border-radius: 50%;
      width: 20px;
      height: 20px;
      display: none;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 11px;
      font-weight: 700;
      line-height: 1;
      transition: all 0.15s;
    }
    .search-clear-btn:hover {
      background: rgba(255, 255, 255, 0.22);
      color: #ffffff;
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
      min-width: 55%;
    }
    .card-title {
      font-size: 16px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
      margin-bottom: 4px;
      overflow-wrap: break-word;
      word-break: normal;
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
    .btn-edit {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: #38bdf8;
      font-weight: 600;
    }
    .btn-edit:hover {
      background: rgba(56, 189, 248, 0.25);
      color: #ffffff;
      border-color: #38bdf8;
    }
    .btn-danger {
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.4);
      color: #fda4af;
      font-weight: 600;
    }
    .btn-danger:hover {
      background: rgba(244, 63, 94, 0.3);
      border-color: #f43f5e;
      color: #ffffff;
    }
    .modal-card-lg {
      max-width: 680px;
    }
    .form-row-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 10px;
    }
    @media (max-width: 600px) {
      .form-row-2col { grid-template-columns: 1fr; }
    }

    /* Preset & Discovery Chips */
    .preset-chips-wrap {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 6px;
      margin-bottom: 14px;
    }
    .preset-chip {
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.25);
      color: #7dd3fc;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11.5px;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.15s;
    }
    .preset-chip:hover {
      background: rgba(56, 189, 248, 0.22);
      border-color: #38bdf8;
      color: #ffffff;
    }
    .engine-radio-group {
      display: flex;
      gap: 8px;
      margin-top: 5px;
    }
    .engine-pill-label {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 7px;
      padding: 8px 12px;
      font-size: 12px;
      cursor: pointer;
      color: var(--text-muted);
      font-weight: 600;
      transition: all 0.15s;
      user-select: none;
    }
    .engine-pill-label input { display: none; }
    .engine-pill-label.active {
      background: rgba(56, 189, 248, 0.15);
      border-color: #38bdf8;
      color: #38bdf8;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.2);
    }
    .spinner-box {
      display: none;
      text-align: center;
      padding: 24px 10px;
      color: #38bdf8;
      font-size: 13.5px;
      font-weight: 600;
    }
    .spinner-icon {
      display: inline-block;
      animation: spin 1s linear infinite;
      font-size: 24px;
      margin-bottom: 8px;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }
  </style>
</head>
<body>

  <!-- Top Navigation Bar -->
  <header class="top-navbar">
    <div class="brand-section">
      <div class="brand-logo">🎙️</div>
      <div>
        <div class="brand-title">
          Media & Outreach
          <span class="brand-badge">CRM</span>
        </div>
        <div class="brand-sub">Executive Prospecting & Pipeline Intelligence</div>
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
      <a href="/content" class="pipeline-tab tab-content" style="text-decoration: none; border-color: rgba(139, 92, 246, 0.5); color: #c4b5fd;"><span>📝 Content Engine</span></a>
    </div>

    <!-- Top Action Buttons -->
    <div class="top-actions">
      <div class="view-toggle-group">
        <button class="view-btn active" id="view-cards-btn" onclick="setViewMode('cards')">🗂️ Cards</button>
        <button class="view-btn" id="view-table-btn" onclick="setViewMode('table')">📋 Table</button>
      </div>

      <button class="btn btn-primary" id="btn-discover-top" onclick="openDiscoverModal()" style="background: linear-gradient(135deg, #0284c7, #38bdf8); color: #070b14; font-weight: 800; border-color: #38bdf8; box-shadow: 0 0 12px rgba(56, 189, 248, 0.35);">
        <span>🌐 Search Online Directories</span>
      </button>

      <a href="/api/export/excel" class="btn btn-success" title="Download Excel Progress Sheet matching your format">
        <span>📥 Export Excel</span>
      </a>

      <button class="btn" onclick="openAddLeadModal()">
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
        <input type="text" id="global-search-input" class="search-input" placeholder="Search existing CRM leads (by show, host, company, topic, hook, notes...)" oninput="handleSearchInput()">
        <button id="search-clear-btn" class="search-clear-btn" onclick="clearSearchInput()" title="Clear search filter">✕</button>
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

  <!-- Edit Lead Modal -->
  <div class="modal-overlay" id="edit-lead-modal">
    <div class="modal-card modal-card-lg">
      <div class="modal-header">
        <div class="modal-title" id="edit-modal-title">✏️ Edit Lead</div>
        <button class="close-btn" onclick="closeEditLeadModal()">&times;</button>
      </div>

      <!-- Edit Media Fields -->
      <div id="edit-media-fields" style="display: none;">
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">Podcast Name</label>
            <input type="text" id="edit-show-name" class="form-input">
          </div>
          <div class="form-group">
            <label class="form-label">Host / Target Contact</label>
            <input type="text" id="edit-show-host" class="form-input">
          </div>
        </div>
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">Contact Email</label>
            <input type="email" id="edit-show-email" class="form-input">
          </div>
          <div class="form-group">
            <label class="form-label">Status</label>
            <select id="edit-show-status" class="form-input"></select>
          </div>
        </div>
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">Website URL</label>
            <input type="url" id="edit-show-website" class="form-input">
          </div>
          <div class="form-group">
            <label class="form-label">LinkedIn URL</label>
            <input type="url" id="edit-show-linkedin" class="form-input">
          </div>
        </div>
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">YouTube URL / Channel</label>
            <input type="url" id="edit-show-youtube" class="form-input">
          </div>
          <div class="form-group">
            <label class="form-label">Active Commented Video URL</label>
            <input type="url" id="edit-show-video-url" class="form-input">
          </div>
        </div>
        <div class="form-group" style="margin-bottom: 8px;">
          <label class="form-label">Topic / Genre / Reach</label>
          <input type="text" id="edit-show-topic" class="form-input">
        </div>
        <div class="form-group" style="margin-bottom: 8px;">
          <label class="form-label">Engagement Hook / Strategic Angle</label>
          <textarea id="edit-show-hook" class="form-input" rows="2"></textarea>
        </div>
        <div class="form-group" style="margin-bottom: 8px;">
          <label class="form-label">Current Activity & Interaction Notes</label>
          <textarea id="edit-show-activity" class="form-input" rows="2"></textarea>
        </div>
      </div>

      <!-- Edit Exec Fields -->
      <div id="edit-exec-fields" style="display: none;">
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">Executive Name</label>
            <input type="text" id="edit-exec-name" class="form-input">
          </div>
          <div class="form-group">
            <label class="form-label">Entity / Company</label>
            <input type="text" id="edit-exec-company" class="form-input">
          </div>
        </div>
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">Title / Role</label>
            <input type="text" id="edit-exec-title" class="form-input">
          </div>
          <div class="form-group">
            <label class="form-label">Status</label>
            <select id="edit-exec-status" class="form-input"></select>
          </div>
        </div>
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">Priority</label>
            <select id="edit-exec-priority" class="form-input">
              <option value="P1">P1 - High Priority</option>
              <option value="P2">P2 - Secondary</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Strategic Group</label>
            <select id="edit-exec-group" class="form-input">
              <option value="Group 1">Group 1: Co-investors (ARCH, AIIM, Leapfrog)</option>
              <option value="Group 2">Group 2: Operating Partners (Atradius, IFU, Norfund)</option>
              <option value="Group 3">Group 3: Family Offices</option>
              <option value="Group 4">Group 4: Founders & Portco Execs</option>
              <option value="Unassigned">Unassigned</option>
            </select>
          </div>
        </div>
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">Direct Email</label>
            <input type="email" id="edit-exec-email" class="form-input">
          </div>
          <div class="form-group">
            <label class="form-label">LinkedIn Profile URL</label>
            <input type="url" id="edit-exec-linkedin" class="form-input">
          </div>
        </div>
        <div class="form-group" style="margin-bottom: 8px;">
          <label class="form-label">Strategic Angle / Entry Hook</label>
          <textarea id="edit-exec-hook" class="form-input" rows="2"></textarea>
        </div>
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">Current Pipeline Activity</label>
            <input type="text" id="edit-exec-activity" class="form-input">
          </div>
          <div class="form-group">
            <label class="form-label">Next Move</label>
            <input type="text" id="edit-exec-next-move" class="form-input">
          </div>
        </div>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px; border-top: 1px solid var(--border); padding-top: 14px;">
        <button class="btn btn-danger" onclick="deleteLeadFromModal()">🗑️ Delete Lead</button>
        <div style="display: flex; gap: 8px;">
          <button class="btn" onclick="closeEditLeadModal()">Cancel</button>
          <button class="btn btn-primary" onclick="saveLeadEdits()">Save Changes</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Discover Podcasts Modal -->
  <div class="modal-overlay" id="discover-modal">
    <div class="modal-card modal-card-lg">
      <div class="modal-header">
        <div>
          <div class="modal-title">⚡ Discover New Podcasts & Video Shows</div>
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">
            Search Apple Podcasts, iTunes, RSS feeds & YouTube to find new shows and extract verified contacts.
          </div>
        </div>
        <button class="close-btn" onclick="closeDiscoverModal()">&times;</button>
      </div>

      <!-- Quick Preset Topic Chips -->
      <div>
        <label class="form-label">Suggested Topic Angles (Click to auto-fill):</label>
        <div class="preset-chips-wrap">
          <span class="preset-chip" onclick="selectPresetTopic('Corporate governance, risk management and operational compliance')">🛡️ Governance & Risk</span>
          <span class="preset-chip" onclick="selectPresetTopic('Operational friction, margin leakage and supply chain productivity')">⚙️ Operations & Margin</span>
          <span class="preset-chip" onclick="selectPresetTopic('Founder blindspots, executive mental health and scaleup resilience')">🧠 Founder Blindspots</span>
          <span class="preset-chip" onclick="selectPresetTopic('Private equity due diligence, M&A cultural integration and people risk')">💼 PE & M&A Diligence</span>
          <span class="preset-chip" onclick="selectPresetTopic('Venture capital diligence, early stage startup governance')">🚀 Venture Capital</span>
          <span class="preset-chip" onclick="selectPresetTopic('Family office direct investing, governance and character de-risking')">🏛️ Family Offices</span>
        </div>
      </div>

      <div class="form-row-2col">
        <div class="form-group">
          <label class="form-label">Topic / Focus Keywords *</label>
          <input type="text" id="discover-topic" class="form-input" placeholder="e.g. corporate compliance, private equity, fraud, M&A...">
        </div>
        <div class="form-group">
          <label class="form-label">Show Name (Optional)</label>
          <input type="text" id="discover-show-name" class="form-input" placeholder="e.g. The Diary Of A CEO, Masters in Business...">
        </div>
      </div>

      <div class="form-row-2col">
        <div class="form-group">
          <label class="form-label">Host Name or Professional Role (Optional)</label>
          <input type="text" id="discover-host" class="form-input" placeholder="e.g. Patrick O'Shaughnessy, General Partner, Investor...">
        </div>
        <div class="form-group">
          <label class="form-label">Results Limit</label>
          <select id="discover-limit" class="form-input">
            <option value="6">6 shows (Fast)</option>
            <option value="12" selected>12 shows (Recommended)</option>
            <option value="24">24 shows (Comprehensive)</option>
          </select>
        </div>
      </div>

      <div class="form-group" style="margin-bottom: 12px;">
        <label class="form-label">Search Source</label>
        <div class="engine-radio-group">
          <label class="engine-pill-label active" onclick="setDiscoveryEngine('all', this)">
            <input type="radio" name="discover-engine" value="all" checked>
            <span>🌐 All Media (Audio + Video)</span>
          </label>
          <label class="engine-pill-label" onclick="setDiscoveryEngine('podcast', this)">
            <input type="radio" name="discover-engine" value="podcast">
            <span>🎙️ Apple Podcasts & RSS</span>
          </label>
          <label class="engine-pill-label" onclick="setDiscoveryEngine('youtube', this)">
            <input type="radio" name="discover-engine" value="youtube">
            <span>▶️ YouTube Video Podcasts</span>
          </label>
        </div>
      </div>

      <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
        <input type="checkbox" id="discover-enrich" checked style="accent-color: var(--primary); cursor: pointer;">
        <label for="discover-enrich" style="font-size: 12px; color: #cbd5e1; cursor: pointer;">
          Auto-enrich contacts: Scrape RSS feed masthead for direct booking emails, Twitter, and website
        </label>
      </div>

      <!-- Spinner Box (Active during search) -->
      <div class="spinner-box" id="discover-spinner">
        <div class="spinner-icon">🔄</div>
        <div>Searching directories, extracting RSS feeds & generating outreach angles...</div>
        <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 4px;">This takes about 5 to 10 seconds.</div>
      </div>

      <!-- Action Buttons -->
      <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border); padding-top: 14px;" id="discover-actions">
        <button class="btn btn-success" onclick="autoDiscoverAllPresets()" title="Auto-crawl across core industry categories">
          <span>⚡ Auto-Discover 4 Core Niches</span>
        </button>
        <div style="display: flex; gap: 8px;">
          <button class="btn" onclick="closeDiscoverModal()">Cancel</button>
          <button class="btn btn-primary" onclick="performDiscoverySearch()" style="padding: 9px 20px; font-weight: 800;">
            <span>🔍 Search & Add to CRM</span>
          </button>
        </div>
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
          <option value="Governance">Governance, Risk & Strategy</option>
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
      const input = document.getElementById('global-search-input');
      const val = input ? input.value : '';
      searchQuery = val.toLowerCase().trim();
      const clearBtn = document.getElementById('search-clear-btn');
      if (clearBtn) {
        clearBtn.style.display = val ? 'flex' : 'none';
      }
      renderLeads();
    }

    function clearSearchInput() {
      const input = document.getElementById('global-search-input');
      if (input) {
        input.value = '';
        input.focus();
      }
      searchQuery = '';
      const clearBtn = document.getElementById('search-clear-btn');
      if (clearBtn) clearBtn.style.display = 'none';
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
        if (searchQuery) {
          container.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 45px 20px; color: var(--text-muted); background: var(--bg-surface); border-radius: 12px; border: 1px dashed var(--border);">
              <div style="font-size: 15px; font-weight: 600; color: #f1f5f9; margin-bottom: 6px;">
                No existing ${activePipeline === 'media' ? 'podcasts' : 'executives'} match "${escapeHtml(searchQuery)}"
              </div>
              <div style="font-size: 12.5px; color: var(--text-muted); margin-bottom: 16px;">
                ${activePipeline === 'media' ? 'Looking for a show not yet in your CRM? You can search external podcast directories & YouTube.' : 'This contact is not in your CRM database.'}
              </div>
              <div style="display: flex; gap: 10px; justify-content: center; align-items: center; flex-wrap: wrap;">
                <button class="btn btn-secondary" onclick="clearSearchInput()" style="padding: 7px 14px; font-size: 12px;">Clear Filter</button>
                ${activePipeline === 'media' ? `
                  <button class="btn btn-primary" onclick="openDiscoverModal('${escapeHtml(searchQuery)}')" style="padding: 7px 16px; font-size: 12px; font-weight: 700; background: linear-gradient(135deg, #0284c7, #38bdf8); color: #070b14;">
                    <span>🌐 Search Online Directories for "${escapeHtml(searchQuery)}"</span>
                  </button>
                ` : `
                  <button class="btn btn-primary" onclick="openAddLeadModal()" style="padding: 7px 16px; font-size: 12px;">
                    <span>➕ Add New Lead</span>
                  </button>
                `}
              </div>
            </div>
          `;
        } else {
          container.innerHTML = `<div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: var(--text-muted); background: var(--bg-surface); border-radius: 12px; border: 1px dashed var(--border);">No leads matching current filters.</div>`;
        }
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
              <div class="card-title" onclick="openEditLeadModal('${escapeHtml(lead.id)}', 'media')" style="cursor: pointer;" title="Click to edit">${escapeHtml(lead.name || 'Untitled Show')}</div>
              <div class="card-subtitle">
                <span class="pill-badge badge-media">${escapeHtml(lead.genre || lead.topic || 'Media')}</span>
                ${lead.reach_metrics ? `<span style="font-size: 11px; color: var(--text-muted);">• ${escapeHtml(lead.reach_metrics)}</span>` : ''}
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 6px; flex-shrink: 0;">
              <select class="status-select ${statusClass}" onchange="updatePodcastStatus('${escapeHtml(lead.id)}', this.value)">
                ${STATUS_OPTIONS_MEDIA.map(opt => `<option value="${escapeHtml(opt)}" ${lead.status === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join('')}
              </select>
              <button class="btn-xs btn-edit" onclick="openEditLeadModal('${escapeHtml(lead.id)}', 'media')" title="Edit show details">✏️ Edit</button>
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
            <a href="/content?source_lead=${encodeURIComponent(lead.id)}&pipeline=media" class="link-pill" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8;">📝 Synthesize</a>
            ${lead.website ? `<a href="${lead.website}" target="_blank" class="link-pill">🌐 Website</a>` : ''}
            ${lead.youtube_url ? `<a href="${lead.youtube_url}" target="_blank" class="link-pill pill-yt">▶️ YouTube</a>` : ''}
            ${lead.linkedin_url ? `<a href="${lead.linkedin_url}" target="_blank" class="link-pill pill-li">💼 LinkedIn</a>` : ''}
            ${lead.apple_url ? `<a href="${lead.apple_url}" target="_blank" class="link-pill">🍏 Apple</a>` : ''}
            ${lead.spotify_url ? `<a href="${lead.spotify_url}" target="_blank" class="link-pill">🎧 Spotify</a>` : ''}
          </div>

          <!-- Engagement Hook / Strategic Angle -->
          <div class="hook-box">
            <div class="hook-label">🎙️ Engagement Hook / Topic:</div>
            <div>${escapeHtml(lead.rupert_angle || lead.pitch_angle || lead.theme || 'Strategic discussion, executive insights, and industry leadership.')}</div>
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
              <div class="card-title" onclick="openEditLeadModal('${escapeHtml(lead.id)}', 'exec')" style="cursor: pointer;" title="Click to edit">${escapeHtml(lead.name || 'Unnamed Contact')}</div>
              <div class="card-subtitle">
                <span class="pill-badge badge-exec">${escapeHtml(lead.company || 'Enterprise')}</span>
                ${lead.priority ? `<span class="pill-badge badge-p1">${escapeHtml(lead.priority)}</span>` : ''}
                ${lead.group ? `<span class="pill-badge badge-group">${escapeHtml(lead.group)}</span>` : ''}
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 6px; flex-shrink: 0;">
              <select class="status-select ${statusClass}" onchange="updateExecutiveStatus('${escapeHtml(lead.id)}', this.value)">
                ${STATUS_OPTIONS_EXEC.map(opt => `<option value="${escapeHtml(opt)}" ${lead.status === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join('')}
              </select>
              <button class="btn-xs btn-edit" onclick="openEditLeadModal('${escapeHtml(lead.id)}', 'exec')" title="Edit lead details">✏️ Edit</button>
            </div>
          </div>

          <!-- Role / Title & Organization -->
          ${lead.title ? `<div style="font-size: 12px; color: #cbd5e1; font-weight: 500;">👔 ${escapeHtml(lead.title)}</div>` : ''}

          <!-- Contact Toolbar -->
          <div class="links-toolbar">
            <a href="/content?source_lead=${encodeURIComponent(lead.id)}&pipeline=exec" class="link-pill" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8;">📝 Synthesize</a>
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
            <th style="text-align: center;">Action</th>
          </tr>
        `;

        if (leads.length === 0) {
          if (searchQuery) {
            tbody.innerHTML = `
              <tr>
                <td colspan="8" style="text-align: center; padding: 40px; color: var(--text-muted);">
                  <div style="font-size: 14px; font-weight: 600; color: #f1f5f9; margin-bottom: 6px;">No existing podcasts match "${escapeHtml(searchQuery)}"</div>
                  <div style="margin-top: 10px; display: flex; gap: 10px; justify-content: center; align-items: center;">
                    <button class="btn btn-secondary" onclick="clearSearchInput()" style="padding: 6px 12px; font-size: 12px;">Clear Filter</button>
                    <button class="btn btn-primary" onclick="openDiscoverModal('${escapeHtml(searchQuery)}')" style="padding: 6px 14px; font-size: 12px; font-weight: 700; background: linear-gradient(135deg, #0284c7, #38bdf8); color: #070b14;">
                      <span>🌐 Search Online Directories for "${escapeHtml(searchQuery)}"</span>
                    </button>
                  </div>
                </td>
              </tr>
            `;
          } else {
            tbody.innerHTML = `<tr><td colspan="8" style="text-align: center; padding: 30px; color: var(--text-muted);">No records found.</td></tr>`;
          }
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
              <div onclick="openEditLeadModal('${escapeHtml(l.id)}', 'media')" style="cursor: pointer; text-decoration: underline dotted;" title="Click to edit">${escapeHtml(l.name)}</div>
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
            <td style="text-align: center;">
              <button class="btn-xs btn-edit" onclick="openEditLeadModal('${escapeHtml(l.id)}', 'media')" title="Edit show details">✏️ Edit</button>
            </td>
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
            <th style="text-align: center;">Action</th>
          </tr>
        `;

        if (leads.length === 0) {
          if (searchQuery) {
            tbody.innerHTML = `
              <tr>
                <td colspan="8" style="text-align: center; padding: 40px; color: var(--text-muted);">
                  <div style="font-size: 14px; font-weight: 600; color: #f1f5f9; margin-bottom: 6px;">No existing executives match "${escapeHtml(searchQuery)}"</div>
                  <div style="margin-top: 10px; display: flex; gap: 10px; justify-content: center; align-items: center;">
                    <button class="btn btn-secondary" onclick="clearSearchInput()" style="padding: 6px 12px; font-size: 12px;">Clear Filter</button>
                    <button class="btn btn-primary" onclick="openAddLeadModal()" style="padding: 6px 14px; font-size: 12px;">
                      <span>➕ Add New Lead</span>
                    </button>
                  </div>
                </td>
              </tr>
            `;
          } else {
            tbody.innerHTML = `<tr><td colspan="8" style="text-align: center; padding: 30px; color: var(--text-muted);">No records found.</td></tr>`;
          }
          return;
        }

        tbody.innerHTML = leads.map(l => `
          <tr>
            <td>
              <select class="status-select" onchange="updateExecutiveStatus('${escapeHtml(l.id)}', this.value)">
                ${STATUS_OPTIONS_EXEC.map(opt => `<option value="${escapeHtml(opt)}" ${l.status === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join('')}
              </select>
            </td>
            <td class="td-title">
              <span onclick="openEditLeadModal('${escapeHtml(l.id)}', 'exec')" style="cursor: pointer; text-decoration: underline dotted;" title="Click to edit">${escapeHtml(l.name)}</span>
            </td>
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
            <td style="text-align: center;">
              <button class="btn-xs btn-edit" onclick="openEditLeadModal('${escapeHtml(l.id)}', 'exec')" title="Edit lead details">✏️ Edit</button>
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

    /* Edit Lead Modal Logic */
    let editingLeadId = null;
    let editingPipelineType = null;

    function openEditLeadModal(id, type) {
      editingLeadId = id;
      editingPipelineType = type || activePipeline;

      const modal = document.getElementById('edit-lead-modal');
      const titleEl = document.getElementById('edit-modal-title');
      const mediaFields = document.getElementById('edit-media-fields');
      const execFields = document.getElementById('edit-exec-fields');

      if (editingPipelineType === 'media') {
        const lead = mediaLeads.find(l => l.id === id);
        if (!lead) return;
        titleEl.innerText = `✏️ Edit Podcast: ${lead.name || 'Show'}`;
        mediaFields.style.display = 'block';
        execFields.style.display = 'none';

        document.getElementById('edit-show-name').value = lead.name || '';
        document.getElementById('edit-show-host').value = lead.host || '';
        document.getElementById('edit-show-email').value = lead.contact_email || '';
        document.getElementById('edit-show-website').value = lead.website || '';
        document.getElementById('edit-show-linkedin').value = lead.linkedin_url || '';
        document.getElementById('edit-show-youtube').value = lead.youtube_url || '';
        document.getElementById('edit-show-video-url').value = lead.video_url || '';
        document.getElementById('edit-show-topic').value = lead.genre || lead.topic || '';
        document.getElementById('edit-show-hook').value = lead.rupert_angle || lead.pitch_angle || '';
        document.getElementById('edit-show-activity').value = lead.current_activity || lead.notes || '';

        const statusSelect = document.getElementById('edit-show-status');
        statusSelect.innerHTML = STATUS_OPTIONS_MEDIA.map(opt => `<option value="${escapeHtml(opt)}" ${lead.status === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join('');
      } else {
        const lead = execLeads.find(l => l.id === id);
        if (!lead) return;
        titleEl.innerText = `✏️ Edit Executive: ${lead.name || 'Lead'}`;
        mediaFields.style.display = 'none';
        execFields.style.display = 'block';

        document.getElementById('edit-exec-name').value = lead.name || '';
        document.getElementById('edit-exec-company').value = lead.company || '';
        document.getElementById('edit-exec-title').value = lead.title || '';
        document.getElementById('edit-exec-priority').value = lead.priority || 'P1';
        document.getElementById('edit-exec-group').value = lead.group || 'Unassigned';
        document.getElementById('edit-exec-email').value = lead.email || '';
        document.getElementById('edit-exec-linkedin').value = lead.linkedin_url || '';
        document.getElementById('edit-exec-hook').value = lead.hook || '';
        document.getElementById('edit-exec-activity').value = lead.current_activity || '';
        document.getElementById('edit-exec-next-move').value = lead.next_move || '';

        const statusSelect = document.getElementById('edit-exec-status');
        statusSelect.innerHTML = STATUS_OPTIONS_EXEC.map(opt => `<option value="${escapeHtml(opt)}" ${lead.status === opt ? 'selected' : ''}>${escapeHtml(opt)}</option>`).join('');
      }

      modal.classList.add('active');
    }

    function closeEditLeadModal() {
      document.getElementById('edit-lead-modal').classList.remove('active');
      editingLeadId = null;
      editingPipelineType = null;
    }

    async function saveLeadEdits() {
      if (!editingLeadId) return;

      if (editingPipelineType === 'media') {
        const name = document.getElementById('edit-show-name').value.trim();
        if (!name) return alert('Podcast name is required');

        const updates = {
          name: name,
          host: document.getElementById('edit-show-host').value.trim(),
          contact_email: document.getElementById('edit-show-email').value.trim(),
          status: document.getElementById('edit-show-status').value,
          website: document.getElementById('edit-show-website').value.trim(),
          linkedin_url: document.getElementById('edit-show-linkedin').value.trim(),
          youtube_url: document.getElementById('edit-show-youtube').value.trim(),
          video_url: document.getElementById('edit-show-video-url').value.trim(),
          topic: document.getElementById('edit-show-topic').value.trim(),
          genre: document.getElementById('edit-show-topic').value.trim(),
          rupert_angle: document.getElementById('edit-show-hook').value.trim(),
          current_activity: document.getElementById('edit-show-activity').value.trim(),
          notes: document.getElementById('edit-show-activity').value.trim()
        };

        const res = await fetch('/api/leads/update', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id: editingLeadId, updates: updates })
        });
        const data = await res.json();
        if (data.success) {
          const target = mediaLeads.find(l => l.id === editingLeadId);
          if (target) Object.assign(target, updates);
          showToast('Podcast updated successfully');
        }
      } else {
        const name = document.getElementById('edit-exec-name').value.trim();
        const company = document.getElementById('edit-exec-company').value.trim();
        if (!name || !company) return alert('Executive name and company are required');

        const updates = {
          name: name,
          company: company,
          title: document.getElementById('edit-exec-title').value.trim(),
          status: document.getElementById('edit-exec-status').value,
          priority: document.getElementById('edit-exec-priority').value,
          group: document.getElementById('edit-exec-group').value,
          email: document.getElementById('edit-exec-email').value.trim(),
          linkedin_url: document.getElementById('edit-exec-linkedin').value.trim(),
          hook: document.getElementById('edit-exec-hook').value.trim(),
          current_activity: document.getElementById('edit-exec-activity').value.trim(),
          next_move: document.getElementById('edit-exec-next-move').value.trim()
        };

        const res = await fetch('/api/executives/update', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id: editingLeadId, updates: updates })
        });
        const data = await res.json();
        if (data.success) {
          const target = execLeads.find(l => l.id === editingLeadId);
          if (target) Object.assign(target, updates);
          showToast('Executive lead updated successfully');
        }
      }

      closeEditLeadModal();
      renderKPIs();
      renderLeads();
    }

    async function deleteLeadFromModal() {
      if (!editingLeadId) return;
      if (!confirm('Are you sure you want to permanently delete this lead from the CRM?')) return;

      if (editingPipelineType === 'media') {
        await fetch('/api/leads/delete', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id: editingLeadId })
        });
        mediaLeads = mediaLeads.filter(l => l.id !== editingLeadId);
        document.getElementById('badge-media-count').innerText = mediaLeads.length;
        showToast('Podcast deleted');
      } else {
        await fetch('/api/executives/delete', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id: editingLeadId })
        });
        execLeads = execLeads.filter(l => l.id !== editingLeadId);
        document.getElementById('badge-exec-count').innerText = execLeads.length;
        showToast('Executive lead deleted');
      }

      closeEditLeadModal();
      renderKPIs();
      renderLeads();
    }

    /* Podcast Discovery Modal Logic */
    function openDiscoverModal(prefillQuery = '') {
      const modal = document.getElementById('discover-modal');
      if (prefillQuery && typeof prefillQuery === 'string') {
        document.getElementById('discover-topic').value = prefillQuery;
      }
      modal.classList.add('active');
    }

    function closeDiscoverModal() {
      document.getElementById('discover-modal').classList.remove('active');
      document.getElementById('discover-spinner').style.display = 'none';
      document.getElementById('discover-actions').style.display = 'flex';
    }

    function selectPresetTopic(topic) {
      document.getElementById('discover-topic').value = topic;
    }

    function setDiscoveryEngine(engine, element) {
      document.querySelectorAll('.engine-pill-label').forEach(el => el.classList.remove('active'));
      element.classList.add('active');
      element.querySelector('input').checked = true;
    }

    async function performDiscoverySearch() {
      const topic = (document.getElementById('discover-topic')?.value || '').trim();
      const showName = (document.getElementById('discover-show-name')?.value || '').trim();
      const host = (document.getElementById('discover-host')?.value || '').trim();
      const limit = parseInt(document.getElementById('discover-limit')?.value || '12');
      const enrich = document.getElementById('discover-enrich')?.checked !== false;

      const engineEl = document.querySelector('input[name="discover-engine"]:checked');
      const engine = engineEl ? engineEl.value : 'all';

      if (!topic && !showName && !host) {
        alert('Please enter a topic/keyword or show name to search.');
        return;
      }

      document.getElementById('discover-spinner').style.display = 'block';
      document.getElementById('discover-actions').style.display = 'none';
      showToast('Searching podcast directories & YouTube...');

      try {
        const res = await fetch('/api/search', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            topic: topic,
            name: showName,
            host: host,
            engine: engine,
            limit: limit,
            enrich: enrich
          })
        });
        const updatedLeads = await res.json();
        const beforeCount = mediaLeads.length;
        mediaLeads = updatedLeads;
        const newCount = mediaLeads.length - beforeCount;

        document.getElementById('badge-media-count').innerText = mediaLeads.length;
        closeDiscoverModal();
        switchPipeline('media');
        showToast(newCount > 0 ? `Discovered & added ${newCount} new shows!` : 'Search complete. Matching shows updated.');
      } catch (err) {
        console.error('Error during podcast discovery:', err);
        showToast('Error searching directories. Please try again.');
        document.getElementById('discover-spinner').style.display = 'none';
        document.getElementById('discover-actions').style.display = 'flex';
      }
    }

    async function autoDiscoverAllPresets() {
      document.getElementById('discover-spinner').style.display = 'block';
      document.getElementById('discover-actions').style.display = 'none';
      showToast('Running preset crawlers across Governance, M&A, VC & Productivity...');

      try {
        const res = await fetch('/api/search/presets', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        });
        const updatedLeads = await res.json();
        const beforeCount = mediaLeads.length;
        mediaLeads = updatedLeads;
        const newCount = mediaLeads.length - beforeCount;

        document.getElementById('badge-media-count').innerText = mediaLeads.length;
        closeDiscoverModal();
        switchPipeline('media');
        showToast(`Preset discovery complete! Added ${Math.max(0, newCount)} new shows.`);
      } catch (err) {
        console.error('Error running preset discovery:', err);
        showToast('Error discovering presets.');
        document.getElementById('discover-spinner').style.display = 'none';
        document.getElementById('discover-actions').style.display = 'flex';
      }
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

CONTENT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Content Engine | NotebookLM Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0b0f19;
      --bg-surface: #111827;
      --card-bg: #1e293b;
      --card-hover: #24344d;
      --border: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(56, 189, 248, 0.3);
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --accent: #10b981;
      --gold: #f59e0b;
      --purple: #a855f7;
      --rose: #f43f5e;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      overflow-x: hidden;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Top Navigation Bar */
    .top-navbar {
      background: rgba(17, 24, 39, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-badge {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: rgba(139, 92, 246, 0.15);
      border: 1px solid rgba(139, 92, 246, 0.4);
      color: #c084fc;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 19px;
      box-shadow: 0 0 14px rgba(139, 92, 246, 0.2);
    }
    .brand-title {
      font-size: 15.5px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.02em;
    }
    .brand-sub {
      font-size: 11px;
      color: var(--text-muted);
    }

    /* Studio View Switcher Tabs */
    .view-switcher-tabs {
      display: inline-flex;
      background: rgba(11, 15, 25, 0.8);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 3px;
      gap: 4px;
    }
    .view-tab-btn {
      background: transparent;
      color: var(--text-muted);
      border: 1px solid transparent;
      border-radius: 6px;
      padding: 6px 14px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .view-tab-btn:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.05);
    }
    .view-tab-btn.active {
      background: linear-gradient(135deg, #0284c7, #0ea5e9);
      color: #ffffff;
      border-color: #38bdf8;
      font-weight: 700;
      box-shadow: 0 0 12px rgba(14, 165, 233, 0.35);
    }

    /* Common Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: #cbd5e1;
      padding: 7px 14px;
      border-radius: 7px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .btn:hover {
      background: #1e293b;
      border-color: rgba(255, 255, 255, 0.2);
      color: #ffffff;
    }
    .btn-primary {
      background: linear-gradient(135deg, #0284c7, #0ea5e9);
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 0 12px rgba(14, 165, 233, 0.3);
    }
    .btn-primary:hover {
      background: linear-gradient(135deg, #0369a1, #0284c7);
      box-shadow: 0 0 16px rgba(14, 165, 233, 0.45);
      color: #ffffff;
    }
    .btn-secondary {
      background: rgba(30, 41, 59, 0.7);
      border-color: var(--border-accent);
      color: #7dd3fc;
    }
    .btn-xs {
      padding: 4px 10px;
      font-size: 11.5px;
      border-radius: 6px;
      font-weight: 600;
    }

    /* ==========================================================
       NotebookLM Studio Main Layout
       ========================================================== */
    .studio-wrapper {
      flex: 1;
      display: flex;
      overflow: hidden;
      height: calc(100vh - 61px);
    }

    /* Left Sidebar: Reference Sources (~310px) */
    .sources-sidebar {
      width: 310px;
      background: var(--bg-surface);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      transition: all 0.25s ease;
    }
    .sources-sidebar.collapsed {
      width: 0;
      opacity: 0;
      pointer-events: none;
    }
    .sidebar-header {
      padding: 16px 18px 12px 18px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .sidebar-title {
      font-size: 13.5px;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .sidebar-badge {
      font-size: 11px;
      background: rgba(56, 189, 248, 0.15);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 12px;
      padding: 2px 8px;
      font-weight: 700;
    }
    .add-source-pill-btn {
      width: 100%;
      background: rgba(56, 189, 248, 0.1);
      border: 1px dashed rgba(56, 189, 248, 0.35);
      color: #7dd3fc;
      border-radius: 8px;
      padding: 9px 12px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s ease;
      margin-bottom: 12px;
    }
    .add-source-pill-btn:hover {
      background: rgba(56, 189, 248, 0.18);
      border-color: #38bdf8;
      color: #ffffff;
    }
    .sources-scroll-list {
      flex: 1;
      overflow-y: auto;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .source-item-card {
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 9px 12px;
      transition: all 0.2s ease;
    }
    .source-item-card:hover {
      border-color: rgba(255, 255, 255, 0.18);
      background: #1e293b;
    }
    .source-item-card.inactive {
      opacity: 0.5;
    }
    .source-icon {
      font-size: 17px;
      flex-shrink: 0;
    }
    .source-details {
      flex: 1;
      min-width: 0;
    }
    .source-name-text {
      font-size: 12px;
      font-weight: 700;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .source-meta-text {
      font-size: 10.5px;
      color: var(--text-muted);
      display: flex;
      gap: 6px;
      align-items: center;
    }
    .source-del-icon {
      background: transparent;
      border: none;
      color: #64748b;
      cursor: pointer;
      font-size: 13px;
      padding: 2px 4px;
      border-radius: 4px;
      transition: all 0.2s;
    }
    .source-del-icon:hover {
      color: #f43f5e;
      background: rgba(244, 63, 94, 0.15);
    }
    .quick-links-area {
      border-top: 1px solid var(--border);
      padding: 12px 16px;
      background: rgba(11, 15, 25, 0.5);
    }
    .quick-links-title {
      font-size: 10.5px;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .quick-links-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      max-height: 120px;
      overflow-y: auto;
    }

    /* Right Main Canvas (ChatGPT / Gemini / NotebookLM centered look) */
    .chat-canvas {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: var(--bg);
      position: relative;
    }
    .chat-scroll-area {
      flex: 1;
      overflow-y: auto;
      padding: 20px 24px;
      scroll-behavior: smooth;
    }
    .chat-centered-container {
      max-width: 860px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 22px;
    }

    /* Welcome / Empty State */
    .gemini-welcome-box {
      text-align: center;
      padding: 48px 16px 24px 16px;
      max-width: 780px;
      margin: 0 auto;
    }
    .gemini-icon-glow {
      font-size: 38px;
      display: inline-block;
      margin-bottom: 12px;
    }
    .gemini-greeting {
      font-size: 26px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.025em;
      margin-bottom: 8px;
    }
    .gemini-sub {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 30px;
    }
    .gemini-prompt-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      text-align: left;
    }
    @media (max-width: 680px) {
      .gemini-prompt-grid { grid-template-columns: 1fr; }
    }
    .gemini-prompt-card {
      background: rgba(30, 41, 59, 0.45);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 14px 18px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .gemini-prompt-card:hover {
      background: rgba(30, 41, 59, 0.85);
      border-color: #38bdf8;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }
    .gemini-prompt-title {
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .gemini-prompt-desc {
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
    }

    /* Messages in Stream */
    .msg-user-bubble {
      align-self: flex-end;
      max-width: 80%;
      background: #1e3a8a;
      color: #ffffff;
      border-radius: 18px 18px 4px 18px;
      padding: 12px 18px;
      font-size: 14px;
      line-height: 1.5;
      box-shadow: 0 4px 14px rgba(30, 58, 138, 0.3);
    }
    .msg-assistant-bubble {
      align-self: flex-start;
      width: 100%;
      background: rgba(17, 24, 39, 0.7);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .assistant-meta-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 10px;
    }
    .assistant-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 700;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 12px;
      padding: 3px 10px;
    }
    .msg-markdown-content {
      font-size: 14px;
      color: #f1f5f9;
      line-height: 1.68;
    }
    .msg-markdown-content h3 { font-size: 15.5px; font-weight: 800; color: #fff; margin-bottom: 8px; margin-top: 14px; }
    .msg-markdown-content h4 { font-size: 14px; font-weight: 700; color: #38bdf8; margin-bottom: 6px; margin-top: 12px; }
    .msg-markdown-content p { margin-bottom: 10px; }
    .msg-markdown-content ul { margin-left: 20px; margin-bottom: 10px; }
    .msg-markdown-content li { margin-bottom: 5px; }

    /* Dossier Callout Box */
    .dossier-callout-box {
      background: rgba(7, 11, 20, 0.75);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 10px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .dossier-thesis-text {
      font-size: 13.5px;
      font-weight: 600;
      color: #ffffff;
      line-height: 1.5;
    }
    .dossier-tension-text {
      font-size: 13px;
      color: #cbd5e1;
      border-left: 2px solid #a855f7;
      padding-left: 10px;
      margin-top: 4px;
    }

    /* 4 Contrarian Angles Grid */
    .angles-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 4px;
    }
    @media (max-width: 680px) {
      .angles-grid { grid-template-columns: 1fr; }
    }
    .angle-card {
      background: rgba(7, 11, 20, 0.65);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 10px;
      transition: all 0.2s ease;
    }
    .angle-card:hover {
      border-color: #38bdf8;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.15);
    }
    .angle-card-badge {
      font-size: 10.5px;
      font-weight: 800;
      text-transform: uppercase;
      color: #c084fc;
      letter-spacing: 0.05em;
    }
    .angle-card-title {
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
    }
    .angle-card-hook {
      font-size: 12px;
      color: #38bdf8;
      font-style: italic;
      line-height: 1.4;
    }
    .angle-card-desc {
      font-size: 11.5px;
      color: var(--text-muted);
      line-height: 1.4;
    }
    .angle-card-btn {
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38bdf8;
      font-size: 11.5px;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
      width: 100%;
    }
    .angle-card-btn:hover {
      background: linear-gradient(135deg, #0284c7, #0ea5e9);
      color: #ffffff;
      border-color: #38bdf8;
    }

    /* Format Generator Action Bar */
    .format-action-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      background: rgba(7, 11, 20, 0.7);
      border: 1px solid var(--border-accent);
      border-radius: 8px;
      padding: 10px 14px;
    }
    .format-pill-btn {
      background: var(--card-bg);
      border: 1px solid var(--border-accent);
      color: #e2e8f0;
      font-size: 11.5px;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .format-pill-btn:hover {
      background: #1e293b;
      border-color: #38bdf8;
      color: #fff;
      transform: translateY(-1px);
    }
    .format-pill-btn.campaign {
      background: linear-gradient(135deg, rgba(244, 63, 94, 0.2), rgba(168, 85, 247, 0.2));
      border-color: rgba(244, 63, 94, 0.5);
      color: #fb7185;
    }
    .format-pill-btn.campaign:hover {
      background: linear-gradient(135deg, #f43f5e, #a855f7);
      color: #ffffff;
    }

    /* Inline Asset Widgets */
    .inline-asset-box {
      background: rgba(17, 24, 39, 0.85);
      border: 1px solid #38bdf8;
      border-radius: 10px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .inline-slide-display {
      background: #070b14;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      padding: 18px 24px;
      min-height: 120px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 8px;
    }

    /* Signature ChatGPT / Gemini Floating Bottom Input Capsule */
    .chat-bottom-wrapper {
      padding: 10px 20px 20px 20px;
      background: linear-gradient(180deg, rgba(11, 15, 25, 0) 0%, rgba(11, 15, 25, 0.95) 40%, #0b0f19 100%);
      width: 100%;
      flex-shrink: 0;
    }
    .chat-capsule {
      max-width: 840px;
      margin: 0 auto;
      background: #1e293b;
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 28px;
      padding: 6px 10px 6px 14px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.45);
      transition: all 0.2s ease;
    }
    .chat-capsule:focus-within {
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25), 0 8px 32px rgba(0, 0, 0, 0.5);
    }
    .capsule-btn-attach {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #94a3b8;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 16px;
      flex-shrink: 0;
      transition: all 0.2s;
    }
    .capsule-btn-attach:hover {
      background: rgba(255, 255, 255, 0.14);
      color: #ffffff;
      transform: scale(1.05);
    }
    .capsule-textarea {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      color: #ffffff;
      font-family: inherit;
      font-size: 14px;
      line-height: 1.45;
      resize: none;
      min-height: 26px;
      max-height: 130px;
      padding: 6px 0;
    }
    .capsule-btn-send {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: linear-gradient(135deg, #0284c7, #38bdf8);
      border: none;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 15px;
      flex-shrink: 0;
      transition: all 0.2s;
      box-shadow: 0 2px 8px rgba(56, 189, 248, 0.35);
    }
    .capsule-btn-send:hover {
      transform: scale(1.06);
      box-shadow: 0 4px 14px rgba(56, 189, 248, 0.55);
    }
    .capsule-status-caption {
      max-width: 840px;
      margin: 6px auto 0 auto;
      font-size: 11px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 14px;
    }

    /* ==========================================================
       Saved Library View & KPI Elements
       ========================================================= */
    .library-container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 20px 24px;
      width: 100%;
    }
    .kpi-ribbon {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-bottom: 20px;
    }
    .kpi-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px 18px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .kpi-card:hover {
      border-color: var(--border-accent);
      transform: translateY(-2px);
    }
    .kpi-label { font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; }
    .kpi-value { font-size: 24px; font-weight: 800; margin: 4px 0; }
    .kpi-sub { font-size: 11px; color: var(--text-muted); }

    .filter-toolbar {
      display: flex;
      gap: 12px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }
    .search-input-wrap {
      flex: 1;
      min-width: 280px;
      position: relative;
    }
    .search-input {
      width: 100%;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: #fff;
      padding: 10px 14px 10px 38px;
      border-radius: 8px;
      font-size: 13px;
      outline: none;
    }
    .search-input:focus { border-color: #38bdf8; }
    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
    }
    .select-filter {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: #fff;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 12.5px;
      outline: none;
    }

    .quick-pill {
      font-size: 11.5px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 14px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s;
    }
    .quick-pill:hover, .quick-pill.active {
      color: #fff;
      border-color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
    }
    .quick-pill.pill-cyan.active { border-color: #38bdf8; color: #38bdf8; }
    .quick-pill.pill-pink.active { border-color: #f43f5e; color: #fb7185; }
    .quick-pill.pill-purple.active { border-color: #a855f7; color: #c084fc; }
    .quick-pill.pill-emerald.active { border-color: #10b981; color: #34d399; }

    .content-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 16px;
    }
    .content-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: all 0.2s ease;
    }
    .content-card:hover {
      border-color: var(--border-accent);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    .tier-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      display: inline-block;
    }
    .tier-badge.t1 { background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.4); }
    .tier-badge.t2 { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
    .tier-badge.t3 { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
    .tier-badge.campaign { background: rgba(244, 63, 94, 0.2); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.4); }
    .tier-badge.research { background: rgba(14, 165, 233, 0.2); color: #7dd3fc; border: 1px solid rgba(14, 165, 233, 0.4); }

    /* Modals */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(6px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 200;
      padding: 20px;
    }
    .modal-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      width: 100%;
      max-width: 660px;
      max-height: 90vh;
      overflow-y: auto;
      padding: 24px;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
    }
    .modal-card-xl { max-width: 1050px; }
    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 12px;
      margin-bottom: 16px;
    }
    .modal-title { font-size: 16px; font-weight: 800; color: #ffffff; }
    .close-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 22px;
      cursor: pointer;
    }
    .close-btn:hover { color: #ffffff; }

    .drop-zone {
      border: 2px dashed rgba(56, 189, 248, 0.35);
      border-radius: 10px;
      padding: 28px 20px;
      text-align: center;
      cursor: pointer;
      background: rgba(7, 11, 20, 0.5);
      transition: all 0.2s ease;
    }
    .drop-zone:hover, .drop-zone.dragover {
      border-color: #38bdf8;
      background: rgba(56, 189, 248, 0.08);
    }
    .form-label {
      font-size: 12px;
      font-weight: 700;
      color: #cbd5e1;
      margin-bottom: 6px;
      display: block;
    }
    .form-input {
      width: 100%;
      background: #070b14;
      border: 1px solid var(--border);
      color: #ffffff;
      padding: 8px 12px;
      border-radius: 6px;
      font-family: inherit;
      font-size: 13px;
      outline: none;
    }
    .form-input:focus { border-color: #38bdf8; }

    /* Toast */
    #toast {
      position: fixed;
      bottom: 24px;
      right: 28px;
      background: #1e293b;
      color: #ffffff;
      border: 1px solid var(--border-accent);
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
      z-index: 300;
      opacity: 0;
      transform: translateY(12px);
      transition: all 0.25s ease;
      pointer-events: none;
    }
    #toast.show {
      opacity: 1;
      transform: translateY(0);
    }
  </style>
</head>
<body>

  <!-- Top Navigation Bar -->
  <header class="top-navbar">
    <div class="brand">
      <button class="btn btn-xs" id="sidebar-toggle-btn" onclick="toggleSourcesSidebar()" style="background: rgba(255, 255, 255, 0.06); border: 1px solid var(--border); color: #cbd5e1; padding: 6px 10px;" title="Toggle Reference Sources Sidebar">
        <span>📁 Sources</span>
      </button>
      <div class="brand-badge">📝</div>
      <div>
        <div class="brand-title" style="display: flex; align-items: center; gap: 8px;">
          <span>Content Engine | NotebookLM Studio</span>
          <span style="font-size: 11px; padding: 2px 8px; border-radius: 12px; background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35); display: inline-flex; align-items: center; gap: 6px; font-weight: 600;">
            <span style="width: 7px; height: 7px; border-radius: 50%; background: #10b981; box-shadow: 0 0 8px #10b981; display: inline-block;"></span>
            ⚡ Gemini Flash
          </span>
        </div>
        <div class="brand-sub">Interactive Research & Voice Synthesis Studio</div>
      </div>
    </div>

    <!-- View Switcher Tabs -->
    <div class="view-switcher-tabs">
      <button class="view-tab-btn active" id="tab-studio-view" onclick="switchMainView('studio')">
        💬 NotebookLM Studio
      </button>
      <button class="view-tab-btn" id="tab-library-view" onclick="switchMainView('library')">
        🗂️ Saved Library & Cards <span id="library-tab-count">(0)</span>
      </button>
    </div>

    <!-- Right Controls -->
    <div style="display: flex; align-items: center; gap: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
        <select id="voice-select-header" class="select-filter" onchange="onVoiceSelectHeaderChange(this.value)" style="font-weight: 700; background: var(--bg-surface); border-color: rgba(139, 92, 246, 0.4); color: #fff; max-width: 320px; cursor: pointer;">
          <option value="forensic-operator">🎙️ Rupert Evill / Forensic Risk</option>
          <option value="christian-hunt">🎙️ Christian Hunt / Human Risk</option>
          <option value="jordan-sabalo">🎙️ Jordan Sabalo / Tech & Growth</option>
          <option value="growth-dealmaker">🎙️ Strategic Dealmaker (PE & M&A)</option>
          <option value="__NEW__" style="color: #c4b5fd; font-weight: 700;">➕ Add / Clone Custom Voice...</option>
        </select>
        <button type="button" class="btn btn-xs" onclick="openVoiceModal()" style="background: rgba(139, 92, 246, 0.25); border: 1px solid rgba(139, 92, 246, 0.5); color: #c4b5fd; font-weight: 700; padding: 7px 14px; border-radius: 6px; display: inline-flex; align-items: center; gap: 5px; cursor: pointer; white-space: nowrap;" title="Create, Clone or Edit Author Voices">
          <span>➕ Custom Voice</span>
        </button>
      </div>
      
      <a href="/" class="btn" style="text-decoration:none;"><span>⬅️ Back to CRM Leads</span></a>
    </div>
  </header>

  <!-- ==========================================================
       VIEW 1: NotebookLM Studio View (Active by default)
       ========================================================== -->
  <div id="view-notebooklm-studio" class="studio-wrapper">

    <!-- Left Sidebar: Reference Sources Panel (~310px) -->
    <aside class="sources-sidebar sources-panel" id="sources-sidebar">
      <div class="sidebar-header">
        <div class="sidebar-title">
          <span>📁 Reference Sources</span>
          <span class="sidebar-badge" id="active-sources-count">0 active</span>
        </div>
      </div>

      <div class="sources-scroll-list" id="sources-list-container">
        <!-- 1-Click Add Source Button -->
        <button class="add-source-pill-btn" onclick="openAddSourceModal()">
          <span>➕ Add Reference Source</span>
        </button>

        <!-- Active Sources List -->
        <div id="sources-list" style="display: flex; flex-direction: column; gap: 8px;">
          <div style="text-align: center; padding: 24px 12px; color: var(--text-muted); font-size: 12px;">
            <div style="font-size: 22px; margin-bottom: 6px;">📂</div>
            No reference sources added yet.<br>
            <span style="font-size: 11px; opacity: 0.8;">Upload PDFs, DOCX, scrape URLs, or hook CRM leads.</span>
          </div>
        </div>
      </div>

      <!-- Quick Researched Links from CRM Dossiers -->
      <div class="quick-links-area">
        <div class="quick-links-title">
          <span>🔗 Researched Citations</span>
        </div>
        <div class="quick-links-chips" id="quick-researched-links">
          <!-- Populated via JS from /api/content/researched-links -->
        </div>
      </div>
    </aside>

    <!-- Right Main Canvas (ChatGPT / Gemini / NotebookLM centered style) -->
    <main class="chat-canvas">
      <div class="chat-scroll-area" id="chat-scroll-area">
        <div class="chat-centered-container" id="chat-messages-container">

          <!-- Centered Welcome / Empty State -->
          <div class="gemini-welcome-box" id="studio-welcome-card">
            <div class="gemini-icon-glow">🔬</div>
            <h1 class="gemini-greeting">What would you like to investigate today?</h1>
            <p class="gemini-sub">
              Ground your inquiry in active reference sources on the left, ask forensic questions, or explore provocative contrarian angles.
            </p>
            <div class="gemini-prompt-grid">
              <div class="gemini-prompt-card" onclick="sendStarterPrompt('Whistleblower retaliation patterns and why corporate hotlines expose informants')">
                <div class="gemini-prompt-title"><span>🔬 Whistleblower retaliation patterns</span></div>
                <div class="gemini-prompt-desc">Why corporate hotlines expose informants instead of protecting them.</div>
              </div>
              <div class="gemini-prompt-card" onclick="sendStarterPrompt('Why PE rollups fail in Year 1: operational integration and the destruction of goodwill')">
                <div class="gemini-prompt-title"><span>💼 Why PE rollups fail in Year 1</span></div>
                <div class="gemini-prompt-desc">How centralizing back-offices and destroying local autonomy murders deal multiples.</div>
              </div>
              <div class="gemini-prompt-card" onclick="sendStarterPrompt('Cross-border remote contractor wage theft and the digital erasure of behavioral friction')">
                <div class="gemini-prompt-title"><span>🌐 Cross-border contractor wage theft</span></div>
                <div class="gemini-prompt-desc">Digital distance and the psychological erasure of ethical friction in vendor desks.</div>
              </div>
              <div class="gemini-prompt-card" onclick="sendStarterPrompt('The Policy Wall Problem: Why pristine compliance binders create false boardroom security under commercial stress')">
                <div class="gemini-prompt-title"><span>⚖️ The Policy Wall Problem</span></div>
                <div class="gemini-prompt-desc">Why written codes fail 67% of frontline stress tests under commercial targets.</div>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- Signature ChatGPT / Gemini Floating Bottom Input Capsule -->
      <div class="chat-bottom-wrapper">
        <div class="chat-capsule">
          <button type="button" class="capsule-btn-attach" onclick="openAddSourceModal()" title="Attach PDF, Word DOCX, Web Link, or Notes">
            <span>📎</span>
          </button>
          <textarea id="chat-input-textarea" class="capsule-textarea" placeholder="Ask a research question, propose an angle, or request a format (e.g. 'make a carousel')..." rows="1" onkeydown="handleChatInputKey(event)" oninput="autoGrowChatInput(this)"></textarea>
          <button type="button" id="chat-send-btn" class="capsule-btn-send" onclick="submitNotebookChat()" title="Send Message">
            <span>➤</span>
          </button>
        </div>
        <div class="capsule-status-caption">
          <span id="chat-sources-status-pill">💡 0 active sources in prompt context (General forensic intelligence mode)</span>
          <span style="opacity: 0.7;">Shift+Enter for newline • Powered by Gemini Flash</span>
        </div>
      </div>
    </main>

  </div>

  <!-- ==========================================================
       VIEW 2: Saved Library & Content Cards Grid (Existing View)
       ========================================================== -->
  <div id="view-saved-library" style="display: none;" class="library-container">

    <!-- KPI Summary Ribbon -->
    <div class="kpi-ribbon" id="kpi-ribbon">
      <div class="kpi-card" onclick="setQuickTierFilter('ALL')">
        <div class="kpi-label">Total Content Pieces</div>
        <div class="kpi-value" id="kpi-total-content" style="color: #c084fc;">0</div>
        <div class="kpi-sub">Synthesized pieces</div>
      </div>
      <div class="kpi-card" onclick="setQuickTierFilter('Research')">
        <div class="kpi-label">🔬 Research Notebooks</div>
        <div class="kpi-value" id="kpi-research-count" style="color: #38bdf8;">0</div>
        <div class="kpi-sub">NotebookLM Dossiers</div>
      </div>
      <div class="kpi-card" onclick="setQuickTierFilter('Tier 1')">
        <div class="kpi-label">Tier 1: Carousels</div>
        <div class="kpi-value" id="kpi-t1-count" style="color: #a855f7;">0</div>
        <div class="kpi-sub">Swipeable slide decks</div>
      </div>
      <div class="kpi-card" onclick="setQuickTierFilter('Tier 2')">
        <div class="kpi-label">Tier 2: In-Feed Essays</div>
        <div class="kpi-value" id="kpi-t2-count" style="color: #10b981;">0</div>
        <div class="kpi-sub">Long-form narrative</div>
      </div>
      <div class="kpi-card" onclick="setQuickTierFilter('Tier 3')">
        <div class="kpi-label">Tier 3: Executive Briefings</div>
        <div class="kpi-value" id="kpi-t3-count" style="color: #38bdf8;">0</div>
        <div class="kpi-sub">Newsletter / Articles</div>
      </div>
      <div class="kpi-card" onclick="setQuickTierFilter('Campaign')">
        <div class="kpi-label">📦 Authority Campaign Packs</div>
        <div class="kpi-value" id="kpi-campaign-count" style="color: #f43f5e;">0</div>
        <div class="kpi-sub">1 Article + 5 Posts + 2 Decks</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Research Citations</div>
        <div class="kpi-value" id="kpi-facts-count" style="color: #f59e0b;">0</div>
        <div class="kpi-sub">Data points & quotes</div>
      </div>
    </div>

    <!-- Filter & Search Toolbar -->
    <div class="filter-toolbar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="content-search-input" class="search-input" placeholder="Filter previously saved content pieces..." oninput="handleContentSearch()">
      </div>

      <div style="display: flex; gap: 8px;">
        <select id="tier-filter-select" class="select-filter" onchange="handleFilterChange()">
          <option value="ALL">All Formats</option>
          <option value="Research">🔬 Research Notebooks (Dossiers)</option>
          <option value="Campaign">📦 Full Authority Campaign Packs</option>
          <option value="Tier 1">Tier 1: Swipeable Carousel</option>
          <option value="Tier 2">Tier 2: In-Feed Essay</option>
          <option value="Tier 3">Tier 3: Executive Briefing</option>
        </select>

        <select id="voice-filter-select" class="select-filter" onchange="handleFilterChange()">
          <option value="ALL">All Voices</option>
          <option value="forensic-operator">Forensic Risk Operator</option>
          <option value="growth-dealmaker">Strategic Dealmaker</option>
        </select>

        <select id="sort-order-select" class="select-filter" onchange="handleFilterChange()">
          <option value="newest">Sort: Newest First</option>
          <option value="oldest">Sort: Oldest First</option>
          <option value="alpha">Sort: Title (A-Z)</option>
        </select>
      </div>
    </div>

    <!-- Quick Filter Pills -->
    <div style="display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap;" id="quick-filter-pills">
      <span class="quick-pill active" id="qp-all" onclick="setQuickTierFilter('ALL')">All Formats <span id="pill-all-count">(0)</span></span>
      <span class="quick-pill pill-cyan" id="qp-research" onclick="setQuickTierFilter('Research')">🔬 Research Notebooks <span id="pill-research-count">(0)</span></span>
      <span class="quick-pill pill-pink" id="qp-campaign" onclick="setQuickTierFilter('Campaign')">📦 Campaign Packs <span id="pill-campaign-count">(0)</span></span>
      <span class="quick-pill pill-purple" id="qp-t1" onclick="setQuickTierFilter('Tier 1')">Tier 1: Carousels <span id="pill-t1-count">(0)</span></span>
      <span class="quick-pill pill-emerald" id="qp-t2" onclick="setQuickTierFilter('Tier 2')">Tier 2: Essays <span id="pill-t2-count">(0)</span></span>
      <span class="quick-pill" id="qp-t3" onclick="setQuickTierFilter('Tier 3')">Tier 3: Briefings <span id="pill-t3-count">(0)</span></span>
    </div>

    <!-- Content Cards Grid -->
    <div class="content-grid" id="content-cards-container">
      <!-- Injected via JavaScript -->
    </div>

  </div>

  <!-- ==========================================================
       MODAL: Add Reference Source to NotebookLM Studio
       ========================================================== -->
  <div class="modal-overlay" id="add-source-modal" style="display: none;">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-title">📁 Add Reference Source</div>
        <button class="close-btn" onclick="closeAddSourceModal()">&times;</button>
      </div>

      <!-- 4 Modal Tabs -->
      <div style="display: flex; gap: 4px; border-bottom: 1px solid var(--border); padding-bottom: 10px; margin-bottom: 14px;">
        <button class="view-tab-btn active" id="src-tab-btn-file" onclick="switchAddSourceTab('file')">📄 Upload File</button>
        <button class="view-tab-btn" id="src-tab-btn-url" onclick="switchAddSourceTab('url')">🌐 Web Links</button>
        <button class="view-tab-btn" id="src-tab-btn-text" onclick="switchAddSourceTab('text')">✍️ Notes / Text</button>
        <button class="view-tab-btn" id="src-tab-btn-crm" onclick="switchAddSourceTab('crm')">💼 CRM Lead Hook</button>
      </div>

      <!-- Tab 1: Upload File -->
      <div id="src-tab-file" class="src-tab-pane">
        <div class="drop-zone" id="file-drop-zone" onclick="document.getElementById('source-file-input').click()">
          <div style="font-size: 32px; margin-bottom: 8px;">📄</div>
          <div style="font-weight: 700; color: #fff; font-size: 14px;">Drag & drop reference file here, or click to browse</div>
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 4px;">Supports PDF (.pdf), Word (.docx), Plain Text (.txt), Markdown (.md)</div>
          <input type="file" id="source-file-input" style="display: none;" accept=".pdf,.docx,.doc,.txt,.md,.json,.csv" onchange="onSourceFileSelected(event)">
        </div>
        <div id="file-selected-info" style="display: none; margin-top: 12px; background: rgba(7, 11, 20, 0.6); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border); font-size: 13px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span id="file-selected-name" style="font-weight: 600; color: #38bdf8;"></span>
            <span id="file-selected-size" style="color: var(--text-muted); font-size: 11.5px;"></span>
          </div>
        </div>
        <div style="display: flex; justify-content: flex-end; gap: 8px; margin-top: 14px;">
          <button class="btn" onclick="closeAddSourceModal()">Cancel</button>
          <button class="btn btn-primary" id="upload-file-btn" onclick="uploadSourceFile()" style="font-weight: 700;" disabled>
            <span>⬆️ Upload & Extract Text</span>
          </button>
        </div>
      </div>

      <!-- Tab 2: Web Links -->
      <div id="src-tab-url" class="src-tab-pane" style="display: none;">
        <label class="form-label">Article or Webpage URLs (one per line):</label>
        <textarea id="source-url-input" class="form-input" style="height: 120px;" placeholder="https://example.com/investigation-article&#10;https://sec.gov/news/press-release/..."></textarea>
        <div style="display: flex; justify-content: flex-end; gap: 8px; margin-top: 14px;">
          <button class="btn" onclick="closeAddSourceModal()">Cancel</button>
          <button class="btn btn-primary" id="scrape-url-btn" onclick="scrapeSourceUrls()" style="font-weight: 700;">
            <span>🌐 Scrape & Ingest Links</span>
          </button>
        </div>
      </div>

      <!-- Tab 3: Paste Text / Notes -->
      <div id="src-tab-text" class="src-tab-pane" style="display: none;">
        <label class="form-label">Source / Note Title:</label>
        <input type="text" id="source-note-title" class="form-input" placeholder="e.g. Interview Notes with Former Chief Risk Officer" style="margin-bottom: 10px;">
        <label class="form-label">Raw Notes / Transcript Content:</label>
        <textarea id="source-note-text" class="form-input" style="height: 140px;" placeholder="Paste raw notes, investigation findings, meeting transcripts, or case studies here..."></textarea>
        <div style="display: flex; justify-content: flex-end; gap: 8px; margin-top: 14px;">
          <button class="btn" onclick="closeAddSourceModal()">Cancel</button>
          <button class="btn btn-primary" onclick="saveNoteSource()" style="font-weight: 700;">
            <span>✍️ Add Note as Source</span>
          </button>
        </div>
      </div>

      <!-- Tab 4: CRM Lead Hook -->
      <div id="src-tab-crm" class="src-tab-pane" style="display: none;">
        <div style="margin-bottom: 10px;">
          <input type="text" id="crm-leads-search" class="form-input" placeholder="🔍 Search across 72 Executives and 139 Podcasts..." oninput="filterCrmLeadsPicker(this.value)">
        </div>
        <div id="crm-leads-picker-container" style="max-height: 240px; overflow-y: auto; display: flex; flex-direction: column; gap: 8px; padding-right: 4px;">
          <!-- Loaded via JS -->
        </div>
        <div style="display: flex; justify-content: flex-end; margin-top: 12px;">
          <button class="btn" onclick="closeAddSourceModal()">Close</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Content View Modal (Slide Deck & Post Copy for Saved Library) -->
  <div class="modal-overlay" id="content-view-modal" style="display: none;">
    <div class="modal-card modal-card-xl">
      <div class="modal-header">
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
          <span id="view-content-tier-badge" class="tier-badge t1">Tier 1</span>
          <div class="modal-title" id="view-content-title">Content Title</div>
        </div>
        <button class="close-btn" onclick="closeContentViewModal()">&times;</button>
      </div>

      <!-- Campaign Pack Tab Navigation -->
      <div class="campaign-tabs-strip" id="campaign-tabs-strip" style="display: none; display: flex; gap: 6px; margin-bottom: 14px; border-bottom: 1px solid var(--border); padding-bottom: 10px; flex-wrap: wrap;">
        <button class="view-tab-btn active" id="camp-tab-btn-article" onclick="switchCampaignTab('article')">📖 Long Article</button>
        <button class="view-tab-btn" id="camp-tab-btn-posts" onclick="switchCampaignTab('posts')">📅 5-Day Posts</button>
        <button class="view-tab-btn" id="camp-tab-btn-c1" onclick="switchCampaignTab('c1')">🗂️ Problem Deck</button>
        <button class="view-tab-btn" id="camp-tab-btn-c2" onclick="switchCampaignTab('c2')">🗂️ Blueprint Deck</button>
        <button class="view-tab-btn" id="camp-tab-btn-dossier" onclick="switchCampaignTab('dossier')">🔬 Dossier</button>
        <button class="btn btn-xs" onclick="copyFullCampaignBundle()" style="margin-left: auto; color: #fb7185; border-color: rgba(244, 63, 94, 0.4);">📋 Copy Entire Bundle</button>
      </div>

      <!-- Campaign View: Long Article -->
      <div id="campaign-article-panel" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; background: rgba(7, 11, 20, 0.5); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border);">
          <span class="campaign-word-badge" id="article-word-count-badge" style="color: #38bdf8; font-weight: 700; font-size: 12px;">📖 2,150 words</span>
          <button class="btn btn-primary btn-xs" onclick="copyCampaignArticle()">📋 Copy Long Article</button>
        </div>
        <textarea id="campaign-article-textarea" class="form-input" style="height: 380px; font-family: inherit; font-size: 13px; line-height: 1.6;" readonly></textarea>
      </div>

      <!-- Campaign View: 5-Day Post Series -->
      <div id="campaign-posts-panel" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; background: rgba(7, 11, 20, 0.5); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border);">
          <div style="font-size: 12px; color: var(--text-muted);">5 Strategic Daily Feed Posts (Mon-Fri)</div>
          <button class="btn btn-primary btn-xs" onclick="copyAllPostsText()">📋 Copy All 5 Posts</button>
        </div>
        <div id="campaign-posts-list" style="max-height: 420px; overflow-y: auto; padding-right: 4px; display: flex; flex-direction: column; gap: 12px;"></div>
      </div>

      <!-- Campaign View: Carousel 1 -->
      <div id="campaign-c1-panel" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
          <span style="font-weight: 700; color: #fff; font-size: 13px;">Carousel 1: Problem Deconstruction Deck</span>
          <button class="btn btn-primary btn-xs" onclick="copyCarouselScript(1)">📑 Copy Deck Script</button>
        </div>
        <div id="c1-deck-style-guide"></div>
        <div class="inline-slide-display" id="c1-slide-card">
          <span id="c1-slide-number" style="font-size: 11px; font-weight: 800; color: #38bdf8; text-transform: uppercase;">#1</span>
          <div id="c1-slide-headline" style="font-size: 16px; font-weight: 800; color: #fff; margin-top: 4px; line-height: 1.35;">Headline</div>
          <div id="c1-slide-bullet" style="font-size: 13.5px; color: #cbd5e1; margin-top: 4px; line-height: 1.5;">Bullet text</div>
          <div id="c1-slide-visual-guide" style="margin-top: 12px;"></div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
          <button class="btn btn-xs" onclick="navigateCarousel(1, -1)">◀ Prev</button>
          <span id="c1-slide-counter-text" style="font-size: 12px; color: #38bdf8; font-weight: 700;">Slide 1 of 7</span>
          <button class="btn btn-xs" onclick="navigateCarousel(1, 1)">Next ▶</button>
        </div>
      </div>

      <!-- Campaign View: Carousel 2 -->
      <div id="campaign-c2-panel" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
          <span style="font-weight: 700; color: #fff; font-size: 13px;">Carousel 2: Tactical Operator Framework Deck</span>
          <button class="btn btn-primary btn-xs" onclick="copyCarouselScript(2)">📑 Copy Deck Script</button>
        </div>
        <div id="c2-deck-style-guide"></div>
        <div class="inline-slide-display" id="c2-slide-card">
          <span id="c2-slide-number" style="font-size: 11px; font-weight: 800; color: #38bdf8; text-transform: uppercase;">#1</span>
          <div id="c2-slide-headline" style="font-size: 16px; font-weight: 800; color: #fff; margin-top: 4px; line-height: 1.35;">Headline</div>
          <div id="c2-slide-bullet" style="font-size: 13.5px; color: #cbd5e1; margin-top: 4px; line-height: 1.5;">Bullet text</div>
          <div id="c2-slide-visual-guide" style="margin-top: 12px;"></div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
          <button class="btn btn-xs" onclick="navigateCarousel(2, -1)">◀ Prev</button>
          <span id="c2-slide-counter-text" style="font-size: 12px; color: #38bdf8; font-weight: 700;">Slide 1 of 7</span>
          <button class="btn btn-xs" onclick="navigateCarousel(2, 1)">Next ▶</button>
        </div>
      </div>

      <!-- Campaign View: Research Dossier -->
      <div id="campaign-dossier-panel" style="display: none;">
        <div class="dossier-callout-box">
          <div style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase;">Investigative Thesis</div>
          <div id="campaign-dossier-thesis" style="font-size: 13.5px; font-weight: 600; color: #fff;"></div>
          <div style="font-size: 11px; font-weight: 700; color: #c084fc; text-transform: uppercase; margin-top: 8px;">Unseen Frontline Tension</div>
          <div id="campaign-dossier-tension" style="font-size: 13px; color: #cbd5e1;"></div>
        </div>
      </div>

      <!-- Standard Single Asset Fallback -->
      <div id="single-asset-panel">
        <div id="single-tier1-deck-container" style="display: none; margin-bottom: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-weight: 700; color: #fff; font-size: 13px;">🗂️ Interactive Slide Deck & Art Direction Guide</span>
            <button class="btn btn-primary btn-xs" onclick="copySingleCarouselScript()">📑 Copy Full Deck Script</button>
          </div>
          <div id="single-deck-style-guide"></div>
          <div class="inline-slide-display" id="single-slide-card">
            <span id="single-slide-number" style="font-size: 11px; font-weight: 800; color: #38bdf8; text-transform: uppercase;">#1</span>
            <div id="single-slide-headline" style="font-size: 16px; font-weight: 800; color: #fff; margin-top: 4px; line-height: 1.35;">Headline</div>
            <div id="single-slide-bullet" style="font-size: 13.5px; color: #cbd5e1; margin-top: 4px; line-height: 1.5;">Bullet text</div>
            <div id="single-slide-visual-guide" style="margin-top: 12px;"></div>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
            <button class="btn btn-xs" onclick="navigateSingleCarousel(-1)">◀ Prev Slide</button>
            <span id="single-slide-counter-text" style="font-size: 12px; color: #38bdf8; font-weight: 700;">Slide 1 of 6</span>
            <button class="btn btn-xs" onclick="navigateSingleCarousel(1)">Next Slide ▶</button>
          </div>
        </div>
        <div id="single-markdown-label" style="font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 6px;">Companion Post Copy / Markdown</div>
        <textarea id="view-content-markdown" class="form-input" style="height: 320px; font-family: inherit; font-size: 13px; line-height: 1.6;" readonly></textarea>
        <div style="display: flex; justify-content: flex-end; gap: 8px; margin-top: 12px;">
          <button class="btn btn-primary btn-xs" onclick="copyMarkdown()">📋 Copy Content</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Author Voice Studio & Style Cloner Modal -->
  <div class="modal-overlay" id="voice-modal" style="display: none;">
    <div class="modal-card modal-card-xl" style="max-width: 800px;">
      <div class="modal-header">
        <div>
          <div class="modal-title" style="font-size: 18px; display: flex; align-items: center; gap: 8px;">
            <span>🎙️ Author Voice Studio & Style Cloner</span>
          </div>
          <div style="font-size: 12.5px; color: var(--text-muted); margin-top: 4px;">
            Train the AI on any executive, partner, or personal writing style. Paste past posts or articles to clone syntax, vocabulary, and cadence.
          </div>
        </div>
        <button class="close-btn" onclick="closeVoiceModal()">&times;</button>
      </div>

      <!-- Preset Quick-Select Buttons -->
      <div style="background: rgba(7, 11, 20, 0.6); border: 1px solid var(--border); border-radius: 8px; padding: 12px 14px; margin-bottom: 18px;">
        <div style="font-size: 11px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px;">
          ⚡ Load Preset or Clone From Scratch:
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <button type="button" class="btn btn-xs" onclick="applyVoicePreset('forensic-operator')" style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.35); color: #7dd3fc; font-weight: 600;">
            ⚡ Rupert Evill
          </button>
          <button type="button" class="btn btn-xs" onclick="applyVoicePreset('christian-hunt')" style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); color: #6ee7b7; font-weight: 600;">
            ⚡ Christian Hunt
          </button>
          <button type="button" class="btn btn-xs" onclick="applyVoicePreset('jordan-sabalo')" style="background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.35); color: #fcd34d; font-weight: 600;">
            ⚡ Jordan Sabalo
          </button>
          <button type="button" class="btn btn-xs" onclick="applyVoicePreset('growth-dealmaker')" style="background: rgba(139, 92, 246, 0.15); border: 1px solid rgba(139, 92, 246, 0.35); color: #c4b5fd; font-weight: 600;">
            ⚡ PE Dealmaker
          </button>
          <button type="button" class="btn btn-xs" onclick="applyVoicePreset('blank')" style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); color: #f1f5f9; font-weight: 600;">
            ✍️ Blank Slate
          </button>
        </div>
      </div>

      <!-- Form Grid -->
      <form id="voice-studio-form" onsubmit="event.preventDefault(); submitCustomVoice();">
        <input type="hidden" id="voice-id-input" value="">

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 14px;">
          <div>
            <label class="form-label" for="voice-name-input">Voice Name / Display Title *</label>
            <input type="text" id="voice-name-input" class="form-input" placeholder="e.g. Jordan Sabalo, Alex Vance / PE Operating Partner" required>
          </div>
          <div>
            <label class="form-label" for="voice-role-input">Professional Role / Title</label>
            <input type="text" id="voice-role-input" class="form-input" placeholder="e.g. Crisis Investigator, Tech Due Diligence Writer">
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 14px;">
          <div>
            <label class="form-label" for="voice-tone-input">Tone & Attitude</label>
            <input type="text" id="voice-tone-input" class="form-input" placeholder="e.g. Direct, contrarian, cynical operator, zero fluff">
          </div>
          <div>
            <label class="form-label" for="voice-cadence-input">Sentence Cadence & Formatting</label>
            <input type="text" id="voice-cadence-input" class="form-input" placeholder="e.g. Short punchy 1-2 sentence lines, double spacing">
          </div>
        </div>

        <div style="margin-bottom: 14px;">
          <label class="form-label" for="voice-philosophy-input">Core Worldview & Philosophy</label>
          <textarea id="voice-philosophy-input" class="form-input" style="height: 75px; line-height: 1.4;" placeholder="What is their contrarian thesis? How do they view corporate reality vs conventional compliance or PR?"></textarea>
        </div>

        <div style="margin-bottom: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <label class="form-label" for="voice-samples-input" style="margin-bottom: 0;">Writing Sample / Style Reference (The Cloner Textarea) 🧬</label>
            <span style="font-size: 11px; color: #a855f7; font-weight: 600;">AI analyzes grammar, rhythm, & mental models</span>
          </div>
          <textarea id="voice-samples-input" class="form-input" style="height: 140px; line-height: 1.5; font-family: inherit;" placeholder="Paste 1 to 3 previous LinkedIn posts, newsletters, or emails here to clone their exact voice..."></textarea>
        </div>

        <div style="margin-bottom: 18px;">
          <label class="form-label" for="voice-banned-input">Banned Words List (comma separated)</label>
          <input type="text" id="voice-banned-input" class="form-input" placeholder="delve, synergy, game-changer, seamless, exciting journey, holistic">
        </div>

        <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px; border-top: 1px solid var(--border); padding-top: 14px;">
          <button type="button" class="btn" onclick="closeVoiceModal()">Cancel</button>
          <button type="button" class="btn btn-primary" onclick="submitCustomVoice()" style="background: linear-gradient(135deg, #8b5cf6, #6366f1); border-color: #8b5cf6; font-weight: 700; padding: 8px 18px;">
            <span>🎙️ Save & Activate Voice</span>
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toast">Copied to clipboard!</div>

  <!-- Client JavaScript -->
  <script>
    let contentItems = [];
    let voiceProfiles = [];
    let activeVoiceId = 'forensic-operator';
    let mediaLeads = [];
    let execLeads = [];
    let tierFilter = 'ALL';
    let voiceFilter = 'ALL';
    let searchQuery = '';
    let sortOrder = 'newest';
    let researchedLinks = [];
    let crmLeadsSources = [];

    // NotebookLM Studio State
    let currentMainView = 'studio';
    let notebookSources = [];
    let notebookChatMessages = [];
    let isChatStreaming = false;
    let selectedFileForUpload = null;
    let currentModalContentItem = null;
    let currentC1Index = 0;
    let currentC2Index = 0;
    let currentCampaignTab = 'article';
    let isSidebarCollapsed = false;

    // Sidebar Toggle
    function toggleSourcesSidebar() {
      const sidebar = document.getElementById('sources-sidebar');
      if (sidebar) {
        isSidebarCollapsed = !isSidebarCollapsed;
        if (isSidebarCollapsed) {
          sidebar.classList.add('collapsed');
        } else {
          sidebar.classList.remove('collapsed');
        }
      }
    }

    // View Switcher: Studio vs Saved Library
    function switchMainView(view) {
      currentMainView = view;
      const studioView = document.getElementById('view-notebooklm-studio');
      const libraryView = document.getElementById('view-saved-library');
      const tabStudio = document.getElementById('tab-studio-view');
      const tabLibrary = document.getElementById('tab-library-view');

      if (view === 'studio') {
        if (studioView) studioView.style.display = 'flex';
        if (libraryView) libraryView.style.display = 'none';
        if (tabStudio) tabStudio.classList.add('active');
        if (tabLibrary) tabLibrary.classList.remove('active');
      } else {
        if (studioView) studioView.style.display = 'none';
        if (libraryView) libraryView.style.display = 'block';
        if (tabStudio) tabStudio.classList.remove('active');
        if (tabLibrary) tabLibrary.classList.add('active');
        renderContentGrid();
      }
    }

    // Load initial page data
    async function loadContentPageData() {
      try {
        const [resContent, resVoices, resMedia, resExec, resLinks] = await Promise.all([
          fetch('/api/content').then(r => r.json()).catch(() => []),
          fetch('/api/voices').then(r => r.json()).catch(() => []),
          fetch('/api/leads').then(r => r.json()).catch(() => []),
          fetch('/api/executives').then(r => r.json()).catch(() => []),
          fetch('/api/content/researched-links').then(r => r.json()).catch(() => [])
        ]);

        contentItems = Array.isArray(resContent) ? resContent : [];
        voiceProfiles = Array.isArray(resVoices) ? resVoices : [];
        mediaLeads = Array.isArray(resMedia) ? resMedia : [];
        execLeads = Array.isArray(resExec) ? resExec : [];
        researchedLinks = Array.isArray(resLinks) ? resLinks : [];

        renderVoiceDropdowns();
        updateCountersAndPills();
        renderQuickResearchedLinks();
        renderSourcesList();
        renderContentGrid();
        loadCrmLeadsForSources();
      } catch (err) {
        console.error('Error loading content data:', err);
      }
    }

    function updateCountersAndPills() {
      const total = contentItems.length;
      const tResearch = contentItems.filter(c => (c.tier || '').toLowerCase().includes('research') || (c.tier || '').includes('🔬')).length;
      const tCamp = contentItems.filter(c => ((c.tier || '').toLowerCase().includes('campaign') || !!c.campaign_pack) && !(c.tier || '').toLowerCase().includes('research')).length;
      const t1 = contentItems.filter(c => (c.tier || '').includes('Tier 1')).length;
      const t2 = contentItems.filter(c => (c.tier || '').includes('Tier 2')).length;
      const t3 = contentItems.filter(c => (c.tier || '').includes('Tier 3') || (c.tier || '').toLowerCase().includes('article')).length;
      const facts = contentItems.reduce((acc, c) => acc + ((c.research_dossier && c.research_dossier.data_points) ? c.research_dossier.data_points.length : 0), 0);

      document.getElementById('library-tab-count').innerText = `(${total})`;
      document.getElementById('kpi-total-content').innerText = total;
      document.getElementById('kpi-research-count').innerText = tResearch;
      document.getElementById('kpi-campaign-count').innerText = tCamp;
      document.getElementById('kpi-t1-count').innerText = t1;
      document.getElementById('kpi-t2-count').innerText = t2;
      document.getElementById('kpi-t3-count').innerText = t3;
      document.getElementById('kpi-facts-count').innerText = facts;

      document.getElementById('pill-all-count').innerText = `(${total})`;
      document.getElementById('pill-research-count').innerText = `(${tResearch})`;
      document.getElementById('pill-campaign-count').innerText = `(${tCamp})`;
      document.getElementById('pill-t1-count').innerText = `(${t1})`;
      document.getElementById('pill-t2-count').innerText = `(${t2})`;
      document.getElementById('pill-t3-count').innerText = `(${t3})`;
    }

    // ==========================================================
    // Author Voice Studio & Style Cloner
    // ==========================================================
    const VOICE_PRESETS = {
      'forensic-operator': {
        id: 'forensic-operator',
        name: 'Rupert Evill / Forensic Risk & Governance Operator',
        role: 'Crisis Investigator & Board Risk Advisor',
        philosophy: 'Corporate failures, corruption, and operational breakdowns are driven by human behaviour under pressure, never a lack of paperwork. Traditional compliance creates an illusion of security through 300-page codes and annual check-the-box training. Real ethics is enlightened self-interest and capital protection.',
        tone: 'Authoritative, analytical, contrarian yet constructive, grounded, zero corporate fluff, forensic insider.',
        cadence: 'Short 1-2 sentence lines with double spacing. Punchy, memorable mental models. Clear intention vs reality contrasts.',
        banned_words: 'delve, game-changer, holistic journey, agree?, synergy, paradigm shift, thought leadership, exciting times',
        sample_texts: [
          "The most dangerous thing a founder-led business can have isn't a scandal. It's a story that's too smooth.",
          "Fast decisions and a founder who 'reviews everything' can look like strength. Sometimes it is. Sometimes it's concentration risk wearing a good suit."
        ]
      },
      'christian-hunt': {
        id: 'christian-hunt',
        name: 'Christian Hunt / Human Risk & Behavioral Science',
        role: 'Author of Humanize Rules & Host of The Human Risk Podcast',
        philosophy: 'Human beings do not make decisions in sterile vacuums. Distance, digital screens, and cognitive friction change how people act. Compliance must be designed with human psychology in mind, not legal idealism.',
        tone: 'Witty, thoughtful, conversational, deeply psychological, behavioral-first.',
        cadence: 'Conversational storytelling, relatable analogies, sharp behavioral observations.',
        banned_words: 'delve, synergy, game-changer, seamless, exciting journey',
        sample_texts: [
          "If you design a process that requires saints to succeed under stress, your process is already broken.",
          "Distance turns theft into a one-click admin task."
        ]
      },
      'jordan-sabalo': {
        id: 'jordan-sabalo',
        name: 'Jordan Sabalo / Contrarian Tech & Growth Investigator',
        role: 'Tech Due Diligence & Economic Investigative Writer',
        philosophy: 'Corporate narratives in tech and remote work look pristine on LinkedIn while frontline reality is filled with unmeasured friction, wage arbitrage, and informal workarounds.',
        tone: 'Gritty, investigative, contrarian, empirical, narrative-driven.',
        cadence: 'Visceral micro-narratives (what happens at 2:15 AM), stark before-and-after contrasts, hard data.',
        banned_words: 'delve, tapestry, beacon, testament, holistic, revolutionize',
        sample_texts: [
          "'We're not just a company, we're a family' is the #1 warning sign that your invoice isn't getting paid.",
          "When an offshore worker is just a tiny Slack circle, the brain stops seeing a real person."
        ]
      },
      'growth-dealmaker': {
        id: 'growth-dealmaker',
        name: 'Strategic Dealmaker & M&A Operator',
        role: 'Private Equity Partner & Strategic Acquirer',
        philosophy: 'Value creation in M&A happens through operational discipline and cultural integration, not financial engineering. Pre-deal due diligence must price human risk and key-person dependencies before signing.',
        tone: 'Pragmatic, commercially sharp, direct, experienced, metric-informed.',
        cadence: 'Concise bullets, clear investment theses, stark risk-reward comparisons.',
        banned_words: 'revolutionary, disruptive, silver bullet, no-brainer, unicorn vibes',
        sample_texts: [
          "EBITDA multiples don't protect you when the head of supply chain walks out 30 days post-close.",
          "If your diligence team spent 40 hours auditing leases and 2 hours auditing management integrity, you didn't do diligence—you did paperwork."
        ]
      }
    };

    function renderVoiceDropdowns() {
      const headerSelect = document.getElementById('voice-select-header') || document.getElementById('studio-voice-select');
      const filterSelect = document.getElementById('voice-filter-select');

      if (headerSelect) {
        const curVal = activeVoiceId || headerSelect.value || 'forensic-operator';
        let optionsHtml = '';
        voiceProfiles.forEach(v => {
          const selected = (v.id === curVal) ? 'selected' : '';
          optionsHtml += `<option value="${escapeHtml(v.id)}" ${selected}>🎙️ ${escapeHtml(v.name)}</option>`;
        });
        optionsHtml += `<option value="__NEW__" style="color: #c4b5fd; font-weight: 700;">➕ Add / Clone Custom Voice...</option>`;
        headerSelect.innerHTML = optionsHtml;
        if (voiceProfiles.some(v => v.id === curVal)) {
          headerSelect.value = curVal;
        }
      }

      if (filterSelect) {
        const curFilter = voiceFilter || 'ALL';
        let filterHtml = `<option value="ALL">All Voices</option>`;
        voiceProfiles.forEach(v => {
          const selected = (v.id === curFilter) ? 'selected' : '';
          filterHtml += `<option value="${escapeHtml(v.id)}" ${selected}>${escapeHtml(v.name)}</option>`;
        });
        filterSelect.innerHTML = filterHtml;
      }
    }

    function onVoiceSelectHeaderChange(val) {
      if (val === '__NEW__') {
        openVoiceModal();
        const headerSelect = document.getElementById('voice-select-header') || document.getElementById('studio-voice-select');
        if (headerSelect && activeVoiceId) {
          headerSelect.value = activeVoiceId;
        }
        return;
      }
      activeVoiceId = val;
      const headerSelect = document.getElementById('voice-select-header');
      const voiceTitle = (headerSelect && headerSelect.selectedIndex >= 0 && headerSelect.options[headerSelect.selectedIndex]) ? headerSelect.options[headerSelect.selectedIndex].text : val;
      showToast('Switched author voice to: ' + voiceTitle);
    }

    function openVoiceModal(editVoiceId = null) {
      const modal = document.getElementById('voice-modal');
      if (!modal) return;
      if (editVoiceId) {
        applyVoicePreset(editVoiceId);
      } else {
        if (!document.getElementById('voice-name-input').value) {
          applyVoicePreset('blank');
        }
      }
      modal.style.display = 'flex';
    }

    function closeVoiceModal() {
      const modal = document.getElementById('voice-modal');
      if (modal) modal.style.display = 'none';
      const headerSelect = document.getElementById('voice-select-header') || document.getElementById('studio-voice-select');
      if (headerSelect && headerSelect.value === '__NEW__') {
        headerSelect.value = activeVoiceId || 'forensic-operator';
      }
    }

    function applyVoicePreset(presetKey) {
      if (presetKey === 'blank') {
        document.getElementById('voice-id-input').value = '';
        document.getElementById('voice-name-input').value = '';
        document.getElementById('voice-role-input').value = '';
        document.getElementById('voice-tone-input').value = '';
        document.getElementById('voice-cadence-input').value = '';
        document.getElementById('voice-philosophy-input').value = '';
        document.getElementById('voice-samples-input').value = '';
        document.getElementById('voice-banned-input').value = '';
        document.getElementById('voice-name-input').focus();
        return;
      }

      const preset = VOICE_PRESETS[presetKey] || voiceProfiles.find(v => v.id === presetKey);
      if (!preset) return;

      document.getElementById('voice-id-input').value = preset.id || '';
      document.getElementById('voice-name-input').value = preset.name || '';
      document.getElementById('voice-role-input').value = preset.role || '';
      document.getElementById('voice-tone-input').value = preset.tone || '';
      document.getElementById('voice-cadence-input').value = preset.cadence || '';
      document.getElementById('voice-philosophy-input').value = preset.philosophy || '';
      
      const sampleText = Array.isArray(preset.sample_texts) 
        ? preset.sample_texts.join(String.fromCharCode(10, 10)) 
        : (preset.sample_writing || preset.sample_texts || '');
      document.getElementById('voice-samples-input').value = sampleText;
      document.getElementById('voice-banned-input').value = preset.banned_words || '';
    }

    async function submitCustomVoice() {
      const name = document.getElementById('voice-name-input').value.trim();
      if (!name) {
        alert('Please provide a Voice Name / Display Title.');
        document.getElementById('voice-name-input').focus();
        return;
      }

      let voiceId = document.getElementById('voice-id-input').value.trim();
      if (!voiceId) {
        voiceId = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
        if (!voiceId) voiceId = 'voice-' + Date.now();
      }

      const role = document.getElementById('voice-role-input').value.trim();
      const tone = document.getElementById('voice-tone-input').value.trim();
      const cadence = document.getElementById('voice-cadence-input').value.trim();
      const philosophy = document.getElementById('voice-philosophy-input').value.trim();
      const samplesRaw = document.getElementById('voice-samples-input').value.trim();
      const bannedWords = document.getElementById('voice-banned-input').value.trim();

      const sampleTexts = samplesRaw ? samplesRaw.split(String.fromCharCode(10, 10)).map(s => s.trim()).filter(Boolean) : [];

      const payload = {
        id: voiceId,
        name: name,
        role: role,
        tone: tone,
        cadence: cadence,
        philosophy: philosophy,
        sample_texts: sampleTexts,
        sample_writing: samplesRaw,
        banned_words: bannedWords
      };

      try {
        const res = await fetch('/api/voices', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (!res.ok) {
          throw new Error('Server returned status ' + res.status);
        }

        const saved = await res.json();
        
        const existingIdx = voiceProfiles.findIndex(v => v.id === saved.id);
        if (existingIdx >= 0) {
          voiceProfiles[existingIdx] = saved;
        } else {
          voiceProfiles.push(saved);
        }

        activeVoiceId = saved.id;
        renderVoiceDropdowns();

        const headerSelect = document.getElementById('voice-select-header') || document.getElementById('studio-voice-select');
        if (headerSelect) {
          headerSelect.value = saved.id;
        }

        closeVoiceModal();
        showToast(`🎙️ Voice "${saved.name}" saved & activated!`);
      } catch (err) {
        console.error('Error saving custom voice:', err);
        alert('Failed to save custom voice: ' + err.message);
      }
    }

    // ==========================================================
    // Sources Management
    // ==========================================================
    function getSourceIcon(type) {
      if (type === 'pdf') return '📄';
      if (type === 'docx' || type === 'doc') return '📝';
      if (type === 'url') return '🌐';
      if (type === 'lead') return '💼';
      if (type === 'note') return '✍️';
      return '📄';
    }

    function renderSourcesList() {
      const container = document.getElementById('sources-list');
      const badge = document.getElementById('active-sources-count');
      const statusPill = document.getElementById('chat-sources-status-pill');
      if (!container) return;

      const activeCount = notebookSources.filter(s => s.active !== false).length;
      if (badge) badge.innerText = `${activeCount} active`;
      if (statusPill) {
        if (activeCount > 0) {
          statusPill.innerHTML = `<span>📌 <strong>${activeCount} reference source${activeCount > 1 ? 's' : ''}</strong> active in session context</span>`;
        } else {
          statusPill.innerHTML = `<span>💡 0 active sources (General forensic intelligence mode)</span>`;
        }
      }

      if (notebookSources.length === 0) {
        container.innerHTML = `
          <div style="text-align: center; padding: 24px 12px; color: var(--text-muted); font-size: 12px;">
            <div style="font-size: 22px; margin-bottom: 6px;">📂</div>
            No reference sources added yet.<br>
            <span style="font-size: 11px; opacity: 0.8;">Upload PDFs, DOCX, scrape URLs, or hook CRM leads.</span>
          </div>
        `;
        return;
      }

      container.innerHTML = notebookSources.map(s => {
        const isActive = s.active !== false;
        return `
          <div class="source-item-card ${isActive ? 'active' : 'inactive'}" id="src-card-${s.id}">
            <input type="checkbox" ${isActive ? 'checked' : ''} onchange="toggleSourceActive('${s.id}')" title="Include in research context">
            <div class="source-icon">${getSourceIcon(s.type)}</div>
            <div class="source-details">
              <div class="source-name-text" title="${escapeHtml(s.name)}">${escapeHtml(s.name)}</div>
              <div class="source-meta-text">
                <span>${s.size_label || (s.text ? s.text.length + ' chars' : 'Doc')}</span>
                <span>•</span>
                <span style="text-transform: uppercase;">${s.type}</span>
              </div>
            </div>
            <button class="source-del-icon" onclick="removeSource('${s.id}')" title="Remove source">✕</button>
          </div>
        `;
      }).join('');
    }

    function toggleSourceActive(sourceId) {
      const src = notebookSources.find(s => s.id === sourceId);
      if (src) {
        src.active = src.active === false ? true : false;
        renderSourcesList();
      }
    }

    function removeSource(sourceId) {
      notebookSources = notebookSources.filter(s => s.id !== sourceId);
      renderSourcesList();
      showToast('Source removed from session');
    }

    function renderQuickResearchedLinks() {
      const container = document.getElementById('quick-researched-links');
      if (!container) return;
      if (!researchedLinks || researchedLinks.length === 0) {
        container.innerHTML = '<span style="font-size: 11px; color: var(--text-muted);">No researched links found in saved dossiers.</span>';
        return;
      }

      container.innerHTML = researchedLinks.slice(0, 12).map(l => {
        let hostname = '';
        try { hostname = new URL(l.url).hostname.replace('www.', ''); } catch (e) { hostname = l.url; }
        const displayTitle = l.title && l.title !== l.url ? l.title : hostname;
        const truncated = displayTitle.length > 24 ? displayTitle.substring(0, 22) + '…' : displayTitle;
        return `
          <button type="button" class="btn-xs" style="background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3); color: #7dd3fc; border-radius: 12px; padding: 3px 8px; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; font-size: 10.5px;" onclick="addQuickCitationSource('${escapeHtml(l.url)}', '${escapeHtml(l.title || hostname)}')" title="${escapeHtml(l.title || l.url)}">
            <span>🔗 ${escapeHtml(truncated)}</span>
            <span style="opacity: 0.6; font-size: 9px;">+Add</span>
          </button>
        `;
      }).join('');
    }

    async function addQuickCitationSource(url, title) {
      const existing = notebookSources.find(s => s.url === url);
      if (existing) {
        showToast('Link already active as source');
        return;
      }
      showToast('Scraping citation link...');
      try {
        const res = await fetch('/api/content/notebook/scrape', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ url: url })
        });
        const data = await res.json();
        if (data.id) {
          data.active = true;
          notebookSources.unshift(data);
          renderSourcesList();
          showToast(`Added source: ${data.name.substring(0, 30)}`);
        }
      } catch (e) {
        console.error(e);
        showToast('Error scraping citation link');
      }
    }

    // ==========================================================
    // Add Source Modal Tabs & Handlers
    // ==========================================================
    function openAddSourceModal() {
      const modal = document.getElementById('add-source-modal');
      if (modal) modal.style.display = 'flex';
      switchAddSourceTab('file');
    }

    function closeAddSourceModal() {
      const modal = document.getElementById('add-source-modal');
      if (modal) modal.style.display = 'none';
      selectedFileForUpload = null;
      const fileInfo = document.getElementById('file-selected-info');
      if (fileInfo) fileInfo.style.display = 'none';
      const uploadBtn = document.getElementById('upload-file-btn');
      if (uploadBtn) uploadBtn.disabled = true;
    }

    function switchAddSourceTab(tab) {
      ['file', 'url', 'text', 'crm'].forEach(t => {
        const pane = document.getElementById(`src-tab-${t}`);
        const btn = document.getElementById(`src-tab-btn-${t}`);
        if (pane) pane.style.display = t === tab ? 'block' : 'none';
        if (btn) {
          if (t === tab) btn.classList.add('active');
          else btn.classList.remove('active');
        }
      });
      if (tab === 'crm') {
        renderCrmLeadsPicker();
      }
    }

    function onSourceFileSelected(e) {
      const file = e.target.files[0];
      if (!file) return;
      selectedFileForUpload = file;
      const fileInfo = document.getElementById('file-selected-info');
      const fileName = document.getElementById('file-selected-name');
      const fileSize = document.getElementById('file-selected-size');
      const uploadBtn = document.getElementById('upload-file-btn');

      if (fileInfo && fileName && fileSize && uploadBtn) {
        fileName.innerText = file.name;
        fileSize.innerText = `${(file.size / 1024).toFixed(1)} KB`;
        fileInfo.style.display = 'block';
        uploadBtn.disabled = false;
      }
    }

    const dropZone = document.getElementById('file-drop-zone');
    if (dropZone) {
      ['dragenter', 'dragover'].forEach(name => {
        dropZone.addEventListener(name, (e) => { e.preventDefault(); dropZone.classList.add('dragover'); });
      });
      ['dragleave', 'drop'].forEach(name => {
        dropZone.addEventListener(name, (e) => { e.preventDefault(); dropZone.classList.remove('dragover'); });
      });
      dropZone.addEventListener('drop', (e) => {
        if (e.dataTransfer.files.length) {
          onSourceFileSelected({ target: { files: e.dataTransfer.files } });
        }
      });
    }

    async function uploadSourceFile() {
      if (!selectedFileForUpload) return;
      const btn = document.getElementById('upload-file-btn');
      btn.disabled = true;
      btn.innerText = 'Extracting Text...';

      const formData = new FormData();
      formData.append('file', selectedFileForUpload);

      try {
        const res = await fetch('/api/content/notebook/upload', {
          method: 'POST',
          body: formData
        });
        const data = await res.json();
        if (data.id) {
          data.active = true;
          notebookSources.unshift(data);
          renderSourcesList();
          closeAddSourceModal();
          showToast(`Extracted ${data.name} (${data.size_label})`);
        } else {
          showToast(data.error || 'Upload error');
        }
      } catch (err) {
        console.error(err);
        showToast('Error uploading and parsing file');
      } finally {
        btn.disabled = false;
        btn.innerHTML = '<span>⬆️ Upload & Extract Text</span>';
      }
    }

    async function scrapeSourceUrls() {
      const textarea = document.getElementById('source-url-input');
      const btn = document.getElementById('scrape-url-btn');
      const rawUrls = (textarea ? textarea.value : '').trim();
      if (!rawUrls) {
        showToast('Please enter at least one URL');
        return;
      }

      btn.disabled = true;
      btn.innerText = 'Scraping articles...';

      const urls = rawUrls.split(/[\\r\\n,]+/).map(u => u.trim()).filter(u => u.startsWith('http'));
      if (urls.length === 0) {
        showToast('No valid http/https URLs found');
        btn.disabled = false;
        btn.innerHTML = '<span>🌐 Scrape & Ingest Links</span>';
        return;
      }

      let addedCount = 0;
      for (const u of urls) {
        try {
          const res = await fetch('/api/content/notebook/scrape', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: u })
          });
          const data = await res.json();
          if (data.id) {
            data.active = true;
            notebookSources.unshift(data);
            addedCount++;
          }
        } catch (e) {
          console.error(e);
        }
      }

      renderSourcesList();
      closeAddSourceModal();
      showToast(`Scraped and ingested ${addedCount} link source(s)!`);
      if (textarea) textarea.value = '';
      btn.disabled = false;
      btn.innerHTML = '<span>🌐 Scrape & Ingest Links</span>';
    }

    function saveNoteSource() {
      const titleInput = document.getElementById('source-note-title');
      const textInput = document.getElementById('source-note-text');
      const title = (titleInput ? titleInput.value : '').trim() || 'Custom Research Note';
      const text = (textInput ? textInput.value : '').trim();

      if (!text) {
        showToast('Please paste note or transcript text');
        return;
      }

      const noteSource = {
        id: `src_note_${Date.now()}_${Math.floor(Math.random()*1000)}`,
        name: title,
        type: 'note',
        text: text,
        size_label: `${text.length.toLocaleString()} chars`,
        active: true
      };

      notebookSources.unshift(noteSource);
      renderSourcesList();
      closeAddSourceModal();
      if (titleInput) titleInput.value = '';
      if (textInput) textInput.value = '';
      showToast(`Added note source: ${title}`);
    }

    async function loadCrmLeadsForSources() {
      try {
        const res = await fetch('/api/content/notebook/crm-leads');
        crmLeadsSources = await res.json();
      } catch (e) {
        console.error(e);
      }
    }

    function renderCrmLeadsPicker(query = '') {
      const container = document.getElementById('crm-leads-picker-container');
      if (!container) return;
      if (!crmLeadsSources || crmLeadsSources.length === 0) {
        container.innerHTML = '<div style="font-size: 12px; color: var(--text-muted); padding: 12px;">Loading CRM leads...</div>';
        return;
      }

      const q = query.toLowerCase().trim();
      const filtered = q
        ? crmLeadsSources.filter(l => (l.name || '').toLowerCase().includes(q) || (l.company || '').toLowerCase().includes(q) || (l.role || '').toLowerCase().includes(q))
        : crmLeadsSources;

      container.innerHTML = filtered.slice(0, 30).map(lead => {
        return `
          <div style="background: rgba(7, 11, 20, 0.6); border: 1px solid var(--border); border-radius: 8px; padding: 10px 12px; display: flex; justify-content: space-between; align-items: center; gap: 10px;">
            <div style="flex: 1; min-width: 0;">
              <div style="display: flex; align-items: center; gap: 6px;">
                <span class="tier-badge ${lead.category === 'Executive' ? 't1' : 't3'}" style="font-size: 10px; padding: 1px 6px;">${lead.category}</span>
                <span style="font-size: 12.5px; font-weight: 700; color: #fff; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${escapeHtml(lead.name)}</span>
              </div>
              <div style="font-size: 11px; color: #38bdf8; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${escapeHtml(lead.hook || lead.role)}</div>
            </div>
            <button class="btn btn-xs btn-primary" onclick="addCrmLeadSource('${escapeHtml(lead.id)}')" style="font-weight: 700;">
              <span>+ Add</span>
            </button>
          </div>
        `;
      }).join('');
    }

    function filterCrmLeadsPicker(val) {
      renderCrmLeadsPicker(val);
    }

    function addCrmLeadSource(leadId) {
      const lead = crmLeadsSources.find(l => l.id === leadId);
      if (!lead) return;
      const existing = notebookSources.find(s => s.id === lead.id);
      if (existing) {
        showToast('Lead already added as source');
        return;
      }

      const newSrc = {
        id: lead.id,
        name: lead.name,
        type: 'lead',
        text: lead.text,
        size_label: `${lead.text.length} chars`,
        active: true
      };

      notebookSources.unshift(newSrc);
      renderSourcesList();
      closeAddSourceModal();
      showToast(`Added CRM lead source: ${lead.name}`);
    }

    // ==========================================================
    // Chat & Synthesis Studio Stream
    // ==========================================================
    function autoGrowChatInput(textarea) {
      textarea.style.height = 'auto';
      textarea.style.height = `${Math.min(textarea.scrollHeight, 130)}px`;
    }

    function handleChatInputKey(e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        submitNotebookChat();
      }
    }

    function sendStarterPrompt(promptText) {
      return submitNotebookChat(promptText);
    }

    function selectContrarianAngle(angleTitle) {
      const text = `Refine and expand on Angle: "${angleTitle}". Challenge conventional compliance assumptions and detail the frontline operational proof points and diagnostics.`;
      return submitNotebookChat(text);
    }

    function triggerFormatGeneration(formatType) {
      const formatLabels = {
        carousel: 'Generate a 7-8 slide carousel deck with headlines, bullets, and companion copy script',
        essay: 'Generate a 600-900 word LinkedIn in-feed essay with punchy spacing and mental models',
        article: 'Generate a 2,000+ word investigative perspective article with sections, citations, and ground-truth case studies',
        weekly_posts: 'Generate a 5-day post series (Monday through Friday) designed for mobile dwell time',
        campaign_pack: 'Generate the entire full authority campaign pack (1 article, 5 posts, 2 carousels, citations)'
      };
      const text = formatLabels[formatType] || `Generate asset in format: ${formatType}`;
      return submitNotebookChat(text, formatType);
    }

    async function submitNotebookChat(customQuery = null, requestedFormat = null) {
      if (isChatStreaming) return;
      const textarea = document.getElementById('chat-input-textarea');
      const query = (customQuery || (textarea ? textarea.value : '')).trim();
      if (!query) return;

      if (!customQuery && textarea) {
        textarea.value = '';
        autoGrowChatInput(textarea);
      }

      // Hide welcome box once chat begins
      const welcomeCard = document.getElementById('studio-welcome-card');
      if (welcomeCard) welcomeCard.style.display = 'none';

      // 1. Append user message
      notebookChatMessages.push({ role: 'user', content: query });
      renderChatMessages();

      // 2. Render loading bubble
      const streamContainer = document.getElementById('chat-messages-container');
      const loadingCard = document.createElement('div');
      loadingCard.id = 'studio-loading-card';
      loadingCard.className = 'msg-assistant-bubble';
      loadingCard.innerHTML = `
        <div style="display: flex; align-items: center; gap: 10px; color: #38bdf8; font-weight: 700; font-size: 13.5px;">
          <span style="font-size: 20px; animation: spin 1s infinite linear;">⚡</span>
          <span>Forensic Intelligence Engine researching & synthesizing live sources...</span>
        </div>
      `;
      streamContainer.appendChild(loadingCard);
      const scrollArea = document.getElementById('chat-scroll-area');
      if (scrollArea) scrollArea.scrollTop = scrollArea.scrollHeight;
      isChatStreaming = true;

      // 3. API Call
      const headerSelect = document.getElementById('voice-select-header') || document.getElementById('studio-voice-select');
      const selectedVoice = headerSelect ? headerSelect.value : activeVoiceId;
      const activeSources = notebookSources.filter(s => s.active !== false);

      try {
        const res = await fetch('/api/content/notebook/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            messages: notebookChatMessages.map(m => ({ role: m.role, content: m.content })),
            sources: activeSources,
            voice_id: selectedVoice,
            requested_format: requestedFormat
          })
        });

        if (!res.ok) {
          const errData = await res.json().catch(() => ({}));
          throw new Error(errData.error || `Server returned ${res.status}: ${res.statusText}`);
        }

        const data = await res.json();
        const loadingEl = document.getElementById('studio-loading-card');
        if (loadingEl) loadingEl.remove();

        // 4. Append assistant message
        notebookChatMessages.push({
          role: 'assistant',
          content: data.reply_text || 'Research synthesis completed.',
          dossier: data.research_dossier || {},
          angles: data.suggested_angles || [],
          asset: data.generated_asset || null
        });

        renderChatMessages();

        if (data.generated_asset) {
          showToast(`Generated ${data.generated_asset.type} & saved to Library!`);
          fetch('/api/content').then(r => r.json()).then(items => {
            contentItems = items;
            updateCountersAndPills();
          }).catch(() => {});
        }
      } catch (err) {
        console.error('Notebook chat error:', err);
        const errMsg = (err && err.message) ? err.message : 'Error connecting to synthesis engine. Please try again.';
        showToast('Error: ' + errMsg);
        const loadingEl = document.getElementById('studio-loading-card');
        if (loadingEl) loadingEl.remove();
        notebookChatMessages.push({
          role: 'assistant',
          content: '⚠️ Error: ' + errMsg,
          dossier: {},
          angles: [],
          asset: null
        });
        renderChatMessages();
      } finally {
        isChatStreaming = false;
      }
    }

    function renderChatMessages() {
      const container = document.getElementById('chat-messages-container');
      if (!container) return;
      if (!notebookChatMessages || notebookChatMessages.length === 0) return;

      container.innerHTML = notebookChatMessages.map((msg, idx) => {
        if (msg.role === 'user') {
          return `
            <div class="msg-user-bubble">
              <div>${escapeHtml(msg.content)}</div>
            </div>
          `;
        }

        const voiceSelect = document.getElementById('voice-select-header') || document.getElementById('studio-voice-select');
        const voiceName = (voiceSelect && voiceSelect.selectedIndex >= 0 && voiceSelect.options[voiceSelect.selectedIndex]) ? voiceSelect.options[voiceSelect.selectedIndex].text : 'Forensic Risk Operator';

        let dossierHtml = '';
        if (msg.dossier && (msg.dossier.thesis || msg.dossier.unseen_tension || (msg.dossier.data_points && msg.dossier.data_points.length))) {
          const dataPointsHtml = (msg.dossier.data_points || []).slice(0, 4).map(dp => `
            <div style="font-size: 12px; color: #e2e8f0; display: flex; gap: 6px; align-items: flex-start;">
              <span style="color: #38bdf8; font-weight: 700;">•</span>
              <div>
                <strong>${escapeHtml(dp.source || 'Audit')}:</strong> ${escapeHtml(dp.fact || '')}
                ${dp.url ? `<a href="${dp.url}" target="_blank" style="color: #38bdf8; text-decoration: none; margin-left: 4px;">🔗</a>` : ''}
              </div>
            </div>
          `).join('');

          dossierHtml = `
            <div class="dossier-callout-box">
              <div style="font-size: 11px; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.05em;">Core Forensic Thesis & Frontline Tension</div>
              <div class="dossier-thesis-text">${escapeHtml(msg.dossier.thesis || '')}</div>
              <div class="dossier-tension-text">${escapeHtml(msg.dossier.unseen_tension || '')}</div>
              ${dataPointsHtml ? `
                <div style="border-top: 1px solid rgba(56, 189, 248, 0.2); padding-top: 8px; margin-top: 4px; display: flex; flex-direction: column; gap: 4px;">
                  ${dataPointsHtml}
                </div>
              ` : ''}
            </div>
          `;
        }

        let anglesHtml = '';
        if (msg.angles && msg.angles.length >= 4) {
          anglesHtml = `
            <div>
              <div style="font-size: 12px; font-weight: 800; color: #ffffff; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                <span>🎯 4 Provocative Contrarian Angles (Click to Refine):</span>
              </div>
              <div class="angles-grid">
                ${msg.angles.map(a => `
                  <div class="angle-card">
                    <div>
                      <div class="angle-card-badge">${escapeHtml(a.id || 'Angle')}</div>
                      <div class="angle-card-title" style="margin-top: 4px;">${escapeHtml(a.title)}</div>
                      <div class="angle-card-hook" style="margin-top: 4px;">"${escapeHtml(a.hook)}"</div>
                      <div class="angle-card-desc" style="margin-top: 6px;">${escapeHtml(a.description)}</div>
                    </div>
                    <button class="angle-card-btn" onclick="selectContrarianAngle('${escapeHtml(a.title)}')">
                      🎯 Select This Angle
                    </button>
                  </div>
                `).join('')}
              </div>
            </div>
          `;
        }

        const formatBarHtml = `
          <div class="format-action-bar">
            <span style="font-size: 11px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-right: 4px;">
              ⚡ 1-Click Generation:
            </span>
            <button class="format-pill-btn" onclick="triggerFormatGeneration('carousel')">
              <span>🗂️ Carousel Only</span>
            </button>
            <button class="format-pill-btn" onclick="triggerFormatGeneration('essay')">
              <span>📝 In-Feed Essay</span>
            </button>
            <button class="format-pill-btn" onclick="triggerFormatGeneration('article')">
              <span>📖 Long Article</span>
            </button>
            <button class="format-pill-btn" onclick="triggerFormatGeneration('weekly_posts')">
              <span>📅 5-Day Posts</span>
            </button>
            <button class="format-pill-btn campaign" onclick="triggerFormatGeneration('campaign_pack')">
              <span>📦 Full Campaign Pack</span>
            </button>
          </div>
        `;

        let assetHtml = '';
        if (msg.asset) {
          assetHtml = renderInlineAssetWidget(msg.asset, idx);
        }

        return `
          <div class="msg-assistant-bubble" id="msg-card-${idx}">
            <div class="assistant-meta-row">
              <span class="assistant-badge">⚡ ${voiceName}</span>
              <span style="font-size: 11.5px; color: var(--text-muted);">${new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}</span>
            </div>
            <div class="msg-markdown-content">${formatMarkdownText(msg.content)}</div>
            ${dossierHtml}
            ${anglesHtml}
            ${formatBarHtml}
            ${assetHtml}
          </div>
        `;
      }).join('');

      const scrollArea = document.getElementById('chat-scroll-area');
      if (scrollArea) scrollArea.scrollTop = scrollArea.scrollHeight;
    }

    function copyPromptDirect(btn) {
      if (!btn) return;
      const prompt = btn.getAttribute('data-prompt');
      if (!prompt) return;
      copyTextDirect(prompt);
      const origText = btn.innerHTML;
      btn.innerHTML = '✅ Copied Prompt!';
      btn.style.color = '#10b981';
      btn.style.borderColor = '#10b981';
      setTimeout(() => {
        btn.innerHTML = origText;
        btn.style.color = '#fbbf24';
        btn.style.borderColor = '#f59e0b';
      }, 2000);
    }

    function renderDeckStyleGuideBannerHtml(vsg) {
      if (!vsg || typeof vsg !== 'object') return '';
      const mood = escapeHtml(vsg.mood || 'Forensic institutional realism');
      const palette = escapeHtml(vsg.palette || 'Obsidian Slate, Hazard Amber, Bone White');
      const ratio = escapeHtml(vsg.aspect_ratio || '4:5 (1080x1350px)');
      const typography = vsg.typography_vibe ? escapeHtml(vsg.typography_vibe) : '';

      return `
        <div class="deck-style-guide-banner" style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 8px; padding: 10px 14px; margin-bottom: 12px; display: flex; flex-direction: column; gap: 5px;">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px;">
            <span style="font-size: 11px; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.5px;">🎨 Deck Visual Identity & Art Direction</span>
            <span style="font-size: 10.5px; background: rgba(56, 189, 248, 0.15); color: #7dd3fc; padding: 2px 8px; border-radius: 4px; font-weight: 700;">📐 ${ratio}</span>
          </div>
          <div style="font-size: 12px; color: #94a3b8;"><strong style="color: #cbd5e1;">Visual Mood:</strong> ${mood}</div>
          <div style="font-size: 12px; color: #94a3b8;"><strong style="color: #cbd5e1;">Color Palette:</strong> ${palette}</div>
          ${typography ? `<div style="font-size: 11.5px; color: #64748b;"><strong style="color: #94a3b8;">Typography:</strong> ${typography}</div>` : ''}
        </div>
      `;
    }

    function renderSlideCardHtml(slide, slideIndex, totalSlides) {
      if (!slide) return '';
      const slideType = escapeHtml(slide.type || ('Slide #' + (slideIndex + 1)));
      const headline = escapeHtml(slide.headline || '');
      const bullet = escapeHtml(slide.bullet || '');
      const visualConcept = slide.visual_concept ? escapeHtml(slide.visual_concept) : '';
      const imagePrompt = slide.image_prompt || '';
      const colorMood = slide.color_mood ? escapeHtml(slide.color_mood) : '';

      let visualHtml = '';
      if (visualConcept || imagePrompt) {
        visualHtml = `
          <div class="slide-visual-guide" style="margin-top: 12px; background: rgba(2, 6, 23, 0.85); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; flex-wrap: wrap; gap: 6px;">
              <div style="display: flex; align-items: center; gap: 6px;">
                <span style="font-size: 11.5px; font-weight: 800; color: #f59e0b;">🎨 Visual Direction</span>
                ${colorMood ? `<span style="font-size: 10px; background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); padding: 1px 6px; border-radius: 4px;">${colorMood}</span>` : ''}
              </div>
              ${imagePrompt ? `<button type="button" class="btn btn-xs copy-prompt-btn" style="background: rgba(245, 158, 11, 0.15); border-color: #f59e0b; color: #fbbf24; font-weight: 700; cursor: pointer;" onclick="copyPromptDirect(this)" data-prompt="${escapeHtml(imagePrompt)}">📋 Copy Image Prompt</button>` : ''}
            </div>
            ${visualConcept ? `<div style="font-size: 12px; color: #cbd5e1; line-height: 1.45; margin-bottom: 8px;"><strong style="color: #94a3b8;">Scene Concept:</strong> ${visualConcept}</div>` : ''}
            ${imagePrompt ? `
              <div style="background: #030712; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 6px; padding: 8px 10px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11px; color: #38bdf8; line-height: 1.5; white-space: pre-wrap; word-break: break-word;">
                <span style="color: #64748b; font-weight: 600; display: block; margin-bottom: 3px; font-family: inherit;">Midjourney / DALL-E / Canva AI Prompt:</span>${escapeHtml(imagePrompt)}
              </div>` : ''}
          </div>
        `;
      }

      return `
        <span style="font-size: 11px; font-weight: 800; color: #38bdf8; text-transform: uppercase;">${slideType}</span>
        <div style="font-size: 16px; font-weight: 800; color: #fff; margin-top: 4px; line-height: 1.35;">${headline}</div>
        <div style="font-size: 13.5px; color: #cbd5e1; margin-top: 6px; line-height: 1.5;">${bullet}</div>
        ${visualHtml}
      `;
    }

    function renderInlineAssetWidget(asset, msgIdx) {
      if (asset.type === 'carousel') {
        const slides = asset.slides || [];
        const currentSlide = slides[0] || {};
        const vsgHtml = renderDeckStyleGuideBannerHtml(asset.visual_style_guide);
        const slideHtml = renderSlideCardHtml(currentSlide, 0, slides.length);
        return `
          <div class="inline-asset-box" id="inline-carousel-viewer-${msgIdx}">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 8px; margin-bottom: 10px;">
              <span style="font-size: 13px; font-weight: 800; color: #38bdf8;">🗂️ Generated Carousel Deck: ${escapeHtml(asset.title || 'Slide Deck')}</span>
              <button class="btn btn-xs btn-primary" onclick="copyTextDirect('${escapeHtml(asset.copy_script || '')}')">📋 Copy Carousel Script</button>
            </div>
            ${vsgHtml}
            <div class="inline-slide-display" id="carousel-slide-box-${msgIdx}">
              ${slideHtml}
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
              <button class="btn btn-xs" onclick="navigateInlineCarousel(${msgIdx}, -1)">◀ Prev Slide</button>
              <span id="carousel-counter-${msgIdx}" style="font-size: 12px; color: #38bdf8; font-weight: 700;">Slide 1 of ${slides.length}</span>
              <button class="btn btn-xs" onclick="navigateInlineCarousel(${msgIdx}, 1)">Next Slide ▶</button>
            </div>
          </div>
        `;
      } else if (asset.type === 'essay') {
        return `
          <div class="inline-asset-box">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 8px;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 13px; font-weight: 800; color: #10b981;">📝 Generated In-Feed Essay</span>
                <span class="tier-badge t2" style="font-size: 10.5px;">⏱️ 3 min read</span>
              </div>
              <button class="btn btn-xs btn-primary" onclick="copyTextDirect('${escapeHtml(asset.markdown || '')}')">📋 Copy Essay</button>
            </div>
            <div style="background: rgba(7, 11, 20, 0.7); border: 1px solid var(--border); border-radius: 8px; padding: 14px; max-height: 280px; overflow-y: auto; font-size: 13px; line-height: 1.7; white-space: pre-wrap; color: #e2e8f0;">${escapeHtml(asset.markdown || '')}</div>
          </div>
        `;
      } else if (asset.type === 'article') {
        return `
          <div class="inline-asset-box">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 8px;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 13px; font-weight: 800; color: #38bdf8;">📖 Generated Investigative Perspective Article</span>
                <span class="tier-badge t3" style="font-size: 10.5px;">📖 ${asset.word_count || 2150} words</span>
              </div>
              <button class="btn btn-xs btn-primary" onclick="copyTextDirect('${escapeHtml(asset.markdown || '')}')">📋 Copy Full Article</button>
            </div>
            <div style="background: rgba(7, 11, 20, 0.7); border: 1px solid var(--border); border-radius: 8px; padding: 14px; max-height: 320px; overflow-y: auto; font-size: 13px; line-height: 1.7; white-space: pre-wrap; color: #e2e8f0;">${escapeHtml(asset.markdown || '')}</div>
          </div>
        `;
      } else if (asset.type === 'weekly_posts') {
        const posts = asset.posts || [];
        return `
          <div class="inline-asset-box">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 8px;">
              <span style="font-size: 13px; font-weight: 800; color: #c084fc;">📅 5-Day Post Series (Mon-Fri)</span>
              <button class="btn btn-xs btn-primary" onclick="copyAllPostsFromAsset(${msgIdx})">📋 Copy All 5 Days</button>
            </div>
            <div style="display: flex; flex-direction: column; gap: 10px; max-height: 320px; overflow-y: auto;">
              ${posts.map(p => `
                <div style="background: rgba(7, 11, 20, 0.6); border: 1px solid var(--border); border-radius: 8px; padding: 12px;">
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 11.5px; font-weight: 800; color: #38bdf8;">${escapeHtml(p.day)}: ${escapeHtml(p.theme || '')}</span>
                    <button class="btn btn-xs" onclick="copyTextDirect('${escapeHtml(p.body || p.headline || '')}')">📋 Copy Day</button>
                  </div>
                  <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.5; white-space: pre-wrap;">${escapeHtml(p.body || p.headline || '')}</div>
                </div>
              `).join('')}
            </div>
          </div>
        `;
      } else if (asset.type === 'campaign_pack') {
        return `
          <div class="inline-asset-box" style="border-color: #f43f5e;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(244, 63, 94, 0.4); padding-bottom: 8px;">
              <span style="font-size: 13.5px; font-weight: 800; color: #fb7185;">📦 Full Authority Campaign Pack (1 Article + 5 Posts + 2 Carousels)</span>
              <button class="btn btn-xs btn-primary" onclick="openCampaignPackModalFromAsset(${msgIdx})" style="background: linear-gradient(135deg, #f43f5e, #a855f7); border-color: #fb7185;">🔍 Open Full Pack Viewer</button>
            </div>
            <div style="font-size: 12.5px; color: var(--text-muted); line-height: 1.5;">
              Synthesized and saved the complete authority campaign bundle to your Library. Includes a 2,000+ word investigative article, Monday-Friday daily posts, Problem Deconstruction Deck, and Tactical Blueprint Deck.
            </div>
          </div>
        `;
      }
      return '';
    }

    let inlineCarouselIndices = {};
    function navigateInlineCarousel(msgIdx, delta) {
      const msg = notebookChatMessages[msgIdx];
      if (!msg || !msg.asset || !msg.asset.slides) return;
      const slides = msg.asset.slides;
      const cur = inlineCarouselIndices[msgIdx] || 0;
      let next = cur + delta;
      if (next < 0) next = slides.length - 1;
      if (next >= slides.length) next = 0;
      inlineCarouselIndices[msgIdx] = next;

      const slide = slides[next];
      const box = document.getElementById(`carousel-slide-box-${msgIdx}`);
      const counter = document.getElementById(`carousel-counter-${msgIdx}`);
      if (box) {
        box.innerHTML = renderSlideCardHtml(slide, next, slides.length);
      }
      if (counter) counter.innerText = `Slide ${next+1} of ${slides.length}`;
    }

    function copyAllPostsFromAsset(msgIdx) {
      const msg = notebookChatMessages[msgIdx];
      if (!msg || !msg.asset || !msg.asset.posts) return;
      const allText = msg.asset.posts.map(p => `=== ${p.day.toUpperCase()} (${p.theme || ''}) ===\n\n${p.body || p.headline}\n`).join('\\n---\\n\\n');
      copyTextDirect(allText);
    }

    function openCampaignPackModalFromAsset(msgIdx) {
      const msg = notebookChatMessages[msgIdx];
      if (!msg || !msg.asset) return;
      const fakeItem = {
        title: msg.asset.title || 'Campaign Pack',
        tier: 'Full Campaign Distribution Pack',
        article: msg.asset.article || '',
        weekly_posts: msg.asset.weekly_posts || [],
        carousel_1: msg.asset.carousel_1 || {},
        carousel_2: msg.asset.carousel_2 || {},
        research_dossier: msg.asset.research_dossier || {}
      };
      openContentViewModal(fakeItem);
    }

    function formatMarkdownText(text) {
      if (!text) return '';
      let html = escapeHtml(text);
      html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
      html = html.replace(/^#### (.*$)/gim, '<h4>$1</h4>');
      html = html.replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>');
      html = html.replace(/\*(.*?)\*/gim, '<em>$1</em>');
      html = html.replace(/^- (.*$)/gim, '<li>$1</li>');
      html = html.replace(/\\n\\n/g, '</p><p>');
      html = html.replace(/\\n/g, '<br>');
      return `<p>${html}</p>`;
    }

    // ==========================================================
    // Saved Library Functions
    // ==========================================================
    function setQuickTierFilter(tier) {
      tierFilter = tier;
      const pills = document.querySelectorAll('.quick-pill');
      pills.forEach(p => p.classList.remove('active'));
      const activePill = document.getElementById(`qp-${tier.toLowerCase()}`) || document.getElementById('qp-all');
      if (activePill) activePill.classList.add('active');
      const select = document.getElementById('tier-filter-select');
      if (select) select.value = tier;
      renderContentGrid();
    }

    function handleFilterChange() {
      tierFilter = document.getElementById('tier-filter-select').value;
      voiceFilter = document.getElementById('voice-filter-select').value;
      sortOrder = document.getElementById('sort-order-select').value;
      renderContentGrid();
    }

    function handleContentSearch() {
      searchQuery = document.getElementById('content-search-input').value.trim();
      renderContentGrid();
    }

    function renderContentGrid() {
      const container = document.getElementById('content-cards-container');
      if (!container) return;

      let filtered = contentItems.slice();

      if (tierFilter !== 'ALL') {
        filtered = filtered.filter(item => {
          const t = (item.tier || '').toLowerCase();
          if (tierFilter === 'Research') return t.includes('research') || t.includes('🔬');
          if (tierFilter === 'Campaign') return t.includes('campaign') || !!item.campaign_pack;
          return (item.tier || '').includes(tierFilter);
        });
      }

      if (voiceFilter !== 'ALL') {
        filtered = filtered.filter(item => item.voice_profile_id === voiceFilter);
      }

      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        filtered = filtered.filter(item =>
          (item.title || '').toLowerCase().includes(q) ||
          (item.topic || '').toLowerCase().includes(q) ||
          (item.content_markdown || '').toLowerCase().includes(q)
        );
      }

      if (sortOrder === 'newest') {
        filtered.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));
      } else if (sortOrder === 'oldest') {
        filtered.sort((a, b) => new Date(a.created_at || 0) - new Date(b.created_at || 0));
      } else if (sortOrder === 'alpha') {
        filtered.sort((a, b) => (a.title || '').localeCompare(b.title || ''));
      }

      if (filtered.length === 0) {
        container.innerHTML = `
          <div style="grid-column: 1 / -1; text-align: center; padding: 40px 20px; color: var(--text-muted);">
            <div style="font-size: 32px; margin-bottom: 8px;">📭</div>
            <div style="font-size: 15px; font-weight: 700; color: #fff;">No content pieces match your filter.</div>
            <div style="font-size: 13px; margin-top: 4px;">Use the NotebookLM Studio tab to synthesize a new piece!</div>
          </div>
        `;
        return;
      }

      container.innerHTML = filtered.map(item => {
        const isCamp = (item.tier || '').toLowerCase().includes('campaign') || !!item.campaign_pack;
        const isResearch = (item.tier || '').toLowerCase().includes('research') || (item.tier || '').includes('🔬');
        const badgeClass = isCamp ? 'campaign' : isResearch ? 'research' : item.tier && item.tier.includes('Tier 1') ? 't1' : item.tier && item.tier.includes('Tier 2') ? 't2' : 't3';

        return `
          <div class="content-card" onclick="openContentViewModalById('${item.id}')">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span class="tier-badge ${badgeClass}">${escapeHtml(item.tier || 'Content')}</span>
              <span style="font-size: 11px; color: var(--text-muted);">${strDate(item.created_at)}</span>
            </div>
            <div style="font-size: 14.5px; font-weight: 700; color: #ffffff; line-height: 1.4;">${escapeHtml(item.title || item.topic || 'Untitled Piece')}</div>
            <div style="font-size: 12px; color: var(--text-muted); line-height: 1.5; max-height: 54px; overflow: hidden;">${escapeHtml((item.content_markdown || item.article || '').substring(0, 140))}…</div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border); padding-top: 10px; margin-top: auto;">
              <span style="font-size: 11.5px; color: #38bdf8; font-weight: 600;">${escapeHtml((voiceProfiles.find(v => v.id === item.voice_profile_id)?.name) || (item.voice_profile_id === 'growth-dealmaker' ? 'Strategic Dealmaker' : 'Forensic Risk Operator'))}</span>
              <button class="btn btn-xs" onclick="event.stopPropagation(); deleteContentItem('${item.id}')" style="color: #f43f5e;" title="Delete">🗑️</button>
            </div>
          </div>
        `;
      }).join('');
    }

    function openContentViewModalById(id) {
      const item = contentItems.find(x => x.id === id);
      if (item) openContentViewModal(item);
    }

    function openContentViewModal(item) {
      currentModalContentItem = item;
      const modal = document.getElementById('content-view-modal');
      const titleEl = document.getElementById('view-content-title');
      const badgeEl = document.getElementById('view-content-tier-badge');
      const campTabs = document.getElementById('campaign-tabs-strip');
      const singlePanel = document.getElementById('single-asset-panel');

      titleEl.innerText = item.title || item.topic || 'Content Piece';
      const isCamp = (item.tier || '').toLowerCase().includes('campaign') || !!item.campaign_pack;
      badgeEl.innerText = item.tier || 'Content';
      badgeEl.className = `tier-badge ${isCamp ? 'campaign' : item.tier && item.tier.includes('Tier 1') ? 't1' : item.tier && item.tier.includes('Tier 2') ? 't2' : 't3'}`;

      if (isCamp) {
        if (campTabs) campTabs.style.display = 'flex';
        if (singlePanel) singlePanel.style.display = 'none';
        switchCampaignTab('article');
      } else {
        if (campTabs) campTabs.style.display = 'none';
        if (singlePanel) singlePanel.style.display = 'block';
        document.getElementById('view-content-markdown').value = item.content_markdown || item.article || '';

        const singleDeckContainer = document.getElementById('single-tier1-deck-container');
        const singleSlides = item.slides_outline || (item.carousel_1 && item.carousel_1.slides) || item.slides || [];
        if (singleDeckContainer && singleSlides.length > 0) {
          singleDeckContainer.style.display = 'block';
          currentSingleIndex = 0;
          updateSingleCarousel();
        } else if (singleDeckContainer) {
          singleDeckContainer.style.display = 'none';
        }
      }

      modal.style.display = 'flex';
    }

    function closeContentViewModal() {
      const modal = document.getElementById('content-view-modal');
      if (modal) modal.style.display = 'none';
    }

    function switchCampaignTab(tab) {
      currentCampaignTab = tab;
      const item = currentModalContentItem;
      if (!item) return;

      ['article', 'posts', 'c1', 'c2', 'dossier'].forEach(t => {
        const btn = document.getElementById(`camp-tab-btn-${t}`);
        const panel = document.getElementById(`campaign-${t}-panel`);
        if (btn) {
          if (t === tab) btn.classList.add('active');
          else btn.classList.remove('active');
        }
        if (panel) panel.style.display = t === tab ? 'block' : 'none';
      });

      if (tab === 'article') {
        const artText = item.article || item.content_markdown || '';
        document.getElementById('campaign-article-textarea').value = artText;
        document.getElementById('article-word-count-badge').innerText = `📖 ${artText.split(/\s+/).length} words`;
      } else if (tab === 'posts') {
        const postsList = document.getElementById('campaign-posts-list');
        const posts = item.weekly_posts || (item.campaign_pack && item.campaign_pack.weekly_posts) || [];
        postsList.innerHTML = posts.map(p => `
          <div style="background: rgba(7, 11, 20, 0.6); border: 1px solid var(--border); border-radius: 8px; padding: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 12px; font-weight: 800; color: #38bdf8;">${escapeHtml(p.day)}: ${escapeHtml(p.theme || '')}</span>
              <button class="btn btn-xs" onclick="copyTextDirect('${escapeHtml(p.body || p.headline || '')}')">📋 Copy Day Post</button>
            </div>
            <div style="font-size: 13px; color: #cbd5e1; line-height: 1.5; white-space: pre-wrap;">${escapeHtml(p.body || p.headline || '')}</div>
          </div>
        `).join('');
      } else if (tab === 'c1') {
        currentC1Index = 0;
        updateCampaignCarousel(1);
      } else if (tab === 'c2') {
        currentC2Index = 0;
        updateCampaignCarousel(2);
      } else if (tab === 'dossier') {
        const dossier = item.research_dossier || {};
        document.getElementById('campaign-dossier-thesis').innerText = dossier.thesis || 'N/A';
        document.getElementById('campaign-dossier-tension').innerText = dossier.unseen_tension || 'N/A';
      }
    }

    function updateCampaignCarousel(deckNum) {
      const item = currentModalContentItem;
      if (!item) return;
      const deckKey = deckNum === 1 ? 'carousel_1' : 'carousel_2';
      const deck = item[deckKey] || (item.campaign_pack && item.campaign_pack[deckKey]) || {};
      const slides = deck.slides || [];
      const curIdx = deckNum === 1 ? currentC1Index : currentC2Index;
      const slide = slides[curIdx] || {};

      const bannerEl = document.getElementById(`c${deckNum}-deck-style-guide`);
      if (bannerEl && deck.visual_style_guide) {
        bannerEl.innerHTML = renderDeckStyleGuideBannerHtml(deck.visual_style_guide);
        bannerEl.style.display = 'block';
      } else if (bannerEl) {
        bannerEl.style.display = 'none';
      }

      const cardEl = document.getElementById(`c${deckNum}-slide-card`);
      if (cardEl) {
        cardEl.innerHTML = renderSlideCardHtml(slide, curIdx, slides.length);
      } else {
        const numEl = document.getElementById(`c${deckNum}-slide-number`);
        if (numEl) numEl.innerText = slide.type || `#${curIdx+1}`;
        const headEl = document.getElementById(`c${deckNum}-slide-headline`);
        if (headEl) headEl.innerText = slide.headline || '';
        const bulEl = document.getElementById(`c${deckNum}-slide-bullet`);
        if (bulEl) bulEl.innerText = slide.bullet || '';
      }
      const countEl = document.getElementById(`c${deckNum}-slide-counter-text`);
      if (countEl) countEl.innerText = `Slide ${curIdx+1} of ${slides.length || 7}`;
    }

    function navigateCarousel(deckNum, delta) {
      const item = currentModalContentItem;
      if (!item) return;
      const deckKey = deckNum === 1 ? 'carousel_1' : 'carousel_2';
      const deck = item[deckKey] || (item.campaign_pack && item.campaign_pack[deckKey]) || {};
      const slides = deck.slides || [];
      if (deckNum === 1) {
        currentC1Index = Math.max(0, Math.min(slides.length - 1, currentC1Index + delta));
      } else {
        currentC2Index = Math.max(0, Math.min(slides.length - 1, currentC2Index + delta));
      }
      updateCampaignCarousel(deckNum);
    }

    let currentSingleIndex = 0;
    function updateSingleCarousel() {
      const item = currentModalContentItem;
      if (!item) return;
      const slides = item.slides_outline || (item.carousel_1 && item.carousel_1.slides) || item.slides || [];
      const deckGuide = item.visual_style_guide || (item.carousel_1 && item.carousel_1.visual_style_guide) || null;
      const curIdx = currentSingleIndex;
      const slide = slides[curIdx] || {};

      const bannerEl = document.getElementById('single-deck-style-guide');
      if (bannerEl && deckGuide) {
        bannerEl.innerHTML = renderDeckStyleGuideBannerHtml(deckGuide);
        bannerEl.style.display = 'block';
      } else if (bannerEl) {
        bannerEl.style.display = 'none';
      }

      const cardEl = document.getElementById('single-slide-card');
      if (cardEl) {
        cardEl.innerHTML = renderSlideCardHtml(slide, curIdx, slides.length);
      }
      const countEl = document.getElementById('single-slide-counter-text');
      if (countEl) countEl.innerText = `Slide ${curIdx+1} of ${slides.length}`;
    }

    function navigateSingleCarousel(delta) {
      const item = currentModalContentItem;
      if (!item) return;
      const slides = item.slides_outline || (item.carousel_1 && item.carousel_1.slides) || item.slides || [];
      if (!slides.length) return;
      currentSingleIndex = Math.max(0, Math.min(slides.length - 1, currentSingleIndex + delta));
      updateSingleCarousel();
    }

    function copySingleCarouselScript() {
      const item = currentModalContentItem;
      if (!item) return;
      const slides = item.slides_outline || (item.carousel_1 && item.carousel_1.slides) || item.slides || [];
      const text = slides.map(s => {
        let block = `[SLIDE ${s.slide || ''} - ${s.type || ''}]\nHEADLINE: ${s.headline || ''}\nBULLET: ${s.bullet || ''}\n`;
        if (s.visual_concept) block += `VISUAL CONCEPT: ${s.visual_concept}\n`;
        if (s.image_prompt) block += `IMAGE PROMPT: ${s.image_prompt}\n`;
        return block;
      }).join(String.fromCharCode(10));
      copyTextDirect(text);
    }

    function copyCarouselScript(deckNum) {
      const item = currentModalContentItem;
      if (!item) return;
      const deckKey = deckNum === 1 ? 'carousel_1' : 'carousel_2';
      const deck = item[deckKey] || (item.campaign_pack && item.campaign_pack[deckKey]) || {};
      const slides = deck.slides || [];
      const text = slides.map(s => {
        let block = `[SLIDE ${s.slide || ''} - ${s.type || ''}]\nHEADLINE: ${s.headline || ''}\nBULLET: ${s.bullet || ''}\n`;
        if (s.visual_concept) block += `VISUAL CONCEPT: ${s.visual_concept}\n`;
        if (s.image_prompt) block += `IMAGE PROMPT: ${s.image_prompt}\n`;
        return block;
      }).join(String.fromCharCode(10));
      copyTextDirect(text);
    }

    function copyCampaignArticle() {
      const text = document.getElementById('campaign-article-textarea').value;
      copyTextDirect(text);
    }

    function copyAllPostsText() {
      const item = currentModalContentItem;
      if (!item) return;
      const posts = item.weekly_posts || (item.campaign_pack && item.campaign_pack.weekly_posts) || [];
      const text = posts.map(p => `=== ${p.day.toUpperCase()} (${p.theme || ''}) ===\n\n${p.body || p.headline}\n`).join('\\n---\\n\\n');
      copyTextDirect(text);
    }

    function copyFullCampaignBundle() {
      const item = currentModalContentItem;
      if (!item) return;
      let bundle = `# CAMPAIGN BUNDLE: ${item.title || item.topic}\n\n`;
      bundle += `## 1. LONG INVESTIGATIVE ARTICLE\n\n${item.article || item.content_markdown || ''}\n\n`;
      bundle += `## 2. 5-DAY POST SERIES\n\n`;
      const posts = item.weekly_posts || (item.campaign_pack && item.campaign_pack.weekly_posts) || [];
      bundle += posts.map(p => `[${p.day}]: ${p.body || p.headline}`).join('\\n\\n') + '\\n\\n';
      copyTextDirect(bundle);
    }

    function copyMarkdown() {
      const text = document.getElementById('view-content-markdown').value;
      copyTextDirect(text);
    }

    async function deleteContentItem(id) {
      if (!confirm('Are you sure you want to delete this piece?')) return;
      try {
        await fetch('/api/content/delete', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id: id })
        });
        contentItems = contentItems.filter(x => x.id !== id);
        updateCountersAndPills();
        renderContentGrid();
        showToast('Piece deleted successfully');
      } catch (err) {
        showToast('Error deleting item');
      }
    }

    // Utility Helpers
    function copyTextDirect(text) {
      if (!text) return;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
          showToast('Copied to clipboard!');
        }).catch(() => {
          fallbackCopyText(text);
        });
      } else {
        fallbackCopyText(text);
      }
    }

    function fallbackCopyText(text) {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand('copy');
        showToast('Copied to clipboard!');
      } catch (err) {
        showToast('Failed to copy');
      }
      document.body.removeChild(ta);
    }

    function showToast(msg) {
      const t = document.getElementById('toast');
      if (!t) return;
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2600);
    }

    function escapeHtml(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    function strDate(iso) {
      if (!iso) return '';
      try { return new Date(iso).toLocaleDateString(); } catch (e) { return iso.substring(0, 10); }
    }

    // Initial Load: Execute immediately AND on DOMContentLoaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', loadContentPageData);
    } else {
      loadContentPageData();
    }
  </script>
</body>
</html>
"""

#!/usr/bin/env python3
"""
Executive Outreach, Media CRM & Content Studio
Dual-Pipeline CRM:
1. Podcast & Media Pipeline (P4 - Target Shows & Enriched Media)
2. Executive & Dealmaker Pipeline (Master Leads & Outreach - PE/VC/DFI Partners)
Dedicated Content Engine (/content):
3. Research Dossiers & Author Voice Cloning (Carousels, Essays, Briefings)
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

try:
    from dotenv import load_dotenv
    env_file = os.path.join(BASE_DIR, ".env")
    load_dotenv(env_file)
except Exception:
    pass

if not os.environ.get("GEMINI_API_KEY"):
    for ep in [
        os.path.join(BASE_DIR, ".env"),
        os.path.join(BASE_DIR, "..", ".env"),
        os.path.join(os.getcwd(), ".env"),
        os.path.join(os.getcwd(), "media_prospecting", ".env")
    ]:
        if os.path.exists(ep):
            try:
                with open(ep, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("GEMINI_API_KEY=") and not line.startswith("#"):
                            os.environ["GEMINI_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
                            break
            except Exception:
                pass
        if os.environ.get("GEMINI_API_KEY"):
            break

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
from src.crm.db import DatabaseManager
from src.content.engine import ResearchSynthesizer, extract_text_from_pdf, extract_text_from_docx, extract_text_from_url

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
db = DatabaseManager()
synthesizer = ResearchSynthesizer()

CONTENT_JSON_PATH = os.path.join(BASE_DIR, "data", "content_items.json")
VOICES_JSON_PATH = os.path.join(BASE_DIR, "data", "voice_profiles.json")


def load_local_content():
    if os.path.exists(CONTENT_JSON_PATH):
        try:
            with open(CONTENT_JSON_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_local_content(items):
    try:
        os.makedirs(os.path.dirname(CONTENT_JSON_PATH), exist_ok=True)
        with open(CONTENT_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, default=str)
    except Exception as e:
        print(f"[!] Error saving local content: {e}")


def save_local_content_item(item):
    items = load_local_content()
    idx = next((i for i, x in enumerate(items) if x.get("id") == item["id"]), None)
    if idx is not None:
        items[idx] = item
    else:
        items.insert(0, item)
    save_local_content(items)


def delete_local_content_item(item_id):
    items = load_local_content()
    items = [x for x in items if x.get("id") != item_id]
    save_local_content(items)


def get_default_voice_profiles():
    if os.path.exists(VOICES_JSON_PATH):
        try:
            with open(VOICES_JSON_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data:
                    return data
        except Exception:
            pass
    return [
        {
            "id": "forensic-operator",
            "name": "Rupert Evill / Forensic Risk & Governance Operator",
            "role": "Crisis Investigator & Board Risk Advisor",
            "philosophy": "Corporate failures, corruption, and operational breakdowns are driven by human behaviour under pressure, never a lack of paperwork. Traditional compliance creates an illusion of security through 300-page codes and annual check-the-box training. Real ethics is enlightened self-interest and capital protection.",
            "tone": "Authoritative, analytical, contrarian yet constructive, grounded, zero corporate fluff, forensic insider.",
            "cadence": "Short 1-2 sentence lines with double spacing. Punchy, memorable mental models. Clear intention vs reality contrasts.",
            "banned_words": "delve, game-changer, holistic journey, agree?, synergy, paradigm shift, thought leadership, exciting times",
            "sample_texts": [
                "The most dangerous thing a founder-led business can have isn't a scandal. It's a story that's too smooth.",
                "Fast decisions and a founder who 'reviews everything' can look like strength. Sometimes it is. Sometimes it's concentration risk wearing a good suit."
            ]
        },
        {
            "id": "christian-hunt",
            "name": "Christian Hunt / Human Risk & Behavioral Science",
            "role": "Author of Humanize Rules & Host of The Human Risk Podcast",
            "philosophy": "Human beings do not make decisions in sterile vacuums. Distance, digital screens, and cognitive friction change how people act. Compliance must be designed with human psychology in mind, not legal idealism.",
            "tone": "Witty, thoughtful, conversational, deeply psychological, behavioral-first.",
            "cadence": "Conversational storytelling, relatable analogies, sharp behavioral observations.",
            "banned_words": "delve, synergy, game-changer, seamless, exciting journey",
            "sample_texts": [
                "If you design a process that requires saints to succeed under stress, your process is already broken.",
                "Distance turns theft into a one-click admin task."
            ]
        },
        {
            "id": "jordan-sabalo",
            "name": "Jordan Sabalo / Contrarian Tech & Growth Investigator",
            "role": "Tech Due Diligence & Economic Investigative Writer",
            "philosophy": "Corporate narratives in tech and remote work look pristine on LinkedIn while frontline reality is filled with unmeasured friction, wage arbitrage, and informal workarounds.",
            "tone": "Gritty, investigative, contrarian, empirical, narrative-driven.",
            "cadence": "Visceral micro-narratives (what happens at 2:15 AM), stark before-and-after contrasts, hard data.",
            "banned_words": "delve, tapestry, beacon, testament, holistic, revolutionize",
            "sample_texts": [
                "'We're not just a company, we're a family' is the #1 warning sign that your invoice isn't getting paid.",
                "When an offshore worker is just a tiny Slack circle, the brain stops seeing a real person."
            ]
        },
        {
            "id": "growth-dealmaker",
            "name": "Strategic Dealmaker & M&A Operator",
            "role": "Private Equity Partner & Strategic Acquirer",
            "philosophy": "Value creation in M&A happens through operational discipline and cultural integration, not financial engineering. Pre-deal due diligence must price human risk and key-person dependencies before signing.",
            "tone": "Pragmatic, commercially sharp, direct, experienced, metric-informed.",
            "cadence": "Concise bullets, clear investment theses, stark risk-reward comparisons.",
            "banned_words": "revolutionary, disruptive, silver bullet, no-brainer, unicorn vibes",
            "sample_texts": [
                "EBITDA multiples don't protect you when the head of supply chain walks out 30 days post-close.",
                "If your diligence team spent 40 hours auditing leases and 2 hours auditing management integrity, you didn't do diligence—you did paperwork."
            ]
        }
    ]


DEFAULT_VOICES = get_default_voice_profiles()


def get_voice_profile_by_id(voice_id):
    profiles = (db.get_voice_profiles() if db.is_connected else None) or get_default_voice_profiles()
    for p in profiles:
        if p.get("id") == voice_id:
            return p
    return profiles[0] if profiles else get_default_voice_profiles()[0]


# ------------------ Routes ------------------

@app.route("/")
def index():
    return render_template_string(CRM_TEMPLATE)


@app.route("/content")
def content_page():
    return render_template_string(CONTENT_TEMPLATE)


@app.route("/api/status")
def api_status():
    media_leads = (db.get_all_media_leads() if db.is_connected else None) or tracker.get_leads()
    exec_leads = (db.get_all_executive_leads() if db.is_connected else None) or exec_tracker.get_leads()
    content_items = (db.get_content_items() if db.is_connected else None) or load_local_content()
    return jsonify({
        "neon_connected": bool(db.is_connected),
        "media_count": len(media_leads),
        "exec_count": len(exec_leads),
        "content_count": len(content_items)
    })


@app.route("/api/leads")
def get_leads():
    if db.is_connected:
        leads = db.get_all_media_leads()
        if leads is not None:
            return jsonify(leads)
    return jsonify(tracker.get_leads())


@app.route("/api/leads/update", methods=["POST"])
def update_lead():
    data = request.get_json() or {}
    lead_id = data.get("id")
    updates = data.get("updates")
    if updates and isinstance(updates, dict):
        tracker.update_lead(lead_id, updates)
        updated_lead = tracker.leads.get(lead_id)
        if db.is_connected and updated_lead:
            db.upsert_media_lead(updated_lead)
        return jsonify({"success": True})
    
    status = data.get("status")
    notes = data.get("notes", "")
    angle = data.get("pitch_angle", "")
    current_activity = data.get("current_activity", "")

    up = {}
    if status is not None: up["status"] = status
    if notes: up["notes"] = notes
    if angle: up["rupert_angle"] = angle
    if current_activity: up["current_activity"] = current_activity
    tracker.update_lead(lead_id, up)
    updated_lead = tracker.leads.get(lead_id)
    if db.is_connected and updated_lead:
        db.upsert_media_lead(updated_lead)
    return jsonify({"success": True})


@app.route("/api/leads/delete", methods=["POST"])
def delete_lead():
    data = request.get_json() or {}
    lead_id = data.get("id")
    success = tracker.delete_lead(lead_id)
    if db.is_connected and lead_id:
        db.delete_media_lead(lead_id)
    return jsonify({"success": success})


@app.route("/api/leads/add", methods=["POST"])
def add_lead():
    data = request.get_json() or {}
    lead_id = re.sub(r'[\W_]+', '_', data.get("name", "show").lower()).strip('_')
    if not lead_id:
        lead_id = f"lead_{int(datetime.now().timestamp())}"
    data["id"] = lead_id
    tracker.add_or_update_lead(data)
    tracker.save()
    if db.is_connected:
        db.upsert_media_lead(tracker.leads[lead_id])
    return jsonify(tracker.leads[lead_id])


@app.route("/api/executives")
def get_executives():
    if db.is_connected:
        leads = db.get_all_executive_leads()
        if leads is not None:
            return jsonify(leads)
    return jsonify(exec_tracker.get_leads())


@app.route("/api/executives/update", methods=["POST"])
def update_executive():
    data = request.get_json() or {}
    lead_id = data.get("id")
    updates = data.get("updates", {})
    success = exec_tracker.update_lead(lead_id, updates)
    updated_lead = exec_tracker.leads.get(lead_id)
    if db.is_connected and updated_lead:
        db.upsert_executive_lead(updated_lead)
    return jsonify({"success": success})


@app.route("/api/executives/delete", methods=["POST"])
def delete_executive():
    data = request.get_json() or {}
    lead_id = data.get("id")
    success = exec_tracker.delete_lead(lead_id)
    if db.is_connected and lead_id:
        db.delete_executive_lead(lead_id)
    return jsonify({"success": success})


@app.route("/api/executives/add", methods=["POST"])
def add_executive():
    data = request.get_json() or {}
    lead_id = exec_tracker.add_lead(data)
    if db.is_connected:
        db.upsert_executive_lead(exec_tracker.leads[lead_id])
    return jsonify(exec_tracker.leads[lead_id])


@app.route("/api/export/excel")
def export_excel():
    """Generates a dynamic multi-tab Excel workbook: P4 Podcasts, Master Leads & Outreach, Content Calendar."""
    podcasts = (db.get_all_media_leads() if db.is_connected else None) or tracker.get_leads()
    execs = (db.get_all_executive_leads() if db.is_connected else None) or exec_tracker.get_leads()
    content_items = (db.get_content_items() if db.is_connected else None) or load_local_content()

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

    # Tab 3: Content Calendar & Dossiers
    ws_content = wb.create_sheet("Content Calendar & Dossiers")
    ws_content.append([
        "Title",
        "Tier Format",
        "Topic",
        "Status",
        "Source Type",
        "Source Reference",
        "Core Thesis",
        "Verified Facts Sample",
        "Slides Count",
        "Created At"
    ])

    for item in content_items:
        dossier = item.get("research_dossier") or {}
        thesis = dossier.get("thesis", "")
        data_points = dossier.get("data_points") or []
        dp_str = " | ".join([dp.get("fact", "") for dp in data_points[:3]]) if isinstance(data_points, list) else ""
        slides = item.get("slides_outline") or []
        slide_count = len(slides) if isinstance(slides, list) else 0

        ws_content.append([
            item.get("title", ""),
            item.get("tier", ""),
            item.get("topic", ""),
            item.get("status", "Draft"),
            item.get("source_type", ""),
            item.get("source_reference", ""),
            thesis,
            dp_str,
            slide_count,
            str(item.get("created_at", ""))[:19]
        ])

    buf = io.BytesIO()
    wb.save(buf)
    buf.seek(0)

    filename = f"Media_Executive_Content_Studio_{datetime.now().strftime('%Y%m%d')}.xlsx"
    return send_file(
        buf,
        as_attachment=True,
        download_name=filename,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


@app.route("/api/export/tsv")
def export_tsv():
    """Returns tab-separated values ready for instant pasting into Google Sheets (12 columns)."""
    leads = (db.get_all_media_leads() if db.is_connected else None) or tracker.get_leads()
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
    if name: query_parts.append(name)
    if host: query_parts.append(host)
    if role: query_parts.append(role)
    if topic: query_parts.append(topic)

    query = " ".join(query_parts) if query_parts else data.get("query", "compliance risk")
    discovered = []

    if engine in ["podcast", "all"]:
        podcast_results = search_podcasts(query=query, limit=limit)
        for show in podcast_results:
            show["media_type"] = "Audio Podcast"
            if enrich and show.get("feed_url"):
                try:
                    rss_info = enrich_from_rss(show["feed_url"])
                    show.update(rss_info)
                except Exception:
                    pass
            discovered.append(show)

    if engine in ["youtube", "all"] and search_youtube:
        yt_results = search_youtube(query=query, limit=limit)
        discovered.extend(yt_results)

    for show in discovered:
        tracker.add_or_update_lead(show)
        if db.is_connected:
            db.upsert_media_lead(show)

    tracker.save()
    if db.is_connected:
        leads = db.get_all_media_leads()
        if leads:
            return jsonify(leads)
    return jsonify(tracker.get_leads())


@app.route("/api/search/presets", methods=["POST"])
def search_presets():
    results = search_preset_categories(limit_per_query=6)
    for show in results:
        show["media_type"] = "Audio Podcast"
        if show.get("feed_url"):
            try:
                rss_info = enrich_from_rss(show["feed_url"])
                show.update(rss_info)
            except Exception:
                pass
        tracker.add_or_update_lead(show)
        if db.is_connected:
            db.upsert_media_lead(show)

    tracker.save()
    if db.is_connected:
        leads = db.get_all_media_leads()
        if leads:
            return jsonify(leads)
    return jsonify(tracker.get_leads())


@app.route("/api/content")
def get_content():
    items = None
    if db.is_connected:
        items = db.get_content_items()
    if not items:
        items = load_local_content()
    
    # Restore campaign fields if packed inside research_dossier
    for item in (items or []):
        rd = item.get("research_dossier")
        if isinstance(rd, dict) and "campaign_pack" in rd:
            cp = rd["campaign_pack"]
            item["campaign_pack"] = cp
            if "weekly_posts" in cp and not item.get("weekly_posts"):
                item["weekly_posts"] = cp["weekly_posts"]
            if "carousel_1" in cp and not item.get("carousel_1"):
                item["carousel_1"] = cp["carousel_1"]
            if "carousel_2" in cp and not item.get("carousel_2"):
                item["carousel_2"] = cp["carousel_2"]
            if "article" in cp and not item.get("article"):
                item["article"] = cp["article"]
    return jsonify(items)


@app.route("/api/content/researched-links")
def get_researched_links():
    """Returns distinct citation URLs and titles from existing dossiers across all content."""
    items = (db.get_content_items() if db.is_connected else None) or load_local_content()
    seen_urls = set()
    links = []
    for item in items:
        dossier = item.get("research_dossier") or {}
        # 1. Citations
        citations = dossier.get("citations") or []
        for c in citations:
            if isinstance(c, dict):
                url = (c.get("url") or "").strip()
                title = (c.get("title") or "").strip() or url
            elif isinstance(c, str):
                url = c.strip()
                title = c.strip()
            else:
                continue
            if url and url.startswith("http") and url not in seen_urls:
                seen_urls.add(url)
                links.append({"url": url, "title": title, "topic": item.get("topic", "")})

        # 2. Source reference if URL
        src_ref = (item.get("source_reference") or "").strip()
        if src_ref and src_ref.startswith("http"):
            for u in re.findall(r'https?://[^\s,]+', src_ref):
                if u not in seen_urls:
                    seen_urls.add(u)
                    links.append({"url": u, "title": item.get("topic") or u, "topic": item.get("topic", "")})

        # 3. Data points URLs
        data_points = dossier.get("data_points") or []
        for dp in data_points:
            if isinstance(dp, dict):
                u = (dp.get("url") or "").strip()
                if u and u.startswith("http") and u not in seen_urls:
                    seen_urls.add(u)
                    links.append({"url": u, "title": dp.get("source") or item.get("topic") or u, "topic": item.get("topic", "")})

    return jsonify(links)


@app.route("/api/content/generate", methods=["POST"])
def generate_content_item():
    is_form = request.content_type and "multipart/form-data" in request.content_type
    source_urls = None
    
    if is_form:
        source_type = request.form.get("source_type", "text")
        tier = request.form.get("tier", "Full Campaign Distribution Pack")
        topic = request.form.get("topic", "").strip()
        voice_id = request.form.get("voice_id", "forensic-operator")
        raw_text = ""
        source_ref = ""
        
        if "file" in request.files and request.files["file"].filename:
            f = request.files["file"]
            source_type = "pdf"
            source_ref = f.filename
            raw_text = extract_text_from_pdf(f.stream)
            if not topic:
                topic = os.path.splitext(f.filename)[0].replace("_", " ").title()
        elif source_type == "url":
            url = request.form.get("url", "").strip()
            source_ref = url
            if url:
                scraped = extract_text_from_url(url)
                raw_text = scraped.get("text", "")
                source_urls = scraped.get("urls", [])
                if not topic and scraped.get("title") and scraped.get("title") != url:
                    topic = scraped["title"]
        elif source_type == "lead":
            lead_id = request.form.get("lead_id", "")
            lead_pipe = request.form.get("lead_type", "media")
            lead = None
            if lead_pipe == "media":
                lead = (db.is_connected and next((x for x in (db.get_all_media_leads() or []) if x.get("id") == lead_id), None)) or tracker.leads.get(lead_id)
            else:
                lead = (db.is_connected and next((x for x in (db.get_all_executive_leads() or []) if x.get("id") == lead_id), None)) or exec_tracker.leads.get(lead_id)
            if lead:
                lead_name = lead.get("name") or lead.get("company") or "Target Lead"
                source_ref = f"{lead_name} ({lead_pipe.capitalize()} Lead)"
                hook = lead.get("rupert_angle") or lead.get("pitch_angle") or lead.get("hook") or ""
                notes = lead.get("current_activity") or lead.get("notes") or ""
                raw_text = f"Subject: {lead_name}\nStrategic Hook: {hook}\nInteraction Context: {notes}\nCategory: {lead.get('genre') or lead.get('topic') or lead.get('company') or 'Leadership'}"
                if not topic:
                    topic = f"Executive Angle: {lead_name}"
        else:
            raw_text = request.form.get("text", "").strip()
            source_ref = request.form.get("source_reference", "Executive Briefing")
    else:
        data = request.get_json() or {}
        source_type = data.get("source_type", "text")
        tier = data.get("tier", "Full Campaign Distribution Pack")
        topic = data.get("topic", "").strip()
        voice_id = data.get("voice_id", "forensic-operator")
        raw_text = data.get("text", "").strip()
        source_ref = data.get("source_reference", "Executive Briefing")
        
        if source_type == "url":
            url = data.get("url", "").strip()
            source_ref = url
            if url:
                scraped = extract_text_from_url(url)
                raw_text = scraped.get("text", "")
                source_urls = scraped.get("urls", [])
                if not topic and scraped.get("title") and scraped.get("title") != url:
                    topic = scraped["title"]
        elif source_type == "lead":
            lead_id = data.get("lead_id", "")
            lead_pipe = data.get("lead_type", "media")
            lead = None
            if lead_pipe == "media":
                lead = (db.is_connected and next((x for x in (db.get_all_media_leads() or []) if x.get("id") == lead_id), None)) or tracker.leads.get(lead_id)
            else:
                lead = (db.is_connected and next((x for x in (db.get_all_executive_leads() or []) if x.get("id") == lead_id), None)) or exec_tracker.leads.get(lead_id)
            if lead:
                lead_name = lead.get("name") or lead.get("company") or "Target Lead"
                source_ref = f"{lead_name} ({lead_pipe.capitalize()} Lead)"
                hook = lead.get("rupert_angle") or lead.get("pitch_angle") or lead.get("hook") or ""
                notes = lead.get("current_activity") or lead.get("notes") or ""
                raw_text = f"Subject: {lead_name}\nStrategic Hook: {hook}\nInteraction Context: {notes}\nCategory: {lead.get('genre') or lead.get('topic') or lead.get('company') or 'Leadership'}"
                if not topic:
                    topic = f"Executive Angle: {lead_name}"

    if not topic:
        topic = "Corporate Governance & Integrity"

    if not raw_text.strip():
        return jsonify({"error": "No content could be extracted or provided."}), 400

    if not source_urls and raw_text:
        urls_found = re.findall(r'https?://[^\s,]+', raw_text)
        if urls_found:
            source_urls = urls_found

    voice_profile = get_voice_profile_by_id(voice_id)
    generated = synthesizer.generate_content(raw_text, voice_profile, source_title=topic, tier=tier, source_urls=source_urls)

    item_id = f"item_{int(datetime.now().timestamp())}_{os.urandom(2).hex()}"
    new_item = {
        "id": item_id,
        "title": generated.get("title", f"{tier}: {topic}"),
        "tier": tier,
        "topic": topic,
        "voice_profile_id": voice_id,
        "source_type": source_type,
        "source_reference": source_ref,
        "content_markdown": generated.get("content_markdown", ""),
        "slides_outline": generated.get("slides_outline", []),
        "research_dossier": generated.get("research_dossier", {}),
        "status": "Ready to Publish",
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }

    # Attach campaign pack properties if present
    if generated.get("campaign_pack") or "weekly_posts" in generated:
        new_item["campaign_pack"] = generated.get("campaign_pack", {})
        new_item["weekly_posts"] = generated.get("weekly_posts", [])
        new_item["carousel_1"] = generated.get("carousel_1", {})
        new_item["carousel_2"] = generated.get("carousel_2", {})
        new_item["article"] = generated.get("article", generated.get("content_markdown", ""))

        # Mirror inside research_dossier for Neon Postgres JSONB persistence
        if not isinstance(new_item["research_dossier"], dict):
            new_item["research_dossier"] = {}
        new_item["research_dossier"]["campaign_pack"] = {
            "weekly_posts": new_item["weekly_posts"],
            "carousel_1": new_item["carousel_1"],
            "carousel_2": new_item["carousel_2"],
            "article": new_item["article"]
        }

    if db.is_connected:
        db.save_content_item(new_item)
    save_local_content_item(new_item)

    return jsonify(new_item)


@app.route("/api/content/delete", methods=["POST"])
def delete_content_item():
    data = request.get_json() or {}
    item_id = data.get("id")
    if not item_id:
        return jsonify({"error": "Missing item id"}), 400
    if db.is_connected:
        db.delete_content_item(item_id)
    delete_local_content_item(item_id)
    return jsonify({"success": True})


@app.route("/api/content/research", methods=["POST"])
def conduct_research():
    """
    NotebookLM-style Deep Research Studio Endpoint.
    Accepts: { prompt, focus_angles, optional_urls, voice_id, auto_generate_campaign, notebook_id }
    Conducts deep empirical fact-mining, produces a dedicated Research Notebook Dossier,
    and optionally synthesizes an immediate Full Authority Campaign Pack (1 Article + 5 Posts + 2 Decks).
    """
    data = request.get_json() or {}
    prompt = (data.get("prompt") or "").strip()
    notebook_id = data.get("notebook_id") or data.get("id")

    existing_notebook = None
    if notebook_id:
        items = (db.get_content_items() if db.is_connected else None) or load_local_content()
        existing_notebook = next((x for x in items if x.get("id") == notebook_id), None)
        if existing_notebook and not prompt:
            prompt = existing_notebook.get("title") or existing_notebook.get("topic") or "Investigative Research"

    if not prompt:
        return jsonify({"error": "A research prompt, sentence, or question is required."}), 400

    focus_angles = data.get("focus_angles") or []
    if isinstance(focus_angles, str):
        focus_angles = [a.strip() for a in focus_angles.split(",") if a.strip()]

    optional_urls = (data.get("optional_urls") or "").strip()
    voice_id = data.get("voice_id", "forensic-operator")
    auto_generate_campaign = bool(data.get("auto_generate_campaign", False))
    voice_profile = get_voice_profile_by_id(voice_id)

    # 1. If transforming an existing saved notebook
    if existing_notebook and existing_notebook.get("research_dossier"):
        researched = {
            "tier": "🔬 Research Notebook",
            "title": existing_notebook.get("title") or prompt,
            "topic": existing_notebook.get("topic") or prompt,
            "executive_summary": existing_notebook.get("content_markdown") or existing_notebook.get("article") or "",
            "research_dossier": existing_notebook.get("research_dossier"),
            "status": "Researched",
            "source_type": "deep_research",
            "source_reference": existing_notebook.get("source_reference") or "🔬 Deep Research Studio (NotebookLM Mode)"
        }
    else:
        researched = synthesizer.conduct_deep_research(
            research_prompt=prompt,
            focus_angles=focus_angles,
            optional_urls=optional_urls,
            voice_profile=voice_profile
        )

    # 2. If auto_generate_campaign is true, synthesize full campaign pack immediately!
    if auto_generate_campaign:
        research_dossier = researched.get("research_dossier", {})
        data_points_text = "\n".join([f"- {dp.get('fact')} ({dp.get('source')})" for dp in research_dossier.get("data_points", []) if isinstance(dp, dict)])
        quotes_text = "\n".join([f'- "{q}"' for q in research_dossier.get("quotes", [])])

        raw_material = f"""RESEARCH INQUIRY / TITLE: {researched.get('title')}
THESIS: {research_dossier.get('thesis', '')}
UNSEEN TENSION: {research_dossier.get('unseen_tension', '')}

EXECUTIVE RESEARCH BRIEF:
{researched.get('executive_summary', '')}

EMPIRICAL DATA POINTS:
{data_points_text}

OPERATOR QUOTES & MENTAL MODELS:
{quotes_text}
"""
        citations_urls = [c.get("url") for c in research_dossier.get("citations", []) if isinstance(c, dict) and c.get("url")]
        if optional_urls:
            found_u = re.findall(r'https?://[^\s,]+', optional_urls)
            for u in found_u:
                if u not in citations_urls:
                    citations_urls.append(u)

        campaign = synthesizer.generate_full_campaign_pack(
            raw_text=raw_material,
            voice_profile=voice_profile,
            source_title=researched.get("title", prompt),
            source_urls=citations_urls,
            existing_dossier=research_dossier
        )

        item_id = f"item_{int(datetime.now().timestamp())}_{os.urandom(2).hex()}"
        new_item = {
            "id": item_id,
            "title": campaign.get("title", f"Campaign Pack: {researched.get('title')}"),
            "tier": "Full Campaign Distribution Pack",
            "topic": researched.get("title", prompt),
            "voice_profile_id": voice_id,
            "source_type": "deep_research",
            "source_reference": "🔬 Deep Research Studio (NotebookLM Mode)",
            "content_markdown": campaign.get("content_markdown") or campaign.get("article", ""),
            "slides_outline": campaign.get("slides_outline", []),
            "research_dossier": campaign.get("research_dossier") or research_dossier,
            "campaign_pack": campaign.get("campaign_pack", {}),
            "weekly_posts": campaign.get("weekly_posts", []),
            "carousel_1": campaign.get("carousel_1", {}),
            "carousel_2": campaign.get("carousel_2", {}),
            "article": campaign.get("article", ""),
            "status": "Ready to Publish",
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        if not isinstance(new_item["research_dossier"], dict):
            new_item["research_dossier"] = {}
        new_item["research_dossier"]["campaign_pack"] = {
            "weekly_posts": new_item["weekly_posts"],
            "carousel_1": new_item["carousel_1"],
            "carousel_2": new_item["carousel_2"],
            "article": new_item["article"]
        }
    else:
        # Save as dedicated Research Notebook item
        item_id = f"item_{int(datetime.now().timestamp())}_{os.urandom(2).hex()}"
        new_item = {
            "id": item_id,
            "title": researched.get("title", f"Research: {prompt}"),
            "tier": "🔬 Research Notebook",
            "topic": prompt,
            "voice_profile_id": voice_id,
            "source_type": "deep_research",
            "source_reference": "🔬 Deep Research Studio (NotebookLM Mode)",
            "content_markdown": researched.get("executive_summary") or researched.get("content_markdown", ""),
            "slides_outline": [],
            "research_dossier": researched.get("research_dossier", {}),
            "status": "Researched",
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }

    if db.is_connected:
        db.save_content_item(new_item)
    save_local_content_item(new_item)

    return jsonify(new_item)



@app.route("/api/content/notebook/upload", methods=["POST"])
def notebook_upload():
    """
    Accepts file upload (.pdf via pypdf, .docx via docx.Document, .txt, .md),
    extracts text, and returns { id, name, type, text, size_label }.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded."}), 400
    f = request.files["file"]
    if not f.filename:
        return jsonify({"error": "Empty filename."}), 400

    filename = f.filename
    ext = os.path.splitext(filename)[1].lower()
    raw_text = ""
    try:
        if ext == ".pdf":
            raw_text = extract_text_from_pdf(f.stream)
        elif ext in [".docx", ".doc"]:
            raw_text = extract_text_from_docx(f.stream)
        elif ext in [".txt", ".md", ".json", ".csv"]:
            raw_text = f.read().decode("utf-8", errors="ignore")
        else:
            raw_text = f.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return jsonify({"error": f"Failed to extract text from file: {e}"}), 500

    char_count = len((raw_text or "").strip())
    size_label = f"{char_count:,} chars" if char_count < 100000 else f"{char_count // 1000}k chars"
    source_id = f"src_{int(datetime.now().timestamp())}_{os.urandom(2).hex()}"

    return jsonify({
        "id": source_id,
        "name": filename,
        "type": ext.lstrip(".") or "file",
        "text": raw_text,
        "size_label": size_label,
        "char_count": char_count
    })


@app.route("/api/content/notebook/scrape", methods=["POST"])
def notebook_scrape():
    """
    Accepts { url }, scrapes clean article text via extract_text_from_url,
    and returns { id, name, type: 'url', text, url, size_label }.
    """
    data = request.get_json() or {}
    url = (data.get("url") or "").strip()
    if not url:
        return jsonify({"error": "No URL provided."}), 400

    scraped = extract_text_from_url(url)
    clean_text = scraped.get("text", "")
    title = scraped.get("title") or url
    char_count = len(clean_text.strip())
    size_label = f"{char_count:,} chars"
    source_id = f"src_{int(datetime.now().timestamp())}_{os.urandom(2).hex()}"

    return jsonify({
        "id": source_id,
        "name": title,
        "type": "url",
        "text": clean_text,
        "url": url,
        "size_label": size_label,
        "char_count": char_count
    })


@app.route("/api/content/notebook/chat", methods=["POST"])
def notebook_chat():
    """
    Interactive NotebookLM Studio Chat Endpoint.
    Accepts { messages, sources, voice_id, requested_format },
    calls engine.chat_notebook, saves generated assets to DB,
    and returns { reply_text, research_dossier, suggested_angles, generated_asset }.
    """
    data = request.get_json() or {}
    messages = data.get("messages") or []
    sources = data.get("sources") or []
    voice_id = data.get("voice_id", "forensic-operator")
    requested_format = data.get("requested_format")
    voice_profile = get_voice_profile_by_id(voice_id)

    result = synthesizer.chat_notebook(
        messages=messages,
        sources=sources,
        voice_profile=voice_profile,
        requested_format=requested_format
    )

    # If an asset was generated, persist it to DB and local content items
    asset = result.get("generated_asset")
    if asset and isinstance(asset, dict):
        try:
            item_id = f"item_{int(datetime.now().timestamp())}_{os.urandom(2).hex()}"
            asset_type = asset.get("type", "content")
            tier_map = {
                "carousel": "Tier 1: Swipeable Carousel",
                "essay": "Tier 2: In-Feed Essay",
                "article": "Tier 3: Executive Briefing",
                "weekly_posts": "📅 5-Day Post Series",
                "campaign_pack": "Full Campaign Distribution Pack"
            }
            tier = tier_map.get(asset_type, "Synthesized Content")
            title = asset.get("title") or (messages[-1].get("content")[:60] if messages else "NotebookLM Asset")

            new_item = {
                "id": item_id,
                "title": title,
                "tier": tier,
                "topic": title,
                "voice_profile_id": voice_id,
                "source_type": "notebook_studio",
                "source_reference": "NotebookLM Studio",
                "content_markdown": asset.get("markdown") or asset.get("article") or asset.get("copy_script") or "",
                "slides_outline": asset.get("slides") or (asset.get("carousel_1", {}).get("slides") if isinstance(asset.get("carousel_1"), dict) else []),
                "research_dossier": result.get("research_dossier", {}),
                "campaign_pack": asset if asset_type == "campaign_pack" else {},
                "weekly_posts": asset.get("posts") or asset.get("weekly_posts") or [],
                "carousel_1": asset if asset_type == "carousel" else asset.get("carousel_1", {}),
                "carousel_2": asset.get("carousel_2", {}),
                "article": asset.get("markdown") if asset_type == "article" else asset.get("article", ""),
                "status": "Ready to Publish",
                "created_at": datetime.utcnow().isoformat(),
                "updated_at": datetime.utcnow().isoformat()
            }
            if not isinstance(new_item["research_dossier"], dict):
                new_item["research_dossier"] = {}
            new_item["research_dossier"]["campaign_pack"] = {
                "weekly_posts": new_item["weekly_posts"],
                "carousel_1": new_item["carousel_1"],
                "carousel_2": new_item["carousel_2"],
                "article": new_item["article"]
            }

            if db.is_connected:
                db.save_content_item(new_item)
            save_local_content_item(new_item)
            asset["saved_item_id"] = item_id
        except Exception as e:
            print(f"[!] Error auto-saving generated notebook asset: {e}")

    return jsonify(result)


@app.route("/api/content/notebook/crm-leads")
def notebook_crm_leads():
    """
    Returns aggregated CRM leads (Executives & Podcasts) formatted for 1-click
    attachment as active reference sources in NotebookLM Studio.
    """
    media_leads = (db.get_all_media_leads() if db.is_connected else None) or tracker.get_leads()
    exec_leads = (db.get_all_executive_leads() if db.is_connected else None) or exec_tracker.get_leads()

    results = []
    for e in (exec_leads or []):
        results.append({
            "id": f"exec_{e.get('id')}",
            "name": f"{e.get('name', 'Executive')} ({e.get('company', 'Firm')})",
            "category": "Executive",
            "company": e.get("company", ""),
            "role": e.get("title", "Executive"),
            "hook": e.get("hook", ""),
            "notes": e.get("current_activity", "") or e.get("notes", ""),
            "text": f"EXECUTIVE PROFILE: {e.get('name')} | Firm: {e.get('company')} | Role: {e.get('title')}\nStrategic Angle / Hook: {e.get('hook')}\nCurrent Status / Notes: {e.get('current_activity')}\nPersona: {e.get('persona', '')}\nLinkedIn: {e.get('linkedin_url', '')}"
        })

    for p in (media_leads or []):
        results.append({
            "id": f"media_{p.get('id')}",
            "name": f"{p.get('name', 'Podcast')} (Host: {p.get('host', 'N/A')})",
            "category": "Media",
            "company": p.get("name", ""),
            "role": p.get("genre", "Audio Podcast"),
            "hook": p.get("rupert_angle") or p.get("pitch_angle") or "",
            "notes": p.get("current_activity", "") or p.get("notes", ""),
            "text": f"SHOW PROFILE: {p.get('name')} | Target Host: {p.get('host')} | Genre: {p.get('genre')}\nRupert Angle / Pitch: {p.get('rupert_angle') or p.get('pitch_angle')}\nCurrent Outreach Activity: {p.get('current_activity')}\nWebsite: {p.get('website', '')}"
        })

    return jsonify(results)


@app.route("/api/voices", methods=["GET", "POST"])
def handle_voices():
    if request.method == "POST":
        data = request.get_json() or {}
        if not data.get("id"):
            name_slug = re.sub(r'[^a-zA-Z0-9]+', '-', data.get("name", "").lower()).strip('-')
            data["id"] = f"{name_slug}-{int(datetime.now().timestamp())}" if name_slug else f"voice_{int(datetime.now().timestamp())}"
        data["updated_at"] = datetime.now().isoformat()
        if isinstance(data.get("sample_texts"), str):
            raw_samples = data["sample_texts"].strip()
            if raw_samples:
                parts = [p.strip() for p in raw_samples.split("\n\n") if p.strip()]
                data["sample_texts"] = parts if parts else [raw_samples]
            else:
                data["sample_texts"] = []
        if db.is_connected:
            db.upsert_voice_profile(data)
        profiles = get_default_voice_profiles()
        idx = next((i for i, x in enumerate(profiles) if x.get("id") == data["id"]), None)
        if idx is not None:
            profiles[idx] = data
        else:
            profiles.append(data)
        try:
            with open(VOICES_JSON_PATH, "w", encoding="utf-8") as f:
                json.dump(profiles, f, indent=2, default=str)
        except Exception as e:
            print(f"[!] Error saving voice profile to JSON: {e}")
        return jsonify(data)
    else:
        default_profiles = get_default_voice_profiles()
        if db.is_connected:
            db_profiles = db.get_voice_profiles()
            db_ids = {p.get("id") for p in db_profiles}
            synced = False
            for dp in default_profiles:
                if dp.get("id") not in db_ids:
                    db.upsert_voice_profile(dp)
                    synced = True
            if synced:
                db_profiles = db.get_voice_profiles()
            return jsonify(db_profiles if db_profiles else default_profiles)
        return jsonify(default_profiles)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    host = os.environ.get("HOST", "0.0.0.0")
    print(f"[*] Starting Media, Executive & Content Dashboard on http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
