# Release Plan — NexusCRM Platform

## Release 1 — Core CRM
**Target date:** End of Week 8
**Audience:** Internal (Sales team, 14 users)

### Scope
Auth & permissions, contact/account management, deal pipeline, core admin and
audit logging. See backlog items NX-1 through NX-14.

### Success Criteria
| Criterion | Target |
|---|---|
| UAT sign-off | Sales power-users approve all Must-priority stories |
| Critical bugs at launch | 0 |
| Data model validated | Supports Release 2 reporting without rework |

### Rollout Approach
Direct internal rollout to all 14 Sales users on go-live day, with the legacy
spreadsheet workflow deprecated immediately (legacy contact database stays read-only
as a reference until Release 2 migration is complete).

### Rollback Plan
If a critical issue is found within 48 hours of go-live, Sales reverts to the
legacy spreadsheet workflow for pipeline tracking while the legacy contact database
(read-only) remains the reference source of truth until the issue is resolved.

---

## Release 2 — Reporting & Integrations
**Target date:** End of Week 16
**Audience:** Internal (Sales + Customer Success, 20 users)

### Scope
Reporting dashboards, email integration, Zapier integration, legacy data migration,
GDPR erasure workflow. See backlog items NX-15 through NX-23.

### Success Criteria
| Criterion | Target |
|---|---|
| External security/GDPR audit | Passed, no critical findings |
| UAT sign-off | Sales + Customer Success approve all Must-priority stories |
| Migration accuracy | < 3% duplicate rate post-migration |
| Critical bugs at launch | 0 |

### Rollout Approach
Phased: dashboards and reporting go live first (Week 15), followed by email/Zapier
integrations and the committed data migration (Week 16), once the migration dry-run
report has been reviewed and approved by the PM and Data Privacy Officer.

### Rollback Plan
See [Go-Live Checklist](15-go-live-checklist.md) for the full cutover and rollback
procedure — the legacy database remains available in read-only mode through the
2-week parallel-run buffer specifically to support this rollback path.
