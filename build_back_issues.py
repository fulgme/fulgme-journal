#!/usr/bin/env python3
"""Build the FULGME Journal back issues (Issue 1 and Issue 2).

Reuses the article-page renderer in build_articles.py by swapping the module's
ISSUE dictionary, so all three issues share one template and one stylesheet.

Run from the repository root:   python3 build_back_issues.py
"""
import html, json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_articles as BA
from back_issues_data import ISSUE1, I1_ARTICLES, ISSUE2, I2_ARTICLES

HERE = pathlib.Path(__file__).resolve().parent
SITE = BA.SITE

BOARD = {
 "1": [
  "Welcome to the inaugural edition of the Forum for United Leaders in Graduate Medical Education (FULGME). This platform is designed to foster a collaborative and innovative environment for graduate medical education professionals.",
  "In this edition, you can look forward to scholarly exchanges that add to the body of knowledge in graduate medical education, showcasing of best practices, innovative ideas and strategies, process improvement strategies, and the building of a supportive community of graduate medical education professionals who learn from each other, collaborate on initiatives, and support each other&rsquo;s growth and development.",
  "We believe that by sharing our collective wisdom and experiences, we can make a significant impact on the future of graduate medical education. Our goal is to create a dynamic and inclusive platform where every voice is heard, and every contribution is valued.",
  "Thank you for joining us on this journey. We look forward to your active participation and to the many exciting discussions and collaborations that lie ahead.",
 ],
 "2": [
  "Welcome to the second edition of the Forum for United Leaders in Graduate Medical Education (FULGME) Journal.",
  "We are thrilled to continue our journey together in fostering a collaborative environment where graduate medical education professionals can exchange ideas, learn from each other, and drive meaningful change.",
  "Our collective efforts are shaping the future of graduate medical education. We invite you to actively engage, share your insights, and contribute to our vibrant community.",
  "In this issue, we continue our tradition of featuring inspiring quotes. Please share a quote that has motivated or inspired you with us at <a href=\"mailto:info@fulgme.org\">info@fulgme.org</a>.",
 ],
}
QUOTE = {
 "1": ("&ldquo;I&rsquo;ve learned that people will forget what you said, people will forget what you did, "
       "but people will never forget how you made them feel.&rdquo;", "Maya Angelou"),
 "2": ("&ldquo;If you can&rsquo;t fly then run, if you can&rsquo;t run then walk, if you can&rsquo;t walk "
       "then crawl, but whatever you do you have to keep moving forward.&rdquo;", "Martin Luther King Jr."),
}


