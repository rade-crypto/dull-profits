"""Generate example 1920x1080 frames for the Dull Profits visual style (render with render.js)."""
C = dict(bg="#1C1F24", bg2="#15171B", panel="#252932", ink="#F2EFE8", ink2="#B9BEC7", muted="#8B93A1", grid="#343944",
         tax="#6B7280", sup="#4C8DD6", pay="#D1679E", loc="#DB8230", own="#F2EFE8", cost="#C9A227", hl="#F5D547")

BASE = f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1920px;height:1080px;background:{C['bg']};color:{C['ink']};font-family:Inter,sans-serif;
     font-variant-numeric:tabular-nums;overflow:hidden;position:relative}}
.h{{font-family:'Inter Display',Inter,sans-serif;font-weight:900}}
.src{{position:absolute;left:116px;top:862px;font:600 36px Inter;letter-spacing:1px;color:{C['muted']};text-transform:uppercase}}
.src b{{color:{C['ink2']};font-weight:700}}
.title{{position:absolute;left:116px;top:104px;font-size:60px;font-weight:800;letter-spacing:-.5px}}
.kicker{{position:absolute;left:116px;top:56px;font:700 36px Inter;letter-spacing:3px;color:{C['muted']};text-transform:uppercase}}
</style></head><body>{{body}}</body></html>"""

def page(body): return BASE.replace("{body}", body)

# ---------- 1. The Split ----------
def split_frame():
    slices = [("TAX", 11, "tax"), ("SUPPLIER", 94, "sup"), ("CARD + SOFTWARE", 13, "pay"), ("LOCATION", 20, "loc"), ("YOU", 62, "own")]
    x0, W, y, H, gap = 116, 1688, 420, 150, 6
    unit = (W - gap * (len(slices) - 1)) / 200
    svg, labels, x = [], [], x0
    for i, (name, cents, k) in enumerate(slices):
        w = cents * unit
        r = 18
        svg.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{H}" rx="{r}" fill="{C[k]}"/>')
        cx = x + w / 2
        row = 0 if name in ("TAX", "LOCATION", "YOU") else 1
        ly = 630 if row == 0 else 755
        if name == "YOU":
            pass
        else:
            svg.append(f'<line x1="{cx:.1f}" y1="{y+H+10}" x2="{cx:.1f}" y2="{ly-44}" stroke="{C["grid"]}" stroke-width="3"/>')
            anchor = "middle"
            tx = cx
            if name == "TAX": anchor, tx = "start", x
            labels.append(f'<text x="{tx:.1f}" y="{ly}" text-anchor="{anchor}" font-size="40" font-weight="700" fill="{C["ink2"]}">{name}</text>'
                          f'<text x="{tx:.1f}" y="{ly+50}" text-anchor="{anchor}" font-size="44" font-weight="800" fill="{C["ink"]}">{cents}¢</text>')
        x += w + gap
    you_x = x0 + W - 62 * unit
    svg.append(f'<text x="{you_x + 62*unit/2:.1f}" y="{y+H/2+22}" text-anchor="middle" font-size="58" font-weight="900" fill="{C["bg"]}" font-family="Inter Display">YOU 62¢</text>')
    body = f"""
<div class="kicker">Follow the two dollars</div>
<div class="title">Where a $2.00 vending soda goes</div>
<div style="position:absolute;right:116px;top:60px;text-align:right">
  <div style="font:700 36px Inter;letter-spacing:3px;color:{C['muted']};text-transform:uppercase">Operator keeps</div>
  <div class="h" style="font-size:150px;line-height:1">$0.62</div>
</div>
<svg width="1920" height="1080" style="position:absolute;left:0;top:0" font-family="Inter">{''.join(svg)}{''.join(labels)}</svg>
<div class="src"><b>Source:</b> VMFS USA revenue-split model (6% tax, 10% commission)</div>"""
    return page(body)

# ---------- 2. Deal File ----------
def deal_frame():
    body = f"""
