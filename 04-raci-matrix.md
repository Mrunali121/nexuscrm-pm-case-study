# RACI Matrix — NexusCRM Platform

**R** = Responsible · **A** = Accountable · **C** = Consulted · **I** = Informed

| Deliverable / Activity | PM | Eng Director | Backend Devs | Frontend Dev | Design | QA | DevOps | Data Privacy Officer | Sponsor |
|---|---|---|---|---|---|---|---|---|---|
| Business case | R | C | I | I | I | I | I | C | A |
| Project charter | R | C | I | I | I | I | I | I | A |
| Stakeholder analysis | A/R | C | I | I | I | I | I | I | I |
| Requirements gathering | A/R | C | C | C | C | C | I | C | I |
| WBS & scheduling | A/R | C | C | C | I | I | I | I | I |
| Data model / architecture design | I | A | R | C | I | I | C | C | I |
| Sprint planning | R | I | C | C | C | C | I | I | I |
| Feature development | I | A | R | R | C | I | I | I | I |
| UI/UX design | C | I | I | C | A/R | I | I | I | I |
| QA test planning & execution | I | I | C | C | I | A/R | I | I | I |
| Risk & dependency register | A/R | C | C | C | I | C | C | C | I |
| Data migration execution | R | A | R | I | I | C | C | C | I |
| UAT coordination | A/R | I | C | C | I | R | I | I | C |
| Security / GDPR audit | C | C | C | I | I | C | R | A | I |
| Go-live checklist & cutover | A/R | C | C | C | I | C | R | C | I |
| Status reporting | A/R | I | I | I | I | I | I | I | I |
| Go/no-go decision (per release) | R | C | I | I | I | C | I | C | A |
| Retrospective | R | C | C | C | C | C | C | I | I |

## Notes
- **Security/GDPR audit** is the one deliverable where the Data Privacy Officer
  holds Accountable rather than the PM — this reflects that go-live cannot proceed
  without their independent sign-off, not a delegation of PM ownership.
- **Go/no-go decisions** sit with the Sponsor as Accountable at both release
  boundaries; the PM is Responsible for preparing the readiness assessment that
  informs the decision.
