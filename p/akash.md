# Akash Network

> akash.network | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/akash/ | JSON https://fshy.ajam.dev/api/v1/entity/akash.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Akash Network (Compute)

- `compute/akash-network` | trial-only | evidence documented | binding retention-clamped | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-06T19:39:36.653Z (live) | stale on 2026-12-07
- url https://akash.network/docs/getting-started/quick-start/
- free tier: 'USD 1 in free credits - enough to run your first deployment and explore the deploy loop', '30 days - your window to use the trial credit'. Quoted: 'Deployments run up to 24 hours each, and you can redeploy as many times as you like inside the 30-day window. GPUs up to the RTX 3090 are available. Anything above - including the RTX 4090, RTX 5090, and datacenter cards like the A100, H100, H200, and B200 - requires a non-trial account.' Prerequisites quoted: 'A valid email address (or Google / GitHub account). That's it! No credit card, no crypto wallet, no blockchain setup, no installation required.' | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-off-credit
- per-object cap: not applicable | source: [1]
- retention: The USD 1 credit and the 24-hour per-deployment cap fail first: at the tracked RTX 3090 rate of USD 0.150 per GPU-hour the credit buys about 6.7 GPU-hours, so the trial proves the deploy loop and nothing more. | source: [1]
- egress: quoted comparison table lists Akash egress as Zero against AWS billed per GB, and commitment as None with the lease closeable whenever you want | metered: no | source: [2]
- identity: email | detail: email, or a Google or GitHub account, and nothing else: the Quick Start prerequisites state 'A valid email address (or Google / GitHub account). That's it! No credit card, no crypto wallet, no blockchain setup, no installation required.', and a second Akash page states 'no card required'. No hold exists because no payment method is taken, so the debit and prepaid questions do not arise at signup; the paid permissionless route is funded in ACT and documents 'no KYC'.
- interface: unknown
- limits:
  - retention-clamped (binding): The USD 1 credit and the 24-hour per-deployment cap fail first: at the tracked RTX 3090 rate of USD 0.150 per GPU-hour the credit buys about 6.7 GPU-hours, so the trial proves the deploy loop and nothing more. [1]
- limits note: The USD 1 credit and the 24-hour per-deployment cap fail first: at the tracked RTX 3090 rate of USD 0.150 per GPU-hour the credit buys about 6.7 GPU-hours, so the trial proves the deploy loop and nothing more.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The permissionless path is the composable half: no KYC, no 30-day clock, funded in ACT, so it is the only decentralized lane here that a wallet alone opens with no identity check. It composes with any card-priced workload that cannot run locally.
- reliability: no reliability event recorded
- notes: The USD 1 trial credit is the current figure. An older blog post still advertises USD 10, so the trial was cut by 10x; a reader who finds the blog first will overestimate by 10x. The GPU price table at /pricing/gpus is client-rendered and returns empty rows, so individual rates below the RTX 3090 tier are not read off Akash's own page. Akash's own usage calculator computes the exact USD/GPU-hour. One inconsistency: Akash homepage marketing states H100s for USD 1.33 per hour while its own H100 pricing page states USD 2.73 as of 2026-10-20. The pricing page is the specific claim and the homepage line is undated, so the page wins. Egress does not bind at Akash: it documents zero egress fees, so the constraint here is the credit and the 24-hour deployment cap, not bandwidth.
- extras:
  - facets.class: decentralized-marketplace
  - facets.free_tier_kind: one-off-credit
  - facets.shape.gpu_class: RTX 3090 and below
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: the trial is USD 1 of credit for 30 days, email/OAuth signup, no card and no wallet; per-deployment cap 24 hours; GPUs above RTX 3090 excluded from trial, all quoted
  - [1] 2026-10-22: probe returned status 200, 162506 bytes, sha256 7a032564a9809899c843b7f7efc046a80cfa05a3b50b784537029717abb7254d
  - [3] 2026-10-22: quoted: 'go permissionless with your own wallet (no KYC; fund deployments with ACT)'. Trial deployments have a 24-hour maximum duration per deployment
  - [4] 2026-10-22: an earlier announcement of the same free trial states 'USD 10 in credit'; the live Quick Start page states USD 1. The page is stale against the docs and the smaller number is the one the docs assert
  - [5] 2026-10-22: Akash own page states on-demand H100 starts at USD 2.73 per GPU-hour as of October 20 2026, and an 8x H100 at USD 21.84 per hour
  - [6] 2026-10-22: independent tracker records Akash RTX 3090 at USD 0.150 per GPU-hour, last updated 2026-10-21, rank 2 of 12 providers for that card
  - [7] 2026-10-22: quoted: receive USD 1 in free trial credits with no card required; trial deployments auto-close after 24 hours; H100, H200, A100, RTX 4090 and RTX 5090 are not available on the free trial
  - [2] 2026-10-22: quoted comparison table lists Akash egress as Zero against AWS billed per GB, and commitment as None with the lease closeable whenever you want
  - [1] 2026-10-22: quoted: USD 1 in free credits, 30-day window, 24-hour deployments, GPUs up to RTX 3090 only, email or OAuth and no card and no wallet
  - [6] 2026-10-22: third-party price index reports RTX 3090 on Akash at USD 0.150 per GPU-hour on-demand, one configuration, observed the same day
  - [8] 2026-10-22: a second index lists RTX 3090 24Gi at USD 0.090 and an RTX 3060 12Gi at USD 0.080 from the Akash marketplace, giving the 0.09 to 0.15 range used in the division
  - [1] 2026-11-06: the trial caps each deployment at 24 hours and reaches only GPUs up to the RTX 3090 | capture: sha256:cfaca1dd4ff5818a97864f9fe2fab4d8020fcd551a3478ef7de3d1967a3e2a75 | quote: Deployments run up to 24 hours each, and you can redeploy as many times as you like inside the 30-day window. GPUs up to the RTX 3090 are available.
- sources:
  - [1] https://akash.network/docs/getting-started/quick-start/
  - [2] https://akash.network/explore/compare/akash-vs-aws/
  - [3] https://akash.network/docs/getting-started/what-is-akash/
  - [4] https://akash.network/blog/introducing-credit-card-payments-in-akash-console/
  - [5] https://akash.network/pricing/gpus/h100/
  - [6] https://computeprices.com/providers/akash/gpus/rtx3090
  - [7] https://akash.network/docs/developers/deployment/akash-console/getting-started/
  - [8] https://skycisa.com/providers/akash-network

## akash network (Storage)

- `storage/akash-network` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://akash.network/docs/learn/core-concepts/persistent-storage/
- free tier: none reachable: It is a compute marketplace, not storage: persistent storage is a paid resource attached to a deployment (per-GB-month in AKT), ephemeral by default, and there is no object-storage or IPFS… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: not-storage
  - dead_end.why: It is a compute marketplace, not storage: persistent storage is a paid resource attached to a deployment (per-GB-month in AKT), ephemeral by default, and there is no object-storage or IPFS…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: It is a compute marketplace, not storage: persistent storage is a paid resource attached to a deployment (per-GB-month in AKT), ephemeral by default, and there is no object-storage or IPFS…
- sources:
  - [1] https://akash.network/docs/learn/core-concepts/persistent-storage/
