# Sprint 3 Planning — Deal Pipeline

**Duration:** Weeks 6–7
**Sprint Goal:** Sales reps can manage deals through a kanban pipeline with
real-time stage changes.

## Committed Stories
| ID | Story | Points | Owner |
|---|---|---|---|
| NX-9 | Kanban pipeline view | 8 | Frontend Dev |
| NX-10 | Drag-and-drop stage changes, no reload | 8 | Frontend Dev + Backend Dev A |
| NX-11 | Deal value roll-ups per stage/rep | 5 | Backend Dev B |

**Committed points: 21**

## Dependency Risk That Materialized
This sprint depended on a WebSocket-based real-time update service that Backend
Dev A was also responsible for as a shared platform component — a dependency
flagged in the [Dependency Register](../12-dependency-management.md) (D-02) at
sprint planning.

**What happened:** the WebSocket service took 3 days longer than estimated,
because it needed to also support the audit-logging requirement (NX-14) coming in
Sprint 4 — an interaction the team hadn't fully scoped at planning time.

**PM response:**
1. Convened Backend Dev A, Frontend Dev, and Engineering Director on Day 5 to
   assess real impact rather than letting it run silently.
2. Identified that NX-11 (deal value roll-ups) did not depend on the WebSocket
   service and could proceed in parallel — reordered Backend Dev B's work to keep
   the team fully utilized while the blocker was resolved.
3. Renegotiated: NX-10 completed 2 days into Sprint 4 instead of end of Sprint 3,
   with the Sponsor informed in the weekly status report rather than surprised at
   the sprint review.

## Outcome
Sprint goal substantially met — pipeline view and value roll-ups shipped on time;
drag-and-drop stage changes landed 2 days into Sprint 4 with no impact on the
Release 1 date, because Sprint 4 had planned slack that absorbed it.

## Lesson carried forward
Shared platform components (like the WebSocket service) are now flagged explicitly
at sprint planning with their full list of downstream consumers, not just the
current sprint's — this gap is captured as an action item in the
[Retrospective](../16-retrospective.md).
