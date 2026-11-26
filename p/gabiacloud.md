# Gabia Cloud Gen1

> gabiacloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gabiacloud/ | JSON https://fshy.ajam.dev/api/v1/entity/gabiacloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gabia Cloud Gen1

- `compute/gabia-cloud-gen1` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.gabiacloud.com/virtual_service/
- free tier: Hourly or monthly billed virtual servers from KRW 45 an hour for the smallest Micro shape, with the same price becoming a lower monthly rate once a full month is used. Billing is post-paid, computed per calendar month with minutes rounded up to the hour, and a private individual pays by automatic credit-card charge. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id | detail: a Korean public certificate is required to pay by card: the service page states an individual pays by automatic credit-card charge and that automatic payment requires card authentication with a 공인인증서, and the record's limits row states that certificate is issued against a Korean resident registration number, so the gate is a national identity number rather than the card itself. Whether a foreign resident can pay by bank transfer without the certificate is not established, and no hold, debit or prepaid statement appears
- interface: unknown
- limits:
  - write-gated (binding): Automatic card payment requires card authentication through a Korean public certificate (' '), which is issued against a Korean resident registration number, so the gate is identity rather than price or capacity. [1]
- limits note: Automatic card payment requires card authentication through a Korean public certificate (' '), which is issued against a Korean resident registration number, so the gate is identity rather than price or capacity.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The KRW 5,000 Micro shape is the cheapest published Korean monthly figure, and the certificate requirement is what stands between a non-resident and it; that pairing is the whole finding.
- reliability: no reliability event recorded
- notes: Registration requires a Korean public certificate tied to a resident registration number.
- extras:
  - facets.class: domestic-gated
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the page states that g클라우드 Gen1 supports an optimised environment from 45 원 an hour, that billing is post-paid per calendar month with minutes rounded up to the hour, that an individual may pay by automatic credit card, and that automatic payment requires card authentication with a 공인인증서
  - [2] 2026-10-22: the price-change notice publishes the Classic ladder: Micro(HDD) 1 vCore with 512 MB and 20 GB at 5,000 원 a month or 7 원 an hour, 베이직 1 vCore with 1 GB and 50 GB at 20,000 원 or 34 원, up to 8 vCore with 16 GB at 299,000 원 a month
- sources:
  - [1] https://www.gabiacloud.com/virtual_service/
  - [2] https://www.gabia.com/gabia_notice/view.php?seq_no=31781
