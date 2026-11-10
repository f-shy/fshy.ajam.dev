# zrok

> zrok.io | Storage, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zrok/ | JSON https://fshy.ajam.dev/api/v1/entity/zrok.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## zrok (netfoundry public instance)

- `storage/zrok` | fails-egress | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:23.416Z (live) | stale on 2026-12-04
- url https://zrok.io/pricing/
- free tier: none reachable: Free plan is bandwidth-metered at 5 GB/day over a rolling 24-hour window, with 50 share backends. It is a tunnelling service, so all traffic transits their edge. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Free plan: 5 GB per day over a rolling 24-hour window; past it running shares are disabled and new shares are refused until usage falls under the limit. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: pages read on 2026-11-03: zrok.io/pricing/ (Free plan: 5 Daily GB, 50 Share Backends (Ephemeral or Reserved)) and netfoundry.io/docs/zrok/myzrok/service-limits (running shares are disabled and new shares are refused when the daily bandwidth is exceeded, until bandwidth falls below the 24-hour limit; Bandwidth limits are based on a rolling 24-hour window.). The identity cost was not read on a vendor page and stays as recorded.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free plan is bandwidth-metered at 5 GB/day over a rolling 24-hour window, with 50 share backends. It is a tunnelling service, so all traffic transits their edge.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free plan is bandwidth-metered at 5 GB/day over a rolling 24-hour window, with 50 share backends. It is a tunnelling service, so all traffic transits their edge.
  - [2] 2026-10-21: cited as the basis of the rejection: Free plan is bandwidth-metered at 5 GB/day over a rolling 24-hour window, with 50 share backends. It is a tunnelling service, so all traffic transits their edge.
  - [1] 2026-11-03: Free plan bandwidth is 5 GB per day | capture: sha256:dbab29b5a316f93b18c0f096b82b790595b110319f919276d3c037e807afd0ed | quote: 5 Daily GB
  - [3] 2026-11-03: exceeding the daily bandwidth disables shares | capture: sha256:ed056d3ff98f500ca07451090336a492c4ef9ca628abf7060c1f3b05e5c9cb97 | quote: If you exceed the daily bandwidth of your plan, any running shares are disabled and the zrok API prevents new shares from being created until bandwidth falls below the 24-hour limit.
  - [3] 2026-11-03: the daily limit is measured over a rolling 24-hour window | capture: sha256:ed056d3ff98f500ca07451090336a492c4ef9ca628abf7060c1f3b05e5c9cb97 | quote: Bandwidth limits are based on a rolling 24-hour window.
  - [1] 2026-11-03: the Free plan lists 50 Share Backends (Ephemeral or Reserved) | capture: sha256:dbab29b5a316f93b18c0f096b82b790595b110319f919276d3c037e807afd0ed | quote: 50 Share Backends (Ephemeral or Reserved)
- sources:
  - [1] https://zrok.io/pricing/
  - [2] https://www.globalnerdy.com/2026/09/22/can-you-use-zroks-free-hosted-plan-for-your-teams-internal-tool-or-5-questions-answered/
  - [3] https://netfoundry.io/docs/zrok/myzrok/service-limits

## zrok (hosted)

- `egress/zrok-hosted` | fails-quota | evidence documented | binding volume-quota | category tunnel (hosted, OpenZiti)
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://zrok.io/pricing/
- free tier: 5 GB/day, 25 environments, 50 share backends, 50 private access frontends | unit: GB | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a rolling daily allowance rather than a per-object cap
- retention: 5 GB per rolling 24 hours; shares are restricted on exceed | source: [1]
- egress: metered at 5 GB/day, which is 0.5% of one day's workload | metered: yes | free allowance: 5 GB per rolling 24 hours | source: [1]
- identity: email | detail: a zrok account; no card required
- interface: cli
- limits:
  - volume-quota (binding): 5 GB per rolling 24 hours; on crossing it the running shares are disabled and new shares refused until the window falls back below the limit [1]
  - request-rate: 2000 requests per 300 s per IP address [2]
  - request-rate: 7500 requests per 300 s per share, from any number of addresses [2]
- limits note: the allowance is a byte volume over a period, which none of the six kinds names; the number is in egress.free_allowance and binding names per-ip-shaping as the nearest kind
- binding note: 5 GB per rolling 24 hours is 150 GB in 30 days, or 0.136 TiB, so the daily byte window bands the month at about 7.3 times below 1 TiB. Crossing it disables running shares and refuses new ones until the window falls back, which is a hard stop rather than a throttle. Two request-rate caps sit underneath and would bind first for a request-heavy workload.
- interface detail: zrok share public against the hosted controller
- tooling: part of interface detail
- composes with: composes with an origin and no domain, and the daily allowance is what stops it. The self-hosted build is the same software without the controller's journal.
- reliability: The limits agent has twice failed to release a limit once usage fell: a 2024 discourse thread and a 2026 repository commit both describe an account staying limited until the journal entry was cleared by hand.
- notes: Hosted zrok service provides public tunnel endpoints with a 10 GB daily transfer allowance (approximately 300 GB monthly).
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the hosted controller relays the share's bytes, which is what the 5 GB daily counter counts
  - wg_path: none
- evidence:
  - [1] 2026-10-22: '5 Daily GB' in the Free column of the rendered HTML; the Markdown extraction drops it
  - [3] 2026-10-23: 'udpTunnel: Forwards raw UDP traffic to a target server' and the private-share access rule
  - [4] 2026-10-23: 'zrok supports HTTP-based backends and raw TCP/UDP backends'
  - [1] 2026-10-23: the free tier is 25 environments and 50 share backends; the 5 GB/day figure is no longer on the pricing page
- sources:
  - [1] https://zrok.io/pricing/
  - [2] https://github.com/openziti/zrok/commit/5a052ee86b84ac9c94ce37804c573f1199f44ec4
  - [3] https://netfoundry.io/docs/zrok/concepts/private-shares/
  - [4] https://netfoundry.io/docs/zrok/concepts/backend-modes/
