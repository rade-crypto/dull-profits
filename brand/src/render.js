// Renders brand.html to PNG with headless Chromium (Source Serif 4 from Google Fonts, Inter installed locally).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = __dirname, out = path.join(dir, '..');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2600, height: 3000 } });
  await page.goto('file://' + path.join(dir, 'brand.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const ok = await page.evaluate(() => document.fonts.check("600 100px 'Source Serif 4'"));
  if (!ok) throw new Error('Source Serif 4 did not load');
  const files = { pfp: 'profile-picture.png', wm: 'wordmark.png', ban: 'youtube-banner.png' };
  for (const [id, f] of Object.entries(files)) await page.locator('#' + id).screenshot({ path: path.join(out, f) });
  await browser.close();
})();
