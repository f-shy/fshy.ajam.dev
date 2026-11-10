# EOSC EU

> open-science-cloud.ec.europa.eu | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/open-science-cloud-ec-europa-eu/ | JSON https://fshy.ajam.dev/api/v1/entity/open-science-cloud-ec-europa-eu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EOSC EU Node — 50 GB personal + 500 GB group file storage per user, free credits from the European Commission

- `storage/eosc-eu-node-50-gb-personal-500-gb-group-file-storage-pe` | fails-identity | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://open-science-cloud.ec.europa.eu/about/access-policy
- free tier: Access-policy table: File Storage (Personal) = 50 GB for Collaborator and Investigator; File Storage (Group) = 500 GB for Investigator only. Investigator also gets 'File Transfer 1TB/month'. Credits: Collaborator 1,000; Investigator '2,000 (individual) / 6,000 (group)', renewed automatically every three months and explicitly not top-up-able. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Retention: credits 'cannot be transferred to another person or carried over between periods' and are 'automatically renewed every three months'; services are ordered for a fixed period and refunded pro rata if released, so nothing here is permanent | source: [1] | note: not stated
- egress: Not metered; the node is EC-procured infrastructure. The binding constraint is the monthly 1 TB transfer allowance, which is the only hard number in the policy. | metered: yes
- identity: institution
- interface: s3, rest
- limits note: per-object-cap: not stated. request-rate: 1 TB/month File Transfer is the sharpest published cap. Retention: credits 'cannot be transferred to another person or carried over between periods' and are 'automatically renewed every three months'; services are ordered for a fixed period and refunded pro rata if released, so nothing here is permanent. Gate: eduGAIN/ORCID/EU Login identity; access group is assigned automatically from your home organisation's affiliation data, and 'The EOSC EU Node does not support automatic transition between access groups.'
- interface detail: rest
- tooling: EOSC EU Node User Space web UI plus credit-metered service orders; no documented S3 endpoint. Treat as API-less until probed by an account holder.
- composes with: The chaining hook is wallets, not accounts: 'When you create a group, a separate Group Wallet will automatically be generated. This wallet is independent of your personal wallet and comes pre-allocated with additional credits.' Investigator groups also carry the 500 GB group file storage. Many groups = many 500 GB pools, and the group storage is separate from the 50 GB personal pool.
- reliability: Credits are not top-up-able ('additional ones will not be provided to you') and do not carry over. A storage-heavy month silently stops you until the next quarter.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Access-policy table: File Storage (Personal) = 50 GB for Collaborator and Investigator; File Storage (Group) = 500 GB for Investigator only. Investigator also gets 'File Transfer 1TB/month'. Credits: Collaborator 1,000; Investigator '2,000 (individual) / 6,000 (group)', renewed automatically every three months and explicitly not top-up-able.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'File Storage (Personal) ... 50GB', 'File Storage (Group) ... 500GB', 'File Transfer ... 1TB/month', 'Credits ... 2,000 (individual) / 6,000 (group)'
  - [2] 2026-10-21: paid 'free of charge (at the point of use) by the European Commission', 'automatically renewed every three months', 'additional ones will not be provided to you', 'When you create a group, a separate Group Wallet will automatically be generated ... pre-allocated with additional credits'
- sources:
  - [1] https://open-science-cloud.ec.europa.eu/about/access-policy
  - [2] https://www.eosc.athenarc.gr/support/frequently-asked-questions/user-credits

## eosc eu node as bulk storage

- `storage/eosc-eu-node-as-bulk-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://open-science-cloud.ec.europa.eu/about/access-policy
- free tier: none reachable: Allocation provides 50 GB personal storage and 500 GB group storage with 1 TB per month transfer. Storage credits do not roll over and cannot be supplemented. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50 GB personal / 500 GB group, 1 TB/month transfer, credits that do not roll over and cannot be topped up. Reported as a candidate above for…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 50 GB personal / 500 GB group, 1 TB/month transfer, credits that do not roll over and cannot be topped up. Reported as a candidate above for completeness
- sources:
  - [1] https://open-science-cloud.ec.europa.eu/about/access-policy
