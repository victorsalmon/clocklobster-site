# Clock Lobster — Site Architecture & Deployment Guide

## What This Is

A static marketing site deployed on **GitHub Pages** with a **serverless backend** on AWS for form handling and CRM integration.

**Live site:** `https://clocklobster.com`

---

## Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────┐
│  GitHub Pages   │────▶│  AWS Lambda      │────▶│   Attio     │
│  (Static HTML)  │     │  (Form Handler)  │     │   (CRM)     │
└─────────────────┘     └──────────────────┘     └─────────────┘
                               │
                               ▼
                        ┌──────────────────┐
                        │  AWS Secrets     │
                        │  (Attio API Key) │
                        └──────────────────┘
```

### Frontend
- **6 HTML pages** — `index.html`, `services.html`, `about.html`, `privacy.html`, `contact.html`, `book-consultation.html`
- **Vanilla CSS** — design tokens, glassmorphism, responsive breakpoints
- **Vanilla JS** — mobile nav, chat widget, scroll animations, form submission
- **Google Calendar embed** — live booking on `/book-consultation`
- **Hosted on:** GitHub Pages (root directory of `main` branch)

### Backend
- **AWS Lambda** (`clocklobster-form-handler`) — Node.js 20.x, `ca-west-1`
- **API Gateway v2** (HTTP API) — CORS-restricted to `clocklobster.com`
- **Rate limiting** — 10 req/s, burst 20
- **Secrets Manager** — `ClockLobster/Site/Secrets` → `ATTIO_WEB_FORM1_KEY`

### Data Flow (Form Submission)
```
User fills form on website
    → Browser POSTs to API Gateway
    → Lambda validates input
    → Lambda reads Attio API key from Secrets Manager
    → Attio: Upsert Person (by email)
    → Attio: Upsert Company (by domain)
    → Attio: Create Note on Person record
    → Browser shows success message
```

---

## File Structure

```
clocklobster-site/
├── index.html                    # Homepage
├── services.html                 # Services + pricing
├── about.html                    # Founder story + philosophy
├── privacy.html                  # Data sovereignty
├── contact.html                  # Contact form + FAQ
├── book-consultation.html        # Booking page (Google Calendar embed)
├── css/main.css                  # All styles
├── js/main.js                    # All scripts + form handler
├── images/                       # Photos and assets
│   └── victor-headshot.jpg
├── CNAME                         # GitHub Pages custom domain
├── .nojekyll                     # Disable Jekyll processing
├── lambda/                       # AWS Lambda backend
│   ├── index.mjs                 # Form handler code
│   ├── template.yaml             # SAM template (optional)
│   └── deploy.ps1                # AWS CLI deployment script
├── lead-magnets/                 # eBook + workbook HTML
├── docs/                         # Documentation
│   ├── SITE_ARCHITECTURE.md      # This file
│   ├── DESIGN_SYSTEM.md          # Colors, fonts, spacing
│   ├── ATTIO_INTEGRATION.md      # Attio API details
│   └── CHANGELOG.md              # Release notes
└── WP Theme/                     # WordPress theme (preserved, not deployed)
```

---

## Deployment

### Frontend (GitHub Pages)

Already automated. Push to `main` branch → GitHub Pages rebuilds.

1. Go to **GitHub repo → Settings → Pages**
2. Source: **Deploy from a branch** → `main` / `root`
3. Custom domain: `clocklobster.com`
4. Check "Enforce HTTPS" (after DNS is properly configured)

**DNS required:**
- A records for `clocklobster.com` → GitHub IPs (see GitHub docs)
- CNAME for `www.clocklobster.com` → `victorsalmon.github.io`

### Backend (AWS Lambda)

See `lambda/deploy.ps1` for the full deployment script.

**Prerequisites:**
- AWS CLI configured with credentials (`aws configure`)
- PowerShell (Windows) or bash

**Deploy:**
```powershell
cd lambda
.\deploy.ps1
```

**After deploy:**
1. Copy the API URL output by the script
2. Paste it into `js/main.js` → `FORM_API_URL`
3. Commit and push

**To update the Lambda code:**
```powershell
cd lambda
# Edit index.mjs, then:
Compress-Archive -Path index.mjs -DestinationPath deployment.zip -Force
aws lambda update-function-code --function-name clocklobster-form-handler --zip-file fileb://deployment.zip --region ca-west-1
```

---

## Environment Variables (Lambda)

| Variable | Value | Source |
|----------|-------|--------|
| `SECRET_NAME` | `ClockLobster/Site/Secrets` | SAM template / deploy script |
| `SECRET_KEY` | `ATTIO_WEB_FORM1_KEY` | SAM template / deploy script |

These are set at deploy time and never committed to Git.

---

## Security

- **API key never in browser** — stored in AWS Secrets Manager, read by Lambda
- **CORS restricted** — API Gateway only accepts requests from `clocklobster.com`
- **Rate limiting** — 10 requests/second per IP
- **Input validation** — Lambda validates email format, required fields
- **No PII in logs** — Lambda logs errors but not full form content

---

## Form Sources Tracked

| Source | Page | Fields Sent |
|--------|------|-------------|
| `lead-magnet` | Homepage | Name, Email, Company |
| `contact` | Contact | Name, Email, Company, Message, Budget |
| `footer` | All pages (footer) | Name, Email, Message |

All create a Person + Note in Attio. Contact and footer forms redirect to `/book-consultation.html` on success.

---

## Costs

| Service | Tier | Estimated Monthly |
|---------|------|-------------------|
| GitHub Pages | Free | $0 |
| AWS Lambda | Free (1M invocations) | $0 |
| API Gateway | Free (1M requests) | $0 |
| Secrets Manager | $0.40/secret | ~$0.40 |
| Attio | Free tier | $0 |
| **Total** | | **~$0.40/mo** |

---

## Troubleshooting

### Forms show success but no data in Attio
- Check `FORM_API_URL` in `js/main.js` is set to the deployed API URL
- Check browser DevTools Network tab for CORS errors
- Check CloudWatch Logs for Lambda errors

### CORS errors in browser
- API Gateway CORS config allows `clocklobster.com`
- If testing locally, add `http://localhost:PORT` to CORS origins in API Gateway

### 500 errors from Lambda
- Check Secrets Manager secret exists at `ClockLobster/Site/Secrets`
- Check Attio API key is valid and has `record:create` + `record:update` scopes
- Check CloudWatch Logs: `/aws/lambda/clocklobster-form-handler`

### GitHub Pages 404
- Ensure `CNAME` file contains `clocklobster.com`
- Ensure DNS A records point to GitHub Pages IPs (not Cloudflare proxy)
- Wait 5–10 minutes for DNS propagation

---

*Last updated: 2026-04-29*
