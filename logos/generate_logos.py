#!/usr/bin/env python3
"""
Generate 5 Clock Lobster logo concepts as SVG files.
"""

import os

LOGOS_DIR = "logos"

# ──────────────────────────────────────────────────────────────────────────────
# 1. KAWAII
# ──────────────────────────────────────────────────────────────────────────────
KAWAII = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="kBody" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ff6b6b"/>
      <stop offset="100%" stop-color="#ee5253"/>
    </linearGradient>
    <linearGradient id="kClaw" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ff9ff3"/>
      <stop offset="100%" stop-color="#f368e0"/>
    </linearGradient>
  </defs>
  <!-- Soft background circle -->
  <circle cx="256" cy="256" r="240" fill="#fff5f7" stroke="#ffdde1" stroke-width="8"/>

  <!-- Cute little legs -->
  <ellipse cx="190" cy="310" rx="22" ry="10" fill="#ff6b6b" transform="rotate(-20 190 310)"/>
  <ellipse cx="322" cy="310" rx="22" ry="10" fill="#ff6b6b" transform="rotate(20 322 310)"/>
  <ellipse cx="180" cy="350" rx="22" ry="10" fill="#ff6b6b" transform="rotate(-35 180 350)"/>
  <ellipse cx="332" cy="350" rx="22" ry="10" fill="#ff6b6b" transform="rotate(35 332 350)"/>

  <!-- Left claw (big & rounded) -->
  <g transform="translate(-10,0)">
    <path d="M130 200 C90 160, 50 200, 70 250 C80 280, 120 270, 140 240 Z" fill="url(#kClaw)"/>
    <circle cx="85" cy="210" r="5" fill="#fff"/>
    <circle cx="105" cy="200" r="5" fill="#fff"/>
    <circle cx="95" cy="225" r="5" fill="#fff"/>
  </g>

  <!-- Right claw (big & rounded) -->
  <g transform="translate(10,0)">
    <path d="M382 200 C422 160, 462 200, 442 250 C432 280, 392 270, 372 240 Z" fill="url(#kClaw)"/>
    <circle cx="427" cy="210" r="5" fill="#fff"/>
    <circle cx="407" cy="200" r="5" fill="#fff"/>
    <circle cx="417" cy="225" r="5" fill="#fff"/>
  </g>

  <!-- Body -->
  <ellipse cx="256" cy="300" rx="90" ry="110" fill="url(#kBody)"/>

  <!-- Segments -->
  <path d="M175 270 Q256 290 337 270" stroke="#c0392b" stroke-width="4" fill="none" opacity="0.3"/>
  <path d="M170 310 Q256 330 342 310" stroke="#c0392b" stroke-width="4" fill="none" opacity="0.3"/>
  <path d="M185 350 Q256 370 327 350" stroke="#c0392b" stroke-width="4" fill="none" opacity="0.3"/>

  <!-- Face -->
  <circle cx="226" cy="260" r="14" fill="#2d3436"/>
  <circle cx="230" cy="256" r="5" fill="#fff"/>
  <circle cx="286" cy="260" r="14" fill="#2d3436"/>
  <circle cx="290" cy="256" r="5" fill="#fff"/>
  <ellipse cx="256" cy="285" rx="10" ry="6" fill="#ff6b6b" opacity="0.6"/>
  <path d="M240 295 Q256 310 272 295" stroke="#2d3436" stroke-width="4" fill="none" stroke-linecap="round"/>

  <!-- Blush -->
  <ellipse cx="200" cy="280" rx="15" ry="8" fill="#ff9ff3" opacity="0.5"/>
  <ellipse cx="312" cy="280" rx="15" ry="8" fill="#ff9ff3" opacity="0.5"/>

  <!-- Antennae -->
  <path d="M226 200 Q210 140 180 120" stroke="#ff6b6b" stroke-width="5" fill="none" stroke-linecap="round"/>
  <circle cx="180" cy="120" r="8" fill="#ff9ff3"/>
  <path d="M286 200 Q302 140 332 120" stroke="#ff6b6b" stroke-width="5" fill="none" stroke-linecap="round"/>
  <circle cx="332" cy="120" r="8" fill="#ff9ff3"/>

  <!-- Text -->
  <text x="256" y="460" text-anchor="middle" font-family="Arial, sans-serif" font-weight="bold" font-size="42" fill="#2d3436">Clock Lobster</text>
