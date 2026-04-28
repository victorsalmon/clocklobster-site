#!/usr/bin/env python3
"""
Generate 10 professional Clock Lobster logo concepts.
Business-appropriate: modern, sleek, professional.
"""

import os

OUT = "brand-kit/options3"

# ── 1. Geometric Shield Crest ────────────────────────────────────────────────
SHIELD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="s1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="s2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
  </defs>
  <!-- Shield background -->
  <path d="M256 40 L450 110 L450 260 C450 380 350 450 256 480 C162 450 62 380 62 260 L62 110 Z" fill="url(#s1)" stroke="#fbbf24" stroke-width="4"/>
  <!-- Inner border -->
  <path d="M256 58 L432 122 L432 260 C432 370 340 435 256 462 C172 435 80 370 80 260 L80 122 Z" fill="none" stroke="#fbbf24" stroke-width="2" opacity="0.6"/>
  
  <!-- Geometric lobster -->
  <!-- Tail segments -->
  <polygon points="256,380 236,350 276,350" fill="url(#s2)"/>
  <polygon points="236,350 222,320 290,320 276,350" fill="url(#s2)"/>
  
  <!-- Body / Clock -->
  <circle cx="256" cy="250" r="70" fill="#0f172a" stroke="#fbbf24" stroke-width="3"/>
  <circle cx="256" cy="250" r="60" fill="none" stroke="#334155" stroke-width="1"/>
  <!-- Clock markers -->
  <g fill="#fbbf24">
    <circle cx="256" cy="195" r="3"/><circle cx="256" cy="305" r="3"/>
    <circle cx="191" cy="250" r="3"/><circle cx="321" cy="250" r="3"/>
    <circle cx="211" cy="205" r="2"/><circle cx="301" cy="205" r="2"/>
    <circle cx="211" cy="295" r="2"/><circle cx="301" cy="295" r="2"/>
  </g>
  <!-- Hands -->
  <line x1="256" y1="250" x2="256" y2="210" stroke="#f8fafc" stroke-width="4" stroke-linecap="round"/>
  <line x1="256" y1="250" x2="285" y2="270" stroke="#e11d48" stroke-width="3" stroke-linecap="round"/>
  <circle cx="256" cy="250" r="5" fill="#fbbf24"/>
  
  <!-- Claws - angular geometric -->
  <polygon points="186,240 140,200 120,230 150,260" fill="url(#s2)"/>
  <polygon points="140,200 130,180 160,190" fill="url(#s2)"/>
  <polygon points="326,240 372,200 392,230 362,260" fill="url(#s2)"/>
  <polygon points="372,200 382,180 352,190" fill="url(#s2)"/>
  
  <!-- Antennae -->
  <line x1="240" y1="185" x2="220" y2="130" stroke="#94a3b8" stroke-width="2" stroke-linecap="round"/>
  <line x1="272" y1="185" x2="292" y2="130" stroke="#94a3b8" stroke-width="2" stroke-linecap="round"/>
  <circle cx="220" cy="130" r="3" fill="#fbbf24"/>
  <circle cx="292" cy="130" r="3" fill="#fbbf24"/>
  
  <!-- Wordmark inside shield -->
  <text x="256" y="435" text-anchor="middle" font-family="Georgia, serif" font-weight="bold" font-size="26" fill="#fbbf24" letter-spacing="3">CLOCK LOBSTER</text>
