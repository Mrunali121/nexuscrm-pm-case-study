# Roadmap — NexusCRM Platform

16-week build across two releases, followed by a 2-week parallel-run buffer before
the legacy system is decommissioned.

## Release 1 — Core CRM (Weeks 3–8)
**Goal:** Replace the legacy contact database and spreadsheets with a working
system of record for contacts, accounts, and deal pipeline.

| Sprint | Weeks | Focus |
|---|---|---|
| Sprint 1 | 3–4 | Auth, permissions, environment & CI/CD setup |
| Sprint 2 | 5–6 | Contact & account management |
| Sprint 3 | 6–7 | Deal pipeline (kanban board, stage logic) |
| Sprint 4 | 7–8 | Admin tools, bulk import, audit logging, hardening |

**Release 1 exit criteria:** Internal UAT passed, 0 critical bugs, Sponsor go/no-go approved.

## Release 2 — Reporting & Integrations (Weeks 9–16)
**Goal:** Give leadership live reporting and connect NexusCRM to email and
downstream automation via Zapier, plus migrate all legacy data.

| Sprint | Weeks | Focus |
|---|---|---|
| Sprint 5 | 9–10 | Reporting engine & live dashboard |
| Sprint 6 | 11–12 | Report exports, rep/team performance views |
| Sprint 7 | 13–14 | Email integration, GDPR erasure workflow |
| Sprint 8 | 15–16 | Zapier integration, data migration tool, backups |

**Release 2 exit criteria:** External security/GDPR audit passed, UAT passed
(Sales + Customer Success), 0 critical bugs, Sponsor go/no-go approved.

## Post-Release (Weeks 17–18)
- Parallel-run: legacy system stays live as fallback while NexusCRM is monitored
  under real usage.
- Legacy system decommissioned once migration is verified stable.

## Explicitly deferred (not on this roadmap)
- Customer-facing self-service portal
- Native mobile app
- Multi-currency support
- Any external productization decision (owned by a separate future initiative)

See [Release Plan](09-release-plan.md) for detailed scope and success criteria per
release, and [Roadmap Chart](roadmap-chart.png) for the visual timeline.
