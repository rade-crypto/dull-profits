// Render animated graphics to PNG sequences. Usage: node render_gfx.js jobs.json scenes.html
// job: {scene, frames, fps, dir, transparent}. Frames where nothing moves are copied instead of re-rendered.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2])); const url = 'file://' + process.argv[3];
  const b = await chromium.launch(); const queue = [...jobs];
  async function worker() {
    const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
    while (queue.length) {
      const j = queue.shift(); fs.mkdirSync(j.dir, { recursive: true });
      await p.goto(url); await p.evaluate(() => document.fonts.ready);
      await p.evaluate(sc => window.setup(sc), j.scene);
      let prevKey = null, prevFile = null;
      for (let f = 0; f < j.frames; f++) {
        const key = await p.evaluate(t => window.draw(t), f / j.fps);
        const file = path.join(j.dir, String(f).padStart(5, '0') + '.png');
        if (key === prevKey) fs.copyFileSync(prevFile, file);
        else await p.screenshot({ path: file, omitBackground: !!j.transparent });
        prevKey = key; prevFile = file;
      }
      console.log('gfx', path.basename(j.dir), j.frames);
    }
    await p.close();
  }
  await Promise.all([worker(), worker(), worker()]);
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
