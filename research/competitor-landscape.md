# Competitor Landscape: Who Else Makes "Boring Business" Videos, and What Works

**Prepared:** 2026-11-26
**For:** Dull Profits (faceless, AI-narrated, calm and sourced explainers on buying, owning and selling unglamorous small businesses; audience 40 to 65+, has capital, often watches on a TV)
**Builds on:** `research/channel-strategy-and-visuals.md` (section A1 lists 11 comparable channels; section C2 covers the inauthentic-content policy text). This report does not repeat those. It adds measured data from 79 channels and about 3,400 search results.

---

## Bottom line (read this first)

1. **The exact lane is open.** No channel, faceless or not, makes calm, sourced explainers about the unit economics of one small business at a time.
   - The big faceless explainers (Wendover, Modern MBA, How Money Works) cover consumer brands and national chains. Among "our" businesses they have only done self-storage (about 1.0M and 1.2M views) and private equity in general.
   - The boring-business space itself is split between two groups. On-camera owners show their own P&L ("I bought a car wash and it made me $500,000"). Mass-produced AI channels churn out "N boring businesses" lists.
2. **Demand for the topics is proven.**
   - Car washes: one owner-creator (Stephen the Investor) has 3.7M, 2.8M and 2.4M views in the past year from a 147K-sub channel.
   - Laundromats: up to 4.9M views. Vending: up to 10.5M.
   - Private-equity roll-ups: dozens of videos above 1M.
   - **Nobody has made the calm, faceless "follow the money" version of any of these.**
3. **The "N boring businesses" list format is saturated and copy-pasted.**
   - In our search sample, 38 list videos have 100K+ views, and most were published in the last 12 months.
   - Titles are cloned word for word. David Heacock's "6 BORING Businesses that Always Make Millionaires (90% success rate)" (2.9M) has at least five copies.
   - The channels that mass-produce this format (30 to 67 uploads a month) have median views of only 1K to 18K. **Don't enter that lane.**
4. **Packaging rules from the data:**
   - A **real dollar figure** in the title nearly doubles a faceless video's odds of being an outlier (22% of outliers vs 12% of normal videos).
   - A **number** helps (×1.45).
   - A **question mark** hurts (×0.64).
   - **Video length makes no difference.** Outliers and normal videos both have a median of about 16 minutes.
5. **What this audience trusts** (from the same-audience channels):
   - Calm, plain delivery with no hype, a "real answer" style, charts with real numbers, and visible credentials.
   - Rob Berger's 50+ audience complained about music-heavy editing and a 1.15× speed-up.
   - Patrick Boyle (dry, skeptical, 34-minute videos) has the highest views-per-subscriber in the whole set: 1.10.
   - Age-specific hooks drive the outliers there: "Working Past 60", "Social Security at 62 vs 67 vs 70", "It Took Me 64 Years…".
6. **The biggest supply gaps that also fit the audience:**
   - Funeral-home economics.
   - HVAC/plumbing roll-ups, told from the seller's side.
   - **Selling or valuing your small business:** no video in our sample above 100K views in the last 5 years. Broker channels have median views under 1,000.
   - ATMs, billboards and pest control.

---

## Method

- **When:** November 26, 2026. All counts are as of that day.
- **Search data:**
  - 257 YouTube search-result pages: 122 topic queries, each sorted by relevance and by view count, plus about 16 same-audience discovery queries.
  - That gives 3,369 unique videos with title, channel, views, length and approximate age.
  - Only the first page of each search (about 20 results) could be read, so **counts are lower bounds**, useful for comparing topics, not for totals.
- **Channel data:** for 79 channels, the 150 most recent long-form uploads (9,022 video rows), read with yt-dlp from the channel "Videos" tab. Subscriber counts come from YouTube itself, rounded to 3 significant figures. Upload counts are the channel's full uploads playlist, including Shorts.
- **Definitions:**
  - **Median views:** the median of the last 30 long-form videos that are at least 3 weeks old, so brand-new uploads don't drag it down.
  - **Views ÷ subs:** median views divided by subscribers. It shows how much of the subscriber base actually watches.
  - **Long-form per month:** estimated from YouTube's approximate upload dates ("2 months ago"), so it is rough for slow channels.
  - **Outlier multiple:** a video's views divided by the median of the 20 uploads around it on the same channel. This corrects for channel growth.
  - **Outlier:** at least 3× its neighbors *and* at least 3× the channel's recent median, with at least 50K views. That gave 649 outliers among the English-language channels.
- **"Faceless / AI" labels** are judged from thumbnails (checked visually as contact sheets) and from upload cadence. Watch pages are behind a bot check, so **the narrator's voice could not be checked**. "AI-made look" means AI-generated thumbnail art plus a mass-production cadence, not a confirmed synthetic voice.
- **Not used:** paid trackers (Social Blade history, vidIQ audience age). Audience-age claims come from the creators' own statements, cited below.
- **Raw data** (not in the repo): `/tmp/claude-0/-home-user-dull-profits/2d3a3f8e-aea6-5074-995c-c55aa0aa7c64/scratchpad/landscape/`. Files: `channel_stats.csv`, `outliers.csv`, `topics.json`, `search/*.jsonl`, `channels/*.json`, `thumbs/sheet*.jpg`.

---

## 1. Channel table

Key: **Subs** = subscribers. **Uploads** = all uploads, including Shorts. **Median** = median views of the last 30 long-form videos. **V/S** = median ÷ subs. **/mo** = long-form uploads per month (approximate). **Length** = median length of the last 30.

### Ring A: direct competitors (boring businesses, owners, small-business economics)

