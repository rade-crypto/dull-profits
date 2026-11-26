"""Episode 1 edit plan: one entry per shot. Used for the stills storyboard and the final render.

at     phrase where the shot starts (as Whisper wrote it in voiceover/timings-clean.json); None = 0:00
kind   F = footage · GF = graphic over darkened footage · G = full-screen graphic · D = Deal File document
clip   file in footage/ ; in = seconds into the clip ; blur = [(x, y, w, h)] boxes to blur (logos, billboards)
scene  graphic (tools/video/gfx/scenes.html). Strings starting with "@" are phrases: they become the time
       (seconds from shot start) when that phrase is spoken, so each number appears as it's said.

On-screen text rules (owner, Nov 26 2026): white text only, as few words as possible, only what the voice says
or a label/number for it, no presenter lines ("later in this video"), no chapter cards, no middle dots.
"""
from pathlib import Path

LOGO = "file://" + str(Path(__file__).resolve().parents[2] / "brand" / "wordmark.png")
SRC_VMFS = "VMFS USA, 2026"
SRC_CANT = "Cantaloupe, 2025 data"
LAX_NIGHT_BLUR = [(1520, 800, 310, 150), (770, 990, 190, 80)]
LAX_DAY_BLUR = [(1350, 690, 260, 130), (970, 1000, 260, 80)]

SPLIT = [  # The $2 soda, per the supplier's model (6% tax, 10% commission, mostly card)
    dict(key="tax", label="Government", amount="11¢", cents=11, row=1, align="left"),
    dict(key="sup", label="Drink company", amount="94¢", cents=94, row=0),
    dict(key="pay", label="Card processor", amount="9¢", cents=9, row=1),
    dict(key="pay", label="Software", amount="4¢", cents=4, row=-1),
    dict(key="loc", label="The building", amount="20¢", cents=20, row=0, align="left"),
    dict(key="own", cents=62, inside="Owner ?"),
]


def split(names_cues, amounts=False, labels=True, **kw):
    sl = []
    for s, cue in zip(SPLIT, names_cues):
        d = dict(s, cue=cue)
        if not labels:
            d.pop("label", None)
        if not amounts:
            d.pop("amount", None)
        elif s["key"] == "own":
            d["inside"] = "Owner 62¢"
        sl.append(d)
    return dict(type="split", params=dict(slices=sl, **kw))


def ftg(at, clip, t_in, **kw):
    return dict(at=at, kind="F", clip=clip, **{"in": t_in}, **kw)


CHAPTERS = [  # for the storyboard sheets and YouTube chapter markers only; never shown in the video
    ("Hook", None),
    ("Who actually owns the machine", "These machines usually belong"),
    ("Following the two dollars", "Those are sales figures"),
    ("Why card payments help", "Card payments do help"),
    ("Winner 1: the location", "Winner number one"),
    ("Winner 2: scale", "Winner number two"),
    ("Winner 3: the payment network", "The third winner"),
    ("Micro markets and smart stores", "But some of the biggest changes"),
    ("A beginner's first six months", "But the passive income videos"),
    ("Buying a route instead", "If you'd rather buy a route"),
    ("Operation Vend Up Broke", "And none of this is new"),
    ("Who really wins", "Back to your $2"),
]

