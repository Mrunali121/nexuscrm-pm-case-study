"""
Builds the multi-page NexusCRM site from the Markdown/CSV documents.

    pip install markdown
    python build_site.py

Writes index.html plus one page per lifecycle document, all in the repo root so GitHub Pages
works however the files were uploaded (drag-and-drop flattens folders).
"""
import csv
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
REPO = "https://github.com/Mrunali121/NexusCRM-PM"

# slug, number, label, title, lead, [source md files], phase
DOCS = [
    ("business-case", "01", "Business case", "Business Case", "Why build it: the problem, the options considered, and the recommendation.", ["01-business-case.md"], "Initiate"),
    ("charter", "02", "Project charter", "Project Charter", "Scope, objectives, team, milestones and success criteria.", ["02-project-charter.md"], "Initiate"),
    ("stakeholders", "03", "Stakeholders", "Stakeholder Analysis", "Who cares, how much power they hold, and how each is engaged.", ["03-stakeholder-analysis.md"], "Initiate"),
    ("raci", "04", "RACI matrix", "RACI Matrix", "Who is Responsible, Accountable, Consulted and Informed for 18 deliverables.", ["04-raci-matrix.md"], "Initiate"),
    ("requirements", "05", "Requirements", "Requirements", "18 functional and 12 non-functional requirements from four workshops.", ["05-requirements/functional-requirements.md", "05-requirements/non-functional-requirements.md"], "Plan"),
    ("wbs", "06", "WBS", "Work Breakdown Structure", "Eight phases, Week 0 to 18.", ["06-wbs.md"], "Plan"),
    ("backlog", "07", "Product backlog", "Product Backlog", "25 stories, story-pointed, MoSCoW-prioritised and mapped to releases. Filter it below.", None, "Plan"),
    ("roadmap", "08", "Roadmap", "Roadmap", "Two releases, sprint by sprint.", ["08-roadmap.md"], "Plan"),
    ("release-plan", "09", "Release plan", "Release Plan", "Scope, rollout approach and rollback plan for each release.", ["09-release-plan.md"], "Plan"),
    ("sprints", "10", "Sprint plans", "Sprint Planning", "Eight two-week sprints. Two are documented in full depth.", ["10-sprint-planning/00-overview.md"], "Execute"),
    ("sprint-03", "10a", "Sprint 3: a risk happens", "Sprint 3: a Dependency Risk That Materialised", "A shared component slips by two days. Here is what the PM did.", ["10-sprint-planning/sprint-03-plan.md"], "Execute"),
    ("sprint-06", "10b", "Sprint 6: a scope trade-off", "Sprint 6: a Scope Trade-off Under Deadline Pressure", "An unplanned legal review threatens a Should-priority feature.", ["10-sprint-planning/sprint-06-plan.md"], "Execute"),
    ("risks", "11", "Risks & issues", "Risk and Issue Register", "Seven risks and two issues, scored and tracked to closure.", ["11-risk-issue-register.md"], "Control"),
    ("dependencies", "12", "Dependencies", "Dependency Management", "Four internal and four external dependencies.", ["12-dependency-management.md"], "Control"),
    ("status-reports", "13", "Status reports", "Status Reports", "Three snapshots: mid-build, release transition, pre-launch.", ["13-status-reports/status-report-week-07.md", "13-status-reports/status-report-week-10.md", "13-status-reports/status-report-week-15.md"], "Control"),
    ("uat", "14", "UAT plan", "UAT Plan", "Entry and exit criteria, ten test scenarios, severity classes.", ["14-uat-plan.md"], "Close"),
    ("go-live", "15", "Go-live checklist", "Go-Live Checklist", "Cutover steps and the rollback plan.", ["15-go-live-checklist.md"], "Close"),
    ("retrospective", "16", "Retrospective", "Retrospective", "What worked, what did not, and who owns each action.", ["16-retrospective.md"], "Close"),
]
PHASES = [("Initiate", "Make the case, get the mandate"), ("Plan", "Scope, schedule, backlog"), ("Execute", "Two releases in 8 sprints"), ("Control", "Risks, dependencies, reporting"), ("Close", "Prove it, launch it, learn")]
SLUG = {d[0]: d for d in DOCS}
LINKS = {}
for d in DOCS:
    for s in d[5] or []:
        LINKS[s] = f"{d[0]}.html"
        LINKS[Path(s).name] = f"{d[0]}.html"
