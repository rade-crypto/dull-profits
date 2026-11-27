# Ep 2 review: the broker's read

The reviewer plays a skeptical car wash broker and M&A advisor. They have sold self-serve, in-bay and express washes, and they know SBA lending, sale-leasebacks and roll-ups. They read `script-v2.md` against fact-check parts A and B and the research notes, checking each claim with a few spot searches.

**Overall verdict.** The facts are solid, and the fact-check fixed the worst problems (the 3.0× vs 4.7× mix-up and the EBITDA vs SDE "gap" line). What a professional would still object to is mostly framing:

1. **The buyer example quietly assumes a business-only deal on a 10-year loan.** Most small car wash deals that go through the SBA include the land.
2. **The Split mixes sources without saying so.** It applies a mature franchise tunnel's costs and investor-listing rent to a Mister membership price. Then the buyer section switches to older self-serve washes, which have different economics.
3. **The owner's checklist skips the items that actually kill deals:** what is in the price (land or not), verifying membership numbers, environmental checks and permits, an equipment inspection, and seller financing.

**Length.** Spoken text is now about **2,000 words** (everything except the headings and `[VISUAL]` lines), which is already over the ~1,850 target. Each edit lists its word change. Edits 1–11 add about +165 in all (1–8 alone about +130). Edit 12 lists optional cuts of about −125, plus where to find the rest. The owner has to approve those cuts, because the rule is never to remove lines the owner has already seen.

New facts are marked **NEW**, each with a primary source. Everything else rewords facts already in the script or the fact-check.

---

## 1. The loan: say it's business-only, and show the 25-year case when the land is included (highest priority)

**Problem.** The FY2026 median term on SBA car wash 7(a) loans was **240 months**, not 120. Most of these loans include real estate (economics.md, from SBA FOIA). SBA allows up to 25 years on the real estate portion of a loan. A broker would say right away that 10 years is the business-only case, and most viewers looking at a $700K wash will be looking at one that comes with land. The 25-year term changes the result a lot. Payments fall from **$94,747** a year to **$62,154** (my own calculation: $630K, 8.75%, 300 months), so about $88K is left instead of $55K, but the buyer pays interest for 15 more years. The script should show both cases rather than just the worse one. It should also not present a 10-year SBA deal leaving $55K as typical, because a lender sizing the loan would subtract a salary for the owner first, and on those numbers the deal might not qualify at all.

**Current:**
> Borrow the other 630,000 at 8.75 percent, the median starting rate on SBA car wash loans in fiscal 2026, over ten years. The payments come to about 94,700 dollars a year. That leaves about 55,000, before income tax and before setting money aside for equipment, and only if the owner works the wash themselves.

**Replacement:**
> Borrow the other 630,000 at 8.75 percent, the median starting rate on SBA car wash loans in fiscal 2026. Over ten years, the usual term when the land isn't included, payments come to about 94,700 dollars a year. That leaves about 55,000, before income tax and equipment, and only if the owner works the wash. If the land is in the deal, the SBA allows up to 25 years on that part. Payments drop to about 62,000. But that's fifteen more years of interest. These are round numbers, not a loan quote.

- **NEW (25 years):** SBA 7(a) terms page: real estate "A maximum of 25 years, including extensions"; equipment and working capital generally 10 years. https://www.sba.gov/partners/lenders/7a-loan-program/terms-conditions-eligibility
- **$62,154 a year:** my own calculation (630,000 × r ÷ (1 − (1+r)^−300), r = 0.0875/12). The 240-month FOIA median gives $66,809.
- **Visual:** two rows in the template 9 Split: "10 years (business only): payments $94,700 → owner ≈ $55,300" and "25 years on the land: payments ≈ $62,200 → owner ≈ $87,800". Source tag: "SBA 7(a) terms; Net to Owner calculation".
- **Caveat for the editor:** "starting rate" is correct, because many 7(a) loans have floating rates. The FOIA file has a `FixedorVariableInterestInd` field. If you want to say how many car wash loans float (this ties back to Zips), count that field. Don't state a share without the count.
- **Words:** about +25.

## 2. The down payment: count the total cost, and mention seller financing

