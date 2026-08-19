# Risk & Issue Register — NexusCRM Platform

Risks are potential future problems; issues are risks (or new problems) that have
already occurred. Reviewed at every sprint planning session.

## Risk Register

| ID | Risk | Likelihood | Impact | Score | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| R-01 | Shared platform components create hidden cross-sprint dependencies | Medium (3) | High (4) | 12 | Explicit dependency mapping per component at sprint planning (see Dependency Register) | PM | Active — materialized in Sprint 3 as I-01 |
| R-02 | Third-party libraries introduce unreviewed licensing constraints | Medium (3) | Medium (3) | 9 | Licensing check added as a standing sprint-planning item | Eng Director | Active — materialized in Sprint 6 as I-02 |
| R-03 | External GDPR/security audit finds a blocking issue ahead of Release 2 | Medium (3) | High (4) | 12 | Audit scheduled with buffer time in Sprint 8/Week 15, not immediately before go-live | Data Privacy Officer | Mitigated — passed with 2 minor (non-blocking) findings |
| R-04 | Legacy data migration produces higher-than-expected duplicate rate | Medium (3) | High (4) | 12 | Dry-run migration mode (NX-18) built specifically to catch this before committing | PM | Closed — dry-run flagged and resolved a mapping error pre-commit |
| R-05 | Sales team resists adopting NexusCRM, reverting to spreadsheets | Low (2) | High (4) | 8 | Sales power-users embedded from requirements stage; UAT run with real users, not just QA | PM | Closed — UAT feedback positive, adoption tracked post-launch |
| R-06 | 9-person team capacity insufficient for 16-week two-release scope | Medium (3) | High (4) | 12 | Must/Should/Could prioritization locked at charter stage so scope can flex without late renegotiation | PM | Mitigated — Won't-priority items correctly stayed in backlog, no deadline slip |
| R-07 | Email integration API rate limits affect two-way sync at scale | Low (2) | Medium (3) | 6 | Load-tested in Sprint 7 QA pass against expected daily volume | QA | Closed — passed load test |

## Issue Log (materialized risks / new problems)

| ID | Issue | Linked Risk | Impact | Resolution | Status |
|---|---|---|---|---|---|
| I-01 | WebSocket service delay blocked drag-and-drop pipeline feature | R-01 | 2-day slip on one story, absorbed by Sprint 4 slack | Reordered sprint work in parallel; no Release 1 date impact | Resolved (Sprint 3) |
| I-02 | PDF export library required unplanned legal licensing review | R-02 | Feature deferred one sprint | Sponsor-approved scope trade-off (CSV first, PDF deferred) | Resolved (Sprint 6) |

## Scoring key
Likelihood / Impact: 1 (Low) – 4 (High). Score ≥ 12 reviewed every sprint planning
session; 6–11 reviewed at sprint review; < 6 monitored only.