</svg>"""

# ──────────────────────────────────────────────────────────────────────────────
# 2. MINIMALIST
# ──────────────────────────────────────────────────────────────────────────────
MINIMALIST = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <clipPath id="mClip">
      <circle cx="256" cy="220" r="160"/>
    </clipPath>
  </defs>

  <!-- Outer thin ring -->
  <circle cx="256" cy="220" r="170" fill="none" stroke="#1e293b" stroke-width="2"/>

  <!-- Lobster mark — ultra simplified using a single stroke path -->
  <g clip-path="url(#mClip)">
    <!-- Body as a single teardrop -->
    <path d="M256 80 C200 80, 160 160, 160 240 C160 320, 200 380, 256 380 C312 380, 352 320, 352 240 C352 160, 312 80, 256 80 Z" fill="none" stroke="#1e293b" stroke-width="6"/>

    <!-- One clean line for each claw -->
    <path d="M180 180 C140 140, 100 180, 120 240" fill="none" stroke="#1e293b" stroke-width="6" stroke-linecap="round"/>
    <path d="M332 180 C372 140, 412 180, 392 240" fill="none" stroke="#1e293b" stroke-width="6" stroke-linecap="round"/>

    <!-- Tiny tick marks for segments -->
    <line x1="190" y1="260" x2="210" y2="260" stroke="#1e293b" stroke-width="4" stroke-linecap="round"/>
    <line x1="302" y1="260" x2="322" y2="260" stroke="#1e293b" stroke-width="4" stroke-linecap="round"/>
    <line x1="200" y1="300" x2="220" y2="300" stroke="#1e293b" stroke-width="4" stroke-linecap="round"/>
    <line x1="292" y1="300" x2="312" y2="300" stroke="#1e293b" stroke-width="4" stroke-linecap="round"/>

    <!-- Clock hands inside the body -->
    <line x1="256" y1="240" x2="256" y2="160" stroke="#1e293b" stroke-width="5" stroke-linecap="round"/>
    <line x1="256" y1="240" x2="300" y2="280" stroke="#1e293b" stroke-width="5" stroke-linecap="round"/>
    <circle cx="256" cy="240" r="6" fill="#1e293b"/>
  </g>

  <!-- Wordmark -->
  <text x="256" y="460" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-weight="300" font-size="40" fill="#1e293b" letter-spacing="6">CLOCK LOBSTER</text>
</svg>"""

# ──────────────────────────────────────────────────────────────────────────────
# 3. PROFESSIONAL
# ──────────────────────────────────────────────────────────────────────────────
PROFESSIONAL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="pBody" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#b91c1c"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>
    <linearGradient id="pGold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>

  <!-- Shield / badge background -->
  <path d="M256 40 L460 120 L460 260 C460 380 360 460 256 480 C152 460 52 380 52 260 L52 120 Z" fill="#0f172a"/>

  <!-- Gold border -->
  <path d="M256 55 L445 128 L445 260 C445 370 352 445 256 463 C160 445 67 370 67 260 L67 128 Z" fill="none" stroke="url(#pGold)" stroke-width="4"/>

  <!-- Lobster -->
  <!-- Tail -->
  <path d="M216 400 Q256 430 296 400 L286 370 Q256 390 226 370 Z" fill="url(#pBody)"/>
  <path d="M226 370 Q256 390 286 370 L276 340 Q256 360 236 340 Z" fill="url(#pBody)"/>

  <!-- Main body -->
  <ellipse cx="256" cy="280" rx="65" ry="85" fill="url(#pBody)"/>

  <!-- Claws -->
  <path d="M195 230 C160 190, 120 220, 135 270 C145 295, 175 285, 190 260 Z" fill="url(#pBody)"/>
  <path d="M317 230 C352 190, 392 220, 377 270 C367 295, 337 285, 322 260 Z" fill="url(#pBody)"/>

  <!-- Claw pincers highlight -->
  <path d="M140 240 L150 250 L145 260" fill="none" stroke="#fbbf24" stroke-width="2" stroke-linecap="round"/>
  <path d="M372 240 L362 250 L367 260" fill="none" stroke="#fbbf24" stroke-width="2" stroke-linecap="round"/>

  <!-- Antennae -->
  <path d="M236 200 Q220 140 200 110" fill="none" stroke="url(#pGold)" stroke-width="3" stroke-linecap="round"/>
  <path d="M276 200 Q292 140 312 110" fill="none" stroke="url(#pGold)" stroke-width="3" stroke-linecap="round"/>
  <circle cx="200" cy="110" r="4" fill="url(#pGold)"/>
  <circle cx="312" cy="110" r="4" fill="url(#pGold)"/>

  <!-- Clock face overlay -->
  <circle cx="256" cy="280" r="35" fill="#0f172a" stroke="url(#pGold)" stroke-width="3"/>
  <line x1="256" y1="280" x2="256" y2="255" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
  <line x1="256" y1="280" x2="275" y2="295" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
  <circle cx="256" cy="280" r="4" fill="#fbbf24"/>

  <!-- Small hour markers -->
  <circle cx="256" cy="250" r="2" fill="#fbbf24"/>
  <circle cx="256" cy="310" r="2" fill="#fbbf24"/>
  <circle cx="226" cy="280" r="2" fill="#fbbf24"/>
  <circle cx="286" cy="280" r="2" fill="#fbbf24"/>

  <!-- Wordmark -->
  <text x="256" y="440" text-anchor="middle" font-family="Georgia, serif" font-weight="bold" font-size="34" fill="#fbbf24" letter-spacing="2">CLOCK LOBSTER</text>
  <text x="256" y="455" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#94a3b8" letter-spacing="4">AUTOMATION AGENCY</text>
