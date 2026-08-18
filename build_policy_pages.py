#!/usr/bin/env python3
"""Build the FULGME Journal policy pages.

Final version. Every statement on these four pages is either sourced from the
published issues or supplied directly by the Editor and Founder in the policy
decision document returned 18 August 2026. Nothing here is inferred.

The publisher postal address is published at the Editor's explicit instruction,
after the privacy risk of publishing a residential address was raised with her.

Internet Archive registration is not claimed anywhere on these pages, because it
has not happened yet.

Invited board contributions are stated as editorial content that is not peer
reviewed, per the Editor's decision of 18 August 2026.
"""
import pathlib

SITE = "https://journal.fulgme.org"
HERE = pathlib.Path(__file__).resolve().parent
LIC = "https://creativecommons.org/licenses/by-nc-nd/4.0/"
REVIEWED = "18 August 2026"
FOURWAVES = "https://event.fourwaves.com/624ae48b-a95e-4903-892e-851e6c6c1023"

NAV = [("../", "Issues"), ("../about/", "About"), ("../editorial-board/", "Editorial Board"),
       ("../policies/", "Policies"), ("../for-authors/", "For Authors")]


def page(slug, title, desc, body):
    cur = ' aria-current="page"'
    nav = "\n".join(
        '      <a href="%s"%s>%s</a>' % (h, cur if h.strip("./") == slug else "", t)
        for h, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | FULGME Journal</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{slug}/">
<link rel="stylesheet" href="../assets/journal.css">
<link rel="license" href="{LIC}">
<link rel="icon" href="../assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="../assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<meta property="og:image" content="https://journal.fulgme.org/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://journal.fulgme.org/assets/og-image.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="FULGME Journal">
<meta property="og:title" content="{title} | FULGME Journal">
<meta property="og:url" content="{SITE}/{slug}/">
<style>
  .pwrap{{max-width:820px;margin:0 auto;padding:0 clamp(1rem,4vw,2.5rem)}}
  .pnav{{background:#fff;border-bottom:1px solid var(--rule)}}
  .pnav .pwrap{{display:flex;flex-wrap:wrap;gap:.2rem}}
  .pnav a{{padding:.75rem .85rem;font-size:.9rem;font-weight:600;color:var(--slate);text-decoration:none;border-bottom:3px solid transparent}}
  .pnav a:hover{{color:var(--blue);background:#F8FAFC}}
  .pnav a[aria-current]{{color:var(--blue);border-bottom-color:var(--gold)}}
  .phead{{background:var(--blue);color:#fff;padding:2.25rem 0 1.9rem;border-bottom:5px solid var(--gold)}}
  .phead .eyebrow{{font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-muted);margin:0 0 .55rem;font-weight:600}}
  .phead h1{{font-family:var(--serif);font-size:clamp(1.8rem,4.5vw,2.6rem);margin:0 0 .4rem;line-height:1.15}}
  .phead p{{margin:0;color:#D6E2EC;max-width:58ch}}
  main.pbody{{padding:2rem 0 3rem}}
  main.pbody h2{{font-family:var(--serif);color:var(--blue);font-size:clamp(1.25rem,3vw,1.55rem);margin:2.2rem 0 .5rem;line-height:1.28}}
  main.pbody h2:first-of-type{{margin-top:0}}
  main.pbody h3{{font-size:1.02rem;color:var(--blue-accent);margin:1.5rem 0 .35rem}}
  main.pbody p,main.pbody li{{max-width:70ch}}
  main.pbody p{{margin:0 0 .9rem}}
  main.pbody ul,main.pbody ol{{margin:.3rem 0 1.1rem;padding-left:1.3rem}}
  main.pbody li{{margin:0 0 .45rem}}
  main.pbody li::marker{{color:var(--gold-dark)}}
  .facts{{border-collapse:collapse;width:100%;font-size:.94rem;margin:1rem 0 1.5rem;background:#fff}}
  .facts th,.facts td{{border:1px solid var(--rule);padding:.6rem .8rem;text-align:left;vertical-align:top}}
  .facts th{{width:34%;background:#F8FAFC;color:var(--blue);font-weight:600}}
  .facts td ul{{margin:.2rem 0 0;padding-left:1.1rem}}
  .lic{{background:#F8F6EF;border:1px solid var(--gold-muted);border-radius:8px;padding:1.1rem 1.3rem;margin:1.2rem 0}}
  .lic p{{margin:0;max-width:none}}
  .lic p + p{{margin-top:.7rem}}
  .steps{{counter-reset:step;list-style:none;padding-left:0;margin:1rem 0 1.5rem}}
  .steps li{{counter-increment:step;position:relative;padding-left:2.6rem;margin:0 0 .9rem;max-width:68ch}}
  .steps li::before{{content:counter(step);position:absolute;left:0;top:.05rem;width:1.85rem;height:1.85rem;
    border-radius:50%;background:var(--blue);color:#fff;font-size:.85rem;font-weight:700;
    display:flex;align-items:center;justify-content:center}}
  .cta{{display:inline-block;background:var(--blue);color:#fff;text-decoration:none;font-weight:600;
    padding:.7rem 1.25rem;border-radius:6px;margin:.2rem 0 1.2rem}}
  .cta:hover{{background:var(--blue-accent);color:#fff}}
  .updated{{margin:2.5rem 0 0;padding-top:1.2rem;border-top:1px solid var(--rule);font-size:.86rem;color:var(--slate)}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<div class="jbar">
  <div class="wrap pwrap">
    <a class="brand" href="../"><img class="blogo" src="../assets/fulgme-mark.png" alt="" width="91" height="94" decoding="async"><span>FULGME<span class="tm">TM</span> Journal</span></a>
    <span class="meta">ISSN 3065-582x</span>
  </div>
</div>

<nav class="pnav" aria-label="Journal sections">
  <div class="pwrap">
{nav}
  </div>
</nav>

<header class="phead">
  <div class="pwrap">
    <p class="eyebrow">FULGME Journal</p>
    <h1>{title}</h1>
    <p>{desc}</p>
  </div>
</header>

<main class="pbody" id="main">
  <div class="pwrap">
{body}
    <p class="updated">This page was last reviewed on {REVIEWED}. Questions about any policy on this
    page should be sent to <a href="mailto:info@fulgme.org">info@fulgme.org</a>.</p>
  </div>
</main>

<footer>
  <div class="wrap pwrap">
    <p><a href="../">Issues</a> &nbsp;&middot;&nbsp; <a href="../about/">About</a> &nbsp;&middot;&nbsp;
       <a href="../editorial-board/">Editorial Board</a> &nbsp;&middot;&nbsp;
       <a href="../policies/">Policies</a> &nbsp;&middot;&nbsp; <a href="../for-authors/">For Authors</a></p>
    <p class="legal">&copy; The author(s). Published by the Forum for United Leaders in Graduate Medical
      Education under <a href="{LIC}" rel="license">CC BY-NC-ND 4.0</a> &nbsp;&bull;&nbsp;
      ISSN 3065-582x (online), 3065-5811 (print) &nbsp;&bull;&nbsp; Journal DOI 10.70785/IHSN6820 &nbsp;&bull;&nbsp;
      <a href="mailto:info@fulgme.org">info@fulgme.org</a></p>
  </div>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------- About
ABOUT = f"""
    <h2>Aims and scope</h2>
    <p>FULGME is a peer-reviewed, open-access journal dedicated to advancing scholarship, innovation,
    and professional development within graduate medical education administration.</p>
    <p>The journal exists for a community that has long done essential work without a formal scholarly
    home. Graduate medical education is built by two groups. One holds the clinical expertise, the
    faculty appointments, and the medical degrees. The other holds the institutional memory, the
    compliance infrastructure, and the operational continuity that allows programs to function.
    FULGME publishes the scholarship of that second group.</p>
    <p>We welcome work from program coordinators and administrators, GME directors and managers,
    designated institutional officials, program directors, and anyone whose work advances the
    administration of graduate medical education. Submissions are accepted year-round.</p>

    <h3>Subject coverage</h3>
    <ul>
      <li>Accreditation readiness, compliance, and Sponsoring Institution operations</li>
      <li>Administrative workflow design and process improvement</li>
      <li>Coordinator and administrator professional development, recognition, and career pathways</li>
      <li>Resident and fellow experience and well-being from an operational perspective</li>
      <li>Program leadership, governance, and committee practice</li>
      <li>Recruitment, onboarding, and workforce planning</li>
    </ul>
    <p>The journal does not publish clinical research or patient care recommendations.</p>

    <h2>Journal information</h2>
    <table class="facts">
      <tr><th>Publisher</th><td>Forum for United Leaders in Graduate Medical Education (FULGME)</td></tr>
      <tr><th>Contact person</th><td>Barbara Gohre, President and Founder</td></tr>
      <tr><th>Publisher address</th><td>8925 West Port Au Prince Lane<br>Peoria, AZ 85381<br>United States</td></tr>
      <tr><th>Contact email</th><td><a href="mailto:info@fulgme.org">info@fulgme.org</a></td></tr>
      <tr><th>ISSN (online)</th><td>3065-582x</td></tr>
      <tr><th>ISSN (print)</th><td>3065-5811</td></tr>
      <tr><th>Journal DOI</th><td>10.70785/IHSN6820</td></tr>
      <tr><th>DOI prefix</th><td>10.70785, registered with Crossref</td></tr>
      <tr><th>First published</th><td>November 2024</td></tr>
      <tr><th>Publication frequency</th><td>Annual. One issue per year, containing a minimum of five
        articles.</td></tr>
      <tr><th>Issues published</th><td>Issue 1, November 2024<br>Issue 2, April 2025<br>Issue 3, August 2026</td></tr>
      <tr><th>Access</th><td>Open access. Free to read, no subscription, no registration required.</td></tr>
      <tr><th>Licence</th><td><a href="{LIC}" rel="license">CC BY-NC-ND 4.0</a>. Copyright is retained by
        the author(s).</td></tr>
      <tr><th>Author charges</th><td>None. See <a href="../policies/#charges">Policies</a>.</td></tr>
      <tr><th>Peer review</th><td>Single-anonymised. Four independent reviewers per submission.
        See <a href="../policies/#peer-review">Policies</a>.</td></tr>
      <tr><th>Language</th><td>English</td></tr>
      <tr><th>Website</th><td><a href="https://www.fulgme.org">fulgme.org</a></td></tr>
    </table>

    <h2>Indexing and discovery</h2>
    <p>Every article is assigned a Crossref DOI and published with Highwire citation metadata,
    Dublin Core metadata, and structured data, so that indexing services and reference managers can
    read it directly from the article page.</p>
    <p>FULGME is registered with Crossref. The journal makes no other indexing claim.</p>
"""

# ---------------------------------------------------------------- Board
BOARD = f"""
    <p>The editorial board is responsible for the scholarly direction of the journal, the integrity of
    the review process, and final decisions on publication.</p>

    <h2>Board members</h2>
    <table class="facts">
      <tr><th>Barbara Gohre, BSHA, C-RGME, C-TAGME</th>
          <td>CEO | President | Founder, FULGME
          <br>Accreditation Manager, Phoenix Children&rsquo;s</td></tr>
      <tr><th>Kelly Conlon, MS, C-TAGME</th>
          <td>Vice President | Editor in Chief, FULGME
          <br>Senior Director, Operations, Graduate Medical Education,
          Northwell Health, Eastern Region</td></tr>
      <tr><th>Stephanie Bowen, MSM, C-TAGME</th>
          <td>Secretary | Associate Editor, FULGME
          <br>Lead GME Program Coordinator, Nemours Children&rsquo;s Health, Jacksonville, Florida
          <br>North Florida UME/GME External Rotating Students
          <br>MCF Pediatric Anesthesiology &amp; Radiology Fellowships
          <br>NCH Pediatric Orthopedic Fellowship</td></tr>
      <tr><th>Crys S. Curkendoll-Draconi, PMP, AA</th>
          <td>Director of Marketing and Grants | Associate Editor, FULGME
          <br>Program Manager, ONMM Residency and Osteopathic Recognition,
          Cleveland Clinic South Pointe Hospital</td></tr>
      <tr><th>Juanita Braxton, PhD, EdS, MBA</th>
          <td>Treasurer | Associate Editor, FULGME
          <br>Executive Director, Imani Consultants</td></tr>
    </table>

    <h2>Editorial responsibilities</h2>
    <p>Board members review submissions within their areas of expertise, advise on scope and standards,
    and decide on acceptance, revision, or rejection. The Editor in Chief makes the final decision on
    every submission, based on the recommendations of the reviewers.</p>
    <p>Board members who author a submission take no part in the review of, or the decision on, their own
    work. Where a board member or editor has any other relationship with a submission, that person is
    recused in the same way.</p>

    <h2>Board contributions to the journal</h2>
    <p>Once a year, board members are invited to contribute to a special topic section. These
    contributions are invited by the editorial board rather than submitted through the open call, and they
    are <strong>editorial content rather than peer-reviewed research</strong>. Each one is labelled as an
    invited board contribution on its own article page, so that readers and indexing services can tell the
    difference.</p>
    <p>A board member takes no part in the decision to publish their own contribution. Invited
    contributions are held to the same standards of accuracy, sourcing, and conflict of interest
    disclosure as everything else the journal publishes.</p>

    <h2>Contact</h2>
    <p>Correspondence for the editorial board should be sent to
    <a href="mailto:info@fulgme.org">info@fulgme.org</a>.</p>
"""

# ---------------------------------------------------------------- Policies
POLICIES = f"""
    <h2 id="open-access">Open access</h2>
    <p>FULGME is a fully open-access journal. Every article is free to read from the moment of
    publication. There is no subscription, no paywall, no embargo period, and no registration
    requirement. Readers may read the full text in HTML or download the PDF at no cost.</p>

    <h2 id="licensing">Licensing and reuse</h2>
    <div class="lic">
      <p><strong>All articles are published under a Creative Commons
      Attribution-NonCommercial-NoDerivatives 4.0 International licence
      (<a href="{LIC}" rel="license">CC BY-NC-ND 4.0</a>).</strong></p>
      <p>You are free to copy and redistribute any article in any medium or format, including for
      teaching and internal institutional use, provided that you credit the author(s) and FULGME and link
      to the licence. You may not use the material for commercial purposes, and you may not distribute a
      modified or adapted version of it.</p>
      <p>This licence replaces the all-rights-reserved statement that appeared in the back matter of
      Issue 1. It applies to every article in every issue, including articles published before this
      policy was adopted.</p>
    </div>

    <h2 id="copyright">Copyright</h2>
    <p>Authors retain copyright in their work. On acceptance, authors grant FULGME a non-exclusive
    licence to publish the article, to distribute it under the CC BY-NC-ND 4.0 licence above, and to
    preserve it in the journal archive.</p>
    <p>Because authors retain copyright, an author remains free to deposit the published article in an
    institutional repository, include it in a promotion or tenure file, and share it directly with
    colleagues.</p>

    <h2 id="peer-review">Peer review</h2>
    <p>FULGME is a peer-reviewed journal. Review is <strong>single-anonymised</strong>: reviewers know the
    identity of the authors, and the authors do not know the identity of the reviewers.</p>
    <table class="facts">
      <tr><th>Reviewers per submission</th><td>Four</td></tr>
      <tr><th>Reviewer independence</th><td>Reviewers are independent of the authors. Anyone with a
        relationship to the submission is recused.</td></tr>
      <tr><th>Review type</th><td>Single-anonymised</td></tr>
      <tr><th>Final decision</th><td>The Editor in Chief, based on the recommendations of all four
        reviewers</td></tr>
      <tr><th>Typical time to decision</th><td>Approximately 90 days from submission</td></tr>
      <tr><th>Possible decisions</th><td>Accept, accept with revisions, revise and resubmit, or decline</td></tr>
    </table>
    <h3>Invited board contributions</h3>
    <p>Once a year, members of the editorial board are invited to contribute to a special topic section.
    These contributions are <strong>editorial content and are not peer reviewed</strong>. They are invited
    by the board rather than submitted through the open call, and every one of them carries a visible
    label on its article page saying so.</p>
    <p>They are held to the same standards of accuracy, sourcing, and conflict of interest disclosure as
    peer-reviewed articles. A board member takes no part in the decision to publish their own
    contribution. Everything else the journal publishes goes through the four-reviewer process described
    above.</p>

    <h2 id="charges">Author charges</h2>
    <p>FULGME charges no fees of any kind. There are no submission fees, article processing charges, page
    charges, colour charges, or fees for supplementary material. Publication is free for authors and free
    for readers, at every stage.</p>

    <h2 id="ethics">Publication ethics</h2>

    <h3>Originality and prior publication</h3>
    <p>FULGME does not require that a submission be previously unpublished. Work that has appeared
    elsewhere, or that is under consideration elsewhere, is eligible for submission.</p>
    <p>Authors must tell the editors at the point of submission where else the work has been published or
    submitted, and must confirm that they hold the rights necessary to publish it here under the CC
    BY-NC-ND 4.0 licence. Where an article has appeared elsewhere first, that prior publication is
    acknowledged on the FULGME article page.</p>

    <h3>Conflicts of interest</h3>
    <p>Authors must disclose any financial or professional relationship that could be perceived to
    influence their work. Every article carries a conflict of interest statement, even where the statement
    is that there is none. Where a board member or editor has a relationship with a submission, that
    person takes no part in the review or the decision.</p>

    <h3>Authorship</h3>
    <p>All listed authors must have contributed substantively to the work and must approve the final
    version. Anyone who contributed substantively must be listed.</p>

    <h3>Consent for named individuals</h3>
    <p>Where an article names an identifiable individual in a case study or personal account, written
    consent from that individual must be on file with the journal before publication. This is the
    journal&rsquo;s established practice.</p>

    <h2 id="corrections">Corrections, retractions, and versioning</h2>
    <p>Published articles are the version of record. Where an error is identified after publication,
    FULGME issues a correction notice on the article page describing what changed and when, rather than
    silently editing the text.</p>
    <p>Articles are never removed from the archive. If a retraction is necessary, the article remains
    available and is clearly marked as retracted, with an explanation. The editorial board has committed
    to this in full.</p>
    <p>Every change to this website is recorded with a date and an author in a public version history.</p>

    <h2 id="archiving">Archiving and preservation</h2>
    <p>The full text of every article is published in both HTML and PDF and is preserved in a public,
    version-controlled repository that holds a complete history of every change. Each article has a
    permanent web address and a Crossref DOI that resolves to it.</p>

    <h2 id="privacy">Privacy</h2>
    <p>This site sets no cookies, runs no analytics or tracking scripts, and loads no third-party
    resources. No personal data is collected from readers.</p>
    <p>Correspondence with authors and reviewers is held by FULGME and is not shared outside the
    editorial process.</p>
"""

# ---------------------------------------------------------------- Authors
AUTHORS = f"""
    <p>FULGME publishes the operational and administrative scholarship of graduate medical education.
    If your work makes a GME program run better, we want to see it. Submissions are accepted
    year-round, and there are no fees at any stage.</p>

    <a class="cta" href="{FOURWAVES}">Go to the FULGME Call for Submissions</a>

    <h2>What we publish</h2>
    <p>The journal publishes the following article types. The word limit is 2,000 words for all types,
    excluding the title page, abstract, references, tables, and figure captions.</p>
    <table class="facts">
      <tr><th>Research</th><td>Original studies with a stated method and results.</td></tr>
      <tr><th>Brief Report</th><td>Shorter empirical work, typically a single-site initiative with outcome data.</td></tr>
      <tr><th>Innovation</th><td>A new structure, tool, or program, with enough detail for others to replicate it.</td></tr>
      <tr><th>Perspective</th><td>Informed argument or professional reflection, grounded in experience.</td></tr>
      <tr><th>Process Improvement</th><td>A described change to a workflow or system, with what was learned.</td></tr>
      <tr><th>Best Practices</th><td>Consolidated practical guidance drawn from experience.</td></tr>
      <tr><th>Review</th><td>A synthesis of existing literature or practice.</td></tr>
    </table>

    <h2>What to include</h2>
    <ul>
      <li>Title</li>
      <li>Every author&rsquo;s full name, credentials, and institutional affiliation</li>
      <li>An abstract. Research and brief reports should use a structured abstract with Background,
          Objective, Methods, Results, and Conclusions.</li>
      <li>The body of the article, with clear section headings, up to 2,000 words</li>
      <li><strong>A reference list for every factual or quantitative claim.</strong> If you state a
          percentage, a count, or a finding from a survey or dataset, cite the source.</li>
      <li>Any figures or tables, with captions, and the underlying numbers</li>
      <li>A conflict of interest statement, even if it is to declare none</li>
      <li>Acknowledgements, if any</li>
      <li>If the work has been published or submitted anywhere else, a note saying where</li>
    </ul>
    <p>The requirement to cite quantitative claims is not a formality. It is what allows another
    coordinator to check your numbers, build on your work, and cite you with confidence.</p>

    <h2>How to submit</h2>
    <p>Submit through the <a href="{FOURWAVES}">FULGME Call for Submissions</a> form. If you have trouble
    with the form, write to <a href="mailto:info@fulgme.org">info@fulgme.org</a> and we will help.</p>

    <h2>What happens next</h2>
    <ol class="steps">
      <li><strong>Acknowledgement.</strong> The editors confirm receipt and check that the submission is
      within scope and complete.</li>
      <li><strong>Review.</strong> Four independent reviewers read your submission. Review is
      single-anonymised: the reviewers see your name, you do not see theirs. No one with a relationship to
      your work reviews it.</li>
      <li><strong>Decision.</strong> The Editor in Chief makes the final decision, based on the
      recommendations of all four reviewers. The decision is accept, accept with revisions, revise and
      resubmit, or decline. Expect roughly 90 days from submission to decision.</li>
      <li><strong>Revision.</strong> If revisions are requested, you receive the reviewer comments and a
      date by which to return the revised manuscript.</li>
      <li><strong>Publication.</strong> Accepted articles appear in the next issue.</li>
    </ol>

    <p>All submissions received through the open call go through this process. The one exception is the
    annual invited board contribution, which is editorial content rather than peer-reviewed research and
    is labelled as such on its article page. See the
    <a href="../policies/#peer-review">peer review policy</a>.</p>

    <h2>After publication</h2>
    <p>Accepted articles are published in the next issue, assigned a Crossref DOI, and made freely
    available in HTML and PDF. Each article receives its own permanent web address and citation metadata,
    so it can be found, cited, and included in your CV or promotion file.</p>
    <p>You retain copyright in your article. FULGME publishes it under
    <a href="{LIC}" rel="license">CC BY-NC-ND 4.0</a>, which means you remain free to deposit it in an
    institutional repository and share it directly with colleagues.</p>
    <p>Authors are encouraged to share their published article. You will find a ready-made citation on
    every article page.</p>

    <h2>Before you submit, check</h2>
    <ul>
      <li>The article is within the 2,000 word limit</li>
      <li>Every quantitative claim has a citation</li>
      <li>Author names, credentials, and affiliations are exactly as you want them to appear permanently</li>
      <li>Any named individual has given written consent</li>
      <li>A conflict of interest statement is included</li>
      <li>Any prior or concurrent publication is disclosed</li>
      <li>You hold the rights needed to publish the work under CC BY-NC-ND 4.0</li>
    </ul>
    <p>Affiliations and author names are worth double-checking. They become part of a permanent, citable
    record, and correcting them afterwards requires a formal correction notice.</p>
"""

PAGES = [
 ("about", "About the Journal",
  "Aims and scope, publisher information, ISSN, publication frequency, and contact details.", ABOUT),
 ("editorial-board", "Editorial Board",
  "The editorial board of the FULGME Journal and its responsibilities.", BOARD),
 ("policies", "Journal Policies",
  "Open access, licensing, copyright, peer review, fees, ethics, corrections, and preservation.", POLICIES),
 ("for-authors", "For Authors",
  "What FULGME publishes, what to include in a submission, how to submit, and what happens next.", AUTHORS),
]

for slug, title, desc, body in PAGES:
    d = HERE / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page(slug, title, desc, body), encoding="utf-8")
    print("wrote", d / "index.html")

# ---- sitemap covering everything -------------------------------------------
urls = [(f"{SITE}/", "monthly", "1.0")]
urls += [(f"{SITE}/{s}/", "yearly", "0.7") for s, *_ in PAGES]
for path, arts in [("issue-3", ["a1", "a2", "a3", "a4", "a5"]),
                   ("issue-2", ["a1", "a2", "a3", "a4"]),
                   ("issue-1", ["a1", "a2", "a3"])]:
    urls.append((f"{SITE}/{path}/", "yearly", "0.9"))
    urls += [(f"{SITE}/{path}/{a}/", "yearly", "0.8") for a in arts]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u, freq, pri in urls:
    sm += ["  <url>", f"    <loc>{u}</loc>", "    <lastmod>2026-08-18</lastmod>",
           f"    <changefreq>{freq}</changefreq>", f"    <priority>{pri}</priority>", "  </url>"]
sm.append("</urlset>")
(HERE / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
print("sitemap.xml now lists", len(urls), "urls")
