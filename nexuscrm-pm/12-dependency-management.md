# Dependency Management — NexusCRM Platform

## Internal Dependencies (cross-team / cross-sprint)

| ID | Dependency | Between | Risk if delayed | Tracking |
|---|---|---|---|---|
| D-01 | Data model design must be finalized before contact/deal stories can start | Design phase → Sprint 1–3 | Rework across multiple sprints | Locked at end of Design phase (Week 3), change-controlled after |
| D-02 | Shared WebSocket service (real-time updates) used by both pipeline UI and future audit logging | Sprint 3 (pipeline) ↔ Sprint 4 (audit log) | Blocks pipeline drag-and-drop feature | Flagged at Sprint 3 planning; materialized as Issue I-01, resolved via reordering |
| D-03 | Reporting engine (Sprint 5) depends on deal/contact data model being stable from Release 1 | Release 1 → Release 2 | Reporting queries built against a moving schema | Data model frozen at Release 1 go-live; any Release 2 schema change goes through change control |
| D-04 | Email integration (Sprint 7) and Zapier integration (Sprint 8) both consume the same API layer | Sprint 7 → Sprint 8 | Zapier work blocked if API contract changes late | API contract designed upfront (WBS 3.3) and versioned per NFR-12 |

## External Dependencies

| ID | Dependency | Vendor/Party | Risk if delayed | Tracking |
|---|---|---|---|---|
| D-05 | Email provider API sandbox access for integration development | Email API vendor | Sprint 7 work blocked at the start | Requested in Week 8, confirmed by Week 9 — built in as a buffer before Sprint 7 start |
| D-06 | External GDPR/security audit firm availability | Third-party audit firm | Release 2 go-live blocked (audit is a hard gate per NFR-07) | Booked in Week 6, scheduled for Week 15 with 3-week buffer before go-live |
| D-07 | Legal review of third-party PDF rendering library license | Meridian Legal | Report export feature delayed | Materialized as Issue I-02; resolved via scope deferral rather than blocking the sprint |
| D-08 | Legacy database export access for migration tooling | Internal IT/DevOps | Data migration development blocked | Access granted in Week 9, ahead of Sprint 8 need |

## How dependencies are managed
- Every dependency is logged at the point it's identified — usually at sprint
  planning or design — with an owner and a "risk if delayed" statement, not just
  a date.
- Dependencies scoring as high-impact (D-02, D-03, D-06) get an explicit callout
  at every sprint planning session until resolved, cross-referenced with the
  [Risk & Issue Register](11-risk-issue-register.md).
- External dependencies (vendor/legal/audit) are booked with deliberate buffer
  time rather than scheduled back-to-back against the date they're needed —
  this buffer is what absorbed D-06 and D-07 without affecting the roadmap.
