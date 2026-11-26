# EOSC EU

> open-science-cloud.ec.europa.eu | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/open-science-cloud-ec-europa-eu/ | JSON https://fshy.ajam.dev/api/v1/entity/open-science-cloud-ec-europa-eu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EOSC EU Node — 50 GB personal + 500 GB group file storage per user, free credits from the European Commission

- `storage/eosc-eu-node-50-gb-personal-500-gb-group-file-storage-pe` | fails-identity | evidence reported | binding none | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:31.169Z (live) | stale on 2026-12-04
- url https://open-science-cloud.ec.europa.eu/about/access-policy
- free tier: Access-policy table: File Storage (Personal) = 50 GB for Collaborator and Investigator; File Storage (Group) = 500 GB for Investigator only. Investigator also gets 'File Transfer 1TB/month'. Credits: Collaborator 1,000; Investigator '2,000 (individual) / 6,000 (group)', renewed automatically every three months and explicitly not top-up-able. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Credits are provided free of charge by the European Commission, are automatically renewed every three months, cannot be transferred to another person or between periods, and additional credits are not provided; services are ordered for a fixed period, so the allocation is not permanent. | source: [1] | note: not stated
- egress: Not metered; the node is EC-procured infrastructure. The binding constraint is the monthly 1 TB transfer allowance, which is the only hard number in the policy. | metered: yes
- identity: institution | detail: eduGAIN / EU Login / eIDAS federated identity; access group is assigned automatically from affiliation information shared by the home organisation; only users from EU27 and Horizon Europe Associated Countries can get a role above Observer.
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
  - [1] 2026-11-19: the first-party access-policy table states the personal and group file storage and transfer allowances | capture: sha256:fd74f46c2fac9dd8e17db6e40765c7e33cfb9522ee1304e0b0c2b97fb6932e1a | quote: | File Transfer | ✗ | ✗ | ✓ (1TB/month) | ✓ (1TB/month) | | File Storage (Personal) | ✗ | ✗ | ✓ (50GB) | ✓ (50GB) | | File Storage (Group) | ✗ | ✗ | ✗ | ✓ (500GB) |
  - [2] 2026-11-19: the first-party credits FAQ states credits do not carry between periods | capture: sha256:f9a116b55288071f730f9b09dd944b8fde7e8d281d70724f57d8f5de4cd2df58 | quote: Please remember that you cannot transfer your credits to another person or between periods.
  - [1] 2026-11-19: the first-party policy states access is assigned from home-organisation affiliation data | capture: sha256:fd74f46c2fac9dd8e17db6e40765c7e33cfb9522ee1304e0b0c2b97fb6932e1a | quote: The exact number of credits you receive, as well as your level of access to various services, are set automatically based on the affiliation information shared by your home organisation.
- sources:
  - [1] https://open-science-cloud.ec.europa.eu/about/access-policy
  - [2] https://www.eosc.athenarc.gr/support/frequently-asked-questions/user-credits

## eosc eu node as bulk storage

- `storage/eosc-eu-node-as-bulk-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:52.048Z (live) | stale on 2026-12-04
- url https://open-science-cloud.ec.europa.eu/about/access-policy
- free tier: None. The access policy grants 50 GB personal and 500 GB group file storage with up to 1 TB upload transfer per month; credits refresh every 90 days and unused credits expire. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the access policy states storage and transfer quotas but no per-object size cap | source: [1] | note: not applicable
- retention: Unused credits expire at the end of each 90-day period; reserved service environments are deactivated on credit or time expiration and reactivation needs a Helpdesk request | source: [1]
- egress: Large File Transfer allows up to 1TB upload per month; file transfer is capped at 1TB/month and charged 7 credits per month | metered: no
- identity: email
- interface: s3
- interface detail: the access policy lists S3 storage on Virtual Machines; File Sync and Share is provided through ownCloud and large transfers through FileSender and FTS
- tooling: not documented
- composes with: stated-absent: the access policy states no way to chain EOSC EU Node storage with other storage offers
- reliability: Allocation provides 50 GB personal storage and 500 GB group storage with 1 TB per month transfer. Storage credits do not roll over and cannot be supplemented.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50 GB personal / 500 GB group, 1 TB/month transfer, credits that do not roll over and cannot be topped up. Reported as a candidate above for…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 50 GB personal / 500 GB group, 1 TB/month transfer, credits that do not roll over and cannot be topped up. Reported as a candidate above for completeness
  - [1] 2026-11-19: the access policy grants at most 50 GB personal file storage | capture: sha256:fd74f46c2fac9dd8e17db6e40765c7e33cfb9522ee1304e0b0c2b97fb6932e1a | quote: | File Storage (Personal) | ✗ | ✗ | ✓ (50GB) | ✓ (50GB) |
  - [1] 2026-11-19: the access policy grants at most 500 GB group file storage | capture: sha256:fd74f46c2fac9dd8e17db6e40765c7e33cfb9522ee1304e0b0c2b97fb6932e1a | quote: | File Storage (Group) | ✗ | ✗ | ✗ | ✓ (500GB) |
  - [1] 2026-11-19: the monthly upload transfer allowance is 1 TB | capture: sha256:fd74f46c2fac9dd8e17db6e40765c7e33cfb9522ee1304e0b0c2b97fb6932e1a | quote: | ** Large File Transfer (FileSender) ** | Up to 1TB transfer (upload) per month | 7 | Credits per month |
  - [1] 2026-11-19: the VM service offers up to 1TB of S3 storage, an S3 interface on the EOSC EU Node | capture: sha256:fd74f46c2fac9dd8e17db6e40765c7e33cfb9522ee1304e0b0c2b97fb6932e1a | quote: | Virtual Machines | Up to 2 vCPU with 8GB RAM, up to 700GB (fast/large) storage, up to 1TB S3 storage (if available), 1 Gbps | Up to 16 vCPU with 64GB RAM, up to 1TB (fast/large) storage, up to 1TB S3 storage (if available), 10 Gbps | Up to 64 vCPU with 128GB RAM, 1 GPU with at least 16GB RAM, 1TB fast/2TB large storage (3TB total storage quota), up to 1TB S3 storage (if available), 10 Gbps | Dependent on size |
  - [1] 2026-11-19: service allocations are tied to 90-day credit periods after which unused credits expire | capture: sha256:fd74f46c2fac9dd8e17db6e40765c7e33cfb9522ee1304e0b0c2b97fb6932e1a | quote: Credits Replenishment: Credits refresh every 90 days, starting from your first login. Unused credits expire at the end of the period for all services, except for credit grants.
- sources:
  - [1] https://open-science-cloud.ec.europa.eu/about/access-policy
