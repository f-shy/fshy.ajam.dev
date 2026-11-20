# metered

> mickeyzzc.tech | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mickeyzzc/ | JSON https://fshy.ajam.dev/api/v1/entity/mickeyzzc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## metered / xirsys / turnix free turn quotas

- `storage/metered-xirsys-turnix-free-turn-quotas` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:52.048Z (live) | stale on 2026-12-04
- url https://blog.mickeyzzc.tech/en/posts/network/third-party-free-p2p-nodes/
- free tier: none reachable: Free monthly bandwidth allowances on TURN relays are 20 GB for Metered, 500 MB for Xirsys, and 10 GB for Turnix. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the page lists monthly transfer quotas and overage prices but no per-object size cap | source: [1] | note: not applicable
- retention: Relay service cuts off when the quota is exhausted or the trial expires; a TURN credential is valid for at most 48 hours | source: [1]
- egress: Free monthly quotas of 500 MB (Xirsys and Metered) and 10 GB (Turnix); overage from USD 0.40/GB (Metered) and USD 30/mo with 40 GB (Turnix) | metered: no
- identity: email
- interface: unknown
- interface detail: the free quotas are TURN relays: Xirsys gives a standard ICE config with no SDK lock-in, Turnix gives standard TURN with multi-region GeoIP routing
- tooling: not documented
- composes with: stated-absent: the page states no way to chain these TURN quotas with other storage offers; they speak standard TURN and can be listed in an ICE config
- reliability: Metered's own pricing page now states a 500 MB/month free TURN trial, Xirsys states 500 MB/month after its trial, and a third-party survey lists Turnix at 10 GB/month
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Listed here so the relay…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Listed here so the relay s
  - [2] 2026-11-19: Metered's first-party free TURN allowance is 500 MB per month | capture: sha256:8660efdfb67d9b74026a5e82e32ebbcac5579a09a35356e6d24add45423617ef | quote: ### Free: 500 MB trial $0/mo - 500 MB monthly TURN usage
  - [1] 2026-11-19:  | capture: sha256:0018cebf87f6c4490e7c5b49e87de2c9fbf3dbe2e5af44ea9a8074148ea9a6d1 | quote: Free quotas also shrink — Metered once advertised 20-50 GB/month free; its pricing page now says 500 MB.
  - [1] 2026-11-19: Xirsys exposes a standard ICE configuration with no SDK lock-in | capture: sha256:0018cebf87f6c4490e7c5b49e87de2c9fbf3dbe2e5af44ea9a8074148ea9a6d1 | quote: | Xirsys | 500 MB/month (after a 30-day full-feature trial) | From USD 39/mo with 50 GB | Standard ICE config, no SDK lock-in |
  - [1] 2026-11-19: the relay stops on the spot when the quota is exhausted or the trial expires | capture: sha256:0018cebf87f6c4490e7c5b49e87de2c9fbf3dbe2e5af44ea9a8074148ea9a6d1 | quote: In production, quota-based free relay does not degrade — it cuts off: quota exhausted, trial expired, card charge failed, and the relay stops on the spot, stranding every session that depended on it.
  - [1] 2026-11-19: Turnix exposes standard TURN with multi-region GeoIP routing | capture: sha256:0018cebf87f6c4490e7c5b49e87de2c9fbf3dbe2e5af44ea9a8074148ea9a6d1 | quote: | Turnix | 10 GB/month | From USD 30/mo with 40 GB | Standard TURN, multi-region with GeoIP routing |
- sources:
  - [1] https://blog.mickeyzzc.tech/en/posts/network/third-party-free-p2p-nodes/
  - [2] https://www.metered.ca/pricing