</svg>"""

# ──────────────────────────────────────────────────────────────────────────────
# 4. CRISP
# ──────────────────────────────────────────────────────────────────────────────
CRISP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <!-- High-contrast, sharp geometry -->

  <!-- Outer precise ring -->
  <circle cx="256" cy="230" r="185" fill="none" stroke="#000" stroke-width="6"/>
  <circle cx="256" cy="230" r="175" fill="none" stroke="#000" stroke-width="2"/>

  <!-- Lobster constructed from straight lines and sharp angles -->
  <!-- Tail -->
  <polygon points="256,400 230,360 282,360" fill="#000"/>
  <polygon points="230,360 210,320 302,320 282,360" fill="#000"/>

  <!-- Body -->
  <polygon points="210,320 190,240 210,160 256,140 302,160 322,240 302,320" fill="#000"/>

  <!-- Claws -->
  <polygon points="190,240 130,200 110,260 150,280" fill="#000"/>
  <polygon points="130,200 140,170 170,190" fill="#000"/>
  <polygon points="322,240 382,200 402,260 362,280" fill="#000"/>
  <polygon points="382,200 372,170 342,190" fill="#000"/>

  <!-- Segments (cut out using white lines) -->
  <line x1="200" y1="200" x2="312" y2="200" stroke="#fff" stroke-width="3"/>
  <line x1="195" y1="240" x2="317" y2="240" stroke="#fff" stroke-width="3"/>
  <line x1="205" y1="280" x2="307" y2="280" stroke="#fff" stroke-width="3"/>

  <!-- Antennae -->
  <polyline points="230,160 210,100 190,90" fill="none" stroke="#000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <polyline points="282,160 302,100 322,90" fill="none" stroke="#000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="190" cy="90" r="5" fill="#000"/>
  <circle cx="322" cy="90" r="5" fill="#000"/>

  <!-- Clock dial negative space -->
  <circle cx="256" cy="240" r="40" fill="#fff" stroke="#000" stroke-width="4"/>
  <line x1="256" y1="240" x2="256" y2="210" stroke="#000" stroke-width="4" stroke-linecap="round"/>
  <line x1="256" y1="240" x2="280" y2="260" stroke="#000" stroke-width="4" stroke-linecap="round"/>
  <circle cx="256" cy="240" r="5" fill="#000"/>

  <!-- Tick marks -->
  <line x1="256" y1="200" x2="256" y2="205" stroke="#000" stroke-width="3"/>
  <line x1="256" y1="280" x2="256" y2="275" stroke="#000" stroke-width="3"/>
  <line x1="216" y1="240" x2="221" y2="240" stroke="#000" stroke-width="3"/>
  <line x1="296" y1="240" x2="291" y2="240" stroke="#000" stroke-width="3"/>

  <!-- Wordmark -->
  <text x="256" y="470" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="44" fill="#000" letter-spacing="4">CLOCK LOBSTER</text>
</svg>"""