</svg>'''

# ── 2. Negative Space Circle ─────────────────────────────────────────────────
NEGATIVE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="n1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#121214"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <!-- Dark circle -->
  <circle cx="256" cy="240" r="200" fill="url(#n1)"/>
  
  <!-- Clock face (negative cut) -->
  <circle cx="256" cy="240" r="100" fill="#f8fafc"/>
  
  <!-- Clock markers in dark -->
  <g fill="#121214">
    <rect x="252" y="148" width="8" height="16" rx="2"/>
    <rect x="252" y="316" width="8" height="16" rx="2"/>
    <rect x="148" y="236" width="16" height="8" rx="2"/>
    <rect x="348" y="236" width="16" height="8" rx="2"/>
  </g>
  <!-- Hands -->
  <line x1="256" y1="240" x2="256" y2="180" stroke="#121214" stroke-width="6" stroke-linecap="round"/>
  <line x1="256" y1="240" x2="300" y2="275" stroke="#e11d48" stroke-width="5" stroke-linecap="round"/>
  <circle cx="256" cy="240" r="7" fill="#121214"/>
  
  <!-- Lobster claws cut out of dark circle -->
  <!-- Left claw shape (white) -->
  <path d="M156 240 C120 180, 80 200, 90 260 C100 300, 140 280, 160 260 Z" fill="#f8fafc"/>
  <path d="M90 260 L70 250 L85 230" fill="none" stroke="#121214" stroke-width="4" stroke-linecap="round"/>
  
  <!-- Right claw shape (white) -->
  <path d="M356 240 C392 180, 432 200, 422 260 C412 300, 372 280, 352 260 Z" fill="#f8fafc"/>
  <path d="M422 260 L442 250 L427 230" fill="none" stroke="#121214" stroke-width="4" stroke-linecap="round"/>
  
  <!-- Antennae as thin white arcs -->
  <path d="M220 160 Q200 100 170 80" fill="none" stroke="#f8fafc" stroke-width="4" stroke-linecap="round"/>
  <path d="M292 160 Q312 100 342 80" fill="none" stroke="#f8fafc" stroke-width="4" stroke-linecap="round"/>
  
  <!-- Outer ring -->
  <circle cx="256" cy="240" r="200" fill="none" stroke="#e11d48" stroke-width="6"/>
  <circle cx="256" cy="240" r="188" fill="none" stroke="#94a3b8" stroke-width="1" opacity="0.5"/>
  
  <text x="256" y="470" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-weight="300" font-size="32" fill="#1e293b" letter-spacing="8">CLOCK LOBSTER</text>
</svg>'''

# ── 3. Side Profile Emblem ───────────────────────────────────────────────────
SIDE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="sp1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
  </defs>
  <!-- Outer ring -->
  <circle cx="256" cy="230" r="210" fill="none" stroke="#0f172a" stroke-width="8"/>
  <circle cx="256" cy="230" r="198" fill="none" stroke="#e11d48" stroke-width="2" opacity="0.8"/>
  
  <!-- Side profile lobster facing right -->
  <!-- Tail curled under -->
  <path d="M140 340 Q120 300 150 280 Q180 260 200 300" fill="none" stroke="url(#sp1)" stroke-width="14" stroke-linecap="round"/>
  <path d="M155 325 Q140 290 165 275" fill="none" stroke="url(#sp1)" stroke-width="12" stroke-linecap="round"/>
  
  <!-- Body segments -->
  <ellipse cx="220" cy="240" rx="35" ry="50" fill="url(#sp1)" transform="rotate(-15 220 240)"/>
  <ellipse cx="260" cy="225" rx="40" ry="55" fill="url(#sp1)" transform="rotate(-10 260 225)"/>
  <ellipse cx="305" cy="215" rx="38" ry="50" fill="url(#sp1)" transform="rotate(-5 305 215)"/>
  
  <!-- Carapace / Clock face -->
  <circle cx="330" cy="205" r="45" fill="#f8fafc" stroke="#0f172a" stroke-width="4"/>
  <circle cx="330" cy="205" r="38" fill="none" stroke="#e2e8f0" stroke-width="1"/>
  <!-- Clock ticks -->
  <g fill="#0f172a">
    <rect x="326" y="163" width="8" height="4" rx="1"/>
    <rect x="326" y="243" width="8" height="4" rx="1"/>
    <rect x="288" y="201" width="4" height="8" rx="1"/>
    <rect x="368" y="201" width="4" height="8" rx="1"/>
  </g>
  <!-- Hands -->
  <line x1="330" y1="205" x2="330" y2="175" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
  <line x1="330" y1="205" x2="355" y2="220" stroke="#e11d48" stroke-width="3" stroke-linecap="round"/>
  <circle cx="330" cy="205" r="4" fill="#0f172a"/>
  
  <!-- Large claw (chela) -->
  <path d="M360 190 C420 150, 460 180, 440 230 C425 265, 385 250 370 220" fill="none" stroke="url(#sp1)" stroke-width="14" stroke-linecap="round"/>
  <path d="M440 230 C455 210, 445 190 430 200" fill="none" stroke="url(#sp1)" stroke-width="10" stroke-linecap="round"/>
  
  <!-- Small claw -->
  <path d="M345 235 C380 270, 400 260 390 230" fill="none" stroke="url(#sp1)" stroke-width="10" stroke-linecap="round"/>
  
  <!-- Antennae -->
  <path d="M300 170 Q280 120 250 100" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  <path d="M315 165 Q310 110 290 85" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  
  <!-- Legs -->
  <line x1="210" y1="280" x2="180" y2="310" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
  <line x1="235" y1="285" x2="210" y2="320" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
  <line x1="265" y1="280" x2="250" y2="315" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
  
  <text x="256" y="470" text-anchor="middle" font-family="Arial, sans-serif" font-weight="bold" font-size="30" fill="#0f172a" letter-spacing="3">CLOCK LOBSTER</text>
