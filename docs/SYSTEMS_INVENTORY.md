# Clock Lobster — Systems Inventory & Operations Manual

This document tracks every service, account, credential, and resource used to run the Clock Lobster website and business operations.

**Last updated:** 2026-04-30

---

## 1. Domain & DNS

### Domain Registrar
- **Domain:** `clocklobster.com`
- **Registrar:** Likely Interserver (hosting provider) or Cloudflare
- **Nameservers:** Cloudflare (`adrian.ns.cloudflare.com`, etc.)

### DNS Provider: Cloudflare
**Records configured:**

| Type | Name | Value | Purpose |
|------|------|-------|---------|
| A | `clocklobster.com` | GitHub Pages IPs | Website hosting |
| A | `mail.clocklobster.com` | `66.45.229.61` | Interserver mail server |
| MX | `clocklobster.com` | `mail.clocklobster.com` (priority 10) | Email routing |
| CNAME | `www` | `victorsalmon.github.io` | WWW redirect |
| CNAME | `mbazxfk6p3asuo4j3qxifetf7letmrym._domainkey` | `*.dkim.amazonses.com` | SES DKIM |
| CNAME | `rdk32ezfpdbgs5htecffra7vhzymjxqw._domainkey` | `*.dkim.amazonses.com` | SES DKIM |
| CNAME | `t2skudcjizw4zilklkttcbjca25lxkml._domainkey` | `*.dkim.amazonses.com` | SES DKIM |
| TXT | `clocklobster.com` | `v=spf1 ...` | SPF records |

**Access:** https://dash.cloudflare.com

---

## 2. Website Hosting

### GitHub Pages
- **Repository:** `victorsalmon/clocklobster-site`
- **Branch:** `main`
- **Source:** Root directory
- **Custom domain:** `clocklobster.com`
- **HTTPS:** Enforced
- **Build:** Automatic on push to `main`

**Local files:** `C:\Users\Victor\clocklobster-site\`

**Pages:**
| Page | File | URL |
|------|------|-----|
| Homepage | `index.html` | `https://clocklobster.com` |
| Services | `services.html` | `https://clocklobster.com/services.html` |
| About | `about.html` | `https://clocklobster.com/about.html` |
| Data Sovereignty | `privacy.html` | `https://clocklobster.com/privacy.html` |
| Contact | `contact.html` | `https://clocklobster.com/contact.html` |
| Book Consultation | `book-consultation.html` | `https://clocklobster.com/book-consultation.html` |

---

## 3. Backend (AWS)

### Account
- **AWS Account ID:** `916292310362`
- **Primary region:** `ca-west-1` (Lambda, API Gateway)
- **Secondary region:** `ca-central-1` (Secrets Manager, SES)

### Lambda Function
- **Name:** `clocklobster-form-handler`
- **Runtime:** Node.js 20.x
- **Region:** `ca-west-1`
- **Handler:** `index.handler`
- **Timeout:** 15 seconds
- **Memory:** 128 MB
- **Code:** `lambda/index.mjs` in repo

### API Gateway
- **Type:** HTTP API v2
- **API ID:** `o5vk8qguvg`
- **Region:** `ca-west-1`
- **Stage:** `$default`
- **Endpoint:** `https://o5vk8qguvg.execute-api.ca-west-1.amazonaws.com/submit`
- **CORS:** Restricted to `clocklobster.com`, `www.clocklobster.com`, `victorsalmon.github.io`
- **Rate limit:** 10 req/s, burst 20

### Secrets Manager
- **Secret name:** `ClockLobster/Site/Secrets`
- **Region:** `ca-central-1`
- **Keys:**
  - `ATTIO_WEB_FORM1_KEY` — Attio API key for form submissions

### IAM
- **Deploy user:** `lambda-install-user` (for deployments)
- **Lambda role:** `clocklobster-lambda-role`
  - Policies: `AWSLambdaBasicExecutionRole`, `SecretsManagerRead`, `SESendEmail`

### SES (Simple Email Service)
- **Region:** `ca-central-1`
- **Verified identity:** `clocklobster.com` (domain-level)
- **Status:** Production access removal requested (currently in sandbox)
- **From address:** `hello@clocklobster.com`
- **To address:** `hello@clocklobster.com`
- **DKIM:** 3 CNAME records configured in Cloudflare

**Monthly cost:** ~$0.40 (Secrets Manager)

---

## 4. CRM: Attio

- **Workspace:** Clock Lobster
- **API key location:** AWS Secrets Manager → `ClockLobster/Site/Secrets` → `ATTIO_WEB_FORM1_KEY`
- **Region:** Global (API endpoint: `https://api.attio.com/v2`)

**What Lambda creates on form submission:**
1. **Person** record (matched by email address)
2. **Company** record (if company name provided, matched by domain)
3. **Note** on the Person (source, company, budget, message)

**Objects used:**
- `people` (Person records)
- `companies` (Company records)
- `notes` (Notes attached to people)

---

## 5. Calendar Booking

### Google Calendar
- **Service:** Google Calendar Appointment Schedules
- **URL:** `https://calendar.app.google/K2DYAnxqBbokq4ry6`
- **Embedded on:** `book-consultation.html` (iframe)
- **Duration:** 30 minutes
- **Name:** "30-Minute Reclamation Consultation"

**Access:** Log in to `calendar.google.com` with your Google account.

---

## 6. Email

### Business Email
- **Address:** `hello@clocklobster.com`
- **Hosting:** Interserver (via `mail.clocklobster.com`)
- **Access:** Interserver control panel or webmail

