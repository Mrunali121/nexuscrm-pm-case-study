# Project Retrospective — NexusCRM Platform

**Format:** Start / Stop / Continue, run at project close (Week 18) with the full
9-person team plus the Data Privacy Officer.

## What went well
- Locking Must/Should/Could priorities at the charter stage (R-06 mitigation) meant
  scope trade-offs during the project — like the PDF export deferral in Sprint 6 —
  were fast, low-drama decisions instead of late renegotiations.
- Embedding Sales power-users from requirements workshops through UAT caught real
  workflow issues early (FR-09, drag-and-drop performance) and drove strong Day-1
  adoption — 14/14 users active with the spreadsheet workflow fully retired within
  2 weeks of Release 1.
- Booking external dependencies (audit firm, legal review) with deliberate buffer
  time meant neither one caused a schedule slip, even though both surfaced
  real issues (I-01, I-02, and the audit's minor findings).
- Weekly status reports with explicit risk/issue callouts kept the Sponsor and
  Steering Committee informed without needing extra ad-hoc meetings.

## What didn't go well
- Shared platform components (like the WebSocket service behind Sprint 3) weren't
  mapped against *all* their downstream consumers at the time they were built —
  only found the audit-logging interaction reactively, causing Issue I-01.
- Third-party library licensing wasn't a standing check at sprint planning, which
  meant the PDF export licensing issue (I-02) was discovered mid-sprint rather
  than anticipated.
- Release 2's UAT group (Customer Success) was brought in later than Sales — in
  hindsight, earlier CS involvement during Sprint 5–6 requirements refinement
  could have caught reporting-view feedback sooner.

## Action items
| Action | Owner | Status |
|---|---|---|
| Map all downstream consumers for any shared platform component before it's built, not just the current sprint's | PM + Eng Director | Adopted as a standing design-phase step |
| Add third-party licensing check as a standing sprint-planning item whenever a new dependency is introduced | PM | Adopted |
| Bring secondary user groups (like CS) into requirements refinement at the same stage as primary users, not just at UAT | PM | Adopted for next project |
| Keep the "buffer time on external dependencies" practice — it protected the schedule twice | PM | Carried forward as standard practice |

## Outcome
Both releases shipped on schedule (Week 8, Week 16). 0 critical bugs at either
go-live. Duplicate contact rate came in at 1.8% against a 3% target. Legacy system
decommissioned cleanly in Week 18 with no rollback needed.
