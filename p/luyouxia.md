# LuYouXia

> luyouxia.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/luyouxia/ | JSON https://fshy.ajam.dev/api/v1/entity/luyouxia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LuYouXia

- `egress/luyouxia` | fails-egress | evidence documented | binding volume-quota | category tcp port forward | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-25T17:26:44.697Z (live) | stale on 2026-12-26
- url https://www.luyouxia.com/price
- price USD 0
- free tier: Trial edition, 0 yuan per year: 1 G of traffic per month, 1 Mbps, 2 routes; supported protocols TCP and HTTP; cleared automatically after 30 days. [translated] | unit: GB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 GB per month on the trial edition.; ingress: tcp | metered: yes | free allowance: 1 GB per month on the trial edition. | source: [1]
- identity: national-id | detail: unverified: the registration page could not be read on 2026-11-25: https://www.luyouxia.com/register.html answers HTTP 404, and https://www.luyouxia.com/reg.html redirects to the homepage, so the gate is not established. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 GB per month [1]
  - per-ip-shaping: 1 Mbps on the trial edition [1]
  - retention-clamped: trial mappings cleared automatically after 30 days [1]
- binding note: Monthly bandwidth allowance is 1 GB (approximately 0.0009 TiB) and port mappings expire after 30 days.
- interface detail: Windows client for device management, a Docker image for Linux, and a web console for mappings.
- tooling: vendor client on Windows/Linux/Docker plus wg-quick on the local box, which the tunnel cannot carry
- composes with: TCP only and purged monthly, so it serves a demo endpoint and not a WG peer.
- reliability: Trial mappings are deleted after 30 days, and the vendor's own matrix marks the trial tier as having no SLA and no rapid failover.
- notes: The price table is script-built: the reader returned navigation chrome and the numbers came from the raw HTML, which is why the protocol row is quotable at all. No UDP on the trial tier; whether a paid tier adds UDP is not stated on the page read.
- evidence note: The plan table was read out of the page HTML after the text extractor returned navigation only. The identity gate is unverified.
- extras:
  - wg_path: none
  - wg_detail: The trial edition's protocol row lists TCP and HTTP only. A 45 KB read of the pricing page contains no occurrence of UDP, and the native-port mapping the help centre describes is a TCP forward.
  - ingress: tcp
  - volume_tib_month: 0.00091
  - volume_stated: 1 GB per month on the trial edition.
  - bytes_transit: yes
  - transit_note: Vendor relays on multi-carrier domestic lines carry the tunnel.
- evidence:
  - [1] 2026-10-23: trial edition is 0 yuan/year, 1 Mbps, 2 routes, 1 G/month, TCP and HTTP only, cleared after 30 days
  - [2] 2026-11-25: the registration page answers HTTP 404 | capture: sha256:6d1808687a0bcd10c0e8c5b6f4e7e3cf52187366391a6c175d99c4d7b540dd91 | quote: 404 NOT FOUND
  - [1] 2026-11-25: the trial edition includes 1 GB of traffic a month | capture: sha256:9268a19544fbb21525b3e16f9555a73d765fd49ee3e9ca86123bf17fa4dfa26e | quote: 每月1G流量
  - [1] 2026-11-25: the trial edition is shaped to 1 Mbps | capture: sha256:9268a19544fbb21525b3e16f9555a73d765fd49ee3e9ca86123bf17fa4dfa26e | quote: 1Mbps
  - [1] 2026-11-25: trial mappings are cleared after 30 days | capture: sha256:9268a19544fbb21525b3e16f9555a73d765fd49ee3e9ca86123bf17fa4dfa26e | quote: 超过30天自动清除
  - [1] 2026-11-25: the trial edition carries TCP and HTTP only | capture: sha256:9268a19544fbb21525b3e16f9555a73d765fd49ee3e9ca86123bf17fa4dfa26e | quote: TCP、HTTP
- sources:
  - [1] https://www.luyouxia.com/price
  - [2] https://www.luyouxia.com/register.html
