# Channel Strategy and Visuals: Research Report

**Prepared:** 2026-11-26
**For:** a faceless YouTube channel about buying, owning and selling "boring" small businesses, with AI TTS male narration and an audience aged 40 to 65+ who have capital
**Episode 1:** "Follow the two dollars" (vending), about 1,393 words. That runs about 9.5 to 10.5 minutes at 135 to 145 wpm, or about 11 minutes at a slow 125 to 130 wpm.

How sourcing works in this report:
- Claims tagged **[S]** were checked against a live source during this session. URLs are in the Sources section at the end.
- Claims tagged **[K]** come from standing knowledge of official license pages that I did not re-fetch today. Re-check those pages before relying on them.
- Descriptions of channels' pacing and thumbnails are my own viewing observations, not measured data.

---

## Bottom line (read this first)

1. **Visual approach.** Use a "documents + diagrams" style, modeled on Wall Street Millennial's filings-on-screen and Modern MBA's slide-style explainers, rather than the cinematic archive style of Magnates Media.
   - Most screen time goes to motion graphics you build yourself (numbers, bars, maps) and highlighted primary-source documents (FTC releases, city contracts, payment-network reports).
   - Stock footage fills in, roughly 25 to 35% of runtime, as breathing room.
   - This style costs nothing, carries no claim risk, and suits a skeptical older audience. It is also the clearest defense against YouTube's "inauthentic/template" demonetization category, because every graphic is unique to its episode's research.
2. **Signature device: "The Split."** Each episode opens on one real transaction, such as a $2 soda, a $15 car wash, a $4.75 laundromat load or a $9,000 funeral. A horizontal money bar (or a paper receipt) slices that amount into labeled segments for tax, supplier, payments, location, labor and owner.
   - The segment colors stay the same across the whole series.
   - A small "Owner's Tally" coin counter in one corner counts down as each slice is taken.
   - Pair it with **"The Deal File"**: a primary-source document on a desk-texture background, with a yellow highlighter sweep and a fixed "SOURCE:" tag in the lower left.
   - These two devices are the channel's brand.
3. **Tool stack at $0** (licenses in section B):
   - Editing: Kdenlive or DaVinci Resolve (free).
   - Data animation: Motion Canvas (MIT) or Manim (MIT). Remotion is free only for individuals and companies of up to 3 people [S].
   - Graphics: Inkscape, GIMP and Canva Free.
   - Stock: Pexels, Pixabay and Coverr, plus Prelinger/Internet Archive and US federal public-domain material.
   - Maps: QGIS with Natural Earth (public domain) and Census TIGER, plus OpenStreetMap with visible attribution [S].
   - Music: YouTube Audio Library.
   - Sound effects: Freesound CC0 only.
   - Fonts: Google Fonts (Inter or IBM Plex Sans).
   - **Avoid CapCut** as the main editor because of its broad user-content license [S] and its paywall creep.
4. **Monetization reality.**
   - Today the YouTube Partner Program needs 1,000 subscribers plus either 4,000 watch hours in 12 months or 10M Shorts views in 90 days [S].
   - **From February 1, 2027, new applicants need 8,000 watch hours in 365 days, or 20M Shorts views in 90 days** [S]. A channel launching now will almost certainly face the 8,000-hour bar.
   - Realistic time to monetization is 12 to 24+ months at two videos a month, and many channels never get there.
   - Expected RPM for US business/finance explainers is roughly $8 to $15 at first, rising toward $15 to $25 with a strongly US, older, B2B-leaning audience [S, third-party estimates].
   - Sponsors such as accounting, POS, lending and business marketplaces are likely to be worth more than AdSense.
5. **AI voice.** A generic TTS narrator voice that imitates no real person is **not** on YouTube's list of content that must be disclosed [S].
   - Still add a plain line in the description, for example "Narration uses a synthetic voice; researched and written by [channel]."
   - Never build an "AI persona" presented as a real advisor, because finance is a named sensitive topic in YouTube's July 2026 clarification [S].

---

## A) Visuals

### A1. Comparable channels

Subscriber counts are third-party tracker snapshots from 2025 to 2026 and are approximate.

