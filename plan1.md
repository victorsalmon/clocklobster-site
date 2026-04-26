# Clock Lobster Site — Build Plan 1

## Executive Summary

Build a fully documented, custom WordPress theme from scratch. All pages will be functional WordPress templates using the specified plugin stack. The site will be built to easily wire into Attio CRM via webhooks.

---

## 1. WordPress Custom Theme Architecture

```
clocklobster-site/
├── clocklobster-theme/           # Custom WordPress theme
│   ├── style.css                 # Theme header + CSS variables
│   ├── index.php
│   ├── functions.php             # Enqueue scripts, theme support
│   ├── header.php                # Glassmorphism sticky nav
│   ├── footer.php                # Footer form + links
│   ├── page-home.php             # Homepage template
│   ├── page-services.php
│   ├── page-about.php
│   ├── page-privacy.php          # Data Sovereignty sales page
│   ├── page-contact.php
│   ├── page-book-consultation.php # Calendar mockup redirect target
│   ├── template-parts/
│   │   ├── section-hero.php
│   │   ├── section-cta.php
│   │   └── chat-widget.php
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   └── assets/
│       └── images/
├── docs/
│   └── SITE_DOCUMENTATION.md     # Full technical documentation
└── lead-magnets/
    └── time-reclamation-playbook.pdf
```

**Design System** (locked in):
- Background: `#121214`
- Surface: `#1e293b`
- CTA: `#e11d48`
- Header font: Outfit (Google Fonts)
- Body font: Inter (Google Fonts)
- Glassmorphism cards (`backdrop-filter: blur(10px)`, 16px+ border-radius)
- Smooth hover micro-animations

---

## 2. Page Structure (Confirmed)

| Page | File | Purpose |
|------|------|---------|
| **Homepage** | `page-home.php` | Conversion landing. Hero → Problem → Solution (3-col) → How It Works → Services Preview → Trust → Lead Magnet → Footer Form |
| **Services** | `page-services.php` | Digital Employees / Automation Machines / Simple Integrations + How We Work + Pricing Philosophy |
| **About** | `page-about.php` | Philosophy-focused: "We Liberate, Not Replace" + Mission + Commitment |
| **Data Sovereignty** | `page-privacy.php` | **Sales page**, not legal doc. Security stack cards + compliance positioning |
| **Contact** | `page-contact.php` | Form (Fluent Forms) → redirects to Book Consultation page |
| **Book Consultation** | `page-book-consultation.php` | Static calendar mockup + meeting details |

---

## 3. Lead Magnet & PDF Strategy

Two-tier lead capture system:

### Tier 1: Freemium Tool (Email Capture Only)
- **What**: Free email-drafting SaaS recommendation
- **Delivery**: Email auto-responder with affiliate link
- **Placement**: Secondary CTA on homepage, sidebar on blog (future)

### Tier 2: Consultation Booking (Higher Intent)
- **What**: "The Time Reclamation Playbook" (branded PDF)
- **Delivery**: Sent via email after booking a consultation call
- **Placement**: Primary CTA driver, footer form redirect flow

---

## 4. Email-Drafting SaaS Affiliate Research

| Tool | What It Does | Affiliate Program | Why It Fits |
|------|-------------|-------------------|-------------|
| **Mailbutler** | Smart email productivity for Gmail/Outlook | Yes — 20% recurring | Broad appeal, easy setup, works everywhere |
| **SaneBox** | AI email filtering and prioritization | Yes — up to $50/sale + recurring | Clear time-saving value prop |
| **Lavender** | AI email coaching for sales teams | Yes — partner program | B2B sales focus |
| **Shortwave** | AI-powered email client | Unclear | Modern, AI-native |

**Recommendation**: **Mailbutler** — easiest to explain ("smart email tools for Gmail/Outlook that save 3+ hours/week"), genuinely useful, simple setup.

---

## 5. Plugin Stack & Integration Strategy

### Required Plugins

| Plugin | Purpose | Cost |
|--------|---------|------|
| **Fluent Forms** | All forms (contact, lead magnet, footer) | Free version sufficient to start |
| **Redirection** (John Godley) | URL redirects, 404 tracking | Free |
| **WP Webhooks** | Bridge WordPress → Attio CRM | Starter $149/year |

### Attio CRM Integration Path

Since there is **no direct WordPress → Attio plugin**, the integration will work as follows:

