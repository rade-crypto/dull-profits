// Screenshot every sheet-*.html in a folder to a PNG. Usage: node sheets.js DIR
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const dir = process.argv[2]; const b = await chromium.launch();
  for (const f of fs.readdirSync(dir).filter(f => /^sheet-\d+\.html$/.test(f))) {
    const p = await b.newPage({ viewport: { width: 1920, height: 1000 }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.join(dir, f)); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(dir, f.replace('.html', '.png')), fullPage: true }); await p.close();
  }
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
