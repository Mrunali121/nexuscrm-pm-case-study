# Stakeholder Analysis — NexusCRM Platform

## Stakeholder Register

| Stakeholder | Role | Interest | Power | Engagement Strategy |
|---|---|---|---|---|
| VP Sales | Sponsor | High — owns the business outcome | High | Weekly status report; decision authority on scope trade-offs |
| Engineering Director | Steering Committee | High — resourcing & technical risk | High | Release-boundary go/no-go meetings; escalation path for technical blockers |
| Head of Customer Success | Steering Committee | High — depends on this for CS automation initiative | High | Consulted on Release 2 reporting/integration requirements |
| Data Privacy Officer | Compliance advisor | Medium — GDPR compliance sign-off | High (veto on go-live) | Consulted at data model design and before each release go-live |
| Sales Team (14 people) | End users | High — daily tool | Low | Represented via 2 Sales power-users in requirements workshops and UAT |
| Customer Success Team | End users | Medium — reporting consumers | Low | Included in UAT for Release 2 reporting features |
| IT/DevOps | Infrastructure owner | Medium — hosting & security | Medium | Involved from Sprint 1 for environment setup; owns go-live checklist items |
| Beta Customer Advisory Group (3 external accounts) | Informal feedback source | Low — informational only | Low | Informed post-launch; no formal engagement during build |

## Power/Interest Grid

| | **Low Interest** | **High Interest** |
|---|---|---|
| **High Power** | IT/DevOps *(monitor, keep satisfied)* | VP Sales, Engineering Director, Data Privacy Officer *(manage closely)* |
| **Low Power** | Beta Customer Advisory Group *(monitor)* | Sales Team, Customer Success Team *(keep informed, involve in UAT)* |

## Key Engagement Decisions
- The **Data Privacy Officer** sits in the "manage closely" quadrant despite not
  being part of daily delivery — their sign-off is a hard gate before either
  release can go live, so they're looped in at design time, not just at the end.
- **Sales Team** power-users were embedded in requirements workshops rather than
  only consulted at UAT, since early input from actual daily users caught several
  workflow assumptions that would have failed adoption post-launch (see
  [Requirements](05-requirements/functional-requirements.md), FR-09).