### AWS SES
- **Purpose:** Form submission notifications
- **From:** `hello@clocklobster.com`
- **To:** `hello@clocklobster.com`
- **Current limit:** Sandbox mode (200 emails/day, verified recipients only)
- **Production request:** Submitted 2026-04-30, awaiting approval

---

## 7. Lead Magnets

### Current Assets (HTML)
| Asset | File | Status |
|-------|------|--------|
| Time Reclamation Playbook | `lead-magnets/time-reclamation-playbook.html` | HTML only |
| 10-Hours-Saved Time Audit | `lead-magnets/10-hours-saved-time-audit.html` | HTML only |

### Future Needs
- Convert both to PDF
- Host PDFs on website or in email automation
- Mailbutler affiliate link in Playbook Chapter 4 (currently placeholder)

---

## 8. Chat Widget

- **Current:** Static mockup (random pre-written responses)
- **Backend:** None (no AI connected)
- **Options considered:**
  - Chatbase (~$19–$399/mo)
  - Tawk.to (free)
  - Botpress (self-hosted)
  - Custom OpenAI Assistants API

**Decision:** Not yet made. Current mockup is acceptable for launch.

---

## 9. Analytics

- **Current:** None
- **Options:**
  - Plausible Analytics (~$9/mo, privacy-friendly)
  - Fathom Analytics (~$14/mo, privacy-friendly)
  - Google Analytics 4 (free, more invasive)

**Decision:** Not yet made.

---

## 10. Affiliate Programs

### Mailbutler
- **Status:** Not signed up
- **Purpose:** Email productivity tool recommendation in Playbook
- **Current:** Placeholder link in `lead-magnets/time-reclamation-playbook.html`
- **Action needed:** Sign up at `mailbutler.io/partners` (or equivalent)

---

## 11. Repository & Code

### GitHub
- **Repo:** `victorsalmon/clocklobster-site`
- **Branch:** `main`
- **Local path:** `C:\Users\Victor\clocklobster-site\`

### Important Files
| File | Purpose |
|------|---------|
| `index.html` | Homepage |
| `services.html` | Services & pricing |
| `about.html` | Founder story (Victor Salmon) |
| `privacy.html` | Data sovereignty |
| `contact.html` | Contact form + FAQ |
| `book-consultation.html` | Booking page (Google Calendar embed) |
| `css/main.css` | All styles |
| `js/main.js` | All scripts + form handler |
| `CNAME` | Custom domain config |
| `.nojekyll` | Disables Jekyll processing |
| `lambda/index.mjs` | Lambda form handler code |
| `lambda/deploy.ps1` | Deployment script |
| `lambda/iam-policy.json` | Minimal IAM policy |
| `images/victor-headshot.jpg` | Founder photo |
| `lead-magnets/*.html` | Lead magnet HTML files |
| `docs/*.md` | Documentation |
| `WP Theme/` | Preserved WordPress theme (not deployed) |

---

## 12. Monthly Costs Summary

| Service | Cost | Notes |
|---------|------|-------|
| GitHub Pages | $0 | Free for public repos |
| AWS Lambda | $0 | Free tier: 1M requests/mo |
| API Gateway | $0 | Free tier: 1M requests/mo |
| AWS SES | $0 | Sandbox (free), production ~$0.10/1000 emails |
| Secrets Manager | ~$0.40 | $0.40/secret/mo |
| Attio | $0 | Free tier |
| Cloudflare | $0 | Free plan |
| Google Calendar | $0 | Free |
| **Total** | **~$0.40/mo** | Increases to ~$1-5/mo with traffic |

---

## 13. Credentials & Access

### Where credentials are stored

| Service | Credential | Location |
|---------|-----------|----------|
| AWS | IAM user access key | Your personal notes (delete `lambda-install-user` when done) |
| AWS | SSO session | `~/.aws/config` (profile: `dev-account`) |
| Attio | API key | AWS Secrets Manager (`ClockLobster/Site/Secrets`) |
| Cloudflare | Login | Your personal account |
| GitHub | Login | Your personal account |
| Google | Calendar login | Your personal Google account |
| Interserver | Hosting login | Your personal account |

**Security notes:**
- No credentials are committed to Git
- `.gitignore` excludes all credential files
- Lambda reads Attio key from Secrets Manager, never hardcoded

---

## 14. Support & Contacts

| Service | Support URL | Notes |
|---------|-------------|-------|
| AWS | https://aws.amazon.com/support | IAM user needs `lambda:InvokeFunction` for testing |
| Attio | https://docs.attio.com | API docs for custom integrations |
| GitHub Pages | https://docs.github.com/pages | Custom domain troubleshooting |
| Cloudflare | https://support.cloudflare.com | DNS propagation issues |
| SES | https://docs.aws.amazon.com/ses | Sandbox removal, DKIM setup |

---

## 15. Pending Decisions

| # | Decision | Options | Status |
|---|----------|---------|--------|
| 1 | Chat widget backend | Chatbase, Tawk.to, Botpress, custom | ⏳ Open |
| 2 | Stock photos / illustrations | Unsplash, AI gen, illustrator | ⏳ Open |
| 3 | Lead magnet PDFs | Convert HTML → PDF | ⏳ Open |
| 4 | Mailbutler affiliate | Sign up for partner program | ⏳ Open |
| 5 | Analytics | Plausible, Fathom, GA4 | ⏳ Open |
| 6 | Terms of Service page | Create legal page | ⏳ Open |
| 7 | Blog / case studies | Future content | ⏳ Open |

---

*This document should be updated whenever a new service is added, credentials are rotated, or costs change significantly.*
