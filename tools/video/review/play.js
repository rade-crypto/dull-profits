// Play the preview in real time from T0 for SPAN seconds and grab frames as fast as possible (catches flashes/jumps at cuts).
//   NODE_PATH=$(npm root -g) node tools/video/review/play.js OUT_DIR T0 SPAN
const { chromium } = require('playwright');
(async () => {
  const [out, t0, span] = process.argv.slice(2); require('fs').mkdirSync(out, { recursive: true });
  const root = __dirname + '/../../../episodes/01-vending-machines/render/player/';
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 960, height: 760 } });
  await p.route('http://player.test/**', r => r.fulfill({ path: root + decodeURIComponent(new URL(r.request().url()).pathname.slice(1)) }));
  await p.goto('http://player.test/index.html', { waitUntil: 'networkidle' }); await p.waitForTimeout(800);
  await p.evaluate(t0 => { const st = performance.now(); Object.defineProperty(audio, 'currentTime', { get() { return +t0 + (performance.now() - st) / 1000; }, set() {}, configurable: true }); cur = -1; playing = true; }, t0);
  const start = Date.now();
  while (Date.now() - start < span * 1000) { const t = await p.evaluate(() => audio.currentTime); await p.locator('#screen').screenshot({ path: `${out}/p${t.toFixed(2).padStart(7, '0')}.jpg`, type: 'jpeg', quality: 60 }); }
  await b.close();
})();
