# OutRay

> outray.dev | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/outray/ | JSON https://fshy.ajam.dev/api/v1/entity/outray.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OutRay

- `egress/outray` | fails-quota | evidence documented | binding volume-quota | category tunnel (hosted, HTTP-first) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://outray.dev/pricing
- price USD 0
- free tier: 2 Tunnels, 0 Custom Domains, 1 Subdomain, 1 Team Member, 2GB Bandwidth | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2GB Bandwidth on the free plan; 25GB on Ray at USD 7/month; ingress: tcp+udp | metered: yes | free allowance: 2GB Bandwidth on the free plan; 25GB on Ray at USD 7/month | source: [1]
- identity: email | detail: 'Get Started Free' leads to https://outray.dev/signup | country: None
- interface: cli
- limits:
  - volume-quota (binding): 2GB bandwidth [1]
- binding note: 2 GB is 0.0018 TiB and the next tier is 25 GB, so no purchasable step reaches one TiB either.
- interface detail: outray 3000
- tooling: outray CLI, Vite and Next plugins
- composes with: not usable at this volume
- reliability: single small vendor; no published rate
- notes: Read only to price the free tier. The UDP capability is asserted in the page metadata ('Supports HTTP, TCP, and UDP protocols') and was not observed in a setup page.
- evidence note: The UDP claim rests on the site's own meta description, not on a UDP setup page; that is why ingress is recorded as tcp+udp and the verdict rests on the quota, which is not in doubt.
- extras:
  - wg_path: none
  - wg_detail: the free plan publishes no UDP port and no reserved port; the product page lists HTTP, TCP and UDP as supported protocols but the pricing table's free column is bandwidth and tunnel count only
  - ingress: tcp+udp
  - volume_tib_month: 0.001819
  - volume_stated: 2GB Bandwidth on the free plan; 25GB on Ray at USD 7/month
  - bytes_transit: yes
  - transit_note: the OutRay edge carries the traffic
- evidence:
  - [1] 2026-10-23: free plan is 2 tunnels and 2GB bandwidth
  - [2] 2026-10-23: 'an open-source alternative to ngrok', npm install -g outray
- sources:
  - [1] https://outray.dev/pricing
  - [2] https://outray.dev/