</svg>'''

# ── 4. Abstract Symmetrical Mark ────────────────────────────────────────────
ABSTRACT = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="a1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
  </defs>
  <!-- Clean white background with subtle centering grid -->
  <line x1="256" y1="40" x2="256" y2="472" stroke="#e2e8f0" stroke-width="1"/>
  <line x1="40" y1="256" x2="472" y2="256" stroke="#e2e8f0" stroke-width="1"/>
  
  <!-- Central circle / clock -->
  <circle cx="256" cy="256" r="90" fill="none" stroke="#0f172a" stroke-width="8"/>
  <circle cx="256" cy="256" r="78" fill="none" stroke="#e2e8f0" stroke-width="1"/>
  
  <!-- Clock hands forming an abstract X with the center -->
  <line x1="256" y1="256" x2="256" y2="186" stroke="#0f172a" stroke-width="8" stroke-linecap="round"/>
  <line x1="256" y1="256" x2="316" y2="296" stroke="#0f172a" stroke-width="6" stroke-linecap="round"/>
  <circle cx="256" cy="256" r="10" fill="#e11d48"/>
  
  <!-- Abstract claw shapes - symmetrical arcs -->
  <path d="M166 256 C120 180, 80 200, 100 280 C110 320, 150 290, 170 260" fill="none" stroke="url(#a1)" stroke-width="12" stroke-linecap="round"/>
  <path d="M100 280 L75 270 L90 245" fill="none" stroke="#0f172a" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  
  <path d="M346 256 C392 180, 432 200, 412 280 C402 320, 362 290, 342 260" fill="none" stroke="url(#a1)" stroke-width="12" stroke-linecap="round"/>
  <path d="M412 280 L437 270 L422 245" fill="none" stroke="#0f172a" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  
  <!-- Antennae as elegant curves -->
  <path d="M220 190 Q200 120 170 90" fill="none" stroke="#0f172a" stroke-width="5" stroke-linecap="round"/>
  <path d="M292 190 Q312 120 342 90" fill="none" stroke="#0f172a" stroke-width="5" stroke-linecap="round"/>
  <circle cx="170" cy="90" r="6" fill="url(#a1)"/>
  <circle cx="342" cy="90" r="6" fill="url(#a1)"/>
  
  <!-- Tail as three simple diamonds -->
  <polygon points="256,366 242,346 256,326 270,346" fill="#0f172a"/>
  <polygon points="256,392 242,372 256,352 270,372" fill="#0f172a" opacity="0.7"/>
  
  <text x="256" y="472" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-weight="300" font-size="28" fill="#0f172a" letter-spacing="10">CLOCK LOBSTER</text>
</svg>'''

