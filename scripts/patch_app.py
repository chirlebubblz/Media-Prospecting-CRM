"""
Fixes app.py:
1. Bulletproof loadAllData() with auto-retry and localStorage instant hydration.
2. Changes default active tab to 'exec' (People & Executives).
3. Adds visible initial loading indicator in the leads container.
4. Cleans up tab names and pipeline switching so People are front-and-center.
"""

import os
import re

app_path = os.path.join(os.path.dirname(__file__), "..", "app.py")
with open(app_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update activePipeline default
code = code.replace("let activePipeline = 'media';", "let activePipeline = 'exec';")

# 2. Update the pipeline switcher HTML to put People & Executives first
new_tabs = """    <div class="pipeline-switcher">
      <button class="pipeline-tab tab-exec active" id="tab-pipeline-exec" onclick="switchPipeline('exec')">
        <span>👥 People & Executives</span>
        <span class="tab-counter" id="badge-exec-count">0</span>
      </button>
      <button class="pipeline-tab tab-media" id="tab-pipeline-media" onclick="switchPipeline('media')">
        <span>🎙️ Podcasts & Media</span>
        <span class="tab-counter" id="badge-media-count">0</span>
      </button>
      <button class="pipeline-tab tab-content" id="tab-pipeline-content" onclick="switchPipeline('content')">
        <span>📝 Content Engine</span>
        <span class="tab-counter" id="badge-content-count">0</span>
      </button>
    </div>"""

code = re.sub(
    r'<div class="pipeline-switcher">.*?</div>\s*<!-- Cloud Status',
    new_tabs + '\n\n    <!-- Cloud Status',
    code,
    flags=re.DOTALL
)

# 3. Add visual initial loading indicator inside leads-cards-container
new_leads_container = """    <!-- Leads Display Container (Cards View) -->
    <div class="leads-grid" id="leads-cards-container">
      <div id="initial-loading-card" style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; color: var(--text-muted); background: var(--bg-surface); border-radius: 12px; border: 1px dashed var(--border);">
        <div style="font-size: 28px; animation: spin 1s linear infinite; display: inline-block; margin-bottom: 12px;">🔄</div>
        <div style="font-size: 16px; font-weight: 700; color: #f1f5f9;">Loading People & Executive Leads...</div>
        <div style="font-size: 12px; color: #94a3b8; margin-top: 4px;">Connecting to Neon cloud database...</div>
      </div>
    </div>"""

code = re.sub(
    r'<!-- Leads Display Container \(Cards View\) -->\s*<div class="leads-grid" id="leads-cards-container">.*?</div>',
    new_leads_container,
    code,
    flags=re.DOTALL
)

# 4. Replace loadAllData with bulletproof implementation
new_load_code = """    async function fetchJsonSafe(url, fallbackVal, retries = 3) {
      for (let i = 0; i < retries; i++) {
        try {
          const res = await fetch(url);
          if (res.ok) {
            const data = await res.json();
            return data;
          }
        } catch (err) {
          console.warn(`Fetch ${url} attempt ${i + 1} failed:`, err);
        }
        if (i < retries - 1) {
          await new Promise(r => setTimeout(r, 600 * (i + 1)));
        }
      }
      return fallbackVal;
    }

    // Load initial data from APIs with auto-retry & instant cache
    async function loadAllData() {
      // 1. Instant Cache Hydration: Render immediately from localStorage if available
      try {
        const cachedExec = localStorage.getItem('crm_exec_leads');
        const cachedMedia = localStorage.getItem('crm_media_leads');
        const cachedContent = localStorage.getItem('crm_content_items');
        if (cachedExec) {
          execLeads = JSON.parse(cachedExec);
          document.getElementById('badge-exec-count').innerText = execLeads.length;
        }
        if (cachedMedia) {
          mediaLeads = JSON.parse(cachedMedia);
          document.getElementById('badge-media-count').innerText = mediaLeads.length;
        }
        if (cachedContent) {
          contentItems = JSON.parse(cachedContent);
          document.getElementById('badge-content-count').innerText = contentItems.length;
        }
        if (execLeads.length > 0 || mediaLeads.length > 0) {
          updateTopActionButtons();
          updateFilterDropdowns();
          renderKPIs();
          renderQuickFilterPills();
          renderLeads();
        }
      } catch (e) {
        console.warn('Cache parse error:', e);
      }

      // 2. Fetch fresh data from APIs safely with auto-retry
      try {
        const [statusData, freshExec, freshMedia, freshContent, freshVoices] = await Promise.all([
          fetchJsonSafe('/api/status', { neon_connected: false }),
          fetchJsonSafe('/api/executives', []),
          fetchJsonSafe('/api/leads', []),
          fetchJsonSafe('/api/content', []),
          fetchJsonSafe('/api/voices', [])
        ]);

        neonConnected = Boolean(statusData && statusData.neon_connected);
        updateCloudStatusIndicator(neonConnected);

        if (Array.isArray(freshExec) && freshExec.length > 0) {
          execLeads = freshExec;
          localStorage.setItem('crm_exec_leads', JSON.stringify(execLeads));
        }
        if (Array.isArray(freshMedia) && freshMedia.length > 0) {
          mediaLeads = freshMedia;
          localStorage.setItem('crm_media_leads', JSON.stringify(mediaLeads));
        }
        if (Array.isArray(freshContent) && freshContent.length > 0) {
          contentItems = freshContent;
          localStorage.setItem('crm_content_items', JSON.stringify(contentItems));
        }
        if (Array.isArray(freshVoices)) {
          voiceProfiles = freshVoices;
        }

        document.getElementById('badge-exec-count').innerText = execLeads.length;
        document.getElementById('badge-media-count').innerText = mediaLeads.length;
        document.getElementById('badge-content-count').innerText = contentItems.length;

        updateTopActionButtons();
        updateFilterDropdowns();
        renderKPIs();
        renderQuickFilterPills();
        renderLeads();
      } catch (err) {
        console.error('Error loading CRM leads:', err);
        const container = document.getElementById('leads-cards-container');
        if (container && execLeads.length === 0 && mediaLeads.length === 0) {
          container.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 50px 20px; color: var(--text-muted); background: var(--bg-surface); border-radius: 12px; border: 1px dashed var(--border);">
              <div style="font-size: 24px; margin-bottom: 8px;">⚠️</div>
              <div style="font-size: 15px; font-weight: 700; color: #f1f5f9; margin-bottom: 6px;">Connecting to Cloud Database...</div>
              <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 16px;">The server or database is warming up. Please click below to load.</div>
              <button class="btn btn-primary" onclick="loadAllData()" style="padding: 8px 18px;">🔄 Retry Loading CRM</button>
            </div>
          `;
        }
      }
    }"""

code = re.sub(
    r'// Load initial data from APIs\s*async function loadAllData\(\) \{.*?\}\s*function updateCloudStatusIndicator',
    new_load_code + '\n\n    function updateCloudStatusIndicator',
    code,
    flags=re.DOTALL
)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(code)

print("[✓] Successfully patched app.py with bulletproof loadAllData and People-first pipeline!")