# ──────────────────────────────────────────────────────────────────────────────
# 5. MODERN
# ──────────────────────────────────────────────────────────────────────────────
MODERN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="moBody" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="moAccent" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="moDark" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <filter id="moShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.25"/>
    </filter>
  </defs>

  <!-- Dark, sleek card background -->
  <rect x="36" y="36" width="440" height="360" rx="32" fill="url(#moDark)" filter="url(#moShadow)"/>

  <!-- Subtle grid pattern -->
  <g stroke="#334155" stroke-width="1" opacity="0.4">
    <line x1="36" y1="116" x2="476" y2="116"/>
    <line x1="36" y1="196" x2="476" y2="196"/>
    <line x1="36" y1="276" x2="476" y2="276"/>
    <line x1="36" y1="356" x2="476" y2="356"/>
    <line x1="116" y1="36" x2="116" y2="396"/>
    <line x1="196" y1="36" x2="196" y2="396"/>
    <line x1="276" y1="36" x2="276" y2="396"/>
    <line x1="356" y1="36" x2="356" y2="396"/>
  </g>

  <!-- Lobster icon -->
  <g transform="translate(0, -10)">
    <!-- Tail -->
    <path d="M236 340 Q256 365 276 340 L268 315 Q256 330 244 315 Z" fill="url(#moBody)"/>
    <path d="M244 315 Q256 330 268 315 L260 290 Q256 305 252 290 Z" fill="url(#moBody)"/>

    <!-- Body -->
    <ellipse cx="256" cy="240" rx="70" ry="90" fill="url(#moBody)"/>

    <!-- Left claw -->
    <path d="M190 200 C150 160, 110 200, 125 250 C135 280, 165 270, 185 240 Z" fill="url(#moBody)"/>
    <path d="M130 210 L145 220 L135 235" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>

    <!-- Right claw -->
    <path d="M322 200 C362 160, 402 200, 387 250 C377 280, 347 270, 327 240 Z" fill="url(#moBody)"/>
    <path d="M382 210 L367 220 L377 235" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>

    <!-- Antennae with neon cyan tips -->
    <path d="M230 160 Q210 110 185 90" fill="none" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
    <circle cx="185" cy="90" r="6" fill="url(#moAccent)"/>
    <path d="M282 160 Q302 110 327 90" fill="none" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
    <circle cx="327" cy="90" r="6" fill="url(#moAccent)"/>

    <!-- Segments -->
    <path d="M190 210 Q256 230 322 210" stroke="#be123c" stroke-width="3" fill="none" opacity="0.6"/>
    <path d="M186 240 Q256 260 326 240" stroke="#be123c" stroke-width="3" fill="none" opacity="0.6"/>
    <path d="M192 270 Q256 290 320 270" stroke="#be123c" stroke-width="3" fill="none" opacity="0.6"/>

    <!-- Sleek clock overlay -->
    <circle cx="256" cy="240" r="38" fill="#0f172a" stroke="url(#moAccent)" stroke-width="3"/>
    <line x1="256" y1="240" x2="256" y2="215" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
    <line x1="256" y1="240" x2="275" y2="255" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
    <circle cx="256" cy="240" r="4" fill="#38bdf8"/>

    <!-- Minimal hour markers -->
    <line x1="256" y1="205" x2="256" y2="212" stroke="#38bdf8" stroke-width="2"/>
    <line x1="256" y1="275" x2="256" y2="268" stroke="#38bdf8" stroke-width="2"/>
    <line x1="221" y1="240" x2="228" y2="240" stroke="#38bdf8" stroke-width="2"/>
    <line x1="291" y1="240" x2="284" y2="240" stroke="#38bdf8" stroke-width="2"/>
  </g>

  <!-- Wordmark -->
  <text x="256" y="445" text-anchor="middle" font-family="'Segoe UI', Roboto, Arial, sans-serif" font-weight="700" font-size="36" fill="#f8fafc" letter-spacing="2">Clock Lobster</text>
  <text x="256" y="465" text-anchor="middle" font-family="'Segoe UI', Roboto, Arial, sans-serif" font-weight="400" font-size="12" fill="#94a3b8" letter-spacing="4">AUTOMATION AGENCY</text>
</svg>"""

# ──────────────────────────────────────────────────────────────────────────────

files = {
    "logo-kawaii.svg": KAWAII,
    "logo-minimalist.svg": MINIMALIST,
    "logo-professional.svg": PROFESSIONAL,
    "logo-crisp.svg": CRISP,
    "logo-modern.svg": MODERN,
}

for filename, content in files.items():
    path = os.path.join(LOGOS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {path}")

print("\nDone! All 5 logo concepts are in the 'logos' folder.")
