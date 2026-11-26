"""Episode 1 edit plan: one entry per shot. Used for the stills storyboard and the final render.

at     phrase where the shot starts (as Whisper wrote it in voiceover/timings-clean.json); None = 0:00
kind   F = footage · GF = graphic over darkened footage · G = full-screen graphic · D = Deal File document
clip   file in footage/ ; in = seconds into the clip
scene  graphic (tools/video/gfx/scenes.html). Strings starting with "@" are phrases: they become the time
       (seconds from shot start) when that phrase is spoken, so each number appears as it's said.
"""

SRC_VMFS = "VMFS USA, 2026"
SRC_CANT = "Cantaloupe, 2025 data"

SPLIT = [  # The $2 soda, per the supplier's model (6% tax, 10% commission, mostly card)
    dict(key="tax", label="GOVERNMENT", amount="11¢", cents=11, row=1, align="left"),
    dict(key="sup", label="DRINK COMPANY", amount="94¢", cents=94, row=0),
    dict(key="pay", label="CARD PROCESSOR", amount="9¢", cents=9, row=1),
    dict(key="pay", label="SOFTWARE", amount="4¢", cents=4, row=-1),
    dict(key="loc", label="THE BUILDING", amount="20¢", cents=20, row=0, align="left"),
    dict(key="own", cents=62, inside="OWNER ?"),
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
            d["inside"] = "OWNER 62¢"
        sl.append(d)
    return dict(type="split", params=dict(slices=sl, **kw))


CHAPTERS = [
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
    dict(at=None, kind="F", clip="01-phone-pay-vending.mp4", **{"in": 1.0}),
    dict(at="and a soda drops", kind="F", clip="c12-vending-closeup.mp4", **{"in": 4.0}),
    dict(at="$2", kind="GF", clip="c02-office-vending.mp4", **{"in": 6.0},
         scene=split(["@government", "@drink company", "@card processor", "@software company", "@the building", None],
                     title="$2.00", titleAt=0, wholeAt="@Before the owner", splitAt="@five other players", dim=0.72,
                     wholeLabel="$2.00"),
         note="The Split: the bar breaks into 5 players; each lights up as it's named. Owner's slice stays blank."),
    dict(at="At one of the busiest airports", kind="F", clip="c05-lax-plane-landing-sunset.mp4", **{"in": 4.0}),
    dict(at="the building takes", kind="GF", clip="c05-lax-dusk-overview.mp4", **{"in": 3.0},
         blur=[(1520, 800, 310, 150), (770, 990, 190, 80)], 
         scene=dict(type="bignum", params=dict(at="@59.5%", count=[0, 59.5], fmt="pct1", size=300, y=250,
                                               lines=[dict(text="of every sale goes to the building"),
                                                      dict(text="The full deal, later in this video", at="@We'll get to that deal")]))),
    dict(at="Online, vending machines", kind="F", clip="c11-phone-night-viewer.mp4", **{"in": 2.0}),
    dict(at="as easy passive income", kind="GF", clip="c02-combo-machine.mp4", **{"in": 3.0},
         scene=dict(type="quote", params=dict(at=0, text="“Easy passive income.”", by="Stock it once a week and let the cash pile up.",
                                              byAt="@Stock a machine", strikeAt="@let the cash pile up", size=150))),
    dict(at="So we check the real numbers", kind="GF", clip="c05-traveler-vending-snack.mp4", **{"in": 1.0},
         scene=dict(type="sources", params=dict(kicker="Where our numbers come from", items=[
             dict(title="Payment data", sub="Cantaloupe's report on 600,000+ machines, 2025", key="pay", cue="@payment data"),
             dict(title="Public contracts", sub="LAX board report · Riverside college district", key="loc", cue="@public contracts"),
             dict(title="Operators' own results", sub="As posted. We flag what we can't verify", key="sup", cue="@operators")]))),
    dict(at="The picture is a lot less exciting", kind="F", clip="c05-traveler-vending-snack.mp4", **{"in": 4.0}),
    dict(at="So let's follow the $2", kind="GF", clip="c12-vending-closeup.mp4", **{"in": 7.0},
         scene=dict(type="chapter", params=dict(kicker="Chapter 1", title="Follow the $2", rule="own"))),

    # ---------------------------------------------------------------- 2 · Who owns the machine
    dict(at="These machines usually belong", kind="F", clip="c02-route-driver-van.mp4", **{"in": 1.0}),
    dict(at="places them in other people's buildings", kind="F", clip="c02-office-vending.mp4", **{"in": 3.0}),
    dict(at="In 2025, US vending operators", kind="GF", clip="c02-van-aerial-road.mp4", **{"in": 1.0},
         scene=dict(type="bignum", params=dict(at="@$7 billion", text="$7B+", size=280, y=260, lines=[
             dict(text="brought in by US vending operators in 2025")], source="IBISWorld, 2025"))),
    dict(at="The biggest names are food service giants", kind="GF", clip="c02-van-aerial-road.mp4", **{"in": 4.0},
         scene=dict(type="tiles", params=dict(kicker="Who runs America's vending machines", big=[
             dict(title="Compass Group", sub="owns Canteen", key="sup", cue="@Compass"),
             dict(title="Aramark", sub="food service giant", key="sup", cue="@Aramark")],
             smallCue="@small, local businesses", smallLabel="Thousands of small, local operators",
             note="Illustration. Not to scale.", source="IBISWorld"))),
    dict(at="Most of them are built around a route", kind="G",
         scene=dict(type="route", opaque=True, params=dict(kicker="A route", steps=[
             dict(text="Restock", cue="@restocking"), dict(text="Pull cash", cue="@pulling cash"), dict(text="Fix what broke", cue="@fixing")]))),
    dict(at="The machines aren't cheap", kind="F", clip="c02-combo-machine.mp4", **{"in": 6.0}),
    dict(at="One supplier sells small", kind="GF", clip="c02-combo-machine.mp4", **{"in": 8.0},
         scene=dict(type="cards", params=dict(kicker="What a machine costs", y=230, h=560, valueSize=120, items=[
             dict(label="Countertop", value="$1,900", icon="countertop", key="sup", cue="@countertop"),
             dict(label="Combo snack + drink", value="$3,450", icon="combo", key="sup", cue="@combo"),
             dict(label="Elevator", value="$8,650", icon="elevator", key="sup", cue="@An elevator machine")],
             source="VMFS USA, 2026"))),
    dict(at="Then there's the deal with the location", kind="F", clip="c08-office-break-room.mp4", **{"in": 1.0}),
    dict(at="Busy places know", kind="GF", clip="c08-office-break-room.mp4", **{"in": 5.0},
         scene=dict(type="bignum", params=dict(at="@five to 20%", text="5–20%", size=280, y=260, lines=[
             dict(text="of gross sales: the usual ask from busy locations")], source="VMFS USA; Nav"))),
    dict(at="Sales per machine depend", kind="GF", clip="c02-hospital-corridor.mp4", **{"in": 1.0},
         scene=dict(type="bars", params=dict(kicker="Monthly sales per machine", max=2600, labelW=520, items=[
             dict(label="Typical site", from_=150, value=700, text="$150–700", key="sup", cue="@a typical site"),
             dict(label="Strong site", value=1500, text="up to $1,500", key="sup", cue="@a strong one"),
             dict(label="Top spots", sub="hospitals, factories, transit", value=2000, text="$2,000+", key="sup", cue="@Top spots")],
             source="VMFS USA"))),

    # ---------------------------------------------------------------- 3 · Following the two dollars
    dict(at="Those are sales figures", kind="F", clip="01-phone-pay-vending.mp4", **{"in": 5.0}),
    dict(at="Here's how one equipment supplier", kind="GF", clip="c03-receipt.mp4", **{"in": 3.0},
         scene=dict(type="ledger", params=dict(kicker="One supplier's model of a $2 soda", w=1200, y=200, lines=[
             dict(label="Price", value="$2.00", cue=0),
             dict(label="Sales tax", value="6%", cue="@6%", dot="tax"),
             dict(label="Location commission", value="10%", cue="@10%", dot="loc"),
             dict(label="Paid by card or phone", value="78%", cue="@paying by card", dot="pay")], source=SRC_VMFS))),
    dict(at="First, about 11 cents", kind="GF", clip="c02-office-vending.mp4", **{"in": 10.0},
         scene=split(["@11 cents", "@94 cents", "@Card processing", "@four more", "@The building takes", "@That leaves"],
                     amounts=True, kicker="Follow the $2", wholeAt=0, splitAt=0, dim=0.8, y=390,
                     tally=dict(label="Operator keeps", at=0, steps=[
                         dict(cents=11, cue="@11 cents"), dict(cents=94, cue="@94 cents"), dict(cents=9, cue="@nine cents"),
                         dict(cents=4, cue="@four more"), dict(cents=20, cue="@20 cents")]), source=SRC_VMFS),
         note="The Split, full: each slice gets its cents as spoken; the tally counts $2.00 down to $0.62."),
    dict(at="before paying for gas", kind="GF", clip="c03-highway-driving.mp4", **{"in": 6.0},
         scene=split([0, 0, 0, 0, 0, 0], amounts=True, labels=False, kicker="Then the operator pays for…", wholeAt=0, splitAt=0, dim=0.8, y=390,
                     costs=[dict(label="Gas", cue="@gas"), dict(label="Labor", cue="@labor"), dict(label="Repairs", cue="@repairs"),
                            dict(label="Insurance", cue="@insurance"), dict(label="Income tax", cue="@income tax")])),
    dict(at="Every restock means driving out", kind="F", clip="c03-highway-driving.mp4", **{"in": 2.0}),
    dict(at="Those costs come out", kind="F", clip="c03-gas-pump-gallons.mp4", **{"in": 2.0}),
    dict(at="Run the full numbers", kind="GF", clip="c09-calculator-hands.mp4", **{"in": 6.0},
         scene=dict(type="ledger", params=dict(kicker="One machine, one month", w=1250, y=190, lines=[
             dict(label="Sales", value="$900", cue="@$900"),
             dict(label="Operator keeps", value="$197", cue="@keeps about", total=True)],
             note="22% margin. Before the owner's own time, any loan and income tax.", noteAt="@22%",
             source="VMFS USA, 2026"))),
    dict(at="And the better the location", kind="D",
         scene=dict(type="doc", params=dict(header="Riverside Community College District · vending agreement, 2022–2027 · excerpt",
                    html='(5) Commission Proposal - The Vendor guarantees commission of <span class="hl" data-cue="0">33% on gross sales</span>, and a signing bonus in the amount of $5,000 ...',
                    source="Riverside CCD vending services agreement, Aug 2022"))),
    dict(at="and that airport from the start", kind="GF", clip="c05-lax-dusk-overview.mp4", **{"in": 8.0},
         blur=[(1520, 800, 310, 150), (770, 990, 190, 80)], 
         scene=dict(type="bars", params=dict(kicker="The location's cut of every sale", max=70, labelW=520, items=[
             dict(label="The $2 soda model", value=10, text="10%", key="loc", cue=0),
             dict(label="Riverside college", value=33, text="33%", key="loc", cue=0.3),
             dict(label="That airport", locked=True, cue="@its deal is bigger")]))),

    # ---------------------------------------------------------------- 4 · Card payments
    dict(at="Card payments do help", kind="F", clip="c04-card-tap-terminal.mp4", **{"in": 1.0}),
    dict(at="people paying by card or phone", kind="GF", clip="c04-card-tap-terminal.mp4", **{"in": 4.0},
         scene=dict(type="cards", params=dict(kicker="Average vending purchase, 2025", y=260, h=470, valueSize=170, items=[
             dict(label="Card or phone", value="$2.45", key="pay", cue="@$2.45"),
             dict(label="Cash", value="$1.57", key="tax", cue="@$1.57")],
             note="Card buyers spend 88¢ more per purchase", noteAt="@Card fees cost", source=SRC_CANT))),
    dict(at="and 78%", kind="GF", clip="c04-dollar-bill-acceptor.mp4", **{"in": 1.0},
         scene=dict(type="bignum", params=dict(at=0, count=[0, 78], fmt="pct0", size=300, y=250, lines=[
             dict(text="of vending sales on that network were cashless")], source=SRC_CANT))),
    dict(at="So the operator ends up", kind="GF", clip="c05-traveler-vending-snack.mp4", **{"in": 6.0},
         scene=dict(type="cards", params=dict(kicker="The bigger money goes to", y=300, h=360, valueSize=96, items=[
             dict(label="Winner 1", value="Location", key="loc", cue="@three kinds"),
             dict(label="Winner 2", value="Scale", key="sup", cue="@three kinds"),
             dict(label="Winner 3", value="Payments", key="pay", cue="@three kinds")]))),

    # ---------------------------------------------------------------- 5 · Winner 1: the location
    dict(at="Winner number one", kind="GF", clip="c05-lax-dusk-overview.mp4", **{"in": 12.0},
         blur=[(1520, 800, 310, 150), (770, 990, 190, 80)], 
         scene=dict(type="chapter", params=dict(kicker="Winner 1", title="The location", rule="loc"))),
    dict(at="That airport is Los Angeles", kind="F", clip="c05-lax-theme-building-day.mp4", **{"in": 2.0},
         note="Blur the small Delta billboard, lower right."),
    dict(at="In 2023, its board", kind="D",
         scene=dict(type="doc", params=dict(header="LA Board of Airport Commissioners · Feb 16, 2023 · board report, excerpt",
                    html='Pursuant to the terms of the proposed concession agreement, First Class will pay LAWA the greater of a minimum monthly guarantee of <span class="hl" data-cue="@$100">$100 per machine</span> or <span class="hl" data-cue="@59.5%">59.5 percent of gross sales</span> over the five-year term and any approved options.',
                    source="LA Board of Airport Commissioners, Feb 16 2023"))),
    dict(at="Even the runner-up bid", kind="GF", clip="c05-contract-signing.mp4", **{"in": 2.0},
         scene=dict(type="bars", params=dict(kicker="Bids for the LAX vending contract (% of gross sales)", max=80, labelW=600, items=[
             dict(label="First Class Vending", sub="won", value=59.5, text="59.5%", key="loc", cue=0),
             dict(label="Canteen", sub="Compass Group", value=51.6, text="51.6%", key="sup", cue="@Canteen"),
             dict(label="Gilly Vending", value=42.0, text="42.0%", key="tax", cue="@Canteen")],
             source="LAX board report, 2023"))),
    dict(at="The operator runs and maintains", kind="F", clip="c05-traveler-vending-snack.mp4", **{"in": 1.0}),
    dict(at="The airport just collects", kind="F", clip="06-airport-terminal-4k.mp4", **{"in": 1.0}),

    # ---------------------------------------------------------------- 6 · Winner 2: scale
    dict(at="Winner number two", kind="GF", clip="c06-trucks-docks-aerial.mp4", **{"in": 2.0},
         scene=dict(type="chapter", params=dict(kicker="Winner 2", title="Scale", rule="sup"))),
    dict(at="Driving between machines", kind="G",
         scene=dict(type="route", opaque=True, params=dict(mode="compare", kicker="Same work, different driving",
                    a=dict(title="100 machines, one area", sub="short loop", cue="@100 machines"),
                    b=dict(title="10 machines, across a city", sub="long drives between stops", cue="@10 machines")))),
    dict(at="Big operators also buy", kind="F", clip="c06-warehouse-drink-racks.mp4", **{"in": 2.0}),
    dict(at="The biggest of them all", kind="F", clip="c06-chicago-skyline.mp4", **{"in": 2.0}),
    dict(at="It started in Chicago", kind="GF", clip="c06-archival-1933-street.mp4", **{"in": 2.0},
         scene=dict(type="bignum", params=dict(at=0, text="1929", size=240, y=300, dim=0.5, lines=[
             dict(text="Canteen starts in Chicago, selling 5¢ candy bars from machines")], source="Canteen"))),
    dict(at="Today, Compass Group describes", kind="GF", clip="c01-office-lobby.mp4", **{"in": 4.0},
         scene=dict(type="quote", params=dict(at=0, size=110, y=300, byOffset=270,
                    text="“The largest unattended retail provider in the United States.”", by="Compass Group, describing Canteen",
                    source="Compass Group"))),
    dict(at="And the big players keep getting bigger", kind="GF", clip="c06-trucks-docks-aerial.mp4", **{"in": 8.0},
         scene=dict(type="flow", params=dict(kicker="2025", src=dict(title="Buffalo Rock", sub="Alabama bottler"), dst=dict(title="Canteen", sub="and its franchise partners"), arrowLabel="sold its vending business",
                    facts=[dict(text="~700 micro markets", cue="@700", key="sup"),
                           dict(text="7,600+ vending locations", cue="@7,600", key="sup")],
                    source="VendingMarketWatch, 2025"))),

    # ---------------------------------------------------------------- 7 · Winner 3: payments
    dict(at="The third winner", kind="GF", clip="c01-card-reader-tap.mp4", **{"in": 2.0},
         scene=dict(type="chapter", params=dict(kicker="Winner 3", title="The payment network", rule="pay"))),
    dict(at="Every tap sends", kind="F", clip="c08-card-tap-unlock.mp4", **{"in": 0.5}),
    dict(at="Cantaloupe, one of the biggest", kind="GF", clip="c01-server-room.mp4", **{"in": 2.0},
         scene=dict(type="cards", params=dict(kicker="Cantaloupe's network, US and Canada, 2025", y=280, h=430, valueSize=150, items=[
             dict(label="Connected machines and kiosks", value="600,000+", key="pay", cue="@600,000"),
             dict(label="Sales handled", value="$4.6B", key="pay", cue="@$4.6 billion")], source=SRC_CANT))),
    dict(at="Cantaloupe earns a cut", kind="GF", clip="c01-server-room.mp4", **{"in": 6.0},
         scene=dict(type="flow", params=dict(kicker="How the payment company gets paid", src=dict(title="Every card sale", sub="at the machine"), dst=dict(title="Cantaloupe", sub="runs the card reader"), arrowLabel="a cut + monthly fees",
                    facts=[dict(text="No snacks to stock. No route to drive.", cue="@without stocking", key="pay")]))),
    dict(at="And Cantaloupe itself just changed hands", kind="GF", clip="c10-handshake-warehouse.mp4", **{"in": 2.0},
         scene=dict(type="flow", params=dict(kicker="May 2026", src=dict(title="365 Retail Markets", sub="a rival"), dst=dict(title="Cantaloupe", sub="payment network"), arrowLabel="bought", facts=[
             dict(text="About $848 million, all cash", cue="@$848 million", key="pay"),
             dict(text="Approved after it agreed to sell a competing kiosk business", cue="@Regulators", key="tax")],
             source="SEC filing; FTC, 2026"))),

    # ---------------------------------------------------------------- 8 · Micro markets
    dict(at="But some of the biggest changes", kind="F", clip="c09-busy-office.mp4", **{"in": 4.0}),
    dict(at="A micro market is an unlocked", kind="F", clip="c08-grab-and-go-cooler.mp4", **{"in": 2.0}),
    dict(at="and a self-checkout kiosk", kind="F", clip="c08-self-checkout-scan.mp4", **{"in": 2.0}),
    dict(at="In 2025, the average vending purchase", kind="GF", clip="c08-kiosk-touchscreen.mp4", **{"in": 2.0},
         scene=dict(type="bars", params=dict(kicker="Average purchase, 2025", max=5.6, labelW=560, items=[
             dict(label="Vending machine", value=2.01, text="$2.01", key="tax", cue="@$2.01"),
             dict(label="Micro market", value=3.02, text="$3.02", key="sup", cue="@$3.02"),
             dict(label="Smart store", sub="locked fridge or cabinet", value=4.49, text="$4.49", key="pay", cue="@$4.49")],
             source=SRC_CANT))),
    dict(at="Micro markets on that network", kind="GF", clip="c08-grab-and-go-cooler.mp4", **{"in": 8.0},
         scene=dict(type="cards", params=dict(kicker="2025, on Cantaloupe's network", y=260, h=470, valueSize=104, items=[
             dict(label="Micro markets", value="$1B+", sub="in sales, up 13%", key="sup", cue="@billion"),
             dict(label="Smart stores", value="71→572", sub="locations in one year", key="pay", cue="@71 locations"),
             dict(label="Smart-store sales", value="$6M", sub="all of them, combined", key="pay", cue="@$6 million")],
             source=SRC_CANT))),
    dict(at="Vending machines still bring in", kind="GF", clip="c02-office-vending.mp4", **{"in": 12.0},
         scene=dict(type="bars", params=dict(kicker="Total sales on that network, 2025", max=3.9, labelW=560, items=[
             dict(label="Vending machines", value=3.3, text="$3.3B", key="tax", cue=0),
             dict(label="Micro markets", value=1.0, text="$1B+", sub="growing 13%", key="sup", cue=0.2),
             dict(label="Smart stores", value=0.006, text="$6M", sub="8× more locations", key="pay", cue=0.4)],
             note="The newest formats are the smallest, and the fastest-growing.", noteAt="@But the fastest growth",
             source=SRC_CANT))),

    # ---------------------------------------------------------------- 9 · A beginner's first six months
    dict(at="But the passive income videos", kind="F", clip="c09-laptop-night.mp4", **{"in": 2.0}),
    dict(at="They posted their numbers", kind="G",
         scene=dict(type="post", opaque=True, params=dict(meta="An operator's post · r/passive_income · Jan 2026",
                    title="Vending machine side hustle: 6-month update",
                    body="$3,200 on two refurbished machines, plus $400 of snacks and drinks. One sits in an office with about 50 employees, the other in an auto repair shop.",
                    tag="Self-reported. We couldn't verify these numbers.", source="Benzinga, Jan 2026"))),
    dict(at="One machine sits in an office", kind="F", clip="c09-busy-office.mp4", **{"in": 14.0}),
    dict(at="The other is in an auto repair shop", kind="F", clip="c09-mechanic-under-lift.mp4", **{"in": 1.0}),
    dict(at="The office machine brings in", kind="GF", clip="c09-auto-repair-shop.mp4", **{"in": 2.0},
         scene=dict(type="ledger", params=dict(kicker="Their first six months, per month", w=1300, y=190, lines=[
             dict(label="Office machine sales", value="$280–350", cue=0, dot="sup"),
             dict(label="Repair-shop machine sales", value="$120–180", cue="@The repair shop", dot="sup"),
             dict(label="Kept after gas, restocking, repairs", value="$130–150", cue="@they say they keep", total=True)],
             note="Self-reported. It fits the supplier's own ranges.", noteAt="@We can't check"))),
    dict(at="Their verdict was simple", kind="GF", clip="c09-restock-drive-suburb.mp4", **{"in": 3.0},
         scene=dict(type="quote", params=dict(at="@It's not as passive", text="“It's not as passive as people make it sound.”",
                                              size=120, y=320, by="The operator's own verdict", byOffset=290))),
    dict(at="Now do the math", kind="G",
         scene=dict(type="payback", opaque=True, params=dict(title="Paying off a $3,500 machine at a typical site", years=15, marks=[
             dict(years=14.6, label="14+ years", sub="if it nets $20 a month", key="loc", op=0.55, align="right", cue="@14 years"),
             dict(years=1.67, label="20 months", sub="if it nets $175 a month", key="own", cue="@20 months")],
             note="And that's if nothing breaks.", noteAt="@if nothing breaks", source="VMFS USA, 2026"))),
    dict(at="Things do break", kind="F", clip="c04-dollar-bill-acceptor.mp4", **{"in": 2.5}),
    dict(at="and an attempted break-in", kind="F", clip="c09-security-camera.mp4", **{"in": 2.0}),
    dict(at="Then there's debt", kind="F", clip="c09-credit-card-overdue.mp4", **{"in": 2.0}),
    dict(at="looked at one creator's breakdown", kind="GF", clip="c09-calculator-hands.mp4", **{"in": 2.0},
         scene=dict(type="quote", params=dict(at="@And his advice", size=110, y=300, byOffset=280,
                    text="His advice: save it in cash. Don't borrow it.",
                    by="George Kamel, on a $3,330 start-up budget (as reported by 24/7 Wall St.)", source="24/7 Wall St., 2026"))),
    dict(at="Put it on a card", kind="F", clip="c09-credit-card-overdue.mp4", **{"in": 7.0}),

    # ---------------------------------------------------------------- 10 · Buying a route
    dict(at="If you'd rather buy a route", kind="F", clip="c10-financial-docs-review.mp4", **{"in": 0.5}),
    dict(at="BizBuy sells figures", kind="GF", clip="c10-spreadsheet-monitor.mp4", **{"in": 2.0},
         scene=dict(type="multiple", params=dict(title="What vending businesses sell for", max=4, marks=[
             dict(x=2.0, label="≈ 2×", sub="yearly owner earnings · typical price $83,500", key="sup", cue="@two times")],
             note="Owner earnings include the owner's own pay.", noteAt="@two times", source="BizBuySell, 2021–25"))),
    dict(at="One Chicago area route", kind="F", clip="c10-arlington-heights-aerial.mp4", **{"in": 3.0}),
    dict(at="The seller estimates", kind="GF", clip="c10-chicago-suburbs-aerial.mp4", **{"in": 10.0},
         scene=dict(type="multiple", params=dict(title="One Chicago-area route, 12 machines", max=4, marks=[
             dict(x=2.0, label="≈ 2×", sub="typical sale", key="tax", cue=0),
             dict(x=2.8, label="2.8×", sub="$138,000 asking ÷ $49,000 a year", key="loc", cue="@nearly three times", above=False)],
             source="The Route Exchange"))),
    dict(at="Those are asking prices", kind="F", clip="c10-calculator-ledger.mp4", **{"in": 1.0}),
    dict(at="A careful buyer asks", kind="F", clip="c10-checking-sales-records.mp4", **{"in": 1.0}),

    # ---------------------------------------------------------------- 11 · Operation Vend Up Broke
    dict(at="And none of this is new", kind="F", clip="c11-newsprint-listings.mp4", **{"in": 5.0}),
    dict(at="In 1998, the Federal Trade Commission", kind="D",
         scene=dict(type="doc", params=dict(header="Federal Trade Commission · press release · Sept 3, 1998 · excerpt", size=42,
                    html='FTC Announces <span class="hl" data-cue="@Operation Vend Up Broke">"OPERATION VEND UP BROKE"</span>: States and Feds Stop Business Opportunity Scams<br><br>"Every year, thousands of consumers literally end up broke after investing in purportedly lucrative vending opportunities." … <span class="hl" data-cue="@fake references">"You can\'t rely on supposedly satisfied consumers supplied by the seller."</span>',
                    source="FTC, Sept 3 1998"))),
    dict(at="The ads have moved", kind="G",
         scene=dict(type="versus", params=dict(adHead="OWN YOUR OWN VENDING ROUTE!", adBody="No experience needed. Prime locations included. Call today!",
                    feedHead="I make $3,000 a month from 5 vending machines", feedBody="Link in bio for my locator", feedCue="@TikTok"))),
    dict(at="and the math behind them", kind="D",
         scene=dict(type="doc", params=dict(header="Trustpilot · 1-star review of a vending \"locator\" service", size=56, y=300,
                    html='"He provided me with <span class="hl" data-cue="0">\'leads\', not actual locations.</span>"',
                    source="Trustpilot review, vending locator service"))),

    # ---------------------------------------------------------------- 12 · Who really wins
    dict(at="Back to your $2", kind="GF", clip="c12-vending-closeup.mp4", **{"in": 2.0},
         scene=split([0, 0, 0, 0, 0, 0], amounts=True, kicker="Back to your $2", wholeAt=0, splitAt=0, dim=0.8, y=390,
                     tally=dict(label="Operator keeps", at=0, steps=[dict(cents=138, cue=0)]))),
    dict(at="The people who win", kind="GF", clip="c02-combo-machine.mp4", **{"in": 1.0},
         scene=dict(type="cards", params=dict(kicker="Who wins in vending", y=230, h=330, valueSize=90, items=[
             dict(label="Own the", value="Location", key="loc", cue="@the location"),
             dict(label="Own the", value="Scale", key="sup", cue="@the scale"),
             dict(label="Own the", value="Technology", key="pay", cue="@the technology")],
             center=dict(label="THE BOX IN THE MIDDLE", cue="@box in the middle")))),
    dict(at="So if you're ever looking", kind="GF", clip="c10-checking-sales-records.mp4", **{"in": 4.0},
         scene=dict(type="checklist", params=dict(title="Before you buy a route, ask:", y=270, rowH=104, font=52, box=64, items=[
             dict(text="Does it own the location, the scale or the tech?", key="hl", cue="@ask which"),
             dict(text="Location contracts: how long, and do they transfer?", cue="@ask which"),
             dict(text="Sales records for every machine", cue="@ask which"),
             dict(text="Age of the machines", cue="@ask which"),
             dict(text="Card vs cash sales", cue="@ask which"),
             dict(text="Who restocks when you can't?", cue="@ask which")]))),
    dict(at="Would you still buy one", kind="GF", clip="c12-vending-closeup.mp4", **{"in": 1.0},
         scene=dict(type="quote", params=dict(at=0, text="Would you still buy one?", size=130, y=330,
                    by="Own a route? Tell us your real numbers in the comments.", byAt="@And if you own", byOffset=210))),
    dict(at="Next time, the car wash", kind="GF", clip="c12-car-wash-tunnel.mp4", **{"in": 2.0},
         scene=dict(type="chapter", params=dict(kicker="Next episode", title="The car wash", rule="hl", dim=0.45))),
    dict(at="Subscribe so you don't miss it", kind="G", scene=dict(type="end", opaque=True, params=dict())),
]

END_TAIL = 20.0  # seconds of end screen after the last word