| Channel | Subs | Uploads | Median | V/S | /mo | Length | Face / voice | What stands out |
|---|---|---|---|---|---|---|---|---|
| Codie Sanchez | 2.28M | 1,135 | 237K | 0.10 | ~3 | 18 min | On camera | Owns the topic. Biggest hits are data-backed lists (5.9M "never fail", 2.8M "always fail") and ownership tests (2.2M vending) |
| UpFlip | 1.78M | 470 | 520K | 0.29 | ~3 | 36 min | Owner interviews | Revenue in every title. Vending 3.3M and 2.0M, laundromat 2.8M and 2.2M |
| CNBC Make It | 2.02M | 3,229 | 133K | 0.07 | ~7 | 8 min | Produced, owners on camera | "It Brings In $X/Year" formula. Vending 3.5M, laundromat 1.6M, porta-potty 1.3M |
| Starter Story | 905K | 598 | 101K | 0.11 | ~10 | 15 min | Interviews | Now mostly apps and online businesses |
| Investment Joy | 2.52M | 717 | 24K | **0.009** | ~3 | 22 min | On camera (laundromat owner) | Built on 2019 to 2022 laundromat P&L videos (4.9M, 4.5M). Now heavily decayed |
| Stephen the Investor | 147K | 185 | 42K | 0.28 | ~5 | 24 min | On camera (car-wash owner) | **3.7M, 2.8M, 2.4M, 1.6M** car-wash P&L videos within ~1 year |
| Car Wash Rob | 13.4K | 176 | 9.7K | 0.72 | ~4 | 33 min | On camera | "I Spent $3,000,000… Collect 7 Days of Cash With Me" (693K) |
| David Heacock | 234K | 1,995 | 21K | 0.09 | ~7 | mixed | On camera (factory owner) | 2.9M "6 BORING Businesses…", 1.8M "Just Buy One of These" |
| Tim Richard | 193K | 59 | 52K | 0.27 | ~3 | 12 min | On camera | 2.2M "9 Machines Making People Rich" |
| Brian Beers | 26K | 480 | 17.5K | 0.67 | ~4 | 11 min | On camera (owns 37 shops) | 608K "I Bought 2 Vending Machines…" |
| Kenny Finance | 57.5K | 307 | 6.4K | 0.11 | ~3 | 18 min | On camera | 854K clone of Codie's "never fail" list |
| Caitlin Doughty (Ask a Mortician) | 2.13M | 284 | 971K | 0.46 | <1 | 29 min | On camera | Death care. Proves a huge audience for funeral topics (2.0M "$3 Billion Funeral Empire") |
| Tyler Cauble | 102K | 783 | 4.6K | 0.05 | ~2.5 | 18 min | On camera (commercial real estate) | Outliers are boring assets: parking lot 583K, Buc-ee's 377K |
| Self Storage Income | 39.5K | 519 | 1.5K | 0.04 | ~2.5 | 46 min | On camera / podcast | Best video 547K ("How Much Money Does Self Storage Make?") |
| Franchise Inspectors | 181K | 390 | 2.3K | 0.01 | ~3 | 6 min | On camera | 1.1M Chick-fil-A, 259K gas stations |
| **Hard Hat Economics** | 18.3K | 187 | 6.9K | 0.38 | ~5 | 8.5 min | **Faceless, AI-made look** | Contrarian blue-collar economics. 424K, 408K, and 142K for "Codie Sanchez Sold Her Laundromats… Why Does She Want YOU to Buy One?" |
| **David Explains Money** | 44.6K | **6** | **144K** | 3.2 | ~1 | 27 min | **Faceless, AI cartoon of a grey-haired businessman** | 1.4M "20 BORING BUSINESSES…" in 4 months. Clearly aimed at older viewers |
| **Mr. Finance** | 83.4K | 179 | 4.3K | 0.05 | **~44** | 23 min | **Faceless, templated AI thumbnails** | "The Economics of Owning a ___" series, mass-produced |
| **Harry's Stealth Wealth** | 34.2K | 364 | 3.1K | 0.09 | **~30** | 18 min | **Faceless, AI mascot** | Clones top list titles (837K) |
| **Ned Talks Business** | 9.6K | 158 | 3.5K | 0.37 | **~33** | 26 min | **Faceless, templated AI art** | "Economics of owning" real estate |
| **Business Cortex** | 53.5K | 154 | 1.1K | 0.02 | ~7 | 12 min | **Faceless, AI images** | "Machines" lists (1.1M once) |
| **Bald Guy Breaks It Down** | 2.45K | 18 | 12K | 4.9 | — | 25 min | **Faceless, AI cartoon** | "POV: You Start With One Vending Machine" / "Your Life as a Car Wash Owner" |

Tiny copycats of the "Economics of Owning a ___" template (Dean Finance, Boring Gold: funeral home, cemetery, car wash, self-storage) get **under 1,000 views per video**. A template alone attracts nobody.

### Ring A2 / D: buying and selling a business (ETA, brokers)

| Channel | Subs | Uploads | Median | V/S | /mo | Length | Face / voice | What stands out |
|---|---|---|---|---|---|---|---|---|
| My First Million | 975K | 2,223 | 48K | 0.05 | ~10 | 56 min | Podcast | Frequent boring-business episodes, but a general entrepreneur audience |
| Chris Koerner (Koerner Office) | 737K | 978 | 59K | 0.08 | ~6 | 15 min | On camera / podcast | Business ideas |
| Carl Allen (Dealmaker) | 134K | 1,583 | 8.7K | 0.06 | ~2.5 | 35 min | On camera | 176K "Buy a Business Without Banks…" |
| Walker Deibel (Buy Then Build) | 91.8K | 386 | 8.1K | 0.09 | ~7 | 15 min | On camera (author) | 114K for a case study of an "auto business in a $40B market" |
| David C. Barnett | 87K | 971 | 893 | 0.01 | ~10 | 42 min | On camera, older host | Buying and selling small businesses. Loyal but tiny reach per video |
| Jonathan Jay (UK) | 36.5K | 1,138 | 777 | 0.02 | ~4 | 10 min | On camera | |
| Acquiring Minds | 18.3K | 478 | 2.7K | 0.15 | ~10 | 77 min | Podcast | |
| Acquisitions Anonymous | 8.8K | 625 | 552 | 0.06 | ~10 | 36 min | Podcast | **Listing teardowns** ("This Rubber Duck Business Makes $321K… But Wants $2.7 MILLION") as audio only |
| Cole Ferguson (business broker) | 7K | 301 | 176 | 0.03 | — | 12 min | On camera | |

