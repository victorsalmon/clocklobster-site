# Human Do Next — Action Items

These are the concrete steps you (the human) need to take to get the site live and functional. Check them off as you complete them.

---

## Phase 1: WordPress Setup

- [ ] **Set up WordPress** locally (LocalWP, XAMPP, MAMP) or on staging server
- [ ] **Upload theme** — Copy `clocklobster-theme/` folder to `/wp-content/themes/`
- [ ] **Activate theme** — WordPress Admin → Appearance → Themes → Activate "Clock Lobster"
- [ ] **Create pages** with these exact slugs:
  - `home`
  - `services`
  - `about`
  - `privacy`
  - `contact`
  - `book-consultation`
- [ ] **Assign page templates** — Edit each page → Page Attributes → Template → select matching template
- [ ] **Set homepage** — Settings → Reading → "A static page" → select "Home" page
- [ ] **Configure menus** — Appearance → Menus → create Primary and Footer menus, assign to theme locations

---

## Phase 2: Plugins

- [ ] **Install Fluent Forms** — Plugins → Add New → search "Fluent Forms" → install free version
- [ ] **Install Redirection** — Plugins → Add New → search "Redirection" by John Godley
- [ ] **Install WP Webhooks** — Purchase from wp-webhooks.com → upload ZIP → activate → enter license
- [ ] **Build Form A: Lead Magnet** — Name, Email, Company → send email with Playbook PDF + Mailbutler link
- [ ] **Build Form B: Contact** — Name, Email, Company, Message, Budget Range → redirect to `/book-consultation/`
- [ ] **Build Form C: Footer Quick Contact** — simplified version of Contact form → redirect to `/book-consultation/`
- [ ] **Style forms for dark theme** — Fluent Forms → Settings → Custom CSS (make inputs match glassmorphism)

---

## Phase 3: Lead Magnets

- [ ] **Convert Playbook to PDF** — Open `lead-magnets/time-reclamation-playbook.html` in browser → Print → Save as PDF
- [ ] **Convert Audit to PDF** — Open `lead-magnets/10-hours-saved-time-audit.html` in browser → Print → Save as PDF
- [ ] **Upload PDFs** to WordPress Media Library or email automation tool
- [ ] **Sign up for Mailbutler affiliate program** — Get your unique referral link
- [ ] **Replace placeholder link** in Playbook HTML and any email templates with real affiliate URL

---

## Phase 4: CRM Integration

- [ ] **Get Attio API token** — Attio → Settings → Developers → API Keys → Generate
- [ ] **Configure WP Webhooks flow** — Follow steps in `docs/ATTIO_INTEGRATION.md`
- [ ] **Test form submission** → Verify Person record created in Attio
- [ ] **Test duplicate handling** → Submit same email twice → verify update, not duplicate
- [ ] **Test Note creation** → Verify message appears as note on Person record

---

## Phase 5: Content & Polish

- [ ] **Personalize founder narrative** — Edit `page-about.php` with your real story, or ask me to iterate
- [ ] **Add stock photos** — Find Unsplash images for hero, services, about sections; or commission illustrations
- [ ] **Review all copy** — Read through each page template and adjust tone/details to match your voice
- [ ] **Set up real email address** — Replace `hello@clocklobster.com` with your actual email everywhere
- [ ] **Configure SEO** — Install Yoast or Rank Math; set page titles and meta descriptions

---

## Phase 6: Launch Prep

- [ ] **Test on mobile** — Browse every page on phone/tablet
- [ ] **Test forms** — Submit each form, verify emails arrive, redirects work
- [ ] **Test chat widget** — Open/close, send messages, verify mock responses
- [ ] **Test navigation** — Click every link, verify no 404s
- [ ] **Set up backups** — Install UpdraftPlus, configure automatic backups
- [ ] **Set up security** — Install Wordfence, configure firewall
- [ ] **Set up caching** — Install LiteSpeed Cache or WP Super Cache
- [ ] **Configure Redirection** — Set up any URL redirects from old site (if applicable)
- [ ] **Go live** — Point domain to hosting, update WordPress URL settings

---

*Last updated: 2026-04-25*
