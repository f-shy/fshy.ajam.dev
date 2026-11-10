# Sevalla

> sevalla.com | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sevalla/ | JSON https://fshy.ajam.dev/api/v1/entity/sevalla.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sevalla (Compute)

- `compute/sevalla` | paid-only | evidence documented | binding write-gated | category platform host | tier Static site hosting (free) / Application hosting (paid)
- needs card unknown, phone no, ID no, institution no | verified 2026-10-24T01:55:00.000Z (live) | stale on 2026-11-24
- url https://sevalla.com/pricing/
- price parsed USD 5/mo
- free tier: static site hosting at USD 0 a month; application hosting starts at USD 5 a month and offers only a free trial, with no perpetual free container | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable to application hosting: there is no free application tier
- retention: not applicable: nothing free to retain
- egress: no egress fee is stated for application hosting; static hosting and object storage carry their own terms | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: an account for the free static tier; a card is needed for the USD 5 application tier, which was not tested
- interface: unknown
- limits:
  - write-gated (binding): no free application or database tier: 'Application hosting ... from $5 USD / month ... Free trial is available' [1]
- limits note: the 1 GB per-site limit is the first wall for anything serving datasets; 100 GB of bandwidth is second, and there is no free application or database container at all.
- binding note: there is no free container at all, so nothing else can bind.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 100 free static sites at 1 GB each is up to 100 GB of published assets with 100 GB/month of egress, which can front a catalogue whose bytes live in object storage elsewhere; it cannot run a process.
- reliability: no reliability event recorded
- notes: Kinsta's PaaS; the Kinsta static product redirects here, so one record covers both. The Kinsta WordPress row is separate and also paid.
- evidence note: the pricing page read lists application hosting from USD 5 with a free trial and static hosting at USD 0; documented records claim that there is no free app container is confirmed
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: perpetual-allowance
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 5.0
  - m24h_usd: 5.0
  - price_arithmetic: USD 5.00 a month is the entry application price; no free allowance
  - free_tier_kind: static-only
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: the application port
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: not stated for the paid application tier
- evidence:
  - [1] 2026-10-22: Static site hosting Free USD 0/month: 1GB size limit/site, 100GB free bandwidth, 600 free build minutes, 100 sites per account, quoted
  - [1] 2026-10-22: Application hosting from USD 5/month and database hosting from USD 5/month, each marked 'Free trial is available' with no free plan listed, quoted
  - [2] 2026-10-22: the Kinsta static-site-hosting URL now serves the Sevalla page (final_url https://sevalla.com/static-site-hosting/, author Kinsta), so the two products are one
  - [1] 2026-10-24: quoted: 'Application hosting / Scale as you go from / $5 / USD / month ... Free trial is available'
  - [1] 2026-10-24: quoted: 'Static site hosting / 260+ global edge locations / Free / USD / month'
- sources:
  - [1] https://sevalla.com/pricing/
  - [2] https://kinsta.com/static-site-hosting/

## Sevalla (free)

- `egress/sevalla` | paid-only | evidence documented | binding volume-quota | category paas l4 port | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://docs.sevalla.com/applications/networking
- price USD 5
- free tier: Scale as you go from $5 USD / month. Deploy your applications in minutes. Free trial is available. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No free application tier. External bandwidth is $0.1 per GB on the H1 $5/month pod.; ingress: tcp | metered: yes | free allowance: No free application tier. External bandwidth is $0.1 per GB on the H1 $5/month pod. | source: [2]
- identity: email | detail: Account signup; the free trial is time-limited, and the cheapest app is H1 at $5/month. | country: None
- interface: rest, cli
- limits:
  - volume-quota (binding): external bandwidth $0.1/GB; no free app tier [1]
- binding note: There is no free application tier at all: the smallest app is $5/month and 1 TiB of external bandwidth would be $102.40 on top.
- interface detail: Networking tab in the application dashboard.
- tooling: Dashboard only for proxy creation; deployments by git push or Docker image.
- composes with: A paid Sevalla app with a TCP proxy could carry SSH; no free path.
- reliability: Legacy TCP proxy endpoints disabled 2026-10-15; clients had to be repointed to the new hostname.
- notes: Free tier exists only for static sites (100 GB bandwidth), which is not a port. Legacy TCP proxy hostnames and ports were disabled on Oct 15, 2026, so an existing .proxy.sevalla.app address stopped working.
- evidence note: Reading the trial terms would fix the exact length; it would not change the verdict.
- extras:
  - wg_path: none
  - wg_detail: TCP proxies only: "Protocol | TCP. Use TLS in your own protocol if the traffic needs encryption." Port assigned from 20000-29999 or 32768-65000.
  - ingress: tcp
  - volume_tib_month: 0
  - volume_stated: No free application tier. External bandwidth is $0.1 per GB on the H1 $5/month pod.
  - bytes_transit: yes
  - transit_note: Sevalla forwards proxy connections to the process port.
- evidence:
  - [1] 2026-10-23: H1 0.3 CPU / 0.3GB $5/month; external bandwidth $0.1/GB
  - [2] 2026-10-23: "Protocol | TCP"; 3 TCP proxies per application; port from 20000-29999 or 32768-65000
- sources:
  - [1] https://sevalla.com/application-hosting/pricing/
  - [2] https://docs.sevalla.com/applications/networking