**Problem.** Fact-check B #30 established that the 10% is of *total project cost* (closing costs and working capital included), and the script still says only "10 percent down". The script also never mentions seller financing, which shows up in most small-business deals. It also links back nicely to the Driven seller note. I give no number for the seller-note cap, because the SOP 50 10 8.1 details I found are all secondary (law firm and lender blogs).

**Current:**
> Now the loan. For a purchase like this, the SBA usually wants at least 10 percent down. That's 70,000.

**Replacement:**
> Now the loan. The SBA usually wants at least 10 percent of the total cost up front, closing costs included. Call it 70,000. Sellers often carry part of the price as a loan, too.

- Source for the 10% of total project cost: SOP 50 10 8.1 via Starfield & Smith (already in fact-check B #30): https://starfieldsmith.com/2026/09/best-practices-change-of-ownership-transactions-under-sop-50-10-8-1-what-sba-lenders-need-to-know/ . Since the SOP's own text wasn't read, keep the on-screen tag as "SBA SOP 50 10 8.1".
- **Words:** about +12.

## 3. Bridge from the Split to the small wash, and stop saying "Most"

**Problem.** The Split is an express tunnel franchise: 23% labour, a 5% royalty, and investor rent. The buyer section is about older self-serve and in-bay washes, which have a skeleton staff, no royalty, and an owner who does the work. Without a sentence saying so, viewers will carry the 21% margin and "workers are the biggest slice" over to the wrong business. "Most" also has no source (fact-check B #27 recommended "Many", and v2 didn't change it).

**Current:**
> Most car washes that change hands aren't 5 million dollar tunnels. They're older, smaller washes, sold through business brokers.

**Replacement:**
> Many car washes that change hands aren't 5 million dollar tunnels. They're older, smaller washes, sold through business brokers. Fewer staff, no franchise fee, and usually the owner doing the work. So the split we just followed isn't their split.

- **Words:** +19.

## 4. BizBuySell: say it's a small sample and the land question is open

**Problem.** The median price comes from 32 reported sales, and BizBuySell doesn't say whether the price includes the land. A broker's first question about any comp is "with or without the real estate?" That decides whether edit 1 means the 10-year case or the 25-year one. I couldn't find a BizBuySell methodology statement on real estate (search only turned up its separate guide "Do Business Valuations Include Real Estate?"), so the script shouldn't claim either way.

**Current:**
> According to BizBuySell, the median car wash sold that way in 2025 went for about 700,000 dollars.

**Replacement:**
> According to BizBuySell, the 32 car washes reported sold that way in 2025 went for a median of about 700,000 dollars. That's a small sample, and it doesn't say how many included the land.

- The 32 is already in fact-check B #28, via Hyperresearch, citing the BizBuySell Insight Report data tables: https://hyperresearch.ai/guides/buying-a-car-wash . **It still needs the BizBuySell browser check that fact-check B already flagged.** If the BizBuySell page *does* say whether real estate is included, replace the second sentence with what it says.
- **Words:** +18.

## 5. The Split: say up front that it's a composite, and call the rent what it is

**Problem.** A professional would object that this isn't any real wash's books. It applies a mature franchise site's cost percentages, the in-place rent on investor listings and Mister's capex ratio to Mister's average membership price. The visual's corner tag is honest, but the narration should say it as well. "Asking rent" is also the wrong term. B+E reports the **in-place NOI** on properties listed for sale. The asking part is the *price*. Those leases have **17.5 years left on average**, which means they are mostly recent sale-leasebacks. That rent is set to support an investor's purchase price, not what an older independent wash pays its landlord.

**Current (a):**
> So let's follow the thirty dollars. We built this from three sources.

**Replacement (a):**
> So let's follow the thirty dollars. This isn't one real wash's books. It's a mature franchise site, scaled to thirty dollars, built from three sources.

**Current (b):**
> The rent is our estimate, from the average asking rent on car washes listed for sale in September 2026.

**Replacement (b):**
> The rent is our estimate: the average rent on car wash properties listed for sale to investors in September 2026. Most of those leases are recent, with about seventeen years left.

- **NEW (17.5 years, NOI is the in-place rent):** B+E, Oct 19, 2026: "Average NOI dipped to $325,222"; "The average remaining lease term held at 17.5 years"; "In a triple net (NNN) lease, the tenant pays property taxes, insurance, and maintenance in addition to rent." https://tradenetlease.com/nnn-car-wash-listed-inventory-september-2026/ (The NNN line also supports adding property tax and insurance on top of the rent in the landlord slice.)
- **Words:** about +20.

## 6. The $460,000: put it next to the cost of building the wash

**Problem.** "That sounds like plenty" invites viewers to treat $460K as a salary. A professional thinks of it as a return on capital: about $460K a year at a mature site, against a build cost the script has already given as $5.1–7.5M. That's single digits before tax, and it's for a tenant. This edit uses only numbers already in the script. Fact-check A B3 couldn't confirm whether Tommy's Item 7 includes land, so the wording below doesn't say.

**Current:**
> On a mature site selling 2.2 million dollars a year, 21 percent comes to about 460,000. That sounds like plenty.

**Replacement:**
> On a mature site selling 2.2 million dollars a year, 21 percent comes to about 460,000. That sounds like plenty, until you set it against a build of five million dollars or more.

- **Words:** +13.

## 7. SBA charge-offs: say the clean data is from before the boom

**Problem.** The reassuring comparison (6.8% vs 7.3%) uses loans approved FY2010–16, which were made *before* the boom (the tag says so, but the narration doesn't). Boom-era loans haven't been fully repaid or written off yet. A lender would object to "haven't gone bad at unusual rates" when the loans that would show it are still outstanding.

**Current:**
> To be fair, those loans haven't gone bad at unusual rates. In the SBA's own data, car wash loans have been charged off a little less often than the average SBA loan. So far, the damage has been at big chains carrying big debts.

**Replacement:**
> To be fair, car wash loans made from 2010 to 2016, before the boom, were charged off a little less often than the average SBA loan. Loans from the boom years are still too new to judge. So far, the big losses have been at chains carrying big debts.

- Source as in fact-check B #25 (SBA 7(a) FOIA, https://data.sba.gov/dataset/7a-504-foia ). "Still too new" follows from fact-check B #25: "Loans from FY2017 on are still largely outstanding."
- **Words:** about +3.

## 8. The owner's checklist: add what's in the price, verified members, environmental checks and permits, and an equipment inspection

**Problem.** The current list is fine, but it misses what really goes wrong in deals:
- Whether the land is in the price, and how the price is split between the real estate and the business.
- Verifying membership counts against the software and the deposits. Sellers quote membership numbers, not paying members.
- An environmental check: washes have oil and water separators and sludge pits, and many sit on former gas station lots.
- Whether the water and sewer discharge permits transfer.
- An equipment inspection by a technician, not just the age of the equipment.

**Current:**
> Who owns the land, and what does the lease say? How many members are there, and how many cancel each month? What's being built within three miles? The city's planning agendas will show it. How old are the conveyor, the brushes and the dryers? And three years of tax returns and card processing statements, not just the seller's spreadsheet.

**Replacement:**
> Is the land in the price? If not, what does the lease say? How many members actually pay each month, and how many cancel? Check it in the wash's own software and the bank deposits. What's being built within three miles? The city's planning agendas will show it. What does an equipment technician say about the conveyor, the brushes and the dryers? Has the land had an environmental check, and do the water and sewer permits transfer? And three years of tax returns, not just the seller's spreadsheet.

- No new numbers. The environmental and permit items are standard due diligence and the script doesn't quantify them, so no source is needed. If you want one on screen, the California reclaim rule (Water Code §10951) is already in the episode.
- **Visual (template 19):** "Land: in the price, or leased?" · "Paying members, checked against deposits" · "New washes within 3 miles" · "Equipment inspection" · "Environmental check and permits" · "3 years of tax returns". Keep the "Not financial advice" footer.
- **Words:** about +22.

## 9. Mister: say who lost money on the share price

**Problem.** "The share price fell by more than half" sitting next to "Leonard Green bought out the other shareholders at 7" lets viewers think private equity lost money on Mister. The loss fell on public buyers from 2021 on. Leonard Green had owned it since 2014, and it bought back the rest at a low price. A professional would point out that this case actually supports the hook ("the biggest winners aren't the ones you'd expect"). Don't claim that Leonard Green made money, because its 2014 entry price wasn't researched. Just say who lost.

**Current:**
> Sales grew by about three quarters. The share price fell by more than half.

**Replacement:**
> Sales grew by about three quarters. The share price fell by more than half. That loss landed on people who bought shares from 2021 on. Leonard Green had been in since 2014.

- **Words:** +17.

## 10. The cash flow is the seller's figure

**Problem.** SDE on a broker comp is the seller's own number, with their add-backs. A professional never says "its cash flow is" without adding "as stated".

**Current:**
> So take a 700,000 dollar wash at that multiple. Its cash flow is about 150,000 dollars a year.

**Replacement:**
> So take a 700,000 dollar wash at that multiple. The seller would put its cash flow at about 150,000 dollars a year. A buyer has to prove it.

- **Words:** +9.

## 11. Smaller wording fixes (no change in length)

| Current | Replacement | Why |
|---|---|---|
| "The workers get the biggest share." (Who really wins) | "At a franchise tunnel, the workers get the biggest share." | The same problem as edit 3: the recap shouldn't sound true of every wash. (+4) |
| "So if you're ever looking at a car wash for sale, here's what the numbers say to ask for." | "So if you're ever looking at a car wash for sale, here are the questions the numbers point to." | More neutral, and easier to defend against an "investment advice" reading (fact-check B #44). (+1) |
| "Then it sold all 382 of them for 385 million, about a million dollars a wash." | Keep the line, but the visual must not set "$1M a wash" next to the "$5.1–7.5M to build" figure. | Driven's 10-K and press releases don't say how much real estate went with the sale. If the land stayed with landlords, comparing $1M to the build cost is apples to oranges. Check the purchase agreement or 10-K note before making any comparison. |

## 12. Optional cuts to get back to about 1,850 words (the owner must approve these)

Edits 1–11 add about +165 words. The owner has already seen v2, so each of these cuts needs the owner's OK:

- "Some states, like Wisconsin, add sales tax on top. We'll leave tax out." (−13). Move it to the on-screen tag "Excludes sales tax".
- "And in 2021, the industrial company Vontier paid about 956 million dollars for DRB, whose software runs checkouts and memberships at tunnel washes." plus "But they aren't untouchable. Since 2024, Vontier has reported lower demand for its car wash products." (−40). Keep DRB only as a name on the template 16 card.
- "A conveyor wash uses about 30 gallons of fresh water per car, according to an industry study. A hose left running can use 100." (−25). The California rule is the part a buyer needs. The gallons comparison is trivia.
- "Local TV counted 25 car washes in the city's 35 square miles." (−11)
- "One real estate brokerage, Matthews, counts about 12,000 conveyor washes in the US, and says" → "Matthews, a real estate brokerage, says" (−10)
- In the Zips paragraph: "Members per site doubled, and sales still fell, from 345 million to 303 million." → "Members per site doubled, and sales still fell." Keep the numbers on screen. (−7)
- The four kinds paragraph: cut "Full-serve washes, where staff clean the inside too." and keep the clip (−9).
- Edit 1's last sentence ("These are round numbers, not a loan quote.") can move to an on-screen tag (−8).

That's about −123. Starting from about 2,000 words, edits 1–11 bring it to about 2,165, and these cuts bring it back to about 2,040. Getting to about 1,850 takes one more section shortened by about 190 words, or leaving out edits 9 and 10 and the optional half of edit 3. The Getty and Essential Properties paragraph is the most expendable.

---

### Sources used in this review (new)
- SBA 7(a) terms, conditions and eligibility (25-year real estate maturity): https://www.sba.gov/partners/lenders/7a-loan-program/terms-conditions-eligibility
- B+E, NNN Car Wash Listed Inventory, September 2026 (in-place NOI, 17.5-year average remaining term, NNN definition): https://tradenetlease.com/nnn-car-wash-listed-inventory-september-2026/
- Searched but **not used** for any number, because they are secondary: the SOP 50 10 8.1 debt-service-coverage floor (reported as 1.25× for acquisitions by FRANdata, https://frandata.com/sba-sop-50-10-8-1-franchise-lending-changes/ ), and the seller-note standby rules. If the script ever gives a coverage number, get the SOP text from sba.gov first.
- Driven Brands closing release (didn't say how much real estate was included): https://www.businesswire.com/news/home/20250410501664/en/Driven-Brands-Announces-Closing-of-Sale-of-U.S.-Car-Wash-Business
