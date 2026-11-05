"""Guide articles for the public site, one folder each at <app>/guides/<slug>/.

Blocks: a string is a paragraph, a list is a bullet list, ("table", header, rows) is a table.
Facts must match the apps. Scripture is cited by reference only, never quoted from memory.
HoloVault guides name no grading company or marketplace; Glipsy guides name no drug brand, give no
dose and make no medical claim.
"""

GUIDES = [
    {
        "app": "lampbible",
        "slug": "advent-reading-plan-2026",
        "date": "2026-11-05",
        "title": "Advent reading plan 2026: 25 chapters from Genesis to the manger",
        "description": ("A free 25-day Advent Bible reading plan for 1 to 25 December 2026, one chapter a day from "
                        "the first promise in Genesis to the birth of Jesus, with the Advent wreath candles for each Sunday."),
        "lead": ("Advent begins on Sunday 29 November 2026. This plan reads one chapter a day from 1 December to "
                 "Christmas Day, following God's promise of a Saviour from Genesis to Bethlehem. It takes about "
                 "five minutes a day."),
        "sections": [
            ("The Advent wreath in 2026", [
                "Many churches light one candle each Sunday of Advent and a fifth, the Christ candle, on Christmas Day. These are the dates this year, with a verse for each:",
                ("table", ["Date", "Candle", "Verse"], [
                    ["Sunday 29 November", "Hope", "Isaiah 9:2"],
                    ["Sunday 6 December", "Peace", "Luke 2:14"],
                    ["Sunday 13 December", "Joy (the rose candle)", "Luke 2:10"],
                    ["Sunday 20 December", "Love", "John 3:16"],
                    ["Friday 25 December", "Christ", "Luke 2:11"],
                ]),
            ]),
            ("The 25-day plan", [
                "One chapter a day. Days 1 to 14 trace the promise through the Old Testament; days 15 to 25 show how it was kept.",
                ("table", ["Day", "Date", "Chapter", "Day", "Date", "Chapter"], [
                    ["1", "1 Dec", "Genesis 3", "14", "14 Dec", "Malachi 3"],
                    ["2", "2 Dec", "Genesis 12", "15", "15 Dec", "Psalm 96"],
                    ["3", "3 Dec", "2 Samuel 7", "16", "16 Dec", "Galatians 4"],
                    ["4", "4 Dec", "Psalm 2", "17", "17 Dec", "Philippians 2"],
                    ["5", "5 Dec", "Isaiah 7", "18", "18 Dec", "Colossians 1"],
                    ["6", "6 Dec", "Isaiah 9", "19", "19 Dec", "Hebrews 1"],
                    ["7", "7 Dec", "Isaiah 11", "20", "20 Dec", "John 1"],
                    ["8", "8 Dec", "Isaiah 40", "21", "21 Dec", "Luke 1"],
                    ["9", "9 Dec", "Isaiah 53", "22", "22 Dec", "Matthew 1"],
                    ["10", "10 Dec", "Isaiah 60", "23", "23 Dec", "Titus 2"],
                    ["11", "11 Dec", "Isaiah 61", "24", "24 Dec", "Luke 2"],
                    ["12", "12 Dec", "Jeremiah 33", "25", "25 Dec", "Matthew 2"],
                    ["13", "13 Dec", "Micah 5", "", "", ""],
                ]),
            ]),
            ("How to keep going", [
                ["Read at the same time each day, before your phone gets busy.",
                 "Missed a day? Read two chapters the next day, or simply carry on. Advent is not a test.",
                 "Read it with your family: one chapter after dinner, one person reading aloud.",
                 "Write down one line that stayed with you. By Christmas you will have 25."],
            ]),
            ("Read it in Lamp Bible", [
                "Lamp Bible has this plan built in and free: \"Advent: 25 Days to Christmas\". From Advent Sunday it adds an Advent wreath that lights a new candle each Sunday, an Advent calendar with a door to open each day of December, and a wreath widget for your Home Screen and Lock Screen. The King James Version and the World English Bible are both included and work offline.",
                "Before Advent, the free \"Give Thanks\" plan reads seven chapters on gratitude from 20 to 26 November, ending on Thanksgiving Day: Psalm 100, Deuteronomy 8, Psalm 103, Luke 17, Philippians 4, 1 Thessalonians 5 and Psalm 136.",
            ]),
        ],
    },
    {
        "app": "lamplock",
        "slug": "scroll-less-this-advent",
        "date": "2026-11-05",
        "title": "How to scroll less this Advent: a simple phone plan for Christians",
        "description": ("Practical ways to spend less time on your phone from Thanksgiving to Christmas 2026: put "
                        "scripture before social apps, set a bedtime schedule, and read one chapter a day of Advent."),
        "lead": ("December is the month we most want to slow down and the month our phones get loudest. "
                 "Here is a plan for Advent 2026, from Sunday 29 November to Christmas Day, that keeps your phone "
                 "useful and gives the first minutes of your attention to God."),
        "sections": [
            ("1. Put scripture before scrolling", [
                "The hardest moment is the reflex: you pick up the phone and your thumb is in a feed before you have decided anything. Change what happens in that moment. Before a social app opens, read one verse. It takes twenty seconds, and it turns a reflex into a choice.",
            ]),
            ("2. Choose three apps, not thirty", [
                "You don't need to lock everything. Pick the two or three apps where your time disappears: usually a short-video app, a feed and one game. Leave messages, maps and your Bible alone.",
            ]),
            ("3. Protect the edges of the day", [
                ["Mornings: no feeds until you have read today's chapter.",
                 "Evenings: the phone goes quiet an hour before bed, and charges outside the bedroom.",
                 "Sundays: try a Sabbath from social apps for the four Sundays of Advent (29 November, 6, 13 and 20 December)."],
            ]),
            ("4. Read through Advent", [
                "Swap some scrolling for one chapter a day from 1 to 25 December, from the promise in Genesis 3 to the birth of Jesus in Luke 2. The full plan is on Lamp Bible's site: the Advent reading plan for 2026.",
            ]),
            ("5. Do it with someone", [
                "Habits stick better together. Ask a friend, your spouse or your small group to take the same four weeks with you and check in each Sunday.",
            ]),
            ("How Lamp Lock helps", [
                "Lamp Lock is a Christian app blocker for iPhone built on Apple's Screen Time. You choose the apps; when you open one, a lock screen with today's verse appears first. Read it (or pray a short prayer, or read a chapter) and the app opens for 15 minutes. Schedules cover mornings and bedtime, strict mode keeps the lock on when you'd rather it wasn't, and Circles lets your small group share streaks. Its reading plans include Advent. Locking your first app is free.",
            ]),
        ],
    },
    {
        "app": "holovault",
        "slug": "what-are-my-cards-worth",
        "date": "2026-11-05",
        "title": "How to find out what your Pokémon cards are worth (before Christmas trading)",
        "description": ("A step-by-step guide to pricing Pokémon, One Piece, Lorcana and Yu-Gi-Oh! cards: find the "
                        "exact card, check condition and variant, and use recent market prices, not asking prices."),
        "lead": ("Christmas is when collections grow fastest: packs under the tree, trades with cousins, a binder "
                 "found in the attic. Before you trade or sell, here is how to work out what a card is really worth."),
        "sections": [
            ("1. Find the exact card", [
                "Two cards with the same name can be worth very different amounts. Look at the bottom of the card for the set symbol and the collector number (for example 4/102). The name, set and number together identify the card.",
            ]),
            ("2. Check the variant", [
                ["Holo, reverse holo or plain: the same card can come in several finishes, each with its own price.",
                 "First editions, promos and special art versions are priced separately.",
                 "Language matters: Japanese and English printings have separate markets."],
            ]),
            ("3. Be honest about condition", [
                "Look at the corners, edges, surface and centering under a bright light. Near Mint cards sell for the most; a crease or whitening on the edges lowers the price a lot. Professionally graded cards in slabs are a market of their own and are priced by their grade.",
            ]),
            ("4. Use market prices, not asking prices", [
                "An asking price is what someone hopes to get. A market price comes from what cards actually sold for recently. Use market prices, and look at the trend over a few months: a card that spiked last week may not hold that price.",
            ]),
            ("5. Trade fairly", [
                "When you trade, compare both sides at market price and in the same condition. Writing it down (or showing a screen with both totals) keeps trades friendly, especially with kids and family at Christmas.",
            ]),
            ("Do it in seconds with HoloVault", [
                "HoloVault is an iPhone card scanner for Pokémon, One Piece, Disney Lorcana and Yu-Gi-Oh! cards. Point the camera at a card and it finds the exact card, set and number, with today's market price, prices by condition and a year of price history. Pack Rip mode prices every card as you open a pack, Trade check compares both sides of a trade, and the Christmas list turns your wishlist into a list family can buy from. It's free to try with 25 scans.",
            ]),
        ],
    },
    {
        "app": "glipsy",
        "slug": "thanksgiving-on-a-glp-1",
        "date": "2026-11-05",
        "title": "Thanksgiving on a GLP-1: a protein-first plate and a calm day",
        "description": ("Practical, gentle tips for Thanksgiving and holiday meals while taking a GLP-1 medicine: "
                        "protein first, fiber and water through the day, smaller portions, and no guilt."),
        "lead": ("Thanksgiving falls on Thursday 26 November in 2026. If you're taking a GLP-1 medicine, a big "
                 "holiday meal can feel different from the ones you remember. These are everyday tips many people "
                 "find helpful. They are not medical advice: your doctor or dietitian knows what's right for you."),
        "sections": [
            ("Start with protein", [
                "Put protein on the plate first and eat it first. Roast turkey breast is an easy choice, at about 25 grams of protein in a 3-ounce serving. With a smaller appetite, starting with protein means you get it in before you feel full.",
            ]),
            ("Add fiber and color", [
                "Green beans, roasted vegetables, salad and a spoon of sweet potato add fiber, which many people taking GLP-1 medicines find helps with constipation. Fill a good part of the plate with them.",
            ]),
            ("Smaller portions of the rich dishes", [
                ["Take a spoonful of each favourite instead of a full serving. You can always go back.",
                 "Eat slowly and stop at the first sign of fullness. Very rich or greasy food is often what makes people feel unwell.",
                 "Save room for one slice of pie you really love rather than a little of everything."],
            ]),
            ("Water through the day", [
                "Sip water from the morning on, not all at once with the meal. A glass before you sit down is a good habit.",
            ]),
            ("Plan the day, then let it go", [
                "If you've noticed that some days of your week feel harder, keep that in mind when you plan the day. One big meal doesn't undo anything. Enjoy the people at the table, and get back to your usual routine on Friday.",
            ]),
            ("Keep it simple with Glipsy", [
                "Glipsy is a free iPhone tracker for GLP-1 shots and pills. It counts protein and fiber, not calories: search everyday foods like roast turkey, or scan a barcode, and see your protein, fiber and water for the day at a glance. Log how you feel afterwards in two taps, and Glip's garden grows with every day you log.",
                "Glipsy is a personal log, not medical advice, and never suggests a dose.",
            ]),
        ],
    },
]