<svg width="1920" height="1080" style="position:absolute;left:0;top:0"><defs>
<filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .08 0"/></filter></defs>
<rect width="1920" height="1080" fill="{C['bg2']}"/><rect width="1920" height="1080" filter="url(#n)"/></svg>
<div class="kicker">The deal file</div>
<div style="position:absolute;left:250px;top:150px;width:1420px;padding:64px 80px;background:#EDE9E0;color:#22252B;
  transform:rotate(-1.2deg);box-shadow:0 30px 80px rgba(0,0,0,.55);font-family:'DejaVu Serif',Georgia,serif">
  <div style="font:700 34px Inter;letter-spacing:2px;color:#6B6F78;text-transform:uppercase;margin-bottom:34px">LAWA Board report · Feb 16, 2023 · excerpt (retyped)</div>
  <div style="font-size:48px;line-height:1.55">First Class will pay LAWA the greater of a minimum monthly guarantee of $100 per machine or
  <span style="background:linear-gradient(transparent 12%, {C['hl']}cc 12%, {C['hl']}cc 92%, transparent 92%);padding:0 6px;font-weight:700">59.5 percent of gross sales</span>
  over the five-year term and any approved options.</div>
</div>
<div class="src"><b>Source:</b> LA Board of Airport Commissioners, Feb 16 2023</div>"""
    return page(body)

# ---------- 3. Big number ----------
def big_frame():
    w = 1688
    body = f"""
<div class="kicker">Winner #1: the location</div>
<div style="position:absolute;left:116px;top:150px">
  <div class="h" style="font-size:300px;line-height:1;letter-spacing:-6px">59.5%</div>
  <div style="font-size:64px;font-weight:700;margin-top:10px">of every vending sale at LAX goes to the airport</div><div style="font-size:40px;color:#B9BEC7;margin-top:14px">or $100 per machine a month, whichever is more</div>
</div>
<svg width="1920" height="1080" style="position:absolute;left:0;top:0" font-family="Inter">
  <rect x="116" y="720" width="{w*0.595:.0f}" height="96" rx="16" fill="{C['loc']}"/>
  <rect x="{116 + w*0.595 + 6:.0f}" y="720" width="{w*0.405 - 6:.0f}" height="96" rx="16" fill="{C['own']}"/>
  <text x="140" y="782" font-size="40" font-weight="800" fill="{C['bg']}">AIRPORT 59.5%</text>
  <text x="{116 + w*0.595 + 30:.0f}" y="782" font-size="40" font-weight="800" fill="{C['bg']}">OPERATOR 40.5%</text>
</svg>
<div class="src"><b>Source:</b> LAX vending contract, Feb 16 2023</div>"""
    return page(body)

# ---------- 4. Comparison bars (single series) ----------
def compare_frame():
    rows = [("Vending machine", 2.01), ("Micro market", 3.02), ("Smart store", 4.49)]
    x0, maxw, y0 = 560, 1010, 300
    s = []
    for i, (name, v) in enumerate(rows):
        y = y0 + i * 165
        w = v / 4.49 * maxw
        s.append(f'<text x="{x0-36}" y="{y+68}" text-anchor="end" font-size="48" font-weight="700" fill="{C["ink"]}">{name}</text>')
        s.append(f'<rect x="{x0}" y="{y}" width="{w:.0f}" height="100" rx="8" fill="{C["sup"]}"/>')
        s.append(f'<text x="{x0 + w + 28:.0f}" y="{y+70}" font-size="64" font-weight="900" font-family="Inter Display" fill="{C["ink"]}">${v:.2f}</text>')
    body = f"""
<div class="kicker">Micro markets and smart stores</div>
<div class="title">Average purchase, 2025</div>
<svg width="1920" height="1080" style="position:absolute;left:0;top:0" font-family="Inter">
  <line x1="{x0}" y1="{y0-30}" x2="{x0}" y2="{y0+3*165-40}" stroke="{C['grid']}" stroke-width="3"/>{''.join(s)}</svg>
