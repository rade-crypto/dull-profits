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
    dict(key="own", cents=62, inside="Operator?"),
]


def split(names_cues, amounts=False, labels=True, owner=None, relabel=None, **kw):
    sl = []
    for i, (s, cue) in enumerate(zip(SPLIT, names_cues)):
        d = dict(s, cue=cue, **((relabel or {}).get(i, {})))
        if not labels:
            d.pop("label", None)
        if not amounts:
            d.pop("amount", None)
        elif s["key"] == "own":
            d["inside"] = owner or "Operator 62¢"
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

import json
EP = Path(__file__).resolve().parent
USMAP = json.load(open(EP.parents[1] / "docs" / "templates" / "usmap.json"))
ROUTE_CLIP, ROUTE_IN = "c10-arlington-heights-aerial.mp4", 9.24       # aerial visible from 13.5 s (under the map before that)
ROUTE_TRACK = json.load(open(EP / "tracks" / "route15.json"))          # tools/video/track.py, ref frame at 15.4 s
ROUTE_PINS = [[327, 573], [533, 565], [767, 433], [1080, 547], [1333, 507], [1080, 673], [640, 687], [380, 653]]  # houses, in the ref frame
ROUTE2_CLIP, ROUTE2_IN = "c10-arlington-heights-aerial.mp4", 3.0
ROUTE2_TRACK = json.load(open(EP / "tracks" / "route81.json"))
ROUTE2_PINS = ROUTE2_TRACK["pins"]
P1 = ("n-drinks-machine-night.mp4", 0.5)   # a stocked machine (swap for a lit office machine once downloaded)
P3 = ("c04-coin-into-slot.mp4", 1.0)            # the cash
C1 = ("c01-office-lobby.mp4", 2.0, "#0B1422")              # food service at work
R1 = ("px-unloading-boxes-truck.mp4", 2.0)       # restocking: a route driver carrying cases from the van
R2 = ("n-cash-box-pull.mp4", 6.0)              # pulling cash: the cash box comes out of the machine
R3 = ("n-wrench-inside-machine.mp4", 2.0)       # fixing: a wrench inside the machine


import sys as _sys
_sys.path.insert(0, str(EP.parents[1] / "tools" / "video"))
from timing import Timeline as _TL
CUT1 = round(_TL(EP / "voiceover" / "timings-clean.json").at("and a soda drops"), 3)   # where the second opening clip starts


def B(at, bg, scene, **kw):
    """A graphic on its own background image: bg=(clip, seconds) becomes a blurred, darkened, slowly drifting still."""
    return dict(at=at, kind="B", bg=bg, scene=scene, **kw)


def sc(type, **params):
    return dict(type=type, params=params)


