# Project Charter — NexusCRM Platform

## 1. Project Overview
NexusCRM is an internal B2B SaaS customer management platform replacing Meridian
Software's legacy contact database and spreadsheet-based sales tracking. Built and
delivered as two releases over 16 weeks by a 9-person cross-functional team.

## 2. Objectives
- Replace the legacy contact database and sales spreadsheets with a single system
  of record for customer and deal data.
- Cut monthly reporting effort from ~6 person-hours to under 1 (via live dashboards).
- Reduce duplicate contact records from ~18% to under 3% via a guided data migration.
- Ship a foundation that supports a future email and Zapier integration layer.
- Meet GDPR requirements as data controller for EU customer records (data
  minimization, access logging, right-to-erasure support).

## 3. Scope

**In scope:**
- Release 1: Auth & permissions, contact/account management, deal pipeline, core admin
- Release 2: Reporting dashboards, email integration, Zapier integration, legacy data migration tool

**Out of scope (explicitly deferred):**
- Customer-facing self-service portal
- Mobile native app (responsive web only for MVP)
- Multi-currency support (single-currency for initial rollout)
- Any future external productization (flagged in Business Case as a separate initiative)

## 4. Team & Governance

| Role | Count |
|---|---|
| Project Manager | 1 |
| Backend Developer | 2 |
| Frontend Developer | 1 |
| UX Designer | 1 |
| QA Engineer | 2 |
| DevOps/SRE | 1 |
| **Total** | **9** (plus part-time Data Privacy Officer consultation) |

**Governance:** Steering Committee (Sponsor + Engineering Director + Head of
Customer Success) meets at each release boundary for go/no-go decisions. PM reports
weekly status to Sponsor; escalations follow the path defined in the RACI matrix.

## 5. Milestones

| Milestone | Target |
|---|---|
| Charter approved | Week 0 |
| Release 1 (Core CRM) live internally | Week 8 |
| Release 2 (Reporting + Integrations) live internally | Week 16 |
| Legacy system decommissioned | Week 18 (2-week parallel-run buffer) |

## 6. Budget
~420 person-days across the 16-week build, within existing team capacity — no
external contractor spend, aside from an external GDPR/security audit ahead of
Release 2 go-live (see [Dependency Management](12-dependency-management.md)).

## 7. Success Criteria
| Metric | Target |
|---|---|
| Both releases shipped on schedule | Week 8 / Week 16 |
| Duplicate contact rate post-migration | < 3% |
| Monthly reporting effort | < 1 person-hour |
| Critical bugs open at go-live | 0 |
| GDPR/security audit | Passed prior to Release 2 go-live |

## 8. Constraints & Assumptions
- Fixed team, no additional hires during the project.
- EU data residency is mandatory — hosting stays on Meridian's existing EU infrastructure.
- Legacy system must remain operational in parallel until data migration is verified.

## 9. Approval
| Role | Sign-off |
|---|---|
| Sponsor (VP Sales) | ✅ |
| Engineering Director | ✅ |
| Project Manager | ✅ |