### Ring B: format peers (faceless business-economics explainers)

| Channel | Subs | Uploads | Median | V/S | /mo | Length | Face / voice | Relevant hits |
|---|---|---|---|---|---|---|---|---|
| Wendover Productions | 4.92M | 292 | 1.10M | 0.22 | ~2.5 | 19 min | Faceless | Dollar stores 4.2M, private equity 2.7M, car dealerships 1.2M, **self storage 1.0M** |
| ColdFusion | 5.27M | 593 | 966K | 0.18 | ~3 | 19 min | Mostly faceless | (Tone model only) |
| More Perfect Union | 4.37M | 2,033 | 1.40M | 0.32 | ~10 | 15 min | Journalism, reporters on camera | Private equity buying dentists 1.06M, hospitals 1.2M |
| Economics Explained | 2.90M | 461 | 599K | 0.21 | ~5 | 18 min | Faceless | Countries and macroeconomics |
| PolyMatter | 1.93M | 189 | 286K | 0.15 | ~1.5 | 19 min | Faceless | "How McDonald's Really Makes Money" 3.9M |
| MagnatesMedia | 1.86M | 255 | 822K | 0.44 | ~1 | 33 min | Narrator, cinematic | |
| Company Man | 1.80M | 506 | 170K | 0.09 | ~5 | 12 min | Faceless | "The Decline of ___… What Happened?" formula. Buffet chain 518K |
| How Money Works | 1.77M | 332 | 836K | 0.47 | ~4 | 19 min | Faceless | Private equity: 1.4M, 1.2M, 964K, 750K |
| Patrick Boyle | 1.37M | 489 | **1.50M** | **1.10** | ~4 | 34 min | On camera | Private-equity returns 818K. Highest views per subscriber in the set |
| Business Casual | 1.15M | 91 | 413K | 0.36 | dormant (~4 yrs) | 8 min | Faceless animation | |
| Logically Answered | 930K | 1,217 | 216K | 0.23 | ~10 | 16.5 min | Faceless | "Small businesses are obsessed with AI slop" 705K |
| Modern MBA | 854K | **85** | 295K | 0.35 | ~2.5 | **37 min** | Faceless | **Self storage 1.2M, Dollar Tree 1.2M, buffets 842K, gyms 392K, "Bars Have 90% Margins" 338K** |
| GEN | 821K | 524 | 288K | 0.35 | ~3 | 22 min | Faceless | Private equity 5.2M and 1.8M |
| Wall Street Millennial | 372K | 984 | 146K | 0.39 | ~10 | 16 min | Faceless | "A.I. Startup Fails To Run Vending Machine" 100K |
| How People Make Money | 139K | 45 | 55K | 0.39 | ~4 | 13 min | Faceless, meme style | 2.4M "The MISERABLE Lives Of CEOs" |

### Ring C: the vending niche itself

| Channel | Subs | Uploads | Median | V/S | /mo | Length | Face / voice | What stands out |
|---|---|---|---|---|---|---|---|---|
| Quik Play | 669K | 375 | 71K | 0.11 | ~1 | 17 min | On camera | **10.5M** "Collecting Money From 4 Of Our Vending Machines!" (2022). Arcades 2.0M and 1.8M |
| Jaime Ibanez | 526K | 216 | 144K | 0.27 | <1 | 13 min | On camera | 7.0M and 3.9M collection videos (2019 to 2020). A Vox report says the channel earned about **3× what his route did** |
| AFC vending | 54.5K | 214 | 9.5K | 0.17 | dormant ~6 yrs | 16 min | On camera | 5.2M "collecting money from my 11 vending machines!" |
| Everything DSK | 132K | 1,544 | 4.2K | 0.03 | ~3 | 10 min | On camera | 220K "How I run a Successful Vending Machine Business at 23" |
| Vendingpreneurs | 47.2K | 1,351 | 3.6K | 0.08 | ~7 | 11 min | On camera, sells coaching | 219K "Don't Start A Vending Machine Business, Until You Watch This…" |
| Dominick Barbato | 27K | 374 | 2.3K | 0.09 | ~1 | 9 min | On camera | 116K "Vending Machines Are NOT Profitable (The Truth)" |

Vending videos from outside the niche: CNBC Make It 3.5M, UpFlip 3.3M and 2.0M ("Is This the Death of Traditional Vending?!"), Codie Sanchez 2.2M, Brian Beers 608K, and WSJ 685K ("We Let AI Run a Vending Machine. It Lost All the Money.").
**There is no economics explainer from a big faceless channel.** The whole niche is cash-collection vlogs, owner interviews and course funnels.

### Ring D: same audience (40 to 65+, has capital)

