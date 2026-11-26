// Grab frames of the preview page at given times (seconds), graphics and footage exactly as the viewer sees them.
//   NODE_PATH=$(npm root -g) node tools/video/review/frames.js OUT_DIR 12.5 13 13.5 ...
const { chromium } = require('playwright');
(async () => {
  const [out, ...ts] = process.argv.slice(2); require('fs').mkdirSync(out, { recursive: true });
  const root = __dirname + '/../../../episodes/01-vending-machines/render/player/';
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.route('http://player.test/**', r => r.fulfill({ path: root + decodeURIComponent(new URL(r.request().url()).pathname.slice(1)) }));
  await p.goto('http://player.test/index.html', { waitUntil: 'networkidle' }); await p.waitForTimeout(800);
  await p.evaluate(() => { Object.defineProperty(audio, 'currentTime', { get() { return window.__t || 0; }, set(v) { window.__t = v; }, configurable: true }); });
  for (const t of ts) {
    await p.evaluate(t => { window.__t = +t; cur = -1; }, t); await p.waitForTimeout(700);
    await p.locator('#screen').screenshot({ path: `${out}/t${(+t).toFixed(2).padStart(7, '0')}.jpg`, type: 'jpeg', quality: 80 });
  }
  if (errs.length) console.log('page errors:', errs); await b.close();
})();
