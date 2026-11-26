const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const f of fs.readdirSync(__dirname).filter(f => f.endsWith('.html'))) {
    const thumb = f.startsWith('thumbnail');
    const p = await b.newPage({ viewport: thumb ? { width: 1280, height: 720 } : { width: 1920, height: 1080 } });
    await p.goto('file://' + path.join(__dirname, f)); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(__dirname, '..', f.replace('.html', '.png')) }); await p.close();
  }
  await b.close();
})();