| Channel | Subs | Uploads | Median | V/S | /mo | Length | Face / voice | Why this audience trusts them |
|---|---|---|---|---|---|---|---|---|
| Patrick Boyle | 1.37M | 489 | 1.50M | 1.10 | ~4 | 34 min | On camera | Ex-hedge-fund, finance professor. Dry, skeptical, long, no hype. "Follow the money" framing (4.8M) |
| The Money Guy Show | 712K | 5,753 | 147K | 0.21 | ~10 | 35 min | Two advisers on camera | Credentials (CPA/CFP), data-led episodes ("Are You Richer Than Your Friends?"). Own survey: median listener age 36, 41% in their 40s. Younger than ours |
| Erin Talks Money | 450K | 2,895 | 111K | 0.25 | ~30 | 23 min | On camera | Retirement explainers. "What $300K, $600K, and $900K Will Pay You in Retirement" |
| Rob Berger | 302K | 1,009 | 59K | 0.20 | ~10 | 18.5 min | On camera, unscripted | **Explicitly aimed at 50+.** ~50% returning viewers. Plain desk videos, no music, 3 to 4-word thumbnails. Viewers objected to a music-heavy edit and a 1.15× speed-up |
| James Conole, CFP | 217K | 1,627 | 71K | 0.33 | ~5 | 15 min | On camera | "Social Security at 62 vs 67 vs 70" 939K |
| Nick Davis, CFP (Brindle & Bay) | 102K | 348 | 47K | 0.46 | ~6 | 18.5 min | On camera, charts | 1.7M "Once You Retire, Upgrade These 10 Things…", 803K "…Stop Working Past 58" |
| Eric at The PeakFP | 86.3K | 433 | 34K | 0.39 | ~15 | 24 min | On camera, charts | 1.8M "The Hidden Social Security Math Nobody Shows Retirees" |
| Ken McElroy | 528K | 2,444 | 19K | 0.04 | ~7 | 18 min | On camera (64-year-old investor) | 689K "It Took Me 64 Years To Learn What I'll Teach You In 11 Minutes" |
| BiggerPockets | 1.27M | 4,340 | 27.5K | 0.02 | ~15 | 32 min | Podcast | 229K "Broke at 47, Millionaire at 55 with 'Boring' Rental Properties" |
| Financial Fast Lane | 378K | 243 | 5.1K | 0.01 | ~6 | 15 min | On camera, older host | Social Security news (2.5M and 2.3M peaks). Now decayed |
| Taylor Demars, CFP | 28.3K | 117 | 3.9K | 0.14 | ~4 | 16 min | On camera | 1.4M "My Honest Advice To Anyone Working Past 60… RETIRE NOW" (248× its neighbors) |
| Ramsey Show Highlights | 4.60M | 11,805 | 96K | 0.02 | ~67 | 9 min | Call-in clips | "Why are SBA Loans a Bad Idea?" 220K |
| John's Money Adventures | 296K | 329 | 26.5K | 0.09 | ~10 | 17 min | Faceless cartoon | Dividend income (1.3M) |
| Tom – Lazy Investor | 103K | 563 | 18.5K | 0.18 | **~67** | 33 min | Faceless cartoon | Mass-produced retirement content |
| Investor Intellect | 35.4K | 408 | 943 | 0.03 | ~15 | 16 min | Faceless, AI grey-haired mascot | Mass-produced. Median under 1K |
| Commercial Property Advisors | 269K | 1,276 | 1.5K | 0.005 | ~4 | 17 min | On camera | Self-storage and mobile-home-park primers from 12+ years ago |
| Over50tv | 57.9K | 806 | 899 | 0.02 | ~2.5 | 8 min | On camera | "How to Value a Small Business" 186K (7 years old) |

**The pattern in ring D:** the channels with the best views-per-subscriber (Patrick Boyle 1.10, Nick Davis 0.46, Eric at PeakFP 0.39, James Conole 0.33) are **credentialed, calm and chart-heavy**, and they answer one specific money question per video. The faceless cartoon-mascot retirement channels that mass-produce (Investor Intellect, Tom – Lazy Investor) have far lower medians.

---

## 2. Outliers: videos that beat their channel's norm

"× norm" = views ÷ median of the 20 surrounding uploads on the same channel.

