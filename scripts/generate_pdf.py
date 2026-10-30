import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Team Operating Guide - Media Prospecting CRM & Content Engine</title>
  <style>
    @page {
      size: A4;
      margin: 18mm 16mm 18mm 16mm;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      line-height: 1.55;
      font-size: 13px;
      margin: 0;
      padding: 0;
      background: #ffffff;
    }
    .header-banner {
      background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
      color: #ffffff;
      padding: 24px 28px;
      border-radius: 10px;
      margin-bottom: 24px;
      border: 1px solid #334155;
    }
    .header-title {
      font-size: 22px;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin: 0 0 4px 0;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .header-badge {
      background: #8b5cf6;
      color: #ffffff;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .header-sub {
      color: #94a3b8;
      font-size: 13px;
      margin: 0;
    }
    .meta-strip {
      display: flex;
      gap: 16px;
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      font-size: 11px;
      color: #cbd5e1;
    }
    .meta-strip strong {
      color: #38bdf8;
    }
    h2 {
      font-size: 16px;
      font-weight: 700;
      color: #0f172a;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 6px;
      margin-top: 26px;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    h3 {
      font-size: 13.5px;
      font-weight: 700;
      color: #1e293b;
      margin-top: 16px;
      margin-bottom: 6px;
    }
    p {
      margin: 0 0 10px 0;
    }
    ul, ol {
      margin: 0 0 12px 0;
      padding-left: 20px;
    }
    li {
      margin-bottom: 5px;
    }
    .alert-box {
      background: #f8fafc;
      border-left: 4px solid #3b82f6;
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      font-size: 12px;
      color: #334155;
      margin: 12px 0;
    }
    .alert-box strong {
      color: #1d4ed8;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 16px 0;
      font-size: 12px;
    }
    th, td {
      border: 1px solid #cbd5e1;
      padding: 8px 10px;
      text-align: left;
    }
    th {
      background: #f1f5f9;
      font-weight: 700;
      color: #334155;
    }
    tr:nth-child(even) {
      background: #f8fafc;
    }
    .pill {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
    }
    .pill-blue { background: #e0f2fe; color: #0369a1; }
    .pill-purple { background: #f3e8ff; color: #7e22ce; }
    .pill-emerald { background: #d1fae5; color: #047857; }
    .pill-amber { background: #fef3c7; color: #b45309; }
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin: 12px 0;
    }
    .card-box {
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 12px 14px;
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }
    .card-box-title {
      font-weight: 700;
      font-size: 13px;
      color: #0f172a;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .workflow-step {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
    }
    .step-num {
      background: #0f172a;
      color: #ffffff;
      font-size: 11px;
      font-weight: 800;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
    }
    .step-content {
      flex: 1;
    }
    .step-title {
      font-weight: 700;
      color: #0f172a;
      font-size: 12.5px;
    }
    .step-desc {
      color: #475569;
      font-size: 11.5px;
      margin-top: 2px;
    }
    .page-break {
      page-break-before: always;
    }
    .footer {
      margin-top: 24px;
      padding-top: 12px;
      border-top: 1px solid #e2e8f0;
      font-size: 10.5px;
      color: #94a3b8;
      display: flex;
      justify-content: space-between;
    }
  </style>
</head>
<body>

  <!-- Header Banner -->
  <div class="header-banner">
    <div class="header-title">
      <span>Media Prospecting CRM & Content Engine</span>
      <span class="header-badge">Team SOP</span>
    </div>
    <div class="header-sub">Executive Prospecting, Media Show Intelligence & AI Voice Synthesis Operations Manual</div>
    <div class="meta-strip">
      <div><strong>Live App:</strong> media-prospecting-crm.onrender.com</div>
      <div><strong>Cloud DB:</strong> Neon PostgreSQL (Auto-Synced)</div>
      <div><strong>Audience:</strong> Growth, Research & Content Team</div>
    </div>
  </div>

  <div class="alert-box">
    <strong>Shared Cloud Environment:</strong> All team updates to contacts, status changes, research documents, and generated articles sync directly to the central Neon database in real time.
  </div>

  <!-- Section 1 -->
  <h2>1. Platform Architecture & Direct Links</h2>
  <div class="grid-2">
    <div class="card-box">
      <div class="card-box-title">
        <span>🎙️ CRM Dashboard (Home)</span>
      </div>
      <p style="font-size: 11.5px; color: #475569; margin-bottom: 6px;"><strong>URL:</strong> <code>https://media-prospecting-crm.onrender.com/</code></p>
      <p style="font-size: 11.5px; color: #475569;">Houses the <strong>72 Executive Contacts</strong> and <strong>139 Podcast Shows</strong>. Used for live search, pipeline management, directory searches, notes, and Excel/TSV exports.</p>
    </div>
    <div class="card-box">
      <div class="card-box-title">
        <span>📝 Content Engine Studio</span>
      </div>
      <p style="font-size: 11.5px; color: #475569; margin-bottom: 6px;"><strong>URL:</strong> <code>https://media-prospecting-crm.onrender.com/content</code></p>
      <p style="font-size: 11.5px; color: #475569;">Ingests PDFs, web links, or CRM angles to extract verified research statistics and draft swipeable LinkedIn carousels, in-feed essays, and executive memos.</p>
    </div>
  </div>

  <!-- Section 2 -->
  <h2>2. CRM Dashboard Operations (Prospecting & Pipeline)</h2>
  
  <div class="workflow-step">
    <div class="step-num">1</div>
    <div class="step-content">
      <div class="step-title">Switching Pipelines & Display Views</div>
      <div class="step-desc">
        Click <strong>🎙️ Podcast & Media</strong> or <strong>💼 Executive & Dealmakers</strong> in the top switcher. Use <strong>🗂️ Cards View</strong> for quick-action links and contact buttons, or <strong>📋 Table View</strong> for high-density scanning.
      </div>
    </div>
  </div>

  <div class="workflow-step">
    <div class="step-num">2</div>
    <div class="step-content">
      <div class="step-title">Instant Global Search & Status Filters</div>
      <div class="step-desc">
        Type into the <code>#global-search-input</code> box to filter leads across names, companies, themes, hooks, or notes in 0ms. Use the Quick Filter pills (<em>Identified, Watch & Comment, Outreach Sent, Booked</em>) to isolate pipeline stages.
      </div>
    </div>
  </div>

  <div class="workflow-step">
    <div class="step-num">3</div>
    <div class="step-content">
      <div class="step-title">Discovering New Shows via Online Directories</div>
      <div class="step-desc">
        Click <strong>🌐 Search Online Directories</strong> in the top action bar. Select a niche preset (e.g., <em>Founder Blindspots, Operations & Systems, PE Diligence</em>) and choose YouTube, Podcasts, or Google News to run curated query strings in new tabs.
      </div>
    </div>
  </div>

  <div class="workflow-step">
    <div class="step-num">4</div>
    <div class="step-content">
      <div class="step-title">Updating Leads, Logging Outreach & Exporting</div>
      <div class="step-desc">
        Change status via the card dropdown, or click <strong>✏️ Edit</strong> to record verified contact emails, LinkedIn URLs, and engagement logs. Click <strong>📥 Export Excel</strong> for the master 3-tab workbook.
      </div>
    </div>
  </div>

  <!-- Page Break for Clean Printing -->
  <div class="page-break"></div>

  <!-- Section 3 -->
  <h2>3. Content Engine Operations (Research & Voice Synthesis)</h2>
  <p>Access via <code>/content</code> or by clicking <strong>📝 Content Engine</strong> in the top header.</p>

  <h3>Step-by-Step Content Synthesis Workflow</h3>

  <div class="workflow-step">
    <div class="step-num">1</div>
    <div class="step-content">
      <div class="step-title">Open the Synthesis Studio</div>
      <div class="step-desc">Click the purple <strong>✨ Synthesize New Content</strong> button in the top-right corner.</div>
    </div>
  </div>

  <div class="workflow-step">
    <div class="step-num">2</div>
    <div class="step-content">
      <div class="step-title">Select Reference Input Source</div>
      <div class="step-desc">Choose one of the 4 dedicated source options:</div>
      <table>
        <thead>
          <tr>
            <th>Source Method</th>
            <th>Input Type</th>
            <th>Primary Use Case</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>📄 Upload PDF</strong></td>
            <td>PDF Files</td>
            <td>Whitepapers, industry reports, academic papers, pitch decks, SEC filings.</td>
          </tr>
          <tr>
            <td><strong>🌐 Web URL</strong></td>
            <td>Live HTTP Links</td>
            <td>Substack articles, Bloomberg/Reuters features, blog posts, online studies.</td>
          </tr>
          <tr>
            <td><strong>✍️ Text / Markdown</strong></td>
            <td>Raw Text</td>
            <td>Interview transcripts, book highlights, draft notes, unformatted thoughts.</td>
          </tr>
          <tr>
            <td><strong>💼 CRM Lead Hook</strong></td>
            <td>Dropdown Selection</td>
            <td>Pick any of the 72 Executives or 139 Podcasts to tailor content to their angle.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="workflow-step">
    <div class="step-num">3</div>
    <div class="step-content">
      <div class="step-title">Select Author Voice Persona</div>
      <div class="step-desc">
        <ul>
          <li><strong>Forensic Risk Operator:</strong> High-stakes operational risk, forensic rigor, counterparty fragility, institutional blindspots.</li>
          <li><strong>Strategic Dealmaker:</strong> M&A execution, bolt-on acquisitions, PE diligence, value creation, commercial leverage.</li>
          <li><strong>+ Add Custom Voice:</strong> Set custom tone attributes and reference style examples.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="workflow-step">
    <div class="step-num">4</div>
    <div class="step-content">
      <div class="step-title">Select Output Formats & Generate</div>
      <div class="step-desc">
        Check <strong>Tier 1</strong> (LinkedIn Carousel Outline + Hook Post), <strong>Tier 2</strong> (In-Feed Thought Leadership Essay), and/or <strong>Tier 3</strong> (Executive Briefing Memo). Click <strong>⚡ Synthesize Content & Research</strong>.
      </div>
    </div>
  </div>

  <h2>4. Reviewing, Copying & Publishing Content</h2>
  <table>
    <thead>
      <tr>
        <th>Action</th>
        <th>Button</th>
        <th>What It Does</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Preview Slides</strong></td>
        <td><code>👁️ View / Copy Post</code></td>
        <td>Interactive slide viewer to preview swipeable carousel decks slide-by-slide.</td>
      </tr>
      <tr>
        <td><strong>Copy Slide Script</strong></td>
        <td><code>📋 Copy Slide Script</code></td>
        <td>Copies full slide deck copy with headlines and visual notes for Canva/Figma.</td>
      </tr>
      <tr>
        <td><strong>Copy LinkedIn Post</strong></td>
        <td><code>📋 Copy LinkedIn Post</code></td>
        <td>Copies formatted in-feed post ready for immediate publishing on LinkedIn.</td>
      </tr>
      <tr>
        <td><strong>Copy Briefing</strong></td>
        <td><code>📋 Copy Briefing</code></td>
        <td>Copies structured executive memorandum with key findings and analysis.</td>
      </tr>
      <tr>
        <td><strong>Inspect Citations</strong></td>
        <td><code>🔬 Dossier</code></td>
        <td>Opens verified data points, empirical facts, and direct links to original sources.</td>
      </tr>
    </tbody>
  </table>

  <!-- Section 5 -->
  <h2>5. Team Best Practices & Operational Rules</h2>
  <ul>
    <li><strong>Keep Notes Specific:</strong> When updating lead cards, log specific dates (e.g., <em>"Connected on LI 10/24 - replied regarding M&A diligence"</em>).</li>
    <li><strong>Ground Content in Empirical Facts:</strong> Always verify that generated articles reference the underlying data points in the <strong>🔬 Dossier</strong> before publishing.</li>
    <li><strong>Export Backups:</strong> Team leads should download the master Excel workbook once a week via <strong>📥 Export Excel</strong> for offline records.</li>
  </ul>

  <div class="footer">
    <div>Media Prospecting CRM & Content Engine • Team Operating Guide</div>
    <div>Generated for Team Distribution • Cloud Synced with Neon DB</div>
  </div>

</body>
</html>
"""

html_path = r"e:\Antigrav projects\Ethics Insight\media_prospecting\docs\Team_Operating_Guide_SOP.html"
pdf_path = r"e:\Antigrav projects\Ethics Insight\media_prospecting\docs\Team_Operating_Guide_SOP.pdf"
artifact_pdf_path = r"C:\Users\jeraf\.gemini\antigravity\brain\5caf9297-78ab-4ec1-80fa-3080450f3de7\Team_Operating_Guide_SOP.pdf"
workspace_pdf_path = r"e:\Antigrav projects\Ethics Insight\Team_Operating_Guide_SOP.pdf"

os.makedirs(os.path.dirname(html_path), exist_ok=True)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[+] Wrote HTML template: {html_path}")

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_exe):
    chrome_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

cmd = [
    chrome_exe,
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={pdf_path}",
    "--no-pdf-header-footer",
    html_path
]

print(f"[+] Running headless browser print to PDF...")
subprocess.run(cmd, check=True)

if os.path.exists(pdf_path):
    print(f"[+] PDF generated successfully: {pdf_path} (Size: {os.path.getsize(pdf_path)} bytes)")
    import shutil
    shutil.copyfile(pdf_path, artifact_pdf_path)
    shutil.copyfile(pdf_path, workspace_pdf_path)
    print(f"[+] Copied to artifact: {artifact_pdf_path}")
    print(f"[+] Copied to workspace: {workspace_pdf_path}")
else:
    print("[!] PDF generation failed")
