# perforce p4

> perforce.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/perforce/ | JSON https://fshy.ajam.dev/api/v1/entity/perforce.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## perforce p4 (helix core) free edition

- `storage/perforce-p4-free-edition` | self-hosted, last resort | verdict fails-quota | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:22:32.525Z (live) | stale on 2026-12-05
- url https://www.perforce.com/products/p4/free-version-control
- free tier: Free for up to 5 users and 20 workspaces; the free edition is self-hosted, so storage is bounded by the machine the user runs the server on ('no limitations on storage no matter which plan you’re on') | unit: users | metered on: identity-count | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- binding note: no storage limit is stated for the free edition; capacity is the disk of the machine the user runs the server on, and the free edition is capped at 5 users and 20 workspaces
- interface detail: not documented
- tooling: Hosted option: P4 Cloud, managed and hosted by Perforce, at $39 per user per month with 64GiB storage included. Free edition: the user installs and runs the P4 server on a rented or free machine (in the cloud or on-premises); no storage limit is imposed by the vendor.
- composes with: not recorded
- reliability: The free edition is a self-hosted server: capacity is the disk of the machine the user runs it on, and the vendor states no storage limit; the free edition is limited to 5 users and 20 workspaces.
- notes: Free edition: up to 5 users, 20 workspaces, 3 Git repos, self-hosted. Paid: P4 Cloud (managed and hosted) at $39 per user per month with 64GiB storage included; Scale and Platform plans are quote-only.
- evidence note: documented: the pages read on 2026-11-03 are two vendor pages. https://www.perforce.com/products/p4/free-version-control states that P4 is free for up to 5 users and 20 workspaces and can be deployed in the cloud or on-premises. https://www.perforce.com/products/p4/pricing states that the free version is a self-hosted solution with no limitations on storage, whichever plan. The user and workspace caps and the absence of a storage limit, which decide the verdict, rest on those pages; the identity kind and the interface are not stated on them (the record's own text marks them defaulted).
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The '20 users / 1 TB' figure does not exist on Perforce's pages. Current free tier is 'up to 5 users and 20 workspaces' with no storage allowance at all — it is a self-hosted server, so…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The '20 users / 1 TB' figure does not exist on Perforce's pages. Current free tier is 'up to 5 users and 20 workspaces' with no storage allowance at all — it is a self-hosted server, so…
  - [2] 2026-10-21: cited as the basis of the rejection: The '20 users / 1 TB' figure does not exist on Perforce's pages. Current free tier is 'up to 5 users and 20 workspaces' with no storage allowance at all — it is a self-hosted server, so byte
  - [1] 2026-11-03: the free edition is for up to 5 users and 20 workspaces | capture: sha256:a9609313ace0793e06174091c9653b0da6fe4ab722f05e1ac9f639f964e1be3d | quote: Perforce P4 is free for up to 5 users and 20 workspaces. Deploy in the cloud or on-premises and start versioning today.
  - [2] 2026-11-03: the free version is self-hosted with no storage limitation | capture: sha256:6d98a5955ac73c7986f5126c17f044156c9ab456055ec0f90150365cecce4ee8 | quote: The free version of P4 is a self-hosted solution. This means no limitations on storage no matter which plan you’re on.
  - [2] 2026-11-03: P4 Cloud includes 64GiB of storage | capture: sha256:6d98a5955ac73c7986f5126c17f044156c9ab456055ec0f90150365cecce4ee8 | quote: 64GiB storage included
  - [1] 2026-11-03: the free edition is free for up to 5 users and 20 workspaces | capture: sha256:a9609313ace0793e06174091c9653b0da6fe4ab722f05e1ac9f639f964e1be3d | quote: Perforce P4 is free for up to 5 users and 20 workspaces. Deploy in the cloud or on-premises and start versioning today.
  - [1] 2026-11-04: the free edition is for up to 5 users and 20 workspaces | capture: sha256:a9609313ace0793e06174091c9653b0da6fe4ab722f05e1ac9f639f964e1be3d | quote: Perforce P4 is free for up to 5 users and 20 workspaces. Deploy in the cloud or on-premises and start versioning today.
- sources:
  - [1] https://www.perforce.com/products/p4/free-version-control
  - [2] https://www.perforce.com/products/p4/pricing
