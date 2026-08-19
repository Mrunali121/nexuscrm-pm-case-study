# Business Case — NexusCRM Platform

**Company:** Meridian Software (B2B SaaS vendor)
**Prepared by:** Project Manager
**Audience:** Executive Steering Committee

## 1. Problem Statement
Meridian's existing customer management tooling is a patchwork of a legacy in-house
contact database and three disconnected spreadsheets used by Sales and Customer
Success. This causes:
- Duplicate and stale customer records (est. 18% of contact records are duplicates)
- No single view of deal pipeline across the 14-person sales team
- Manual, error-prone monthly reporting to leadership (avg. 6 person-hours/month)
- Inability to integrate with email or third-party tools, blocking a planned
  Customer Success automation initiative

## 2. Market Opportunity
Customer interviews (9 existing accounts) and a competitive review of 4 comparable
SMB CRM products confirmed demand for a lightweight, integration-friendly CRM as
both an internal tool and — pending internal rollout success — a potential future
customer-facing product line.

## 3. Options Considered

| Option | Pros | Cons |
|---|---|---|
| A — Buy an existing CRM (e.g. HubSpot, Pipedrive) | Fast to deploy, proven | Recurring per-seat cost at scale, limited fit with internal data model, GDPR data residency review required for any EU customer data touched by a third party |
| B — Build NexusCRM in-house | Full control of data residency (important given GDPR and EU customer base), extensible foundation for future product line, one-time investment | Requires internal engineering capacity, longer time to first value |
| C — Do nothing | No cost | Status quo problems compound; blocks the CS automation initiative already committed to leadership |

**Recommendation:** Option B. The one-time build cost is recovered within ~14 months
via reduced reporting overhead and reclaimed sales admin time, and it removes the
GDPR data-residency question entirely by keeping customer data in Meridian's
existing EU-hosted infrastructure.

## 4. High-Level Cost-Benefit
| | Estimate |
|---|---|
| One-time build cost (team time, 16 weeks) | ~420 person-days |
| Ongoing hosting/maintenance | Comparable to current legacy DB hosting |
| Annual savings (reporting time, reduced duplicate cleanup, no per-seat licensing) | ~70 person-days/year |
| Payback period | ~14 months |

## 5. Strategic Fit
Directly enables the CS automation initiative already on the FY roadmap, and
establishes a data foundation that could later be productized — flagged to the
Steering Committee as a possible Phase 3 (post-MVP) direction, explicitly out of
scope for this project.

## 6. Recommendation
Approve NexusCRM as a 16-week, two-release internal build, governed by the attached
[Project Charter](02-project-charter.md).
