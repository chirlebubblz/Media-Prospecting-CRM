# Ethics Insight Media Dashboard — Server & Team Deployment Guide

This guide details three ways to make the dashboard accessible to your entire team.

---

## Option 1: Local Network / VPN (Active Right Now)

The dashboard is now configured to listen on `0.0.0.0:5050`.

If your team members are on the **same office Wi-Fi, local network, or corporate VPN (NordVPN/Tailscale)**, they can open the dashboard directly in their web browser right now:

```
http://192.168.0.108:5050
```

*(Note: If Windows Defender Firewall blocks incoming connections on port 5050, allow Python through the firewall or run `netsh advfirewall firewall add rule name="Flask 5050" dir=in action=allow protocol=TCP localport=5050` in an Admin prompt).*

---

## Option 2: Instant Public HTTPS Link (Cloudflare Tunnel / ngrok)

If your team is remote and you want to share a live HTTPS link in 30 seconds without setting up a cloud server:

### A. Cloudflare Tunnel (Free, No Account Needed)
1. Download `cloudflared` from [cloudflare.com](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/).
2. Run in terminal:
   ```bash
   cloudflared tunnel --url http://localhost:5050
   ```
3. Cloudflare gives you an instant public HTTPS URL (e.g. `https://random-name.trycloudflare.com`) that your team can use from anywhere.

### B. Ngrok
```bash
ngrok http 5050
```

---

## Option 3: Permanent 24/7 Cloud Server Deployment (Recommended)

To run the dashboard 24/7 without keeping your personal computer running, choose one of these standard deployment options:

### A. Render / Railway / Heroku (Easiest Cloud Setup)
1. Push this directory to a private GitHub/GitLab repository.
2. Connect the repository to **Render** (render.com) or **Railway** (railway.app) as a **Web Service**.
3. Settings:
   - **Environment:** Python 3.11
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT` (or use the included `Procfile`)
4. Attach a persistent disk to `/app/data` so changes to `leads.json` persist permanently.

### B. Docker / Docker Compose (Any VPS: DigitalOcean, AWS, Hetzner, Linode)
The repository includes a ready-to-use `Dockerfile` and `docker-compose.yml`.

1. Clone or copy the `media_prospecting/` folder to your server.
2. Run:
   ```bash
   docker compose up -d --build
   ```
3. The dashboard will run automatically, restart on server reboot, and persist all lead changes in `./data/leads.json`.

---

## Environment Variables
| Variable | Default | Purpose |
| :--- | :--- | :--- |
| `PORT` | `5050` | Port for the web server |
| `HOST` | `0.0.0.0` | Network binding interface |
