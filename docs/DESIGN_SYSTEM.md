# Design System

## Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg` | `#121214` | Page background |
| `--surface` | `#1e293b` | Cards, panels, elevated surfaces |
| `--surface-light` | `#334155` | Hover states, secondary surfaces |
| `--cta` | `#e11d48` | Primary buttons, labels, accents |
| `--cta-hover` | `#be123c` | Button hover state |
| `--text-primary` | `#f8fafc` | Headings, primary text |
| `--text-secondary` | `#94a3b8` | Body text, descriptions |
| `--text-muted` | `#64748b` | Captions, labels, placeholders |
| `--border` | `rgba(255,255,255,0.08)` | Dividers, card borders |
| `--glass-bg` | `rgba(30,41,59,0.65)` | Glassmorphism backgrounds |
| `--glass-border` | `rgba(255,255,255,0.1)` | Glassmorphism borders |
| `--success` | `#22c55e` | Checkmarks, positive indicators |
| `--accent` | `#38bdf8` | Secondary accent, links, highlights |

## Typography

| Role | Font | Weights | Usage |
|------|------|---------|-------|
| Headings | Outfit | 400, 500, 600, 700, 800 | All H1–H6, buttons, nav |
| Body | Inter | 300, 400, 500, 600, 700 | Paragraphs, descriptions, labels |

**Scale:**
- H1: `clamp(2.25rem, 5vw, 3.75rem)`
- H2: `clamp(1.875rem, 4vw, 2.25rem)`
- H3: `clamp(1.5rem, 3vw, 1.875rem)`
- H4: `1.5rem`
- Body: `1rem` (16px base)
- Small: `0.9375rem`
- Caption: `0.875rem`

**Line Heights:**
- Headings: `1.1`
- Body: `1.6`
- Relaxed: `1.75`

## Spacing Scale

| Token | Value |
|-------|-------|
| `--space-1` | 0.25rem (4px) |
| `--space-2` | 0.5rem (8px) |
| `--space-3` | 0.75rem (12px) |
| `--space-4` | 1rem (16px) |
| `--space-6` | 1.5rem (24px) |
| `--space-8` | 2rem (32px) |
| `--space-10` | 2.5rem (40px) |
| `--space-12` | 3rem (48px) |
| `--space-16` | 4rem (64px) |
| `--space-20` | 5rem (80px) |
| `--space-24` | 6rem (96px) |
| `--space-32` | 8rem (128px) |

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 8px | Small buttons, tags |
| `--radius-md` | 12px | Buttons, inputs |
| `--radius-lg` | 16px | Cards, panels |
| `--radius-xl` | 24px | Large containers |
| `--radius-full` | 9999px | Pills, avatars |

## Shadows

| Token | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.3)` | Subtle elevation |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.3), 0 10px 20px rgba(0,0,0,0.2)` | Cards default |
| `--shadow-lg` | `0 10px 30px rgba(0,0,0,0.4)` | Hover states, modals |
| `--shadow-glow` | `0 0 40px rgba(225,29,72,0.15)` | CTA emphasis |

## Transitions

| Token | Value | Usage |
|-------|-------|-------|
| `--transition-fast` | 150ms ease | Color changes, link hovers |
| `--transition-base` | 300ms ease | Transform, box-shadow |
| `--transition-slow` | 500ms ease | Page transitions, reveals |

## Glassmorphism

```css
.glass-card {
    background: rgba(30, 41, 59, 0.65);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 2rem;
}
```

**Requirements for glassmorphism:**
- Element must have `position` (relative/absolute/fixed)
- Parent must have distinct background (not same color)
- `backdrop-filter` requires content behind the element

## Buttons

| Variant | Background | Border | Text | Shadow |
|---------|-----------|--------|------|--------|
| Primary | `#e11d48` | none | `#fff` | `0 4px 14px rgba(225,29,72,0.35)` |
| Secondary | transparent | `1.5px solid rgba(255,255,255,0.08)` | `#f8fafc` | none |

**Hover states:**
- Primary: darker red, translateY(-2px), stronger shadow
- Secondary: lighter border, subtle background fill

## Responsive Breakpoints

| Name | Width | Behavior |
|------|-------|----------|
| Mobile | < 480px | Single column, chat widget full-width |
| Tablet | 768px+ | 2-column grids, nav visible, hero side-by-side |
| Desktop | 1024px+ | 3-4 column grids, full layout |

**Mobile-first approach:** Base styles are mobile. Media queries add complexity at larger sizes.

## Animation: Hero Automation Flow

Located in `css/main.css` under `.automation-visual`.

**Components:**
- 3 nodes (person, system, output) connected by invisible flow
- 4 animated particles traveling between nodes
- Floating words that appear near input node
- Reports that appear near output node
- System node pulses with glow

**To modify:**
- Change emoji in `.flow-node` divs
- Adjust `animation-delay` on `.flow-particle` classes for timing
- Modify `@keyframes` for different movement paths

## Image Strategy

Currently using:
- CSS gradients for section backgrounds
- Emoji/icons for visual elements (no external image dependencies)
- Unsplash can be added for photography

**To add stock photos:**
1. Find image on Unsplash
2. Use format: `https://images.unsplash.com/photo-{ID}?w=800&auto=format&fit=crop`
3. Insert as `<img>` or background-image
4. Add `alt` text for accessibility

## Accessibility Notes

- All interactive elements have focus states (browser default or custom)
- `aria-label` and `aria-expanded` on toggles
- Semantic HTML: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`
- Heading hierarchy: single H1 per page, logical H2→H3 nesting
- Color contrast meets WCAG AA (light text on dark background)
- Mobile menu toggle is keyboard accessible

## Changing the Design

**To change colors:** Edit CSS variables at top of `css/main.css`. All components reference variables.

**To change fonts:** Update Google Fonts URL in `functions.php` and CSS `--font-header` / `--font-body` variables.

**To change spacing:** Modify `--space-*` variables. Components use these consistently.

**To change border radius:** Update `--radius-*` variables.
