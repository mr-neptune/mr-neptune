"""Generate assets/profile.svg, the full-page illustrated profile."""
import math
import os
import random
import textwrap
from xml.sax.saxutils import escape

random.seed(1028)
W = 900
M = 56
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "profile.svg")

INK = "#f5f2e6"
SOFT = "#d3e0e4"
GOLD = "#f3d98b"
BLUE = "#9cc6ee"

EXPERIENCE = [
    ("Sep 2026 – Present", "Amazon", "SDE Intern, Prime Tech"),
    ("May – Aug 2026", "BitGo", "Software Engineer Intern, Wallet Core"),
    ("Sep – Dec 2025", "Emailgistics", "Senior Software Engineer Intern"),
    ("Jan – Apr 2025", "Supernova MGU", "AI Software Engineer Intern"),
    ("Sep – Dec 2024", "Caribou Contest", "Full Stack Developer Intern"),
]
SKILLS = [
    ("Languages", ["Go", "Python", "Java", "TypeScript", "C++", "Rust", "SQL"]),
    ("Backend and frontend", ["Spring Boot", "Gin", "FastAPI", "Flask", "React", "Vue.js"]),
    ("Cloud and data", ["AWS", "Docker", "Kubernetes", "Kafka", "PostgreSQL", "MongoDB", "Redis", "Grafana"]),
    ("AI", ["TensorFlow", "Keras", "LangChain", "RAG", "Multi-agent systems", "Reinforcement learning"]),
]
PROJECTS = [
    ("2048-Auto", "A TD(λ) CNN agent with expectimax search that reaches the 8192 tile in 52% of test games and 4096 in 94.8%."),
    ("fantasy_cracker", "An autopilot for 9-category fantasy basketball: ML projections, Claude's reading of the news and 2,000-run matchup simulations."),
    ("WebWhisper", "A multi-provider AI agent in a browser side panel for YouTube, Reddit, LinkedIn and Instagram."),
    ("Sidechat", "A chat UI with side questions, conversation forking and rewind."),
    ("Chamber Claw 3000", "A text-based dungeon crawler in C++, built around object-oriented design."),
]
AWARDS = [
    "Top 0.5%, CEMC CSMC (2021, 2022)",
    "Top 1%, AMC 12 (2021, 2022)",
    "Top 5%, Euclid Contest (2023)",
]
ABOUT = (
    "I'm a backend-focused Computer Science student at the University of Waterloo "
    "(AI specialization, Combinatorics & Optimization minor, class of 2028). I work on "
    "AI operations, cryptographic infrastructure and distributed systems, and I usually "
    "end up teaching a program to play a game along the way."
)


def text(x, y, s, size, fill=INK, anchor="start", extra=""):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
        f'text-anchor="{anchor}" {extra}>{escape(s)}</text>'
    )


def heading(y, s):
    return (
        f'<use href="#f" transform="translate({M + 9} {y - 8}) scale(1.05)" fill="{BLUE}"/>'
        + text(M + 30, y, s, 30, GOLD, extra='letter-spacing="1"')
    )


body = []
cx, cy = W / 2, 190

# Title block.
body.append(text(W / 2, 186, "Wayne Wen", 76, anchor="middle", extra='letter-spacing="2"'))
body.append(text(W / 2, 232, "Computer Science at the University of Waterloo", 23, SOFT, "middle", 'letter-spacing="1"'))
y = 350

# About.
y += 88
body.append(heading(y, "About"))
y += 46
for line in textwrap.wrap(ABOUT, 74):
    body.append(text(M, y, line, 21))
    y += 32

# Experience.
y += 52
body.append(heading(y, "Experience"))
y += 22
for when, where, role in EXPERIENCE:
    y += 34
    body.append(text(M, y, where, 23, GOLD))
    body.append(text(W - M, y, when, 19, SOFT, "end"))
    y += 30
    body.append(text(M, y, role, 20))
    y += 12

# Skills.
y += 62
body.append(heading(y, "Skills"))
y += 12
for label, chips in SKILLS:
    y += 38
    body.append(text(M, y, label, 20, SOFT, extra='font-style="italic"'))
    y += 14
    x = M
    for chip in chips:
        w = len(chip) * 10.2 + 32
        if x + w > W - M:
            x = M
            y += 48
        body.append(
            f'<rect x="{x}" y="{y}" width="{w:.0f}" height="38" rx="19" fill="#17263f" '
            f'fill-opacity=".72" stroke="{BLUE}" stroke-opacity=".6"/>'
        )
        body.append(text(x + w / 2, y + 26, chip, 19, INK, "middle"))
        x += w + 10
    y += 40

# Projects.
y += 62
body.append(heading(y, "Projects"))
y += 10
for name, desc in PROJECTS:
    y += 38
    body.append(text(M, y, name, 23, GOLD))
    for line in textwrap.wrap(desc, 76):
        y += 29
        body.append(text(M, y, line, 20))
    y += 8

# Awards.
y += 58
body.append(heading(y, "Awards"))
y += 12
for award in AWARDS:
    y += 34
    body.append(text(M, y, award, 21))

# Footer.
y += 86
body.append(text(W / 2, y, "Thanks for stopping by.", 24, INK, "middle", 'font-style="italic"'))

