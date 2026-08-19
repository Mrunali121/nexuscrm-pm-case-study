# Functional Requirements — NexusCRM Platform

Gathered via 4 requirements workshops with Sales, Customer Success, and Engineering
(Weeks 1–2), and prioritized with the Product Owner role (held by the PM for this
project).

## Authentication & Permissions
| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Users authenticate via company SSO (existing Google Workspace) | Must |
| FR-02 | Three role tiers: Admin, Sales Rep, Read-only (Customer Success) | Must |
| FR-03 | Admins can deactivate a user without deleting their historical activity log | Must |

## Contact & Account Management
| ID | Requirement | Priority |
|---|---|---|
| FR-04 | Create, edit, and merge contact records, with a duplicate-detection warning on save | Must |
| FR-05 | Contacts can be grouped under a parent Account (company) record | Must |
| FR-06 | Full activity history (calls, emails, notes) visible on a contact's timeline | Must |
| FR-07 | Bulk import of contacts via CSV with field mapping | Should |

## Deal Pipeline
| ID | Requirement | Priority |
|---|---|---|
| FR-08 | Kanban-style pipeline view with configurable deal stages | Must |
| FR-09 | Drag-and-drop stage changes must NOT require a page reload — flagged by Sales power-users as a dealbreaker for daily adoption during requirements workshops | Must |
| FR-10 | Deal value roll-up visible per stage and per sales rep | Must |
| FR-11 | Won/lost reason capture on deal close | Should |

## Reporting (Release 2)
| ID | Requirement | Priority |
|---|---|---|
| FR-12 | Live pipeline dashboard replacing the manual monthly report | Must |
| FR-13 | Exportable reports (CSV, PDF) for leadership review | Should |
| FR-14 | Rep-level and team-level performance views | Should |

## Integrations (Release 2)
| ID | Requirement | Priority |
|---|---|---|
| FR-15 | Two-way email sync (send/receive logged against contact timeline) | Must |
| FR-16 | Zapier integration for at least 3 common triggers (new deal, stage change, deal won) | Should |

## Data Migration
| ID | Requirement | Priority |
|---|---|---|
| FR-17 | Guided migration tool from legacy database with duplicate resolution step | Must |
| FR-18 | Migration dry-run mode with a report before committing changes | Must |

See [Non-Functional Requirements](non-functional-requirements.md) for performance,
security, and compliance requirements.
