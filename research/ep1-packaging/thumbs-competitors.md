# Competitor thumbnails: what wins (Nov 27, 2026)

## Sample
75 thumbnails from i.ytimg.com (none blocked), saved as `/tmp/claude-0/-home-user-dull-profits/2d3a3f8e-aea6-5074-995c-c55aa0aa7c64/scratchpad/thumbs/<views>_<channel>_<id>.jpg`. The list with titles is in `.../scratchpad/thumbtools/list.tsv`.
- **(a) Vending:** the 25 most-viewed vending videos, plus 5 faceless vending videos (13K–100K).
- **(b) Faceless explainers:** 15 outliers and 7 typical videos (Modern MBA, How Money Works, Wendover, Hard Hat Economics, GEN, PolyMatter, Company Man, Logically Answered, How People Make Money, David Explains Money, Mr. Finance).
- **(c) 40–65:** 8 outliers and 7 typical videos (Eric PeakFP, Taylor Demars, James Conole, Rob Berger, Ken McElroy, Patrick Boyle, BiggerPockets, Money Guy). Sheet 3 also has 8 owner-channel thumbnails (Stephen the Investor, Codie, CNBC, UpFlip).
- Outlier = at least 3× the channel median (landscape data); typical = 0.8–1.2×.

**Contact sheets** (tiles labelled with views and channel; each has a `-25pct.jpg` copy for the small-size test):
- `.../scratchpad/thumbs/sheet1-vending.jpg` (30)
- `.../scratchpad/thumbs/sheet2-faceless-explainers.jpg` (22)
- `.../scratchpad/thumbs/sheet3-age40-65-and-owner-channels.jpg` (23)

Saturation (0–255), clutter (edge-pixel share) and "dark-dominant" (at least 45% of pixels below 60/255) were measured by `thumbtools/metrics.py`. Everything else was coded by eye.

## Counts

| Feature | Vending top 25 | Faceless outliers (15) | 40–65 outliers (8) | 40–65 typical (7) |
|---|---|---|---|---|
| Real human face | **24** (10/10 of top 10) | 2 (**0/10** from the 7 big channels) | 8 | 7 |
| Words, median | **2** | 5 | 4 | 3 |
| 3 words or fewer | 16 | 5 | 3 | 4 |
| Repeats the title | 3 | 4 | 1 | 0 |
| $ figure | 8 (2 of top 10) | **0** | 0 | 0 |
| Any number | 13 | 2 | **4** | **0** |
| Arrow / circle | 7 / 0 | 2 / 0 | 2 / 2 | 3 / 1 |
| Cash on screen | 10 (6 of top 10) | 0 | 0 | 0 |
| Hero object or brand | machine in 23 | **7 objects, 6 brands** | – | – |
| Labelled data chart | **0** | 1 | **3** | 1 (+3 generic red crash lines) |
| Warning look | 7 | 2 | 0 | 1 |
| Yellow box or text | 9 | 2 | 4 | 2 |
| Saturation, median | **96** | 71 | 98 | 103 |
| Clutter, median | **21.8%** | 17.7% | 13.8% | 12.5% |
| Dark-dominant | 4 | 2 | 0 | 3 |
| Headline readable at 25% | 22 | 15 | 6 of 6 with text | 6 of 6 with text |

## (a) Vending
- **The top 10 all share one formula:** a face, a bright snack-wall machine and 1–4 words. Quik Play's three hits (10.6M, 2.5M, 2.0M) withhold the number ("HOW MUCH?!" with a cash bag and a green arrow).
- **Long text loses:** all 5 thumbnails with 6+ words are under 700K. NowThis's 8-word caption and Every Level's "$41" sign vanish at 25%.
- **Warning art goes with skeptical titles** (FAILURE, EXPOSED, DO NOT ATTEMPT). It appears on 7/25, all at 372K or below except "REGRETS" (1.1M).
- **The only document look:** Vendingpreneurs' tweet card with "easy" highlighted in yellow (219K, about 60× their median).
- **Faceless vending is weak:** a stock photo with a logo (100K), a cartoon (41K), an AI-photoreal shocked man (23K), and the same "SO YOU WANT TO OWN A VENDING … EMPIRE" AI diagram on two channels (19K, 13K). The diagram is the most cluttered tile; its ~10 labels are unreadable at 25%.

## (b) Faceless explainers: winning without a face
- **One familiar object, big:** steak, a KFC bucket, a Costco box, a Dollar General sign, a Blackstone card in a vise, the Wish icon. A known brand stands in for a face.
- **Information on the object:** Modern MBA cut its steak into **"$ / $$ / $$$"** slices (3.4M, 11.5× median), the closest thing to The Split in the sample. Wendover prints its headline on a real-looking store sign.
- **A short twist the title doesn't contain:** "EXCEPT AMERICA", "THIS ISN'T WORKING", "Don't Trust Them.", "BANKRUPT" with "-99%".
- **Calmer than vending:** saturation 71 vs 96, clutter 17.7% vs 21.8%.
- **Same art, different results:** Mr. Finance's 233K and 4.9K videos use one template, so the topic did the work.

## (c) 40–65 audience
- **Specific charts mark the outliers.** The three biggest (1.8M, 1.4M, 939K) each show a labelled chart with a circled point or arrow:
  - claiming ages 62/67/70 with their crossovers;
  - an "AGE 60" curve turning from green to red;
  - Social Security % bars.

  Typical videos use generic crash squiggles. Numbers: 4/8 outliers, 0/7 typical.
- **Yellow highlight boxes** carry the hook ("YOU'VE BEEN LIED TO"), on **navy panels**, close to our palette.
- **Lowest clutter of any group** (13.8%). The template alone doesn't decide:
  - Rob Berger's 370K and 71K videos share one textless desk frame.
  - Eric's 1.8M and 39K videos share a template.
  - Stephen's 2.4M and 50K videos share a Quik Play clone.

## Overused in vending
1. **The owner's face before a bright snack-wall machine:** a face in 24/25 and a machine in 23/25. At 25% the sheet reads as one red and orange wall.
2. **Cash, a pointer and an income banner:**
   - cash in 10/25 and arrows in 7/25;
   - Quik Play's green arrow, split line and "HOW MUCH?!", copied by Stephen twice;
   - "$X/MONTH" or "/WEEK" banners in 5/25.
3. **Warning theatre:** red, caution tape, a hand on the head and one-word verdicts (7/25). The faceless corner adds the "SO YOU WANT TO OWN A … EMPIRE" AI diagram.

## Open lanes (inferred, untested)
- **No rival for a data graphic:** vending has 0/25 charts and only one document. A Split bar on a real machine or can, like Modern MBA's steak, has no direct competitor.
- **Navy stands out, with one condition:** dark-dominant thumbnails are rare (4/25), but navy needs one large bright element (the white owner slice or the yellow highlight) because YouTube's TV interface is dark.
- **Short, big text:** 3 words or fewer, with numbers at least a sixth of the frame height, so they survive the 25% test.

**Caveats:** small samples; views, not CTR; the vending list contains only winners; title, topic and channel size also drive the results.