# Templates are numbered as in docs/templates (template sheets). Footage-only shots have nothing on top.
SHOTS = [
    # ---------------------------------------------------------------- 1 · Hook
    # one video file for both opening clips, joined by a hard cut on "and a soda drops" (no player switch 1.2 s in)
    dict(at=None, kind="F", clips=[("01-phone-pay-vending.mp4", 1.0, CUT1), ("c12-vending-closeup.mp4", 4.0, None, {"cut": True})]),
    B("$2", [("prev", 0, 4.3), ("n-coins-office-vending.mp4", 1.0)],                                               # T9 The Split
      split(["@government", "@drink company", "@card processor", "@software company", "@the building", None],
            title="$2.00", titleAt=0, wholeAt="@Before the owner", splitAt="@five other players")),
    ftg("At one of the busiest airports", "c05-lax-plane-landing-sunset.mp4", 4.0),
    dict(at="the building takes", kind="GF", clip="c05-lax-dusk-overview.mp4", **{"in": 3.0}, zoom=(1.3, 0, 0), push=0.06,   # T1
         scene=sc("num", at="@59.5%", count=[0, 59.5], fmt="pct1", label="of every sale goes to the building", y=110)),
    ftg("Online, vending machines", "c11-phone-night-viewer.mp4", 2.0),
    # Fix A: how it's pitched, over the things it describes. No strike-through: the verdict comes later, from evidence.
    dict(at="as easy passive income", kind="GF", clip=P1[0], **{"in": P1[1]},                                          # T15c
         scene=sc("claim", x=1804, align="right", y=590, size=100, items=[
             dict(html="Easy<br>[passive income]", at="@easy"),
             dict(html="Stock it<br>[once a week]", at="@Stock a machine"),
             dict(html="Let the cash<br>[pile up]", at="@let the cash")])),
    B("So we check the real numbers+0.5", ("c10-checking-sales-records.mp4", 2.0),                                       # T8 papers
      sc("papers", items=[dict(title="Payment data", sub="Cantaloupe, 2025", cue="@payment data"),
                          dict(title="Public contracts", sub="LAX board, 2023", cue="@public contracts"),
                          dict(title="Operators' own results", sub="Posted online", cue="@operators")])),
    ftg("The picture is a lot less exciting", "c03-hand-truck.mp4", 8.0),
    ftg("and it shows where the money", "px-counting-money-office.mp4", 18.0),
    ftg("So let's follow the $2", "c12-coins-in-hand.mp4", 4.0),

    # ---------------------------------------------------------------- 2 · Who owns the machine
    ftg("These machines usually belong", "n-vans-depot-aerial.mp4", 0.0),   # an operator's fleet
    ftg("places them in other people's buildings", "c02-office-vending.mp4", 3.0),
    # Fix B: the same clip keeps playing and the lens racks soft; the van aerial takes over on "more than"
    B("In 2025, US vending operators", [("prev", 0, 3.9), ("c02-van-aerial-road.mp4", 1.0)],                         # T1
      sc("num", x=116, y=420, size=200, items=[dict(at="@$7 billion", text="$7 billion", kicker="US vending operators' sales, 2025", kickerAt="@US vending",
                                                    pre="More than", preAt="@more than", source="IBISWorld", sourceAt="@according to")])),
    # Fix C: the giants over food service at work, then the map of small operators
    B("The biggest names are food service giants", ("n-cafeteria-serving.mp4", 4.0),                                # T16
      sc("stack", x=116, y=150, size=150, gap=170, mask=True, kicker="Food service giants", kickerAt="@food service giants",
         lines=[dict(text="Compass Group", at="@Compass"), dict(text="Aramark", at="@Aramark")])),
    # Fix C + D: the map fills with dots, zooms through to one suburb and dissolves into the playing aerial; pins drop on
    # houses and the route loop draws, tracked to the ground
    dict(at="But most of the map+1.1", kind="GF", clip=ROUTE_CLIP, **{"in": ROUTE_IN},                                     # T33 + T4
         scene=sc("usmap", camera=False, states=USMAP["states"], dots=USMAP["dots"], chicago=USMAP["chicago"],
                  dotsAt=0.1, dotsSpread=2.2, label="Small, local businesses", labelAt="@small, local",
                  zoomAt="@Most of them are built-0.7", revealAt="@Most of them are built-0.2",
                  pins=ROUTE_PINS, pinsAt="@route", routeAt="@drives", routeDur=1.6, lap=4.0,
                  track=dict(t0=round(ROUTE_TRACK["from"] - ROUTE_IN, 3), H=ROUTE_TRACK["H"]))),
    ftg("restocking snacks", *R1),
    ftg("pulling cash", *R2),
    ftg("and fixing whatever broke", *R3),
    # Fix E: a machine on screen, then line drawings of the three kinds with their prices, counted on the word
    ftg("The machines aren't cheap", "n-street-vending-man.mp4", 3.0),
    B("One supplier sells", [("prev", 0, 5.3), ("n-office-coins-vending2.mp4", 2.0, 5.0), ("n-subway-vending-woman2.mp4", 1.0)],   # T26
      sc("machines", kicker="One supplier's prices", kickerAt="@One supplier", source="VMFS USA", sourceAt="@$1,900", lowerAt="@gently lowers",
         items=[dict(kind="counter", label="Countertop", value="$1,900", cue="@countertop", valueAt="@$1,900"),
                dict(kind="combo", label="Combo", value="$3,500", cue="@combo", valueAt="@$3,500"),
                dict(kind="elevator", label="Elevator", value="$8,650", cue="@An elevator machine", valueAt="@$8,650")])),
    ftg("Then there's the deal with the location", "n-phone-pay-office-machine.mp4", 0.0),
    dict(at="Busy places know", kind="GF", clip="c02-transit-station.mp4", **{"in": 4.0}, shade="right",                             # T1
         scene=sc("num", at="@five to 20%", text="5–20%", kicker="Share of gross sales", kickerAt="@share of gross", align="right", x=1804, y=70, source="VMFS USA", sourceAt="@five to 20%", sourceY=440)),
    ftg("Sales per machine depend+1.0", "n-office-coins-vending2.mp4", 8.0),
    B("The same supplier's guide", ("c09-busy-office.mp4", 12.0),                                                    # T12
      sc("bars", kicker="Sales per machine, per month", kickerAt=0.2, max=2600, items=[
          dict(label="Typical site", from_=150, value=700, text="$150–700", key="sup", cue="@a typical site", valueAt="@$150"),
          dict(label="Strong site", value=1500, text="up to $1,500", key="sup", cue="@a strong one"),
          dict(label="Hospitals, factories, transit hubs", value=2000, text="$2,000+", key="sup", cue="@$2,000")], source="VMFS USA")),
    dict(at="Top spots like hospitals", kind="F", clips=[("c02-hospital-corridor.mp4", 2.0, 1.7), ("c02-factory-floor.mp4", 1.0, 1.1, {"cut": True}),
                                                        ("c05-traveler-vending-snack.mp4", 1.0, None, {"cut": True})]),
    B("can do $2,000", "prev",
      sc("bars", kicker="Sales per machine, per month", max=2600, items=[
          dict(label="Typical site", from_=150, value=700, text="$150–700", key="sup", cue=0),
          dict(label="Strong site", value=1500, text="up to $1,500", key="sup", cue=0),
          dict(label="Hospitals, factories, transit hubs", value=2000, text="$2,000+", key="sup", cue="@$2,000")], source="VMFS USA"), carry=True),

    # ---------------------------------------------------------------- 3 · Following the two dollars
    ftg("Those are sales figures+1.2", "n-can-opening.mp4", 0.5, push=0.05),
    B("Here's how one equipment supplier", ("c03-receipt.mp4", 5.0),                                                 # T11
      sc("receipt", title="One $2 soda", lines=[dict(label="Price", value="$2.00", cue=0), dict(label="Sales tax", value="6%", cue="@6%"),
                                                dict(label="Location's cut", value="10%", cue="@10%"), dict(label="Paid by card", value="Most", cue="@paying by card")],
         source="VMFS USA, 2026")),
    B("First, about 11 cents+0.8", [("c01-state-capitol.mp4", 2.0, 3.0), ("c01-bottling-line.mp4", 2.0)],              # T9 + T7, sandwiched
      split(["@11 cents", 99, 99, 99, 99, 99], amounts=True, owner="Operator?", wholeAt=0, splitAt=0, y=390, source=SRC_VMFS,
            tally=dict(label="Operator keeps", at=0, steps=[dict(cents=11, cue="@11 cents")]))),
    ftg("The biggest slice is the product", "c01-bottling-line.mp4", 4.6),
    B("Roughly half the pre-tax price", [("c03-cans-conveyor.mp4", 0.0, 2.6), ("n-can-opening.mp4", 6.4)],
      split([0, "@94 cents", 99, 99, 99, 99], amounts=True, owner="Operator?", wholeAt=0, splitAt=0, y=390, source=SRC_VMFS,
            tally=dict(label="Operator keeps", at=0, steps=[dict(cents=11, cue=0), dict(cents=94, cue="@94 cents")])), carry=True),
    ftg("Then the tech companies take theirs", "n-card-terminal.mp4", 6.0),
    B("Card processing costs", "prev",
      split([0, 0, "@nine cents", "@four more", 99, 99], amounts=True, owner="Operator?", wholeAt=0, splitAt=0, y=390, source=SRC_VMFS,
            tally=dict(label="Operator keeps", at=0, steps=[dict(cents=11, cue=0), dict(cents=94, cue=0), dict(cents=9, cue="@nine cents"),
                                                            dict(cents=4, cue="@four more")])), carry=True),
    ftg("The building takes its 10%+1.0", "c01-office-lobby.mp4", 21.0),
    B("That's 20 cents", "prev",
      split([0, 0, 0, 0, "@20 cents", "@That leaves"], amounts=True, wholeAt=0, splitAt=0, y=390, source=SRC_VMFS,
            tally=dict(label="Operator keeps", at=0, steps=[dict(cents=11, cue=0), dict(cents=94, cue=0), dict(cents=9, cue=0),
                                                            dict(cents=4, cue=0), dict(cents=20, cue="@20 cents")])), carry=True),
    B("before paying for gas", [("prev", 0, 2.4), ("px-truck-full-boxes.mp4", 0.0)],
      split([0, 0, 0, 0, 0, 0], amounts=True, wholeAt=0, splitAt=0, y=390, source=SRC_VMFS,
            tally=dict(label="Operator keeps", at=0, steps=[dict(cents=138, cue=0)]), costsDy=150, costsGap=54,
            costs=[dict(label="Gas", cue="@gas"), dict(label="Labor", cue="@labor"), dict(label="Repairs", cue="@repairs"),
                   dict(label="Insurance", cue="@insurance"), dict(label="Income tax", cue="@income tax")]), carry=True),
    ftg("Every restock means driving out+0.8", "c03-highway-driving.mp4", 2.0),
    ftg("Those costs come out", "c03-gas-pump-gallons.mp4", 20.0),
    B("Run the full numbers", ("c02-driver-paperwork.mp4", 2.0),                                                     # T11
      sc("receipt", title="One machine, one month", lines=[dict(label="Sales", value="$900", cue="@$900")],
         total=dict(label="Operator keeps", value="$197", cue="@keeps about"),
         note=dict(text="About 22%, before paying themselves", cue="@22 %"), source=SRC_VMFS, w=1040)),
    ftg("and it's before the operator pays", "c02-driver-paperwork.mp4", 15.4),
    ftg("And the better the location", "px-college-hallway.mp4", 1.0),
    dict(at="Some public contracts", kind="D", bg=[("prev", 0, 5.0), ("px-students-hallway-4k.mp4", 2.0)], soft=14.0, dim=0.42,                                                                  # T8
         scene=dict(type="doc", params=dict(header="Riverside Community College District vending agreement, 2022",
                    html='(5) Commission Proposal - The Vendor guarantees commission of <span class="hl" data-cue="@33%">33% on gross sales</span>, and a signing bonus in the amount of $5,000 ...'))),
    B("and that airport from the start", ("n-airport-low-angle.mp4", 0.8),                                           # T12
      sc("bars", kicker="The location's cut", max=70, items=[
          dict(label="Typical", value=10, text="10%", key="loc", cue=0),
          dict(label="Riverside", value=33, text="33%", key="loc", cue=0.4),
          dict(label="That airport", locked=True, cue="@its deal is bigger")], source="VMFS USA; Riverside CCD, 2022")),

    # ---------------------------------------------------------------- 4 · Card payments
    ftg("Card payments do help", "c04-card-tap-terminal.mp4", 1.0),
    B("people paying by card or phone", [("c01-card-reader-tap.mp4", 1.5, 7.6), ("c04-coin-into-slot.mp4", 0.5)],                                            # T14
      sc("versus", a=dict(label="Card or phone", value="$2.45", sub="average purchase", cue="@$2.45"),
         b=dict(label="Cash", value="$1.57", sub="average purchase", cue="@$1.57"), source=SRC_CANT)),
    B("and 78%", ("n-phone-tap-kiosk.mp4", 3.0),                                                                      # T22
      sc("ring", pct=78, at=0, label="of vending sales on that network were cashless", source=SRC_CANT)),
    ftg("So the operator ends up", "n-drinks-machine-night.mp4", 0.3),
    B("The bigger money in vending", [("prev", 0, 3.0), ("n-airport-busy-wide.mp4", 2.6)],                                                # T17
      sc("claim", x=116, y=300, size=110, items=[dict(html="Three kinds<br>of [players]", at="@three kinds")])),

    # ---------------------------------------------------------------- 5 · Winner 1: the location
    dict(at="Winner number one", kind="GF", clip="n-airport-busy-wide.mp4", **{"in": 0.0}, shade="left", scene=sc("tag", at="@the location", lead="1", leadAt="@number one", title="Location", rule="var(--loc)", size=72)),
    dict(at="That airport is Los Angeles+0.8", kind="GF", clip="c05-lax-theme-building-day.mp4", **{"in": 2.0}, shade="left", zoom=(1.45, 0, 0),   # T37
         scene=sc("tag", at=0.3, title="Los Angeles<br>International Airport", sub="California", y=90)),
    ftg("In 2023, its board+1.0", "c05-contract-signing.mp4", 3.0),
    dict(at="where the operator pays", kind="D", bg=[("prev", 0, 4.6), ("c05-lax-theme-building-day.mp4", 7.0)], soft=14.0, dim=0.42,                                                                           # T8
         scene=dict(type="doc", params=dict(header="LA Board of Airport Commissioners, Feb 16, 2023",
                    html='Pursuant to the terms of the proposed concession agreement, First Class will pay LAWA the greater of a minimum monthly guarantee of <span class="hl" data-cue="@$100">$100 per machine</span> or <span class="hl" data-cue="@59.5%">59.5 percent of gross sales</span> over the five-year term and any approved options.'))),
    B("Even the runner-up bid", ("c05-lax-dusk-overview.mp4", 10.0),                                                   # T19
      sc("ranked", kicker="LAX vending bids", items=[dict(name="First Class Vending", value="59.5%", cue=0),
                                                     dict(name="Canteen", value="51.6%", cue="@Canteen"),
                                                     ], source="LAX board report, 2023")),
    ftg("The operator runs and maintains", "n-tech-opens-panel.mp4", 2.0),
    ftg("The airport just collects", "n-airport-keypad-vending.mp4", 0.0),

    # ---------------------------------------------------------------- 6 · Winner 2: scale
    dict(at="Winner number two", kind="GF", clip="c06-trucks-docks-aerial.mp4", **{"in": 2.0}, shade="left", scene=sc("tag", at="@scale", lead="2", leadAt="@number two", title="Scale", rule="var(--sup)", size=72)),
    ftg("Driving between machines+1.4", "c06-downtown-traffic-aerial.mp4", 0.2),
    B("so an operator with 100 machines", "prev",                                          # T18
      sc("density", a=dict(label="100 machines, one area", cue="@100 machines"), b=dict(label="10 machines, a whole city", cue="@10 machines"))),
    ftg("Big operators also buy", "c06-warehouse-drink-racks.mp4", 2.0),
    B("The biggest of them all", ("c12-office-tower.mp4", 0.0),                                                       # T16
      sc("company", at="@Canteen", name="Canteen", lines=[dict(text="Owned by Compass Group", cue="@owned by")])),
    dict(at="It started in Chicago", kind="GF", clip="c06-archival-1933-street.mp4", **{"in": 2.0},                   # T1 on archive film
         scene=sc("num", at="@1929", text="1929", kicker="Chicago", label="5¢ candy bar machines", labelAt="@five", y=300)),
    B("Today, Compass Group describes+0.5", ("c01-office-lobby.mp4", 8.0),                                                # T24
      sc("quote", at=0.3, size=110, text="The largest unattended retail provider in the United States.”", span="@@the largest unattended retail provider in the United States",
         name="Compass Group, on Canteen", nameDy=290, nameAt="@a label that covers"), dim=0.42),
    B("And the big players keep getting bigger", [("n-inventory-check.mp4", 0.0, 8.0), ("n-vans-depot-aerial.mp4", 5.0)],   # T23
      sc("clipping", at="@In 2025", date="2025", place="Alabama", headline="Buffalo Rock sells its vending business to Canteen",
         body='Almost <span class="hl" data-cue="@700">700 micro markets</span> and more than <span class="hl" data-cue="@7,600">7,600 vending locations</span>.', headSize=80, w=1200, x=360)),

    # ---------------------------------------------------------------- 7 · Winner 3: payments
    dict(at="The third winner", kind="GF", clip="n-card-terminal.mp4", **{"in": 2.2}, shade="left", scene=sc("tag", at="@payments", lead="3", leadAt="@third winner", title="Payments", rule="var(--pay)", size=72)),
    ftg("Every tap sends+1.3", "px-payment-terminal.mp4", 1.0),
    dict(at="Cantaloupe, one of the biggest", kind="GF", clips=[("c01-server-room.mp4", 0, 7), ("n-data-center.mp4", 1, None)], push=0.06,   # T1
         scene=sc("num", y=330, size=200, items=[dict(at="@600,000", text="600,000", pre="More than", preAt="@more than", kicker="Connected machines and kiosks"),
                                                 dict(at="@$4.6 billion", text="$4.6 billion", kicker="Sales they handled, 2025", source=SRC_CANT)])),
    ftg("Cantaloupe earns a cut", "px-paying-groceries-card.mp4", 0.0),
    ftg("And Cantaloupe itself just changed hands", "c10-handshake-warehouse.mp4", 1.0),
    B("In May", ("c05-boardroom-wide.mp4", 2.0),                                   # T23
      sc("clipping", at=0, date="May 2026", place="", headline="365 Retail Markets completes its purchase of Cantaloupe",
         body='About <span class="hl" data-cue="@$848 million">$848 million</span>, cleared after it agreed to <span class="hl" data-cue="99">sell a competing kiosk business</span>.', headSize=80, w=1200, x=360)),
    ftg("Regulators only let the deal through", "c11-penn-ave-capitol-dusk.mp4", 13.0),
    B("after the company agreed", "prev",
      sc("clipping", at=0, date="May 2026", place="", headline="365 Retail Markets completes its purchase of Cantaloupe",
         body='About <span class="hl" data-cue="0">$848 million</span>, cleared after it agreed to <span class="hl" data-cue="@sell off">sell a competing kiosk business</span>.', headSize=80, w=1200, x=360), carry=True),

    # ---------------------------------------------------------------- 8 · Micro markets
    ftg("But some of the biggest changes", "px-office-corridor.mp4", 0.0),
    ftg("A micro market is an unlocked", "c02-restocking-shelf-proxy.mp4", 2.0),
    ftg("and a self-checkout kiosk", "c08-self-checkout-scan.mp4", 2.0),
    B("In 2025, the average vending purchase", [("c08-kiosk-touchscreen.mp4", 0.5, 5.4), ("n-coins-office-vending.mp4", 12.5)],                                   # T12
      sc("bars", kicker="Average purchase, 2025", max=5.6, items=[
          dict(label="Vending machine", value=2.01, text="$2.01", key="own", cue="@$2.01"),
          dict(label="Micro market", value=3.02, text="$3.02", key="own", cue="@$3.02")], source=SRC_CANT)),
    ftg("At smart stores", "n-touchscreen-dispenser.mp4", 0.0),
    B("it was $4.49", "prev",
      sc("bars", kicker="Average purchase, 2025", max=5.6, items=[
          dict(label="Vending machine", value=2.01, text="$2.01", key="own", cue=0),
          dict(label="Micro market", value=3.02, text="$3.02", key="own", cue=0),
          dict(label="Smart store", value=4.49, text="$4.49", key="own", cue="@$4.49")], source=SRC_CANT), carry=True),
    dict(at="Micro markets on that network", kind="GF", clip="n-self-service-kiosks.mp4", **{"in": 0.0},              # T1
         push=0.06, scene=sc("num", at="@billion", text="$1 billion", pre="More than", preAt="@more than", label="micro market sales, up 13%", labelAt="@billion", y=110, source=SRC_CANT)),
    B("Smart stores grew from", ("n-touchscreen-snack-machine.mp4", 1.5),                                                      # T20
      sc("growth", kicker="Smart stores on Cantaloupe's network", a=dict(value="71", sub="locations", cue="@71"), b=dict(value="572", sub="a year later", cue="@572"), source=SRC_CANT)),
    dict(at="Though together+0.8", kind="GF", clip="c08-kiosk-touchscreen.mp4", **{"in": 0.5},                                 # T1
         scene=sc("num", at="@$6 million", text="$6 million", label="smart store sales, 2025", y=200, size=180, source=SRC_CANT, sourceAt="@$6 million")),
    B("Vending machines still bring in+0.8", [("c02-combo-machine.mp4", 5.6, 6.0), ("c08-smart-cabinet.mp4", 0.5)],                                             # T12
      sc("bars", kicker="Total sales on that network, 2025", max=3.9, items=[
          dict(label="Vending machines", value=3.3, text="$3.3B", key="own", cue="@$3.3 billion"),
          dict(label="Micro markets", value=1.0, text="$1B+", key="own", cue="@$3.3 billion+0.5"),
          dict(label="Smart stores", value=0.006, text="$6M", key="own", cue="@$3.3 billion+1")], source=SRC_CANT)),

    # ---------------------------------------------------------------- 9 · A beginner's first six months
    ftg("But the passive income videos", "c09-laptop-night.mp4", 2.0),
    B("They posted their numbers", [("c09-laptop-night.mp4", 6.0, 4.2), ("c09-calculator-hands.mp4", 1.0)],                                                     # T11
      sc("receipt", title="Getting started", lines=[dict(label="Two refurbished machines", value="$3,200", cue="@$3,200"),
                                                    dict(label="Snacks and drinks", value="$400", cue="@400 on snacks")], source="a beginner's post on Reddit", x=110, at="@$3,200-0.3")),
    ftg("One machine sits in an office", "n-office-50-staff.mp4", 0.0),
    ftg("The other is in an auto repair shop", "c09-mechanic-under-lift.mp4", 1.0),
    B("The office machine brings in", [("c08-office-break-room.mp4", 1.0, 5.8), ("c09-auto-repair-shop.mp4", 0.0)],                                              # T11
      sc("receipt", title="Each month", source="a beginner's post on Reddit", lines=[dict(label="Office machine", value="$280–350", cue="@$280"),
                                               dict(label="Repair shop", value="$120–180", cue="@The repair shop")])),
    ftg("After gas, restocking and repairs", "c09-restock-drive-suburb.mp4", 8.0),
    B("they say they keep", "prev",
      sc("receipt", title="Each month", lines=[dict(label="Office machine", value="$280–350", cue=0),
                                               dict(label="Repair shop", value="$120–180", cue=0)],
         source="a beginner's post on Reddit", total=dict(label="Kept", value="$130–150", cue="@they say they keep"), note=dict(text="after gas, restocking and repairs", cue="@they say they keep")), carry=True),
    ftg("We can't check those numbers", "c03-receipt.mp4", 12.0),
    B("Their verdict was simple", ("c02-van-side-door-cases.mp4", 0.5),                                             # T24
      sc("quote", at="@It's not as passive", size=120, text="It's not as passive<br>as people make it sound.”", name="A beginner operator", role="Reddit", nameDy=300), dim=0.42),
    B("Now do the math", ("c10-chicago-suburbs-aerial.mp4", 40.0),                                                            # T1 on its own background
      sc("num", at="@nets about", text="$20–175", kicker="A typical site nets, per month", kickerAt="@One supplier", source="VMFS USA", y=330)),
    B("At that rate", [("n-office-coins-vending2.mp4", 14.0, 6.2), ("px-coins-into-jar.mp4", 0.0)],                                                               # T41
      sc("months", total=168, fill=20, kicker="Paying off a $3,500 combo machine", kickerAt="@a $3", a=dict(value="20 months", sub="to pay off a $3,500 machine", cue="@20 months"),
         b=dict(value="14+ years", sub="at a weak site", cue="@14 years")), dim=0.48),
    dict(at="Things do break", kind="F", clips=[("c02-repair-closeup.mp4", 9, 3.1), ("c04-dollar-bill-acceptor.mp4", 0, None, {"until": 2.3})]),
    ftg("and an attempted break-in", "c09-security-camera.mp4", 2.0),
    ftg("Then there's debt", "c09-credit-card-overdue.mp4", 1.6),   # ends before the paper whips away
    B("looked at one creator's breakdown", ("px-person-accounting.mp4", 1.0),                                             # T1 on its own background
      sc("num", at="@$3,330", text="$3,330", kicker="One creator's breakdown, to start", kickerAt="@one creator's", source="George Kamel, as reported by 24/7 Wall St.", sourceAt="@$3", y=330)),
    B("And his advice", ("c09-one-dollar-bill.mp4", 1.0),                                                         # T24
      sc("quote", at="@Save it in cash", size=130, text="Save it in cash.<br>Don't borrow it.”", name="George Kamel", role="As reported by 24/7 Wall St.", nameDy=320)),
    ftg("Put it on a card", "n-card-into-reader.mp4", 4.0),

    # ---------------------------------------------------------------- 10 · Buying a route
    dict(at="If you'd rather buy a route", kind="F", clips=[("c10-financial-docs-review.mp4", 0.2, 5), ("n-docs-review-senior.mp4", 1, None)]),
    B("BizBuy sells figures", [("c10-spreadsheet-monitor.mp4", 1.0, 10.8), ("c09-calculator-hands.mp4", 7.5)],                                                   # T21
      sc("equation", kicker="Vending businesses sold, 2021–2025", kickerAt="@vending businesses", ops=["≈"],
         terms=[dict(value="2×", sub="a year's earnings", cue="@two times", hl=True), dict(value="$83,500", sub="typical sale price", cue="@$83")], source="BizBuySell")),
    dict(at="One Chicago area route", kind="GF", clip=ROUTE2_CLIP, **{"in": ROUTE2_IN},                                   # T4 on the playing aerial
         scene=sc("usmap", camera=False, pins=ROUTE2_PINS, pinsAt=0.3, routeAt=0.9, routeDur=2.2, lap=5.0,
                  value="$138,000", valueAt="@$138", label="One Chicago-area route", labelAt=0.2, color="#0B1422", y=36, labelSize=48,
                  track=dict(t0=round(ROUTE2_TRACK["from"] - ROUTE2_IN, 3), H=ROUTE2_TRACK["H"]))),
    B("The seller estimates", "prev",                                              # T21
      sc("equation", ops=["÷", "≈"], terms=[dict(value="$138,000", sub="asking price", cue=0.2, still=True), dict(value="$49,000", sub="a year, seller's estimate", cue="@49,000"),
                                          dict(value="3×", sub="earnings", cue="@nearly three times", hl=True)], size=150, source="The Route Exchange")),
    ftg("Those are asking prices", "c10-calculator-ledger.mp4", 1.0),
    ftg("A careful buyer asks", "n-records-review-warehouse.mp4", 0.0),

    # ---------------------------------------------------------------- 11 · Operation Vend Up Broke
    B("And none of this is new", ("c11-fraud-highlighted.mp4", 0.3),                                  # T23
      sc("clipping", at="@In 1998", date="Sept. 3, 1998", place="Washington", headline="“Operation<br>Vend Up Broke”", w=1200, x=360,
         body='The FTC and <span class="hl" data-cue="@10 states">10 states</span> announce <span class="hl" data-cue="@40 enforcement">40 enforcement actions</span> against sellers of vending business opportunities.')),
    ftg("against companies selling", "c11-gavel-strike.mp4", 1.0),
    ftg("The pitch back then", "n-money-counter.mp4", 0.5),
    dict(at="The FTC warned", kind="D", bg=[("prev", 0, 3.0), ("c11-landline-dialing.mp4", 2.0)], soft=14.0, dim=0.42,                                                                               # T8
         scene=dict(type="doc", params=dict(header="FTC press release, Sept 3, 1998", size=50,
                    html='"Every year, thousands of consumers literally end up broke after investing in purportedly lucrative vending opportunities." … <span class="hl" data-cue="@fake references">"You can\'t rely on supposedly satisfied consumers supplied by the seller."</span>'))),
    ftg("The ads have moved", "n-phone-social-feed.mp4", 1.0),

    # ---------------------------------------------------------------- 12 · Who really wins
    B("Back to your $2", [("c02-office-vending.mp4", 9.5), ("c05-ohare-crowd-legs.mp4", 2.0)],                                                            # T9 recap + T7
      split([0, "@The supplier takes", "@payment companies", "@payment companies+0.3", "@The building takes", "@the operator keeps"],
            amounts=True, wholeAt=0, splitAt=0, y=390, source=SRC_VMFS,
            relabel={0: dict(label="Tax"), 1: dict(label="Supplier"), 2: dict(label="Payments", amount="13¢", row=-1), 3: dict(label=None, amount=None)},
            tally=dict(label="Operator keeps", at="@the operator keeps", steps=[dict(cents=138, cue="@the operator keeps")]))),
    ftg("if the location is good+1.2", "01-phone-pay-vending.mp4", 3.0),                                                   # callback: the opening machine
    B("The people who win", [("px-people-at-vending-machines.mp4", 0.0, 5.0), ("05-machines-night-4k.mp4", 0.0)],                                                 # T17
      sc("columns", items=[dict(label="Location", key="loc", cue="@the location"), dict(label="Scale", key="sup", cue="@the scale"),
                           dict(label="Technology", key="pay", cue="@the technology")])),
    ftg("So if you're ever looking", "c10-checking-sales-records.mp4", 3.2),
    dict(at="Would you still buy one", kind="GF", clip="n-man-buys-drink-night.mp4", **{"in": 0.0},                       # T1
         scene=sc("num", at=0.3, text="Would you still<br>buy one?", size=110, y=110)),
    dict(at="Next time, the car wash", kind="GF", clip="c12-car-wash-tunnel.mp4", **{"in": 2.0},                       # T50
         scene=sc("stack", x=116, y=150, size=150, mask=True, kicker="Next", kickerAt="@Next", lines=[dict(text="The car wash", at="@the car wash")])),
    B("Subscribe so you don't miss it", [("prev", 0, 12.0), ("n-coffee-vending-woman.mp4", 0.0)], dict(type="end", params=dict(logo=LOGO, y=110, see=True))),
]

END_TAIL = 18.0  # seconds of end screen after the last word
