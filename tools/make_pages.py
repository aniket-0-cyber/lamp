#!/usr/bin/env python3
"""Builds the landing pages, sitemap.xml and llms.txt of the public site from the data below.

Run from anywhere: python3 tools/make_pages.py. It writes <app>/index.html for each live app,
index.html (the home page), sitemap.xml and llms.txt. The support, privacy and terms pages are
hand-written and left alone. Facts here must match each app's App Store listing (APPSTORE.md).
"""
import html
import json
from datetime import date
from pathlib import Path

SITE = "https://wicklightlabs.com"
STUDIO = "Wicklight Labs"
ROOT = Path(__file__).resolve().parent.parent
TODAY = date.today().isoformat()
# Apple's official badge (developer.apple.com/app-store/marketing/guidelines), kept in assets/.
BADGE = "../assets/app-store-badge.svg"

APPS = [
    {
        "slug": "lampbible",
        "name": "Lamp Bible",
        "store_name": "Lamp Bible: Daily Verse",
        "store": "https://apps.apple.com/us/app/lamp-bible-daily-verse/id6818715500",
        "category": "ReferenceApplication",
        "title": "Lamp Bible: daily Bible verse widget for iPhone, KJV and AI Bible study",
        "headline": "A daily Bible verse on your Lock Screen, and the whole Bible offline.",
        "lead": ("Lamp Bible is a free iPhone app for Christians who want to start each day in the Word. "
                 "It puts a new verse on your Lock Screen and Home Screen every day, gives you the King James "
                 "Version and the World English Bible with no internet needed, and answers your questions "
                 "with real, cited scripture."),
        "summary": ("Free iPhone Bible app with a daily verse widget for the Lock Screen and Home Screen, the KJV "
                    "and World English Bible offline, audio Bible, reading plans, a prayer list, Sleep with "
                    "Scripture, and Ask, AI answers that quote real verses checked word for word. Also in Spanish "
                    "with the Reina-Valera 1909."),
        "colors": {"bg": "#FCF7F1", "text": "#2E2420", "muted": "#7A6A60", "accent": "#B8652F", "card": "#FFFFFF",
                   "dark_bg": "#14110F", "dark_text": "#FAF2E3", "dark_muted": "#C9B9A3", "dark_accent": "#F5CC85", "dark_card": "#1F1A17"},
        "serif": True,
        "features": [
            ("A verse wherever you look", [
                "A new verse every day on Lock Screen and Home Screen widgets, in a sky that follows your day",
                "A short reflection and prayer with today's verse",
                "Gentle reminders at the times you choose, and milestones for your days in the Word"]),
            ("The whole Bible, offline", [
                "King James Version and World English Bible, no internet needed",
                "Search any word, or jump straight to a reference like John 3:16",
                "Listen: the Bible read aloud, verse by verse, even with the screen locked",
                "Highlight, take notes, favorite and share any verse as an image or video"]),
            ("Reading plans", [
                "The Bible in a Year, the New Testament, John in 21 Days, Psalms for Hard Days, Proverbs in 31 Days and more",
                "Seasonal plans for Advent and Lent",
                "One reading a day with a progress ring; a missed day never resets you"]),
            ("Prayer, rest and memory", [
                "A private prayer list you pray through one request at a time, and answered prayers to look back on",
                "Sleep with Scripture: a psalm read softly over rain, ocean or fireplace sounds",
                "One minute of guided breathing with a calming verse for anxious moments",
                "Memory verses that fade word by word and come back just before you'd forget"]),
            ("Ask: answers grounded in scripture", [
                "Ask about anxiety, grief, forgiveness, prayer or any passage",
                "Every answer quotes real verses, checked word for word against the Bible text",
                "5 free questions a month; unlimited with Premium"]),
        ],
        "price": ("Lamp Bible is free to download, with the daily verse, widgets, the full Bible, audio and the "
                  "prayer list free. Lamp Premium adds unlimited Ask, Sleep with Scripture, a reflection with "
                  "every verse, every reading plan and all themes: $39.99 a year with a 7-day free trial, or "
                  "$4.99 a week (US prices)."),
        "privacy": ("No account, no ads and no tracking. Your prayers, notes, highlights and plans stay on your "
                    "iPhone. Ask sends only the question you type, and only after you agree to it."),
        "faq": [
            ("Is there an app that puts a Bible verse on my iPhone Lock Screen?",
             "Yes. Lamp Bible has Lock Screen and Home Screen widgets that show a new Bible verse every day. Add the widget once and the verse changes on its own each morning, with no internet needed."),
            ("Does Lamp Bible have the King James Version?",
             "Yes. Lamp Bible includes the King James Version (KJV) and the World English Bible, both stored on your phone so they work offline. The Spanish edition uses the Reina-Valera 1909."),
            ("Is Lamp Bible free?",
             "Yes. The daily verse, widgets, the full Bible, audio and the prayer list are free. Lamp Premium ($39.99 a year with a 7-day free trial, or $4.99 a week in the US) adds unlimited Ask, Sleep with Scripture, every reading plan and all themes."),
            ("Can an AI Bible app give wrong verses?",
             "In Lamp Bible's Ask, every verse an answer cites is checked against the Bible text and replaced with the exact words before you see it, so the scripture you read is always the real text."),
            ("Does Lamp Bible work without internet?",
             "Yes. The Bible, the daily verse, the widgets, plans and the prayer list all work offline. Only Ask needs a connection."),
            ("Is there a Bible in a Year plan?",
             "Yes. Lamp Bible has The Bible in a Year (365 days), the New Testament, and shorter plans such as John in 21 Days and Proverbs in 31 Days."),
        ],
        "shots": [("1", "Bible verse widgets on the Home Screen and Lock Screen"), ("2", "Today's verse with a reflection"),
                  ("3", "Ask: an answer quoting real Bible verses"), ("4", "Reading plans"), ("5", "A private prayer list")],
    },
    {
        "slug": "lamplock",
        "name": "Lamp Lock",
        "store_name": "Lamp Lock: Bible App Blocker",
        "store": "https://apps.apple.com/us/app/lamp-lock-bible-app-blocker/id6818823592",
        "category": "LifestyleApplication",
        "title": "Lamp Lock: Christian app blocker that unlocks your apps after a Bible verse",
        "headline": "Your social apps wait until you've read today's verse.",
        "lead": ("Lamp Lock is a Christian screen time app for iPhone. You choose the apps that take your time, "
                 "like Instagram, TikTok or YouTube; when you open one, a lock screen appears instead. Read today's "
                 "Bible verse, pray a short prayer or read a chapter, and your apps open for 15 minutes."),
        "summary": ("Christian app blocker for iPhone built on Apple's Screen Time: chosen apps stay locked until you "
                    "read a Bible verse, pray or read a chapter, then open for a set time. Strict mode, focus "
                    "sessions, daily limits, schedules, reading plans, guided prayers, streaks and Circles with "
                    "friends. No account, no ads."),
        "colors": {"bg": "#0E1630", "text": "#F4EEDF", "muted": "#AEB4C6", "accent": "#E8C27A", "card": "#16203F",
                   "dark_bg": "#0E1630", "dark_text": "#F4EEDF", "dark_muted": "#AEB4C6", "dark_accent": "#E8C27A", "dark_card": "#16203F"},
        "serif": True,
        "features": [
            ("How it works", [
                "Pick the apps that take your time",
                "Open one and your lock screen appears instead",
                "Read today's verse, answer a question about it, pray a short guided prayer, read your Bible for a few minutes, or show your printed Bible to the camera",
                "Your apps open for 15 minutes, then lock again"]),
            ("Built to change the habit", [
                "Strict mode: a lock that can't be switched off on a whim, with a cool-down you choose in advance",
                "Focus sessions, daily limits, and schedules for mornings and bedtime",
                "A pause that grows with every unlock, and a cap on unlocks a day",
                "Your real screen time, today and this week"]),
            ("More than a lock", [
                "The whole Bible with search: King James Version and World English Bible",
                "Reading plans, one chapter a day, including Advent and a 40-day challenge",
                "Guided prayers for mornings, anxious thoughts, focus and rest, and a private prayer journal",
                "An olive tree that grows on your Home and Lock Screen with every day you read"]),
            ("Together, if you want", [
                "Circles: share your streak with friends, family or a small group",
                "Ask: Bible questions answered with real, cited scripture"]),
        ],
        "price": ("Lamp Lock is free to start: lock one app with today's verse. Lamp Lock Premium locks as many apps "
                  "and categories as you like and adds strict mode, daily limits, schedules, focus sessions of any "
                  "length and every plan: $39.99 a year with a 7-day free trial, $5.99 a week, or $79.99 once for "
                  "life (US prices)."),
        "privacy": ("Lamp Lock uses Apple's Screen Time, so it never sees which apps you use or for how long. No "
                    "account, no ads, no analytics. Everything stays on your phone unless you choose to use Ask "
                    "or Circles."),
        "faq": [
            ("Is there an app that makes me read the Bible before opening Instagram or TikTok?",
             "Yes. Lamp Lock locks the apps you choose with Apple's Screen Time. When you open one, you read today's verse (or pray, or read a chapter) first, and then the app opens for 15 minutes."),
            ("What is the best Christian app blocker for iPhone?",
             "Lamp Lock is a Christian app blocker that puts a Bible verse between you and your most distracting apps. It adds strict mode, focus sessions, daily limits and reading plans, with no account and no ads, and the first app is free to lock."),
            ("Can I lock apps until I pray?",
             "Yes. Instead of reading the verse you can pray a short guided prayer, written for mornings, anxious thoughts, focus or rest, to unlock your apps."),
            ("Does Lamp Lock see what I do on my phone?",
             "No. Lamp Lock works through Apple's Screen Time, which keeps app names and usage on the device. Lamp Lock never sees which apps you use and has no analytics."),
            ("Is Lamp Lock free?",
             "Lamp Lock is free to start and locks one app with today's verse. Premium ($39.99 a year with a 7-day free trial, $5.99 a week, or $79.99 once, US prices) locks any number of apps and adds strict mode, limits and schedules."),
            ("Can I do it with friends or my small group?",
             "Yes. Circles lets you share your streak with friends, family or a small group using a code. Only a nickname and your streak are shared, and only if you join."),
        ],
        "shots": [("1", "The lock screen over a locked app"), ("2", "Reading today's verse to unlock"),
                  ("3", "The olive tree and lock widgets"), ("4", "A focus session"), ("5", "Circles with friends")],
    },
    {
        "slug": "holovault",
        "name": "HoloVault",
        "store_name": "TCG Card Scanner: HoloVault",
        "store": "https://apps.apple.com/us/app/tcg-card-scanner-holovault/id6819069009",
        "category": "ReferenceApplication",
        "title": "HoloVault: TCG card scanner and collection value tracker for iPhone",
        "headline": "Scan any trading card and see what it's worth in seconds.",
        "lead": ("HoloVault is a trading card scanner for iPhone. Point your camera at a card from Pokémon, One Piece, "
                 "Disney Lorcana or Yu-Gi-Oh! and it finds the exact card, set and number with today's market price. "
                 "Add it with one tap and track your whole collection's value like a portfolio."),
        "summary": ("iPhone TCG card scanner for Pokémon, One Piece, Disney Lorcana and Yu-Gi-Oh! cards: scan one card, "
                    "a stack or 200 photos, see today's market price and a year of price history, track collection "
                    "value like a portfolio, open packs with Pack Rip, set checklists, wishlist price alerts and a "
                    "Christmas list to share. No account, no ads."),
        "colors": {"bg": "#08080F", "text": "#F4F4F8", "muted": "#A3A3B5", "accent": "#A395FF", "card": "#13121F",
                   "dark_bg": "#08080F", "dark_text": "#F4F4F8", "dark_muted": "#A3A3B5", "dark_accent": "#A395FF", "dark_card": "#13121F"},
        "accent2": "#6FB1FF",
        "serif": False,
        "features": [
            ("Scan", [
                "One card, a whole stack, or up to 200 photos at once",
                "Not sure which printing? Pick from side-by-side matches",
                "Search by name or number when you'd rather type"]),
            ("Pack Rip", [
                "Scan every card as you open a pack and watch the running total climb",
                "See what you pulled against what the pack cost, and share it"]),
            ("Your collection, like a portfolio", [
                "Total value and how it moved since the last prices, with a value chart you can drag across",
                "Performance: what you paid against what it's worth, by game, tier and set",
                "Rare, Epic and Legendary tiers, with your best cards on their own shelf"]),
            ("Every card", [
                "Today's market price, a year of price history, and prices for each condition",
                "Trending today: the cards on the move across four games",
                "Set checklists, a wishlist with price alerts, and a Christmas list to send to family",
                "Trade check and a centering check"]),
        ],
        "price": ("HoloVault is free to try with 25 scans and 25 cards. HoloVault Pro gives unlimited scans and "
                  "cards, Performance, full price history, price alerts and every theme: $39.99 a year for every "
                  "game with a 7-day free trial, $19.99 a year for one game, or $5.99 a week (US prices)."),
        "privacy": ("No account, no ads, no tracking. To identify a card, only the cropped photo of that card is "
                    "sent, read by a third-party AI service and not stored on our server. Prices come from licensed "
                    "market data, never from AI."),
        "faq": [
            ("What app can scan Pokémon cards and tell me what they're worth?",
             "HoloVault scans Pokémon cards (and One Piece, Disney Lorcana and Yu-Gi-Oh! cards) with your iPhone camera, finds the exact card, set and number, and shows today's market price with a year of price history."),
            ("Is there a Lorcana or One Piece card scanner for iPhone?",
             "Yes. HoloVault scans Disney Lorcana and One Piece Card Game cards as well as Pokémon and Yu-Gi-Oh!, and tracks the value of your whole collection across all four games."),
            ("How do I track my card collection's value?",
             "Scan or search each card in HoloVault and add it to your collection. HoloVault shows the total value, how it moved since the last prices, a value chart, and what you paid against what it's worth."),
            ("Can I scan a whole pack while opening it?",
             "Yes. Pack Rip mode scans every card as you open a pack, keeps a running total, and shows what you pulled against what the pack cost, ready to share."),
            ("Is HoloVault free?",
             "HoloVault is free to try with 25 scans and 25 cards. HoloVault Pro ($39.99 a year for every game with a 7-day free trial, $19.99 a year for one game, or $5.99 a week in the US) removes the limits."),
            ("Where do HoloVault's prices come from?",
             "From licensed market price data, updated daily, shown with its source and date. AI only reads the name and number printed on the card; it never sets a price."),
        ],
        "shots": [("1", "A scanned card with its market price"), ("2", "Pack Rip: what you pulled"),
                  ("3", "Collection value over time"), ("4", "A card's price trend"), ("5", "Set checklists")],
        "notice": ("HoloVault is an independent app, not affiliated with, endorsed, sponsored or approved by any "
                   "trading card game publisher, grading company or marketplace. Pokémon, One Piece, Disney Lorcana "
                   "and Yu-Gi-Oh! are trademarks of their respective owners. Prices are estimates based on market "
                   "data, not appraisals or financial advice."),
    },
]

