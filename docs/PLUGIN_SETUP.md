# Plugin Setup Guide

## Required Plugins

### 1. Fluent Forms
**Purpose:** All forms (contact, lead capture, footer consultation request)
**Cost:** Free version sufficient to start. Pro required for webhooks ($79/yr).

**Installation:**
1. WordPress Admin → Plugins → Add New
2. Search "Fluent Forms"
3. Install and activate "Fluent Forms – Fastest Form Builder"

**Forms to Create:**

#### Form A: Lead Magnet Download (Homepage + Lead Magnet Section)
- **Fields:** Name (text), Email (email, required), Company (text)
- **Actions after submit:**
  - Send email to user with PDF attachment (Time Reclamation Playbook)
  - Send email to user with Mailbutler affiliate link
  - Store entry in Fluent Forms entries
  - (Pro) Send webhook to email marketing platform or Attio

#### Form B: Contact Form (Contact Page)
- **Fields:** Name (text, required), Email (email, required), Company (text), Message (textarea, required), Budget Range (dropdown: Under $2k / $2k–$8k / $8k–$20k / $20k+ / Not sure yet)
- **Actions after submit:**
  - Send notification email to hello@clocklobster.com
  - Redirect to `/book-consultation/`
  - Store entry
  - (With WP Webhooks) Trigger webhook to Attio

#### Form C: Footer Quick Contact (Footer)
- **Fields:** Name, Email, Company, Message (simplified)
- **Actions after submit:**
  - Send notification email
  - Redirect to `/book-consultation/`
  - Store entry

**Styling:**
Fluent Forms will inherit your theme styles. You may need to adjust form field backgrounds to match dark theme:
- Go to Fluent Forms → Settings → Custom CSS
- Add custom styles to make inputs match glassmorphism theme (dark backgrounds, light text)

---

### 2. Redirection
**Purpose:** URL redirects, 404 error tracking, permalink monitoring
**Cost:** Free

**Installation:**
1. WordPress Admin → Plugins → Add New
2. Search "Redirection"
3. Install and activate "Redirection" by John Godley

**Recommended Configuration:**
1. Complete the setup wizard
2. Enable "Monitor permalink changes in WordPress posts and pages"
3. Enable "Keep a log of all redirects and 404 errors"
4. Set up redirect: `/old-page/` → `/new-page/` (if migrating from old site)

**Why we use it:**
- If you change page permalinks, Redirection auto-creates 301 redirects
- Tracks 404 errors so you can fix broken links
- No server configuration needed (no .htaccess editing)

---

### 3. WP Webhooks
**Purpose:** Bridge WordPress events → Attio CRM (and other services)
**Cost:** Starter $149/yr (1 site)

**Installation:**
1. Purchase from wp-webhooks.com
2. Download plugin ZIP
3. WordPress Admin → Plugins → Add New → Upload Plugin
4. Activate and enter license key

**Integration Setup for Attio:**

#### Step 1: Create a Flow
1. WP Webhooks → Automations → Add New
2. Name: "Contact Form → Attio"
3. Trigger: Select "WordPress" → "Form submitted" (requires Fluent Forms integration)

#### Step 2: Configure Trigger
- Select the specific Fluent Form ID (Form B: Contact Form)
- Map fields:
  - `first_name` → Person name
  - `email` → Email address
  - `company` → Company name
  - `message` → Note content
  - `budget_range` → Custom field

#### Step 3: Configure Action
- Action type: "Send webhook"
- URL: `https://api.attio.com/v2/objects/people/records`
- Method: POST
- Headers:
  - `Authorization: Bearer {YOUR_ATTIO_API_TOKEN}`
  - `Content-Type: application/json`
- Body: JSON payload (see ATTIO_INTEGRATION.md for exact format)

#### Step 4: Test
1. Submit test form entry
2. Check WP Webhooks logs for success/failure
3. Verify record appears in Attio

**Alternative without WP Webhooks:**
Fluent Forms Pro has a native webhook action. If you purchase Fluent Forms Pro ($79/yr), you can send webhooks directly without WP Webhooks. However, WP Webhooks offers more flexibility for complex flows, data mapping, and conditional logic.

---

## Recommended Additional Plugins

| Plugin | Purpose | Cost |
|--------|---------|------|
| **Yoast SEO** or **Rank Math** | SEO optimization | Free |
| **WP Super Cache** or **LiteSpeed Cache** | Page caching | Free |
| **Wordfence** | Security firewall | Free |
| **UpdraftPlus** | Backup | Free |

---

## Plugin Conflicts to Avoid

- **Page Builders:** Do NOT install Elementor, Divi, or Beaver Builder. This is a custom theme and page builders will conflict with template files.
- **Form Plugins:** Don't install WPForms, Gravity Forms, or Contact Form 7. Use Fluent Forms exclusively for consistency.
- **Redirection Plugins:** Only use Redirection by John Godley. Disable others.

---

## Updating Plugins

Always test plugin updates on a staging site first. Major updates to Fluent Forms or WP Webhooks could affect form behavior or webhook payloads.

**Safe update order:**
1. Backup site (UpdraftPlus)
2. Update on staging
3. Test all forms submit correctly
4. Test webhook flows
5. Update on production

---

## Support Resources

- **Fluent Forms:** fluentforms.com/docs
- **Redirection:** redirection.me/support
- **WP Webhooks:** wp-webhooks.com/docs
- **Attio API:** docs.attio.com
