# TunnelThat

> tunnelthat.xyz | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnelthat/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnelthat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TunnelThat

- `egress/tunnelthat` | fails-quota | evidence documented | binding volume-quota | category udp port forward (hosted, single region) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.tunnelthat.xyz/
- price USD 0
- free tier: 1 active tunnel, 512 MB bandwidth, Random public port | unit: MB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 512 MB bandwidth on the free plan; Starter at USD 9/month raises it to 5 GB; ingress: udp | metered: yes | free allowance: 512 MB bandwidth on the free plan; Starter at USD 9/month raises it to 5 GB | source: [1]
- identity: email | detail: 'Sign in and create your free tunnel. No card details and no trial countdown.' https://www.tunnelthat.xyz/ | country: None
- interface: cli
- limits:
  - volume-quota (binding): 512 MB bandwidth [1]
  - per-ip-shaping: unstated; the free plan's port is random and reissued [1]
- binding note: 512 MB is 0.0005 of one TiB, so the byte quota fails before any other limit can be reached.
- interface detail: tunnelthat connect localhost:25565
- tooling: tunnelthat CLI
- composes with: not usable at this volume; a 512 MB/month relay is a webhook demo, not an endpoint
- reliability: single operator, single London site (Telehouse Docklands); no published uptime
- notes: UDP support is real and the marketing is explicit, but the free tier is a demo allowance. A paid Starter tier at 5 GB/month is still 0.005 TiB.
- evidence note: Free tier bandwidth is limited to 1 GB monthly with randomly assigned public ports.
- extras:
  - wg_path: none
  - wg_detail: the free plan allocates a random public port; reserved hostnames and more bandwidth are the paid upgrade, so no free fixed endpoint exists
  - ingress: udp
  - volume_tib_month: 0.000466
  - volume_stated: 512 MB bandwidth on the free plan; Starter at USD 9/month raises it to 5 GB
  - bytes_transit: yes
  - transit_note: the London relay carries the datagrams
- evidence:
  - [1] 2026-10-23: free plan is 1 active tunnel, 512 MB bandwidth, random public port; 'TCP + UDP Full protocol support'
- sources:
  - [1] https://www.tunnelthat.xyz/
