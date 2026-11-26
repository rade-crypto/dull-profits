// Renders brand.html's SVGs to PNG with headless Chromium (uses locally installed Inter Display).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = __dirname, out = path.join(dir, '..');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2600, height: 5000 } });
  await page.goto('file://' + path.join(dir, 'brand.html'));
  await page.evaluate(() => document.fonts.ready);
  const files = { c1: 'profile-split.png', c2: 'profile-coin.png', c3: 'profile-monogram.png', wm: 'wordmark.png', ban: 'youtube-banner.png' };
  for (const [id, f] of Object.entries(files)) await page.locator('#' + id).screenshot({ path: path.join(out, f) });
  await browser.close();
})();
