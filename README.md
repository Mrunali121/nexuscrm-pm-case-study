# NexusCRM — B2B SaaS Customer Management Platform
### A Full-Lifecycle Project Management Case Study

**Role:** Project Manager (simulated project)
**Methodology:** Hybrid — Waterfall-style initiation & planning, Scrum execution (2-week sprints)
**Duration:** 18 weeks (16-week build across 2 releases + 2-week parallel-run buffer)
**Team:** 9 people (PM, 2 Backend Dev, 1 Frontend Dev, 1 Designer, 2 QA, 1 DevOps, plus part-time Data Privacy Officer)

## Live website
Open `index.html` through GitHub Pages: https://mrunali121.github.io/NexusCRM-PM/ . Every document has its own page, and the backlog page has filters. Rebuild with `pip install markdown` then `python build_site.py`.

## About this repository

This is a flagship-depth portfolio project simulating a realistic internal B2B
SaaS build: **NexusCRM**, a customer management platform built to replace a
company's legacy contact database and spreadsheet-based sales tracking.

Unlike a typical Agile-only exercise, this case study runs the **entire PM
lifecycle** — from business case through go-live and retrospective — the way a
mid-to-senior PM would actually run a multi-release enterprise software project,
including GDPR/compliance considerations relevant to operating in the EU.

## Project summary

| | |
|---|---|
| **Product** | NexusCRM — internal B2B CRM (contacts, deal pipeline, reporting, integrations) |
| **Releases** | 2 — Core CRM (Week 8), Reporting & Integrations (Week 16) |
| **Team size** | 9 (cross-functional) |
| **Business goal** | Replace legacy tooling, cut reporting effort from 6 hrs/month to <1 hr, meet GDPR obligations |
| **Outcome** | Both releases shipped on schedule, 0 critical bugs at either go-live, 1.8% post-migration duplicate rate (target <3%) |

## Full lifecycle documentation

| Phase | Document | What it shows |
|---|---|---|
| Business case | [`01-business-case.md`](01-business-case.md) | Problem, options considered, cost-benefit, recommendation |
| Charter | [`02-project-charter.md`](02-project-charter.md) | Scope, objectives, team, milestones, success criteria |
| Stakeholders | [`03-stakeholder-analysis.md`](03-stakeholder-analysis.md) | Stakeholder register + power/interest grid |
| Governance | [`04-raci-matrix.md`](04-raci-matrix.md) | Ownership across 18 deliverables, 9 roles |
| Requirements | [`05-requirements/`](05-requirements) | Functional (18) + non-functional (12) requirements |
| Scheduling | [`06-wbs.md`](06-wbs.md) | 8-phase work breakdown structure, Week 0–18 |
| Backlog | [`07-product-backlog.csv`](07-product-backlog.csv) | 25 stories, story-pointed, MoSCoW, release-mapped |
| Roadmap | [`08-roadmap.md`](08-roadmap.md) · [chart](roadmap-chart.png) | Two-release roadmap with sprint-level breakdown |
| Release plan | [`09-release-plan.md`](09-release-plan.md) | Scope, rollout approach, and rollback plan per release |
| Sprint plans | [`10-sprint-planning/`](10-sprint-planning) | All 8 sprints, with 2 documented in full narrative depth |
| Risk & issues | [`11-risk-issue-register.md`](11-risk-issue-register.md) | 7 risks + 2 materialized issues, scored and resolved |
| Dependencies | [`12-dependency-management.md`](12-dependency-management.md) | 4 internal + 4 external dependencies, tracked to closure |
| Status reports | [`13-status-reports/`](13-status-reports) | 3 real snapshots — mid-build, release transition, pre-launch |
| UAT | [`14-uat-plan.md`](14-uat-plan.md) | Entry/exit criteria, 10 test scenarios, severity classification |
| Go-live | [`15-go-live-checklist.md`](15-go-live-checklist.md) | Cutover checklist + rollback plan |
| Retrospective | [`16-retrospective.md`](16-retrospective.md) | What worked, what didn't, owned action items |
| Charts | [`generate_charts.py`](generate_charts.py) | The Python script producing both charts above — reproducible, not static images |
| Live site | [`index.html`](index.html) + 18 pages, [`site.css`](site.css), [`build_site.py`](build_site.py) | Multi-page website generated from these documents, published via GitHub Pages |

## The two decisions this case study is built around

Most of this repo follows a clean, on-schedule execution — because that's what
good planning produces. But two moments are documented in full narrative depth
because they show actual PM judgment under pressure, not just a template filled in:

1. **[Sprint 3 — a dependency risk that materialized](10-sprint-planning/sprint-03-plan.md).**
   A shared platform component caused a real 2-day slip. The response — reorder
   work in parallel, absorb it in planned slack, tell the Sponsor before the
   sprint review rather than after — is the difference between a risk register
   that's decorative and one that's actually used.

2. **[Sprint 6 — a scope trade-off under deadline pressure](10-sprint-planning/sprint-06-plan.md).**
   An unplanned legal licensing review threatened a Should-priority feature.
   Rather than absorbing the delay silently or cutting corners technically, the
   trade-off was surfaced to the Sponsor explicitly, with the lower-priority
   feature deferred — and delivered one sprint later with zero roadmap impact.

Both are cross-referenced through the risk register, dependency log, status
reports, and retrospective — the way they'd actually thread through real project
artifacts, not just live in one document.

## Why the hybrid methodology
Enterprise B2B SaaS builds inside an existing company rarely run pure Scrum from
day one — there's usually a business case and charter to secure budget and
executive alignment first. This case study reflects that reality: Waterfall-style
governance for initiation/planning, then Scrum for execution, which is also the
blended approach most commonly expected in traditional German engineering and
enterprise software environments alongside pure-Agile tech roles.

---
*This is a self-directed portfolio project built to demonstrate full-lifecycle PM
methodology across both Agile and traditional governance practices. Company, team,
and product are illustrative.*