**Option A: Fluent Forms Webhook → Attio**
- Fluent Forms Pro has a webhook action
- On form submission, POST data directly to Attio's REST API
- Maps fields: Name → Person, Email → Email, Company → Company, Message → Note

**Option B: WP Webhooks → Attio (Recommended)**
- WP Webhooks captures WordPress events (form submission)
- Formats payload and sends to Attio webhook/API endpoint
- More flexible for complex workflows, keeps data inside WordPress before sending

**Option C: Zapier/Make Bridge**
- Fluent Forms → Zapier/Make → Attio
- Easier setup but adds monthly cost and external dependency

**Recommendation**: Start with **Option B (WP Webhooks)** since you're already buying it. Most control, native Attio REST API support, pre-configured webhook payloads in documentation.

---

## 6. Chat Widget RAG Options

| Option | RAG | How It Works | Cost | Pros | Cons |
|--------|-----|-------------|------|------|------|
| **Chatbase** | Yes | Upload docs → train vector index → embed widget | ~$19-399/mo | No-code, brandable, analytics, human handoff | Monthly SaaS cost |
| **SiteGPT** | Yes | Scrape site + upload files → train bot → embed widget | ~$19-999/mo | Auto-syncs website content, WordPress plugin | Less mature than Chatbase |
| **Custom OpenAI Assistants API** | Yes | Upload docs to OpenAI → create Assistant → custom chat UI | Pay-per-use (~$0.20-0.40/1k tokens) | Full control, no SaaS lock-in, data goes directly to OpenAI | Requires custom UI dev, API integration |
| **Botpress** | Yes | Visual flow builder + Knowledge Base (vector search) | Free self-hosted or cloud | Open-source, highly customizable, can self-host | Steeper learning curve |
| **Tidio / Crisp + AI** | Limited | Traditional chat widget + AI knowledge base layer | $29-394/mo | Live chat + AI hybrid | Weaker RAG capabilities |

**Recommendation for Clock Lobster**: **Chatbase** (fastest deployment, 30-minute setup) **OR** **Custom OpenAI Assistants API** (full data sovereignty, no third-party SaaS). Decision pending.

---

## 7. Data Sovereignty Page — Security Stack

Based on OWASP Top 10 for LLMs 2025 and Microsoft AI Red Team practices:

1. **Containerized Isolation** — Dedicated runtime per client, zero commingling
2. **Sandboxed Execution** — Controlled AI boundaries
3. **Least Privilege by Design** — Minimal access, reviewed regularly
4. **Prompt Injection Hardening** — OWASP 2025 LLM01 mitigation (input validation, output sanitization, system prompt leakage prevention)
5. **Enterprise AI Search (Tavily)** — PII blocking, malicious source filtering, prompt injection resistance
6. **AI Red Teaming** — Adversarial testing before go-live (Microsoft PyRIT methodology)
7. **Encrypted Sovereign Cloud Backup** — Geo-compliant data residency
8. **Audit Logging & Observability** — Full transparency on every action
9. **Secure Plugin Architecture** — Validated, scoped, monitored integrations
10. **Content Safety Filtering** — Harmful/biased output interception

---

## 8. Documentation Plan

```
docs/
├── SITE_DOCUMENTATION.md
├── THEME_STRUCTURE.md
├── DESIGN_SYSTEM.md
├── PLUGIN_SETUP.md
├── ATTIO_INTEGRATION.md
├── CHAT_WIDGET_OPTIONS.md
└── CHANGELOG.md
```

Each file will include file locations, CSS variable references, how to edit colors/fonts/copy, plugin configuration steps, webhook payload examples for Attio, where to insert affiliate links, and how to swap chat widget providers.

---

## 9. Open Questions Before Build

1. **Email Affiliate Tool**: Proceed with **Mailbutler** as the recommended free email-drafting tool?
2. **Chat Widget**: **Chatbase** (fast, hosted) or **Custom OpenAI Assistants API** (sovereign, custom-built)?
3. **Founder Story**: Should I write a philosophy-focused founder narrative for the About page, or will you supply your own story later?
4. **Images**: Placeholder boxes with labels, or Unsplash stock photo URLs inserted directly?
5. **Services Pricing**: Mention price tiers/ranges on Services page, or keep it entirely consultation-driven?

---

*Plan created for Clock Lobster — Business Time Reclamation*
*Date: 2026-04-25*
