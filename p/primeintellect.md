# Prime Intellect

> primeintellect.ai | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/primeintellect/ | JSON https://fshy.ajam.dev/api/v1/entity/primeintellect.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Prime Intellect Sandboxes

- `compute/prime-intellect` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:44.838Z (live) | stale on 2026-11-22
- url https://www.primeintellect.ai/sandboxes
- free tier: no free tier: tier-free per-second pricing at $0.02 a vCPU-hour, $0.0125 a GiB-hour of memory and $0.0002 a GiB-hour of disk, with no subscription or minimum spend | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.02 a vCPU-hour, $0.0125 a GiB-hour of memory and $0.0002 a GiB-hour of disk [1]
  - request-rate (binding): 100 concurrent sandboxes in the worked example; the page advertises scaling to tens of thousands [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The sandboxes page was read on 2026-10-22 and publishes metered resource rates. The offering has no subscription tier ladder and charges metered usage.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 1
  - shape.disk: 5
  - shape.note: the worked example: 1 vCPU, 1 GiB and 5 GiB of disk at $0.0335 a sandbox-hour
  - session_cap.restart_required: no
  - session_cap.note: every workload stays in an isolated microVM; the page states no reap
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.gib: 5
  - ps.price: $0.0002 a GiB-hour
  - ps.durability: sandbox disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Tier-free pricing built for scale, with no subscriptions or minimum spend' with 'vCPU $0.02 / hour', 'Memory $0.0125 / GiB / hour', 'Disk $0.0002 / GiB / hour', and '1 vCPU · 1 GiB RAM · 5 GiB disk · 100 Sandboxes $3.35 / hour = $0.0335 / sandbox / hour', quoted
- sources:
  - [1] https://www.primeintellect.ai/sandboxes

## Prime Intellect

- `compute/prime-intellect-2` | dead | evidence documented | binding volume-quota | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.primeintellect.ai/blog/fast-compute-grants
- free tier: The grant program is gone. Its own page now returns HTTP 404, and no signup credit exists: the docs describe a prepaid model where 'your Prime Intellect credits are deducted every minute while the Pod is active' and 'If your credits run out, your Pods will be automatically deleted'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): Both doors fail: there is no signup credit, so the first pod needs a funded balance, and the USD 500 to USD 100,000 Fast Compute Grants program no longer has a live page. [1]
- limits note: Both doors fail: there is no signup credit, so the first pod needs a funded balance, and the USD 500 to USD 100,000 Fast Compute Grants program no longer has a live page.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None while the grant is closed. If it reopened it would be a real credit lane, because the platform aggregates other providers and accepts prepaid balances.
- reliability: no reliability event recorded
- notes: REFUTATION of a widely recirculated grant. Two figures circulate: 'USD 500 to USD 100,000 Fast Compute Grants' and 'USD 50 free compute at ICLR'. Both source pages return 404 as of 2026-10-22, and the ICLR page carried an expiry of 31 December 2024. The grant was real in 2024; it is not an offer now. Unverified: a live page on primeintellect.ai naming an amount and an application route.
- extras:
  - facets.class: gpu-marketplace-grant
- evidence:
  - [1] 2026-10-22: fetch --head returned 'HTTP/1.1 404 Not Found'; the page previously offered 'USD 500-USD 100k worth of Prime Intellect compute credits'
  - [2] 2026-10-22: fetch --head returned 'HTTP/1.1 404 Not Found'
  - [3] 2026-10-22: quoted: 'Your Prime Intellect credits are deducted every minute while the Pod is active. If your credits run out, your Pods will be automatically deleted'; no free tier described
  - [4] 2026-10-22: independent check dated 2026-08-21 records that both the grants and ICLR pages returned 404 and that no live official page states either offer
- sources:
  - [1] https://www.primeintellect.ai/blog/fast-compute-grants
  - [2] https://www.primeintellect.ai/grants
  - [3] https://docs.primeintellect.ai/faq
  - [4] https://buildaicurrent.com/credits/prime-intellect-free-credits/
