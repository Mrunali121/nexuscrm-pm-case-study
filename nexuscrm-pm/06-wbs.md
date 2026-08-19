# Work Breakdown Structure — NexusCRM Platform

WBS coded to 3 levels. Time-phased across Weeks 0–18 (16-week build + 2-week
parallel-run buffer before legacy decommission).

```
1. Initiation                                                   [Week 0]
   1.1 Business case & approval
   1.2 Project charter
   1.3 Stakeholder analysis

2. Planning                                                      [Weeks 1–2]
   2.1 Requirements workshops (Sales, CS, Engineering)
   2.2 Functional & non-functional requirements sign-off
   2.3 RACI & governance model
   2.4 Product backlog creation & prioritization
   2.5 Release plan & roadmap

3. Design                                                        [Weeks 2–3]
   3.1 Data model / architecture design
   3.2 UX wireframes & prototype
   3.3 API contract design (supports Release 2 integrations)

4. Release 1 — Core CRM Build                                    [Weeks 3–8]
   4.1 Sprint 1 — Auth, permissions, environment setup
   4.2 Sprint 2 — Contact & account management
   4.3 Sprint 3 — Deal pipeline (kanban, stage logic)
   4.4 Sprint 4 — Core admin, bulk import, hardening

5. Release 1 — Testing & Launch                                  [Week 8]
   5.1 Internal UAT (Sales power-users)
   5.2 Bug triage & fixes
   5.3 Go/no-go review
   5.4 Release 1 go-live (internal rollout)

6. Release 2 — Reporting & Integrations Build                    [Weeks 9–14]
   6.1 Sprint 5 — Dashboard & reporting engine
   6.2 Sprint 6 — Report export, rep/team views
   6.3 Sprint 7 — Email integration
   6.4 Sprint 8 — Zapier integration, data migration tool

7. Release 2 — Testing & Launch                                  [Weeks 15–16]
   7.1 External security/GDPR audit
   7.2 UAT (Sales + Customer Success)
   7.3 Legacy data migration (dry-run, then committed)
   7.4 Go/no-go review
   7.5 Release 2 go-live

8. Closure                                                        [Weeks 17–18]
   8.1 Parallel-run monitoring (legacy system kept live as fallback)
   8.2 Legacy system decommission
   8.3 Project retrospective
   8.4 Handover to BAU support
```

See [Product Backlog](07-product-backlog.csv) for the story-level breakdown feeding
sections 4 and 6, and [Sprint Planning](10-sprint-planning/) for sprint-level detail.