<div class="src"><b>Source:</b> Cantaloupe Micropayment Trends Report 2026</div>"""
    return page(body)

# ---------- 5. Operator's ledger ----------
def ledger_frame():
    rows = [("Two refurbished machines", "$3,200", ""), ("Starting stock", "$400", ""),
            ("Office machine (~50 staff)", "$280–350", "/mo sales"), ("Auto repair shop", "$120–180", "/mo sales"),
            ("Kept after gas, stock, repairs", "$130–150", "/mo")]
    trs = "".join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:26px 0;border-bottom:3px solid {C["grid"]};'
                  f'{"color:"+C["ink"]+";font-weight:800" if i==4 else ""}"><span style="font-size:48px">{a}</span>'
                  f'<span><span class="h" style="font-size:60px">{b}</span><span style="font-size:36px;color:{C["ink2"]}"> {c}</span></span></div>'
                  for i, (a, b, c) in enumerate(rows))
    body = f"""
<div class="kicker">A beginner's first six months</div>
<div class="title">One operator's ledger</div>
<div style="position:absolute;left:116px;top:200px;width:1688px">{trs}</div>
<div class="src"><b>Source:</b> self-reported on Reddit (via Benzinga, Jan 2026), unverified</div>"""
    return page(body)

# ---------- 6. Thumbnail (1280x720) ----------
def thumb():
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>*{{margin:0}}body{{width:1280px;height:720px;background:{C['bg']};
font-family:'Inter Display',Inter,sans-serif;color:{C['ink']};overflow:hidden;position:relative}}</style></head><body>
<div style="position:absolute;left:70px;top:70px;font-weight:900;font-size:120px;letter-spacing:-2px">$2.00 SODA</div>
<svg width="1280" height="720" style="position:absolute;left:0;top:0">
 <rect x="70" y="300" width="620" height="190" rx="22" fill="{C['sup']}"/>
 <rect x="700" y="300" width="70" height="190" rx="14" fill="{C['loc']}"/>
 <rect x="796" y="270" width="414" height="250" rx="26" fill="{C['own']}"/>
 <text x="1003" y="430" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="116" fill="{C['bg']}">62¢</text>
</svg>
<div style="position:absolute;left:796px;top:545px;width:414px;text-align:center;font-weight:900;font-size:64px">YOU</div>
</body></html>"""

# ---------- 7. TV layout guide ----------
def guide_frame():
    body = f"""
<svg width="1920" height="1080" style="position:absolute;left:0;top:0" font-family="Inter">
 <rect x="116" y="65" width="1688" height="853" fill="none" stroke="{C['sup']}" stroke-width="4" stroke-dasharray="18 12"/>
 <rect x="0" y="918" width="1920" height="162" fill="{C['loc']}" opacity=".22"/>
 <text x="960" y="1010" text-anchor="middle" font-size="40" font-weight="800" fill="{C['ink']}">BOTTOM 15%: keep clear (progress bar, captions, end screens)</text>
 <text x="140" y="110" font-size="36" font-weight="700" fill="{C['sup']}">SAFE AREA: 6% margin on every edge</text>
</svg>
<div style="position:absolute;left:170px;top:170px">
  <div class="h" style="font-size:160px;line-height:1">$0.62</div><div style="font-size:36px;color:{C['ink2']};margin-bottom:40px">Key number: 120–200 px</div>
  <div style="font-size:52px;font-weight:700">Labels and titles: 48–56 px</div><div style="font-size:36px;color:{C['ink2']};margin-bottom:40px">Inter, bold, tabular numbers</div>
  <div style="font-size:36px;font-weight:600">Smallest text anywhere: 36 px</div>
  <div style="font-size:36px;color:{C['ink2']};margin-top:40px">Off-white #F2EFE8 on charcoal #1C1F24 · one idea per screen · hold 4–8 s</div>
</div>"""
    return page(body)

frames = {"01-the-split": split_frame(), "02-deal-file": deal_frame(), "03-big-number": big_frame(),
          "04-comparison": compare_frame(), "05-operators-ledger": ledger_frame(), "06-tv-layout-guide": guide_frame()}
for k, v in frames.items(): open(f"{k}.html", "w").write(v)
open("thumbnail-concept.html", "w").write(thumb())
print("ok")