COMING = [{"name": "Glipsy", "line": "A GLP-1 shot tracker with protein and water goals. Coming soon to the App Store."}]


def esc(text):
    return html.escape(text, quote=True)


def css(c, serif, accent2=None):
    heading = '"New York", "Iowan Old Style", Georgia, serif' if serif else '-apple-system, "SF Pro Display", system-ui, sans-serif'
    foil = f"linear-gradient(90deg, {c['accent']}, {accent2})" if accent2 else c["accent"]
    return f""":root {{ --bg:{c['bg']}; --text:{c['text']}; --muted:{c['muted']}; --accent:{c['accent']}; --card:{c['card']}; --foil:{foil}; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:{c['dark_bg']}; --text:{c['dark_text']}; --muted:{c['dark_muted']}; --accent:{c['dark_accent']}; --card:{c['dark_card']}; }} }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--text); font:17px/1.6 -apple-system, system-ui, "Segoe UI", sans-serif; }}
a {{ color:var(--accent); }}
.wrap {{ max-width:1040px; margin:0 auto; padding:0 20px; }}
header.top {{ display:flex; align-items:center; gap:12px; padding:18px 0; }}
header.top img {{ width:40px; height:40px; border-radius:10px; }}
header.top .brand {{ font-weight:700; font-size:18px; text-decoration:none; color:var(--text); }}
header.top nav {{ margin-left:auto; display:flex; gap:16px; font-size:15px; }}
header.top nav a {{ color:var(--muted); text-decoration:none; }}
.hero {{ display:grid; grid-template-columns:1.1fr 0.9fr; gap:40px; align-items:center; padding:36px 0 24px; }}
.hero h1 {{ font-family:{heading}; font-size:clamp(32px, 5vw, 52px); line-height:1.1; margin:0 0 16px; letter-spacing:-0.01em; }}
.hero p.lead {{ font-size:19px; color:var(--muted); margin:0 0 24px; }}
.hero .phone img {{ width:100%; max-width:340px; display:block; margin:0 auto; border-radius:28px; box-shadow:0 30px 60px rgba(0,0,0,0.25); }}
.badge img {{ height:54px; }}
.meta {{ font-size:14px; color:var(--muted); margin-top:10px; }}
.shots {{ display:flex; gap:16px; overflow-x:auto; padding:20px 0 28px; scroll-snap-type:x mandatory; }}
.shots figure {{ margin:0; flex:0 0 220px; scroll-snap-align:start; }}
.shots img {{ width:220px; border-radius:20px; display:block; }}
.shots figcaption {{ font-size:13px; color:var(--muted); margin-top:8px; }}
section {{ padding:24px 0; }}
h2 {{ font-family:{heading}; font-size:28px; margin:0 0 18px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; }}
.card {{ background:var(--card); border-radius:20px; padding:20px 22px; border:1px solid rgba(127,127,127,0.18); }}
.card h3 {{ margin:0 0 8px; font-size:18px; }}
.card ul {{ margin:0; padding-left:20px; }}
.card li {{ margin:6px 0; color:var(--muted); }}
.plain p {{ color:var(--muted); max-width:760px; }}
details {{ background:var(--card); border-radius:16px; padding:14px 18px; margin:10px 0; border:1px solid rgba(127,127,127,0.18); }}
summary {{ font-weight:600; cursor:pointer; }}
details p {{ color:var(--muted); margin:10px 0 2px; }}
.others {{ display:flex; gap:14px; flex-wrap:wrap; }}
.others a {{ display:flex; align-items:center; gap:10px; background:var(--card); border-radius:16px; padding:10px 14px; text-decoration:none; color:var(--text); border:1px solid rgba(127,127,127,0.18); }}
.others img {{ width:36px; height:36px; border-radius:9px; }}
footer {{ padding:28px 0 48px; font-size:14px; color:var(--muted); }}
footer .links {{ display:flex; gap:18px; flex-wrap:wrap; margin-bottom:10px; }}
.accentbar {{ height:4px; width:56px; border-radius:2px; background:var(--foil); margin-bottom:18px; }}
@media (max-width: 760px) {{
  .hero {{ grid-template-columns:1fr; gap:24px; padding-top:16px; }}
  .hero .phone img {{ max-width:220px; }}
  header.top nav {{ gap:12px; font-size:14px; }}
}}
"""