LINKS.update({"07-product-backlog.csv": "backlog.html", "05-requirements": "requirements.html", "10-sprint-planning": "sprints.html",
              "10-sprint-planning/": "sprints.html", "13-status-reports": "status-reports.html", "README.md": "index.html", "index.html": "index.html"})

ORDER = [d[0] for d in DOCS]


def rail(cur):
    out = []
    for ph, _ in PHASES:
        out.append(f"<h4>{ph}</h4>")
        for d in DOCS:
            if d[6] == ph:
                c = ' aria-current="page"' if d[0] == cur else ""
                out.append(f'<a href="{d[0]}.html"{c}><i>{d[1]}</i>{d[2]}</a>')
    return "".join(out)


def shell(slug, title, inner, head="", desc=""):
    r = rail(slug)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} | NexusCRM Case Study</title>
<meta name="description" content="{html.escape(desc or 'NexusCRM: a full-lifecycle project management case study.')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,600;0,700;1,600&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
</head>
<body>
<header class="topbar"><a class="brand" href="index.html">Nexus<b>CRM</b></a>
<nav aria-label="Main"><a href="index.html">Overview</a><a href="sprint-03.html">Sprint 3</a><a href="sprint-06.html">Sprint 6</a><a href="risks.html">Risks</a><a href="retrospective.html">Retrospective</a></nav>
<a class="cta" href="{REPO}" target="_blank" rel="noopener">GitHub</a></header>
<div class="layout">
<aside class="rail" aria-label="Lifecycle documents"><details open><summary>All 18 documents</summary>{r}</details></aside>
<main>
{head}{inner}
<footer><span>NexusCRM is a self-directed portfolio case study. Company, team and data are illustrative.</span><span><a href="{REPO}" target="_blank" rel="noopener">GitHub</a> · <a href="https://mrunali121.github.io/" target="_blank" rel="noopener">Portfolio</a></span></footer>
</main>
</div>
</body>
</html>
"""


def pager(slug):
    i = ORDER.index(slug)
    a = f'<a href="{ORDER[i-1]}.html">&larr; {SLUG[ORDER[i-1]][2]}</a>' if i else '<a href="index.html">&larr; Overview</a>'
    b = f'<a href="{ORDER[i+1]}.html">{SLUG[ORDER[i+1]][2]} &rarr;</a>' if i < len(ORDER) - 1 else '<a href="index.html">Back to overview &rarr;</a>'
    return f'<div class="pager">{a}{b}</div>'


def pagehead(d):
    return f'<header class="pagehead"><div class="eyebrow">{d[6]} · Document {d[1]}</div><h1>{html.escape(d[3])}</h1><p>{d[4]}</p></header>'


def fix_links(body):
    def f(m):
        h = m.group(1)
        key = h.split("#")[0]
        key = re.sub(r"^(\.\./)+", "", key)
        if key in LINKS:
            return f'href="{LINKS[key]}"'
        if Path(key).name in LINKS:
            return f'href="{LINKS[Path(key).name]}"'
        if key.endswith((".png",)):
            return f'href="{Path(key).name}"'
        if key.endswith(".py"):
            return f'href="{REPO}/blob/main/{key}" target="_blank" rel="noopener"'
        return m.group(0)
    body = re.sub(r'href="([^"#][^"]*)"', f, body)
    body = re.sub(r'src="(?:\.\./)+([^"]+)"', r'src="\1"', body)
    return body


def md(path):
    t = (ROOT / path).read_text(encoding="utf-8")
    m = re.match(r"\s*#\s+(.*)\n", t)
    t = t[m.end():] if m else t
    return m.group(1) if m else "", markdown.markdown(t, extensions=["tables", "fenced_code", "sane_lists"])


def write(slug, title, inner, head, desc=""):
    (ROOT / f"{slug}.html").write_text(shell(slug, title, inner, head, desc), encoding="utf-8")


for d in DOCS:
    slug, _, _, title, lead, srcs, _ = d
    if srcs is None:
        continue
    parts = []
    for s in srcs:
        h1, body = md(s)
        if len(srcs) > 1:
            body = f"<h2>{html.escape(h1)}</h2>" + body
        parts.append(body)
    inner = "".join(parts)
    if slug == "roadmap":
        inner += '<figure class="fig"><a href="roadmap-chart.png" target="_blank" rel="noopener"><img src="roadmap-chart.png" alt="Roadmap chart: two releases across 18 weeks"></a><figcaption>Roadmap chart (generated by generate_charts.py)</figcaption></figure>'
    if slug == "sprints":
        inner += '<figure class="fig"><a href="release-velocity-chart.png" target="_blank" rel="noopener"><img src="release-velocity-chart.png" alt="Sprint velocity by release"></a><figcaption>Velocity by sprint (generated by generate_charts.py)</figcaption></figure>'
        inner += '<div class="two"><a class="chip" href="sprint-03.html"><i>10a</i><b>Sprint 3 in depth</b><span>A dependency risk that materialised</span></a><a class="chip" href="sprint-06.html"><i>10b</i><b>Sprint 6 in depth</b><span>A scope trade-off under pressure</span></a></div>'
    inner = '<div class="doc">' + fix_links(inner) + pager(slug) + "</div>"
    write(slug, title, inner, pagehead(d), lead)

# ---- backlog (interactive) ----
rows = list(csv.DictReader(open(ROOT / "07-product-backlog.csv", encoding="utf-8")))
tr = ""
for r in rows:
    pr = r["Priority (MoSCoW)"]
    k = "must" if pr.startswith("Must") else "should" if pr.startswith("Should") else "wont"
    st = r["Status"]
    tr += (f'<tr data-p="{k}" data-r="{html.escape(r["Release"])}"><td><code>{r["ID"]}</code></td><td>{html.escape(r["Epic"])}</td><td>{html.escape(r["User Story"])}</td>'
           f'<td><span class="pill {k}">{html.escape(pr)}</span></td><td>{r["Story Points"]}</td><td>{r["Release"]}</td><td>{r["Sprint"]}</td>'
           f'<td><span class="pill {"done" if st == "Done" else "wont"}">{st}</span></td></tr>')
pts = sum(int(r["Story Points"]) for r in rows if r["Release"] in ("R1", "R2"))
inner = ('<div class="doc"><div class="tools" role="group" aria-label="Filters">'
         '<button data-f="all" aria-pressed="true">All</button><button data-f="must" aria-pressed="false">Must</button><button data-f="should" aria-pressed="false">Should</button>'
         '<button data-f="wont" aria-pressed="false">Won\'t</button><button data-r="R1" aria-pressed="false">Release 1</button><button data-r="R2" aria-pressed="false">Release 2</button>'
         '<input id="q" type="search" placeholder="Search stories..." aria-label="Search stories"></div>'
         f'<p id="count" class="mono" style="font-size:13px;color:var(--mute)"></p><p>{pts} story points are planned across the two releases.</p>'
         '<table id="bl"><thead><tr><th>ID</th><th>Epic</th><th>Story</th><th>Priority</th><th>Pts</th><th>Release</th><th>Sprint</th><th>Status</th></tr></thead><tbody>' + tr + "</tbody></table>"
         '<p><a href="07-product-backlog.csv">Download the raw CSV</a></p>' + pager("backlog") + "</div>"
         '''<script>
(function(){var rows=[].slice.call(document.querySelectorAll('#bl tbody tr')),btn=[].slice.call(document.querySelectorAll('.tools button')),q=document.getElementById('q'),c=document.getElementById('count');
var st={p:'all',r:''};
function run(){var t=q.value.toLowerCase(),n=0;rows.forEach(function(r){var ok=(st.p==='all'||r.dataset.p===st.p)&&(!st.r||r.dataset.r===st.r)&&(!t||r.textContent.toLowerCase().indexOf(t)>-1);r.style.display=ok?'':'none';if(ok)n++});c.textContent=n+' of '+rows.length+' stories shown'}
btn.forEach(function(b){b.addEventListener('click',function(){if(b.dataset.f){st.p=b.dataset.f;st.r=''}else{st.r=st.r===b.dataset.r?'':b.dataset.r;st.p='all'}
btn.forEach(function(x){x.setAttribute('aria-pressed',String((x.dataset.f&&x.dataset.f===st.p&&!st.r)||(x.dataset.r&&x.dataset.r===st.r)))});run()})});
q.addEventListener('input',run);run()})();
</script>''')
write("backlog", "Product Backlog", inner, pagehead(SLUG["backlog"]), SLUG["backlog"][4])

# ---- index ----
ph = ""
for i, (name, sub) in enumerate(PHASES, 1):
    chips = "".join(f'<a class="chip" href="{d[0]}.html"><i>{d[1]}</i><b>{d[2]}</b><span>{d[4].split(".")[0]}.</span></a>' for d in DOCS if d[6] == name)
    ph += f'<div class="phase"><div><h3>{i}. {name}</h3><small>{sub}</small></div><div class="chips">{chips}</div></div>'
home = f"""
<section class="hero">
<div class="eyebrow">Project management case study · hybrid Waterfall + Scrum</div>
<h1>An 18-week CRM build, run <em>end to end</em></h1>
<p class="lead">NexusCRM replaces a company's legacy contact database and sales spreadsheets. This case study walks the whole project lifecycle, from business case to retrospective, with 18 documents and two real moments of judgment.</p>
<div class="btns"><a class="btn p" href="business-case.html">Start at the business case &rarr;</a><a class="btn g" href="sprint-03.html">Jump to the decisions</a></div>
</section>
<div class="stats"><div><b>18</b><span>weeks, incl. 2-week buffer</span></div><div><b>2</b><span>releases shipped on schedule</span></div><div><b>9</b><span>cross-functional team</span></div><div><b>0</b><span>critical bugs at go-live</span></div></div>
<section class="sect"><h2>Two moments of judgment</h2><p class="sub">Most of the project runs to plan. These two show what the PM actually did when it did not.</p>
<div class="two">
<div class="decision"><div class="eyebrow">Sprint 3 · Risk</div><h3>A dependency risk becomes real</h3><p>A shared component causes a 2-day slip. Work is re-ordered in parallel, the slack absorbs it, and the Sponsor hears before the sprint review.</p><a href="sprint-03.html">Read the story &rarr;</a></div>
<div class="decision"><div class="eyebrow">Sprint 6 · Trade-off</div><h3>Scope versus a legal deadline</h3><p>An unplanned licensing review threatens a Should feature. The trade-off goes to the Sponsor, the feature moves one sprint, and the roadmap is unaffected.</p><a href="sprint-06.html">Read the story &rarr;</a></div>
</div></section>
<section class="sect"><h2>The lifecycle in five phases</h2><p class="sub">Every card opens its own page.</p><div class="phases">{ph}</div></section>
<section class="sect"><h2>Why a hybrid approach</h2><p>An enterprise build inside an existing company needs a business case and charter to secure budget and executive alignment first. So initiation and planning follow Waterfall-style governance, then delivery runs as Scrum in two-week sprints. This blended model is common in German engineering and enterprise software environments.</p></section>
<section class="sect"><h2>Outcome</h2><p>Both releases shipped on schedule, with no critical bugs at either go-live and a 1.8% post-migration duplicate rate against a target below 3%.</p></section>
"""
write("index", "A Full-Lifecycle PM Case Study", home, "", "NexusCRM: an 18-week hybrid Waterfall and Scrum project, from business case to retrospective.")
print("Built", len(DOCS) + 1, "pages")
