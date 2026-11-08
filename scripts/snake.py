#!/usr/bin/env python3
"""TVA/Loki-themed contribution graph + 'Temporal Snake' built from your real GitHub data.
Usage: python scripts/snake.py dist/snake.svg   (ACTIVITY_MOCK=1 for a layout preview)"""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import activity as A
from html import escape as E

OUT = sys.argv[1] if len(sys.argv) > 1 else "snake.svg"
LV = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
FILL = ["#0f1d14", "#14502c", "#17a14a", "#39ff6a", "#ffb347"]
TOP  = ["#17281d", "#1c6a3a", "#2bd062", "#a8ffc4", "#ffe2a8"]
DUR = 28

def build(u):
    cal = u["contributionsCollection"]["contributionCalendar"]
    weeks = cal["weeks"]; total = cal["totalContributions"]
    n = len(weeks); CS, G = 14, 3; X0, Y0 = 62, 112
    cells = []   # (col,row,level,count,date)
    for c, w in enumerate(weeks):
        for d in w["contributionDays"]:
            dt = datetime.date.fromisoformat(d["date"]); row = (dt.weekday() + 1) % 7
            cells.append((c, row, LV.get(d.get("contributionLevel", "NONE"), 0), d["contributionCount"], dt))
    pos = lambda c, r: (X0 + c * (CS + G) + CS / 2, Y0 + r * (CS + G) + CS / 2)
    order = {}
    path = []
    for c in range(n):
        rows = range(7) if c % 2 == 0 else range(6, -1, -1)
        for r in rows: order[(c, r)] = len(path); path.append(pos(c, r))
    N = len(path); d = "M%.1f %.1f " % path[0] + " ".join("L%.1f %.1f" % p for p in path[1:])
    H = Y0 + 7 * (CS + G) + 120
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 %d" width="1000" height="%d">' % (H, H)]
    s.append('''<defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowU" filterUnits="userSpaceOnUse" x="0" y="0" width="1000" height="600"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1307"/><stop offset="1" stop-color="#050805"/></linearGradient>
<radialGradient id="head" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#fff6d8"/><stop offset=".35" stop-color="#ffb347"/><stop offset=".8" stop-color="#e06a0c"/><stop offset="1" stop-color="#5a2305"/></radialGradient>
<radialGradient id="body" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#e6ffe9"/><stop offset=".4" stop-color="#39ff6a"/><stop offset="1" stop-color="#06561f"/></radialGradient>
<radialGradient id="vig" cx=".5" cy=".5" r=".78"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".5"/></radialGradient>
<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".25"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<style>.m{font-family:"Courier New",Courier,monospace}</style>''')
    s.append('<rect width="1000" height="%d" fill="url(#bg)"/>' % H)
    s.append('<text x="500" y="34" text-anchor="middle" class="m" font-size="14" letter-spacing="8" fill="#e07a14">TEMPORAL SNAKE // CONTRIBUTIONS</text>')
    s.append('<text x="500" y="56" text-anchor="middle" class="m" font-size="11" letter-spacing="4" fill="#39ff6a">%d EVENTS ON THE SACRED TIMELINE</text>' % total)
    # glowing frame wires
    for y, ph in ((78, 0), (Y0 + 7 * (CS + G) + 16, 2)):
        s.append('<path d="M40 %d H960" stroke="#39ff6a" stroke-width="2" stroke-dasharray="14 10" opacity=".8" filter="url(#glowU)"><animate attributeName="stroke-dashoffset" to="-240" dur="3s" begin="-%ds" repeatCount="indefinite"/></path>' % (y, ph))
    # month + weekday labels
    last = None
    for c, w in enumerate(weeks):
        dt = datetime.date.fromisoformat(w["contributionDays"][0]["date"])
        if dt.month != last:
            last = dt.month
            s.append('<text x="%.1f" y="%d" class="m" font-size="10" fill="#e07a14">%s</text>' % (X0 + c * (CS + G), Y0 - 8, dt.strftime("%b").upper()))
    for r, lab in ((1, "MON"), (3, "WED"), (5, "FRI")):
        s.append('<text x="%d" y="%.1f" text-anchor="end" class="m" font-size="9" fill="#8a8a6a">%s</text>' % (X0 - 8, Y0 + r * (CS + G) + CS - 3, lab))
    # tiles (3D extruded, eaten by the snake)
    for c, r, lv, cnt, dt in cells:
        x = X0 + c * (CS + G); y = Y0 + r * (CS + G)
        s.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="3" fill="#020503"/>' % (x + 1.5, y + 2, CS, CS))
        anim = ""
        if lv > 0 and (c, r) in order:
            f = order[(c, r)] / max(N - 1, 1)
            anim = '<animate attributeName="opacity" dur="%ds" repeatCount="indefinite" keyTimes="0;%.4f;%.4f;0.96;1" values="1;1;.12;.12;1"/>' % (DUR, f, min(f + .004, .95))
        glow = ' filter="url(#glow)"' if lv >= 3 else ""
        s.append('<g%s>%s<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="3" fill="%s"/><rect x="%.1f" y="%.1f" width="%d" height="%d" rx="3" fill="url(#gloss)"/><rect x="%.1f" y="%.1f" width="%d" height="2" rx="1" fill="%s" opacity=".7"/></g>' % (glow, anim, x, y, CS, CS, FILL[lv], x, y, CS, CS, x + 1, y + .5, CS - 2, TOP[lv]))
    # snake: glowing wire trail + orange head + green body
    s.append('<path id="route" d="%s" fill="none" stroke="none"/>' % d)
    for k in range(9, 0, -1):
        s.append('<circle r="%.1f" fill="url(#body)" opacity="%.2f" filter="url(#glow)"><animateMotion dur="%ds" begin="-%.2fs" repeatCount="indefinite"><mpath href="#route"/></animateMotion></circle>' % (7.2 - k * .45, 1 - k * .07, DUR, k * .22))
    s.append('<circle r="8.5" fill="url(#head)" stroke="#fff2b8" stroke-opacity=".8" filter="url(#glow)"><animateMotion dur="%ds" repeatCount="indefinite"><mpath href="#route"/></animateMotion></circle>' % DUR)
    # legend
    ly = Y0 + 7 * (CS + G) + 52
    s.append('<text x="%d" y="%d" class="m" font-size="10" fill="#8a8a6a">LESS</text>' % (X0, ly + 11))
    for i in range(5):
        s.append('<rect x="%d" y="%d" width="%d" height="%d" rx="3" fill="%s"/>' % (X0 + 38 + i * 20, ly, CS, CS, FILL[i]))
    s.append('<text x="%d" y="%d" class="m" font-size="10" fill="#8a8a6a">MORE</text>' % (X0 + 38 + 5 * 20 + 6, ly + 11))
    s.append('<text x="938" y="%d" text-anchor="end" class="m" font-size="10" letter-spacing="2" fill="#8a8a6a">github.com/%s</text>' % (ly + 11, E(A.USER)))
    s.append('<text x="500" y="%d" text-anchor="middle" class="m" font-size="10" letter-spacing="4" fill="#39ff6a" opacity=".8">THE SNAKE DEVOURS TIME. THE TIMELINE REGROWS.</text>' % (H - 22))
    s.append('<rect width="1000" height="%d" fill="url(#vig)"/></svg>' % H)
    return "".join(s)

if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    try:
        user = A.mock() if os.environ.get("ACTIVITY_MOCK") else A.fetch()
        svg = build(user)
    except Exception as e:
        print("snake.py error:", e, file=sys.stderr); svg = A.fallback(str(e))
    open(OUT, "w", encoding="utf-8").write(svg)
    print("wrote", OUT, len(svg), "bytes")