def issue_page(ISSUE, ARTICLES):
    toc = "\n".join(
        f'        <li><a href="{a["slug"]}/"><span class="id">{a["id"]}</span>'
        f'{a["title"]}</a></li>' for a in ARTICLES)
    cards = []
    for a in ARTICLES:
        names = ", ".join(x["name"] for x in a["authors"])
        affs = " &nbsp;&middot;&nbsp; ".join(a["affiliations"])
        doi = (f'<p class="doi">DOI <code>{a["doi"]}</code></p>' if a.get("doi")
               else '<p class="doi">DOI pending correction</p>')
        cards.append(f'''      <article class="card acard">
        <p class="art-top"><span class="kicker">{a["type"]}</span><span class="artid">{a["id"]}</span></p>
        <h3><a href="{a["slug"]}/">{a["title"]}</a></h3>
        <p class="byline">{names}</p>
        <p class="affil">{affs}</p>
        {doi}
        <p class="abs">{a["abstract_plain"]}</p>
        <p><a class="btn" href="{a["slug"]}/">Read full article <span aria-hidden="true">&rsaquo;</span></a></p>
      </article>''')
    quote, who = QUOTE[ISSUE["num"]]
    board = "\n".join(f'        <p>{p}</p>' for p in BOARD[ISSUE["num"]])
    note = (f'      <div class="notice"><p><strong>About this issue.</strong> {ISSUE["note"]}</p></div>\n'
            if ISSUE.get("note") else "")

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FULGME Journal, {ISSUE["label"]}, {ISSUE["published"]} | Forum for United Leaders in Graduate Medical Education</title>
<meta name="description" content="FULGME Journal {ISSUE["label"]}, {ISSUE["published"]}. Peer-reviewed, open-access scholarship in graduate medical education administration.">
<link rel="canonical" href="{SITE}/{ISSUE["path"]}/">
<link rel="stylesheet" href="../assets/journal.css">
<meta name="citation_journal_title" content="FULGME: Forum for United Leaders in Graduate Medical Education">
<meta name="citation_publisher" content="Forum for United Leaders in Graduate Medical Education">
<meta name="citation_issn" content="{ISSUE["issn"]}">
<meta name="citation_issue" content="{ISSUE["issue"]}">
<meta name="citation_publication_date" content="{ISSUE["pub_iso"].replace("-", "/")}">
<meta name="citation_doi" content="{ISSUE["issue_doi"]}">
<link rel="icon" href="../assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="../assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<meta property="og:image" content="https://journal.fulgme.org/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://journal.fulgme.org/assets/og-image.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="FULGME Journal">
<meta property="og:title" content="FULGME Journal, {ISSUE["label"]}, {ISSUE["published"]}">
<meta property="og:url" content="{SITE}/{ISSUE["path"]}/">
<style>
  .icover{{background:var(--blue);color:#fff;padding:2.5rem 0 2rem;border-bottom:5px solid var(--gold)}}
  .icover .eyebrow{{font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-muted);margin:0 0 .8rem;font-weight:600}}
  .icover h1{{font-family:var(--serif);font-size:clamp(1.9rem,5vw,2.8rem);margin:0 0 .35rem;line-height:1.12}}
  .icover .tm{{font-size:.34em;vertical-align:super;color:var(--gold);font-family:var(--sans);font-weight:600}}
  .icover p{{margin:0;color:#D6E2EC;max-width:56ch}}
  .icover .wrap,.iwrap{{max-width:1060px}}
  .iwrap{{margin:0 auto;padding:0 clamp(1rem,4vw,2.5rem)}}
  .icols{{display:grid;grid-template-columns:minmax(0,1fr) 310px;gap:clamp(1.5rem,3vw,2.75rem);align-items:start;padding:2.25rem 0 1rem}}
  @media (max-width:900px){{.icols{{grid-template-columns:1fr}}.iside{{order:-1}}}}
  .iside{{position:sticky;top:1.25rem;display:grid;gap:1.25rem}}
  @media (max-width:900px){{.iside{{position:static}}}}
  .iside h2,.toc h2{{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin:0;padding:.9rem 1.1rem;border-bottom:1px solid var(--rule);background:#F8FAFC;border-radius:8px 8px 0 0;font-weight:700}}
  .toc ol{{list-style:none;margin:0;padding:.5rem 0}}
  .toc li{{border-bottom:1px solid #EEF2F6}} .toc li:last-child{{border-bottom:0}}
  .toc a{{display:block;padding:.7rem 1.1rem;text-decoration:none;color:var(--ink);font-size:.92rem;line-height:1.45}}
  .toc a:hover{{background:#F3F7FA;color:var(--blue)}}
  .toc .id{{display:inline-block;font-weight:700;color:var(--gold-dark);margin-right:.5rem}}
  .meta-list{{margin:0;padding:.8rem 1.1rem 1.1rem;font-size:.87rem}}
  .meta-list div{{display:grid;grid-template-columns:7.5rem 1fr;gap:.35rem;padding:.32rem 0;border-bottom:1px dotted #E3E9EF}}
  .meta-list div:last-child{{border-bottom:0}}
  .meta-list dt{{color:var(--slate);font-weight:600}} .meta-list dd{{margin:0;word-break:break-word}}
  .block{{padding:clamp(1.25rem,3vw,1.9rem);margin:0 0 1.5rem}}
  h2.sec{{font-family:var(--serif);font-size:clamp(1.3rem,3vw,1.65rem);color:var(--blue);margin:0 0 .8rem}}
  .acard{{padding:clamp(1.25rem,3vw,1.9rem);margin:0 0 1.25rem}}
  .acard h3{{font-family:var(--serif);font-size:clamp(1.1rem,2.6vw,1.4rem);line-height:1.3;margin:0 0 .5rem}}
  .acard h3 a{{color:var(--blue);text-decoration:none}} .acard h3 a:hover{{text-decoration:underline}}
  .acard .byline{{margin:0;font-weight:600;font-size:.97rem}}
  .acard .affil{{margin:.2rem 0 0;font-size:.87rem;color:var(--slate)}}
  .acard .doi{{margin:.55rem 0 0;font-size:.82rem;color:var(--slate)}}
  .acard .doi code{{font-family:ui-monospace,Menlo,Consolas,monospace;background:#F1F5F8;padding:.12rem .35rem;border-radius:3px;font-size:.9em}}
  .acard .abs{{margin:.85rem 0 1rem;font-size:.95rem;max-width:74ch}}
  .pullquote{{margin:1.4rem 0 0;padding:1rem 1.2rem;background:#F8F6EF;border-left:4px solid var(--gold);border-radius:0 6px 6px 0}}
  .pullquote blockquote{{margin:0;font-family:var(--serif);font-size:1.08rem;font-style:italic;color:var(--blue);line-height:1.5}}
  .pullquote cite{{display:block;margin-top:.5rem;font-style:normal;font-size:.83rem;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--slate)}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<div class="jbar">
  <div class="wrap iwrap">
    <a class="brand" href="../"><img class="blogo" src="../assets/fulgme-mark.png" alt="" width="91" height="94" decoding="async"><span>FULGME<span class="tm">TM</span> Journal</span></a>
    <span class="meta">{ISSUE["label"]} &middot; {ISSUE["published"]}</span>
  </div>
</div>

<header class="icover">
  <div class="iwrap">
    <p class="eyebrow">{ISSUE["published"]} &nbsp;&middot;&nbsp; {ISSUE["label"]}</p>
    <h1>FULGME<span class="tm">TM</span> Journal</h1>
    <p>Forum for United Leaders in Graduate Medical Education. A peer-reviewed, open-access journal advancing research, authorship, scholarship, innovation, and professional development in graduate medical education leaders.</p>
  </div>
</header>

<main id="main">
<div class="iwrap icols">
  <div>
{note}      <section class="card block" aria-labelledby="board">
      <h2 class="sec" id="board">A Message from the Board</h2>
{board}
      <div class="pullquote">
        <blockquote>{quote}</blockquote>
        <cite>{who}</cite>
      </div>
    </section>

    <h2 class="sec">Articles in this issue</h2>
{chr(10).join(cards)}
  </div>

  <aside class="iside" aria-label="Issue contents and information">
    <nav class="card toc" aria-labelledby="toc-h">
      <h2 id="toc-h">Inside this Issue</h2>
      <ol>
{toc}
      </ol>
    </nav>
    <section class="card" aria-labelledby="info-h">
      <h2 id="info-h">Issue Information</h2>
      <dl class="meta-list">
        <div><dt>Publisher</dt><dd>Forum for United Leaders in Graduate Medical Education</dd></div>
        <div><dt>ISSN (online)</dt><dd>3065-582x</dd></div>
        <div><dt>ISSN (print)</dt><dd>3065-5811</dd></div>
        <div><dt>Issue</dt><dd>{ISSUE["num"]}</dd></div>
        <div><dt>Published</dt><dd>{ISSUE["published"]}</dd></div>
        <div><dt>Journal DOI</dt><dd>{ISSUE["journal_doi"]}</dd></div>
        <div><dt>Issue DOI</dt><dd>{ISSUE["issue_doi"]}</dd></div>
        <div><dt>Access</dt><dd>Peer reviewed, open access</dd></div>
        <div><dt>Contact</dt><dd><a href="mailto:info@fulgme.org">info@fulgme.org</a></dd></div>
      </dl>
    </section>
    <section class="card" aria-labelledby="dl-h">
      <h2 id="dl-h">Download</h2>
      <div style="padding:1rem 1.1rem">
        <a class="btn" href="pdf/{ISSUE["issue_pdf"]}" download><span aria-hidden="true">&#8681;</span> {ISSUE["label"]} (PDF)</a>
      </div>
    </section>
  </aside>
</div>
</main>

<footer>
  <div class="wrap iwrap">
    <p><a href="../">FULGME Journal</a> &nbsp;&middot;&nbsp; <a href="https://www.fulgme.org">fulgme.org</a> &nbsp;&middot;&nbsp; <a href="mailto:info@fulgme.org">info@fulgme.org</a></p>
    <p class="legal">&copy; The author(s). Published by the Forum for United Leaders in Graduate Medical Education under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" rel="license">CC BY-NC-ND 4.0</a> &nbsp;&bull;&nbsp;
      {ISSUE["label"]}, {ISSUE["published"]} &nbsp;&bull;&nbsp; ISSN: {ISSUE["issn"]} &nbsp;&bull;&nbsp;
      Journal DOI: {ISSUE["journal_doi"]} &nbsp;&bull;&nbsp; Issue DOI: {ISSUE["issue_doi"]}</p>
  </div>
</footer>

<script type="application/ld+json">
{json.dumps({"@context":"https://schema.org","@type":"PublicationIssue",
 "issueNumber":ISSUE["num"],"datePublished":ISSUE["pub_iso"],
 "name":f'FULGME Journal, {ISSUE["label"]}, {ISSUE["published"]}',
 "url":f'{SITE}/{ISSUE["path"]}/',
 "isPartOf":{"@type":"Periodical","name":"FULGME: Forum for United Leaders in Graduate Medical Education",
   "issn":ISSUE["issn"],"publisher":{"@type":"Organization",
   "name":"Forum for United Leaders in Graduate Medical Education","url":"https://www.fulgme.org"}},
 "hasPart":[{"@type":"ScholarlyArticle","name":html.unescape(a["title"]),
   "author":[{"@type":"Person","name":html.unescape(x["name"])} for x in a["authors"]],
   "url":f'{SITE}/{ISSUE["path"]}/{a["slug"]}/',
   **({"identifier":f'https://doi.org/{a["doi"]}'} if a.get("doi") else {})} for a in ARTICLES]},
 indent=2)}
</script>
</body>
</html>
'''


def build(ISSUE, ARTICLES):
    BA.ISSUE = ISSUE                      # the renderer reads this module global
    root = HERE / ISSUE["path"]
    root.mkdir(parents=True, exist_ok=True)
    for i, a in enumerate(ARTICLES):
        d = root / a["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(
            BA.page(a, ARTICLES[i - 1] if i > 0 else None,
                       ARTICLES[i + 1] if i < len(ARTICLES) - 1 else None), encoding="utf-8")
        print("  wrote", d / "index.html")
    (root / "index.html").write_text(issue_page(ISSUE, ARTICLES), encoding="utf-8")
    print("  wrote", root / "index.html")


ALL = [(ISSUE1, I1_ARTICLES), (ISSUE2, I2_ARTICLES)]
for ISSUE, ARTS in ALL:
    print(ISSUE["label"])
    build(ISSUE, ARTS)

# ---- sitemap covering all three issues -------------------------------------
urls = [(f"{SITE}/", "monthly", "1.0")]
for path, arts in [("issue-3", ["a1", "a2", "a3", "a4", "a5"]),
                   ("issue-2", [a["slug"] for a in I2_ARTICLES]),
                   ("issue-1", [a["slug"] for a in I1_ARTICLES])]:
    urls.append((f"{SITE}/{path}/", "yearly", "0.9"))
    urls += [(f"{SITE}/{path}/{s}/", "yearly", "0.8") for s in arts]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u, freq, pri in urls:
    sm += ["  <url>", f"    <loc>{u}</loc>", "    <lastmod>2026-08-17</lastmod>",
           f"    <changefreq>{freq}</changefreq>", f"    <priority>{pri}</priority>", "  </url>"]
sm.append("</urlset>")
(HERE / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
print("wrote sitemap.xml with", len(urls), "urls")
