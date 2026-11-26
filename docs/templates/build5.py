from pathlib import Path
import json
head = Path('templates2.html').read_text().split('<body class="S">')[0]
B = '../../episodes/01-vending-machines/render/stills'
M = json.load(open('/tmp/claude-0/-home-user-dull-profits/2d3a3f8e-aea6-5074-995c-c55aa0aa7c64/scratchpad/geo/map.json'))
def bg(n, extra=''): return f'<div class="bg" style="background-image:url({B}/{n}.jpg){extra}"></div>'
def foot(n): return f'<div class="a" style="inset:0;background:url({B}/{n}.jpg) center/cover"></div>'
sh = 'text-shadow:0 2px 12px rgba(0,0,0,.6),0 6px 40px rgba(0,0,0,.55)'
AP = '&#39;'
T = []
paths = ''.join(f'<path d="{s["d"]}" fill="rgba(255,255,255,.08)" stroke="rgba(255,255,255,.45)" stroke-width="1.5"/>' for s in M['all'])
pins = ''
for k, lab, dx, dy in [('LAX', 'LAX', -150, 10), ('Riverside', 'Riverside', 20, 50), ('Chicago', 'Chicago', 24, -20), ('Birmingham', 'Buffalo Rock', 24, 30)]:
    x, y = M['pts'][k]
    pins += f'<circle cx="{x}" cy="{y}" r="13" fill="#FFE14D"/><text x="{x+dx}" y="{y+dy}" fill="#fff" font-family="Libre Franklin, LF" font-weight="600" font-size="46">{lab}</text>'
T.append(f'{bg("bg-71")}<svg class="a" style="left:240px;top:110px" width="1440" height="920">{paths}{pins}</svg>')
x1, y1 = M['ca']['LAX']; x2, y2 = M['ca']['Riverside']
T.append(f'{bg("bg-05")}<svg class="a" style="left:160px;top:40px" width="760" height="1000"><path d="{M["ca"]["d"]}" fill="rgba(255,255,255,.1)" stroke="#fff" stroke-width="3"/><circle cx="{x1}" cy="{y1}" r="16" fill="#FFE14D"/><circle cx="{x2}" cy="{y2}" r="16" fill="#FFE14D"/></svg>'
         f'<div class="a" style="left:1000px;top:330px"><div class="sm">LAX</div><div class="num" style="font-size:150px">59.5%</div><div class="sm" style="margin-top:50px">Riverside college district</div><div class="num" style="font-size:150px">33%</div></div>')
T.append(f'<div class="a" style="left:0;top:0;width:960px;height:1080px;background:url({B}/bg-10.jpg) center/cover"></div><div class="a" style="left:960px;top:0;width:960px;height:1080px;background:url({B}/bg-47.jpg) 70% center/cover"></div>'
         f'<div class="a" style="left:957px;top:0;width:6px;height:1080px;background:#fff"></div>'
         f'<div class="a" style="left:110px;top:700px;{sh}"><div class="lab">Cash</div><div class="num" style="font-size:160px">$1.57</div></div>'
         f'<div class="a" style="left:1070px;top:700px;{sh}"><div class="lab">Card or phone</div><div class="num" style="font-size:160px">$2.45</div></div>')
T.append(f'{bg("bg-31")}<div class="a lab" style="left:120px;top:300px">How people paid, 2025</div>'
         f'<div class="a" style="left:120px;top:400px;width:1680px;height:130px;display:flex;gap:6px"><div style="flex:78;background:var(--pay)"></div><div style="flex:22;background:rgba(255,255,255,.85)"></div></div>'
         f'<div class="a" style="left:120px;top:570px"><div class="num" style="font-size:150px">78%</div><div class="sm">card or phone</div></div>'
         f'<div class="a" style="left:1440px;top:570px"><div class="num" style="font-size:150px">22%</div><div class="sm">cash</div></div>')
T.append(f'{foot("bg-34")}<div class="a" style="left:110px;top:90px;color:#0B1422"><div style="width:90px;height:5px;background:#0B1422;margin-bottom:22px"></div><div style="font:600 58px LF">Los Angeles International Airport</div><div class="sm" style="margin-top:8px;color:#0B1422">California</div></div>')
T.append(f'{foot("bg-50")}<div class="a" style="left:110px;top:100px;{sh}"><div class="num" style="font-size:110px">May 2026</div><div class="sm" style="margin-top:12px">365 Retail Markets closes its purchase of Cantaloupe</div></div>')
T.append(f'{bg("bg-17")}<div class="a lab" style="left:120px;top:200px">A typical site nets, per month</div>'
         f'<div class="a" style="left:120px;top:520px;width:1680px;height:4px;background:rgba(255,255,255,.4)"></div>'
         + ''.join(f'<div class="a sm" style="left:{120+1680*v/200-30}px;top:580px">${v}</div>' for v in (0, 50, 100, 150, 200)) +
         f'<div class="a" style="left:{120+1680*20/200}px;top:490px;width:{1680*155/200}px;height:64px;background:var(--loc)"></div>'
         f'<div class="a num" style="left:{120+1680*20/200}px;top:330px;font-size:130px">$20</div><div class="a num" style="left:{120+1680*175/200-200}px;top:330px;font-size:130px">$175</div>')