| Channel | Video | Views | × norm | Length | Why it worked (pattern) |
|---|---|---|---|---|---|
| Stephen the Investor | I Bought and Renovated a Car Wash and it Made me $500,000 | 3.7M | 61× | 23 min | Purchase plus dollar result |
| Stephen the Investor | I Spent $425,000 Buying a Self Serve Car Wash, Heres How Much Money it Makes.. | 2.4M | 30× | 24 min | Price paid plus "how much it makes" |
| Investment Joy | Does The Laundromat I BOUGHT 3 Years Ago Make Money? | 848K | 40× | 19 min | Ownership test with real P&L |
| Investment Joy | My Laundromat Made $123,284.10 | 966K | 30× | 13 min | Exact dollar figure to the cent |
| Car Wash Rob | I Spent $3,000,000 Buying Car Washes – Collect 7 Days of Cash With Me | 693K | 27× | 37 min | Big price plus real cash count |
| Codie Sanchez | Businesses that Always Fail? 7 Businesses with Shockingly High Failure Rates [Backed by Data] | 2.8M | 15× | 21 min | Data-backed contrarian list (the inverse of her 5.9M "never fail") |
| Codie Sanchez | I Bought 3 Vending Machines… My Earnings SHOCKED Me! | 2.2M | 4.9× | 24 min | Vending ownership test |
| Brian Beers | I Bought 2 Vending Machines… The Earnings Were Crazy | 608K | 29× | 10 min | Same vending test, copied a year later. Still works |
| Brian Beers | The $60B Business Nobody Talks About | 168K | 124× | 13 min | Market size plus "nobody talks about" |
| David Heacock | 6 BORING Businesses that Always Make Millionaires (90% success rate) | 2.9M | 359× | 16 min | Boring list plus statistic in parentheses |
| David Heacock | You Don't Need to Start a Business. Just Buy One of These. | 1.8M | 37× | 15 min | "Buy, don't start" |
| Kenny Finance | 10 Businesses That Never Fail (and How to Buy Them) | 854K | 683× | 13.5 min | Clone of Codie's title plus a "buy" angle |
| Kenny Finance | Why I'm Buying EMPTY Parking Lots (And You Should Too) | 296K | 47× | 7 min | Unexpected boring asset |
| Tyler Cauble | $30k/Month from A Parking Lot?? | 583K | 149× | 15 min | Monthly income from an unglamorous asset |
| Tyler Cauble | Why Buc-ee's Builds $50 Million Gas Stations | 377K | 157× | 12 min | Familiar place plus dollar figure plus "why" |
| Franchise Inspectors | Why are Gas Stations Selling so Cheap? | 259K | 98× | 7 min | Market anomaly framed as a question to answer |
| Hard Hat Economics (faceless) | Codie Sanchez Sold Her Laundromats… Why Does She Want YOU to Buy One? | 142K | 32× | 10 min | Skeptical reply to a famous guru |
| Hard Hat Economics (faceless) | Why Mechanics Are Done With Dealerships. Ford's CEO Still Doesn't Get It | 424K | 154× | 7 min | Blue-collar insider view plus contrarian take |
| David Explains Money (faceless AI) | 20 BORING BUSINESSES That Make Money While You Sleep | 1.4M | 10.5× | 28 min | Long list with an older-man mascot. A clone of an Indian channel's 2.7M title |
| Mr. Finance (faceless AI) | The Economics of Owning a Cafe | 233K | 17× | 24 min | Template. The rare hit in a 44-a-month stream |
| Modern MBA | Why Crumbl Cookies Can't Survive | 2.3M | 5.1× | 30 min | Familiar brand plus "can't survive" |
| Modern MBA | The Crumbling Business of Marijuana | 1.7M | 7.1× | 54 min | Whole-industry economics |
| PolyMatter | How McDonald's Really Makes Money | 3.9M | 4.5× | 9 min | "How X really makes money" (real estate twist) |
| GEN | How Private Equity Turns Your Favorite Channels Into Slop | 5.2M | 40× | 22 min | Private equity plus something the viewer personally uses |
| CNBC Make It | I Quit My Nursing Job For My Laundromat Business – It Brings In $475K/Year | 1.6M | 5.5× | 10 min | Relatable owner plus annual revenue |
| UpFlip | Is This the Death of Traditional Vending?! ($117 Startup) | 2.0M | 8.2× | 34 min | "Death of" plus a tiny dollar figure |
| Eric at The PeakFP | The Hidden Social Security Math Nobody Shows Retirees | 1.8M | 12.8× | 7.5 min | Same audience: "hidden math" for a named age group |
| Taylor Demars, CFP | My Honest Advice To Anyone Working Past 60… RETIRE NOW | 1.4M | 248× | 18 min | Same audience: direct address by age |
| Nick Davis, CFP | Once You Retire, Upgrade These 10 Things Before Telling Anyone | 1.7M | 68× | 19.5 min | Same audience: life-stage list |
| Ken McElroy | It Took Me 64 Years To Learn What I'll Teach You In 11 Minutes | 689K | 19× | 12 min | Same audience: age and experience as the hook |
| Rob Berger | I Attended a Free Dinner Investment Seminar--Here's what happened. | 326K | 10.5× | 23 min | Same audience: consumer protection, exposing a sales pitch aimed at retirees |
| BiggerPockets | Broke at 47, Millionaire at 55 with "Boring" Rental Properties | 229K | 12× | 36 min | Same audience: late-start success with "boring" assets |

**What the outliers have in common:**
- **A specific dollar figure tied to one asset:** "$500,000", "$123,284.10", "$30k/Month", "$50 Million Gas Stations", "$60B Business".
- **A familiar physical place**, seen from the money side: car wash, laundromat, gas station, parking lot, McDonald's, Crumbl.
- **Ownership proof:** "I bought… here's what it made." Dull Profits can't do this, so it substitutes a document: the Deal File.
- **A contrarian or skeptical turn:** "always fail", "can't survive", "Why… Selling so Cheap?", "…Why Does She Want YOU to Buy One?"
- **For older viewers: age in the title** ("Working Past 60", "64 Years", "Broke at 47") and protection from being sold to ("Free Dinner Investment Seminar").
- **Not length.** Outliers range from 7 to 54 minutes, and the medians match normal videos (about 16 minutes).

---

## 3. Title and format patterns: the numbers

**Title features, outliers vs normal videos.** Normal = less than 1.5× the neighbors.

| Feature | All 72 English channels: outliers / normal (lift) | 21 faceless channels: outliers / normal (lift) |
|---|---|---|
| Contains a $ figure | 27% / 17% (×1.6) | **22% / 12% (×1.9)** |
| Contains any number | 53% / 40% (×1.3) | 42% / 29% (×1.45) |
| A word in ALL CAPS | 19% / 14% (×1.3) | 16% / 10% (×1.6) |
| First person ("I", "my", "we") | 31% / 17% (×1.8) | 7% / 7% (×0.9) |
| Contrarian words ("nobody", "never", "truth", "fail"…) | 15% / 12% (×1.3) | 14% / 12% (×1.15) |
| Question mark | 12% / 16% (×0.8) | **11% / 18% (×0.64)** |
| Word "boring" | 3% / 2% (×1.65) | 2% / 4% (×0.5) |
| Median length | 15.8 vs 15.7 min | 16.9 vs 16.2 min |

How to read this: title features explain only part of what makes an outlier (topic and thumbnail matter more). Still, the direction is consistent:
- **Put the real number in the title.**
- **Make a statement rather than ask a question.**
- **Don't count on "boring" doing the work for a faceless channel.**

**Formulas that recur among outliers in this space:**
1. **"[One asset] makes/made $X"**: "$30k/Month from A Parking Lot", "It Brings In $475K/Year".
2. **"Why [familiar place] [surprising fact]"**: "Why Buc-ee's Builds $50 Million Gas Stations", "Why Buffets Suddenly Disappeared" (842K), "Why are Gas Stations Selling so Cheap?"
3. **"[Industry fact]. [Twist]."**: Modern MBA's "Bars Have 90% Margins. Most Still Go Broke." and "Nobody Makes Money Renting Cars".
4. **"How [X] Really/Actually Makes Money"**: PolyMatter's McDonald's (3.9M), "How Used Car Dealerships Actually Make Money?" (197K).
5. **"Data-backed" lists**: Codie's "[Backed by Data]" (5.9M, 2.8M). This only works for the first mover; the clones rank far lower.
6. **Skeptical reply to a famous claim**: Hard Hat Economics on Codie's laundromats (32×).
7. **Age-addressed (ring D)**: "…Working Past 60", "…at 62 vs 67 vs 70", "…$3M+ Retirees in 18 Minutes".