| Channel | Approx. size | Visual style | Pacing and motifs (observed) | Thumbnail style (observed) |
|---|---|---|---|---|
| **Modern MBA** | ~800K subs; 63 videos, so very high views per video [S] | Slide-style animation with analytical voiceover [S]: clean diagrams, company logos, charts, some stock | Measured and dense; long videos (20 to 40 min); diagrams build up piece by piece; few cuts per minute. Sponsors include NetSuite and Zapier [S] | Product or logo object plus 2 to 4 words; clean, uncluttered |
| **PolyMatter** | ~1.9M subs, 188 videos [S] | Flat 2D vector illustration, maps, a tightly limited palette | Calm, essayistic; ~10 to 15 min; consistent illustration language is the brand | One illustrated subject, 1 to 3 words, a lot of negative space |
| **Wendover Productions** | ~4.9M subs [S] | Animated maps, motion graphics, stock plus some original footage | Logistics and aviation explainers, 15 to 30 min; maps carry the argument; steady, unhurried narration | Real object photo with a simple graphic overlay (arrow, route line) |
| **Company Man** | ~1.8M subs [S] | Stock photos and simple logo animations [S]; Ken Burns pans | Fast publishing cadence; straightforward "what happened to X" narration; the lowest production cost of this group | Storefront or logo photo plus a short question |
| **How Money Works** | ~1.7M subs [S] | Motion graphics over conversational narration [S]; kinetic type and charts | Brisker cuts; heavy use of on-screen text | Bold text plus an object, high-saturation colors |
| **Business Casual** | ~1.1M+ subs (snapshot) [S] | Custom 2D animation, narrative storytelling [S] | Character-driven; costly to produce | Cartoon illustration |
| **MagnatesMedia** | ~1.9M subs, 255 videos [S] | Animated maps, archive footage, dramatic narration [S] | Cinematic rise-and-fall; tense music; **the wrong tone for this audience** | Founder face plus dramatic text |
| **Wall Street Millennial** | ~366K subs, but high estimated revenue ($10K to $32K/mo) [S] | Charts, filings and screen-recorded data [S] | Deadpan and document-led; very cheap to make | Ticker or logo plus a blunt claim |
| **ColdFusion** | ~5.2M subs [S] | Cinematic B-roll, calm narration, restrained on-screen text [S] | A tone model for "calm and credible" | Moody photo, minimal text |
| **Logically Answered** | ~912K subs [S] | Stock footage with research-led narration [S] | Mostly stock; average views are low relative to subscribers (176K) [S], a warning about generic stock | Stock image plus a question |
| **Codie Sanchez / Contrarian Thinking** (on camera; the closest topical comparison) | ~1.75M subs, average video ~19 min (Apr 2025) [S] | A human host: talking head, interviews, field visits | High energy, "wealth" framing. **This leaves an opening for a calm, numbers-first, no-hype alternative** | Face plus bold dollar figures |

Findings that matter for this channel:
- **Business-documentary channels converge on 9 to 12 minutes and 1,400 to 1,800 words** [S, OutlierKit]. Episode 1 (1,393 words) is in range.
- OutlierKit names three common failures [S]:
  1. Spending the first 30 seconds on an intro.
  2. Summarizing instead of telling events in sequence.
  3. Relying on unlicensed news clips.
- OutlierKit also finds that **primary-source research beats production budget**, and that **motion graphics you make yourself are the strongest differentiator and carry no claim risk** [S].
- **No faceless channel clearly owns the "boring business economics with real numbers" niche.** The searches turned up mostly face-on creators (Codie Sanchez), podcasts, and marketplaces selling faceless YouTube channels themselves [S]. That is a real gap.
- One note on the episode-1 ending: "how car washes became money machines" leans slightly toward hype. "How the car wash business really makes money" fits the brand better.

### A2. Recommended visual approach for a solo creator with $0

**Target screen-time mix for a 10 to 12 minute episode:**
- 40 to 50% your own data graphics: The Split, bars, unit-economics tables, simple maps.
- 20 to 25% primary-source documents: "Deal File" highlights of FTC releases, LAX Board documents, Cantaloupe reports and supplier pricing pages. Retype quotes as text graphics when the source is copyrighted.
- 25 to 35% stock or archive B-roll: unbranded vending machines, route vans, office break rooms, 1950s vending and automat footage from Prelinger/Internet Archive.
- 0 to 5% AI-generated stills, used only for abstract or illustrative purposes, never for "realistic" scenes of real places (see B5).

**Beat-by-beat visual plan for Episode 1 (draft):**

| Script beat | Visual |
|---|---|
| Cold open: "You tap your phone, a soda drops. $2." | Stock close-up of a card tap on an unbranded machine. A freeze-frame turns into The Split bar at full width labeled "$2.00". Five grey "?" segments appear. |
| LAX 59.5% teaser | Brief flash of "59.5%" with the source tag "LA Board of Airport Commissioners, 2023". Hold it for 2 seconds to open the loop. |
| Who owns the machine; the $7B industry; no firm above 5% | A US map with many small dots and a few bigger dots (Natural Earth or Census outlines). Title card: "Operator". |
| Machine costs ($1,900 / $3,500 / $9,000) | Three machine silhouettes (Inkscape) with price tags animating up. Source tag: supplier name. |
| Location commissions 5 to 20%; sales $150 to $2,000+/mo | A horizontal "location quality" scale from office break room to hospital, with monthly sales below each point. |
| **The Split:** tax 11¢, product 94¢, card 9¢, software 4¢, location 20¢, operator 62¢ | The signature sequence. Each slice drops out of the bar into a labeled bin. The Owner's Tally counts down $2.00 → $1.89 → 95¢ → 86¢ → 82¢ → 62¢. Hold the final frame for 4+ seconds. |
| $900/mo machine → $197 kept (22%) | A simple P&L table, one row highlighted at a time. |
| California college 28% | A Deal File excerpt of the contract line, highlighted. |
| Card vs cash ($2.45 vs $1.57), 78% cashless | Two side-by-side bars, then a donut showing 78%. Source: Cantaloupe. |
| Winner 1: LAX 59.5% or $100/machine | A Deal File of the LAX Board item with the highlighter on "59.5%". The Split re-runs with a 59.5% orange slice that swallows most of the bar. |
| Winner 2: scale, route density | A map comparison: 100 clustered pins versus 10 scattered pins, with drive lines (QGIS plus OSM, with attribution). |
| Canteen 1929, five-cent candy | Prelinger/archive vending footage (check per-item rights), then a 1929 to today timeline. |
| Winner 3: payments (600K devices, $4.5B) | A network diagram of devices feeding one hub, with a counter ticking. |
| Micro markets ($2.01 / $3.02 / $4.49; 71 → 572 smart stores) | Three ascending bars plus a growth bar. Stock footage of office micro-market shelves. |
| Reddit beginner's numbers | **Do not screenshot.** Retype the figures as your own "Operator's Ledger" graphic with the source line "Source: operator post on Reddit, r/[sub], [month year]". |
| Payback math (1.5 to 14 years) | A horizontal timeline bar with a machine icon sliding along it. |
| George Kamel's advice | A text quote card with attribution. **Do not use his video** (Content ID and reused-content risk). |
| FTC Operation Vend Up Broke, 1998 | A Deal File of the FTC press release (a federal work, so public domain [K]). Newspaper-ad-style mock graphic, then a phone-screen-style mock graphic. Built from scratch, with no real ad copy and no real TikTok UI. |
| Recap and close | The full Split returns, compact. End screen: next episode with The Split preview for "$15 car wash". |