HORIZON = y + 70
H = HORIZON + 290

stars = []
for i in range(int(H / 11)):
    sx, sy = random.randint(0, W), random.randint(0, HORIZON - 40)
    r = random.choice([0.7, 0.9, 1.2, 1.6])
    cls = f' class="tw t{i % 4}"' if i % 3 == 0 else ""
    stars.append(f'<circle cx="{sx}" cy="{sy}" r="{r}" fill="#f4f1de" opacity=".8"{cls}/>')

ticks = []
for i in range(36):
    a = math.radians(i * 10)
    r1, r2 = 136, 146 if i % 3 else 154
    ticks.append(
        f'<line x1="{cx + r1 * math.cos(a):.1f}" y1="{cy + r1 * math.sin(a):.1f}" '
        f'x2="{cx + r2 * math.cos(a):.1f}" y2="{cy + r2 * math.sin(a):.1f}"/>'
    )
squares = []
for start in (0, 45):
    pts = " ".join(
        f"{cx + 122 * math.cos(math.radians(start + k * 90)):.1f},"
        f"{cy + 122 * math.sin(math.radians(start + k * 90)):.1f}"
        for k in range(4)
    )
    squares.append(f'<polygon points="{pts}"/>')

flowers = []
pts = sorted(
    (HORIZON + 60 + random.random() ** 0.7 * 230, random.randint(-10, W + 10))
    for _ in range(320)
)
for fy, fx in pts:
    t = (fy - HORIZON - 60) / 230
    colour = random.choice(["#7fb2e5", "#9cc6ee", "#5d93d1", "#b9d8f4", "#e8eef7"])
    flowers.append(
        f'<use href="#f" transform="translate({fx} {fy:.0f}) scale({0.5 + t * 1.5:.2f}) '
        f'rotate({random.randint(0, 72)})" fill="{colour}" opacity="{0.75 + t * 0.25:.2f}"/>'
    )

petals = "".join(
    f'<ellipse class="p" style="animation-delay:-{d}s" cx="{px}" cy="{HORIZON - py}" rx="4" ry="2" fill="#b9d8f4"/>'
    for px, py, d in [(120, 60, 0), (330, 20, 3), (620, 50, 1.5), (780, 10, 5)]
)

ridge = (
    f"M0 {HORIZON + 30} L110 {HORIZON - 30} L220 {HORIZON + 15} L350 {HORIZON - 45} "
    f"L480 {HORIZON + 20} L620 {HORIZON - 25} L760 {HORIZON + 15} L900 {HORIZON - 35} V{HORIZON + 120} H0Z"
)
hill = f"M0 {HORIZON + 62} C170 {HORIZON + 24} 300 {HORIZON + 68} 460 {HORIZON + 52} S760 {HORIZON + 26} 900 {HORIZON + 56} V{H} H0Z"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Wayne Wen's profile, illustrated as a night sky above a field of blue flowers">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#121835"/><stop offset=".55" stop-color="#1b2a52"/><stop offset=".84" stop-color="#2c4674"/><stop offset=".93" stop-color="#7f9fb4"/><stop offset="1" stop-color="#d9c9a4"/></linearGradient>
<linearGradient id="field" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f6f70"/><stop offset="1" stop-color="#17383f"/></linearGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#cfe9d8" stop-opacity=".28"/><stop offset="1" stop-color="#cfe9d8" stop-opacity="0"/></radialGradient>
<g id="f"><ellipse cy="-5" rx="3.2" ry="5"/><ellipse cy="-5" rx="3.2" ry="5" transform="rotate(72)"/><ellipse cy="-5" rx="3.2" ry="5" transform="rotate(144)"/><ellipse cy="-5" rx="3.2" ry="5" transform="rotate(216)"/><ellipse cy="-5" rx="3.2" ry="5" transform="rotate(288)"/><circle r="2" fill="#f3d98b"/></g>
</defs>
<style>
.tw{{animation:tw 4s ease-in-out infinite}}.t1{{animation-delay:-1s}}.t2{{animation-delay:-2s}}.t3{{animation-delay:-3s}}
@keyframes tw{{50%{{opacity:.2}}}}
.spin{{transform-origin:{cx}px {cy}px;animation:spin 90s linear infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.p{{animation:drift 9s ease-in-out infinite}}
@keyframes drift{{0%{{transform:translate(0,0);opacity:0}}20%{{opacity:.9}}100%{{transform:translate(110px,70px) rotate(40deg);opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.tw,.spin,.p{{animation:none}}}}
text{{font-family:Georgia,'Times New Roman',serif}}
</style>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
{''.join(stars)}
<circle cx="{cx}" cy="{cy}" r="240" fill="url(#glow)"/>
<g class="spin" fill="none" stroke="#d8efe0" stroke-opacity=".32" stroke-width="1.2"><circle cx="{cx}" cy="{cy}" r="158"/><circle cx="{cx}" cy="{cy}" r="136"/><circle cx="{cx}" cy="{cy}" r="122"/>{''.join(ticks)}{''.join(squares)}</g>
<path d="{ridge}" fill="#54748f" opacity=".6"/>
<path d="{hill}" fill="url(#field)"/>
{''.join(flowers)}
{petals}
{''.join(body)}
</svg>
"""
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(svg)
print(H)
