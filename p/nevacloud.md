# Nevacloud

> nevacloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nevacloud/ | JSON https://fshy.ajam.dev/api/v1/entity/nevacloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nevacloud

- `compute/nevacloud` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:55.982Z (live) | stale on 2026-12-05
- url https://nevacloud.com/en/free-vps/
- free tier: IDR 50,000 of credit as a promo code, granted by lottery to applicants who follow the provider on Instagram and post about it, redeemable within 30 days. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-shot-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Plan cards on the free-VPS page state 'Unlimited Bandwidth'; no overage price is published. | metered: no | source: [1]
- identity: email | detail: an email address plus Instagram and Twitter (X) accounts: the page states 'Each email, Twitter, and Instagram account can only receive one free service', the claim steps require following on both networks and posting a tweet, and 'accounts flagged as dummy accounts will not pass verification'. No card, phone or ID document is stated, and no hold exists because the grant is a promo code rather than a payment instrument
- interface: unknown
- limits:
  - write-gated (binding): The credit is not granted on signup but awarded by selection after a social-media action, and each email, Twitter and Instagram account can claim once, so the gate is editorial rather than technical. [1]
- limits note: The credit is not granted on signup but awarded by selection after a social-media action, and each email, Twitter and Instagram account can claim once, so the gate is editorial rather than technical.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: IDR 50,000 is roughly USD 3, which is a few days of the smallest instance rather than a workload, so it composes with nothing durable.
- reliability: no reliability event recorded
- notes: The useful comparison is that Jagoan's IDR 150,000 is granted automatically on signup while this IDR 50,000 is awarded by selection, which is the difference between a credit and a contest.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: one-shot-credit
- evidence:
  - [1] 2026-10-22: 'You'll get a Nevacloud promo code that can be redeemed for IDR 50,000 in credit', 'must be redeemed within 30 days', 'The offer is limited per user. Each email, Twitter, and Instagram account can only receive one free service', 'accounts flagged as dummy accounts will not pass verification', quoted
  - [1] 2026-10-22: the claim steps: 'Follow Nevacloud on Instagram and Twitter (X), and make sure you share a Tweet about Nevacloud before claiming your Free VPS', quoted
  - [1] 2026-11-03: the plan cards list unlimited bandwidth | capture: sha256:4ecfe7f25e53de9cda42903da56532b33945c3bbdd69aa49ddb7afe350b3441d | quote: Unlimited Bandwidth
- sources:
  - [1] https://nevacloud.com/en/free-vps/
