const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + __dirname + '/templates3.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  for (let i = 1; i <= 8; i++) await p.locator('#v' + i).screenshot({ path: __dirname + `/v${i}.jpg`, type: 'jpeg', quality: 85 });
  await b.close();
})();
