# Go-Live Checklist — NexusCRM Platform

Used for both Release 1 and Release 2 cutovers, adapted per release scope.

## Pre-Launch (T-minus 1 week)
- [ ] All Must-priority UAT scenarios signed off
- [ ] 0 open critical/high-severity bugs
- [ ] External security/GDPR audit passed (Release 2 only — hard gate per NFR-07)
- [ ] Data migration dry-run reviewed and approved (Release 2 only)
- [ ] Rollback plan documented and reviewed with Engineering Director
- [ ] Backups verified with a tested restore (per NFR-09)
- [ ] Go/no-go meeting held with Steering Committee

## Launch Day
- [ ] Final backup taken immediately before cutover
- [ ] Committed data migration executed (Release 2 only) and record count reconciled
      against the legacy source
- [ ] Feature flags / access enabled for the target user group
- [ ] Legacy system set to read-only (not decommissioned yet — see Post-Launch)
- [ ] Launch announcement sent to affected users with a quick-start guide
- [ ] PM and DevOps on standby for the first business day

## Post-Launch (Week 1)
- [ ] Daily check-in with Sales/CS leads for the first 5 business days
- [ ] Monitor error logs and performance against NFR-01/NFR-02 targets
- [ ] Triage any reported issues same-day; critical issues trigger rollback discussion
- [ ] Weekly status report resumes normal cadence after Day 5 if stable

## Parallel-Run & Decommission (Weeks 17–18, after Release 2)
- [ ] Legacy system remains available read-only for the 2-week buffer
- [ ] Confirm no critical issues have required a rollback to legacy
- [ ] Final data reconciliation between legacy and NexusCRM
- [ ] Sponsor sign-off to decommission legacy system
- [ ] Legacy system archived per data retention policy, then decommissioned

## Rollback Plan
If a critical issue is found within the first 5 business days post-launch:
1. PM convenes Engineering Director and DevOps within 2 hours of confirmation.
2. If unresolvable same-day, users revert to the legacy workflow (spreadsheet for
   Release 1 features; legacy read-only DB remains the reference source of truth).
3. Root cause fixed and re-validated in a subsequent sprint before re-attempting
   cutover for the affected feature only — not a full release rollback unless the
   issue is systemic.
