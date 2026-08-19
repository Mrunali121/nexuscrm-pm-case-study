# Status Report — Week 7 (Release 1, Sprint 3)

**Overall status:** 🟡 On track, one active dependency risk

## Summary
Sprint 3 is progressing but has hit the WebSocket dependency issue flagged at
planning (see Risk R-01 / Issue I-01). Impact is contained — reordering work in
parallel means Release 1's Week 8 date is not at risk.

## Progress this week
- NX-9 (kanban pipeline view): complete
- NX-11 (deal value roll-ups): complete, moved up in sequence to keep Backend Dev B utilized
- NX-10 (drag-and-drop stage changes): blocked on shared WebSocket service; will slip ~2 days into Sprint 4

## Decisions made
- Reordered Sprint 3 work so NX-11 proceeded in parallel while the WebSocket
  blocker was resolved, rather than leaving capacity idle.

## Risks / issues
- **I-01 (new):** WebSocket service delay, linked to R-01. Contained — absorbed by
  Sprint 4's planned slack, no Release 1 date impact expected.

## Metrics
| Metric | Target | Current |
|---|---|---|
| Release 1 date | Week 8 | On track |
| Sprint 3 velocity | 21 pts | 13 pts done, 8 pts rolling into Sprint 4 |
| Open critical bugs | 0 | 0 |

## Next week
Sprint 3 close-out, Sprint 4 planning (admin tools, bulk import, audit logging,
plus the 2-day carryover of NX-10).

---
*Distributed to: Sponsor, Engineering Director, Head of Customer Success*