def json_ld(app):
    base = f"{SITE}/{app['slug']}/"
    software = {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": app["store_name"],
        "alternateName": app["name"],
        "description": app["summary"],
        "url": base,
        "operatingSystem": "iOS 18.0 or later",
        "applicationCategory": app["category"],
        "installUrl": app["store"],
        "downloadUrl": app["store"],
        "image": base + "img/icon-512.png",
        "screenshot": [base + f"img/{n}.jpg" for n, _ in app["shots"]],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "description": "Free to download, with optional in-app subscriptions."},
        "publisher": {"@type": "Organization", "name": STUDIO, "url": f"{SITE}/"},
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in app["faq"]],
    }
    return "\n".join(f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>' for block in (software, faq))


def head(title, description, url, image, style, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<link rel="alternate" type="text/plain" href="{SITE}/llms.txt" title="llms.txt">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{image}">
<style>
{style}</style>
{extra}
</head>
"""


def app_page(app):
    base = f"{SITE}/{app['slug']}/"
    others = [a for a in APPS if a["slug"] != app["slug"]]
    features = "\n".join(
        f'<div class="card"><h3>{esc(title)}</h3><ul>' + "".join(f"<li>{esc(item)}</li>" for item in items) + "</ul></div>"
        for title, items in app["features"])
    shots = "\n".join(
        f'<figure><img src="img/{n}.jpg" alt="{esc(alt)}" width="220" loading="lazy"><figcaption>{esc(alt)}</figcaption></figure>'
        for n, alt in app["shots"][1:])
    faq = "\n".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in app["faq"])
    other_links = "\n".join(
        f'<a href="../{o["slug"]}/"><img src="../{o["slug"]}/img/icon.png" alt="" width="36" height="36"><span>{esc(o["name"])}</span></a>'
        for o in others)
    notice = f'<p>{esc(app["notice"])}</p>' if app.get("notice") else ""
    first_alt = app["shots"][0][1]
    return head(app["title"], app["summary"], base, base + "img/icon-512.png", css(app["colors"], app["serif"], app.get("accent2")), json_ld(app)) + f"""<body>
<div class="wrap">
<header class="top">
  <img src="img/icon.png" alt="{esc(app['name'])} icon" width="40" height="40">
  <a class="brand" href="./">{esc(app['name'])}</a>
  <nav><a href="support/">Support</a><a href="privacy/">Privacy</a>{'<a href="terms/">Terms</a>' if (ROOT / app['slug'] / 'terms').exists() else ''}</nav>
</header>
<main>
<div class="hero">
  <div>
    <div class="accentbar"></div>
    <h1>{esc(app['headline'])}</h1>
    <p class="lead">{esc(app['lead'])}</p>
    <a class="badge" href="{app['store']}"><img src="{BADGE}" alt="Download {esc(app['store_name'])} on the App Store" height="54"></a>
    <p class="meta">Free on iPhone · iOS 18 or later · No account, no ads</p>
  </div>
  <div class="phone"><img src="img/1.jpg" alt="{esc(first_alt)}" width="340"></div>
</div>
<div class="shots" aria-label="Screenshots">
{shots}
</div>
<section>
  <h2>What {esc(app['name'])} does</h2>
  <div class="grid">
{features}
  </div>
</section>
<section class="plain">
  <h2>Price</h2>
  <p>{esc(app['price'])}</p>
  <h2>Privacy</h2>
  <p>{esc(app['privacy'])} <a href="privacy/">Privacy Policy</a></p>
</section>
<section>
  <h2>Questions</h2>
{faq}
</section>
<section>
  <h2>More apps</h2>
  <div class="others">
{other_links}
  </div>
</section>
</main>
<footer>
  <div class="links"><a href="{app['store']}">{esc(app['name'])} on the App Store</a><a href="support/">Support</a><a href="privacy/">Privacy Policy</a>{'<a href="terms/">Terms of Use</a>' if (ROOT / app['slug'] / 'terms').exists() else ''}<a href="../">All apps</a></div>
  <p>Made by <a href="../">Wicklight Labs</a>.</p>
  {notice}
</footer>
</div>
</body>
</html>
"""


def home_page():
    cards = "\n".join(
        f"""<a class="card applink" href="{a['slug']}/"><img src="{a['slug']}/img/icon.png" alt="" width="64" height="64">
<div><h3>{esc(a['name'])}</h3><p>{esc(a['summary'])}</p></div></a>""" for a in APPS)
    coming = "\n".join(f'<div class="card applink"><div><h3>{esc(c["name"])}</h3><p>{esc(c["line"])}</p></div></div>' for c in COMING)
    colors = {"bg": "#FBF8F4", "text": "#1E1B18", "muted": "#6E655D", "accent": "#9A5A2A", "card": "#FFFFFF",
              "dark_bg": "#111013", "dark_text": "#F4F1EC", "dark_muted": "#B2AAA0", "dark_accent": "#E8C27A", "dark_card": "#1B1A1E"}
    style = css(colors, True) + """.applink { display:flex; gap:18px; align-items:flex-start; text-decoration:none; color:var(--text); margin:14px 0; }
.applink img { border-radius:15px; flex:0 0 64px; }
.applink h3 { margin:0 0 4px; font-size:20px; }
.applink p { margin:0; color:var(--muted); font-size:15px; }
"""
    listing = {
        "@context": "https://schema.org", "@type": "ItemList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/{a['slug']}/", "name": a["store_name"]} for i, a in enumerate(APPS)],
    }
    org = {"@context": "https://schema.org", "@type": "Organization", "name": STUDIO, "url": f"{SITE}/", "logo": f"{SITE}/lampbible/img/icon-512.png"}
    extra = "\n".join(f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>' for block in (org, listing))
    return head("Wicklight Labs: small, private iPhone apps", "Wicklight Labs makes small, private iPhone apps: Lamp Bible (a daily Bible verse widget), Lamp Lock (a Christian app blocker) and HoloVault (a TCG card scanner).",
                f"{SITE}/", f"{SITE}/lampbible/img/icon-512.png", style, extra) + f"""<body>
<div class="wrap">
<main>
<section class="plain">
  <p style="font-weight:700; letter-spacing:0.08em; text-transform:uppercase; font-size:13px; margin:28px 0 10px;">Wicklight Labs</p>
  <div class="accentbar"></div>
  <h1 style="font-family:'New York', Georgia, serif; font-size:40px; margin:0 0 8px;">Small, private apps for iPhone</h1>
  <p>No accounts, no ads, no tracking. Each app does one thing well.</p>
</section>
<section>
{cards}
{coming}
</section>
</main>
<footer><div class="links"><a href="llms.txt">llms.txt</a><a href="sitemap.xml">Sitemap</a></div></footer>
</div>
</body>
</html>
"""


# Every crawler is welcome, search engines and AI assistants alike.
ROBOTS = f"""User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
"""


def sitemap():
    urls = [f"{SITE}/"]
    for a in APPS:
        urls.append(f"{SITE}/{a['slug']}/")
        for sub in ("support", "privacy", "terms"):
            if (ROOT / a["slug"] / sub / "index.html").exists():
                urls.append(f"{SITE}/{a['slug']}/{sub}/")
    body = "\n".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n'


def llms():
    parts = ["# Wicklight Labs: Lamp Bible, Lamp Lock and HoloVault",
             "",
             "> Wicklight Labs makes small, private iPhone apps. No accounts, no ads, no tracking. All are free to download with optional subscriptions.",
             ""]
    for a in APPS:
        parts += [f"## {a['store_name']}", "", a["summary"], "",
                  f"- [Website]({SITE}/{a['slug']}/): features, price, privacy and FAQ",
                  f"- [App Store]({a['store']})",
                  f"- Price: {a['price']}",
                  f"- Privacy: {a['privacy']}", ""]
        parts += ["Common questions:", ""] + [f"- {q} {ans}" for q, ans in a["faq"]] + [""]
    parts += ["## Coming soon", ""] + [f"- {c['name']}: {c['line']}" for c in COMING] + [""]
    return "\n".join(parts)


if __name__ == "__main__":
    for app in APPS:
        (ROOT / app["slug"] / "index.html").write_text(app_page(app))
    (ROOT / "index.html").write_text(home_page())
    (ROOT / "sitemap.xml").write_text(sitemap())
    (ROOT / "llms.txt").write_text(llms())
    (ROOT / "robots.txt").write_text(ROBOTS)
    (ROOT / "CNAME").write_text("wicklightlabs.com\n")
    print("wrote", ", ".join([a["slug"] for a in APPS] + ["index.html", "sitemap.xml", "llms.txt"]))