# ── 5. Art Deco Badge ────────────────────────────────────────────────────────
ARTDECO = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="ad1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#312e81"/>
    </linearGradient>
    <linearGradient id="ad2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <!-- Art deco sunburst background -->
  <circle cx="256" cy="230" r="220" fill="url(#ad1)"/>
  <g stroke="#fbbf24" stroke-width="1" opacity="0.3">
    <line x1="256" y1="10" x2="256" y2="450"/>
    <line x1="36" y1="230" x2="476" y2="230"/>
    <line x1="100" y1="74" x2="412" y2="386"/>
    <line x1="412" y1="74" x2="100" y2="386"/>
    <line x1="74" y1="100" x2="386" y2="412"/>
    <line x1="386" y1="100" x2="74" y2="412"/>
  </g>
  
  <!-- Double circle frame -->
  <circle cx="256" cy="230" r="190" fill="none" stroke="url(#ad2)" stroke-width="4"/>
  <circle cx="256" cy="230" r="178" fill="none" stroke="url(#ad2)" stroke-width="1"/>
  
  <!-- Lobster - symmetrical geometric -->
  <!-- Body / clock -->
  <circle cx="256" cy="230" r="60" fill="#0f172a" stroke="url(#ad2)" stroke-width="3"/>
  <!-- Art deco clock markers -->
  <g fill="#fbbf24">
    <rect x="252" y="166" width="8" height="14"/><rect x="252" y="280" width="8" height="14"/>
    <rect x="190" y="226" width="14" height="8"/><rect x="308" y="226" width="14" height="8"/>
  </g>
  <line x1="256" y1="230" x2="256" y2="186" stroke="#f8fafc" stroke-width="4" stroke-linecap="round"/>
  <line x1="256" y1="230" x2="286" y2="250" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
  <circle cx="256" cy="230" r="5" fill="#fbbf24"/>
  
  <!-- Geometric claws -->
  <polygon points="196,210 140,170 120,200 160,240" fill="#0f172a" stroke="url(#ad2)" stroke-width="2"/>
  <polygon points="140,170 130,150 160,160" fill="#0f172a" stroke="url(#ad2)" stroke-width="2"/>
  <polygon points="316,210 372,170 392,200 352,240" fill="#0f172a" stroke="url(#ad2)" stroke-width="2"/>
  <polygon points="372,170 382,150 352,160" fill="#0f172a" stroke="url(#ad2)" stroke-width="2"/>
  
  <!-- Tail -->
  <polygon points="256,300 236,330 276,330" fill="#0f172a" stroke="url(#ad2)" stroke-width="2"/>
  <polygon points="236,330 226,360 286,360 276,330" fill="#0f172a" stroke="url(#ad2)" stroke-width="2"/>
  
  <!-- Antennae with diamond tips -->
  <line x1="236" y1="178" x2="216" y2="120" stroke="url(#ad2)" stroke-width="3" stroke-linecap="round"/>
  <polygon points="216,120 210,110 222,110" fill="url(#ad2)"/>
  <line x1="276" y1="178" x2="296" y2="120" stroke="url(#ad2)" stroke-width="3" stroke-linecap="round"/>
  <polygon points="296,120 290,110 302,110" fill="url(#ad2)"/>
  
  <text x="256" y="450" text-anchor="middle" font-family="Georgia, serif" font-weight="bold" font-size="28" fill="url(#ad2)" letter-spacing="4">CLOCK LOBSTER</text>
  <text x="256" y="468" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#94a3b8" letter-spacing="6">AUTOMATION AGENCY</text>
