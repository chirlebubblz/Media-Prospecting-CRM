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
            <div style="display: flex; align-items: center; gap: 6px;">
              <button class="btn-xs btn-edit" onclick="openEditLeadModal('${escapeHtml(lead.id)}', 'media')" title="Edit show details">✏️ Edit</button>
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
            <div style="display: flex; align-items: center; gap: 6px;">
              <button class="btn-xs btn-edit" onclick="openEditLeadModal('${escapeHtml(lead.id)}', 'exec')" title="Edit lead details">✏️ Edit</button>
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
  <title>Content Engine | Research Dossiers & Voice Cloning</title>
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
      gap: 16px;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-badge {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: rgba(139, 92, 246, 0.2);
      border: 1px solid rgba(139, 92, 246, 0.5);
      color: #c084fc;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: 0 0 15px rgba(139, 92, 246, 0.25);
    }
    .brand-title {
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.02em;
    }
    .brand-sub {
      font-size: 12px;
      color: var(--text-muted);
    }

    /* Container */
    .container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 24px 28px;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: #cbd5e1;
      padding: 8px 14px;
      border-radius: 7px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .btn:hover {
      background: #172540;
      border-color: var(--border-accent);
      color: #ffffff;
    }
    .btn-primary {
      background: linear-gradient(135deg, #7c3aed, #a855f7);
      border-color: #a855f7;
      color: #ffffff;
      box-shadow: 0 0 14px rgba(168, 85, 247, 0.35);
    }
    .btn-primary:hover {
      background: linear-gradient(135deg, #6d28d9, #9333ea);
      box-shadow: 0 0 18px rgba(168, 85, 247, 0.5);
      color: #ffffff;
    }
    .btn-success {
      background: rgba(16, 185, 129, 0.15);
      border-color: rgba(16, 185, 129, 0.4);
      color: #34d399;
    }
    .btn-success:hover {
      background: rgba(16, 185, 129, 0.25);
      color: #6ee7b7;
    }
    .btn-emerald {
      background: linear-gradient(135deg, #059669, #10b981);
      border-color: #10b981;
      color: #ffffff;
      font-weight: 700;
      box-shadow: 0 0 14px rgba(16, 185, 129, 0.35);
    }
    .btn-emerald:hover {
      background: linear-gradient(135deg, #047857, #059669);
      color: #ffffff;
    }
    .btn-danger {
      background: rgba(244, 63, 94, 0.15);
      border-color: rgba(244, 63, 94, 0.35);
      color: #fb7185;
    }
    .btn-danger:hover {
      background: rgba(244, 63, 94, 0.25);
      color: #fda4af;
    }
    .btn-xs {
      padding: 5px 10px;
      font-size: 11.5px;
      border-radius: 6px;
    }

    /* KPI Ribbon */
    .kpi-ribbon {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px;
      margin-bottom: 22px;
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
      background: #121c2e;
      transform: translateY(-1px);
    }
    .kpi-label {
      font-size: 11.5px;
      color: var(--text-muted);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .kpi-value {
      font-size: 26px;
      font-weight: 800;
      color: #ffffff;
      margin: 4px 0 2px 0;
      font-family: 'JetBrains Mono', monospace;
    }
    .kpi-sub {
      font-size: 11.5px;
      color: var(--text-muted);
    }

    /* Filter & Search Toolbar */
    .filter-toolbar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
      margin-bottom: 18px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      padding: 12px 18px;
      border-radius: 10px;
    }
    .search-input-wrap {
      flex: 1;
      min-width: 260px;
      position: relative;
    }
    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 14px;
      color: var(--text-muted);
      pointer-events: none;
    }
    .search-input {
      width: 100%;
      background: var(--bg);
      border: 1px solid var(--border);
      color: #ffffff;
      padding: 9px 36px 9px 34px;
      border-radius: 7px;
      font-size: 13px;
      outline: none;
      transition: all 0.2s;
    }
    .search-input:focus {
      border-color: #a855f7;
      box-shadow: 0 0 10px rgba(168, 85, 247, 0.2);
    }
    .search-clear-btn {
      position: absolute;
      right: 10px;
      top: 50%;
      transform: translateY(-50%);
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 14px;
      cursor: pointer;
    }
    .filter-controls {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .select-filter {
      background: var(--bg);
      border: 1px solid var(--border);
      color: #cbd5e1;
      padding: 8px 12px;
      border-radius: 7px;
      font-size: 12.5px;
      outline: none;
      cursor: pointer;
    }
    .select-filter:focus {
      border-color: #a855f7;
    }

    /* Quick Filter Pills */
    .quick-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 20px;
      background: rgba(14, 22, 38, 0.7);
      border: 1px solid var(--border);
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s;
    }
    .quick-pill:hover {
      border-color: var(--border-accent);
      color: #ffffff;
    }
    .quick-pill.active {
      background: rgba(168, 85, 247, 0.2);
      border-color: #a855f7;
      color: #c4b5fd;
    }
    .quick-pill.pill-emerald.active {
      background: rgba(16, 185, 129, 0.2);
      border-color: #10b981;
      color: #34d399;
    }

    /* Content Cards Grid */
    .content-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 18px;
    }
    .content-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: all 0.2s;
    }
    .content-card:hover {
      border-color: var(--border-accent);
      background: var(--card-hover);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    .tier-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 9px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.03em;
    }
    .tier-badge.t1 { background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.35); }
    .tier-badge.t2 { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35); }
    .tier-badge.t3 { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.35); }

    .content-card-title {
      font-size: 16px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
      cursor: pointer;
    }
    .content-card-title:hover {
      color: var(--primary);
    }
    .content-card-excerpt {
      font-size: 12.5px;
      color: #94a3b8;
      line-height: 1.5;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      white-space: pre-wrap;
    }
    .dossier-stats-strip {
      background: rgba(7, 11, 20, 0.6);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 8px 12px;
      font-size: 11.5px;
      color: #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .content-actions-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border);
      padding-top: 10px;
      margin-top: auto;
    }

    /* Modals */
    .modal-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(8px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-overlay.active {
      display: flex;
    }
    .modal-card {
      background: #0f172a;
      border: 1px solid var(--border-accent);
      border-radius: 14px;
      width: 100%;
      max-width: 620px;
      max-height: 90vh;
      overflow-y: auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
    }
    .modal-card-lg { max-width: 760px; }
    .modal-card-xl { max-width: 900px; }
    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 12px;
    }
    .modal-title {
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
    }
    .close-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 22px;
      cursor: pointer;
      line-height: 1;
    }
    .close-btn:hover { color: #ffffff; }

    /* Form Fields */
    .form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .form-label {
      font-size: 12px;
      font-weight: 700;
      color: #cbd5e1;
    }
    .form-input {
      background: rgba(7, 11, 20, 0.8);
      border: 1px solid var(--border);
      color: #ffffff;
      padding: 9px 12px;
      border-radius: 7px;
      font-size: 13px;
      outline: none;
      font-family: inherit;
    }
    .form-input:focus {
      border-color: #a855f7;
      box-shadow: 0 0 10px rgba(168, 85, 247, 0.2);
    }
    .form-row-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }

    /* Modal Tabs Header */
    .modal-tabs-header {
      display: flex;
      gap: 6px;
      background: rgba(7, 11, 20, 0.6);
      padding: 4px;
      border-radius: 8px;
      border: 1px solid var(--border);
      margin-bottom: 12px;
    }
    .modal-tab-btn {
      flex: 1;
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 8px 12px;
      font-size: 12px;
      font-weight: 700;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .modal-tab-btn:hover { color: #ffffff; background: rgba(255, 255, 255, 0.05); }
    .modal-tab-btn.active {
      background: #1e293b;
      color: #38bdf8;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }

    /* Slide Deck Viewer */
    .slide-deck-viewer {
      background: rgba(7, 11, 20, 0.7);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .slide-deck-nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
    }
    .slide-card-presentation {
      background: linear-gradient(135deg, #121c2e, #0e1626);
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: 8px;
      padding: 20px;
      min-height: 140px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      position: relative;
    }
    .slide-number-pill {
      position: absolute;
      top: 12px;
      right: 14px;
      font-size: 11px;
      font-weight: 800;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.15);
      padding: 2px 8px;
      border-radius: 12px;
    }
    .slide-headline-text {
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.35;
      margin-bottom: 8px;
    }
    .slide-bullet-text {
      font-size: 13.5px;
      color: #cbd5e1;
      line-height: 1.5;
      white-space: pre-wrap;
    }

    /* Hook & Quote Box */
    .hook-box {
      background: rgba(168, 85, 247, 0.08);
      border-left: 3px solid #a855f7;
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      font-size: 12.5px;
      color: #e2e8f0;
      font-style: italic;
    }

    /* Spinner */
    .spinner-box {
      display: none;
      text-align: center;
      padding: 20px;
      background: rgba(7, 11, 20, 0.6);
      border: 1px dashed var(--border);
      border-radius: 8px;
      font-size: 13px;
      color: #38bdf8;
    }
    .spinner-icon {
      font-size: 26px;
      display: inline-block;
      animation: spin 1s infinite linear;
      margin-bottom: 6px;
    }
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

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
      <div class="brand-badge">📝</div>
      <div>
        <div class="brand-title" style="display: flex; align-items: center; gap: 8px;">
          <span>Content Engine</span>
          <span style="font-size: 11px; padding: 2px 8px; border-radius: 12px; background: rgba(139, 92, 246, 0.2); color: #c4b5fd; border: 1px solid rgba(139, 92, 246, 0.4);">Voice Cloning Studio</span>
        </div>
        <div class="brand-sub">Research Dossiers & Author Voice Cloning</div>
      </div>
    </div>

    <div style="display: flex; align-items: center; gap: 10px;">
      <a href="/" class="btn" style="text-decoration:none;"><span>⬅️ Back to CRM Leads</span></a>
      <button class="btn btn-primary" onclick="openCreateModal()"><span>✨ Synthesize New Content</span></button>
    </div>
  </header>

  <!-- Main Container -->
  <main class="container">

    <!-- KPI Summary Ribbon -->
    <div class="kpi-ribbon" id="kpi-ribbon">
      <div class="kpi-card" onclick="setQuickTierFilter('ALL')">
        <div class="kpi-label">Total Content Pieces</div>
        <div class="kpi-value" id="kpi-total-content" style="color: #c084fc;">0</div>
        <div class="kpi-sub">Synthesized pieces</div>
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
        <input type="text" id="content-search-input" class="search-input" placeholder="Search content pieces by title, thesis, or topic..." oninput="handleContentSearch()">
        <button id="search-clear-btn" class="search-clear-btn" onclick="clearContentSearch()" style="display: none;">✕</button>
      </div>

      <div class="filter-controls">
        <select id="tier-filter-select" class="select-filter" onchange="handleFilterChange()">
          <option value="ALL">All Tiers</option>
          <option value="Tier 1">Tier 1: Swipeable Carousel</option>
          <option value="Tier 2">Tier 2: In-Feed Essay</option>
          <option value="Tier 3">Tier 3: Executive Briefing</option>
        </select>

        <select id="voice-filter-select" class="select-filter" onchange="handleFilterChange()">
          <option value="ALL">All Voices</option>
          <option value="forensic-operator">Forensic Risk Operator</option>
          <option value="growth-dealmaker">Strategic Dealmaker</option>
          <option value="custom">Custom Voice</option>
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
      <span class="quick-pill active" id="qp-all" onclick="setQuickTierFilter('ALL')">All Tiers <span id="pill-all-count">(0)</span></span>
      <span class="quick-pill pill-purple" id="qp-t1" onclick="setQuickTierFilter('Tier 1')">Tier 1: Carousels <span id="pill-t1-count">(0)</span></span>
      <span class="quick-pill pill-emerald" id="qp-t2" onclick="setQuickTierFilter('Tier 2')">Tier 2: Essays <span id="pill-t2-count">(0)</span></span>
      <span class="quick-pill" id="qp-t3" onclick="setQuickTierFilter('Tier 3')">Tier 3: Briefings <span id="pill-t3-count">(0)</span></span>
    </div>

    <!-- Content Cards Grid -->
    <div class="content-grid" id="content-cards-container">
      <!-- Injected via JavaScript -->
    </div>

  </main>

  <!-- Content View Modal (Slide Deck & Post Copy) -->
  <div class="modal-overlay" id="content-view-modal">
    <div class="modal-card modal-card-xl">
      <div class="modal-header">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span id="view-content-tier-badge" class="tier-badge t1">Tier 1</span>
          <div class="modal-title" id="view-content-title">Content Title</div>
        </div>
        <button class="close-btn" onclick="closeContentViewModal()">&times;</button>
      </div>

      <!-- Quick Action Copy Bar -->
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; background: rgba(7, 11, 20, 0.5); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border); flex-wrap: wrap;">
        <div style="font-size: 12px; color: var(--text-muted);">
          Source: <span id="view-content-source-label" style="color: #ffffff; font-weight: 600;">Document</span>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <button class="btn btn-primary btn-xs" onclick="copyFullPost()">📋 Copy Full Post</button>
          <button class="btn btn-xs" id="btn-copy-slide-script" onclick="copySlideScript()" style="display: none;">📑 Copy Slide Script</button>
          <button class="btn btn-xs" onclick="copyLinkedInPost()">💼 Copy for LinkedIn</button>
          <button class="btn btn-xs" onclick="copyBriefing()">📄 Copy Briefing</button>
          <button class="btn btn-xs" onclick="copyMarkdown()">⬇️ Copy Markdown</button>
        </div>
      </div>

      <!-- Slide Deck Viewer (For Carousels) -->
      <div class="slide-deck-viewer" id="slide-deck-container" style="display: none;">
        <div class="slide-deck-nav">
          <button class="btn btn-xs" onclick="navigateSlide(-1)">◀ Prev Slide</button>
          <span id="slide-counter-text" style="font-size: 12.5px; font-weight: 700; color: #38bdf8;">Slide 1 of 5</span>
          <button class="btn btn-xs" onclick="navigateSlide(1)">Next Slide ▶</button>
        </div>
        <div class="slide-card-presentation">
          <span class="slide-number-pill" id="slide-current-number">#1</span>
          <div class="slide-headline-text" id="slide-current-headline">Headline</div>
          <div class="slide-bullet-text" id="slide-current-bullet">Bullet text</div>
        </div>
      </div>

      <!-- Content Markdown Reader -->
      <div class="form-group" style="margin-top: 14px;">
        <label class="form-label" style="display: flex; justify-content: space-between; align-items: center;">
          <span>Formatted Content / Copy:</span>
          <span style="font-size: 11px; color: var(--text-muted);">Ready to paste directly into LinkedIn or newsletter</span>
        </label>
        <textarea id="view-content-markdown" class="form-input" style="height: 320px; font-family: inherit; font-size: 13px; line-height: 1.6;" readonly></textarea>
      </div>

      <div style="display: flex; justify-content: flex-end; gap: 8px; border-top: 1px solid var(--border); padding-top: 14px;">
        <button class="btn" onclick="closeContentViewModal()">Close</button>
      </div>
    </div>
  </div>

  <!-- Research Dossier Modal -->
  <div class="modal-overlay" id="dossier-modal">
    <div class="modal-card modal-card-lg">
      <div class="modal-header">
        <div class="modal-title" id="dossier-modal-title">🔬 Verified Research Dossier</div>
        <button class="close-btn" onclick="closeDossierModal()">&times;</button>
      </div>

      <div style="display: flex; flex-direction: column; gap: 14px;">
        <div style="background: rgba(56, 189, 248, 0.05); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 10px; padding: 14px;">
          <div style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase;">Core Thesis:</div>
          <div id="dossier-thesis" style="font-size: 14px; font-weight: 600; color: #ffffff; margin-top: 4px;"></div>
          <div style="font-size: 11px; font-weight: 700; color: #c084fc; text-transform: uppercase; margin-top: 10px;">Unseen Tension:</div>
          <div id="dossier-tension" style="font-size: 13px; color: #cbd5e1; margin-top: 3px;"></div>
        </div>

        <div>
          <div class="form-label" style="margin-bottom: 8px;">📊 Verified Facts & Data Points:</div>
          <div id="dossier-data-points" style="display: flex; flex-direction: column; gap: 8px;"></div>
        </div>

        <div>
          <div class="form-label" style="margin-bottom: 8px;">💬 Forensic Quotes & Mental Models:</div>
          <div id="dossier-quotes" style="display: flex; flex-direction: column; gap: 6px;"></div>
        </div>

        <div>
          <div class="form-label" style="margin-bottom: 8px;">🔗 Citations & Sources:</div>
          <div id="dossier-citations" style="display: flex; flex-direction: column; gap: 6px;"></div>
        </div>
      </div>

      <div style="display: flex; justify-content: flex-end; border-top: 1px solid var(--border); padding-top: 14px; margin-top: 10px;">
        <button class="btn" onclick="closeDossierModal()">Close</button>
      </div>
    </div>
  </div>

  <!-- Synthesize New Content Modal -->
  <div class="modal-overlay" id="new-content-modal">
    <div class="modal-card modal-card-lg">
      <div class="modal-header">
        <div>
          <div class="modal-title">✨ Synthesize New Content</div>
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">
            Synthesize PDFs, web URLs, briefs, or CRM lead angles into ready-to-publish content conditioned on author voices.
          </div>
        </div>
        <button class="close-btn" onclick="closeNewContentModal()">&times;</button>
      </div>

      <!-- 4 Input Mode Tabs -->
      <div>
        <label class="form-label">Select Knowledge / Research Source:</label>
        <div class="modal-tabs-header">
          <button class="modal-tab-btn active" id="tab-src-pdf" onclick="switchContentSourceTab('pdf')">📄 Upload PDF</button>
          <button class="modal-tab-btn" id="tab-src-url" onclick="switchContentSourceTab('url')">🌐 Web URL</button>
          <button class="modal-tab-btn" id="tab-src-text" onclick="switchContentSourceTab('text')">✍️ Paste Text / .MD</button>
          <button class="modal-tab-btn" id="tab-src-lead" onclick="switchContentSourceTab('lead')">🎯 Select Lead Hook</button>
        </div>
      </div>

      <!-- PDF Tab Panel -->
      <div id="panel-src-pdf" style="display: block;">
        <div class="form-group">
          <label class="form-label">Upload PDF Document / Whitepaper</label>
          <input type="file" id="gen-pdf-file" accept=".pdf" class="form-input" style="padding: 14px; background: rgba(7, 11, 20, 0.4); border: 2px dashed var(--border);">
          <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 4px;">Supports industry reports, academic papers, regulatory guidance, and pitch decks.</div>
        </div>
      </div>

      <!-- URL Tab Panel -->
      <div id="panel-src-url" style="display: none;">
        <div class="form-group">
          <label class="form-label">Article, Report, or Substack URL *</label>
          <input type="url" id="gen-url-input" class="form-input" placeholder="https://www.wsj.com/... or https://subdomain.substack.com/p/...">
        </div>
      </div>

      <!-- Text Tab Panel -->
      <div id="panel-src-text" style="display: none;">
        <div class="form-group">
          <label class="form-label">Executive Briefing, Speech Transcript, or Raw Markdown</label>
          <textarea id="gen-text-input" class="form-input" rows="5" placeholder="Paste report excerpts, interview transcripts, or rough thesis bullets..."></textarea>
        </div>
      </div>

      <!-- Lead Tab Panel -->
      <div id="panel-src-lead" style="display: none;">
        <div class="form-row-2col">
          <div class="form-group">
            <label class="form-label">Pipeline Source</label>
            <select id="gen-lead-pipeline" class="form-input" onchange="populateLeadDropdown()">
              <option value="media">🎙️ Podcast & Media Host</option>
              <option value="exec">💼 Executive & Dealmaker</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Select CRM Target Lead</label>
            <select id="gen-lead-id" class="form-input"></select>
          </div>
        </div>
      </div>

      <!-- Generation Settings -->
      <div class="form-row-2col">
        <div class="form-group">
          <label class="form-label">Content Tier Format *</label>
          <select id="gen-tier-select" class="form-input">
            <option value="Tier 1: Short-Form Carousel" selected>Tier 1: Swipeable Carousel & Companion Post</option>
            <option value="Tier 2: In-Feed Long-Form Essay">Tier 2: In-Feed Long-Form Essay</option>
            <option value="Tier 3: LinkedIn Article">Tier 3: Executive Briefing / Article</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Author Voice Profile</label>
          <select id="gen-voice-select" class="form-input">
            <option value="forensic-operator">Rupert / Forensic Risk Operator (Contrarian, Zero Fluff)</option>
            <option value="growth-dealmaker">Strategic Dealmaker & M&A Operator (Commercially Sharp)</option>
            <option value="custom">Custom Voice</option>
          </select>
        </div>
      </div>

      <div class="form-group">
        <label class="form-label">Working Title / Core Topic Angle (Optional)</label>
        <input type="text" id="gen-topic-input" class="form-input" placeholder="e.g. Why Traditional Compliance Creates Fraud Risk">
      </div>

      <div class="spinner-box" id="gen-spinner">
        <div class="spinner-icon">⚡</div>
        <div>Mining research facts, extracting quotes, and conditioning voice output...</div>
        <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 4px;">Takes about 2 to 4 seconds.</div>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border); padding-top: 14px;" id="gen-actions">
        <button class="btn" onclick="closeNewContentModal()">Cancel</button>
        <button class="btn btn-emerald" onclick="generateContent()" style="padding: 9px 20px;">
          <span>⚡ Generate Content & Dossier</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Toast Element -->
  <div id="toast">Saved</div>

  <!-- Client JavaScript -->
  <script>
    let contentItems = [];
    let voiceProfiles = [];
    let mediaLeads = [];
    let execLeads = [];
    let tierFilter = 'ALL';
    let voiceFilter = 'ALL';
    let searchQuery = '';
    let sortOrder = 'newest';
    let currentModalContentItem = null;
    let currentSlideIndex = 0;
    let currentSourceTab = 'pdf';

    async function loadContentPageData() {
      try {
        const [resContent, resVoices, resMedia, resExec] = await Promise.all([
          fetch('/api/content').then(r => r.json()).catch(() => []),
          fetch('/api/voices').then(r => r.json()).catch(() => []),
          fetch('/api/leads').then(r => r.json()).catch(() => []),
          fetch('/api/executives').then(r => r.json()).catch(() => [])
        ]);

        contentItems = Array.isArray(resContent) ? resContent : [];
        voiceProfiles = Array.isArray(resVoices) ? resVoices : [];
        mediaLeads = Array.isArray(resMedia) ? resMedia : [];
        execLeads = Array.isArray(resExec) ? resExec : [];

        updateCountersAndPills();
        populateLeadDropdown();
        renderContentGrid();
      } catch (err) {
        console.error('Error loading content data:', err);
        showToast('Error loading content data');
      }
    }

    function updateCountersAndPills() {
      const total = contentItems.length;
      const t1 = contentItems.filter(c => (c.tier || '').includes('Tier 1')).length;
      const t2 = contentItems.filter(c => (c.tier || '').includes('Tier 2')).length;
      const t3 = contentItems.filter(c => (c.tier || '').includes('Tier 3') || (c.tier || '').toLowerCase().includes('article')).length;
      const facts = contentItems.reduce((acc, c) => acc + ((c.research_dossier && c.research_dossier.data_points) ? c.research_dossier.data_points.length : 0), 0);

      document.getElementById('kpi-total-content').innerText = total;
      document.getElementById('kpi-t1-count').innerText = t1;
      document.getElementById('kpi-t2-count').innerText = t2;
      document.getElementById('kpi-t3-count').innerText = t3;
      document.getElementById('kpi-facts-count').innerText = facts;

      document.getElementById('pill-all-count').innerText = `(${total})`;
      document.getElementById('pill-t1-count').innerText = `(${t1})`;
      document.getElementById('pill-t2-count').innerText = `(${t2})`;
      document.getElementById('pill-t3-count').innerText = `(${t3})`;
    }

    function renderContentGrid() {
      const container = document.getElementById('content-cards-container');
      let filtered = contentItems.slice();

      // Tier filter
      if (tierFilter !== 'ALL') {
        filtered = filtered.filter(c => (c.tier || '').toLowerCase().includes(tierFilter.toLowerCase()));
      }

      // Voice filter
      if (voiceFilter !== 'ALL') {
        filtered = filtered.filter(c => (c.voice_profile_id || '').toLowerCase() === voiceFilter.toLowerCase());
      }

      // Search query
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase().trim();
        filtered = filtered.filter(c => {
          const title = (c.title || '').toLowerCase();
          const topic = (c.topic || '').toLowerCase();
          const text = (c.content_markdown || '').toLowerCase();
          const thesis = ((c.research_dossier && c.research_dossier.thesis) || '').toLowerCase();
          return title.includes(q) || topic.includes(q) || text.includes(q) || thesis.includes(q);
        });
      }

      // Sort
      if (sortOrder === 'alpha') {
        filtered.sort((a, b) => (a.title || '').localeCompare(b.title || ''));
      } else if (sortOrder === 'oldest') {
        filtered.sort((a, b) => (a.created_at || '').localeCompare(b.created_at || ''));
      } else {
        filtered.sort((a, b) => (b.created_at || '').localeCompare(a.created_at || ''));
      }

      if (filtered.length === 0) {
        container.innerHTML = `
          <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; background: var(--bg-surface); border: 1px dashed var(--border); border-radius: 12px;">
            <div style="font-size: 32px; margin-bottom: 8px;">📝</div>
            <div style="font-size: 15px; font-weight: 700; color: #ffffff;">No content pieces match this filter</div>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 4px;">Click "✨ Synthesize New Content" to create research-backed copy.</div>
          </div>
        `;
        return;
      }

      container.innerHTML = filtered.map(item => {
        const isT1 = (item.tier || '').includes('Tier 1');
        const isT2 = (item.tier || '').includes('Tier 2');
        const tierClass = isT1 ? 't1' : (isT2 ? 't2' : 't3');
        const factsCount = (item.research_dossier && item.research_dossier.data_points) ? item.research_dossier.data_points.length : 0;
        const citesCount = (item.research_dossier && item.research_dossier.citations) ? item.research_dossier.citations.length : 0;
        const slidesCount = Array.isArray(item.slides_outline) ? item.slides_outline.length : 0;

        return `
          <div class="content-card">
            <div style="display: flex; justify-content: space-between; align-items: center; gap: 8px;">
              <span class="tier-badge ${tierClass}">${escapeHtml(item.tier || 'Content')}</span>
              <span style="font-size: 11px; padding: 2px 8px; border-radius: 12px; background: var(--tag-bg); color: #94a3b8; border: 1px solid var(--border);">${escapeHtml(item.topic || 'General')}</span>
            </div>

            <div class="content-card-title" onclick="openContentViewModal('${escapeHtml(item.id)}')">
              ${escapeHtml(item.title || 'Untitled Post')}
            </div>

            <div style="font-size: 11px; color: var(--text-muted); display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">
              <span>Source:</span>
              <span style="color: #cbd5e1; font-weight: 600;">${escapeHtml(item.source_reference || item.source_type || 'Internal')}</span>
              ${isT1 && slidesCount ? `<span>• 📑 ${slidesCount} Slides</span>` : ''}
            </div>

            <div class="content-card-excerpt">
              ${escapeHtml(item.content_markdown || '')}
            </div>

            <div class="dossier-stats-strip">
              <span>🔬 <strong>${factsCount}</strong> Research Facts</span>
              <span>🔗 <strong>${citesCount}</strong> Citations</span>
            </div>

            <div class="content-actions-footer">
              <div style="display: flex; gap: 6px;">
                <button class="btn btn-primary btn-xs" onclick="openContentViewModal('${escapeHtml(item.id)}')">👁️ View / Copy</button>
                <button class="btn btn-xs" onclick="openDossierModal('${escapeHtml(item.id)}')">🔬 Dossier</button>
              </div>
              <button class="btn btn-danger btn-xs" onclick="deleteContentItem('${escapeHtml(item.id)}')">🗑️</button>
            </div>
          </div>
        `;
      }).join('');
    }

    function handleContentSearch() {
      const input = document.getElementById('content-search-input');
      const clearBtn = document.getElementById('search-clear-btn');
      searchQuery = input.value;
      clearBtn.style.display = searchQuery ? 'block' : 'none';
      renderContentGrid();
    }

    function clearContentSearch() {
      const input = document.getElementById('content-search-input');
      const clearBtn = document.getElementById('search-clear-btn');
      input.value = '';
      searchQuery = '';
      clearBtn.style.display = 'none';
      renderContentGrid();
    }

    function handleFilterChange() {
      tierFilter = document.getElementById('tier-filter-select').value;
      voiceFilter = document.getElementById('voice-filter-select').value;
      sortOrder = document.getElementById('sort-order-select').value;
      updatePillsState();
      renderContentGrid();
    }

    function setQuickTierFilter(tier) {
      tierFilter = tier;
      document.getElementById('tier-filter-select').value = tier;
      updatePillsState();
      renderContentGrid();
    }

    function updatePillsState() {
      document.querySelectorAll('#quick-filter-pills .quick-pill').forEach(p => p.classList.remove('active'));
      if (tierFilter === 'ALL') document.getElementById('qp-all').classList.add('active');
      else if (tierFilter.includes('Tier 1')) document.getElementById('qp-t1').classList.add('active');
      else if (tierFilter.includes('Tier 2')) document.getElementById('qp-t2').classList.add('active');
      else if (tierFilter.includes('Tier 3')) document.getElementById('qp-t3').classList.add('active');
    }

    /* Modal Open / Close */
    function openCreateModal() {
      openNewContentModal();
    }

    function openNewContentModal() {
      document.getElementById('new-content-modal').classList.add('active');
      switchContentSourceTab('pdf');
      populateLeadDropdown();
    }

    function closeNewContentModal() {
      document.getElementById('new-content-modal').classList.remove('active');
      document.getElementById('gen-spinner').style.display = 'none';
      document.getElementById('gen-actions').style.display = 'flex';
    }

    function switchContentSourceTab(tab) {
      currentSourceTab = tab;
      document.querySelectorAll('.modal-tab-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(`tab-src-${tab}`).classList.add('active');

      document.getElementById('panel-src-pdf').style.display = tab === 'pdf' ? 'block' : 'none';
      document.getElementById('panel-src-url').style.display = tab === 'url' ? 'block' : 'none';
      document.getElementById('panel-src-text').style.display = tab === 'text' ? 'block' : 'none';
      document.getElementById('panel-src-lead').style.display = tab === 'lead' ? 'block' : 'none';
    }

    function populateLeadDropdown() {
      const pipe = document.getElementById('gen-lead-pipeline').value;
      const select = document.getElementById('gen-lead-id');
      const list = pipe === 'media' ? mediaLeads : execLeads;

      if (!list || list.length === 0) {
        select.innerHTML = '<option value="">No leads available</option>';
        return;
      }

      select.innerHTML = list.map(l => `
        <option value="${escapeHtml(l.id)}">${escapeHtml(l.name)} (${escapeHtml(l.company || l.genre || 'Lead')})</option>
      `).join('');
    }

    async function generateContent() {
      const tier = document.getElementById('gen-tier-select').value;
      const voiceId = document.getElementById('gen-voice-select').value;
      const topic = document.getElementById('gen-topic-input').value.trim();

      const spinner = document.getElementById('gen-spinner');
      const actions = document.getElementById('gen-actions');
      spinner.style.display = 'block';
      actions.style.display = 'none';

      try {
        let res;
        if (currentSourceTab === 'pdf') {
          const fileInput = document.getElementById('gen-pdf-file');
          if (!fileInput.files || fileInput.files.length === 0) {
            alert('Please select a PDF file to upload.');
            spinner.style.display = 'none';
            actions.style.display = 'flex';
            return;
          }
          const formData = new FormData();
          formData.append('file', fileInput.files[0]);
          formData.append('source_type', 'pdf');
          formData.append('tier', tier);
          formData.append('voice_id', voiceId);
          if (topic) formData.append('topic', topic);

          res = await fetch('/api/content/generate', {
            method: 'POST',
            body: formData
          });
        } else if (currentSourceTab === 'url') {
          const url = document.getElementById('gen-url-input').value.trim();
          if (!url) {
            alert('Please enter a web URL.');
            spinner.style.display = 'none';
            actions.style.display = 'flex';
            return;
          }
          res = await fetch('/api/content/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              source_type: 'url',
              url: url,
              tier: tier,
              voice_id: voiceId,
              topic: topic
            })
          });
        } else if (currentSourceTab === 'text') {
          const text = document.getElementById('gen-text-input').value.trim();
          if (!text) {
            alert('Please paste source text or briefing notes.');
            spinner.style.display = 'none';
            actions.style.display = 'flex';
            return;
          }
          res = await fetch('/api/content/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              source_type: 'text',
              text: text,
              tier: tier,
              voice_id: voiceId,
              topic: topic || 'Strategic Leadership'
            })
          });
        } else {
          const leadId = document.getElementById('gen-lead-id').value;
          const leadType = document.getElementById('gen-lead-pipeline').value;
          res = await fetch('/api/content/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              source_type: 'lead',
              lead_id: leadId,
              lead_type: leadType,
              tier: tier,
              voice_id: voiceId,
              topic: topic
            })
          });
        }

        if (!res.ok) {
          const errData = await res.json().catch(() => ({}));
          throw new Error(errData.error || 'Failed to generate content');
        }

        const createdItem = await res.json();
        contentItems.unshift(createdItem);

        closeNewContentModal();
        updateCountersAndPills();
        renderContentGrid();
        showToast('✨ Voice-conditioned content generated successfully!');
        openContentViewModal(createdItem.id);
      } catch (err) {
        console.error('Error generating content:', err);
        alert(`Generation failed: ${err.message}`);
        spinner.style.display = 'none';
        actions.style.display = 'flex';
      }
    }

    async function deleteContentItem(itemId) {
      if (!confirm('Are you sure you want to permanently delete this content piece?')) return;
      try {
        const res = await fetch('/api/content/delete', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id: itemId })
        });
        if (res.ok) {
          contentItems = contentItems.filter(c => c.id !== itemId);
          updateCountersAndPills();
          renderContentGrid();
          showToast('Content piece deleted');
        }
      } catch (err) {
        showToast('Error deleting content piece');
      }
    }

    /* Content View Modal */
    function openContentViewModal(itemId) {
      const item = contentItems.find(c => c.id === itemId);
      if (!item) return;
      currentModalContentItem = item;

      document.getElementById('view-content-title').innerText = item.title || 'Untitled Post';
      const badge = document.getElementById('view-content-tier-badge');
      const isT1 = (item.tier || '').includes('Tier 1');
      const isT2 = (item.tier || '').includes('Tier 2');
      badge.className = `tier-badge ${isT1 ? 't1' : (isT2 ? 't2' : 't3')}`;
      badge.innerText = item.tier || 'Content';

      document.getElementById('view-content-source-label').innerText = `${item.source_reference || item.source_type} (${item.topic})`;
      document.getElementById('view-content-markdown').value = item.content_markdown || '';

      const slideContainer = document.getElementById('slide-deck-container');
      const copyScriptBtn = document.getElementById('btn-copy-slide-script');

      if (isT1 && Array.isArray(item.slides_outline) && item.slides_outline.length > 0) {
        slideContainer.style.display = 'flex';
        copyScriptBtn.style.display = 'inline-flex';
        currentSlideIndex = 0;
        updateSlideView();
      } else {
        slideContainer.style.display = 'none';
        copyScriptBtn.style.display = 'none';
      }

      document.getElementById('content-view-modal').classList.add('active');
    }

    function closeContentViewModal() {
      document.getElementById('content-view-modal').classList.remove('active');
      currentModalContentItem = null;
    }

    function navigateSlide(delta) {
      if (!currentModalContentItem || !currentModalContentItem.slides_outline) return;
      const slides = currentModalContentItem.slides_outline;
      currentSlideIndex = Math.max(0, Math.min(slides.length - 1, currentSlideIndex + delta));
      updateSlideView();
    }

    function updateSlideView() {
      if (!currentModalContentItem || !currentModalContentItem.slides_outline) return;
      const slides = currentModalContentItem.slides_outline;
      const slide = slides[currentSlideIndex];
      if (!slide) return;

      document.getElementById('slide-counter-text').innerText = `Slide ${currentSlideIndex + 1} of ${slides.length}`;
      document.getElementById('slide-current-number').innerText = `#${slide.slide || (currentSlideIndex + 1)}`;
      document.getElementById('slide-current-headline').innerText = slide.headline || '';
      document.getElementById('slide-current-bullet').innerText = slide.bullet || '';
    }

    /* Copy Actions */
    function copyFullPost() {
      if (!currentModalContentItem) return;
      copyText(currentModalContentItem.content_markdown || '');
    }

    function copySlideScript() {
      if (!currentModalContentItem || !currentModalContentItem.slides_outline) return;
      const script = currentModalContentItem.slides_outline.map(s => `[Slide ${s.slide}]
${s.headline}
${s.bullet}
`).join('\n');
      copyText(script);
    }

    function copyLinkedInPost() {
      if (!currentModalContentItem) return;
      copyText(currentModalContentItem.content_markdown || '');
    }

    function copyBriefing() {
      if (!currentModalContentItem) return;
      const d = currentModalContentItem.research_dossier || {};
      let text = `# ${currentModalContentItem.title}

Thesis: ${d.thesis || ''}

Tension: ${d.unseen_tension || ''}

`;
      if (d.data_points) {
        text += `Key Facts:\n` + d.data_points.map(dp => `- ${dp.fact} (${dp.source})`).join('\n') + `\n\n`;
      }
      text += currentModalContentItem.content_markdown || '';
      copyText(text);
    }

    function copyMarkdown() {
      if (!currentModalContentItem) return;
      copyText(currentModalContentItem.content_markdown || '');
    }

    function copyText(str) {
      if (!str) return;
      navigator.clipboard.writeText(str).then(() => {
        showToast('Copied to clipboard');
      }).catch(() => {
        showToast('Copied text');
      });
    }

    /* Dossier Modal */
    function openDossierModal(itemId) {
      const item = contentItems.find(c => c.id === itemId);
      if (!item) return;

      const d = item.research_dossier || {};
      document.getElementById('dossier-modal-title').innerText = `🔬 Verified Dossier: ${item.title}`;
      document.getElementById('dossier-thesis').innerText = d.thesis || item.title || 'Core investigative thesis.';
      document.getElementById('dossier-tension').innerText = d.unseen_tension || 'Frontline operational workarounds bypass formal controls.';

      // Data points
      const dpContainer = document.getElementById('dossier-data-points');
      if (d.data_points && d.data_points.length > 0) {
        dpContainer.innerHTML = d.data_points.map(dp => `
          <div style="background: rgba(7, 11, 20, 0.6); border: 1px solid var(--border); border-radius: 8px; padding: 10px 14px;">
            <div style="font-size: 13px; color: #ffffff; font-weight: 500;">📌 ${escapeHtml(dp.fact)}</div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">
              Source: <span style="color: #38bdf8;">${escapeHtml(dp.source)}</span>
              ${dp.url ? ` • <a href="${escapeHtml(dp.url)}" target="_blank" style="color: #38bdf8; text-decoration: underline;">View Citation ↗</a>` : ''}
            </div>
          </div>
        `).join('');
      } else {
        dpContainer.innerHTML = `<div style="font-size: 12px; color: var(--text-muted);">No structured facts extracted.</div>`;
      }

      // Quotes
      const qContainer = document.getElementById('dossier-quotes');
      if (d.quotes && d.quotes.length > 0) {
        qContainer.innerHTML = d.quotes.map(q => `
          <div class="hook-box">
            "${escapeHtml(q)}"
          </div>
        `).join('');
      } else {
        qContainer.innerHTML = `<div style="font-size: 12px; color: var(--text-muted);">No direct quotes extracted.</div>`;
      }

      // Citations
      const cContainer = document.getElementById('dossier-citations');
      if (d.citations && d.citations.length > 0) {
        cContainer.innerHTML = d.citations.map(c => `
          <div style="font-size: 12px; color: #cbd5e1; display: flex; align-items: center; gap: 6px;">
            <span>🔗</span>
            ${c.url ? `<a href="${escapeHtml(c.url)}" target="_blank" style="color: #38bdf8; text-decoration: underline;">${escapeHtml(c.title || c.url)}</a>` : `<span>${escapeHtml(c.title)}</span>`}
          </div>
        `).join('');
      } else {
        cContainer.innerHTML = `<div style="font-size: 12px; color: var(--text-muted);">No citation links indexed.</div>`;
      }

      document.getElementById('dossier-modal').classList.add('active');
    }

    function closeDossierModal() {
      document.getElementById('dossier-modal').classList.remove('active');
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

    function escapeHtml(str) {
      if (!str) return '';
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // Initialize
    loadContentPageData();
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
from src.content.engine import ResearchSynthesizer, extract_text_from_pdf, extract_text_from_url

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
            "name": "Rupert / Forensic Risk Operator",
            "role": "Crisis Investigator & Board Risk Advisor",
            "philosophy": "Corporate failures and breakdowns are driven by human behaviour under pressure, not lack of paperwork. Traditional compliance creates an illusion of security.",
            "tone": "Authoritative, analytical, contrarian yet constructive, grounded, zero corporate fluff, forensic insider.",
            "cadence": "Short 1-2 sentence lines with double spacing. Punchy, memorable mental models.",
            "banned_words": "delve, game-changer, holistic journey, agree?, synergy, paradigm shift"
        },
        {
            "id": "growth-dealmaker",
            "name": "Strategic Dealmaker & M&A Operator",
            "role": "Private Equity Partner & Strategic Acquirer",
            "philosophy": "Value creation in M&A happens through operational discipline and cultural integration, not financial engineering.",
            "tone": "Pragmatic, commercially sharp, direct, experienced, metric-informed.",
            "cadence": "Concise bullets, clear investment theses, stark risk-reward comparisons.",
            "banned_words": "revolutionary, disruptive, silver bullet, no-brainer, unicorn vibes"
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
    if db.is_connected:
        items = db.get_content_items()
        if items:
            return jsonify(items)
    return jsonify(load_local_content())


@app.route("/api/content/generate", methods=["POST"])
def generate_content_item():
    is_form = request.content_type and "multipart/form-data" in request.content_type
    
    if is_form:
        source_type = request.form.get("source_type", "text")
        tier = request.form.get("tier", "Tier 1: Short-Form Carousel")
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
        tier = data.get("tier", "Tier 1: Short-Form Carousel")
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

    voice_profile = get_voice_profile_by_id(voice_id)
    generated = synthesizer.generate_content(raw_text, voice_profile, source_title=topic, tier=tier)

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


@app.route("/api/voices", methods=["GET", "POST"])
def handle_voices():
    if request.method == "POST":
        data = request.get_json() or {}
        if not data.get("id"):
            data["id"] = f"voice_{int(datetime.now().timestamp())}"
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
        except Exception:
            pass
        return jsonify(data)
    else:
        profiles = (db.get_voice_profiles() if db.is_connected else None) or get_default_voice_profiles()
        return jsonify(profiles)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    host = os.environ.get("HOST", "0.0.0.0")
    print(f"[*] Starting Media, Executive & Content Dashboard on http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
