// Render final-state frames of graphic scenes over a background frame. Usage: node stills.js jobs.json scenes.html
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2])); const page_url = 'file://' + process.argv[3];
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const j of jobs) {
    await p.goto(page_url); await p.evaluate(() => document.fonts.ready);
    if (j.bg) await p.evaluate(bg => { document.body.style.background = `#000 url(file://${bg}) center/cover no-repeat`; }, j.bg);
    if (j.scene) { await p.evaluate(sc => window.setup(sc), j.scene); await p.evaluate(t => window.draw(t), j.t); }
    await p.screenshot({ path: j.out });
  }
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