</svg>'''

# ── 6. Modern Gradient Icon ──────────────────────────────────────────────────
MODERN_GRAD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="mg1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="mg2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="mg3" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <filter id="mgShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <!-- Sleek card background -->
  <rect x="32" y="32" width="448" height="360" rx="40" fill="url(#mg1)" filter="url(#mgShadow)"/>
  
  <!-- Subtle grid -->
  <g stroke="#334155" stroke-width="1" opacity="0.3">
    <line x1="32" y1="112" x2="480" y2="112"/><line x1="32" y1="192" x2="480" y2="192"/>
    <line x1="32" y1="272" x2="480" y2="272"/><line x1="32" y1="352" x2="480" y2="352"/>
    <line x1="112" y1="32" x2="112" y2="392"/><line x1="192" y1="32" x2="192" y2="392"/>
    <line x1="272" y1="32" x2="272" y2="392"/><line x1="352" y1="32" x2="352" y2="392"/>
  </g>
  
  <!-- Lobster -->
  <g transform="translate(0,-10)">
    <!-- Tail -->
    <path d="M240 340 Q256 360 272 340 L264 318 Q256 332 248 318 Z" fill="url(#mg2)"/>
    <path d="M248 318 Q256 332 264 318 L256 296 Q256 310 256 296 Z" fill="url(#mg2)" opacity="0.8"/>
    
    <!-- Body -->
    <ellipse cx="256" cy="240" rx="65" ry="85" fill="url(#mg2)"/>
    
    <!-- Claws -->
    <path d="M195 200 C155 160, 115 200, 130 250 C140 280, 170 270, 185 240 Z" fill="url(#mg2)"/>
    <path d="M317 200 C357 160, 397 200, 382 250 C372 280, 342 270, 327 240 Z" fill="url(#mg2)"/>
    
    <!-- Segments -->
    <path d="M195 220 Q256 240 317 220" stroke="#9f1239" stroke-width="3" fill="none" opacity="0.5"/>
    <path d="M190 250 Q256 270 322 250" stroke="#9f1239" stroke-width="3" fill="none" opacity="0.5"/>
    <path d="M200 280 Q256 300 312 280" stroke="#9f1239" stroke-width="3" fill="none" opacity="0.5"/>
    
    <!-- Antennae -->
    <path d="M232 160 Q216 110 192 90" fill="none" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
    <circle cx="192" cy="90" r="5" fill="url(#mg3)"/>
    <path d="M280 160 Q296 110 320 90" fill="none" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
    <circle cx="320" cy="90" r="5" fill="url(#mg3)"/>
    
    <!-- Glowing clock overlay -->
    <circle cx="256" cy="240" r="42" fill="#0f172a" stroke="url(#mg3)" stroke-width="4"/>
    <line x1="256" y1="240" x2="256" y2="210" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
    <line x1="256" y1="240" x2="280" y2="258" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
    <circle cx="256" cy="240" r="5" fill="#38bdf8"/>
    <!-- Markers -->
    <line x1="256" y1="200" x2="256" y2="208" stroke="#38bdf8" stroke-width="2"/>
    <line x1="256" y1="280" x2="256" y2="272" stroke="#38bdf8" stroke-width="2"/>
    <line x1="216" y1="240" x2="224" y2="240" stroke="#38bdf8" stroke-width="2"/>
    <line x1="296" y1="240" x2="288" y2="240" stroke="#38bdf8" stroke-width="2"/>
  </g>
  
  <text x="256" y="440" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-weight="700" font-size="34" fill="#f8fafc" letter-spacing="2">Clock Lobster</text>
  <text x="256" y="462" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#94a3b8" letter-spacing="5">AUTOMATION AGENCY</text>
</svg>'''

