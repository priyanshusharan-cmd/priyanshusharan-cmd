# Regenerates every SVG in ../assets:  python3 scripts/generate_assets.py assets
import random, os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

BG = "#060A18"
PANEL = "#0B1228"
LINE = "#1B2650"
TEXT = "#EAF0FF"
MUTED = "#8A97C2"
DIM = "#4A5687"
CYAN = "#5EEAD4"
AMBER = "#F5B841"
VIOLET = "#A78BFA"
PINK = "#F472B6"
BLUE = "#60A5FA"

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Inter',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'JetBrains Mono',Menlo,Consolas,monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def stars(w, h, n, seed, twinkle=True):
    rnd = random.Random(seed)
    out = []
    for i in range(n):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h)
        r = rnd.choice([0.6, 0.8, 1.0, 1.0, 1.3, 1.6])
        o = rnd.uniform(0.25, 0.9)
        cls = ""
        if twinkle and rnd.random() < 0.35:
            cls = f' class="tw" style="animation-delay:-{rnd.uniform(0, 6):.2f}s;animation-duration:{rnd.uniform(3, 7):.2f}s"'
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{TEXT}" opacity="{o:.2f}"{cls}/>')
    return "\n    ".join(out)


def write(name, svg):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg.strip() + "\n")


# ---------------------------------------------------------------- HERO
FIG8 = "M 0 0 C 40 -62, 140 -62, 140 0 C 140 62, 40 62, 0 0 C -40 -62, -140 -62, -140 0 C -140 62, -40 62, 0 0 Z"

