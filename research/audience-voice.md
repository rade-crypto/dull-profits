# Audience Voice: What Viewers of Competing Content Say

**For:** Dull Profits (calm, sourced explainers on buying, owning and selling unglamorous small businesses)
**Date:** November 26, 2026
**Question:** What do people who watch or read "boring business" content praise, distrust and get annoyed by, and what do they keep asking that nobody answers?

---

## The short version

1. **"It's not passive" is the most common reaction by far.** Owners in every community we could reach say the same thing in nearly the same words: you are buying a job, on call seven days a week.
2. **The most-liked criticisms are about missing numbers, not hype tone.** The top review of *Buy Then Build* (45 likes) attacks it for counting the owner's own wage as "return" and leaving out taxes and personal guarantees.
3. **People assume the course is the real product.** The most-liked review of Codie Sanchez's *Main Street Millionaire* (44 likes) asks why someone who owns "over 23 businesses" is selling a $2k course and a $10k membership.
4. **Owners mock the cash-pile shots.** Car wash operators say cash pulled from a bill changer is not revenue. They also say a money-counting video gets 100 times the views of an honest repair video.
5. **Experienced owners trust three things:** tax returns, the lease and the age of the equipment. Their advice is consistent: "3 years tax returns are the only numbers you should trust."
6. **AI voice is not rejected outright, but it is the main tell for "slop."** Viewers name specific triggers: mispronunciations, awkward pauses, repetitive scripts, barely relevant stock footage, epic music and long intros. Older viewers are the ones being fed slop, and their adult children notice.
7. **The seller's side is almost unserved.** Buyers get endless content. People with a business to sell, and the 50 to 65+ owners this channel targets, get very little.

---

## 1. Method, and what we could and couldn't access

**Approach:** We collected public comments and reviews from communities where people discuss boring-business content and buying small businesses. We scanned roughly 350 posts, reviews and comments, and coded the about 110 that spoke to these questions into themes.

**What worked (all normal public pages or public APIs):**