# ── 7. Monogram Seal ─────────────────────────────────────────────────────────
MONOGRAM = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="m1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Outer seal rings -->
  <circle cx="256" cy="230" r="210" fill="none" stroke="#0f172a" stroke-width="3"/>
  <circle cx="256" cy="230" r="200" fill="none" stroke="#0f172a" stroke-width="1"/>
  <circle cx="256" cy="230" r="180" fill="none" stroke="#e11d48" stroke-width="2"/>
  
  <!-- C and L monogram forming clock/lobster -->
  <!-- C as outer circle with a gap -->
  <path d="M256 110 A120 120 0 1 0 256 350" fill="none" stroke="#0f172a" stroke-width="20" stroke-linecap="round"/>
  <!-- L as clock hand inside -->
  <line x1="256" y1="230" x2="256" y2="150" stroke="#0f172a" stroke-width="18" stroke-linecap="round"/>
  <line x1="256" y1="230" x2="316" y2="230" stroke="#0f172a" stroke-width="18" stroke-linecap="round"/>
  
  <!-- Lobster claw accents completing the C -->
  <path d="M150 180 C110 160, 90 200, 110 240 C120 260, 150 250, 160 230" fill="none" stroke="#e11d48" stroke-width="14" stroke-linecap="round"/>
  <path d="M362 180 C402 160, 422 200, 402 240 C392 260, 362 250, 352 230" fill="none" stroke="#e11d48" stroke-width="14" stroke-linecap="round"/>
  
  <!-- Center dot -->
  <circle cx="256" cy="230" r="12" fill="#e11d48"/>
  
  <!-- Decorative dots around seal -->
  <g fill="#0f172a">
    <circle cx="256" cy="30" r="4"/><circle cx="256" cy="430" r="4"/>
    <circle cx="46" cy="230" r="4"/><circle cx="466" cy="230" r="4"/>
    <circle cx="116" cy="90" r="3"/><circle cx="396" cy="90" r="3"/>
    <circle cx="116" cy="370" r="3"/><circle cx="396" cy="370" r="3"/>
  </g>
  
  <text x="256" y="470" text-anchor="middle" font-family="Georgia, serif" font-weight="bold" font-size="28" fill="#0f172a" letter-spacing="4">CLOCK LOBSTER</text>
  <text x="256" y="488" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="#64748b" letter-spacing="6">EST. 2026</text>
</svg>'''

# ── 8. Isometric Tech ────────────────────────────────────────────────────────
ISOMETRIC = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="i1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#9f1239"/>
    </linearGradient>
    <linearGradient id="i2" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>
  <!-- Dark tech background -->
  <rect x="20" y="20" width="472" height="380" rx="24" fill="#0f172a"/>
  <!-- Circuit lines -->
  <g stroke="#1e293b" stroke-width="2" fill="none">
    <path d="M20 100 H120 V60 H200"/><path d="M20 180 H80 V140 H160 V200 H240"/>
    <path d="M492 100 H400 V60 H320"/><path d="M492 180 H440 V140 H360 V200 H280"/>
    <path d="M20 300 H100 V340 H180"/><path d="M492 300 H420 V340 H340"/>
  </g>
  <g fill="#38bdf8">
    <circle cx="120" cy="100" r="4"/><circle cx="200" cy="60" r="4"/>
    <circle cx="80" cy="180" r="4"/><circle cx="160" cy="140" r="4"/>
    <circle cx="240" cy="200" r="4"/><circle cx="400" cy="100" r="4"/>
    <circle cx="320" cy="60" r="4"/><circle cx="440" cy="180" r="4"/>
    <circle cx="360" cy="140" r="4"/><circle cx="280" cy="200" r="4"/>
  </g>
  
  <!-- Isometric lobster -->
  <!-- Body as hexagonal prism -->
  <polygon points="256,140 316,170 316,250 256,280 196,250 196,170" fill="url(#i1)"/>
  <polygon points="196,170 256,140 256,200 196,230" fill="#be123c"/>
  <polygon points="256,140 316,170 316,230 256,200" fill="#9f1239"/>
  
  <!-- Clock face on front face -->
  <circle cx="256" cy="215" r="32" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <line x1="256" y1="215" x2="256" y2="192" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
  <line x1="256" y1="215" x2="272" y2="228" stroke="#94a3b8" stroke-width="2" stroke-linecap="round"/>
  <circle cx="256" cy="215" r="3" fill="#38bdf8"/>
  
  <!-- Left claw (isometric block) -->
  <polygon points="196,200 156,180 156,220 196,240" fill="url(#i1)"/>
  <polygon points="156,180 176,160 196,180 196,200 156,220 136,200" fill="#be123c"/>
  
  <!-- Right claw (isometric block) -->
  <polygon points="316,200 356,180 356,220 316,240" fill="url(#i1)"/>
  <polygon points="356,180 336,160 316,180 316,200 356,220 376,200" fill="#9f1239"/>
  
  <!-- Tail -->
  <polygon points="256,280 276,310 236,310" fill="url(#i1)"/>
  <polygon points="276,310 286,340 246,340 236,310" fill="#be123c"/>
  
  <!-- Antennae -->
  <line x1="236" y1="155" x2="216" y2="115" stroke="#94a3b8" stroke-width="2" stroke-linecap="round"/>
  <circle cx="216" cy="115" r="4" fill="#38bdf8"/>
  <line x1="276" y1="155" x2="296" y2="115" stroke="#94a3b8" stroke-width="2" stroke-linecap="round"/>
  <circle cx="296" cy="115" r="4" fill="#38bdf8"/>
  
  <text x="256" y="440" text-anchor="middle" font-family="'Courier New', monospace" font-weight="bold" font-size="30" fill="#0f172a" letter-spacing="4">CLOCK LOBSTER</text>
  <text x="256" y="460" text-anchor="middle" font-family="'Courier New', monospace" font-size="12" fill="#64748b" letter-spacing="3">DIGITAL EMPLOYEES</text>
</svg>'''

