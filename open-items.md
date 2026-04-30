# Open Items — Decisions Pending

These are active decisions that need to be made before proceeding further. Check them off and update this file when resolved.

---

## 1. Chat Widget Implementation Path ✅ RESOLVED

**Decision:** Tawk.to free live chat
**Rationale:** Human agents avoid AI hallucation risk for a boutique trust-based business; free tier covers needs; mobile app available for on-the-go responses.
**Status:** Script deployed on all 6 pages. Verification in Tawk.to dashboard pending — see troubleshooting checklist in `human-do-next.md`.

---

## 2. Images & Visual Assets

**Options:**
- **Unsplash stock photos** — Insert real photography URLs directly into templates
- **CSS illustrations/gradients only** — Keep the current icon/emoji + gradient approach
- **AI-generated images** (e.g., Nano Banana, Midjourney, DALL-E) — Custom branded visuals
- **Hire illustrator** — Custom cartoon/illustrated style for the automation hero

**Current state:** Founder headshot added. Hero, services, and about sections still use CSS gradients and emoji icons.
**Decision needed:** What visual direction for remaining photography/illustration?

---

## 3. Founder Narrative Personalization ✅ RESOLVED

**Decision:** Personalized About page copy written with Victor Salmon as founder.
**Status:** Live on `about.html`. Origin story emphasizes growth, ambition, and hope — matching aspirational tone.

---

## 4. Mailbutler Affiliate Link

**Current state:** Placeholder link in `lead-magnets/time-reclamation-playbook.html` Chapter 4.
**Action needed:** Sign up for Mailbutler partner program and replace placeholder with real affiliate URL.

---

## 5. Attio CRM Webhook Activation ✅ RESOLVED

**Decision:** AWS Lambda + API Gateway instead of WP Webhooks
**Rationale:** Static site has no WordPress backend; serverless approach is zero-maintenance and costs ~$0.40/mo.
**Status:** Lambda deployed in `ca-west-1`. Form submissions upsert Person, create Note, and trigger SES email.

---

## 6. Fluent Forms Implementation ✅ RESOLVED

**Decision:** Static HTML forms with vanilla JS fetch to Lambda endpoint
**Rationale:** No WordPress means no Fluent Forms; static forms are simpler and fully styled in `css/main.css`.
**Status:** All forms (lead magnet, contact, footer) submitting to live API.

---

## 7. Calendar Backend for Booking Page ✅ RESOLVED

**Decision:** Google Calendar appointment scheduling
**Rationale:** Free, integrated with existing Google Workspace, embeddable via iframe.
**Status:** Live embed on `book-consultation.html` — URL: https://calendar.app.google/K2DYAnxqBbokq4ry6

---

## 8. Additional Pages

**Potential future pages:**
- Blog / Insights (for SEO and thought leadership)
- Case Studies / Testimonials (when you have client stories)
- Detailed service pages (one per service tier)
- FAQ page (expand from contact page teaser)
- Terms of Service (legal)

**Decision needed:** Which pages to add next?

---

*Last updated: 2026-04-29*