hero = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="1200" height="440" role="img" aria-label="Priyanshu Sharan. CS engineer at BMSCE building apps, AI agent security and orbital simulations.">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0A1230"/>
      <stop offset="0.55" stop-color="{BG}"/>
      <stop offset="1" stop-color="#120A2A"/>
    </linearGradient>
    <radialGradient id="neb1" cx="0.78" cy="0.45" r="0.45">
      <stop offset="0" stop-color="{VIOLET}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="neb2" cx="0.12" cy="0.1" r="0.5">
      <stop offset="0" stop-color="{CYAN}" stop-opacity="0.12"/>
      <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{TEXT}"/>
      <stop offset="0.6" stop-color="#CFE0FF"/>
      <stop offset="1" stop-color="{CYAN}"/>
    </linearGradient>
    <filter id="glow" x="-200%" y="-200%" width="500%" height="500%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="frame"><rect width="1200" height="440" rx="22"/></clipPath>
    <path id="fig8" d="{FIG8}"/>
  </defs>
  <style>
    .tw {{ animation: tw 5s ease-in-out infinite; }}
    @keyframes tw {{ 0%,100% {{ opacity:.15 }} 50% {{ opacity:.95 }} }}
    .rise {{ opacity:0; animation: rise .9s cubic-bezier(.2,.7,.2,1) forwards; }}
    .d1 {{ animation-delay:.15s }} .d2 {{ animation-delay:.35s }} .d3 {{ animation-delay:.55s }} .d4 {{ animation-delay:.75s }}
    @keyframes rise {{ from {{ opacity:0; transform:translateY(14px) }} to {{ opacity:1; transform:none }} }}
    .role {{ opacity:0; animation: cyc 12s infinite; }}
    .r2 {{ animation-delay:3s }} .r3 {{ animation-delay:6s }} .r4 {{ animation-delay:9s }}
    @keyframes cyc {{ 0% {{ opacity:0; transform:translateY(10px) }} 3%,22% {{ opacity:1; transform:none }} 25%,100% {{ opacity:0; transform:translateY(-10px) }} }}
    .cur {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity:0 }} }}
    .spin {{ transform-origin: 900px 220px; animation: spin 90s linear infinite; }}
    .spin2 {{ transform-origin: 900px 220px; animation: spin 140s linear infinite reverse; }}
    @keyframes spin {{ to {{ transform: rotate(360deg) }} }}
    .dash {{ stroke-dasharray: 2 7; animation: flow 6s linear infinite; }}
    @keyframes flow {{ to {{ stroke-dashoffset: -90 }} }}
  </style>

  <g clip-path="url(#frame)">
    <rect width="1200" height="440" fill="url(#bg)"/>
    <rect width="1200" height="440" fill="url(#neb1)"/>
    <rect width="1200" height="440" fill="url(#neb2)"/>
    <g>
    {stars(1200, 440, 140, 7)}
    </g>

    <!-- grid horizon -->
    <g opacity="0.18" stroke="{BLUE}" stroke-width="1">
      {''.join(f'<line x1="0" y1="{400 + i*i*1.6:.1f}" x2="1200" y2="{400 + i*i*1.6:.1f}"/>' for i in range(0, 6))}
    </g>

    <!-- orbital system -->
    <g class="spin2" opacity="0.35">
      <ellipse cx="900" cy="220" rx="300" ry="120" fill="none" stroke="{LINE}" stroke-width="1.2"/>
    </g>
    <g class="spin" opacity="0.5">
      <ellipse cx="900" cy="220" rx="250" ry="150" fill="none" stroke="{LINE}" stroke-width="1" stroke-dasharray="1 6"/>
      <circle cx="1150" cy="220" r="3" fill="{BLUE}"/>
    </g>

    <g transform="translate(900 220) scale(1.45)">
      <use href="#fig8" fill="none" stroke="{MUTED}" stroke-opacity="0.35" stroke-width="1" class="dash"/>
      <g filter="url(#glow)">
        <circle r="7" fill="{AMBER}">
          <animateMotion dur="9s" repeatCount="indefinite" begin="0s"><mpath href="#fig8"/></animateMotion>
        </circle>
        <circle r="6" fill="{CYAN}">
          <animateMotion dur="9s" repeatCount="indefinite" begin="-3s"><mpath href="#fig8"/></animateMotion>
        </circle>
        <circle r="6" fill="{VIOLET}">
          <animateMotion dur="9s" repeatCount="indefinite" begin="-6s"><mpath href="#fig8"/></animateMotion>
        </circle>
      </g>
    </g>
    <text x="900" y="395" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{DIM}" letter-spacing="2">THREE-BODY  ·  FIGURE-EIGHT CHOREOGRAPHY</text>

    <!-- copy -->
    <g font-family="{SANS}">
      <text class="rise d1" x="80" y="118" font-family="{MONO}" font-size="16" fill="{CYAN}" letter-spacing="1">~/hello-world  <tspan fill="{DIM}">// priyanshusharan-cmd</tspan></text>
      <text class="rise d2" x="76" y="196" font-size="68" font-weight="800" fill="url(#name)" letter-spacing="-1.5">Priyanshu</text>
      <text class="rise d2" x="76" y="266" font-size="68" font-weight="800" fill="url(#name)" letter-spacing="-1.5">Sharan</text>
      <text class="rise d3" x="80" y="310" font-size="19" fill="{MUTED}">CS Engineering @ BMS College of Engineering, Bangalore</text>

      <g class="rise d4" font-family="{MONO}" font-size="18">
        <rect x="80" y="334" width="440" height="40" rx="10" fill="{PANEL}" stroke="{LINE}"/>
        <text x="98" y="360" fill="{AMBER}">&gt;</text>
        <text x="118" y="360" fill="{TEXT}">building</text>
        <g>
          <text class="role" x="220" y="360" fill="{CYAN}">full-stack mobile apps</text>
          <text class="role r2" x="220" y="360" fill="{VIOLET}">AI-agent security</text>
          <text class="role r3" x="220" y="360" fill="{AMBER}">orbital simulators</text>
          <text class="role r4" x="220" y="360" fill="{PINK}">a self-hosted cloud</text>
        </g>
        <rect class="cur" x="498" y="345" width="9" height="20" fill="{CYAN}"/>
      </g>
    </g>

    <rect x="0.5" y="0.5" width="1199" height="439" rx="22" fill="none" stroke="{LINE}"/>
  </g>