### A3. Designing for older viewers watching on TVs

- **Why it matters:**
  - YouTube had a record **15.8% of all US TV viewing in August 2026**, roughly twice Netflix [S].
  - Nielsen also reported YouTube viewing among people **50+ up 9%** in a recent Gauge [S].
  - Assume a large share of this audience watches on a living-room TV from 8 to 10 feet away.
- **Text size at a 1920×1080 canvas:**
  - Body labels at least 48 to 56 px.
  - Key numbers 120 to 200 px.
  - Never below 36 px.
  - Rule of thumb: if you can't read it on a phone at arm's length, a TV viewer can't read it from the sofa.
- **Safe area:** keep text inside a 5 to 7% margin from every edge. Keep the bottom ~15% clear of important content, because YouTube's progress bar, captions and end-screen elements sit there.
- **Contrast:**
  - Use off-white (#F2EFE8) on charcoal (#1C1F24), with at least 7:1 contrast for text.
  - Avoid full-frame pure white, which looks harsh on TVs.
  - Avoid thin weights, red-on-black and red/green pairs.
  - A colorblind-safe accent pair is blue and orange.
- **Fonts:** heavy sans-serif with **tabular (fixed-width) numerals**, so digits don't jump as counters animate. Inter, IBM Plex Sans and Source Sans 3 are all on Google Fonts.
- **Pacing:**
  - Shots last 4 to 8 seconds, not the 1 to 2 seconds typical of retention-bait edits.
  - Show one idea per screen.
  - Hold any on-screen text for at least 1 second plus about 0.3 seconds per word.
  - Build numbers in sync with the narration: show the number as it is spoken, not before.
- **Narration speed:** set TTS to about 135 to 145 wpm, with slight pauses at section breaks.
- **Captions:** upload an accurate SRT made from the final narration script. Don't rely on auto-captions. This helps hard-of-hearing viewers and anyone watching muted.
- **Audio:**
  - Mix music at about −24 to −30 LUFS under a voice at about −14 LUFS integrated.
  - Use no music under dense number passages.
  - Older listeners struggle with voice over busy music.
- **Credibility cues:** a source tag on every number, real document excerpts, dates on every statistic ("in 2025"), and no flashy transitions or whooshes on every cut.

---

## B) Free tools and assets: licenses for monetized use

### B1. Editors

| Tool | Monetized use OK? | Notes |
|---|---|---|
| **DaVinci Resolve (free)** | Yes; free for commercial use [K] | Includes Fusion (motion graphics) and Fairlight (audio). Exports up to UHD/60p. **Linux gotcha:** the free Linux build has historically lacked H.264/H.265/AAC decode and encode. You may need to transcode stock clips to DNxHR/ProRes and convert the final export with ffmpeg. Verify on the current version. |
| **Kdenlive** | Yes; GPL, and your output belongs to you [K] | Native on Linux, light, fine for a narration-plus-graphics workflow. Shotcut is a similar alternative. |
| **CapCut (free)** | Technically yes, but **not recommended** | The June 2025 terms update set off a backlash over a "perpetual, irrevocable, worldwide, royalty-free, sub-licensable" license to user content, reportedly extending to name, likeness and voice in some uses [S]. CapCut says that clause hadn't changed for years [S]; either way, it is broad. Reported 2025 price increase to $19.99/mo for Pro [S, one source, unverified]. Many effects and templates are Pro-only, and some stock and music in CapCut is licensed for in-app or TikTok use only. Check each asset. |

### B2. Motion graphics and data animation

| Tool | License | Fit |
|---|---|---|
| **Motion Canvas** | MIT (free, commercial OK) [K] | Code-driven (TypeScript) animation. Ideal for The Split, counters and bars, and reusable across episodes as "your" component. |
| **Manim (Community Edition)** | MIT [K] | Python; excellent for animated numbers and equations; steeper learning curve for styling. |
| **Remotion** | **Free for individuals and companies of up to 3 people**; otherwise a Company License ("Creators" $25/seat/mo, "Automators" $0.01/render with a $100/mo minimum) [S] | React-based. Fine for a solo creator; re-check if you hire a team. |
| **Blender** | GPL; your renders and output are yours [K] | 3D vending machine models or a 3D receipt. Probably overkill at first. |
| **Canva Free** | Free content is licensed for use *inside your designs*, including commercial use; no standalone resale of raw assets [S] | Good for thumbnails and simple cards. **Do not use Canva "Popular Music"** in monetized videos: its license bars commercial or promotional use [S]. Elements may include trademarks; avoid branded ones. |
| **Inkscape / GIMP / Krita / Photopea** | Free/OSS (Photopea is free with ads) [K] | Vector icons of machines, receipts, maps, thumbnails. |

### B3. Stock footage and photos

| Source | License summary | Gotchas |
|---|---|---|
| **Pexels** | Free, commercial OK, no attribution required [K] | No implied endorsement by people shown. Don't portray identifiable people negatively (for example, a stock person as a "scammer"). Trademarks shown remain protected. |
| **Pixabay** | Free, commercial OK, no attribution [S] | Bans commercial use of recognizable trademarks/brands in relation to goods and services, and "immoral" uses of recognizable people [S]. You alone are responsible for clearances [S]. AI-generated items must be labeled by uploaders [S], so check the label before treating a clip as real footage. |
| **Mixkit** | Two video licenses, "Free" and "**Restricted**", plus separate music and SFX licenses [S] | Check which license each item carries. The page warns that the applicable license varies by item [S]. |
| **Coverr** | Free for commercial use, no attribution [K] | Smaller library; check for logos. |
| **Unsplash** | Free photos, commercial OK, no attribution required [K] | Can't compile photos into a competing library; trademark and people caveats as with Pexels. |
| **Wikimedia Commons** | **Per-file** license: public domain, CC0, CC BY or CC BY-SA [K] | CC BY/BY-SA need visible attribution (author, license, link), on screen or in the description. Record each file's license in a credits log. Commons excludes NC/ND licenses, but always read the file page. |
| **US federal government** (FTC, SBA, Census, BLS, NARA, NASA, DOT) | Works by federal employees are public domain (17 U.S.C. §105) [K] | **Contractor-made and third-party material on .gov sites may still be copyrighted.** Agency seals and logos can't imply endorsement. **State and local government works (City of LA, LAX, state colleges) are *not* automatically public domain.** Show short highlighted excerpts with commentary, which is a fair-use posture, rather than whole documents. |
| **Prelinger Archives (Internet Archive)** | Many films are public domain, others vary [K] | Excellent mid-century vending and automat footage. Check the rights field on each item. Some uploads carry Content ID claims from third parties who registered PD footage, so keep download records. |

### B4. Maps

- **OpenStreetMap (ODbL)** [S]:
  - When the map is a **major component**, show "© OpenStreetMap contributors" in a corner of the map long enough to read. It doesn't need to stay up during pans or zooms. **Also** credit in the end credits or the video description, with the URL openstreetmap.org/copyright.
  - If the map is incidental, attribution in the credits or description is enough.
  - Don't bulk-download tiles from openstreetmap.org (its tile usage policy) [K]. Render your own in QGIS from OSM extracts, or style vector data.
- **Natural Earth:** public domain country, state, coastline and city data; no attribution required [K]. Best for clean US and world base maps.
- **US Census TIGER/Line:** public-domain county, ZIP and road geometry [K]. Good for route-density maps.
- **QGIS** (free, GPL) [K] to compose the maps; export a PNG or SVG sequence for animation.

### B5. Music and sound effects

| Source | Monetized YouTube? | Gotchas |
|---|---|---|
| **YouTube Audio Library** (in YouTube Studio) | Yes; the safest option [K] | Some tracks require an attribution line in the description; copy it exactly. Licensed for YouTube use only, so don't reuse the tracks elsewhere. |
| **Pixabay Music** | Allowed under the Pixabay license [S] | **Content ID claims happen** because some uploaders register their tracks with fingerprinting services. The standard fix is to dispute with the Pixabay license certificate [S, secondhand]. While a claim is active, ad revenue may go to the claimant. Save the certificate at download. |
| **Freesound** | CC0: yes. CC BY: yes, with attribution. **CC BY-NC: no** for monetized videos [K] | Filter by license. CC0 is easiest. |
| **Canva Popular Music** | **No** [S] | See B2. |

For this tone, use sparse, calm piano or ambient beds, and silence under number-dense passages.

### B6. Fonts

- **Google Fonts**: most are under the SIL Open Font License, which is free for commercial video, thumbnails and logos [K].
- Recommended: **Inter** or **IBM Plex Sans** for UI and numbers (both have tabular figures). **Source Serif 4** or **IBM Plex Serif** give the Deal File a document look.
- Check each font's license tab; a few use Apache or UFL licenses, all permissive.

### B7. Legal and policy gotchas

1. **Branded products in stock clips** (Coca-Cola machines, Pepsi cans): showing a brand incidentally in editorial commentary is generally low risk. Pixabay's license, however, restricts commercial use of recognizable trademarks [S], and a brand prominent in your **thumbnail** can read as implied endorsement. Prefer unbranded or blurred machines in thumbnails and prominent shots.
2. **Company logos** (Cantaloupe, Compass, Canteen): showing a logo briefly to *identify* a company you're discussing is common practice (nominative use). Don't animate it into your branding, put it in a sponsor-like position, or alter it. Use press-kit images under the kit's terms.
3. **Reddit posts:**
   - Users own their posts. Screenshots also expose usernames.
   - **Facts are not copyrightable**, so retype the numbers into your own graphic and cite the post (subreddit and date) without the username.
   - Avoid reading posts verbatim. YouTube's reused-content policy flags "content that exclusively features readings of other materials you did not originally create" [S].
4. **News articles:** a brief headline or one-sentence excerpt on screen with your commentary is a typical fair-use posture. **Never** use broadcast news video, which carries the highest Content ID and claim risk [S]. Fair use is a defense, not a permission [S].
5. **Contracts and government documents:** highlight short excerpts. Federal documents (FTC) are public domain [K]. City and state documents are public records but can be copyrighted, so excerpt rather than reproducing them in full.
6. **Other creators' videos** (for example, the George Kamel review): don't clip them. Quote a sentence on a text card with attribution, or paraphrase.
7. **AI-generated images:**
   - Purely AI-generated material generally can't be copyrighted in the US (US Copyright Office AI report, Part 2, Jan 2025) [K], so anyone can reuse yours.
   - YouTube requires disclosure for *realistic* synthetic scenes, including "AI generated extra footage of a real place" and "a realistic scene that didn't actually occur" [S]. An AI image of "LAX terminal vending machines" would require it.
   - Older, skeptical viewers lose trust quickly when they spot AI imagery. Limit AI to abstract or illustrative uses (such as a stylized receipt texture) and never depict real people, real brands or real places with it.
8. **Keep a credits/rights log per episode** (asset, source URL, license, date downloaded, attribution text). This is how you win disputes.

---

## C) Monetization and policy

### C1. YPP thresholds (as of 2026-11-26)

- **Ads and Premium revenue now:** 1,000 subscribers plus either **4,000 public watch hours in 12 months** or **10M public Shorts views in 90 days** [S]. Shorts-feed watch hours don't count toward the 4,000 [S].
- **Fan-funding tier** (memberships, Super Thanks/Chat, some Shopping; **no ads**): 500 subscribers, 3 public uploads in 90 days, and either 3,000 watch hours in 12 months or 3M Shorts views in 90 days [S].
- **Announced August 10, 2026, effective February 1, 2027** [S, official YouTube blog]:
  - New applicants need **8,000 qualified watch hours in 365 days** or **20M qualified Shorts views in 90 days**. The subscriber bar stays at 1,000 [S, vidIQ].
  - The fan-funding and shopping thresholds are unchanged [S].
  - Existing YPP members aren't subject to the new entry bar, but must accept the updated terms by January 31, 2027 [S].
  - Shorts revenue sharing will require 10M Shorts views per 90 days, even for existing partners [S].
- **What this means for a channel launching now:** you will almost certainly have to meet **8,000 hours**.
  - 8,000 hours is 480,000 minutes. At about 4 to 5 minutes average view duration on a 12-minute video, that is **roughly 100,000 to 120,000 long-form views within 12 months**.
  - Also watch the inactivity rule: no uploads or community posts for 6+ months can cost you monetization [S].

### C2. The "inauthentic content" policy and faceless AI-voice channels

**July 15, 2025:** YouTube renamed "repetitious content" to "**inauthentic content**", describing it as a clarification rather than a new rule [S]. The official policy text [S] says:
- **Not allowed:** "Image slideshows, templated storylines, or scrolling text with minimal or no narrative, commentary, or educational value", and "AI-generated content made with generic or unoriginal templates giving the impression of mass production."
- **Allowed:** "Same intro and outro for your videos, but the bulk of your content is different". AI tools are fine when "the final product still shows your own creative vision."

**July 16, 2026:** YouTube split inauthentic content into **three non-monetizable buckets** [S, TechCrunch/TechRepublic]:
1. Generic, repetitive or template-based content that is easy to make with AI, CGI or templates and varies little between videos. This includes tutorials that reproduce what is already common on the platform.
2. Off-putting or distressing content made to manipulate emotions for views.
3. **AI personas (AI representations of real people) discussing sensitive topics, explicitly including finance**, legal and medical.

Enforcement is at the **channel level**, and you can reapply after 90 days [S].

**How this channel stays safe:**
- **Original research in every episode:** primary documents, your own calculations, a distinct question per episode. That is the opposite of "reproducing what's already common."
- **A clear narrative arc** (setup → follow the money → winners → reality check → history → takeaway). YouTube's own words are that template content doesn't "have a narrative arc" [S].
- **Graphics built for each episode's data.** A recurring device like The Split is fine, just as a shared intro and outro are fine, as long as the bulk of each video is different [S].
- **A human-written script** with an editorial point of view. AI can help with editing and outlining [S].
- **Don't mass-produce.** Two strong episodes a month beat eight thin ones.
- **No AI avatar or "persona"** presented as a human expert (for example, "I'm Frank, a 30-year broker"). The narrator is the channel's voice and nothing more.
- **No reading** of Reddit posts or articles verbatim (reused-content policy) [S].
- **Avoid wall-to-wall generic stock.** Logically Answered's views run low relative to its subscribers [S], which suggests what a stock-only look gets you.

### C3. Does an AI TTS narrator need the "altered or synthetic" label?

YouTube's Help Center [S] **requires disclosure** when content:
- makes a real person appear to say or do something they didn't,
- alters footage of a real event or place,
- generates a realistic scene that didn't occur, or
- creates music that is the main focus.

The listed example for voices is cloning *someone else's* voice.

It **does not require disclosure** for:
- production assistance (AI-written or AI-improved scripts and outlines),
- captions,
- voice or audio repair, and
- "**cloning one's own voice to create voice overs**."

The page doesn't mention generic TTS narration [S].

**Conclusion:** a stock synthetic narrator that imitates no real person isn't in the "must disclose" categories, so the upload checkbox is generally not required for narration alone. Two recommendations:
- **Do** add a plain sentence to every description: "Narration uses a synthetic voice. Research, script and graphics by [channel]." Trust matters a lot with this audience, and disclosing "won't limit a video's audience or impact its eligibility to earn money" [S].
- **Do** tick the box if you ever use realistic AI footage or images of real places, events or people. Failing to disclose when required can lead to labels applied for you, content removal or YPP suspension [S].

### C4. RPM expectations

- Business-documentary niche gross CPM is about **$10 to $25**, and creators keep about 55% of long-form ad revenue, so **RPM is roughly half of CPM** [S, OutlierKit].
- Third-party RPM tables (all vendor blogs; directional only) [S]:
  - Business/entrepreneurship long-form: $6 to $16 in one table, $12 to $25 in another.
  - US finance/investing: about $8 to $25.
  - Non-US audiences: 30 to 60% of US RPM.
  - Shorts: cents per thousand.
- **Planning number:** $8 to $12 RPM in year 1, rising to $15 to $20+ if the audience is 70%+ US, older, and watching topics that attract B2B, lending and software advertisers. RPM peaks in Q4 and drops in January.
- **Sanity check:** 50,000 monthly views × $10 RPM = **$500/month**. Reaching $5K/month from ads alone takes about 400K to 600K monthly views.

### C5. Realistic timeline and effort (honest version)

- Estimated solo time per 11-minute documentary-style video is **16 to 28 hours** [S]: research 4 to 8, script 3 to 5, voice ~1, visuals 6 to 10, packaging 1 to 2. The episode-1 data-graphics approach sits at the higher end the first time and gets faster once The Split and the Deal File are reusable components.
- At 2 episodes a month:
  - **Months 0 to 6:** most videos get dozens to low thousands of views. That is normal, and the period is mostly for building a back catalog and learning the packaging.
  - **Months 6 to 18:** a breakout video, usually one with a strong curiosity hook such as "LAX takes 59.5%", is what typically pushes a channel toward 8,000 hours.
  - **Many channels never reach YPP.** Treat 12 to 24 months as the median-optimistic case.
- Buyers of faceless channels also discount them for demonetization risk [S]. This is a real business risk, which is another reason to build an email list.

### C6. Other revenue (often bigger than AdSense in this niche)

- **Sponsors that fit the audience:**
  - Accounting and ERP: QuickBooks, Xero, NetSuite. NetSuite already sponsors Modern MBA [S].
  - Payroll and HR: Gusto, ADP.
  - POS: Square, Clover, Toast.
  - Business insurance: Next, Hiscox.
  - Legal and entity formation.
  - Unattended-retail tech: Cantaloupe, Nayax. **This is a conflict of interest when you analyze them. Disclose it, or decline vendors you cover.**
- **Acquisition ecosystem:**
  - **BizBuySell** has active SBA lending partnerships: LoanBud's "SBA Loan Eligible" badge (Jan 2026) and iBusiness Funding's 7(a) access (Oct 2025) [S]. A public creator or affiliate program **was not found**; contact their advertising or partnerships team directly.
  - Empire Flippers and Flippa are online-business marketplaces; check whether they offer affiliate programs.
  - SBA 7(a) lenders and loan marketplaces.
  - Quality-of-earnings and due-diligence firms, and search-fund or acquisition-education programs.
  - **Caution:** lender and broker *referral fees* can require state licensing, so get advice before taking per-loan or per-deal commissions.
- **Owned products:**
  - A free email newsletter with "deal teardowns" and the episode's spreadsheet (vending P&L model, payback calculator).
  - Later, a paid template pack or an occasional paid deep-dive.
  - Older viewers with capital value **checklists and models**.
- **Compliance:**
  - Use YouTube's "includes paid promotion" checkbox and say "sponsored" verbally and on screen (FTC Endorsement Guides) [K].
  - Add a standing "educational, not financial or legal advice" line.

---

## D) Packaging and retention

### D1. Title options for Episode 1

Each is under about 60 characters, calm, specific and number-led:

1. **Who Gets Paid When You Buy a $2 Vending Machine Soda**
2. **LAX Takes 59.5% of Every Sale: Inside Vending Economics**
3. **Follow the $2: The Real Math of a Vending Machine**
4. **Vending Machines Aren't Passive Income. Here's the Real Math.**
5. **Where Your $2 Goes: The Vending Business, by the Numbers**

Recommendation: launch with #1 or #2 and A/B test with **Test & Compare**. It tests up to three titles, thumbnails or combinations and picks the winner by **watch time**, not click-through rate, so it rewards titles that attract the viewers who stay [S]. Test titles that set honest expectations against curiosity-led titles.

### D2. Thumbnail concepts

1. **"The Split"** (the series template):
   - Dark charcoal background, with a large unbranded soda bottle or can on the left.
   - On the right, a thick horizontal bar sliced into five muted segments, with only the last one (green) labeled **"62¢"**.
   - Top text: **"$2.00"**. Nothing else.
   - It works at phone size and on a TV, and every future episode reuses the layout with a new item and number.
2. **"The Airport Deal"**:
   - A stock photo of an unbranded vending machine in a terminal, slightly darkened.
   - A huge **"59.5%"** in warm yellow, with a small label: "to the airport".
   - Curiosity comes from the number, not from a face or arrows.
3. **"The Receipt"**:
   - A tall paper receipt on a dark desk, with the lines TAX 11¢ / DRINK 94¢ / CARD 9¢ / BUILDING 20¢ in large monospace type.
   - The bottom line **"YOU: 62¢"** is circled in red pen.
   - Keep the font big enough to read on a phone, even if only 3 or 4 lines fit.

Thumbnail rules for this audience:
- 2 to 4 words at most.
- One focal object, high contrast, no shocked faces, no red arrows, no "$$$" imagery.
- The title and thumbnail should **complement each other, not repeat each other**.

### D3. The first 30 seconds

- **The current cold open is strong.** "You tap your phone, and a soda drops. Two dollars. Before the owner keeps a single cent, five other players get paid" works because it is concrete, visual and creates a question.
- **Keep the order: hook → stakes/open loop → credibility → promise → go.**
  1. Hook (0 to 8 s): the tap and the five players, with The Split bar showing five "?" segments.
  2. Open loop (8 to 15 s): "One airport takes 59.5%." Show the number, not the answer.
  3. Credibility (15 to 25 s): "We checked payment-network data, city contracts and operators' own results." Briefly flash 3 source logos or document thumbnails.
  4. Promise (25 to 30 s): "Let's follow the two dollars."
- **No channel intro, no "welcome back", no subscribe ask** in the first minute. Spending the first 30 seconds on intros is a named failure mode [S].
- Speak to the viewer's real question. For this audience that is "should I put money into this?" and not "how do I get rich?"
- **Pay off the open loop** in the middle of the video (LAX in Winner 1). Then open a new loop before each section ("the third winner never stocks a single snack").

### D4. Ideal length

- **10 to 14 minutes** for standard episodes, which matches the documentary norm of 9 to 12 [S].
- Episode 1 at about 1,393 words runs about 10 to 11 minutes at an older-friendly TTS pace. That is right, and it clears the 8-minute mark for mid-rolls (place one at a natural section break, not mid-number).
- Occasional 18 to 25 minute "deep dives" (for example, "Buying a laundromat: the full due-diligence walk-through") suit high-intent viewers on TVs, but only once the 12-minute format retains well.

### D5. Chapters (Episode 1 draft; adjust timestamps to the final render)

YouTube chapters need 0:00 first, at least 3 chapters, and each at least 10 seconds [K].

```
0:00 The $2 soda
0:40 Who actually owns the machine
1:30 What machines and locations cost
2:45 Following the $2: tax, product, payments, location
4:30 What the operator really keeps
5:15 Winner #1: the location (LAX's 59.5% deal)
6:15 Winner #2: scale
7:00 Winner #3: the payment network
7:45 Micro markets and smart stores
8:45 A beginner's real six months
9:45 The 1998 FTC crackdown
10:30 Who wins in vending
```

Chapters help older viewers jump back to a number, and they help search ("LAX vending contract").

### D6. Upload cadence

- **One long-form episode every two weeks** is sustainable at 16 to 28 hours per video [S]. Move to weekly only once the components are reusable.
- Publish on a fixed day and time; consistency builds a habit with this audience.
- Test evening or weekend slots, since TV viewing is heavier then. This is not verified for this niche; check YouTube Studio's "When your viewers are on YouTube" once you have data.
- After February 2027, an existing partner needs at least **two long-form uploads per 90 days** (or other activity thresholds) to stay active, a bar a biweekly cadence clears easily [S, vidIQ].
- Use Community posts between episodes: a poll ("Would you buy a vending route?"), or a chart from the next episode.

### D7. Shorts: yes, but as trailers, not a strategy

- **Why be careful:**
  - Shorts RPM is tiny [S].
  - Shorts-feed hours don't count toward the watch-hour bar [S].
  - The Shorts route to YPP doubles to 20M views in 2027 [S].
  - Shorts audiences skew younger than this channel's audience.
  - Shorts are nonetheless 77% of global YouTube views (2025) [S], so they work as discovery.
- **How to cut them:**
  - Make 2 or 3 Shorts per episode, 30 to 50 seconds each.
  - Build each around **one** number reveal: "LAX takes 59.5% of every vending sale", "Where $2 of soda money goes", "The 1998 FTC sweep: 40 cases against vending scams".
  - Recompose graphics for 9:16 instead of cropping 16:9, and use large on-screen captions.
  - Attach each one to the full episode with the **Related Video link** [S].
  - Post them 2 to 5 days after the long-form, as a second wave.
  - vidIQ reports YouTube now considers viewers' long-form history when recommending to Shorts viewers [S], which helps tie the two formats together.
- **Stop** if Shorts viewers aren't clicking through to the long-form and the channel's long-form audience gets younger and less engaged.

---

## Sources

**YouTube policy and monetization (checked this session)**
- YouTube Help: YPP overview and eligibility. https://support.google.com/youtube/answer/72851?hl=en
- YouTube Blog (Aug 10, 2026): "New opportunities to earn and changes to the YouTube Partner Program". https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/
- vidIQ: YPP changes 2027. https://vidiq.com/blog/post/youtube-partner-program-changes-2027/
- YouTube Help: Channel monetization policies (inauthentic/reused content). https://support.google.com/youtube/answer/1311392?hl=en
- TechCrunch (Jul 20, 2026): YouTube clarifies policies around AI slop. https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- Tubefilter (Jul 13, 2026): inauthentic content monetization policy update. https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/
- TechRepublic: YouTube tightens monetization rules. https://techrepublic.com/article/news-youtube-ai-video-monetization-rules
- Social Media Today (2025): YouTube clarifies monetization update. https://www.socialmediatoday.com/news/youtube-clarifies-monetization-update-inauthentic-repeated-content/752892/
- YouTube Help: Disclosing use of altered or synthetic content. https://support.google.com/youtube/answer/14328491?hl=en
- YouTube Help: A/B test titles and thumbnails. https://support.google.com/youtube/answer/16391400?hl=en
- YouTube Blog: Related videos traffic guide. https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/
- vidIQ: Shorts and long-form viewers algorithm. https://vidiq.com/blog/post/youtube-shorts-long-form-viewers-algorithm
- TVREV / Tubular: 77% of 2025 views from Shorts. https://www.tvrev.com/news/tube-trends-over-75-of-youtube-views-came-from-shorts-in-2025-tubular

**Comparable channels and niche economics**
- OutlierKit: Faceless business documentary channels, 2026 format teardown. https://outlierkit.com/resources/faceless-business-documentary-channels/
- CreatorDB: Modern MBA. https://creatordb.app/creatorstats/modernmba/
- CreatorDB: Wendover Productions. https://creatordb.app/creatorstats/wendoverproductions/
- Social Blade: PolyMatter. https://socialblade.com/youtube/handle/polymatter/achievements
- vidIQ stats: Codie Sanchez. https://vidiq.com/youtube-stats/channel/UC5fI3kxC-ewZ6ZXEYgznM7g
- Empire Flippers: Faceless YouTube vs other online businesses. https://empireflippers.com/faceless-youtube-business-vs-other-online-businesses/
- 1of10: YouTube CPM/RPM by niche, 2026. https://www.1of10.com/blog/youtube-cpm-rpm-by-niche/
- vidIQ: Highest-paying niches, 2026. https://www.vidiq.com/blog/post/most-profitable-youtube-niches
- OutlierKit: RPM in the finance niche. https://outlierkit.com/blog/youtube-rpm-finance-niche

**TV viewing**
- Nielsen July 2026 Gauge. https://www.nielsen.com/news-center/2026/tv-usage-kicks-usual-summer-slowdown-fueled-by-world-cup-and-streaming-in-nielsens-july-gauge-reports/
- Tubefilter (Oct 22, 2026): YouTube's record share of US TV. https://www.tubefilter.com/2026/10/22/nielsen-the-gauge-youtube-record-watch-time-share-us-tv/amp/
- FourWeekMBA: YouTube 15.8% of US TV in August 2026. https://fourweekmba.com/ai-youtube-took-a-record-15-8-of-us-tv-in-august-2x-netflix/

**Tools and licenses (checked this session)**
- TechRadar: CapCut terms of service. https://www.techradar.com/pro/popular-video-editing-app-capcut-wants-to-use-any-content-you-produce-for-free-forever-heres-what-you-should-know
- CapCut: About CapCut's Terms of Service. https://capcut.com/resource/about-capcut-terms-of-service
- Remotion license and pricing. https://www.remotion.dev/docs/license/pricing
- Pixabay license summary. https://pixabay.com/service/license-summary/
- Pixabay terms. https://pixabay.com/service/terms/
- Mixkit licenses. https://mixkit.co/license/
- OSMF attribution guidelines. https://osmfoundation.org/wiki/Licence/Attribution_Guidelines
- Canva Popular Music License. https://canva.com/policies/popular-music-license
- Canva Content License Agreement. https://www.canva.com/policies/content-license-agreement/

**Tools and licenses (official pages; not re-fetched this session, so verify)**
- Pexels license. https://www.pexels.com/license/
- Unsplash license. https://unsplash.com/license
- Coverr license. https://coverr.co/license
- Wikimedia Commons reuse. https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia
- USA.gov government works and copyright. https://www.usa.gov/government-copyright
- Prelinger Archives. https://archive.org/details/prelinger
- Natural Earth terms. https://www.naturalearthdata.com/about/terms-of-use/
- OSM tile usage policy. https://operations.osmfoundation.org/policies/tiles/
- Freesound FAQ (licenses). https://freesound.org/help/faq/
- YouTube Audio Library help. https://support.google.com/youtube/answer/3376882
- Google Fonts FAQ. https://developers.google.com/fonts/faq
- DaVinci Resolve. https://www.blackmagicdesign.com/products/davinciresolve
- Kdenlive. https://kdenlive.org
- Motion Canvas. https://motioncanvas.io
- Manim Community. https://www.manim.community
- Blender license. https://www.blender.org/about/license/
- US Copyright Office, AI reports. https://www.copyright.gov/ai/
- YouTube chapters. https://support.google.com/youtube/answer/9884579
- FTC Endorsement Guides FAQ. https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking

**Episode-specific primary sources useful for visuals**
- FTC (Sept 1998): "Operation Vend Up Broke" press release. https://ftc.gov/news-events/press-releases/1998/09/ftc-announces-operation-vend-broke-states-and-feds-stop-business
- PR Newswire: BizBuySell and LoanBud SBA Loan Eligible program (Jan 2026). https://www.prnewswire.com/news-releases/bizbuysell-and-loanbud-partner-to-launch-sba-loan-eligible-program-302666934.html
- PR Newswire: iBusiness Funding and BizBuySell SBA 7(a) partnership (Oct 2025). https://www.prnewswire.com/news-releases/ibusiness-funding-and-bizbuysell-announce-partnership-to-unlock-sba-7a-financing-options-for-business-buyers-nationwide-302590784.html

**Caveats:**
- Subscriber counts are tracker snapshots.
- RPM figures come from vendor blogs, not YouTube.
- The 2027 subscriber threshold (unchanged at 1,000) comes from vidIQ; YouTube's blog post doesn't restate it.
- The Resolve-on-Linux codec limitation and the [K] license summaries should be re-checked against current official pages before you rely on them.