SHOTS = [
    # ---------------------------------------------------------------- 1 · Hook
    ftg(None, "01-phone-pay-vending.mp4", 1.0),
    dict(at="$2", kind="GF", clip="c02-office-vending.mp4", **{"in": 6.0},
         scene=split(["@government", "@drink company", "@card processor", "@software company", "@the building", None],
                     title="$2.00", titleAt=0, wholeAt="@Before the owner", splitAt="@five other players", dim=0.72)),
    ftg("At one of the busiest airports", "c05-lax-plane-landing-sunset.mp4", 4.0),
    dict(at="the building takes", kind="GF", clip="c05-lax-dusk-overview.mp4", **{"in": 3.0}, blur=LAX_NIGHT_BLUR,
         scene=dict(type="bignum", params=dict(at="@59.5%", count=[0, 59.5], fmt="pct1", size=300, y=280,
                                               lines=[dict(text="of every sale goes to the building")]))),
    ftg("Online, vending machines", "c11-phone-night-viewer.mp4", 2.0),
    dict(at="as easy passive income", kind="GF", clip="c11-phone-night-viewer.mp4", **{"in": 4.0},
         scene=dict(type="pitch", params=dict(replace=True, size=110, y=640, dim=0.45, lines=[
             dict(text="“Easy passive income.”", at=0),
             dict(text="“Stock it once a week.”", at="@Stock a machine"),
             dict(text="“Let the cash pile up.”", at="@let the cash pile up")]))),
    dict(at="So we check the real numbers", kind="GF", clip="c05-traveler-vending-snack.mp4", **{"in": 1.0},
         scene=dict(type="sources", params=dict(dim=0.75, items=[
             dict(title="Payment data", key="pay", cue="@payment data"),
             dict(title="Public contracts", key="loc", cue="@public contracts"),
             dict(title="Operators' own results", key="sup", cue="@operators")]))),
    ftg("The picture is a lot less exciting", "c05-ohare-crowd-legs.mp4", 3.0),
    ftg("So let's follow the $2", "c12-coins-in-hand.mp4", 4.0),

    # ---------------------------------------------------------------- 2 · Who owns the machine
    ftg("These machines usually belong", "c02-route-driver-van.mp4", 1.0),
    ftg("places them in other people's buildings", "c02-office-vending.mp4", 3.0),
    dict(at="more than $7 billion", kind="GF", clip="c02-van-aerial-road.mp4", **{"in": 1.0},
         scene=dict(type="bignum", params=dict(at="@$7 billion", text="$7B+", size=280, y=300, lines=[
             dict(text="US vending operators, 2025")], source="IBISWorld"))),
    dict(at="The biggest names are food service giants", kind="GF", clip="c10-chicago-suburbs-aerial.mp4", **{"in": 30.0},
         scene=dict(type="tiles", params=dict(y=300, big=[
             dict(title="Compass Group", key="sup", cue="@Compass"),
             dict(title="Aramark", key="sup", cue="@Aramark")],
             smallCue="@small, local businesses", smallLabel="and thousands of small, local operators"))),
    dict(at="Most of them are built around a route", kind="GF", clips=[("c02-van-side-door-cases.mp4", 0, 4.5), ("c09-restock-drive-suburb.mp4", 1, None)],
         scene=dict(type="words", params=dict(items=[
             dict(text="Restock", cue="@restocking"), dict(text="Pull cash", cue="@pulling cash"), dict(text="Fix what broke", cue="@fixing")]))),
    dict(at="The machines aren't cheap", kind="GF", clips=[("c02-combo-machine.mp4", 6, 7.5), ("c12-vending-closeup.mp4", 0.5, None)],
         scene=dict(type="cards", params=dict(valueSize=110, items=[
             dict(label="Countertop", value="$1,900", key="sup", cue="@countertop"),
             dict(label="Combo", value="$3,450", key="sup", cue="@combo"),
             dict(label="Elevator", value="$8,650", key="sup", cue="@An elevator machine")],
             source="VMFS USA"))),
    ftg("Then there's the deal with the location", "c08-office-break-room.mp4", 1.0),
    dict(at="Busy places know", kind="GF", clip="c02-transit-station.mp4", **{"in": 4.0},
         scene=dict(type="bignum", params=dict(at="@five to 20%", text="5–20%", size=280, y=300, lines=[
             dict(text="of gross sales")]))),
    dict(at="Sales per machine depend", kind="GF", clips=[("c09-busy-office.mp4", 2, 13.3), ("c02-hospital-corridor.mp4", 0.5, 2.2), ("c02-factory-floor.mp4", 1, 1.8), ("c02-transit-station.mp4", 12, None)],
         scene=dict(type="bars", params=dict(kicker="Sales per machine, per month", max=2600, labelW=470, items=[
             dict(label="Typical site", from_=150, value=700, text="$150–700", key="sup", cue="@a typical site"),
             dict(label="Strong site", value=1500, text="up to $1,500", key="sup", cue="@a strong one"),
             dict(label="Top spots", value=2000, text="$2,000+", key="sup", cue="@Top spots")],
             source="VMFS USA"))),

    # ---------------------------------------------------------------- 3 · Following the two dollars
    ftg("Those are sales figures", "01-phone-pay-vending.mp4", 5.0),
    dict(at="Here's how one equipment supplier", kind="GF", clip="c03-receipt.mp4", **{"in": 3.0},
         scene=dict(type="ledger", params=dict(w=1100, y=220, lines=[
             dict(label="Price", value="$2.00", cue=0),
             dict(label="Sales tax", value="6%", cue="@6%", dot="tax"),
             dict(label="Location's cut", value="10%", cue="@10%", dot="loc"),
             dict(label="Paid by card", value="78%", cue="@paying by card", dot="pay")], source=SRC_VMFS))),
    dict(at="First, about 11 cents", kind="GF", clips=[("c02-office-vending.mp4", 10, 5.5), ("c01-bottling-line.mp4", 1, 7.8), ("c01-card-reader-tap.mp4", 1, 8.6), ("c01-office-lobby.mp4", 4, None)],
         scene=split(["@11 cents", "@94 cents", "@Card processing", "@four more", "@The building takes", "@That leaves"],
                     amounts=True, wholeAt=0, splitAt=0, dim=0.8, y=390,
                     tally=dict(label="Operator keeps", at=0, steps=[
                         dict(cents=11, cue="@11 cents"), dict(cents=94, cue="@94 cents"), dict(cents=9, cue="@nine cents"),
                         dict(cents=4, cue="@four more"), dict(cents=20, cue="@20 cents")]), source=SRC_VMFS)),
    dict(at="before paying for gas", kind="GF", clip="c03-gas-pump-gallons.mp4", **{"in": 20.0},
         scene=split([0, 0, 0, 0, 0, 0], amounts=True, labels=False, wholeAt=0, splitAt=0, dim=0.8, y=390,
                     costs=[dict(label="Gas", cue="@gas"), dict(label="Labor", cue="@labor"), dict(label="Repairs", cue="@repairs"),
                            dict(label="Insurance", cue="@insurance"), dict(label="Income tax", cue="@income tax")])),
    ftg("Every restock means driving out", "c03-highway-driving.mp4", 2.0),
    ftg("Those costs come out", "c03-hand-truck.mp4", 2.0),
    dict(at="Run the full numbers", kind="GF", clips=[("c09-calculator-hands.mp4", 6, 7), ("c02-driver-paperwork.mp4", 2, None)],
         scene=dict(type="ledger", params=dict(w=1100, y=240, lines=[
             dict(label="Sales", value="$900", cue="@$900"),
             dict(label="Operator keeps", value="$197", cue="@keeps about", total=True)],
             source=SRC_VMFS))),
    dict(at="And the better the location", kind="D",
         scene=dict(type="doc", params=dict(header="Riverside Community College District vending agreement, 2022",
                    html='(5) Commission Proposal - The Vendor guarantees commission of <span class="hl" data-cue="@33%">33% on gross sales</span>, and a signing bonus in the amount of $5,000 ...'))),
    dict(at="and that airport from the start", kind="GF", clip="c05-lax-dusk-overview.mp4", **{"in": 8.0}, blur=LAX_NIGHT_BLUR,
         scene=dict(type="bars", params=dict(kicker="The location's cut", max=70, labelW=470, items=[
             dict(label="Typical", value=10, text="10%", key="loc", cue=0),
             dict(label="Riverside", value=33, text="33%", key="loc", cue=0.3),
             dict(label="That airport", locked=True, cue="@its deal is bigger")]))),

    # ---------------------------------------------------------------- 4 · Card payments
    ftg("Card payments do help", "c04-card-tap-terminal.mp4", 1.0),
    dict(at="people paying by card or phone", kind="GF", clips=[("c04-card-tap-terminal.mp4", 4, 3.6), ("c01-card-reader-tap.mp4", 0.5, 6.5), ("c08-card-tap-unlock.mp4", 0, None)],
         scene=dict(type="cards", params=dict(kicker="Average purchase, 2025", valueSize=130, items=[
             dict(label="Card or phone", value="$2.45", key="pay", cue="@$2.45"),
             dict(label="Cash", value="$1.57", key="tax", cue="@$1.57")], source=SRC_CANT))),
    dict(at="and 78%", kind="GF", clip="c04-dollar-bill-acceptor.mp4", **{"in": 1.0},
         scene=dict(type="bignum", params=dict(at=0, count=[0, 78], fmt="pct0", size=300, y=280, lines=[
             dict(text="of sales were cashless")], source=SRC_CANT))),
    dict(at="So the operator ends up", kind="GF", clips=[("c05-traveler-vending-snack.mp4", 6, 3), ("c06-warehouse-drink-racks.mp4", 2, 3), ("01-phone-pay-vending.mp4", 3, None)],
         scene=dict(type="cards", params=dict(valueSize=100, items=[
             dict(label="", value="Location", key="loc", cue="@three kinds"),
             dict(label="", value="Scale", key="sup", cue="@three kinds"),
             dict(label="", value="Payments", key="pay", cue="@three kinds")]))),

    # ---------------------------------------------------------------- 5 · Winner 1: the location
    ftg("Winner number one", "c05-lax-dusk-overview.mp4", 12.0, blur=LAX_NIGHT_BLUR),
    ftg("That airport is Los Angeles", "c05-lax-theme-building-day.mp4", 2.0, blur=LAX_DAY_BLUR),
    dict(at="In 2023, its board", kind="D",
         scene=dict(type="doc", params=dict(header="LA Board of Airport Commissioners, Feb 16, 2023",
                    html='Pursuant to the terms of the proposed concession agreement, First Class will pay LAWA the greater of a minimum monthly guarantee of <span class="hl" data-cue="@$100">$100 per machine</span> or <span class="hl" data-cue="@59.5%">59.5 percent of gross sales</span> over the five-year term and any approved options.'))),
    dict(at="Even the runner-up bid", kind="GF", clip="c05-contract-signing.mp4", **{"in": 2.0},
         scene=dict(type="bars", params=dict(kicker="LAX vending bids", max=80, labelW=470, items=[
             dict(label="First Class Vending", value=59.5, text="59.5%", key="loc", cue=0),
             dict(label="Canteen", value=51.6, text="51.6%", key="sup", cue="@Canteen"),
             dict(label="Gilly Vending", value=42.0, text="42.0%", key="tax", cue="@Canteen")],
             source="LAX board report, 2023"))),
    ftg("The operator runs and maintains", "c05-traveler-vending-snack.mp4", 1.0),
    ftg("The airport just collects", "06-airport-terminal-4k.mp4", 1.0),

    # ---------------------------------------------------------------- 6 · Winner 2: scale
    ftg("Winner number two", "c06-trucks-docks-aerial.mp4", 2.0),
    dict(at="Driving between machines", kind="GF", clip="c06-downtown-traffic-aerial.mp4", **{"in": 0.5},
         scene=dict(type="words", params=dict(y=520, items=[
             dict(text="100 machines, one area", cue="@100 machines"),
             dict(text="10 machines, across a city", cue="@10 machines")]))),
    ftg("Big operators also buy", "c06-warehouse-drink-racks.mp4", 2.0),
    ftg("The biggest of them all", "c06-chicago-skyline.mp4", 2.0),
    dict(at="It started in Chicago", kind="GF", clip="c06-archival-1933-street.mp4", **{"in": 2.0},
         scene=dict(type="bignum", params=dict(at=0, text="1929", size=240, y=320, dim=0.5, lines=[
             dict(text="Chicago, 5¢ candy bars")]))),
    dict(at="Today, Compass Group describes", kind="GF", clip="c01-office-lobby.mp4", **{"in": 4.0},
         scene=dict(type="quote", params=dict(at=0, size=110, y=330,
                    text="“The largest unattended retail provider in the United States.”", by="Compass Group"))),
    dict(at="And the big players keep getting bigger", kind="GF", clips=[("c06-trucks-docks-aerial.mp4", 4, 5), ("c06-warehouse-drink-racks.mp4", 10, 6), ("c02-van-side-door-cases.mp4", 0, None)],
         scene=dict(type="flow", params=dict(kicker="2025", src=dict(title="Buffalo Rock"), dst=dict(title="Canteen"), arrowLabel="sold",
                    facts=[dict(text="~700 micro markets", cue="@700", key="sup"),
                           dict(text="7,600+ vending locations", cue="@7,600", key="sup")],
                    source="VendingMarketWatch"))),

    # ---------------------------------------------------------------- 7 · Winner 3: payments
    ftg("The third winner", "c01-card-reader-tap.mp4", 2.0),
    ftg("Every tap sends", "c08-card-tap-unlock.mp4", 0.5),
    dict(at="Cantaloupe, one of the biggest", kind="GF", clips=[("c01-server-room.mp4", 0, 9.5), ("c08-card-tap-unlock.mp4", 0, None)],
         scene=dict(type="cards", params=dict(kicker="Cantaloupe, 2025", valueSize=130, items=[
             dict(label="Machines and kiosks", value="600,000+", key="pay", cue="@600,000"),
             dict(label="Sales", value="$4.6B", key="pay", cue="@$4.6 billion")]))),
    dict(at="Cantaloupe earns a cut", kind="GF", clip="c04-card-tap-terminal.mp4", **{"in": 0.0},
         scene=dict(type="flow", params=dict(src=dict(title="Every card sale"), dst=dict(title="Cantaloupe"), arrowLabel="a cut + monthly fees"))),
    dict(at="And Cantaloupe itself just changed hands", kind="GF", clips=[("c10-handshake-warehouse.mp4", 1, 5.5), ("c05-contract-signing.mp4", 1, 7), ("c05-boardroom-wide.mp4", 2, None)],
         scene=dict(type="flow", params=dict(kicker="May 2026", src=dict(title="365 Retail Markets"), dst=dict(title="Cantaloupe"), arrowLabel="bought",
                    facts=[dict(text="About $848 million", cue="@$848 million", key="pay")], source="SEC filing"))),

    # ---------------------------------------------------------------- 8 · Micro markets
    ftg("But some of the biggest changes", "c09-busy-office.mp4", 4.0),
    ftg("A micro market is an unlocked", "c08-grab-and-go-cooler.mp4", 2.0),
    ftg("and a self-checkout kiosk", "c08-self-checkout-scan.mp4", 2.0),
    dict(at="In 2025, the average vending purchase", kind="GF", clips=[("c08-kiosk-touchscreen.mp4", 1, 6.5), ("c08-self-checkout-scan.mp4", 8, 6), ("c08-card-tap-unlock.mp4", 0, None)],
         scene=dict(type="bars", params=dict(kicker="Average purchase, 2025", max=5.6, labelW=470, items=[
             dict(label="Vending machine", value=2.01, text="$2.01", key="tax", cue="@$2.01"),
             dict(label="Micro market", value=3.02, text="$3.02", key="sup", cue="@$3.02"),
             dict(label="Smart store", value=4.49, text="$4.49", key="pay", cue="@$4.49")],
             source=SRC_CANT))),
    dict(at="Micro markets on that network", kind="GF", clips=[("c08-grab-and-go-cooler.mp4", 7, 10.5), ("c09-busy-office.mp4", 8, None)],
         scene=dict(type="cards", params=dict(valueSize=110, items=[
             dict(label="Micro market sales", value="$1B+", key="sup", cue="@billion"),
             dict(label="Smart stores", value="71→572", key="pay", cue="@71 locations"),
             dict(label="Smart store sales", value="$6M", key="pay", cue="@$6 million")]))),
    dict(at="Vending machines still bring in", kind="GF", clips=[("c02-office-vending.mp4", 11, 6.5), ("c08-office-break-room.mp4", 3, None)],
         scene=dict(type="bars", params=dict(kicker="Total sales, 2025", max=3.9, labelW=470, items=[
             dict(label="Vending machines", value=3.3, text="$3.3B", key="tax", cue=0),
             dict(label="Micro markets", value=1.0, text="$1B+", key="sup", cue=0.2),
             dict(label="Smart stores", value=0.006, text="$6M", key="pay", cue=0.4)],
             source=SRC_CANT))),

    # ---------------------------------------------------------------- 9 · A beginner's first six months
    ftg("But the passive income videos", "c09-laptop-night.mp4", 2.0),
    dict(at="They posted their numbers", kind="GF", clip="c09-laptop-night.mp4", **{"in": 6.0},
         scene=dict(type="post", params=dict(meta="",
                    title="Vending machine side hustle: 6-month update",
                    body="$3,200 on two refurbished machines. $400 on snacks and drinks."))),
    ftg("One machine sits in an office", "c09-busy-office.mp4", 14.0),
    ftg("The other is in an auto repair shop", "c09-mechanic-under-lift.mp4", 1.0),
    dict(at="The office machine brings in", kind="GF", clips=[("c09-busy-office.mp4", 20, 6.5), ("c09-auto-repair-shop.mp4", 1.5, 6.5), ("c09-restock-drive-suburb.mp4", 6, None)],
         scene=dict(type="ledger", params=dict(w=1150, y=220, lines=[
             dict(label="Office machine", value="$280–350/mo", cue=0, dot="sup"),
             dict(label="Repair shop machine", value="$120–180/mo", cue="@The repair shop", dot="sup"),
             dict(label="Kept", value="$130–150/mo", cue="@they say they keep", total=True)]))),
    dict(at="Their verdict was simple", kind="GF", clip="c09-restock-drive-suburb.mp4", **{"in": 11.0},
         scene=dict(type="quote", params=dict(at="@It's not as passive", text="“It's not as passive as people make it sound.”", size=120, y=330))),
    dict(at="Now do the math", kind="GF", clips=[("c02-driver-paperwork.mp4", 12, 9.5), ("c03-receipt.mp4", 14, None)],
         scene=dict(type="payback", params=dict(title="Paying off a $3,500 machine", years=15, marks=[
             dict(years=14.6, label="14+ years", key="loc", op=0.55, align="right", cue="@14 years"),
             dict(years=1.67, label="20 months", key="own", cue="@20 months")],
             source=SRC_VMFS))),
    ftg("Things do break", "c04-dollar-bill-acceptor.mp4", 0.5),
    ftg("and an attempted break-in", "c09-security-camera.mp4", 2.0),
    ftg("Then there's debt", "c09-credit-card-overdue.mp4", 2.0),
    dict(at="looked at one creator's breakdown", kind="GF", clip="c09-calculator-hands.mp4", **{"in": 2.0},
         scene=dict(type="quote", params=dict(at="@And his advice", size=104, y=330,
                    text="Save it in cash. Don't borrow it.", by="George Kamel, via 24/7 Wall St."))),
    ftg("Put it on a card", "01-phone-pay-vending.mp4", 5.5),

    # ---------------------------------------------------------------- 10 · Buying a route
    dict(at="If you'd rather buy a route", kind="F", clips=[("c10-financial-docs-review.mp4", 0.2, 5), ("c01-office-lobby.mp4", 12, None)]),
    dict(at="BizBuy sells figures", kind="GF", clip="c10-spreadsheet-monitor.mp4", **{"in": 1.0},
         scene=dict(type="multiple", params=dict(title="What vending businesses sell for", max=4, marks=[
             dict(x=2.0, label="≈ 2×", key="sup", cue="@two times")],
             source="BizBuySell"))),
    ftg("One Chicago area route", "c10-arlington-heights-aerial.mp4", 3.0),
    dict(at="The seller estimates", kind="GF", clip="c10-chicago-suburbs-aerial.mp4", **{"in": 10.0},
         scene=dict(type="multiple", params=dict(title="One Chicago-area route, 12 machines", max=4, marks=[
             dict(x=2.0, label="≈ 2×", key="tax", cue=0),
             dict(x=2.8, label="2.8×", key="loc", cue="@nearly three times", above=False)],
             source="The Route Exchange"))),
    ftg("Those are asking prices", "c10-calculator-ledger.mp4", 1.0),
    ftg("A careful buyer asks", "c10-checking-sales-records.mp4", 1.0),

    # ---------------------------------------------------------------- 11 · Operation Vend Up Broke
    ftg("And none of this is new", "c11-newsprint-listings.mp4", 5.0),
    dict(at="In 1998, the Federal Trade Commission", kind="D",
         scene=dict(type="doc", params=dict(header="FTC press release, Sept 3, 1998", size=48,
                    html='FTC Announces <span class="hl" data-cue="@Operation Vend Up Broke">"OPERATION VEND UP BROKE"</span>: States and Feds Stop Business Opportunity Scams<br><br>"Every year, thousands of consumers literally end up broke after investing in purportedly lucrative vending opportunities." … <span class="hl" data-cue="@fake references">"You can\'t rely on supposedly satisfied consumers supplied by the seller."</span>'))),
    ftg("The ads have moved", "c11-phone-night-viewer.mp4", 6.0),
    dict(at="and the math behind them", kind="D",
         scene=dict(type="doc", params=dict(header="Trustpilot review of a vending locator", size=56, y=300,
                    html='"He provided me with <span class="hl" data-cue="0">\'leads\', not actual locations.</span>"'))),

    # ---------------------------------------------------------------- 12 · Who really wins
    dict(at="Back to your $2", kind="GF", clips=[("c12-vending-closeup.mp4", 1, 8), ("c02-office-vending.mp4", 2, None)],
         scene=split([0, 0, 0, 0, 0, 0], amounts=True, wholeAt=0, splitAt=0, dim=0.8, y=390,
                     tally=dict(label="Operator keeps", at=0, steps=[dict(cents=138, cue=0)]))),
    dict(at="The people who win", kind="GF", clip="c02-combo-machine.mp4", **{"in": 1.0},
         scene=dict(type="cards", params=dict(valueSize=100, items=[
             dict(label="", value="Location", key="loc", cue="@the location"),
             dict(label="", value="Scale", key="sup", cue="@the scale"),
             dict(label="", value="Technology", key="pay", cue="@the technology")]))),
    dict(at="So if you're ever looking", kind="GF", clip="c10-checking-sales-records.mp4", **{"in": 4.0},
         scene=dict(type="checklist", params=dict(title="Before you buy a route", y=280, rowH=104, font=54, box=64, items=[
             dict(text="Does it own the location, scale or tech?", key="hl", cue="@ask which"),
             dict(text="Location contracts that transfer", cue="@ask which"),
             dict(text="Sales records for every machine", cue="@ask which"),
             dict(text="Machine age", cue="@ask which"),
             dict(text="Card vs cash sales", cue="@ask which")]))),
    dict(at="Would you still buy one", kind="GF", clip="c09-laptop-night.mp4", **{"in": 4.0},
         scene=dict(type="quote", params=dict(at=0, text="Would you still buy one?", size=140, y=420))),
    ftg("Next time, the car wash", "c12-car-wash-tunnel.mp4", 2.0),
    dict(at="Subscribe so you don't miss it", kind="G", scene=dict(type="end", opaque=True, params=dict(logo=LOGO, y=300))),
]

END_TAIL = 20.0  # seconds of end screen after the last word