</svg>
"""
write("hero.svg", hero)

# ---------------------------------------------------------------- TERMINAL
lines = [
    ("cmd", "whoami"),
    ("out", [(TEXT, "Priyanshu Sharan"), (MUTED, "  ·  3rd-year CSE  ·  BMSCE, Bangalore")]),
    ("cmd", "cat focus.txt"),
    ("out", [(CYAN, "mobile apps"), (DIM, "  ·  "), (VIOLET, "AI-agent security"), (DIM, "  ·  "), (AMBER, "physics simulations")]),
    ("cmd", "cat wins.log"),
    ("out", [(AMBER, "★ "), (TEXT, "Best UI/UX"), (MUTED, "  —  Hacktoberfest 2026, with Team Hopsync")]),
    ("cmd", "ls ./building"),
    ("out", [(PINK, "homeport/"), (MUTED, "  self-hosted P2P personal cloud on a Raspberry Pi 4")]),
    ("cmd", "echo $PHILOSOPHY"),
    ("out", [(TEXT, "learn by shipping. "), (MUTED, "one real project beats ten tutorials.")]),
]
rows = []
y = 104
delay = 0.3
for kind, content in lines:
    if kind == "cmd":
        rows.append(
            f'<g class="ln" style="animation-delay:{delay:.2f}s"><text x="40" y="{y}"><tspan fill="{CYAN}">priyanshu</tspan><tspan fill="{DIM}">@</tspan><tspan fill="{VIOLET}">bmsce</tspan><tspan fill="{DIM}"> ~ </tspan><tspan fill="{AMBER}">$</tspan><tspan fill="{TEXT}"> {esc(content)}</tspan></text></g>'
        )
        delay += 0.45
        y += 28
    else:
        spans = "".join(f'<tspan fill="{c}">{esc(t)}</tspan>' for c, t in content)
        rows.append(f'<g class="ln" style="animation-delay:{delay:.2f}s"><text x="40" y="{y}"><tspan fill="{DIM}">↳ </tspan>{spans}</text></g>')
        delay += 0.35
        y += 40
cur_y = y
term_h = cur_y + 36

term = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {term_h}" width="1200" height="{term_h}" role="img" aria-label="About: Priyanshu Sharan, third-year CSE at BMSCE Bangalore. Focus: mobile apps, AI-agent security, physics simulations. Won Best UI/UX at Hacktoberfest 2026 with Team Hopsync. Building Homeport, a self-hosted personal cloud.">
  <defs>
    <linearGradient id="tb" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#101935"/><stop offset="1" stop-color="#140F30"/>
    </linearGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{CYAN}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{CYAN}" stop-opacity="0.06"/>
      <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="c"><rect width="1200" height="{term_h}" rx="18"/></clipPath>
  </defs>
  <style>
    .ln {{ opacity:0; animation: ln .35s ease-out forwards; }}
    @keyframes ln {{ from {{ opacity:0; transform:translateX(-8px) }} to {{ opacity:1; transform:none }} }}
    .cur {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity:0 }} }}
    .scan {{ animation: scan 7s linear infinite; }}
    @keyframes scan {{ from {{ transform:translateY(-120px) }} to {{ transform:translateY({term_h}px) }} }}
  </style>
  <g clip-path="url(#c)">
    <rect width="1200" height="{term_h}" fill="{BG}"/>
    <rect width="1200" height="48" fill="url(#tb)"/>
    <line x1="0" y1="48" x2="1200" y2="48" stroke="{LINE}"/>
    <circle cx="30" cy="24" r="7" fill="#FF5F57"/><circle cx="54" cy="24" r="7" fill="#FEBC2E"/><circle cx="78" cy="24" r="7" fill="#28C840"/>
    <text x="600" y="29" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{MUTED}">01 — about  ·  zsh  ·  120×{len(lines)*3}</text>
    <rect class="scan" x="0" y="0" width="1200" height="120" fill="url(#scan)"/>
    <g font-family="{MONO}" font-size="17">
      {chr(10).join('      ' + r for r in rows)}
      <g class="ln" style="animation-delay:{delay:.2f}s">
        <text x="40" y="{cur_y}"><tspan fill="{CYAN}">priyanshu</tspan><tspan fill="{DIM}">@</tspan><tspan fill="{VIOLET}">bmsce</tspan><tspan fill="{DIM}"> ~ </tspan><tspan fill="{AMBER}">$</tspan></text>
        <rect class="cur" x="226" y="{cur_y - 15}" width="10" height="19" fill="{CYAN}"/>
      </g>
    </g>
    <rect x="0.5" y="0.5" width="1199" height="{term_h - 1}" rx="18" fill="none" stroke="{LINE}"/>
  </g>
</svg>
"""
write("about.svg", term)

