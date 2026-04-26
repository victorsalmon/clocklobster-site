# AGENTS.md — Context for AI Assistants

## Project: Clock Lobster

This file tells any AI assistant (human or automated) what they need to know before working on this codebase.

---

## Always Read These First

Before making any changes, read these files in order:

1. **`to-do.md`** — Master task tracker. Know what's active, completed, and pending.
2. **`open-items.md`** — Open decisions that may block or guide your work.
3. **`human-do-next.md`** — What the human owner is working on. Don't duplicate their efforts.
4. **`docs/SITE_DOCUMENTATION.md`** — Full project overview, tech stack, quick start.
5. **`docs/THEME_STRUCTURE.md`** — How the WordPress theme is organized.
6. **`docs/DESIGN_SYSTEM.md`** — Design tokens (colors, fonts, spacing). All changes must respect these.

Then read any docs relevant to your specific task:
- **`docs/PLUGIN_SETUP.md`** — If working with forms, redirects, or webhooks
- **`docs/ATTIO_INTEGRATION.md`** — If working with CRM data flows
- **`docs/CHAT_WIDGET_OPTIONS.md`** — If working on the chat widget
- **`docs/CHANGELOG.md`** — To understand recent changes

---

## Project Basics

**What this is:** A premium B2B WordPress site for Clock Lobster, a boutique automation agency that builds "digital employees" (AI agents in containers) for small and medium businesses.

**Tech stack:**
- WordPress custom theme (PHP templates, no page builder)
- Vanilla CSS with custom properties (design tokens in `css/main.css`)
- Vanilla JavaScript (modular, no frameworks)
- Google Fonts: Outfit (headings) + Inter (body)

**Plugins used:**
- Fluent Forms — form builder
- Redirection by John Godley — URL redirects
- WP Webhooks — WordPress → Attio CRM bridge

---

## Design Rules

- **Background:** `#121214` (deep charcoal)
- **Surface:** `#1e293b` (slate)
- **CTA:** `#e11d48` (lobster red)
- **Text primary:** `#f8fafc` (off-white)
- **Text secondary:** `#94a3b8` (muted slate)
- **Card style:** Glassmorphism (`backdrop-filter: blur(16px)`, 16px+ radius)
- **Hover:** Micro-animations (transform/translateY, box-shadow transitions)
- **Mobile-first:** Base styles are mobile. Add complexity at 768px+ and 1024px+ breakpoints.

Never introduce new colors or fonts without updating `docs/DESIGN_SYSTEM.md` and `css/main.css`.

---

## Code Conventions

- **PHP:** WordPress coding standards. Use `esc_url()`, `esc_html()`, `esc_attr()` for output.
- **CSS:** Custom properties for all values. Utility classes for common patterns.
- **JS:** Vanilla JS, no jQuery. Modular IIFE pattern in `js/main.js`.
- **Templates:** `page-{slug}.php` naming. Always include `get_header()` and `get_footer()`.

---

## Content Philosophy

The copy should always feel:
- **Professional but warm** — not corporate, not casual
- **Human-centric** — automation elevates people; it doesn't replace them
- **Security-first** — data sovereignty is a core differentiator, not an afterthought
- **Transparent** — pricing ranges are public, processes are documented

When writing new copy, reference the tone in existing page templates (`page-home.php`, `page-about.php`, etc.).

---

## File Locations

```
clocklobster-site/
├── clocklobster-theme/      # WordPress theme
│   ├── css/main.css         # All styles
│   ├── js/main.js           # All scripts
│   ├── template-parts/      # Reusable components
│   ├── page-*.php           # Page templates
│   ├── header.php           # Site header + nav
│   ├── footer.php           # Site footer + chat widget
│   ├── functions.php        # Theme setup
│   └── style.css            # WP theme header
├── docs/                    # Documentation
├── lead-magnets/            # eBook + workbook HTML
├── to-do.md                 # Task tracker
├── open-items.md            # Pending decisions
├── human-do-next.md         # Human action items
└── AGENTS.md                # This file
```

---

## How to Make Changes

1. Read the relevant docs (see "Always Read These First" above).
2. Check `to-do.md` and `open-items.md` to understand context.
3. Make minimal, focused changes.
4. Update `docs/CHANGELOG.md` with what you changed.
5. Commit with a semantic message (`feat:`, `fix:`, `docs:`, `refactor:`).
6. Update `to-do.md` if tasks are completed or new ones are discovered.
7. Update `human-do-next.md` if the human needs to do something as a result.

---

## Contact & Ownership

- **Owner:** Victor / Clock Lobster
- **Site:** https://clocklobster.com (future)
- **Email:** hello@clocklobster.com (future)
- **Repository:** https://github.com/victorsalmon/clocklobster-site

---

*This file should be updated whenever project structure, conventions, or context change significantly.*
