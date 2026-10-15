
    let allLeads = [];
    let currentFilter = 'all';
    let currentEngine = 'podcast';
    let activeLead = null;

    async function loadLeads() {
      const res = await fetch('/api/leads');
      allLeads = await res.json();
      updateStats();
      renderLeads();
    }

    function setEngine(engine) {
      currentEngine = engine;
      const btnPod = document.getElementById('btn-engine-podcast');
      const btnYt = document.getElementById('btn-engine-youtube');
      if (engine === 'youtube') {
        btnPod.className = 'engine-btn';
        btnYt.className = 'engine-btn active-yt';
        document.getElementById('search-query').placeholder = 'Search YouTube video podcasts: e.g. compliance interview, risk management show...';
      } else {
        btnPod.className = 'engine-btn active';
        btnYt.className = 'engine-btn';
        document.getElementById('search-query').placeholder = 'Search keywords: e.g. productivity operations, founder risk, private equity due diligence...';
      }
    }

    function updateStats() {
      document.getElementById('stat-total').innerText = allLeads.length;
      const bookedCount = allLeads.filter(l => l.status === 'Booked').length;
      document.getElementById('stat-booked').innerText = bookedCount;
      const emailsCount = allLeads.filter(l => l.contact_email && l.contact_email !== 'None').length;
      document.getElementById('stat-emails').innerText = emailsCount;
      const ytCount = allLeads.filter(l => (l.media_type || '').includes('YouTube')).length;
      document.getElementById('stat-youtube').innerText = ytCount;
    }

    function setFilter(filter, el) {
      document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      el.classList.add('active');
      currentFilter = filter;
      renderLeads();
    }

    function renderLeads() {
      const container = document.getElementById('leads-container');
      container.innerHTML = '';

      let filtered = allLeads;
      if (currentFilter === 'has_email') {
        filtered = allLeads.filter(l => l.contact_email && l.contact_email !== 'None');
      } else if (currentFilter === 'podcast_only') {
        filtered = allLeads.filter(l => !(l.media_type || '').includes('YouTube') && !(l.media_type || '').includes('Publication'));
      } else if (currentFilter === 'youtube_only') {
        filtered = allLeads.filter(l => (l.media_type || '').includes('YouTube'));
      } else if (currentFilter !== 'all') {
        filtered = allLeads.filter(l => l.status === currentFilter);
      }

      document.getElementById('results-count').innerText = `Showing ${filtered.length} of ${allLeads.length} vetted media outlets`;

      filtered.forEach(lead => {
        const card = document.createElement('div');
        card.className = 'media-card';

        let badgeClass = 'badge-podcast';
        let badgeLabel = '🎙️ Podcast';
        if (lead.status === 'Booked') {
          badgeClass = 'badge-booked';
          badgeLabel = '✓ Booked on Show';
        } else if ((lead.media_type || '').includes('YouTube')) {
          badgeClass = 'badge-youtube';
          badgeLabel = '📺 YouTube Video';
        }

        const hostDisplay = lead.host || 'Host N/A';
        const producerDisplay = lead.producer ? ` • Producer: ${lead.producer}` : '';

        // Build Social / Platform Link Pills
        let linksHtml = '';
        if (lead.website) linksHtml += `<a href="${lead.website}" target="_blank" class="link-pill">🌐 Website</a>`;
        if (lead.linkedin_url) linksHtml += `<a href="${lead.linkedin_url}" target="_blank" class="link-pill pill-li">💼 LinkedIn</a>`;
        if (lead.apple_url) linksHtml += `<a href="${lead.apple_url}" target="_blank" class="link-pill">🍎 Apple</a>`;
        if (lead.spotify_url) linksHtml += `<a href="${lead.spotify_url}" target="_blank" class="link-pill pill-sp">🎧 Spotify</a>`;
        if (lead.youtube_url) linksHtml += `<a href="${lead.youtube_url}" target="_blank" class="link-pill pill-yt">📺 YouTube</a>`;
        if (lead.twitter_url) linksHtml += `<a href="${lead.twitter_url}" target="_blank" class="link-pill">🐦 X/Twitter</a>`;

        const summaryText = lead.summary || lead.description || 'Editorial summary not yet generated.';
        const angleHook = lead.rupert_angle || lead.pitch_angle || 'Custom narrative hook pending.';
        const talkingPoints = lead.talking_points || '';

        card.innerHTML = `
          <div>
            <!-- Top Badges & Status -->
            <div class="card-top">
              <div class="badges-wrapper">
                <span class="media-badge ${badgeClass}">${badgeLabel}</span>
                ${lead.genre ? `<span class="media-badge badge-metric">${escapeHtml(lead.genre)}</span>` : ''}
                ${lead.reach_metrics ? `<span class="media-badge badge-metric" style="color: #38bdf8;">${escapeHtml(lead.reach_metrics.split('•')[0])}</span>` : ''}
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

            <!-- Title & Host -->
            <div class="show-title">${escapeHtml(lead.name)}</div>
            <div class="host-producer-line">Host: <strong>${escapeHtml(hostDisplay)}</strong>${escapeHtml(producerDisplay)}</div>

            <!-- Links Toolbar -->
            <div class="links-toolbar">
              ${linksHtml || '<span style="font-size: 12px; color: var(--text-muted);">No external links found</span>'}
            </div>

            <!-- Contact Box -->
            <div class="email-box">
              <span class="email-text" title="${lead.contact_email || ''}">
                ${lead.contact_email ? '✉️ ' + lead.contact_email : '⚠️ No direct email in feed'}
              </span>
              <div style="display: flex; gap: 6px;">
                ${lead.contact_email ? `<button class="btn-xs" onclick="copyText('${lead.contact_email}')">Copy</button>` : ''}
                ${lead.website ? `<button class="btn-xs" onclick="deepScrapeLead('${lead.id}', '${lead.website}')" title="Scrape show website/masthead for email">🔍 Scrape Site</button>` : ''}
              </div>
            </div>

            <!-- Editorial Intelligence (Topic, Theme, Summary) -->
            <div class="editorial-section">
              ${lead.topic ? `
                <div class="section-field">
                  <div class="field-label">Core Topic & Theme</div>
                  <div class="field-content"><strong>${escapeHtml(lead.topic)}</strong> ${lead.theme ? '— ' + escapeHtml(lead.theme) : ''}</div>
                </div>
              ` : ''}
              <div class="section-field">
                <div class="field-label">Podcast Summary / What They're All About</div>
                <div class="field-content">${escapeHtml(summaryText.substring(0, 240))}${summaryText.length > 240 ? '...' : ''}</div>
              </div>
            </div>

            <!-- Highlighted Rupert Evill / Ethics Insight Strategic Angle Box -->
            <div class="rupert-angle-box">
              <div class="angle-header">
                <span>🎯 Strategic Angle for Rupert Evill / Ethics Insight</span>
              </div>
              <div class="angle-hook">"${escapeHtml(angleHook)}"</div>
              ${talkingPoints ? `<div class="talking-points-text">${escapeHtml(talkingPoints)}</div>` : ''}
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
      showToast('Crawling website & masthead for contact emails...');
      const res = await fetch('/api/leads/deep-scrape', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: leadId, website: websiteUrl })
      });
      const data = await res.json();
      if (data.email) {
        showToast(`Found contact email: ${data.email}!`);
        const item = allLeads.find(l => l.id === leadId);
        if (item) item.contact_email = data.email;
        updateStats();
        renderLeads();
      } else {
        showToast('No public email found on website pages.');
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

    function quickSearch(keyword) {
      document.getElementById('search-query').value = keyword;
      performSearch();
    }

    async function performSearch() {
      const q = document.getElementById('search-query').value.trim();
      if (!q) return;

      const endpoint = currentEngine === 'youtube' ? '/api/search/youtube' : '/api/search';
      showToast(`Searching ${currentEngine === 'youtube' ? 'YouTube' : 'podcasts'} for "${q}"...`);

      const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: q, limit: 12, enrich: true })
      });
      const data = await res.json();
      allLeads = data;
      updateStats();
      renderLeads();
      showToast(`Search complete! Found new targets.`);
    }

    async function triggerAutoDiscovery() {
      showToast('Running multi-keyword auto-discovery across compliance & finance...');
      const res = await fetch('/api/search/presets', { method: 'POST' });
      const data = await res.json();
      allLeads = data;
      updateStats();
      renderLeads();
      showToast('Auto-discovery complete!');
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
        l.name,
        'Cold',
        'P1',
        'Group 1',
        l.status || 'Identified',
        'Ready to Pitch',
        l.rupert_angle || l.pitch_angle || '',
        `Host - ${l.name}`,
        'Send custom pitch',
        l.genre || 'Media Host',
        l.linkedin_url || ''
      ].join('\t');
      navigator.clipboard.writeText(row);
      showToast(`📋 Copied row for ${l.name}! Paste into your Google Sheet.`);
    }

    // Pitch Modal Logic
    function openPitchModal(leadId) {
      activeLead = allLeads.find(l => l.id === leadId);
      if (!activeLead) return;

      document.getElementById('modal-show-title').innerText = activeLead.name;
      document.getElementById('modal-host-name').innerText = `Host: ${activeLead.host || 'Production Team'}`;
      document.getElementById('modal-target-email').innerText = activeLead.contact_email || 'Not detected in feed (try "Scrape Site" button)';
      
      generatePitchText('custom_angle');
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
      const host = activeLead.host ? activeLead.host.split(' ')[0] : 'there';
      const showName = activeLead.name;
      const customHook = activeLead.rupert_angle || activeLead.pitch_angle || 'Why Smart Boards Audit the Wrong Signals';
      const talkingPoints = activeLead.talking_points || '• The 67% behavioral gap in corporate risk\n• Why checklist diligence fails\n• Reading human friction in operations';

      let text = '';
      let subject = '';

      if (type === 'custom_angle') {
        subject = `Guest Idea for ${showName}: ${customHook.split('—')[0].trim()}`;
        text = `Subject: ${subject}

` +
`Hi ${host},

` +
`Really enjoy your conversations on ${showName} regarding ${activeLead.topic || 'leadership and execution'}.

` +
`Given your focus on ${activeLead.theme || 'helping leaders navigate high-stakes execution'}, I wanted to propose a timely topic for an upcoming episode:

` +
`"${customHook}"

` +
`A few concrete, counter-intuitive takeaways we could unpack for your audience:
` +
`${talkingPoints}

` +
`By way of brief background: Rupert Evill leads Ethics Insight and writes The Integrity Gap, helping organizations operationalize behavioral risk intelligence and due diligence beyond check-the-box exercises.

` +
`Would this angle resonate with your listeners for an upcoming conversation?

` +
`Best regards,

` +
`Rupert Evill
` +
`Ethics Insight
` +
`https://ethicsinsight.com`;
      } else if (type === 'behavioral') {
        subject = `Guest Topic for ${showName}: Why Smart Boards Audit the Wrong Signals (The 67% Behavioral Gap)`;
        text = `Subject: ${subject}

` +
`Hi ${host},

` +
`Really enjoyed your coverage on ${showName}.

` +
`In corporate diligence, boards consistently fall into the "IBM Syndrome": commissioning 60-page checklists because they're auditable, while remaining blind to the qualitative behavioral friction that actually craters enterprise value.

` +
`Research reveals that standard due diligence catches only 33% of organizational risks—the remaining 67% stem from behavioral and implementation gaps.

` +
`I would love to explore a timely discussion on:
` +
`"The Quantitative Trap: Why Smart Boards Audit the Wrong Signals"

` +
`Key talking points we could unpack:
` +
`• Abraham Wald’s WWII Bomber Paradox applied to compliance: why boards only audit clean 'returning planes'.
` +
`• The 'Open Door' Myth: why policies mean nothing if no one crosses the threshold of executive doors.
` +
`• The Signal of Silence: why zero whistleblower reports across operations indicates fear, not integrity.

` +
`By way of background: Rupert Evill leads Ethics Insight and writes The Integrity Gap, helping organizations operationalize behavioral compliance.

` +
`Would this angle resonate with your listeners?

` +
`Warm regards,

` +
`Rupert Evill
` +
`Ethics Insight`;
      } else if (type === 'productivity') {
        subject = `Guest Idea for ${showName}: Fraud & Internal Friction as Silent Margin Killers`;
        text = `Subject: ${subject}

` +
`Hi ${host},

` +
`Following your discussions on ${showName} around operational efficiency, one critical topic that rarely gets addressed is how internal misconduct and shadow workflows secretly destroy productivity.

` +
`I’d love to propose an episode exploring:
` +
`"Fraud as an Operational Productivity Drain — Why Internal Leakage Destroys More Margins Than Supply Chains"

` +
`We could unpack:
` +
`• The hidden productivity cost of employees bypassing controls to 'get things done'.
` +
`• How middle managers unwittingly suppress operational risk signals.
` +
`• Turning behavioral telemetry into margin protection.

` +
`Let me know if this would be a fit for an upcoming conversation!

` +
`Best,

` +
`Rupert Evill
` +
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
  