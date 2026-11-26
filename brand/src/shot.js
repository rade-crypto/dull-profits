const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1600,height:1000},deviceScaleFactor:1});
await p.goto('file://'+path.join(__dirname,'preview.html'));await p.waitForTimeout(500);
await p.screenshot({path:path.join(__dirname,'..','logo-concepts.png'),fullPage:true});await b.close();})();
