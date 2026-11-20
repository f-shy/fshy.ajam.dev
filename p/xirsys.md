# Xirsys free

> xirsys.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xirsys/ | JSON https://fshy.ajam.dev/api/v1/entity/xirsys.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Xirsys free (Developer plan)

- `storage/xirsys-free` | fails-quota | evidence documented | binding volume-quota | category turn-relay
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:04:13.395Z (live) | stale on 2026-12-04
- url https://xirsys.com/pricing
- free tier: Developer (free) account: after day 30 it has one region, 2 channels, unlimited STUN and 500 MB per month of TURN, a hard cap (relay stops until the monthly reset); the first 30 days include all 12 production regions. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 500 MB per month of TURN on the free plan, then paid plans: Basic $39 per month (50 GB, $0.50 per GB over), Standard $99 (150 GB, $0.40 per GB over), Pro $199 (500 GB, $0.20 per GB over), Elite $499 (2 TB, $0.09 per GB over). | metered: yes
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): 500 MB per month of TURN (hard cap) [1]
- limits note: Free tier provides 500 MB per month (~16 MB per day).
- binding note: TURN is capped at 500 MB per month on the free plan and relay stops until the monthly reset; paid plans start at 50 GB per month
- interface detail: REST API issuing ICE server credentials; TURN over UDP/TCP/TLS.
- tooling: curl against the Xirsys API for channel/credential creation; standard WebRTC clients.
- composes with: no advantage over Cloudflare TURN, which gives 2,000x the free volume.
- reliability: Free tier functions as a developer test sandbox rather than high-throughput production transport.
- notes: 500 MB monthly TURN bandwidth on the free Developer plan, capped bandwidth, single geographic region after a 30-day all-region trial. STUN unlimited.
- evidence note: Pages read on 2026-11-03: xirsys.com/pricing After day 30 one region, 2 channels, unlimited STUN, 500 MB/mo TURN; 500 MB/mo TURN. A hard cap; relay stops until the monthly reset.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 500 MB monthly TURN bandwidth on the free Developer plan, capped bandwidth, single geographic region after a 30-day all-region trial. STUN unlimited.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Xirsys offer a 500 MB free tier, capped to a single region'
  - [3] 2026-10-21: 'New Free accounts can use all available regions during their first 30 days; after the trial they use their assigned home region'
  - [4] 2026-10-21: 'Developer (Free) | Free | Unlimited STUN usage; 500 MB monthly TURN bandwidth; capped bandwidth and access to a single geographic region'
  - [1] 2026-11-03: after 30 days the free account has one region, 2 channels, unlimited STUN and 500 MB per month of TURN | capture: sha256:fd59cf495800d2a181e241982ee37cc07fe82128346db2233caa9d2e7371b145 | quote: After day 30 your account remains active but will be limited to one region, 2 channels, unlimited STUN, and 500 MB/mo TURN.
  - [1] 2026-11-03: the free Developer plan caps TURN at 500 MB per month and relay stops until the reset | capture: sha256:fd59cf495800d2a181e241982ee37cc07fe82128346db2233caa9d2e7371b145 | quote: - 500 MB/mo TURN — a hard cap; relay stops until the monthly reset
  - [1] 2026-11-03: Elite includes 2 TB at $0.09 per GB over | capture: sha256:fd59cf495800d2a181e241982ee37cc07fe82128346db2233caa9d2e7371b145 | quote: 2 TBmonthly TURN bandwidth included*$0.09 /GB over*
  - [5] 2026-11-03: free sign-up asks to accept the terms and sends a verification email | capture: sha256:c38de6ed863f539628c9adb81259727d98d0992a4c7029821a58baa866117617 | quote: Send Verification Email
  - [1] 2026-11-03: Basic includes 50 GB of TURN at $0.50 per GB over | capture: sha256:fd59cf495800d2a181e241982ee37cc07fe82128346db2233caa9d2e7371b145 | quote: 50 GBmonthly TURN bandwidth included*$0.50 /GB over*
  - [1] 2026-11-03: Standard includes 150 GB at $0.40 per GB over | capture: sha256:fd59cf495800d2a181e241982ee37cc07fe82128346db2233caa9d2e7371b145 | quote: 150 GBmonthly TURN bandwidth included*$0.40 /GB over*
  - [1] 2026-11-03: Pro includes 500 GB at $0.20 per GB over | capture: sha256:fd59cf495800d2a181e241982ee37cc07fe82128346db2233caa9d2e7371b145 | quote: 500 GBmonthly TURN bandwidth included*$0.20 /GB over*
  - [1] 2026-11-03: Basic is $39 per month billed monthly | capture: sha256:fd59cf495800d2a181e241982ee37cc07fe82128346db2233caa9d2e7371b145 | quote: $39/mo
  - [1] 2026-11-03: after day 30 the free account is limited to one region, 2 channels, unlimited STUN and 500 MB/mo TURN | capture: sha256:fd59cf495800d2a181e241982ee37cc07fe82128346db2233caa9d2e7371b145 | quote: After day 30 your account remains active but will be limited to one region, 2 channels, unlimited STUN, and 500 MB/mo TURN.
- sources:
  - [1] https://xirsys.com/pricing
  - [2] https://iceperf.com/providers/xirsys
  - [3] https://docs.xirsys.com/
  - [4] https://us.fitgap.com/products/014909/xirsys
  - [5] https://global.xirsys.net/dashboard/signup
