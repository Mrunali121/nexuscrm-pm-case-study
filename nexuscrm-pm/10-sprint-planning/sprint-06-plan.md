# Sprint 6 Planning — Report Exports & Performance Views

**Duration:** Weeks 11–12
**Sprint Goal:** Leadership can export reports and view rep/team-level performance.

## Committed Stories
| ID | Story | Points | Owner |
|---|---|---|---|
| NX-16 | Report export (CSV, PDF) | 5 | Backend Dev A |
| NX-17 | Rep-level and team-level performance views | 5 | Frontend Dev + Backend Dev B |

**Committed points: 10** (lighter sprint by design — team capacity partly reserved
for the upcoming external security audit prep ahead of Sprint 7)

## Scope Trade-off Under Deadline Pressure
Mid-sprint, PDF export turned out to require a third-party rendering library that
introduced a licensing review — Meridian's legal team needed 5 business days to
clear it, which didn't fit inside the sprint.

**PM decision process:**
1. Assessed options: (a) delay the whole sprint goal for legal clearance, (b) ship
   CSV export only and defer PDF to Sprint 8 buffer, (c) build a lower-quality
   in-house PDF export to avoid the licensing question entirely.
2. Consulted Engineering Director: option (c) was rejected — technical debt for a
   Should-priority feature wasn't worth it.
3. Brought (a) vs (b) to the Sponsor with the trade-off stated plainly: CSV covers
   the actual reporting need leadership raised in requirements workshops; PDF was
   a nice-to-have add-on.
4. Sponsor chose (b). PDF export moved to the Sprint 8 buffer, contingent on legal
   clearance landing in time — it did, and PDF export shipped in Sprint 8 as planned.

## Outcome
CSV export and both performance views shipped on schedule. PDF export shipped one
sprint later with zero impact on the Release 2 date, because it was never on the
critical path once deferred.

## Lesson carried forward
Third-party library licensing checks are now a standing item at sprint planning
whenever a new dependency is introduced, not something discovered mid-sprint —
captured as an action item in the [Retrospective](../16-retrospective.md).
