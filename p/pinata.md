# pinata 402

> pinata.cloud | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pinata/ | JSON https://fshy.ajam.dev/api/v1/entity/pinata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pinata — dedicated gateway (free plan)

- `storage/pinata-dedicated-gateway` | fails-egress | evidence reported | binding request-rate | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.pinata.cloud/gateways/dedicated-ipfs-gateways
- free tier: 1 dedicated gateway included on Free; serves only CIDs pinned to your own account unless a Gateway Access Control is added. 10 GB/month bandwidth, 10,000 requests/month on Free. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered at 10 GB/month and 10,000 requests/month on Free. '10GB of Bandwidth per month through Dedicated Gateway / 10,000 Requests per month through Dedicated Gateway' (free-plan announcement). Unmetered request rate, but hard monthly byte cap. | metered: no | free allowance: 10 GB per month
- identity: email
- interface: rest
- limits:
  - request-rate (binding): 10,000 requests/month [1]
- limits note: Restricted-by-default gateway; Custom Domain required to serve HTML; 10 GB/mo bandwidth; 10k req/mo.
- binding note: calls are bounded rather than bytes, which is fatal to a nightly job on a monthly counter
- interface detail: rest
- tooling: Any HTTP client against <name>.mypinata.cloud; Pinata SDK gateways.public.get(); custom domain available on paid plans only.
- composes with: 1 GB storage per account is the ceiling, so a dedicated gateway can only ever front 1 GB of content per free account. Chaining accounts does not help because a dedicated gateway is restricted to its own account's pins by default. You would need a Gateway Access Control per gateway to serve cross-account CIDs, which is a paid/enterprise feature.
- reliability: The architectural point that kills this class: a dedicated gateway is account-scoped, so it cannot be used as a shared egress tier for other people's content, and a shared gateway (gateway.pinata.cloud) is unmetered but serves only public IPFS content. You still need somewhere to pin 500 GB, which Free does not provide.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 1 dedicated gateway included on Free; serves only CIDs pinned to your own account unless a Gateway Access Control is added. 10 GB/month bandwidth, 10,000 requests/month on Free.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'All Pinata Dedicated Gateways are restricted by default. This mean they will only serve CIDs that are pinned to your account'
  - [3] 2026-10-21: '10GB of Bandwidth per month through Dedicated Gateway', '10,000 Requests per month'
- sources:
  - [1] https://pinata.cloud/pricing
  - [2] https://docs.pinata.cloud/gateways/dedicated-ipfs-gateways
  - [3] https://pinata.cloud/blog/pinatas-new-free-plan/

## pinata 402 / account-free ipfs

- `storage/pinata-402-account-free-ipfs` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://402.pinata.cloud/
- free tier: None reachable: Not a free tier at all. It is x402 pay-per-upload with no account. Every upload is paid in crypto; nothing is free. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Not a free tier at all — it is x402 pay-per-upload with no account. Every upload is paid in crypto; nothing is free.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Not a free tier at all — it is x402 pay-per-upload with no account. Every upload is paid in crypto; nothing is free.
- sources:
  - [1] https://402.pinata.cloud/
