#!/usr/bin/env python3
"""Builds a TVA-themed 'Timeline Activity' SVG from your real GitHub data.
Runs inside the GitHub Action (uses the built-in GITHUB_TOKEN, no extra setup).
Usage: python scripts/activity.py dist/activity.svg
Set ACTIVITY_MOCK=1 to preview the layout with random sample data."""
import os, sys, json, math, random, datetime, urllib.request
from html import escape as E

USER  = os.environ.get("GH_USER") or os.environ.get("GITHUB_REPOSITORY_OWNER") or "Arun597134"
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
OUT   = sys.argv[1] if len(sys.argv) > 1 else "activity.svg"
QUERY = """query($login:String!){user(login:$login){
 repositories(ownerAffiliations:OWNER,isFork:false,first:100){totalCount nodes{languages(first:6,orderBy:{field:SIZE,direction:DESC}){edges{size node{name}}}}}
 contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount contributionLevel}}}}}}"""

def fetch():
    req = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": "bearer " + TOKEN, "Content-Type": "application/json", "User-Agent": "tva-activity"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    if "errors" in d or not d.get("data", {}).get("user"):
        raise RuntimeError(json.dumps(d.get("errors", d))[:300])
    return d["data"]["user"]

def mock():
    random.seed(4); today = datetime.date.today(); start = today - datetime.timedelta(days=364)
    days = []
    for i in range(365):
        dt = start + datetime.timedelta(days=i)
        c = max(0, int(random.gauss(3, 4)) if random.random() > .35 else 0)
        lv = "NONE" if c == 0 else "FIRST_QUARTILE" if c < 3 else "SECOND_QUARTILE" if c < 6 else "THIRD_QUARTILE" if c < 10 else "FOURTH_QUARTILE"
        days.append({"date": dt.isoformat(), "contributionCount": c, "contributionLevel": lv})
    weeks = [{"contributionDays": days[i:i+7]} for i in range(0, 365, 7)]
    langs = [("Python", 520), ("JavaScript", 340), ("Java", 180), ("HTML", 90), ("CSS", 60)]
    return {"repositories": {"totalCount": 14, "nodes": [{"languages": {"edges": [{"size": s, "node": {"name": n}} for n, s in langs]}}]},
            "contributionsCollection": {"contributionCalendar": {"totalContributions": sum(d["contributionCount"] for d in days), "weeks": weeks}}}

def tube(d, w=6, pid=None, dark="#05401a", mid="#17d159", high="#d9ffe5", op=1):
    i = ' id="%s"' % pid if pid else ""
    return ('<g opacity="%s" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="%s" stroke="%s" stroke-width="%s"/>'
            '<path%s d="%s" stroke="%s" stroke-width="%s" filter="url(#glow)"/><path d="%s" stroke="%s" stroke-width="%.1f" transform="translate(-1,-1.5)" opacity=".8"/></g>'
            ) % (op, d, dark, w + 5, i, d, mid, w, d, high, max(w * .22, 1))

def smooth(pts):
    d = "M%.1f %.1f" % pts[0]
    for i in range(len(pts) - 1):
        p0 = pts[max(i - 1, 0)]; p1 = pts[i]; p2 = pts[i + 1]; p3 = pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += " C%.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p2)
    return d