ticks = ''.join(f'<div class="a" style="left:{160+1600*k/4-2}px;top:600px;width:4px;height:40px;background:#fff"></div><div class="a sm" style="left:{160+1600*k/4-25}px;top:660px">{k}×</div>' for k in range(5))
T.append(f'{bg("bg-70")}<div class="a lab" style="left:160px;top:180px">What vending routes sell for</div><div class="a" style="left:160px;top:618px;width:1600px;height:4px;background:rgba(255,255,255,.6)"></div>{ticks}'
         f'<div class="a" style="left:{160+800-14}px;top:592px;width:28px;height:56px;background:var(--sup)"></div><div class="a" style="left:{160+800-150}px;top:390px;width:300px;text-align:center"><div class="num" style="font-size:120px">≈2×</div><div class="sm">typical sale</div></div>'
         f'<div class="a" style="left:{160+1600*2.8/4-14}px;top:592px;width:28px;height:56px;background:var(--loc)"></div><div class="a" style="left:{160+1600*2.8/4-150}px;top:740px;width:300px;text-align:center"><div class="num" style="font-size:120px">2.8×</div><div class="sm">Chicago listing</div></div>')
cells = ''.join(f'<div style="width:46px;height:46px;{"background:#fff" if i < 20 else "border:3px solid var(--loc)"}"></div>' for i in range(168))
T.append(f'{bg("bg-24")}<div class="a" style="left:120px;top:150px;display:grid;grid-template-columns:repeat(14,46px);gap:12px">{cells}</div>'
         f'<div class="a" style="left:1080px;top:200px"><div class="num" style="font-size:120px">20 months</div><div class="sm" style="margin-top:10px">to pay off at a good site</div>'
         f'<div class="num" style="font-size:120px;margin-top:80px">14 years</div><div class="sm" style="margin-top:10px">at a weak one</div></div>')
T.append(f'{bg("bg-42")}<svg class="a" style="left:460px;top:80px" width="1000" height="920"><circle cx="360" cy="330" r="250" fill="rgba(22,153,138,.35)" stroke="#16998A" stroke-width="5"/><circle cx="640" cy="330" r="250" fill="rgba(79,126,194,.35)" stroke="#4F7EC2" stroke-width="5"/><circle cx="500" cy="570" r="250" fill="rgba(184,142,48,.35)" stroke="#B88E30" stroke-width="5"/></svg>'
         f'<div class="a lab" style="left:620px;top:330px">Location</div><div class="a lab" style="left:1110px;top:330px">Scale</div><div class="a lab" style="left:840px;top:760px">Technology</div>')
T.append(f'<div class="a" style="inset:0;background:#0A111D"></div>'
         f'<div class="a" style="left:160px;top:220px;width:1000px;background:#F7F8F5;color:#111827;padding:50px 60px;font:400 46px LCT;line-height:1.5;transform:rotate(-1deg);box-shadow:0 30px 80px rgba(0,0,0,.5)"><div style="font:700 46px LF;margin-bottom:20px">LA Board of Airport Commissioners</div>First Class will pay LAWA the greater of $100 per machine or <span style="background:#FFE14D">59.5 percent of gross sales</span>.</div>'
         f'<svg class="a" style="left:0;top:0" width="1920" height="1080"><line x1="800" y1="560" x2="1230" y2="520" stroke="#fff" stroke-width="3"/></svg>'
         f'<div class="a" style="left:1200px;top:240px;width:600px;height:600px;border-radius:50%;background:#F7F8F5;border:8px solid #fff;color:#111827;display:flex;align-items:center;justify-content:center;text-align:center;font:400 96px LCT;line-height:1.15;box-shadow:0 30px 80px rgba(0,0,0,.5)"><span style="background:#FFE14D;padding:0 10px">59.5<br>percent</span></div>')
