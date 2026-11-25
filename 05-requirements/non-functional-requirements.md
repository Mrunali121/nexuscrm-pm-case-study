# Non-Functional Requirements — NexusCRM Platform

## Performance
| ID | Requirement |
|---|---|
| NFR-01 | Pipeline board loads in under 2 seconds for up to 2,000 active deals |
| NFR-02 | Dashboard queries (Release 2) return in under 3 seconds at current data volume |

## Security & Compliance
| ID | Requirement |
|---|---|
| NFR-03 | All customer data hosted on Meridian's existing EU infrastructure (data residency) |
| NFR-04 | Role-based access control enforced at the API layer, not just the UI |
| NFR-05 | Full audit log of record access and changes, retained per Meridian's data retention policy |
| NFR-06 | Right-to-erasure requests supported via an admin-initiated data purge workflow |
| NFR-07 | External security/GDPR audit must pass with no critical findings before Release 2 go-live |

## Reliability
| ID | Requirement |
|---|---|
| NFR-08 | 99.5% uptime target during business hours (internal tool, not customer-facing) |
| NFR-09 | Daily automated backups with a tested restore procedure |

## Usability
| ID | Requirement |
|---|---|
| NFR-10 | Core workflows (add contact, move deal stage, log activity) achievable in ≤ 3 clicks |
| NFR-11 | Responsive web layout supporting desktop and tablet (mobile native explicitly out of scope) |

## Maintainability
| ID | Requirement |
|---|---|
| NFR-12 | API documented and versioned to support the Release 2 Zapier integration and any future integrations |