def build(u, synced=True):
    cal = u["contributionsCollection"]["contributionCalendar"]
    weeks = cal["weeks"]; total = cal["totalContributions"]
    days = [d for w in weeks for d in w["contributionDays"]]
    today = datetime.date.today().isoformat()
    days = [d for d in days if d["date"] <= today]
    wk = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in weeks]
    longest = cur = 0
    for d in days:
        cur = cur + 1 if d["contributionCount"] > 0 else 0; longest = max(longest, cur)
    cur = 0
    for i, d in enumerate(reversed(days)):
        if d["contributionCount"] > 0: cur += 1
        elif i == 0: continue
        else: break
    best = max((d["contributionCount"] for d in days), default=0)
    # languages
    agg = {}
    for r in u["repositories"]["nodes"]:
        for e in r["languages"]["edges"]: agg[e["node"]["name"]] = agg.get(e["node"]["name"], 0) + e["size"]
    langs = sorted(agg.items(), key=lambda x: -x[1])[:6]; ltot = sum(v for _, v in langs) or 1

    x0, x1, yt, yb = 70, 930, 120, 290
    maxv = max(max(wk), 4); n = len(wk)
    pts = [(x0 + i * (x1 - x0) / max(n - 1, 1), yb - (v / maxv) * (yb - yt)) for i, v in enumerate(wk)]
    line = smooth(pts)
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 610" width="1000" height="610">']
    s.append('''<defs><filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1307"/><stop offset="1" stop-color="#050805"/></linearGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#39ff6a" stop-opacity=".38"/><stop offset="1" stop-color="#39ff6a" stop-opacity="0"/></linearGradient>
<linearGradient id="card" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1f3224"/><stop offset="1" stop-color="#0a110c"/></linearGradient>
<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".2"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="sph" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#fff"/><stop offset=".3" stop-color="#7dffa3"/><stop offset=".7" stop-color="#16c653"/><stop offset="1" stop-color="#05381a"/></radialGradient>
<radialGradient id="vig" cx=".5" cy=".5" r=".78"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".5"/></radialGradient>
<clipPath id="chart"><rect x="60" y="100" width="880" height="200"/></clipPath></defs>
<style>.m{font-family:"Courier New",Courier,monospace}</style>''')
    s.append('<rect width="1000" height="610" fill="url(#bg)"/>')
    s.append('<text x="500" y="34" text-anchor="middle" class="m" font-size="14" letter-spacing="8" fill="#e07a14">TIMELINE ACTIVITY // LAST 12 MONTHS</text>')
    s.append('<text x="500" y="56" text-anchor="middle" class="m" font-size="11" letter-spacing="4" fill="#39ff6a">VARIANT: %s</text>' % E(USER.upper()))
    for k in range(5):
        y = yb - k * (yb - yt) / 4
        s.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#39ff6a" stroke-opacity=".14"/><text x="58" y="%.1f" text-anchor="end" class="m" font-size="10" fill="#8a8a6a">%d</text>' % (x0, y, x1, y, y + 3, round(maxv * k / 4)))
    last = None
    for i, w in enumerate(weeks):
        dt = datetime.date.fromisoformat(w["contributionDays"][0]["date"])
        if dt.month != last:
            last = dt.month
            s.append('<text x="%.1f" y="%d" text-anchor="middle" class="m" font-size="10" fill="#e07a14">%s</text>' % (pts[i][0], yb + 18, dt.strftime("%b").upper()))
    s.append('<g clip-path="url(#chart)"><path d="%s L%.1f %d L%.1f %d Z" fill="url(#area)"/></g>' % (line, x1, yb, x0, yb))
    s.append(tube(line, 5, "wire"))
    s.append('<path d="%s" pathLength="1000" fill="none" stroke="#f3fff6" stroke-width="3" stroke-dasharray="40 960" filter="url(#glow)"><animate attributeName="stroke-dashoffset" from="1000" to="0" dur="5s" repeatCount="indefinite"/></path>' % line)
    s.append('<circle r="5" fill="#fff" filter="url(#glow)"><animateMotion dur="8s" repeatCount="indefinite"><mpath href="#wire"/></animateMotion></circle>')
    for i in sorted(range(n), key=lambda i: -wk[i])[:3]:
        if wk[i] == 0: continue
        px, py = pts[i]
        s.append('<circle cx="%.1f" cy="%.1f" r="8" fill="url(#sph)" filter="url(#glow)"/><text x="%.1f" y="%.1f" text-anchor="middle" class="m" font-size="12" font-weight="bold" fill="#ffd98a">%d</text>' % (px, py, px, py - 14, wk[i]))
    # stat plates
    plates = [("TOTAL CONTRIBUTIONS", total), ("CURRENT STREAK", "%d days" % cur), ("LONGEST STREAK", "%d days" % longest), ("BEST DAY", best)]
    for i, (lab, val) in enumerate(plates):
        x = 60 + i * 225; y = 340; w = 205; h = 80
        for k in range(8, 0, -1): s.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="10" fill="%s"/>' % (x + k * .9, y + k * 1.1, w, h, "#04200d" if k > 4 else "#073817"))
        s.append('<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -4;0 0" dur="%ds" begin="-%d" repeatCount="indefinite"/>' % (4 + i, i))
        s.append('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="url(#card)" stroke="#39ff6a" stroke-width="1.5" filter="url(#glow)"/><rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="url(#gloss)"/>' % (x, y, w, h, x, y, w, h))
        s.append('<text x="%d" y="%d" text-anchor="middle" class="m" font-size="28" font-weight="bold" fill="#ecd9a8">%s</text><text x="%d" y="%d" text-anchor="middle" class="m" font-size="10" letter-spacing="2" fill="#39ff6a">%s</text></g>' % (x + w / 2, y + 42, E(str(val)), x + w / 2, y + 64, lab))
    # languages
    s.append('<text x="60" y="458" class="m" font-size="12" letter-spacing="5" fill="#e07a14">TECH FREQUENCY // TOP LANGUAGES</text>')
    cols = ["#39ff6a", "#ff9a2e", "#ffd98a", "#17b8a6", "#c4581a", "#9dffb8"]
    bx = 60; by = 474; bw = 880; bh = 26
    for k in range(6, 0, -1): s.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="6" fill="#04200d"/>' % (bx + k * .8, by + k * 1.0, bw, bh))
    cx = bx; leg = []
    for i, (name, size) in enumerate(langs):
        wseg = bw * size / ltot
        s.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" opacity=".92"/><rect x="%.1f" y="%d" width="%.1f" height="9" fill="#fff" opacity=".2"/>' % (cx, by, max(wseg - 2, 1), bh, cols[i], cx, by, max(wseg - 2, 1)))
        leg.append((name, size / ltot * 100, cols[i])); cx += wseg
    s.append('<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="none" stroke="#39ff6a" stroke-opacity=".6"/>' % (bx, by, bw, bh))
    lx = 60
    for name, pct, col in leg:
        s.append('<rect x="%d" y="522" width="12" height="12" rx="3" fill="%s"/><text x="%d" y="532" class="m" font-size="12" fill="#eaf5ea">%s %.1f%%</text>' % (lx, col, lx + 18, E(name), pct))
        lx += 22 + len(name) * 7.4 + 62
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    s.append('<text x="500" y="580" text-anchor="middle" class="m" font-size="10" letter-spacing="3" fill="#8a8a6a">LAST SYNC %s · github.com/%s</text>' % (stamp, E(USER)))
    s.append('<rect width="1000" height="610" fill="url(#vig)"/></svg>')
    return "".join(s)

def fallback(msg):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 200" width="1000" height="200"><rect width="1000" height="200" fill="#0a0d0a" stroke="#39ff6a"/>'
            '<text x="500" y="90" text-anchor="middle" font-family="monospace" font-size="18" fill="#ecd9a8">TIMELINE SYNC FAILED</text>'
            '<text x="500" y="124" text-anchor="middle" font-family="monospace" font-size="12" fill="#39ff6a">%s</text></svg>') % E(msg[:110])

if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    try:
        user = mock() if os.environ.get("ACTIVITY_MOCK") else fetch()
        svg = build(user)
    except Exception as e:
        print("activity.py error:", e, file=sys.stderr); svg = fallback(str(e))
    open(OUT, "w", encoding="utf-8").write(svg)
    print("wrote", OUT, len(svg), "bytes")
