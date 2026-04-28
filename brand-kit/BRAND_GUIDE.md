# Clock Lobster Brand Guide

## Brand Overview

**Clock Lobster** is a boutique automation agency that builds "digital employees" — AI agents running in containers — for small and medium businesses. The brand identity merges two symbols:

- **Clock** — representing time, precision, and the hours we reclaim for our clients
- **Lobster** — representing tenacity, adaptability, and the "open claw" reaching for more

The logo embodies this fusion: a lobster whose body **is** a clock face, with its claws serving as clock hands frozen at **10:10** — the universal symbol of a happy, symmetric time.

---

## Logo

### Logo Mark Description

The Clock Lobster icon is a cute, illustrated character that merges a lobster with a clock face:

1. **Body** — a filled circle in dark lobster red (#be123c) serving as the clock face and carapace
2. **Eyes** — two large expressive white eyes with black pupils near the top of the body, giving the character a friendly, approachable look
3. **Hour markers** — 12 small white dots arranged around the body edge
4. **Center hub** — a bright red circle with a dark inner dot where the claws originate
5. **Left claw (hour hand)** — a thick arm extending from center toward 10 o'clock, ending in a chunky two-lobed pincer (large ellipse + small thumb)
6. **Right claw (minute hand)** — mirrors the left claw toward 2 o'clock
7. **Antennae** — two curved strokes with round dot tips extending from above the eyes
8. **Tail fan** — a filled spread shape at the 6 o'clock position
9. **Walking legs** — three small round bumps on each side of the body

### Logo Variants

| File | Use Case |
|------|----------|
| `clock-lobster-icon.svg` | Primary icon — lobster red (#e11d48) on transparent. Default choice. |
| `clock-lobster-icon-white.svg` | White (#f8fafc) on transparent. For dark/colored backgrounds. |
| `clock-lobster-icon-dark.svg` | Charcoal (#121214) on transparent. For light backgrounds, print, watermarks. |
| `clock-lobster-horizontal.svg` | Icon + "Clock Lobster" text side by side. Website headers, email signatures. |
| `clock-lobster-stacked.svg` | Icon above "Clock Lobster" text. Hero sections, print, presentations. |
| `clock-lobster-social-avatar.svg` | Square-cropped icon, slightly bolder strokes. X, Facebook, Instagram, LinkedIn profiles. |
| `clock-lobster-favicon.svg` | Simplified 64x64 — just clock face + claw hands. Browser tab favicon. |

---

## Color Palette

### Primary Colors

| Name | Hex | RGB | Use |
|------|-----|-----|-----|
| **Lobster Red** | `#e11d48` | 225, 29, 72 | CTA buttons, logo, accents, links |
| **Deep Charcoal** | `#121214` | 18, 18, 20 | Page backgrounds |
| **Slate** | `#1e293b` | 30, 41, 59 | Card surfaces, secondary backgrounds |
| **Moonlight** | `#f8fafc` | 248, 250, 252 | Primary text, headings on dark backgrounds |
| **Mist** | `#94a3b8` | 148, 163, 184 | Secondary text, captions, muted elements |

### Accent Colors

| Name | Hex | Use |
|------|-----|-----|
| **Dark Lobster** | `#be123c` | Hover states, depth on red elements |
| **Rose Glow** | `#fb7185` | Gradients, highlights, error states |
| **Surface Light** | `#334155` | Borders, subtle dividers on dark backgrounds |

### Usage Rules

- **Lobster Red** is the only brand accent color. Do not introduce blue, green, or other hues.
- Use **Moonlight** for all primary text on dark backgrounds.
- Use **Mist** for supporting/caption text only.
- Dark background (`#121214`) is the default. Light backgrounds are the exception.

---

## Typography

### Headings

- **Font:** Outfit (Google Fonts)
- **Weight:** 700 (Bold)
- **Letter spacing:** -0.5px to -1px
- **Usage:** Page titles, section headings, the word "Clock" in logo lockups

### Body

- **Font:** Inter (Google Fonts)
- **Weight:** 400 (Regular), 500 (Medium for emphasis)
- **Letter spacing:** 0
- **Usage:** Body copy, form labels, captions

### In Logo Text

The word **"Clock"** appears in Lobster Red (`#e11d48`). The word **"Lobster"** appears in Moonlight (`#f8fafc`). Both use Outfit Bold.

---

## Logo Usage Rules

### Clear Space

Maintain a minimum clear space around the logo equal to the height of the center hub dot. Nothing — text, images, edges — should enter this zone.

### Minimum Size

- **Icon only:** 32x32px (for favicons and tiny UI elements)
- **Icon + text (horizontal):** 200px wide minimum
- **Icon + text (stacked):** 120px wide minimum

### Do

- Use the primary (red) icon on dark backgrounds
- Use the white icon on colored or photo backgrounds
- Use the dark icon on white/light backgrounds
- Maintain aspect ratio when scaling
- Export to PNG at 2x resolution for web use

### Don't

- Don't rotate the logo
- Don't add drop shadows or outer glows
- Don't stretch or distort the aspect ratio
- Don't place the red icon on a red background
- Don't recreate the logo in different colors
- Don't add outlines or strokes beyond the original design
- Don't use the favicon version at large sizes (it's simplified)

---

## Social Media Assets

All social templates are in `brand-kit/social/`:

| File | Dimensions | Platform |
|------|-----------|----------|
| `twitter-header.svg` | 1500x500 | X / Twitter header |
| `facebook-cover.svg` | 820x312 | Facebook Page cover |
| `instagram-post.svg` | 1080x1080 | Instagram post template |

### Profile Pictures

Use `logos/clock-lobster-social-avatar.svg` for all platform profile pictures. The bold strokes ensure readability at small circular crops.

### Converting for Upload

SVGs are provided for infinite scalability. To upload to social platforms, export to PNG:

- X/Twitter header: 1500x500px PNG
- Facebook cover: 820x312px PNG
- Instagram post: 1080x1080px PNG
- Profile pictures: 400x400px PNG

Use any vector editor (Figma, Illustrator, Inkscape) or browser print-to-PNG to convert.

---

## Brand Voice

The Clock Lobster brand voice is:

- **Professional but warm** — never corporate, never casual
- **Human-centric** — automation elevates people, it doesn't replace them
- **Security-first** — data sovereignty is a differentiator
- **Transparent** — pricing ranges are public, processes are documented

In social media copy:
- Lead with the value to the business owner, not the technology
- Use concrete numbers ("reclaim 10+ hours/week") over vague claims
- Maintain confidence without arrogance

---

## File Reference

```
brand-kit/
├── logos/
│   ├── clock-lobster-icon.svg              Primary (red on transparent)
│   ├── clock-lobster-icon-white.svg        White on transparent
│   ├── clock-lobster-icon-dark.svg         Dark on transparent
│   ├── clock-lobster-horizontal.svg        Icon + text (side by side)
│   ├── clock-lobster-stacked.svg           Icon + text (stacked)
│   ├── clock-lobster-social-avatar.svg     Square social profile
│   └── clock-lobster-favicon.svg           Simplified favicon
├── social/
│   ├── twitter-header.svg                  X header (1500x500)
│   ├── facebook-cover.svg                  FB cover (820x312)
│   └── instagram-post.svg                  IG post template (1080x1080)
├── BRAND_GUIDE.md                          This file
└── README.md                               Quick reference
```

---

*Last updated: 2026-04-27*