T.append(f'{bg("bg-07",";filter:blur(14px) brightness(.4)")}<div class="a" style="left:160px;top:180px;width:760px"><div class="lab" style="margin-bottom:40px">The pitch</div>'
         + ''.join(f'<div class="num" style="font-size:72px;margin:28px 0;text-decoration:line-through;text-decoration-color:#FFE14D;text-decoration-thickness:6px">{t}</div>' for t in ('Easy money', 'Once a week', 'Passive')) +
         f'</div><div class="a" style="left:958px;top:180px;width:4px;height:700px;background:rgba(255,255,255,.5)"></div><div class="a" style="left:1060px;top:180px;width:760px"><div class="lab" style="margin-bottom:40px">The reality</div>'
         + ''.join(f'<div class="num" style="font-size:72px;margin:28px 0">{t}</div>' for t in ('$130–150 a month', 'Weekly route', 'Repairs, gas, debt')) + '</div>')
seg = [('var(--tax)', 11, 'Tax 11¢'), ('var(--sup)', 94, 'Drink company 94¢'), ('var(--pay)', 13, 'Cards 13¢'), ('var(--loc)', 20, 'Building 20¢'), ('#fff', 62, 'Owner 62¢')]
segs, labs, y = '', '', 0
labs_y = []
for col, c, lab in seg:
    h = 760 * c / 200
    segs += f'<div style="height:{h-4}px;margin-bottom:4px;background:{col}"></div>'
    ty = max(170 + y + h/2 - 28, (labs_y[-1] + 70) if labs_y else 0); labs_y.append(ty)
    labs += f'<div class="a sm" style="left:1080px;top:{ty}px">{lab}</div>'
    y += h
T.append(f'{bg("bg-20")}<div class="a" style="left:700px;top:150px;width:320px;height:800px;border:6px solid #fff;border-radius:40px 40px 30px 30px;padding:14px;overflow:hidden"><div style="height:100%;display:flex;flex-direction:column">{segs}</div></div>{labs}'
         f'<div class="a" style="left:160px;top:420px"><div class="num" style="font-size:170px">$2.00</div><div class="sm">one soda</div></div>')
T.append(f'{bg("bg-28")}<div class="a" style="left:160px;top:330px"><div class="lab">That airport{AP}s cut</div><div style="font:600 280px LF;line-height:1.1;margin-top:10px">?%</div></div>')
tiles = [('bg-12', 'Office', '$150–700'), ('x-hospital', 'Hospital', '$2,000+'), ('x-factory', 'Factory', '$2,000+'), ('bg-18', 'Transit hub', '$2,000+')]
T.append('<div class="a" style="left:110px;top:120px;font:600 50px LF">Monthly sales by location</div>' + ''.join(
    f'<div class="a" style="left:{110 + i*440}px;top:220px;width:400px"><div style="height:420px;background:url({B}/{f}.jpg) center/cover"></div><div class="sm" style="margin-top:24px">{lab}</div><div class="num" style="font-size:96px;margin-top:6px">{v}</div></div>' for i, (f, lab, v) in enumerate(tiles)))
T.append(''.join(f'<div class="a" style="left:{180 + i*540}px;top:90px;width:480px;height:854px;background:url({B}/{f}.jpg) {pos} center/cover"></div>' for i, (f, pos) in enumerate([('bg-01', '45%'), ('bg-77', '55%'), ('bg-57', '40%')])) +
         '<div class="a sm" style="left:180px;top:975px">How vending gets pitched online</div>')
T.append(f'{bg("bg-48")}<div class="a" style="left:160px;top:240px"><div class="sm">Cantaloupe handled</div><div class="num" style="font-size:170px">$4.6 billion</div>'
         f'<div class="sm" style="margin-top:60px">That{AP}s about</div><div class="num" style="font-size:170px;color:#FFE14D">2.3 billion</div><div class="lab" style="margin-top:6px">$2 sodas</div></div>')
T.append(f'{bg("bg-83",";filter:blur(6px) brightness(.5)")}<div class="a" style="left:160px;top:330px"><div class="lab">Next</div><div class="num" style="font-size:220px;margin-top:10px">The car wash</div><div class="sm" style="margin-top:30px">What one wash really costs, and who gets paid</div></div>')
body = '<body class="S">' + ''.join(f'<div class="f" id="x{i+1}">{t}</div>\n' for i, t in enumerate(T)) + '</body></html>'
body = body.replace(' LF"', " 'LF'\"").replace(' LF;', " 'LF';").replace(' LCT;', " 'LCT';").replace(' LCT"', " 'LCT'\"")
Path('templates5.html').write_text(head + body)
print(len(T))