| Source | What it gave us | Engagement signal used |
|---|---|---|
| **BiggerPockets forums** (real-estate investors; skews older and has capital) | ~145 posts across 20 threads on laundromats, vending, car washes and buying businesses; ~45 relevant | Likes per post (from the page's structured data) |
| **Car Wash Forum** (carwashforum.com; working operators, some with 30+ years) | ~45 posts across 4 first-time-buyer threads | Reactions per post |
| **Goodreads** reviews of the books behind the competing channels: *Main Street Millionaire* (Codie Sanchez), *Buy Then Build* (Walker Deibel), *The Sweaty Startup* (Nick Huber), *HBR Guide to Buying a Small Business* | ~120 reviews loaded, ~75 read closely, with star ratings | Likes per review; rating distributions |
| **Hacker News** (comment search API plus full threads on vending economics, car washes, self-storage, private equity and AI slop) | ~45 relevant comments | Story points; reply counts per comment (HN hides comment scores) |
| **Trustpilot** pages for vending "done-for-you" and locator companies | 9 reviews | Number and share of 1-star reviews |
| **News articles quoting Reddit threads and owners** (Benzinga via Yahoo/Briefly, Entrepreneur on WSJ, NewsNation, Fortune, Freakonomics, Input) | Secondhand Reddit quotes; owner and expert quotes | None (upvotes not reported) |
| **Surveys** (Raptive, Adobe, Animoto, Pew, YouGov via Martech, Kapwing) | Data on trust in AI content and AI voices | Survey percentages |

**What we couldn't access:**
- **Reddit was fully blocked in this environment.** Direct pages and `.json` returned "You've been blocked by network security". WebFetch refused the site, and web search excludes reddit.com. We did not use mirrors or archives to get around the block.
  - Reddit voices appear here only where news articles quoted them, so **we have no Reddit upvote counts**.
  - This is the biggest gap. r/vending, r/laundromat and r/smallbusiness are the closest communities to our audience.
- **YouTube comments were off-limits by instruction.** We did not try to scrape them.
- **Some sites block bots:** vendiscuss.net (the main vending operator forum), selfstoragetalk.com, Quora, Fishbowl, Blind, and BBB complaint pages. Benzinga and Moneywise were blocked directly, though some of their articles were readable through syndicated copies (Yahoo, Briefly). Most AOL copies now return 404.
- **Searchfunder** (the search-fund and ETA community; ETA means entrepreneurship through acquisition, i.e. buying an existing business) shows opening posts publicly, but its comments require a login.

**How to read the numbers:**
- **Engagement is small and uneven across platforms.** 45 likes on Goodreads and 13 reactions on a trade forum are both strong for their venues, but they can't be compared with each other.
- **The sample is not random.** Read the counts as "how often this came up in what we found," not as population shares.
- **The signal is agreement across communities.** The same four complaints show up independently among real-estate investors, car wash operators, book readers and tech workers:
  1. it isn't passive;
  2. the numbers leave things out;
  3. the course is the product;
  4. location and lease are the real asset.

Raw notes and scrapes are kept outside the repo, because the repo is public.

---

## 2. Theme table

"Voices" means distinct people or sources coded to the theme, out of about 110 coded items.

| # | Theme | Voices | Strongest engagement | Mostly from |
|---|---|---|---|---|
| 1 | **"It's not passive; you're buying a job"** | ~26 | Laundromat owner's write-up, 43 likes (BiggerPockets); "2% of the business" reply, 13 reactions (Car Wash Forum) | BiggerPockets, Car Wash Forum, Reddit via press, owners in WSJ/Freakonomics |
| 2 | **"The numbers leave things out"** (the owner's wage counted as profit, taxes, repairs, cash taken out of a machine counted as revenue) | ~17 | Top *Buy Then Build* review, 45 likes; second review, 14 likes | Goodreads, Hacker News, Car Wash Forum, BiggerPockets |
| 3 | **"The guru is selling the course; the content is the real business"** | ~11 | Top *Main Street Millionaire* review, 44 likes | Goodreads, BiggerPockets, Hacker News, Car Wash Forum |
| 4 | **Location, lease and real estate are the real asset** | ~11 | HN "real business of car washes is real estate," 17 replies; HN vending economics thread, 251 points | Hacker News, BiggerPockets, operators |
| 5 | **Scams: locators, done-for-you packages, turnkey routes** | ~12 | VendPros: 5 of 6 Trustpilot reviews are 1-star ($30k and $50k losses claimed) | Trustpilot, BBB, Substack, vending forum |
| 6 | **"Too thin": wanted real case studies, real P&Ls, specifics** | ~11 | 9 likes and 8 likes (*Main Street Millionaire* 1-star reviews) | Goodreads, BiggerPockets |
| 7 | **AI voice as the tell for low-effort "slop"** | ~13 (9 comments, 4 surveys) | AI Slop Report thread, 159 points; Raptive: suspected AI cuts trust about 50% | Hacker News, surveys |
| 8 | **Cash piles, quarter buckets, "$700K" titles** | ~9 | "Brag about the revenue" reply, 5 reactions | Car Wash Forum, press |
| 9 | **Verify everything: 3 years of tax returns; cash gets skimmed** | ~9 | "Tax returns are the only numbers you should trust," 11 reactions | Car Wash Forum, BiggerPockets, Searchfunder |
| 10 | **Equipment and repair surprises** | ~9 | "You... are probably going to spend triple that year 1," 6 reactions | Car Wash Forum, BiggerPockets, Freakonomics |
| 11 | **Ethics: low wages, raising prices, private equity** | ~8 | HN PE thread, 552 points; one 1-star review, 6 likes | Goodreads, Hacker News |
| 12 | **Praise: honest about costs and problems** | ~8 | 11 likes; 8 likes | Goodreads, HN, Car Wash Forum, BiggerPockets |
| 13 | **Financing myths: $0 down, seller financing, personal guarantees** | ~7 | Laundromat seller's "5 lessons" post, 16 likes | BiggerPockets, Goodreads, newsletters, r/smallbusiness via press |
| 14 | **Padding, long intros, repetition** | ~7 | (low) | Goodreads, Hacker News |
| 15 | **Stock footage is generic or irrelevant** | ~6 | (low; comments sit in slop threads) | Hacker News |

---

## 3. What people say, by theme (verbatim)

Quotes are copied as written, typos included. "BP" means BiggerPockets and "CWF" means Car Wash Forum.

### Theme 1: "It's not passive; you're buying a job"

- > "Management, finances, and all that corporate stuff is about 2% of the business... Dont expect to pick up money once a week and thats it... Dont judge this business off a you tubers videos... go get a job or even volunteer at a local car wash and work it for a few months then you can decide if your built for it or not. MOST ARE NOT."
  - Car wash operator "Blanco," CWF, Aug 5, 2025, **13 reactions**
  - [thread](https://www.carwashforum.com/threads/prospective-1st-time-owner-where-to-even-start.26313/)
- > "DON'T BELIEVE YOUTUBERS . There are a few with videos still being circulated that have gone broke. It's not an unattended or passive business. It's a 7 day a week job. I like to say it will be the easiest 80 hour a week job you'll ever have."
  - Equipment technician, CWF, Aug 6, 2025, **11 reactions** (same thread)
- > "They are not the passive income dream that some influencers will have you believe they are... In a typical week, we would work 7-10 hours... We never hired a manager because it simply would have taken too much out of our profits."
  - Laundromat buyer and seller (bought for $190k; earnings before owner pay, or SDE, about $77k; sold for $300k after 16 months), BP, Nov 15, 2024, **43 likes**
  - [thread](https://www.biggerpockets.com/forums/961/topics/1219064-what-i-learned-from-owning-and-selling-a-laundromat-exploring-a-different-asset-cla)
  - Her follow-up: "People think they're just going to hire a manager to solve all their problems and make the investment passive for them, but it's not that simple."
- > "A Laundromat without a lease is a truck load of used equipment... Paying a Service Tech $100+ to come out an un-jam a quarter will wipe you out... it will not be as passive as rental properties. More like a motel then an apartment building."
  - Owner of 5 laundromats, BP, May 2, 2019, 3 likes
  - [post](https://www.biggerpockets.com/forums/88/topics/703075-coin-laundry-business-is-it-passive-income#post_4148744)
- > "Operating a laundromat felt far closer to running a small convenience store than a hands-off investment."
  - Laundromat owner, BP, Dec 23, 2025
  - [thread](https://www.biggerpockets.com/forums/961/topics/1272463-are-laundromats-really-passive)
  - A reply in the same thread: "most insurance company won't ensure the laundromat without a employee present... It has been anything but passive."
- > "Vending is NOT fully passive income. I'd call it semi-passive, like 70% passive."
  - Reddit vending operator, quoted by Benzinga, Apr 9, 2026
  - The same operator: "Look for a location before ANYTHING."
- > "Maybe it's ambition or maybe all of the 'passive income' slop somehow seeped into me."
  - Reddit r/smallbusiness poster who bought a gym, via Benzinga/[Yahoo](https://finance.yahoo.com/news/took-over-commercial-gym-says-183141522.html), Feb 8, 2026
- **r/smallbusiness, as summarized by Benzinga (Jul 2025):**
  - Operators warned that "a $200,000 business typically generates around $50,000 to $60,000 in seller discretionary earnings. In other words, you're likely 'buying a job.'"
  - We could not open the original article. This comes from a search summary.
- > "Watching videos about buying a laundromat and buying a laundromat are very different activities... The gap between stated intent and closed transactions is enormous, and it's where the hype lives."
  - Prof. Scott Shane, [Fortune](https://fortune.com/2026/08/09/gen-z-founders-laundromat-moved-across-country/), Aug 9, 2026
  - BizBuySell recorded fewer than 10,000 completed business sales in 2025.
- > "People are getting trapped into looking at all these videos that glamorize the industry"
  - Carlos Ochoa, the "Laundromat Money" TikTok creator (2M followers) who helped start the trend
  - [Entrepreneur on WSJ](https://www.entrepreneur.com/business-news/tiktok-made-owning-a-laundromat-look-like-easy-money-now-some-owners-are-airing-the-dirty-laundry), Oct 20, 2026

### Theme 2: "The numbers leave things out"

- > "This book grossly oversells the opportunity of entrepreneurship through acquisition and irresponsibly excludes numbers that go against the book's pitch... SDE should not be included in its entirety in your return because a part of it (or all of it) is the salary for the 8-12 hour days you are putting in to run the business... Business taxes are for some reason completely excluded from ROI calculations... SBA loans... require you to personally guarantee all loans"
  - 2-star review of *Buy Then Build*, Goodreads, Jun 25, 2020, **45 likes (the most-liked review on its Goodreads page)**
  - [book page](https://www.goodreads.com/book/show/42591890)
- > "you can't just calculate investment returns without considering when you recieve the money... buying businesses by borrowing 90% of the money and using your own assets as collateral is absurdly reckless."
  - 2-star review of *Buy Then Build*, Goodreads, 2019, **14 likes**
- > "My favorite are the ones who make a big show of taking cash out of their bill changers and brag about the 'revenue'."
  - Equipment technician, CWF, Aug 7, 2025, 5 reactions
  - A bill changer just swaps bills for quarters, so that cash is the customer's money, not sales.
  - The same technician: "one young lady that had a decent presence that ultimate lost the site to the bank in under 24 months."
- > "These are content creators and they know what sells. People love to see the buckets of quarters or stacks of bills... how to rebuild a hydrominder 506... might get 1k views in a year or two if you're lucky, or you can create a money collection video showing stacks of cash and get 100K views in a couple weeks."
  - Car wash operator, CWF, Aug 7, 2025
- > "Maintenance seems low for a wash doing 640k. My guess is they are doing a lot of work themselves and not putting it on the books. You having no experience are probably going to spend triple that year 1."
  - CWF, Mar 26, 2024, 6 reactions
  - [thread](https://www.carwashforum.com/threads/need-help-with-1st-carwash-purchase.23773/)
  - Another reply: "I'd plug in 5% of gross for repair expenses... If an express tunnel comes close into the market could lop 30% off your gross."
- > "Owners typically don't pay themselves which inflates profits which is one reason not to use the numbers."
  - Would-be laundromat buyer, BP, May 2, 2019 (coin-laundry thread above)
- **Hacker News, "The economics of vending machines"** (251 points, 163 comments), [thread](https://news.ycombinator.com/item?id=24678064):
  - > "Here's the real lede: > Ibanez's YouTube channel... now earns more than his machines. The margins on vending machines are tiny"
  - > "The gross margin on each product is about 40%, you then lose 15-25% on stocking... plus... gas, a car, insurance, repairs... You're getting maybe 5% net margin."
- > "The case studies? Cherry-picked success stories that conveniently ignore the thousands who followed similar paths and failed miserably. The financial calculations? Hilariously optimistic"
  - 1-star review of *The Sweaty Startup*, Goodreads, Apr 29, 2025
  - [book page](https://www.goodreads.com/book/show/216950437)

### Theme 3: "The guru is selling the course"

- > "if buying businesses is soooo profitable and easy then why is she selling the American Dream via a $2k online course and an annual $10k community membership? Wouldn't someone with like over 23 businesses be like super busy?... I'm not sure I'm buying what she's selling…"
  - 2-star review of *Main Street Millionaire*, Goodreads, Dec 16, 2024, **44 likes (the most-liked review on its Goodreads page)**
  - [book page](https://www.goodreads.com/book/show/209455833)
- > "you could get all the info for free by following her on social media. Also it just doesn't have enough details to really help buy a business. It seems more like a long winded sales pitch for her paid courses and 'communities'."
  - 1-star review, Goodreads, Jan 26, 2025, 9 likes
- > "she never walks the reader through a single detailed success story in the book."
  - 1-star review, Goodreads, Aug 25, 2025, 8 likes
- > "I would be skeptical of jumping into a business based on YouTube videos hosted by and featuring people that are likely primarily trying to sell you their respective courses... It isn't as simple as 'buy my laundromat' and print money."
  - BP, Aug 24, 2023, 3 likes
  - [post](https://www.biggerpockets.com/forums/961/topics/1137721-buying-small-businesses#post_6493350)
- On a well-known car wash YouTuber:
  > "I believe he made a lot more money (someone somewhere said seven figures)off his YouTube content than anything else."
  - CWF, Aug 2025
- **Context:** *Main Street Millionaire* is still rated **4.33 from 3,536 ratings**. Only about 3% of ratings are 1 or 2 stars.
  - Critics are a minority, but they are the most-liked minority.
  - Fans praise the clear step-by-step structure, the tone, and that it is "motivational and realistic" (5-star review, 11 likes).

### Theme 4: Location, lease and real estate are the real asset

- > "the name of the game is location location location... there's likely already a machine in such location... you have to have many machines"
  - HN vending economics thread
- > "My guess is that the most 'gold mine' locations are already controlled by entrenched players... all the marginally profitable locations are competed over by amateurs who routinely lose money and get disillusioned."
  - Same thread
- > "The real business of car washes is real estate"
  - HN, Mar 17, 2024, **17 replies** (the most-replied comment in a 599-comment thread)
  - [thread](https://news.ycombinator.com/item?id=39735096)
  - It drew a fact-check reply: "Is there any evidence of this? Companies like Mister Carwash lease nearly all their properties... they run 436 sites and lease 427."
- > "The real winner is the one who owns the real estate under the business."
  - BP laundromat thread, Jan 11, 2024
- > "it seems easier than it really is... demand is not elastic: if you build a second site in town you go from 100 units with 90 used... [to] 200 units in town but still only 90 used."
  - HN self-storage thread (282 points, 456 comments), Sep 17, 2026
  - [thread](https://news.ycombinator.com/item?id=49740260)

### Theme 5: Scams (locators, done-for-you packages, turnkey routes)

- **[VendPros on Trustpilot](https://www.trustpilot.com/review/www.vendpros.net):** 2.5 out of 5. Five of six reviews are 1-star (Jun to Jul 2025):
  - "Total con, DO NOT 'INVEST'" ($30k)
  - "I was misled into investing $50,000…" ("many of these reviews appear suspicious or inauthentic")
  - "All the reviews are fake and made up some how."
- **[A vending locator on Trustpilot](https://ca.trustpilot.com/review/vendinglocationpro.com):** all three reviews are 1-star (2025):
  - "He provided me with 'leads', not actual locations."
  - "he does not give refunds"
- **Vending forum, from a search summary (not verified):**
  > "Within pre-pay, there are two kinds: ones that sell you locations, and ones that steal your money."
- **[Substack](https://kalebgorman.substack.com/p/how-to-avoid-vending-machine-scams), May 18, 2023,** written after someone close to the author was hit:
  - The money is made by the people selling the machines and "the idea of easy, passive income."
  - > "You'll be promised $100 +/month. Not likely."

### Theme 6: "Too thin: show me a real one"

- > "I was hoping this book would go into much more detail. If you've already listened to the podcast... this book will read like a bunch of episodes jammed together."
  - *Sweaty Startup* reviewer, 2025
- > "Examples or anecdotal evidence not credible or convincing as they lack concrete sources and hard numbers."
  - *Buy Then Build* reviewer, 2021
- > "A solid, yet detail-sparse overview..."
  - *HBR Guide* reviewer, 4 likes
- > "One of the most common questions I get about laundromats and other small businesses is how to value them."
  - Laundromat seller, BP, Jan 2025
- > "I would love to buy a car wash or laundry mat. I dont know how to evaluate a business like this or secure funding."
  - BP, Aug 13, 2025

### Theme 7: Cash piles, quarter buckets and clickbait

- Owners on CWF on the money-collection genre:
  - "About 15 minutes of counting cash and playing with quarters."
  - "Certainly a lot more exciting than watching a money counter and coin sorter for 15 minutes!"
  - A sarcastic suggestion, Aug 11, 2025, 5 reactions: "We should also post pics of the Ferraris we drive and Rolex's we wear while we show up once a week to pick up the money."
- **The press describes the same genre:**
  - "videos of influencers collecting quarters" ([Freakonomics](https://freakonomics.com/podcast/laundromats/), Nov 2025)
  - titles like "2-Day Workweek Earns $700K" ([NewsNation/Yahoo](https://www.yahoo.com/news/making-fast-money-vending-machines-145926413.html), Feb 2025)
  - a 21-year-old vending YouTuber who reported $5k to $10k a month from YouTube ads, against $10k to $12k a month from his roughly 30 machines ([Input](https://www.inverse.com/input/culture/vending-machine-youtubers), Feb 2022)

### Theme 8: Verify everything

- > "3 years tax returns are the only numbers you should trust. Everything else can be cooked."
  - CWF, Aug 6, 2025, 11 reactions
  - The forum's moderator, in another thread: "you use tax returns to verify income" (5 reactions).
- > "Because it is a cash based business some owners will say I made 'X' but only reported 'Y'."
  - BP, 2019
- > "Also a cash business. He knew he was leaking money. He automated to no cash except for the vending machines. His revenue increased 25% immediately."
  - BP, Dec 23, 2025, 2 likes
- > "SBA lenders underwrite to the tax returns, so if those don't show a profit (at or least a profit after reasonable add backs), you likely don't have a deal."
  - Laundromat seller who is also an SBA loan broker, BP, Jan 2025

### Theme 9: Financing myths

- > "Some had clearly heard about buying a laundromat on YouTube and just wanted someone to listen to their brilliant plan to buy five laundromats in the next year... there's been an unrealistic expectation set by the gurus that relying on seller financing is a viable strategy... the good deals are not being done with high levels of it."
  - Laundromat seller, BP, Jan 6, 2025, **16 likes**
  - [thread](https://www.biggerpockets.com/forums/961/topics/1225054-5-lessons-learned-from-selling-my-laundromat)
- **r/smallbusiness, via a Benzinga search summary:** "sellers prefer buyers with [SBA] loans because they can receive 80-100% of the purchase price at closing"
- **[Still Searching newsletter](https://stillsearching.beehiiv.com/p/you-ve-been-lied-to-about-buying-businesses), Jun 23, 2025:** lists the influencer claims it calls misleading:
  - "You CAN buy a business with $0 down."
  - "You CAN secure 100% seller financing."
  - "Ownership CAN be passive."
- **A business broker reviewing *Buy Then Build* (2026):**
  > "I hate how many times the author suggests... call brokers and build relationships with them so they call you before bringing deals to the marker. Frankly you're cooked pal... My loyalty is to my client, the seller"

### Theme 10: What gets praised

- > "There's a guy Investment Joy on YouTube... Just a pretty normal guy who runs a few small businesses... He talks about the various costs and problems, too."
  - HN, Sep 18, 2026
  - [comment](https://news.ycombinator.com/item?id=49748989)
  - A car wash operator who described these creators as content creators who "know what sells" still conceded that the same channel's "latest videos are telling of the true nature of the business."
- > "I have built, bought and sold a number of businesses over the past 20 years, and have read plenty of garbage from people who either don't know the reality of running a business... or are regurgitating some get-rich-quick garbage... But this book was very different."
  - *HBR Guide* reviewer, 8 likes
  - The *HBR Guide*, the most sober book of the set, also has the highest rating: 4.41.
- > "Your point about laundromats not being completely passive is super important; I feel like that gets glossed over a lot in online discussions."
  - BP, Dec 30, 2024
- > "I think if anything this book convinced me not to buy a business right now... Not passive at all."
  - 4-star review, Goodreads, May 2025
  - Readers give credit for honesty even when it talks them out of buying.

---

## 4. AI voice, faceless channels and stock footage

**What viewers say** (Hacker News; comment scores are hidden, so the thread's points are shown):

- > "I'm observing this with my dad. He watched some genuine history documentaries on YouTube, and now the feed keeps showing him AI slop history videos. You know the type: an hour long, overdramatic AI voice with pronunciation issues, barely relevant stock footage, loads of factual mistakes and nonsensical sentences, epic Hollywood music on a loop... He knows it's crap, keeps making fun of the horrible AI voice... and yet, he keeps watching them."
  - Dec 29, 2025, in the "AI Slop Report" thread (159 points, 171 comments)
  - [comment](https://news.ycombinator.com/item?id=46419192)
  - In the same thread: "I surprised my father once watching these kind of crap, he couldn't understand it wasnt even human made."
- > "I don't mind AI voice overs. I am appalled by the fact that people just give it the text, generate the voice over, and don't bother to listen to it to remove the awkward pauses and blatant mispronunciations."
  - Apr 12, 2026
  - [comment](https://news.ycombinator.com/item?id=47736215)
- > "watch it for three minutes, immediately get a kind of uncanny vibe, and then the AI voice will make a pronunciation mistake... or the script starts getting redundant or repetitive in ways that are common with AI."
  - Feb 24, 2026
  - [comment](https://news.ycombinator.com/item?id=47144443)
- > "I hate that voice so much. So many videos that are just a vapid TTS reading some ChatGPT-esque summary with some stock footage but you only find out that's what it is after the unskippable advert."
  - Oct 26, 2023
  - [comment](https://news.ycombinator.com/item?id=38027888)
- > "no visible narrator, pronunciation mistakes an AI would make, repeating stock footage"
  - Mar 30, 2026, listing how they spot slop
  - [comment](https://news.ycombinator.com/item?id=47581145)
- > "one paragraph of information laboriously spread out over five minutes of generic stock footage"
  - 2023
  - [comment](https://news.ycombinator.com/item?id=35596517)
- > "Long intro (skip the first 25 seconds), long outro, crappy text to speech voice over."
  - 2024
  - [comment](https://news.ycombinator.com/item?id=39072488)

**What the surveys say:**

| Survey | Finding |
|---|---|
| **Raptive** (Jul 2025, 3,000 US adults) | Content people *suspected* was AI-made lost about half its trust, whether or not it actually was AI. ([summary](https://ppc.land/raptive-study-shows-ai-content-cuts-reader-trust-by-half/)) |
| **Adobe** (Feb 2026) | 88% have wondered whether a voice was AI; 77% trust human voices most; 14% don't trust any voice they think is AI. ([Adobe](https://www.adobe.com/express/learn/blog/ai-audio-consumer-trust)) |
| **Animoto** (Jan 2026) | 83% say they can spot AI video; 36% say it lowers their view of the brand. "Odd voices" were one of the most-cited clues, at 55% (secondary summary). ([Business Wire](https://www.businesswire.com/news/home/20260121875037/en)) |
| **Pew** (Sep 2025) | 76% say it matters to know whether content is AI- or human-made; 53% aren't confident they can tell. Adults 65+ hear far less about AI (32% have heard "a lot", versus 62% of under-30s). ([Pew](https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/)) |
| **YouGov and Bynder, via Martech** (Jun 2026) | YouGov: 32% would trust a brand less if they knew its content was AI-made, versus 15% who would trust it more. Bynder: 56% of readers with a preference picked the unlabeled AI article as more engaging, but 52% felt less engaged once told it was AI. ([Martech](https://martech.org/consumers-like-ai-content-until-they-know-its-ai/)) |
| **Kapwing** (Nov 2025) | 21% of the first 500 Shorts shown to a new account were AI slop. ([Kapwing](https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/)) |

**Counterpoint:** a blind test of 1,326 radio listeners ([Radio Ink](https://radioink.com/?p=105638), Jul 24, 2026) found AI and human voiceovers "within a few points of each other on trust, energy, and likability." Once listeners were told which voice was which, reactions split by content type, and confidence in AI fell fastest for news.

**Reading:** In blind tests a good AI voice holds its own. The penalty comes from **suspicion and sloppiness**, and from the label itself: being told something is AI costs some engagement. Viewers name the specific tells:
- mispronunciations and odd pauses;
- repetitive, padded scripts;
- footage that doesn't match the words;
- epic music;
- long intros;
- bait thumbnails.

Older viewers are more exposed to slop and less aware of it, and their adult children are the ones complaining.

---

## 5. What the 40+ / owner / buyer crowd specifically says

These voices come mainly from BiggerPockets (real-estate investors with capital), Car Wash Forum (operators with 33 to 38 years in the business), the *HBR Guide* readership, and one self-described 53-year-old.

- **They are already skeptical of YouTube.** One prospective buyer wrote: "Currently I am 53 and an automation tech for major oil company... There are tons of YouTube videos etc. But not all content is legitimate." ([CWF, Aug 31, 2024](https://www.carwashforum.com/threads/tips-on-buying-first-car-wash.24419/)). They arrive wanting the unglamorous version.
- **They think in real-estate terms and need translating.** Typical BP questions include:
  - "With rentals, I am more educated and well versed on evaluation of a 'good rental'... I am unsure of the equivalent when it comes to a coin laundry."
  - "In the self storage market, they have ratios based on population to determine demand. Does the same metric hold true for laundromats?"
- **Their checklist is the same every time:**
  1. the lease (term remaining, rent increases);
  2. three years of tax returns, plus card versus cash revenue;
  3. equipment age and condition, with a technician's inspection;
  4. who covers when an employee calls out;
  5. insurance;
  6. whether to buy the real estate too.
- **Partners and family plans come up a lot.** For example: "my wife and teenage son will handle the trash and daily inspections money collection." Veterans warn against partnerships: "Don't do it; I M O!!!" (forum moderator).
- **Sellers are underserved.** On Hacker News (552-point thread on private equity buying essential services): "Why is there so much attention paid to the buyer (private equity) and no attention paid to the folks who sold the businesses to them?" (6 replies, [link](https://news.ycombinator.com/item?id=48293524)). Another: "I wonder if there is a way to make it easier for these people to sell their company when its time to retire."
- **Exit doubts:** "The local corner store, laundromat, and plumbing company are usually not something that can be sold easily. If they do, it takes years to find a buyer" ([HN, 2024](https://news.ycombinator.com/item?id=39400759)).
- **They respect people with scars.** The most-thanked posts are long, specific write-ups from people who bought and sold, and they give the real figures: purchase price, SDE, multiple, hours per week, closing costs.

---

## 6. Unanswered questions people keep asking

1. **"What will I actually take home?"** SDE minus a market wage for my own hours (or a manager's pay), minus debt service, taxes and a repair reserve. Nobody shows the line after "SDE."
2. **"How do I value it?"** SDE times a multiple: which multiple, why, and what moves it (lease length, equipment age, card versus cash revenue).
3. **"How do I verify cash revenue?"** Tax returns versus the owner's claims, utility bills, card-processor statements, bill-changer traps.
4. **"Can I get an SBA loan for a $100k to $500k business?"** And what does the personal guarantee mean for my house?
5. **"What happens when the lease ends?"** Several owners call this the business's real value.
6. **"How many hours, really, and who covers the gaps?"** Being on call, employee no-shows, insurance requiring an attendant.
7. **"Is it really a real-estate play?"** Car washes and self-storage come up most.
8. **"Who pays $20 a month for unlimited car washes, and what happens when an express tunnel opens nearby?"**
9. **"What happens when a second self-storage facility opens in town?"**
10. **Vending: how do I get locations without paying a locator? What commission is normal? What is a route for sale really worth, and are its location contracts transferable?**
11. **"What does a seller look for in a buyer, and how much seller financing is realistic?"**
12. **"If I'm the seller (often 55 to 70), who buys, what multiple do I get, and does private equity pay more?"**

---

## 7. Topics people are asking for next

- **Laundromat, with a real deal file:** a $190k purchase, $77k SDE, a $300k sale 16 months later, and the hours it took. (A public BP write-up provides a template for the kind of deal to source.)
- **Car wash:** self-serve versus express tunnel, memberships ("who's paying $20 a month?"), and whether it's really a real-estate play (Mister Car Wash leases 427 of its 436 sites).
- **Self-storage:** supply gluts, rate increases on existing tenants, and fees (insurance fees re-added every three months is a complaint people already have).
- **Selling your business:** what buyers, brokers and private equity actually pay, and what sellers wish they had known.
- **HVAC and plumbing roll-ups and vet clinics:** what happens to prices and staff after private equity buys in (552-point HN thread, many first-hand stories).
- **Vending locators and "done-for-you" packages:** what you actually get for the money.
- **SBA 7(a) loans explained:** 10% down, personal guarantee, underwriting to tax returns.
- **Valuation explained:** SDE versus EBITDA versus your salary.

---

## 8. What this means for Dull Profits

1. **Make the owner's own time a slice of The Split.** The most-liked criticisms in this research (45 likes on *Buy Then Build*, 44 on *Main Street Millionaire*) are about numbers that were left out: the owner's wage hidden inside SDE, taxes, repairs and personal guarantees.
   - Show SDE, then subtract a market wage for the hours, the loan payment, taxes and a repair reserve, and show what's left.
   - Episode 1 already defines route multiples as "what it earns the owner each year, before they pay themselves." One added sentence, "and part of that is your own wage," would answer the critique directly.
2. **Show the opposite of the cash pile.** Operators openly mock bill-changer cash shown as "revenue" and quarter-bucket thumbnails.
   - A recurring beat or Deal File comparing "what the video shows" with "what the tax return shows" would be a recognizable signature.
   - Never use cash-pile imagery, even in B-roll.
3. **Lead with the checklist owners actually use.** Close each episode with the same short due-diligence card: lease, 3 years of tax returns, equipment age, card versus cash, insurance, who covers the shifts.
   - The 40+ crowd already thinks this way, and the format becomes a series signature.
4. **Make the AI narration pass the "slop" sniff test.** The voice stays AI; what viewers object to is sloppiness. Their named tells give a quality-control list:
   - **Mispronunciations and awkward pauses:** do a full listen-through before locking each cut.
   - **Repetitive or padded scripts:** no recap padding.
   - **Footage that doesn't match the words:** every shot should match what is being said, and a graphic beats generic stock.
   - **Epic music and long intros:** keep the music bed quiet, and open on a number.
   - **Undisclosed AI:** keep the plain disclosure line already planned for every description.
     - The label has a measurable cost: in Bynder's test, 52% felt less engaged once told content was AI.
     - Our judgment is that hiding it is the bigger risk with an audience that already suspects AI: 76% say knowing matters (Pew), and suspected AI content loses about half its trust (Raptive).
     - So the narration has to earn trust through the other fixes above.
5. **Say what you're not selling.** Distrust of the course funnel is the second-strongest theme. A plain line in each description, such as "No course, no coaching, no affiliate links," answers it, if that stays true.
6. **Show the failures alongside the wins.** Viewers credit honesty even when it talks them out of buying. Owners trust people who show how deals went wrong. Good sourced examples:
   - the car wash lost to the bank in under 24 months;
   - the $30k and $50k vending "done-for-you" losses on Trustpilot;
   - the laundromat that was "free" and still a bad deal.

   Fits the Deal File format. For vending, today's version of the 1998 "Vend Up Broke" story is the locator who sells "leads, not actual locations."
7. **Use the seller's side as a lane nobody owns.** The target audience includes many owners in their 50s and 60s who will sell. The commenters above point out that sellers get almost no content.
   - An episode like "Selling your business: what buyers will really pay (and what PE does after)" serves the audience the competing channels ignore.

---

## Sources

**Forums and reviews (primary audience voice)**
- BiggerPockets, "What I learned from owning and selling a laundromat" (2024–25): https://www.biggerpockets.com/forums/961/topics/1219064-what-i-learned-from-owning-and-selling-a-laundromat-exploring-a-different-asset-cla
- BiggerPockets, "5 Lessons Learned From Selling My Laundromat" (2025): https://www.biggerpockets.com/forums/961/topics/1225054-5-lessons-learned-from-selling-my-laundromat
- BiggerPockets, "Coin Laundry Business: Is it passive income?" (2019): https://www.biggerpockets.com/forums/88/topics/703075-coin-laundry-business-is-it-passive-income
- BiggerPockets, "Are laundromats really passive" (2025): https://www.biggerpockets.com/forums/961/topics/1272463-are-laundromats-really-passive
- BiggerPockets, "Buying small businesses" (2023–24): https://www.biggerpockets.com/forums/961/topics/1137721-buying-small-businesses
- BiggerPockets, "Anyone have experience in buying a laundry mat" (2022–24): https://www.biggerpockets.com/forums/32/topics/1069409-anyone-have-experience-in-buying-a-laundry-mat
- Car Wash Forum, "Prospective 1st time owner" (Aug 2025): https://www.carwashforum.com/threads/prospective-1st-time-owner-where-to-even-start.26313/
- Car Wash Forum, "Tips on buying first car wash" (Aug–Sep 2024): https://www.carwashforum.com/threads/tips-on-buying-first-car-wash.24419/
- Car Wash Forum, "Need help with 1st carwash purchase" (Mar 2024): https://www.carwashforum.com/threads/need-help-with-1st-carwash-purchase.23773/
- Goodreads: *Main Street Millionaire* https://www.goodreads.com/book/show/209455833 · *Buy Then Build* https://www.goodreads.com/book/show/42591890 · *The Sweaty Startup* https://www.goodreads.com/book/show/216950437 · *HBR Guide to Buying a Small Business* https://www.goodreads.com/book/show/30652292
- Hacker News threads: vending economics https://news.ycombinator.com/item?id=24678064 · car washes https://news.ycombinator.com/item?id=39735096 · self-storage https://news.ycombinator.com/item?id=49740260 · private equity and essential services https://news.ycombinator.com/item?id=48292941 · AI Slop Report https://news.ycombinator.com/item?id=46409125
- Trustpilot: VendPros https://www.trustpilot.com/review/www.vendpros.net · Vendinglocationpro https://ca.trustpilot.com/review/vendinglocationpro.com

**Press quoting Reddit, owners and experts**
- Benzinga via Yahoo, gym buyer on r/smallbusiness (Feb 8, 2026): https://finance.yahoo.com/news/took-over-commercial-gym-says-183141522.html
- Benzinga via Briefly, vending "70% passive" (Apr 9, 2026): https://briefly-stg.herokuapp.com/anchor/Online_marketing/story/a-vending-machine-business-finally-took-off-after-multiple-failed-ideas-now-they-say-its-not-as-passiv
- Benzinga, r/smallbusiness "best boring businesses" (Jul 2025; read via search summary only): https://www.benzinga.com/news/topics/25/07/46509130/a-potential-investor-reached-out-to-small-business-owners-asking-what-are-the-best-boring-businesses-
- Entrepreneur on WSJ, laundromat influencers (Oct 20, 2026): https://www.entrepreneur.com/business-news/tiktok-made-owning-a-laundromat-look-like-easy-money-now-some-owners-are-airing-the-dirty-laundry
- Fortune, Gen Z laundromat buyers and Scott Shane (Aug 9, 2026): https://fortune.com/2026/08/09/gen-z-founders-laundromat-moved-across-country/
- NewsNation via Yahoo, "Making fast money on vending machines" (Feb 20, 2025): https://www.yahoo.com/news/making-fast-money-vending-machines-145926413.html
- Input/Inverse, vending YouTubers (Feb 25, 2022): https://www.inverse.com/input/culture/vending-machine-youtubers
- Freakonomics / The Economics of Everyday Things, ep. 113 "Laundromats" (Nov 2, 2025): https://freakonomics.com/podcast/laundromats/
- Kaleb Gorman, "How to avoid vending machine scams" (May 18, 2023): https://kalebgorman.substack.com/p/how-to-avoid-vending-machine-scams
- Still Searching, "You've Been Lied To About Buying Businesses" (Jun 23, 2025): https://stillsearching.beehiiv.com/p/you-ve-been-lied-to-about-buying-businesses

**Surveys and data**
- Raptive "AI stink" study (Jul 2025): https://raptive.com/blog/the-ai-stink-is-real-and-its-costing-brands/
- Adobe, AI audio and consumer trust (Feb 2026): https://www.adobe.com/express/learn/blog/ai-audio-consumer-trust
- Animoto, 2026 report via Business Wire: https://www.businesswire.com/news/home/20260121875037/en
- Pew Research, How Americans View AI (Sep 17, 2025): https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/
- Martech (YouGov), "Consumers like AI content until they know it's AI": https://martech.org/consumers-like-ai-content-until-they-know-its-ai/
- Kapwing, AI Slop Report (Nov 2025): https://www.kapwing.com/blog/ai-slop-report-the-global-rise-of-low-quality-ai-videos/
- Radio Ink, blind AI versus human voiceover listening study: https://radioink.com/?p=105638
