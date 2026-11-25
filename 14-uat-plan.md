# UAT Plan — NexusCRM Platform

## Purpose
Validate that NexusCRM meets real-world business needs from the perspective of
actual end users, ahead of each release go-live decision.

## Scope
- **Release 1 UAT:** Sales team (2 power-users + 1 sales manager)
- **Release 2 UAT:** Sales team (same group) + Customer Success (2 users)

## Entry Criteria
- All Must-priority backlog items for the release are complete and deployed to staging
- 0 open critical bugs from internal QA
- Test scenarios reviewed and approved by the PM

## Exit Criteria
- 100% of Must-priority test scenarios pass
- ≥ 90% of Should-priority test scenarios pass, with any failures logged and
  triaged as either fix-before-launch or accepted-and-deferred by the Sponsor
- 0 open critical or high-severity defects

## Test Scenarios (representative sample)

| ID | Scenario | Priority | Release |
|---|---|---|---|
| UAT-01 | Create a new contact, verify duplicate-detection warning triggers correctly | Must | R1 |
| UAT-02 | Move a deal through all pipeline stages via drag-and-drop with no reload | Must | R1 |
| UAT-03 | Deactivate a user and confirm their historical activity log is preserved | Must | R1 |
| UAT-04 | Bulk import 200 contacts via CSV with field mapping | Should | R1 |
| UAT-05 | View live pipeline dashboard and confirm figures match manual spot-check | Must | R2 |
| UAT-06 | Export a report as PDF and confirm formatting is usable for a leadership deck | Should | R2 |
| UAT-07 | Send and receive an email from within a contact record, confirm it logs to the timeline | Must | R2 |
| UAT-08 | Trigger a Zapier automation on deal-won and confirm downstream action fires | Should | R2 |
| UAT-09 | Submit a right-to-erasure request and confirm the record is purged per policy | Must | R2 |
| UAT-10 | Run the migration dry-run and confirm the report flags a known duplicate correctly | Must | R2 |

## Defect Severity Classification
| Severity | Definition | Handling |
|---|---|---|
| Critical | Blocks a Must-priority workflow entirely | Must fix before go-live |
| High | Significant usability issue, workaround exists | Fix before go-live unless Sponsor accepts risk |
| Medium | Minor usability issue | Logged, fixed in next sprint |
| Low | Cosmetic | Logged, backlog |

## Sign-off
Each release requires written sign-off from the UAT participant group lead
(Sales Manager for Release 1; Sales Manager + Head of Customer Success for
Release 2) before the go/no-go review proceeds.
