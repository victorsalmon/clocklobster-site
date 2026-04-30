# Human Do Next — Action Items

These are the concrete steps you (the human) need to take to get the site fully live and polished. Check them off as you complete them.

---

## Phase 1: Verify Core Systems

- [ ] **Tawk.to dashboard setup**
  - Log in to https://dashboard.tawk.to
  - Go to **Administration → Chat Widget → Widget Visibility**
  - Ensure "Hide widget" is **OFF**
  - Check **Widget Appearance** → set colors to match dark theme (`#121214` background, `#f8fafc` text, `#e11d48` CTA)
  - Go to **Domains** and add `clocklobster.com` and `www.clocklobster.com` to the whitelist (if restricted)
  - Download the Tawk.to mobile app (iOS/Android) for on-the-go chat responses
  - If verification still fails after 30 minutes, try clicking "Re-verify" in the dashboard

- [ ] **Wait for AWS SES production access**
  - Watch for approval email from AWS (may take 24–48 hours)
  - Once approved, test the contact form on the live site to verify email delivery to `hello@clocklobster.com`

- [ ] **Test forms end-to-end**
  - Submit the lead magnet form on the homepage
  - Submit the contact form on `contact.html`
  - Submit the footer quick-contact form
  - Verify each creates/updates a Person in Attio CRM
  - Verify Notes are attached with correct source labels

---

## Phase 2: Content & Assets

- [ ] **Get Mailbutler affiliate link**
  - Sign up at https://www.mailbutler.io/partners
  - Replace placeholder in `lead-magnets/time-reclamation-playbook.html` Chapter 4

- [ ] **Source remaining images**
  - Find Unsplash images for hero background, services section, and about page
  - Or generate AI images (Midjourney/DALL-E) with prompt: *dark futuristic automation theme, deep charcoal and lobster red accents, glassmorphism UI elements*
  - Or commission an illustrator for a custom automation hero

- [ ] **Convert lead magnets to PDF**
  - Open `lead-magnets/time-reclamation-playbook.html` in browser → Print → Save as PDF
  - Open `lead-magnets/10-hours-saved-time-audit.html` in browser → Print → Save as PDF
  - Upload PDFs to email automation or file hosting for automated delivery

---

## Phase 3: Polish & Launch Prep

- [ ] **Review all copy**
  - Read through each of the 6 HTML pages and adjust tone/details to match your voice
  - Check for any remaining placeholder text or "lorem ipsum"

- [ ] **Mobile testing**
  - Browse every page on phone/tablet (iOS Safari + Android Chrome)
  - Test hamburger menu opens/closes
  - Test forms are usable on small screens
  - Verify Google Calendar embed is scrollable/zoomable on mobile

- [ ] **Add Open Graph meta tags**
  - Add `<meta property="og:title">`, `<meta property="og:description">`, `<meta property="og:image">` to each page `<head>`
  - Create a 1200x630 OG image (can reuse brand kit assets)

- [ ] **Add privacy-friendly analytics**
  - Options: Plausible.io, Fathom, or GA4
  - Add tracking script to all pages (preferably in `js/main.js` or just before `</body>`)

- [ ] **Test navigation**
  - Click every internal link on every page
  - Verify no 404s
  - Verify external links open in new tab where appropriate

- [ ] **SEO basics**
  - Ensure each page has a unique `<title>` and `<meta name="description">` (already present, but review)
  - Submit sitemap to Google Search Console (create `sitemap.xml` if needed)

---

## Phase 4: Future Enhancements

- [ ] **Blog / Insights page** — For SEO and thought leadership
- [ ] **Case Studies page** — When you have client success stories
- [ ] **FAQ page** — Expand from contact page teaser into full FAQ
- [ ] **Terms of Service** — Legal protection for service engagements
- [ ] **Newsletter signup** — Separate from lead magnet for ongoing nurture

---

*Last updated: 2026-04-29*
