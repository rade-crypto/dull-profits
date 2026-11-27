// node firstvis.js in.json out.json : for each {n, scene, dur}, the first time (s) anything of the graphic is visible.
// Used to start a graphic background's focus pull when its first text or shape appears, not at the cut.
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2])); const out = {};
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  const url = 'file://' + path.join(__dirname, 'gfx', 'scenes.html');
  for (const j of jobs) {
    await p.goto(url); await p.evaluate(() => document.fonts.ready); await p.evaluate(sc => window.setup(sc), j.scene);
    out[j.n] = await p.evaluate(dur => {
      const els = [...document.querySelectorAll('#stage *')].filter(e => {
        const cs = getComputedStyle(e), tag = e.tagName.toLowerCase();
        const own = (e.childElementCount === 0 && e.textContent.trim()) || ['svg', 'img', 'path', 'circle', 'line', 'rect', 'g'].includes(tag)
          || (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== 'transparent') || cs.backgroundImage !== 'none' || parseFloat(cs.borderTopWidth) > 0;
        return own; });
      const vis = e => { const r = e.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return false;
        if (r.right < 0 || r.bottom < 0 || r.left > 1920 || r.top > 1080) return false;
        let o = 1; for (let x = e; x && x !== document.documentElement; x = x.parentElement) { const cs = getComputedStyle(x);
          o *= +cs.opacity; if (cs.display === 'none' || cs.visibility === 'hidden') return false;
          const m = cs.clipPath.match(/inset\(\S+ ([\d.]+)%/); if (m && +m[1] >= 99.5) return false; }
        return o > 0.05; };
      for (let f = 0; f / 30 < dur; f++) { window.draw(f / 30); if (els.some(vis)) return +(f / 30).toFixed(3); }
      return dur; }, j.dur);
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out)); await b.close();
})();
