"""Episode 1 edit plan: one entry per shot. Used for the stills storyboard and the final render.

at     phrase where the shot starts (as Whisper wrote it in voiceover/timings-clean.json); None = 0:00
kind   F = footage · GF = light graphic on footage · B = graphic on its own background image · G = full-screen · D = Deal File
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

def B(at, bg, scene, **kw):
    """A graphic on its own background image: bg=(clip, seconds) becomes a blurred, darkened, slowly drifting still."""
    return dict(at=at, kind="B", bg=bg, scene=scene, **kw)


def sc(type, **params):
    return dict(type=type, params=params)


# Templates are numbered as in docs/templates (template sheets). Footage-only shots have nothing on top.
SHOTS = [
    # ---------------------------------------------------------------- 1 · Hook
    ftg(None, "01-phone-pay-vending.mp4", 1.0),
    ftg("and a soda drops", "c12-vending-closeup.mp4", 4.0),
    B("$2", ("c12-vending-closeup.mp4", 6.0),                                               # T9 The Split
      split(["@government", "@drink company", "@card processor", "@software company", "@the building", None],
            title="$2.00", titleAt=0, wholeAt="@Before the owner", splitAt="@five other players")),
    ftg("At one of the busiest airports", "c05-lax-plane-landing-sunset.mp4", 4.0),
    dict(at="the building takes", kind="GF", clip="c05-lax-dusk-overview.mp4", **{"in": 3.0}, blur=LAX_NIGHT_BLUR,   # T1
         scene=sc("num", at="@59.5%", count=[0, 59.5], fmt="pct1", label="of every sale goes to the building", y=110)),
    ftg("Online, vending machines", "c11-phone-night-viewer.mp4", 2.0),
    dict(at="as easy passive income", kind="GF", clip="c11-phone-night-viewer.mp4", **{"in": 4.0},                   # T15 on the footage, low
         scene=sc("strike", x=140, y=780, size=110, lines=[
             dict(text="“Easy passive income.”", at=0, strikeDelay=1.4),
             dict(text="“Stock it once a week.”", at="@Stock a machine", strikeDelay=1.6),
             dict(text="“Let the cash pile up.”", at="@let the cash pile up", strikeDelay=1.4)])),
    B("So we check the real numbers", ("c10-checking-sales-records.mp4", 2.0),                                       # T8 papers
      sc("papers", items=[dict(title="Payment data", sub="Cantaloupe, 2025", cue="@payment data"),
                          dict(title="Public contracts", sub="LAX board, 2023", cue="@public contracts"),
                          dict(title="Operators' own results", sub="Posted online", cue="@operators")])),
    ftg("The picture is a lot less exciting", "c03-hand-truck.mp4", 8.0),
    ftg("So let's follow the $2", "c12-coins-in-hand.mp4", 4.0),

    # ---------------------------------------------------------------- 2 · Who owns the machine
    dict(at="These machines usually belong", kind="F", clips=[("c02-route-driver-van.mp4", 0.0, None, {"until": 4.65})]),  # source has a cut at 4.7 s
    ftg("places them in other people's buildings", "c02-office-vending.mp4", 3.0),
    dict(at="more than $7 billion", kind="GF", clip="c02-van-aerial-road.mp4", **{"in": 1.0},                        # T1
         scene=sc("num", at="@$7 billion", text="$7B+", label="US vending operators, 2025", source="IBISWorld", y=110)),
    B("The biggest names are food service giants", ("c06-chicago-skyline.mp4", 3.0),                                 # T16
      sc("company", at="@Compass", size=170, names=[dict(text="Compass Group", cue="@Compass"), dict(text="Aramark", cue="@Aramark")],
         lines=[dict(text="and thousands of small, local operators", cue="@small, local businesses")])),
    dict(at="Most of them are built around a route", kind="G",                                                        # T4
         scene=sc("routeMap", img=("c10-chicago-suburbs-aerial.mp4", 31.0), at="@drives a loop", drawDur=3.5,
                  pts=[[180, 880], [460, 800], [800, 850], [1120, 900], [1180, 990], [840, 1010], [500, 1000], [220, 980]])),
    B("The machines aren't cheap", ("n-street-vending-man.mp4", 3.0),                                                # T17
      sc("columns", items=[dict(label="Countertop", value="$1,900", key="sup", cue="@countertop"),
                           dict(label="Combo", value="$3,450", key="sup", cue="@combo"),
                           dict(label="Elevator", value="$8,650", key="sup", cue="@An elevator machine")], source="VMFS USA")),
    ftg("Then there's the deal with the location", "c08-office-break-room.mp4", 1.0),
    dict(at="Busy places know", kind="GF", clip="c02-transit-station.mp4", **{"in": 4.0},                             # T1
         scene=sc("num", at="@five to 20%", text="5–20%", label="of gross sales", y=380)),
    B("Sales per machine depend", ("c02-hospital-corridor.mp4", 2.0),                                                # T12
      sc("bars", kicker="Sales per machine, per month", max=2600, items=[
          dict(label="Typical site", from_=150, value=700, text="$150–700", key="sup", cue="@a typical site"),
          dict(label="Strong site", value=1500, text="up to $1,500", key="sup", cue="@a strong one"),
          dict(label="Hospitals, factories, transit hubs", value=2000, text="$2,000+", key="sup", cue="@Top spots")], source="VMFS USA")),

    # ---------------------------------------------------------------- 3 · Following the two dollars
    ftg("Those are sales figures", "n-can-opening.mp4", 0.5),
    B("Here's how one equipment supplier", ("c03-receipt.mp4", 5.0),                                                 # T11
      sc("receipt", title="One $2 soda", lines=[dict(label="Price", value="$2.00", cue=0), dict(label="Sales tax", value="6%", cue="@6%"),
                                                dict(label="Location's cut", value="10%", cue="@10%"), dict(label="Paid by card", value="Most", cue="@paying by card")],
         source="VMFS USA, 2026")),
    B("First, about 11 cents", ("c01-bottling-line.mp4", 3.0),                                                       # T9 + T7
      split(["@11 cents", "@94 cents", "@Card processing", "@four more", "@The building takes", "@That leaves"],
            amounts=True, wholeAt=0, splitAt=0, y=390,
            tally=dict(label="Operator keeps", at=0, steps=[
                dict(cents=11, cue="@11 cents"), dict(cents=94, cue="@94 cents"), dict(cents=9, cue="@nine cents"),
                dict(cents=4, cue="@four more"), dict(cents=20, cue="@20 cents")]), source=SRC_VMFS)),
    B("before paying for gas", ("c01-bottling-line.mp4", 3.0),
      split([0, 0, 0, 0, 0, 0], amounts=True, labels=False, wholeAt=0, splitAt=0, y=390,
            costs=[dict(label="Gas", cue="@gas"), dict(label="Labor", cue="@labor"), dict(label="Repairs", cue="@repairs"),
                   dict(label="Insurance", cue="@insurance"), dict(label="Income tax", cue="@income tax")])),
    ftg("Every restock means driving out", "c03-highway-driving.mp4", 2.0),
    ftg("Those costs come out", "c03-gas-pump-gallons.mp4", 20.0),
    B("Run the full numbers", ("c02-driver-paperwork.mp4", 6.0),                                                     # T11
      sc("receipt", title="One machine, one month", lines=[dict(label="Sales", value="$900", cue="@$900")],
         total=dict(label="Operator keeps", value="$197", cue="@keeps about"),
         note=dict(text="About 22%, before paying themselves", cue="@22 %"), source=SRC_VMFS)),
    dict(at="And the better the location", kind="D",                                                                  # T8
         scene=dict(type="doc", params=dict(header="Riverside Community College District vending agreement, 2022",
                    html='(5) Commission Proposal - The Vendor guarantees commission of <span class="hl" data-cue="@33%">33% on gross sales</span>, and a signing bonus in the amount of $5,000 ...'))),
    B("and that airport from the start", ("n-airport-low-angle.mp4", 2.0),                                           # T12
      sc("bars", kicker="The location's cut", max=70, items=[
          dict(label="Typical", value=10, text="10%", key="loc", cue=0),
          dict(label="Riverside", value=33, text="33%", key="loc", cue=0.4),
          dict(label="That airport", locked=True, cue="@its deal is bigger")])),

    # ---------------------------------------------------------------- 4 · Card payments
    ftg("Card payments do help", "c04-card-tap-terminal.mp4", 1.0),
    B("people paying by card or phone", ("c01-card-reader-tap.mp4", 2.0),                                            # T14
      sc("versus", a=dict(label="Card or phone", value="$2.45", sub="average purchase", cue="@$2.45"),
         b=dict(label="Cash", value="$1.57", sub="average purchase", cue="@$1.57"), source=SRC_CANT)),
    B("and 78%", ("n-phone-tap-kiosk.mp4", 3.0),                                                                      # T22
      sc("ring", pct=78, at=0, label="of vending sales on that network were cashless", source=SRC_CANT)),
    B("So the operator ends up", ("n-drinks-machine-night.mp4", 2.0),                                                # T17
      sc("columns", items=[dict(label="Location", key="loc", cue="@three kinds"), dict(label="Scale", key="sup", cue="@three kinds+0.5"),
                           dict(label="Payments", key="pay", cue="@three kinds+1")], size=150)),

    # ---------------------------------------------------------------- 5 · Winner 1: the location
    ftg("Winner number one", "n-airport-busy-wide.mp4", 0.0),
    dict(at="That airport is Los Angeles", kind="GF", clip="c05-lax-theme-building-day.mp4", **{"in": 2.0}, blur=LAX_DAY_BLUR,   # T37
         scene=sc("tag", at=0.3, title="Los Angeles International Airport", sub="California", color="#0B1422", y=90)),
    dict(at="In 2023, its board", kind="D",                                                                           # T8
         scene=dict(type="doc", params=dict(header="LA Board of Airport Commissioners, Feb 16, 2023",
                    html='Pursuant to the terms of the proposed concession agreement, First Class will pay LAWA the greater of a minimum monthly guarantee of <span class="hl" data-cue="@$100">$100 per machine</span> or <span class="hl" data-cue="@59.5%">59.5 percent of gross sales</span> over the five-year term and any approved options.'))),
    B("Even the runner-up bid", ("c05-contract-signing.mp4", 3.0),                                                   # T19
      sc("ranked", kicker="LAX vending bids", items=[dict(name="First Class Vending", value="59.5%", cue=0),
                                                     dict(name="Canteen", value="51.6%", cue="@Canteen"),
                                                     dict(name="Gilly Vending", value="42.0%", cue="@Canteen+0.6")], source="LAX board report, 2023")),
    ftg("The operator runs and maintains", "c02-repair-closeup.mp4", 2.0),
    ftg("The airport just collects", "06-airport-terminal-4k.mp4", 1.0),

    # ---------------------------------------------------------------- 6 · Winner 2: scale
    ftg("Winner number two", "c06-trucks-docks-aerial.mp4", 2.0),
    B("Driving between machines", ("c06-downtown-traffic-aerial.mp4", 2.0),                                          # T18
      sc("density", a=dict(label="100 machines, one area", cue="@100 machines"), b=dict(label="10 machines, a whole city", cue="@10 machines"))),
    ftg("Big operators also buy", "c06-warehouse-drink-racks.mp4", 2.0),
    B("The biggest of them all", ("c12-office-tower.mp4", 2.0),                                                       # T16
      sc("company", at="@Canteen", name="Canteen", lines=[dict(text="Owned by Compass Group", cue="@Compass Group")])),
    dict(at="It started in Chicago", kind="GF", clip="c06-archival-1933-street.mp4", **{"in": 2.0},                   # T1 on archive film
         scene=sc("num", at="@1929", text="1929", kicker="Chicago", label="5¢ candy bar machines", labelAt="@five", y=300)),
    B("Today, Compass Group describes", ("c01-office-lobby.mp4", 8.0),                                                # T24
      sc("quote", at=0.3, size=110, text="The largest unattended retail provider in the United States.", name="Compass Group, on Canteen", nameDy=290)),
    B("And the big players keep getting bigger", ("c06-warehouse-drink-racks.mp4", 12.0),                            # T23
      sc("clipping", at=0, date="2025", place="Alabama", headline="Buffalo Rock sells its vending business to Canteen",
         body='Almost <span class="hl" data-cue="@700">700 micro markets</span> and more than <span class="hl" data-cue="@7,600">7,600 vending locations</span>.', headSize=80, w=1200, x=360)),

    # ---------------------------------------------------------------- 7 · Winner 3: payments
    ftg("The third winner", "n-card-terminal.mp4", 2.2),
    ftg("Every tap sends", "c08-card-tap-unlock.mp4", 0.5),
    dict(at="Cantaloupe, one of the biggest", kind="GF", clips=[("c01-server-room.mp4", 0, 7), ("n-data-center.mp4", 1, None)],   # T1
         scene=sc("num", y=110, size=200, items=[dict(at="@600,000", text="600,000+", kicker="Connected machines and kiosks"),
                                                 dict(at="@$4.6 billion", text="$4.6B", kicker="Sales they handled, 2025")])),
    ftg("Cantaloupe earns a cut", "n-contactless-machine.mp4", 0.0),
    ftg("And Cantaloupe itself just changed hands", "c10-handshake-warehouse.mp4", 1.0),
    B("In May", ("c05-boardroom-wide.mp4", 4.0),                                   # T23
      sc("clipping", at=0, date="May 2026", place="", headline="365 Retail Markets completes its purchase of Cantaloupe",
         body='About <span class="hl" data-cue="@$848 million">$848 million</span>, cleared after it agreed to <span class="hl" data-cue="@sell off">sell a competing kiosk business</span>.', headSize=80, w=1200, x=360)),

    # ---------------------------------------------------------------- 8 · Micro markets
    ftg("But some of the biggest changes", "c09-busy-office.mp4", 4.0),
    ftg("A micro market is an unlocked", "c08-grab-and-go-cooler.mp4", 2.0),
    ftg("and a self-checkout kiosk", "c08-self-checkout-scan.mp4", 2.0),
    B("In 2025, the average vending purchase", ("c08-kiosk-touchscreen.mp4", 2.0),                                   # T12
      sc("bars", kicker="Average purchase, 2025", max=5.6, items=[
          dict(label="Vending machine", value=2.01, text="$2.01", key="tax", cue="@$2.01"),
          dict(label="Micro market", value=3.02, text="$3.02", key="sup", cue="@$3.02"),
          dict(label="Smart store", value=4.49, text="$4.49", key="pay", cue="@$4.49")], source=SRC_CANT)),
    dict(at="Micro markets on that network", kind="GF", clip="n-self-service-kiosks.mp4", **{"in": 0.0},              # T1
         scene=sc("num", at="@billion", text="$1B+", label="micro market sales, up 13%", labelAt="@13%", y=110)),
    B("Smart stores grew from", ("n-touchscreen-snack-machine.mp4", 3.0),                                                      # T20
      sc("growth", kicker="Smart stores on Cantaloupe's network", a=dict(value="71", sub="locations", cue="@71"), b=dict(value="572", sub="a year later", cue="@572"))),
    dict(at="Though together", kind="GF", clip="n-self-checkout-kiosk.mp4", **{"in": 2.0},                                 # T1
         scene=sc("num", at="@$6 million", text="$6M", label="smart store sales, 2025", y=110)),
    B("Vending machines still bring in", ("c02-combo-machine.mp4", 3.0),                                             # T12
      sc("bars", kicker="Total sales on that network, 2025", max=3.9, items=[
          dict(label="Vending machines", value=3.3, text="$3.3B", key="tax", cue="@$3.3 billion"),
          dict(label="Micro markets", value=1.0, text="$1B+", key="sup", cue="@$3.3 billion+0.5"),
          dict(label="Smart stores", value=0.006, text="$6M", key="pay", cue="@$3.3 billion+1")], source=SRC_CANT)),

    # ---------------------------------------------------------------- 9 · A beginner's first six months
    ftg("But the passive income videos", "c09-laptop-night.mp4", 2.0),
    B("They posted their numbers", ("c09-laptop-night.mp4", 6.0),                                                     # T11
      sc("receipt", title="Getting started", lines=[dict(label="Two refurbished machines", value="$3,200", cue="@$3,200"),
                                                    dict(label="Snacks and drinks", value="$400", cue="@400 on snacks")], source="a beginner's post on Reddit")),
    ftg("One machine sits in an office", "n-office-50-staff.mp4", 0.0),
    ftg("The other is in an auto repair shop", "c09-mechanic-under-lift.mp4", 1.0),
    B("The office machine brings in", ("c09-auto-repair-shop.mp4", 2.0),                                              # T11
      sc("receipt", title="Each month", lines=[dict(label="Office machine", value="$280–350", cue=0),
                                               dict(label="Repair shop", value="$120–180", cue="@The repair shop")],
         total=dict(label="Kept", value="$130–150", cue="@they say they keep"), note=dict(text="after gas, restocking and repairs", cue="@they say they keep"))),
    ftg("We can't check those numbers", "c09-auto-repair-shop.mp4", 4.0),
    B("Their verdict was simple", ("c09-restock-drive-suburb.mp4", 11.0),                                             # T24
      sc("quote", at="@It's not as passive", size=120, text="It's not as passive as people make it sound.", name="A beginner operator", role="Reddit", nameDy=300)),
    B("Now do the math", ("c03-highway-driving.mp4", 5.0),                                                            # T1 on its own background
      sc("num", at="@nets about", text="$20–175", kicker="A typical site nets, per month", source="VMFS USA", y=330)),
    B("At that rate", ("c03-highway-driving.mp4", 5.0),                                                               # T41
      sc("months", total=168, fill=20, a=dict(value="20 months", sub="to pay off a $3,500 machine", cue="@20 months"),
         b=dict(value="14+ years", sub="at a weak site", cue="@14 years"))),
    dict(at="Things do break", kind="F", clips=[("c02-repair-closeup.mp4", 9, 2.4), ("c04-dollar-bill-acceptor.mp4", 0, None, {"until": 2.3})]),
    ftg("and an attempted break-in", "c09-security-camera.mp4", 2.0),
    ftg("Then there's debt", "c09-credit-card-overdue.mp4", 2.0),
    B("looked at one creator's breakdown", ("n-advisor-tablet.mp4", 3.0),                                             # T1 on its own background
      sc("num", at="@$3,330", text="$3,330", label="to start, in one creator's breakdown", y=330)),
    B("And his advice", ("c09-credit-card-overdue.mp4", 4.0),                                                         # T24
      sc("quote", at="@Save it in cash", size=130, text="Save it in cash.<br>Don't borrow it.", name="George Kamel", role="Personal finance host", nameDy=320)),
    ftg("Put it on a card", "n-card-into-reader.mp4", 0.5),

    # ---------------------------------------------------------------- 10 · Buying a route
    dict(at="If you'd rather buy a route", kind="F", clips=[("c10-financial-docs-review.mp4", 0.2, 5), ("n-docs-review-senior.mp4", 1, None)]),
    B("BizBuy sells figures", ("c10-spreadsheet-monitor.mp4", 3.0),                                                   # T21
      sc("equation", kicker="Vending businesses sold, 2021–2025", ops=["≈"],
         terms=[dict(value="$83,500", sub="typical sale price", cue="@$83,500"), dict(value="2×", sub="a year's earnings", cue="@two times", hl=True)], source="BizBuySell")),
    dict(at="One Chicago area route", kind="G",                                                                       # T4
         scene=sc("routeMap", img=("c10-arlington-heights-aerial.mp4", 4.0), at=0.4, drawDur=3.0,
                  label="One Chicago-area route, 12 machines", value="$138,000", valueAt="@$138", size=160,
                  pts=[[120, 560], [460, 520], [840, 590], [1120, 540], [1420, 650], [1640, 800], [1240, 880], [800, 920], [420, 870], [160, 780]])),
    B("The seller estimates", ("c10-arlington-heights-aerial.mp4", 4.0),                                              # T21
      sc("equation", ops=["÷", "≈"], terms=[dict(value="$138,000", sub="asking price", cue=0.2), dict(value="$49,000", sub="a year, seller's estimate", cue="@49,000"),
                                          dict(value="2.8×", sub="earnings", cue="@nearly three times", hl=True)], size=150, source="The Route Exchange")),
    ftg("Those are asking prices", "c10-calculator-ledger.mp4", 1.0),
    ftg("A careful buyer asks", "n-records-review-warehouse.mp4", 0.0),

    # ---------------------------------------------------------------- 11 · Operation Vend Up Broke
    ftg("And none of this is new", "c11-newsprint-listings.mp4", 5.0),
    B("In 1998, the Federal Trade Commission", ("c11-newsprint-listings.mp4", 8.0),                                  # T23
      sc("clipping", at=0, date="Sept. 3, 1998", place="Washington", headline="“Operation Vend Up Broke”", w=1200, x=360,
         body='The FTC and <span class="hl" data-cue="@10 states">10 states</span> announce <span class="hl" data-cue="@40 enforcement">40 enforcement actions</span> against sellers of vending business opportunities.')),
    dict(at="The FTC warned", kind="D",                                                                               # T8
         scene=dict(type="doc", params=dict(header="FTC press release, Sept 3, 1998", size=50,
                    html='"Every year, thousands of consumers literally end up broke after investing in purportedly lucrative vending opportunities." … <span class="hl" data-cue="@fake references">"You can\'t rely on supposedly satisfied consumers supplied by the seller."</span>'))),
    ftg("The ads have moved", "n-phone-social-feed.mp4", 2.0),
    dict(at="and the math behind them", kind="D",
         scene=dict(type="doc", params=dict(header="Trustpilot review of a vending locator", size=56, y=300,
                    html='"He provided me with <span class="hl" data-cue="0">\'leads\', not actual locations.</span>"'))),

    # ---------------------------------------------------------------- 12 · Who really wins
    B("Back to your $2", ("c12-vending-closeup.mp4", 6.0),                                                            # T9 recap + T7
      split([0, 0, 0, 0, 0, 0], amounts=True, wholeAt=0, splitAt=0, y=390,
            tally=dict(label="Operator keeps", at=0, steps=[dict(cents=138, cue=0)]))),
    B("The people who win", ("c05-traveler-vending-snack.mp4", 3.0),                                                 # T17
      sc("columns", items=[dict(label="Location", key="loc", cue="@the location"), dict(label="Scale", key="sup", cue="@the scale"),
                           dict(label="Technology", key="pay", cue="@the technology")])),
    ftg("So if you're ever looking", "c10-checking-sales-records.mp4", 4.0),
    dict(at="Would you still buy one", kind="GF", clip="c02-office-vending.mp4", **{"in": 12.0},                       # T1
         scene=sc("num", at=0.3, text="Would you still<br>buy one?", size=110, y=110)),
    ftg("Next time, the car wash", "c12-car-wash-tunnel.mp4", 2.0),
    dict(at="Subscribe so you don't miss it", kind="G", scene=dict(type="end", opaque=True, params=dict(logo=LOGO, y=300))),
]

END_TAIL = 20.0  # seconds of end screen after the last word