**Length and cadence:**
- The best faceless explainers in views-per-subscriber (How Money Works 0.47, Wall Street Millennial 0.39, Modern MBA 0.35, GEN 0.35) run 16 to 37 minutes. Their cadence ranges from 2.5 to 10 a month.
- The mass-producers (30 to 67 a month) all sit at medians of 1K to 18K, whatever the topic.

**Thumbnails seen in this space** (from the contact sheets):
- The AI farms use cartoon mascots (often a **grey-haired man in a suit**, clearly aimed at older viewers) or templated AI scenes ("SO YOU WANT TO OWN A…").
- Owners use their face plus the dollar figure.
- Wendover and Modern MBA use one clean object and 2 to 4 words.
- A real document, highlighted, appears nowhere. **The Deal File look is unclaimed.**

---

## 4. Topic gap table

From 122 search queries (first page each). "100K+" and "1M+" count relevant videos found, after removing kids, toys, DIY, gaming, crime news and non-English results. Treat them as relative signals, not totals.

| Topic | Biggest relevant video found | 100K+ found | 1M+ found | Who covers it now | Verdict for Dull Profits |
|---|---|---|---|---|---|
| **Vending machines** | 10.5M Quik Play cash-collection vlog (2022). Best "business" video: CNBC Make It 3.5M | 31 | 13 | Collection vlogs, interview shows, course sellers | **Crowded with vlogs, empty of economics.** Ep1's "follow the $2" angle is differentiated |
| **Laundromats** | 4.9M Investment Joy "Does a laundromat make money?" (2019) | 42 | 8 | Owner vlogs, UpFlip, CNBC Make It | Proven demand. **No explainer.** Strong Ep2 candidate |
| **Car washes** | 3.8M Stephen the Investor (9 months old) | 32 | 4 | One owner-creator dominates. Bloomberg Originals' private-equity car-wash video 329K | **Hottest right now** (20 of the 32 are from the last year). Private equity "express wash" roll-up economics barely covered |
| **Self-storage** | Modern MBA 1.2M and Wendover 1.0M (explainers). Self Storage Income 547K | 10 (+2) | 2 | Two big faceless explainers already did it | **Partly taken.** Needs a fresh angle (mom-and-pop vs REIT math, auctions and delinquency) |
| **Funeral homes / death care** | 5.9M ABC Four Corners (news). Caitlin Doughty 2.0M "$3 Billion Funeral Empire" | 18 | 6 | News investigations, Caitlin Doughty. Owner-economics only by tiny AI channels (<1K views) | **Big gap:** strong curiosity, no calm business explainer. Good for an older audience |
| **HVAC / plumbing / home-services roll-ups** | 1.6M Morning Brew "I started a plumbing company to sell it to private equity". 2.3M CBC (scam) | ~3 business, 11 total | 1 business | Consumer scam exposés, career videos | **Gap with proven demand.** The seller's view ("what private equity pays for your HVAC company") is untouched |
| **Private equity (general)** | 5.3M GEN, 4.0M More Perfect Union, 2.7M Wendover | 38 | 18 | Saturated with "private equity is ruining X" | Don't do generic private equity. Use it as context inside specific-business episodes |
| **Gas stations** | 3.8M CNBC (billionaire), 1.4M UpFlip, Codie 1.6M "Forget Gas Stations…" | 6 | 2 | Interviews | Proven. Moderate competition |
| **Car dealerships** | 8.2M "How Car Dealerships Rip You Off" (consumer). Wendover 1.2M | 23 | 13 | Consumer angle dominates | Possible later ("how a dealer makes money on you", from the owner's books) |
| **Franchises** | 2.2M Mashed "How Much McDonald's Franchise Owners Really Make" | 15 | 3 | Mixed | Proven. Fits "has capital" viewers deciding between a franchise and an independent business |
| **ATMs** | 1.7M TommyBryson "How to start a ATM Business | $3683 Per Month" (7 years old) | ~3 | 1 | Hustle channels, old | **Gap.** Ideal for The Split (surcharge, interchange, placement, cash loading) |
| **Billboards** | 307K Codie Sanchez | 4 | 0 | Thin | Open. Modest demand |
| **Parking lots** | 583K Tyler Cauble | 3 | 0 | Thin | Open. Modest demand |
| **Mobile-home / RV parks** | 703K "Your Life at Every Level of Living in an RV Park"; Codie 458K | 8 | 0 | Real-estate educators | Moderate. A 55+ angle exists ("$780 lot rent became $1,640: retiring to a 55+ park" 157K) |
| **Portable toilets / septic** | 1.3M CNBC Make It "My Porta-Potty Business Brings In $4.3M/Year" | 4 | 1 | Thin | Open, quirky, good for The Split |
| **Dry cleaning** | 371K | 3 | 0 | Thin | Open ("dying industry" angle) |
| **Pest control** | about 100K (a Hindi explainer) | 1 | 0 | Almost nothing | Open but **demand unproven**. Best as a private-equity roll-up story (big national firms buying local ones) |
| **Dental / vet private equity** | 1.06M More Perfect Union, 891K Tucker Carlson | 2 | 1 | Politically charged | Possible. Handle neutrally |
| **Pressure washing / junk / landscaping** | 11.5M "I MADE $1000 IN 1 DAY PRESSURE WASHING ROOFS" | 39 | 6 | Young hustle creators | Wrong audience (start-from-zero hustle) |
| **"N boring businesses" lists** | Codie 5.9M; Heacock 2.9M; AI channels 2.7M, 1.7M, 1.5M (last 4 months) | 38 | 14 | Saturated, cloned titles | **Avoid as a format** |
| **Buying a business / ETA / SBA** | Codie 1.0M "How to Buy a Business With No Money" (3 years old) | 25 | 0 | Codie plus small ETA podcasts (medians under 10K) | Moderate demand. Nobody makes it visual and calm |
| **Selling / valuing your business** | 743K "Value a Small Business like Warren Buffett" (**14 years old**) | 4 (none in the last 5 years) | 0 | Broker and exit channels with medians under 1K | **The largest supply gap**, aimed squarely at the "might sell" viewer. Lower view ceiling, but the highest sponsor value |

---

## 5. Policy update: concrete enforcement against faceless channels (2026)

Section C2 of the earlier report already covers the policy text. New concrete examples found:

- **January 2026:** YouTube terminated or wiped **16 channels with about 35M subscribers and 4.7B lifetime views**, estimated at about $10M a year in revenue. Eleven were terminated and five had their content removed.
  - Named channels include Héroes de Fantasía, Super Cat League, CuentosFacianantes and Imperiodejesus.
  - **These were AI fiction, animal and religious "slop" channels, not business explainers** (IBTimes, Tribune, TheNextWeb).
- **Channel-level review:** TheNextWeb (June 2026) reports that monetization can be pulled from a whole channel based on a pattern across its **last 30 uploads**.
- **A faceless narrative channel, not spam, was hit:**
  - A Bible-story channel with about 588K subscribers and about $30K a month was reportedly fully demonetized for "inauthentic and mass-produced content".
  - It was described as "AI-assisted but not AI spam", and an appeal was pending.
  - This comes from a single creator-tools blog (Fliki), so treat it as unconfirmed.
- **Creator sentiment:**
  - The Hollywood Reporter quotes a 1.7M-subscriber creator: "the people who do the same content as me without their face in it, most of them are getting demonetised."
  - Some faceless operators are reportedly hiring on-camera hosts through Fiverr and Upwork.
- **In this niche specifically:**
  - The mass-producers are still live as of today: Mr. Finance (~44 a month), Ned Talks Business (~33), Harry's Stealth Wealth (~30), Tom – Lazy Investor (~67). We cannot see whether they are monetized.
  - **No business-explainer channel was found named in any enforcement report.**
  - The risk signal is the template plus the cadence ("The Economics of Owning a ___", identical thumbnails, 30+ a month), not the AI voice itself.

What this means: stay low-cadence (2 to 4 a month), make every episode's graphics and research unique, avoid a fill-in-the-blank title template, and never use an AI persona presented as a human adviser.

---

## 6. Best channels to study (top 10, across all rings)

| Rank | Channel | Copy this | Avoid this |
|---|---|---|---|
| 1 | **Modern MBA** (faceless, 854K, 295K median) | Whole-industry unit economics of familiar places (bars, buffets, gyms, self-storage). "[Fact]. [Twist]." titles. Only 85 uploads, yet 0.35 views per subscriber: quality over quantity works | 40 to 60 minute runtimes are too much before trust exists. Start at 12 to 18 minutes |
| 2 | **Stephen the Investor** (on camera, 147K, 3.7M/2.8M/2.4M hits) | Proof that car-wash P&L numbers draw millions. Put the purchase price and profit in the title; show the books | First-person "I bought" framing we can't do, and unaudited claims. Our substitute is the Deal File |
| 3 | **Patrick Boyle** (on camera, 1.37M, V/S 1.10) | The tone for a wealthy, older, skeptical audience: dry, sourced, unhurried, "follow the money", long and dense | Relying on a personality and jokes. Our voice is the documents and graphics |
| 4 | **Wendover Productions** (faceless, 4.92M) | "How [X] Quietly Consumed America" systems framing, maps, a calm voice. Dollar stores 4.2M; self storage 1.0M | High production cost. Topics too broad for our niche |
| 5 | **Rob Berger** (on camera, 302K, 50+) | What 50+ viewers want: plain, "a real answer", no background music, no speed-ups, 3 to 4-word thumbnails, a newsletter for returning viewers (about 50% return) | Unscripted desk format (needs a face) |
| 6 | **Codie Sanchez** (on camera, 2.28M) | Owns the topic's search demand. Her "[Backed by Data]" failure-rate lists (5.9M, 2.8M) and vending test (2.2M) show which questions people ask | Hype ("SHOCKED"), course funnel, wealth-guru framing. This is the contrast we should stand against |
| 7 | **How Money Works** (faceless, 1.77M, V/S 0.47) | Faceless explainers with strong views per subscriber. Private-equity topics (1.4M, 1.2M, 964K) prove the audience for roll-up economics | Sarcastic-caps titles ("tHe pOpULaTiOn…") and a doom tone. Wrong for 55+ viewers |
| 8 | **Wall Street Millennial** (faceless, 372K, V/S 0.39) | Cheap, document-led, deadpan, 10 a month without looking templated. Filings on screen | Snark and tech-stock focus |
| 9 | **Nick Davis, CFP / Eric at The PeakFP** (on camera, V/S 0.46 / 0.39) | Same-audience hooks ("…Working Past 58", "Hidden Social Security Math Nobody Shows Retirees"). Real-number charts on screen | Clickbait drift ("Before Telling Anyone") |
| 10 | **Hard Hat Economics** (faceless, 18.3K, V/S 0.38) | The closest faceless competitor in spirit: blue-collar economics, 7 to 10 minutes, a skeptical reply to Codie's laundromat pitch hit 32× | Photo-real AI thumbnails of people (credibility and labeling risk), and "career bubble" doom |

A **cautionary study**: David Explains Money (faceless AI, 6 videos, 1.4M hit, an older-man cartoon mascot). It shows that older viewers will click a "boring business" list from a faceless channel. It also shows how easily that slot is filled with cloned titles and no sourcing. If our early episodes are cheap lists, we compete with it.

---

## 7. What this means for Dull Profits

1. **Own "one business, one transaction, real numbers".**
   - Every outlier in the direct ring ties a dollar figure to a single asset. The faceless channels that do this today are AI list farms with no sources.
   - Dull Profits should be the only channel where **every number has a document on screen**. The Split plus the Deal File is a visual identity nobody in this space uses.
2. **Write titles as a statement with a real number, not a question.**
   - The data supports this: a $ figure gives ×1.9, a number ×1.45, a question mark ×0.64.
   - Episode 1 candidates in the formats that worked:
     - "A Vending Machine Sells $900 a Month. The Owner Keeps $197."
     - "Who Actually Gets Your $2 at a Vending Machine"
     - "LAX Takes 59.5% of Every Vending Sale. Here's Where the Rest Goes."
   - Avoid "boring", "passive" and "SHOCKED".
3. **Choose topics in this order** (demand proven, calm explainer supply thin):
   - car washes (the private-equity express-wash boom),
   - laundromats,
   - funeral homes,
   - HVAC/plumbing roll-ups (seller's view),
   - ATMs,
   - selling or valuing your business.
   - Self-storage is already explained twice at about 1M views each. Come back to it with a different angle.
4. **Build a "what's it worth / should I sell" strand for the viewer with capital.**
   - No sell-side or valuation video has passed 100K views in five years, and the people who make them (brokers) get under 1K a video.
   - A visual, calm "Deal File: listing teardown" (asking price vs. real cash flow, using BizBuySell-style listings, anonymized) would be unique.
   - It is the format Acquisitions Anonymous proves works for an audio audience of operators.
   - Expect lower views but much higher sponsor value (brokers, SBA lenders, accountants).
5. **Use age and life-stage hooks the way the retirement channels do.** For example:
   - "Selling Your Business at 62: What Buyers Actually Pay"
   - "Buying a Laundromat at 55: The Real Payback Math"
   - The same-audience outliers (1.4M "Working Past 60", 689K "It Took Me 64 Years") show that addressing age directly works with this viewer.
6. **Match the trust signals of the best same-audience channels:**
   - Calm narration at about 135 to 145 wpm, with no speed-up.
   - No music under numbers.
   - Sources on screen, and dates on every statistic.
   - A "not financial advice" line.
   - A short, honest description that says the narration uses a synthetic voice.
   - This audience punishes hype and heavy editing (Rob Berger's comments). Patrick Boyle's dry skepticism gets the best views-per-subscriber in the set.
7. **Stay far from the mass-production pattern.**
   - The channels at 30 to 67 uploads a month with templated "Economics of Owning a ___" titles have medians of 1K to 18K, and they match the profile YouTube is enforcing against.
   - Aim for 2 to 4 episodes a month, a unique research question and unique graphics per episode, and titles that are not fill-in-the-blank.
8. **Occasionally answer the famous claims.**
   - A calm, sourced "reality check" of a widely repeated guru claim works for a small faceless channel. Hard Hat Economics' reply about Codie's laundromats ran at 32× its norm.
   - Examples: "Do 90% of these businesses really never fail?", "What a vending course doesn't show you", "Codie says buy a laundromat. Here's the math at 2026 prices."
   - Keep it about the numbers, never personal.

**Candidate differentiators (summary):**
- The Split, with the same colors every episode.
- The Deal File: real documents, highlighted.
- An age-aware "buy, own or sell" framing for people with capital.
- TV-readable graphics.
- A calm, sourced tone with no hype.
- Listing teardowns.
- Seller-side private-equity roll-up episodes.

---

## Sources

Data (collected Nov 26, 2026): YouTube channel "Videos" tabs and uploads playlists via yt-dlp 2026.11.23; YouTube search-result pages (first page, relevance and view-count sorts). Raw files are in the scratchpad folder listed under Method.

Articles and pages:
- TheNextWeb (Jun 15, 2026), "YouTube's AI slop purge is punishing the human creators who never showed their faces": https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage
- IBTimes UK, "16 Channels With 35 Million Subs Just Got Wiped Out": https://www.ibtimes.co.uk/youtube-cracks-down-ai-generated-content-1800213
- Express Tribune (Jan 30, 2026), "YouTube deletes 4.7 billion views worth of AI spam videos": https://tribune.com.pk/story/2589917/youtube-deletes-47-billion-views-worth-of-ai-spam-videos-in-major-platform-crackdown
- Hollywood Reporter, faceless creators and YouTube AI (quoted via search summary; paywalled): https://www.hollywoodreporter.com/business/digital/faceless-creators-youtube-ai-damage-1236617586/
- Fliki blog (unconfirmed single source for the 588K Bible channel): https://fliki.ai/blog/youtube-ai-demonetization
- WinBuzzer (Jul 23, 2026), "YouTube Draws Three Monetization Lines Around AI Slop": https://winbuzzer.com/2026/07/23/youtube-draws-three-monetization-lines-around-ai-slop-xcxwbn/
- My Wife Quit Her Job podcast ep. 516, Rob Berger interview (50+ niche, ~50% returning viewers, audience reactions to editing): https://mywifequitherjob.com/episode516/
- Rob Berger, About page (audience approaching or in retirement): https://robberger.com/about-me
- Money Guy Show listener survey figures (median age 36; 41% in their 40s), via Podscan and moneyguy.com: https://www.podscan.fm/podcasts/money-guy-show , https://moneyguy.com/episode/are-you-richer-than-your-friends-2025-edition/
- RePlay Magazine / Input on vending YouTubers (Jaime Ibanez channel earning about 3× his route): https://www.replaymag.com/?p=13492 , https://www.inputmag.com/culture/vending-machine-youtubers
- Yahoo News, "Making fast money on vending machines: Is it that easy?": https://www.yahoo.com/news/making-fast-money-vending-machines-145926413.html
- Searchfunder, skeptical take on zero-down laundromat deals: https://searchfunder.com/post/summer-of-alternative-financing-zero-down-codie-sanchez-laundromat-deals-assets-or-liabilities
