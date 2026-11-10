# LocalCan

> localcan.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/localcan/ | JSON https://fshy.ajam.dev/api/v1/entity/localcan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LocalCan

- `egress/localcan` | fails-quota | evidence documented | binding volume-quota | category http tunnel with tcp on paid plans | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.localcan.com/pricing
- price USD 0 (paid tiers above)
- free tier: 1 live Public URL, 60-min sessions, 1 GB/month | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 GB per month on the free plan; the plan table gives no daily or burst allowance.; ingress: http-only | metered: yes | free allowance: 1 GB per month on the free plan; the plan table gives no daily or burst allowance. | source: [1]
- identity: email | detail: free signup, no card: 'Free 14-day trial included. No credit card required.' | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 GB/month [1]
- binding note: 1 GB/month is 0.0009 TiB, so the byte quota fails about a thousand times before 1 TiB/month and long before any transport question. Free is also one URL with 60-minute sessions.
- interface detail: Desktop app plus CLI.
- tooling: desktop app and CLI; Linux is CLI-only.
- composes with: Cannot carry 1 TiB/month at any tier that was read.
- reliability: Sessions are capped at 60 minutes on free, so a long transfer is cut every hour.
- notes: TCP exists as a product ('Tunnel databases, SSH boxes, and Kubernetes clusters') but appears from the first paid column upward. No page read mentions UDP.
- evidence note: Nothing would raise this: the quota is explicit and the free column lists no TCP.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_tib_month: 0.0009
  - volume_stated: 1 GB per month on the free plan; the plan table gives no daily or burst allowance.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: '1 live Public URL 60-min sessions, 1 GB/month'; paid column adds 'HTTPS / TCP'
- sources:
  - [1] https://www.localcan.com/pricing