# ---------------------------------------------------------------- SECTION LABELS
def label(fname, num, title, accent):
    x0 = 70 + len(title) * 19.5 + 24
    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 64" width="1200" height="64" role="img" aria-label="{esc(title)}">
  <defs>
    <linearGradient id="l" gradientUnits="userSpaceOnUse" x1="{x0}" y1="0" x2="1200" y2="0">
      <stop offset="0" stop-color="{accent}" stop-opacity="0.9"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .p {{ animation: p 3s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
    @keyframes p {{ 0%,100% {{ opacity:1; transform:scale(1) }} 50% {{ opacity:.4; transform:scale(.6) }} }}
    .sweep {{ stroke-dasharray: 60 900; animation: sw 4s linear infinite; }}
    @keyframes sw {{ from {{ stroke-dashoffset: 0 }} to {{ stroke-dashoffset: -960 }} }}
  </style>
  <circle class="p" cx="10" cy="32" r="5" fill="{accent}"/>
  <text x="30" y="39" font-family="{MONO}" font-size="16" fill="{accent}" letter-spacing="2">{num}</text>
  <text x="70" y="40" font-family="{SANS}" font-size="22" font-weight="700" fill="#8FA0D0" letter-spacing="4">{esc(title.upper())}</text>
  <line x1="{x0}" y1="32" x2="1200" y2="32" stroke="url(#l)" stroke-width="1.5"/>
  <line class="sweep" x1="{x0}" y1="32" x2="1200" y2="32" stroke="{accent}" stroke-width="2"/>
</svg>
"""
    write(fname, svg)


label("label-work.svg", "02", "Selected work", CYAN)
label("label-stack.svg", "03", "Toolkit", VIOLET)
label("label-activity.svg", "04", "Activity", AMBER)
label("label-connect.svg", "05", "Connect", PINK)

# ---------------------------------------------------------------- PROJECT CARDS
CW, CH = 580, 300


def tag_row(tags, x, y, accent):
    out, cx = [], x
    for t in tags:
        w = len(t) * 7.9 + 22
        out.append(
            f'<rect x="{cx:.1f}" y="{y}" width="{w:.1f}" height="26" rx="13" fill="{accent}" fill-opacity="0.09" stroke="{accent}" stroke-opacity="0.35"/>'
            f'<text x="{cx + w / 2:.1f}" y="{y + 17.5}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{accent}">{esc(t)}</text>'
        )
        cx += w + 8
    return "".join(out)


def card(fname, title, kicker, desc_lines, tags, accent, status, art, extra_style=""):
    sw = len(status) * 8.2 + 34
    desc = "".join(
        f'<text x="32" y="{150 + i * 25}" font-family="{SANS}" font-size="16" fill="{MUTED}">{esc(l)}</text>' for i, l in enumerate(desc_lines)
    )
    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW}" height="{CH}" role="img" aria-label="{esc(title)}: {esc(kicker)}. {esc(' '.join(desc_lines))}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{PANEL}"/><stop offset="1" stop-color="{BG}"/>
    </linearGradient>
    <radialGradient id="h" cx="0.92" cy="0.1" r="0.6">
      <stop offset="0" stop-color="{accent}" stop-opacity="0.22"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{accent}" stop-opacity="0"/><stop offset="0.5" stop-color="{accent}"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
    <filter id="gl" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <clipPath id="c"><rect width="{CW}" height="{CH}" rx="18"/></clipPath>
  </defs>
  <style>
    .dot {{ animation: d 1.8s ease-in-out infinite; }}
    @keyframes d {{ 50% {{ opacity:.25 }} }}
    .edge {{ animation: e 5s ease-in-out infinite; }}
    @keyframes e {{ 0%,100% {{ transform:translateX(-{CW}px) }} 50% {{ transform:translateX({CW}px) }} }}
    {extra_style}
  </style>
  <g clip-path="url(#c)">
    <rect width="{CW}" height="{CH}" fill="url(#g)"/>
    <rect width="{CW}" height="{CH}" fill="url(#h)"/>
    {art}
    <rect class="edge" x="0" y="0" width="{CW}" height="2" fill="url(#edge)"/>
    <text x="32" y="52" font-family="{MONO}" font-size="13" fill="{accent}" letter-spacing="2">{esc(kicker.upper())}</text>
    <text x="30" y="100" font-family="{SANS}" font-size="38" font-weight="800" fill="{TEXT}" letter-spacing="-0.5">{esc(title)}</text>
    {desc}
    {tag_row(tags, 32, 238, accent)}
    <g transform="translate({CW - 32 - sw} 32)">
      <rect width="{sw:.1f}" height="28" rx="14" fill="{BG}" stroke="{accent}" stroke-opacity="0.5"/>
      <circle class="dot" cx="16" cy="14" r="4" fill="{accent}"/>
      <text x="28" y="19" font-family="{MONO}" font-size="12" font-weight="700" fill="{accent}" letter-spacing="1.5">{esc(status)}</text>
    </g>
    <rect x="0.5" y="0.5" width="{CW - 1}" height="{CH - 1}" rx="18" fill="none" stroke="{LINE}"/>
  </g>
</svg>
"""
    write(fname, svg)


# Warden: shield with a scanning beam
warden_art = f"""
    <g transform="translate(470 150)" opacity="0.9">
      <path d="M0 -62 L50 -44 L50 4 C50 38 26 58 0 70 C-26 58 -50 38 -50 4 L-50 -44 Z" fill="{VIOLET}" fill-opacity="0.06" stroke="{VIOLET}" stroke-opacity="0.45" stroke-width="1.5"/>
      <path d="M-18 4 L-5 17 L20 -12" fill="none" stroke="{VIOLET}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" filter="url(#gl)" class="tick"/>
      <rect class="beam" x="-60" y="-66" width="120" height="3" fill="{VIOLET}" opacity="0.7"/>
    </g>
"""
card(
    "card-warden.svg", "Warden", "AI-agent firewall",
    ["Agents obey what they read. Warden", "traces where every value came from", "and blocks orders that weren't yours."],
    ["Python", "MCP", "provenance", "zero deps"], VIOLET, "SECURITY", warden_art,
    ".beam { animation: beam 2.6s ease-in-out infinite; } @keyframes beam { 0%,100% { transform:translateY(0) } 50% { transform:translateY(130px) } }"
    " .tick { stroke-dasharray: 60; animation: tk 2.6s ease-in-out infinite; } @keyframes tk { 0%,40% { stroke-dashoffset:60 } 60%,100% { stroke-dashoffset:0 } }",
)

# Celestia: mini orbit
cel_art = f"""
    <g transform="translate(470 150)">
      <ellipse rx="70" ry="26" fill="none" stroke="{CYAN}" stroke-opacity="0.35" transform="rotate(-20)"/>
      <ellipse rx="46" ry="62" fill="none" stroke="{CYAN}" stroke-opacity="0.2" transform="rotate(30)"/>
      <circle r="10" fill="{AMBER}" filter="url(#gl)"/>
      <g transform="rotate(-20)"><circle r="4.5" fill="{CYAN}" filter="url(#gl)"><animateMotion dur="6s" repeatCount="indefinite" path="M70 0 A70 26 0 1 1 -70 0 A70 26 0 1 1 70 0"/></circle></g>
      <g transform="rotate(30)"><circle r="3" fill="{TEXT}"><animateMotion dur="10s" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1" calcMode="linear" path="M46 0 A46 62 0 1 1 -46 0 A46 62 0 1 1 46 0"/></circle></g>
    </g>
"""
card(
    "card-celestia.svg", "Celestia", "Orbital dynamics lab",
    ["Interactive three-body simulator with", "click-to-place bodies, full playback", "and a headless test suite."],
    ["Python", "Streamlit", "REBOUND", "Manim", "Docker"], CYAN, "LIVE", cel_art,
    ".o1 { animation: sp 6s linear infinite; } .o2 { animation: sp 10s linear infinite reverse; } @keyframes sp { to { transform: rotate(360deg) } }",
)

# Ridify: road with a car
rid_art = f"""
    <g transform="translate(408 112) scale(0.78)">
      <path d="M0 70 C 50 70, 70 10, 130 10 S 190 50, 200 50" fill="none" stroke="{AMBER}" stroke-opacity="0.18" stroke-width="14" stroke-linecap="round" id="road"/>
      <path d="M0 70 C 50 70, 70 10, 130 10 S 190 50, 200 50" fill="none" stroke="{AMBER}" stroke-opacity="0.6" stroke-width="1.5" stroke-dasharray="6 8"/>
      <circle cx="0" cy="70" r="5" fill="{CYAN}"/><circle cx="200" cy="50" r="5" fill="{PINK}"/>
      <g filter="url(#gl)">
        <rect x="-9" y="-5" width="18" height="10" rx="4" fill="{AMBER}">
          <animateMotion dur="3.6s" repeatCount="indefinite" rotate="auto" keyPoints="0;1;1" keyTimes="0;0.8;1" calcMode="spline" keySplines="0.45 0 0.25 1;0 0 1 1" path="M0 70 C 50 70, 70 10, 130 10 S 190 50, 200 50"/>
        </rect>
      </g>
    </g>
"""
card(
    "card-ridify.svg", "Ridify", "Campus ride-sharing",
    ["Student carpooling gated by verified", "college email, real-time over Socket.IO,", "with physics-tuned Flutter motion."],
    ["Flutter", "Node.js", "MongoDB", "Socket.IO"], AMBER, "LIVE", rid_art,
)

# CampusIQ: progress ring
circ = 2 * 3.14159 * 44
iq_art = f"""
    <g transform="translate(470 150)">
      <circle r="44" fill="none" stroke="{PINK}" stroke-opacity="0.15" stroke-width="9"/>
      <circle class="ring" r="44" fill="none" stroke="{PINK}" stroke-width="9" stroke-linecap="round" transform="rotate(-90)" stroke-dasharray="{circ:.1f}" filter="url(#gl)"/>
      <text y="6" text-anchor="middle" font-family="{MONO}" font-size="18" font-weight="700" fill="{TEXT}">GPA</text>
      <text y="24" text-anchor="middle" font-family="{MONO}" font-size="9" fill="{MUTED}" letter-spacing="1">TRACKED</text>
    </g>
"""
card(
    "card-campusiq.svg", "CampusIQ", "Academic tracker",
    ["GPA, SGPA and CGPA tracking, attendance", "prediction, timetables and a goal", "calculator for next semester."],
    ["React Native", "Expo", "TypeScript", "Zustand"], PINK, "MOBILE", iq_art,
    f".ring {{ animation: rg 4s ease-in-out infinite; }} @keyframes rg {{ 0% {{ stroke-dashoffset:{circ:.1f} }} 60%,85% {{ stroke-dashoffset:{circ * 0.08:.1f} }} 100% {{ stroke-dashoffset:{circ:.1f} }} }}",
)

# ---------------------------------------------------------------- STACK
groups = [
    ("languages", CYAN, ["Dart", "TypeScript", "JavaScript", "Python"]),
    ("mobile", AMBER, ["Flutter", "React Native", "Expo", "Zustand"]),
    ("backend", VIOLET, ["Node.js", "Express", "MongoDB", "Socket.IO", "Firebase"]),
    ("science", PINK, ["Streamlit", "REBOUND", "Manim", "NumPy"]),
    ("tooling", BLUE, ["Git", "Docker", "Render", "Figma", "MCP"]),
]
rowsvg = []
y = 46
for i, (g, col, items) in enumerate(groups):
    rowsvg.append(f'<text x="40" y="{y + 22}" font-family="{MONO}" font-size="14" fill="{DIM}">{g}</text>')
    rowsvg.append(f'<text x="160" y="{y + 22}" font-family="{MONO}" font-size="14" fill="{DIM}">→</text>')
    cx = 196
    for j, it in enumerate(items):
        w = len(it) * 9.6 + 32
        d = 0.15 + i * 0.12 + j * 0.06
        rowsvg.append(
            f'<g class="chip" style="animation-delay:{d:.2f}s"><rect x="{cx:.1f}" y="{y}" width="{w:.1f}" height="34" rx="9" fill="{col}" fill-opacity="0.08" stroke="{col}" stroke-opacity="0.4"/>'
            f'<circle cx="{cx + 14:.1f}" cy="{y + 17}" r="3" fill="{col}"/>'
            f'<text x="{cx + 24:.1f}" y="{y + 22.5}" font-family="{MONO}" font-size="15" fill="{TEXT}">{esc(it)}</text></g>'
        )
        cx += w + 10
    y += 52
sh = y + 14
stack = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {sh}" width="1200" height="{sh}" role="img" aria-label="Toolkit. Languages: Dart, TypeScript, JavaScript, Python. Mobile: Flutter, React Native, Expo, Zustand. Backend: Node.js, Express, MongoDB, Socket.IO, Firebase. Science: Streamlit, REBOUND, Manim, NumPy. Tooling: Git, Docker, Render, Figma, MCP.">
  <defs>
    <clipPath id="c"><rect width="1200" height="{sh}" rx="18"/></clipPath>
    <radialGradient id="h" cx="1" cy="1" r="0.8"><stop offset="0" stop-color="{VIOLET}" stop-opacity="0.14"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
  </defs>
  <style>
    .chip {{ opacity:0; animation: ch .5s cubic-bezier(.2,.7,.2,1) forwards; }}
    @keyframes ch {{ from {{ opacity:0; transform:translateY(8px) }} to {{ opacity:1; transform:none }} }}
    .o1 {{ animation: sp 9s linear infinite; }} .o2 {{ animation: sp 14s linear infinite reverse; }}
    @keyframes sp {{ to {{ transform: rotate(360deg) }} }}
  </style>
  <g clip-path="url(#c)">
    <rect width="1200" height="{sh}" fill="{BG}"/>
    <rect width="1200" height="{sh}" fill="url(#h)"/>
    <g opacity="0.5">{stars(1200, sh, 26, 3, twinkle=False)}</g>
    {''.join(rowsvg)}
    <g transform="translate(1040 {sh/2:.0f})" opacity="0.8">
      <ellipse rx="92" ry="34" fill="none" stroke="{VIOLET}" stroke-opacity="0.3" transform="rotate(-18)"/>
      <ellipse rx="60" ry="80" fill="none" stroke="{CYAN}" stroke-opacity="0.18" transform="rotate(28)"/>
      <circle r="9" fill="{AMBER}" opacity="0.9"/>
      <g transform="rotate(-18)"><circle r="4" fill="{VIOLET}"><animateMotion dur="9s" repeatCount="indefinite" path="M92 0 A92 34 0 1 1 -92 0 A92 34 0 1 1 92 0"/></circle></g>
      <g transform="rotate(28)"><circle r="3" fill="{CYAN}"><animateMotion dur="14s" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1" calcMode="linear" path="M60 0 A60 80 0 1 1 -60 0 A60 80 0 1 1 60 0"/></circle></g>
    </g>
    <rect x="0.5" y="0.5" width="1199" height="{sh - 1}" rx="18" fill="none" stroke="{LINE}"/>
  </g>
</svg>
"""
write("stack.svg", stack)

# ---------------------------------------------------------------- FOOTER
footer = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 150" width="1200" height="150" role="img" aria-label="Thanks for stopping by.">
  <defs>
    <linearGradient id="w" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}"/><stop offset="0.5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{AMBER}"/>
    </linearGradient>
  </defs>
  <style>
    .wv {{ animation: wv 8s linear infinite; }}
    @keyframes wv {{ to {{ transform: translateX(-400px) }} }}
    .fade {{ animation: fd 4s ease-in-out infinite; }}
    @keyframes fd {{ 50% {{ opacity:.45 }} }}
  </style>
  <g opacity="0.55">{stars(1200, 150, 30, 11)}</g>
  <g class="wv">
    <path d="{' '.join(f'M{x} 60 q 100 -30 200 0 t 200 0' for x in range(0, 1601, 400))}" fill="none" stroke="url(#w)" stroke-width="2" opacity="0.7"/>
    <path d="{' '.join(f'M{x} 72 q 100 24 200 0 t 200 0' for x in range(0, 1601, 400))}" fill="none" stroke="url(#w)" stroke-width="1" opacity="0.35"/>
  </g>
  <text class="fade" x="600" y="122" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{MUTED}" letter-spacing="3">THANKS FOR STOPPING BY  ·  KEEP SHIPPING</text>
</svg>
"""
write("footer.svg", footer)
print("ok")