# ── 9. Luxe Line Art ─────────────────────────────────────────────────────────
LUXE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <!-- Elegant thin-line lobster with watch face -->
  
  <!-- Outer fine circle -->
  <circle cx="256" cy="230" r="200" fill="none" stroke="#d4d4d8" stroke-width="1"/>
  <circle cx="256" cy="230" r="185" fill="none" stroke="#0f172a" stroke-width="2"/>
  
  <!-- Lobster - single weight elegant lines -->
  <!-- Tail -->
  <path d="M256 380 Q236 350 246 330 Q256 310 266 330 Q276 350 256 380" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  <path d="M246 330 Q230 310 240 295 Q256 280 272 295 Q282 310 266 330" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  
  <!-- Body segments flowing into watch -->
  <path d="M240 295 Q220 260 230 220 Q240 180 256 160 Q272 180 282 220 Q292 260 272 295" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  
  <!-- Watch face / Carapace -->
  <circle cx="256" cy="210" r="55" fill="none" stroke="#0f172a" stroke-width="3"/>
  <circle cx="256" cy="210" r="48" fill="none" stroke="#d4d4d8" stroke-width="1"/>
  
  <!-- Watch markers -->
  <g fill="#0f172a">
    <rect x="252" y="158" width="8" height="4" rx="1"/><rect x="252" y="258" width="8" height="4" rx="1"/>
    <rect x="204" y="206" width="4" height="8" rx="1"/><rect x="304" y="206" width="4" height="8" rx="1"/>
  </g>
  <!-- Watch hands -->
  <line x1="256" y1="210" x2="256" y2="175" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  <line x1="256" y1="210" x2="280" y2="228" stroke="#e11d48" stroke-width="2" stroke-linecap="round"/>
  <circle cx="256" cy="210" r="4" fill="#e11d48"/>
  
  <!-- Crown -->
  <rect x="252" y="148" width="8" height="10" rx="2" fill="#0f172a"/>
  
  <!-- Elegant claws -->
  <path d="M200 200 C170 170, 140 190, 150 230 C155 250, 180 240, 195 220" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  <path d="M150 230 C140 220, 145 205 155 210" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
  
  <path d="M312 200 C342 170, 372 190, 362 230 C357 250, 332 240, 317 220" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  <path d="M362 230 C372 220, 367 205 357 210" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
  
  <!-- Antennae -->
  <path d="M240 160 Q220 110 200 90" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
  <path d="M272 160 Q292 110 312 90" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
  <circle cx="200" cy="90" r="4" fill="none" stroke="#0f172a" stroke-width="2"/>
  <circle cx="312" cy="90" r="4" fill="none" stroke="#0f172a" stroke-width="2"/>
  
  <text x="256" y="470" text-anchor="middle" font-family="'Times New Roman', serif" font-weight="400" font-style="italic" font-size="32" fill="#0f172a" letter-spacing="3">Clock Lobster</text>
  <text x="256" y="488" text-anchor="middle" font-family="'Times New Roman', serif" font-size="10" fill="#a1a1aa" letter-spacing="4">AUTOMATION ATELIER</text>
