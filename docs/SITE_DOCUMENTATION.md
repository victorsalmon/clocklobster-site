# Clock Lobster Site Documentation

## Overview

This is the complete documentation for the Clock Lobster WordPress custom theme and associated assets. Clock Lobster is a premium B2B landing site built to drive consultation bookings for business automation services.

**Tech Stack:**
- WordPress (custom theme, no page builder dependency)
- Semantic HTML5 + PHP templates
- Vanilla CSS with custom properties (design tokens)
- Vanilla JavaScript (modular, no frameworks)
- Fluent Forms (form builder)
- Redirection (URL management)
- WP Webhooks (Attio CRM integration)

**Repository:** `clocklobster-site`
**Theme Directory:** `clocklobster-theme/`
**Lead Magnets:** `lead-magnets/`

---

## Quick Start

1. Upload `clocklobster-theme/` to `/wp-content/themes/`
2. Activate the theme in WordPress Admin → Appearance → Themes
3. Install required plugins (see Plugin Setup below)
4. Create WordPress pages with matching slugs: `home`, `services`, `about`, `privacy`, `contact`, `book-consultation`
5. Assign page templates in Page Editor → Template dropdown
6. Configure menus in Appearance → Menus (Primary and Footer locations)
7. Set up forms, redirects, and webhooks per Plugin Setup

---

## File Structure

```
clocklobster-site/
├── clocklobster-theme/           # WordPress theme
│   ├── style.css                 # Theme header (WP requires this)
│   ├── index.php                 # Fallback template
│   ├── functions.php             # Enqueues, theme support, menus
│   ├── header.php                # Glassmorphism sticky nav
│   ├── footer.php                # Footer form + links + chat widget
│   ├── page-home.php             # Landing page template
│   ├── page-services.php         # Services detail
│   ├── page-about.php            # Philosophy + founder story
│   ├── page-privacy.php          # Data Sovereignty sales page
│   ├── page-contact.php          # Contact form + FAQ
│   ├── page-book-consultation.php # Calendar mockup redirect target
│   ├── css/
│   │   └── main.css              # All theme styles, animations, responsive
│   ├── js/
│   │   └── main.js               # Mobile nav, chat widget, scroll animations
│   └── template-parts/
│       └── chat-widget.php       # Floating chat bubble + modal
├── lead-magnets/
│   ├── time-reclamation-playbook.html   # Email-capture eBook
│   └── 10-hours-saved-time-audit.html   # Post-booking workbook
└── docs/                         # This documentation
```

---

## Page Templates

| Template File | Page Slug | Purpose |
|--------------|-----------|---------|
| `page-home.php` | `home` | Conversion landing page |
| `page-services.php` | `services` | Service tiers + pricing |
| `page-about.php` | `about` | Philosophy + founder narrative |
| `page-privacy.php` | `privacy` | Data Sovereignty sales page |
| `page-contact.php` | `contact` | Contact form + FAQ |
| `page-book-consultation.php` | `book-consultation` | Calendar booking mockup |

**To assign a template:** Edit the WordPress page → Page Attributes → Template → select the matching template name.

---

## Design System

See `DESIGN_SYSTEM.md` for complete design tokens.

**Quick Reference:**
- Background: `#121214`
- Surface: `#1e293b`
- CTA: `#e11d48`
- Header Font: Outfit (Google Fonts)
- Body Font: Inter (Google Fonts)
- Card Style: Glassmorphism (`backdrop-filter: blur(16px)`)
- Border Radius: 16px+

---

## Plugin Setup

See `PLUGIN_SETUP.md` for detailed installation and configuration.

**Required Plugins:**
1. Fluent Forms (free) — all contact and lead capture forms
2. Redirection by John Godley (free) — URL redirects + 404 tracking
3. WP Webhooks (Starter $149/yr) — WordPress → Attio CRM bridge

---

## CRM Integration (Attio)

See `ATTIO_INTEGRATION.md` for webhook payloads and field mappings.

**Summary:** WP Webhooks captures Fluent Forms submissions and sends formatted JSON to Attio's REST API. Fields map as: Name → Person, Email → Email, Company → Company, Message → Note.

---

## Chat Widget

See `CHAT_WIDGET_OPTIONS.md` for implementation paths.

**Current State:** Static CSS/JS mockup in `template-parts/chat-widget.php`. Pre-loaded with 5 mock responses. Replace with Chatbase embed or custom OpenAI Assistants API when ready.

---

## Lead Magnets

| Resource | File | Delivery Trigger |
|----------|------|-----------------|
| The Time Reclamation Playbook | `lead-magnets/time-reclamation-playbook.html` | Email capture form submission |
| The 10-Hours-Saved Time Audit | `lead-magnets/10-hours-saved-time-audit.html` | Consultation booking confirmation |

**To convert to PDF:** Open HTML in browser → Print → Save as PDF. Or use a command-line tool like `wkhtmltopdf` or `puppeteer`.

**Affiliate Link:** Replace placeholder Mailbutler link in Playbook Chapter 4 with your actual affiliate URL after signing up for their partner program.

---

## Making Changes

### Change Colors
Edit CSS custom properties in `clocklobster-theme/css/main.css` at the top of the file.

### Change Copy
Edit the relevant `page-*.php` template. All copy is inline HTML.

### Add a New Page
1. Create `page-{slug}.php` in theme root
2. Add `Template Name:` header comment
3. Include `get_header()` and `get_footer()`
4. Assign template in WordPress page editor

### Update Navigation
Configure in WordPress Admin → Appearance → Menus. Register locations: Primary, Footer.

---

## Support

For questions or modifications, reference this documentation and the specific `.md` files in `docs/`. All theme files are commented and follow WordPress coding standards.

**Version:** 1.0.0
**Last Updated:** 2026-04-25
