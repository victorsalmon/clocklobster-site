# Theme Structure

## File Purposes

### Root Template Files

| File | Purpose |
|------|---------|
| `style.css` | WordPress theme header comment (required). Points to main stylesheet location. |
| `index.php` | Fallback template. Displays page content using `the_content()`. |
| `functions.php` | Theme setup: enqueues styles/scripts, registers menus, adds theme support. |
| `header.php` | Site header with glassmorphism sticky nav, logo, primary menu, CTA button, mobile toggle. |
| `footer.php` | Footer grid with brand info, nav menus, contact form placeholder, copyright, and chat widget include. |

### Page Templates

| File | Slug | Sections |
|------|------|----------|
| `page-home.php` | `home` | Hero with automation animation, Problem/Agitation stats, 3-col Solution, How It Works (3 steps), Services Preview (3 cards), Trust badges, Lead Magnet (email capture) |
| `page-services.php` | `services` | Hero, Service Tiers (Digital Employees / Automation Machines / Simple Integrations), How We Work (4 cards), Pricing Philosophy (3 tiers) |
| `page-about.php` | `about` | Hero, Founder Narrative, Philosophy (4 cards), Mission Statement, Commitment (3 cards) |
| `page-privacy.php` | `privacy` | Hero, Sovereignty Promise, Security Stack (10 cards), Compliance (3 cards), CTA |
| `page-contact.php` | `contact` | Hero, Contact Grid (info + form placeholder), FAQ Teaser (4 cards) |
| `page-book-consultation.php` | `book-consultation` | Hero, Booking Info (consultation details + next steps), Calendar Mockup, Contact fallback |

### Assets

| File | Purpose |
|------|---------|
| `css/main.css` | Complete stylesheet: CSS variables, reset, typography, layout, components, animations, chat widget, responsive breakpoints. |
| `js/main.js` | Mobile menu toggle, chat widget open/close, mock chat responses, IntersectionObserver scroll animations. |
| `template-parts/chat-widget.php` | Floating chat bubble + modal window with static mock conversation. |

## Template Hierarchy

WordPress looks for templates in this order for a page with slug `example`:
1. `page-example.php` (custom template — we use this)
2. `page-{id}.php`
3. `page.php`
4. `index.php`

We use `page-{slug}.php` naming so templates auto-match pages without manual assignment. However, you must still set the Template in the WordPress page editor for the template name to appear correctly.

## How Content Flows

```
User requests /services/
    ↓
WordPress finds page with slug "services"
    ↓
Loads page-services.php (or falls back to page.php)
    ↓
get_header() → header.php
    ↓
Page template renders sections
    ↓
get_footer() → footer.php (includes chat-widget.php)
    ↓
wp_footer() enqueues scripts
```

## Adding a New Page

1. Create `page-{slug}.php`
2. Add this at the top:
```php
<?php
/**
 * Template Name: Your Page Name
 *
 * @package Clock Lobster
 */
get_header();
?>
```
3. Build your sections with HTML + CSS utility classes
4. End with:
```php
<?php get_footer(); ?>
```
5. Create the page in WordPress with matching slug
6. Assign template in Page Editor → Template dropdown

## Template Parts

Template parts are reusable components. Currently we have:
- `chat-widget.php` — included in footer.php

To add more:
1. Create file in `template-parts/`
2. Include with `get_template_part('template-parts/filename')` (omit .php)

## Functions.php Reference

### `clocklobster_setup()`
- `add_theme_support('title-tag')` — auto-generates `<title>`
- `add_theme_support('post-thumbnails')` — enables featured images
- `add_theme_support('html5')` — semantic markup for forms, comments, etc.
- `register_nav_menus()` — registers Primary and Footer menu locations

### `clocklobster_scripts()`
- Enqueues Google Fonts (Outfit + Inter)
- Enqueues `css/main.css`
- Enqueues `js/main.js` (loaded in footer)

### Hooks
- `after_setup_theme` → `clocklobster_setup`
- `wp_enqueue_scripts` → `clocklobster_scripts`
- `use_default_gallery_style` → `__return_false` (keeps theme clean)

## Menu Locations

| Location | Slug | Used In |
|----------|------|---------|
| Primary | `primary` | header.php main navigation |
| Footer | `footer` | footer.php footer navigation |

Configure menus in WordPress: Appearance → Menus → Manage Locations