</svg>'''

# ── 10. Dynamic Wordmark Lockup ──────────────────────────────────────────────
WORDMARK = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="w1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
  </defs>
  
  <!-- Horizontal lockup layout -->
  <!-- Icon on left -->
  <g transform="translate(60, 206)">
    <!-- Stopwatch / lobster hybrid -->
    <circle cx="70" cy="70" r="65" fill="none" stroke="#0f172a" stroke-width="8"/>
    <circle cx="70" cy="70" r="55" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
    
    <!-- Clock face -->
    <g fill="#0f172a">
      <rect x="66" y="18" width="8" height="6" rx="1"/><rect x="66" y="116" width="8" height="6" rx="1"/>
      <rect x="18" y="66" width="6" height="8" rx="1"/><rect x="116" y="66" width="6" height="8" rx="1"/>
    </g>
    <line x1="70" y1="70" x2="70" y2="35" stroke="#0f172a" stroke-width="5" stroke-linecap="round"/>
    <line x1="70" y1="70" x2="95" y2="85" stroke="#e11d48" stroke-width="4" stroke-linecap="round"/>
    <circle cx="70" cy="70" r="6" fill="#0f172a"/>
    
    <!-- Stopwatch crown -->
    <rect x="64" y="2" width="12" height="10" rx="2" fill="#0f172a"/>
    <rect x="60" y="-4" width="20" height="6" rx="2" fill="#0f172a"/>
    
    <!-- Lobster claws wrapping around -->
    <path d="M5 50 C-15 30, -25 50, -15 70 C-10 80, 10 75, 20 65" fill="none" stroke="url(#w1)" stroke-width="6" stroke-linecap="round"/>
    <path d="M-15 70 L-25 65 L-20 55" fill="none" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
    
    <path d="M135 50 C155 30, 165 50, 155 70 C150 80, 130 75, 120 65" fill="none" stroke="url(#w1)" stroke-width="6" stroke-linecap="round"/>
    <path d="M155 70 L165 65 L160 55" fill="none" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
    
    <!-- Antennae -->
    <path d="M50 10 Q40 -20 25 -30" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
    <path d="M90 10 Q100 -20 115 -30" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  </g>
  
  <!-- Wordmark to right -->
  <text x="240" y="260" font-family="'Segoe UI', Arial, sans-serif" font-weight="800" font-size="48" fill="#0f172a" letter-spacing="-1">Clock</text>
  <text x="240" y="310" font-family="'Segoe UI', Arial, sans-serif" font-weight="800" font-size="48" fill="#e11d48" letter-spacing="-1">Lobster</text>
  
  <!-- Subtitle -->
  <text x="240" y="340" font-family="'Segoe UI', Arial, sans-serif" font-weight="400" font-size="14" fill="#64748b" letter-spacing="4">AUTOMATION AGENCY</text>
  
  <!-- Underline accent -->
  <line x1="240" y1="355" x2="440" y2="355" stroke="#e11d48" stroke-width="4" stroke-linecap="round"/>
</svg>'''


FILES = {
    "option-01-shield-crest.svg": SHIELD,
    "option-02-negative-space.svg": NEGATIVE,
    "option-03-side-profile.svg": SIDE,
    "option-04-abstract-mark.svg": ABSTRACT,
    "option-05-art-deco.svg": ARTDECO,
    "option-06-modern-gradient.svg": MODERN_GRAD,
    "option-07-monogram-seal.svg": MONOGRAM,
    "option-08-isometric-tech.svg": ISOMETRIC,
    "option-09-luxe-line-art.svg": LUXE,
    "option-10-wordmark-lockup.svg": WORDMARK,
}

for name, svg in FILES.items():
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Created {path}")

print(f"\nDone! {len(FILES)} logo concepts saved to {OUT}/")
