# Changelog

All notable changes to the Clock Lobster site will be documented in this file.

## [1.0.0] - 2026-04-25

### Added
- Initial WordPress custom theme with 6 page templates:
  - Homepage (conversion landing with automation hero animation)
  - Services (3 service tiers + pricing philosophy)
  - About (founder narrative + philosophy)
  - Data Sovereignty (10-card security stack sales page)
  - Contact (form + FAQ)
  - Book Consultation (calendar mockup)
- Glassmorphism design system with CSS custom properties
- Responsive grid system (mobile-first)
- Automation hero animation (CSS keyframes with flowing particles)
- Static chat widget mockup with 5 pre-loaded responses
- Mobile navigation with hamburger toggle
- Scroll-triggered fade-in animations via IntersectionObserver
- Lead magnet content:
  - "The Time Reclamation Playbook" (email-capture eBook with Mailbutler affiliate)
  - "The 10-Hours-Saved Time Audit" (post-booking workbook)
- Complete documentation suite:
  - Site Documentation
  - Theme Structure
  - Design System
  - Plugin Setup
  - Attio CRM Integration
  - Chat Widget Options

### Technical
- WordPress theme header in `style.css`
- Google Fonts enqueue (Outfit + Inter)
- Theme support: title-tag, post-thumbnails, html5, responsive-embeds
- Registered nav menus: Primary, Footer
- Modular JS: mobile nav, chat widget, scroll animations
- CSS organized with design tokens (variables for colors, spacing, typography, effects)

### Notes
- Affiliate link for Mailbutler is a placeholder — replace with actual partner link after registration
- Chat widget is static mockup — replace with Chatbase or custom OpenAI when ready
- Fluent Forms placeholders indicate where form shortcodes should be inserted
- All page templates use `page-{slug}.php` naming for auto-detection
