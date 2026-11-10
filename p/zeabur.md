# Zeabur

> zeabur.com | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zeabur/ | JSON https://fshy.ajam.dev/api/v1/entity/zeabur.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zeabur (Free Plan)

- `compute/zeabur` | qualifies-with-caveat | evidence documented | binding retention-clamped | category platform host | tier Free Plan
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:26.171Z (live) | stale on 2026-12-05
- url https://zeabur.com/docs/en-US/pricing/free-plan
- free tier: Free Plan at USD 0: 'No credit card required', deploy as many projects and services as you like from GitHub, with services that 'automatically sleep after a period of inactivity'. | unit: mixed | metered on: unstated | read on: 2026-10-24 | source: [1]
- per-object cap: a single file upload is capped at 50 MB on Free; 48 hours of log retention; build machine 2C4G
- retention: 48 hours of logs on Free; no statement about service data
- egress: the current plan pages state no egress allowance; the network traffic changelog states US$1 / 10GB beyond a free quota of 100GB (developers and teams) or 10GB (serverless plan users), which may be superseded | metered: yes | free allowance: 100 GB (developers and teams) or 10 GB (serverless plan users), per the network traffic changelog; not stated on the current plan pages | price per TB: USD 100 per TB | source: [2]
- identity: email | detail: 'No credit card required — just sign up and start deploying'
- interface: cli
- limits:
  - retention-clamped (binding): services on the Free Plan sleep after a period of inactivity; the interval is not published [1]
  - volume-quota: 10 GB of network usage free on the serverless plan, then USD 1 per 10 GB or automatic suspension [2]
  - per-object-cap: 50 MB single-file upload; 0 advanced-model agent messages; no email sends [3]
- binding note: sleep is the first thing that matters and the vendor does not publish the timeout, so the row cannot be planned against.
- interface detail: Zeabur CLI (npx zeabur, token login for CI), GitHub deploys and the dashboard; the plan comparison lists API Keys as a quota but no API reference was read
- tooling: not stated
- composes with: not established
- reliability: the sleep interval is unpublished, so 'a period of inactivity' cannot be sized; the vendor also states the Free Plan carries no SLA
- notes: The Free Plan does deploy serverless services, without a card, and they sleep. The old USD 5 monthly credit is gone. What is not established is whether the Free Plan has any compute allowance at all or is metered against a card-free quota, and the sleep interval.
- evidence note: the Free Plan page was read and states the auto-sleep and the no-card rule; the sleep duration and any compute allowance are not published on it
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: free
  - session_cap.restart_required: no
  - session_cap.note: sleeps after an unpublished period of inactivity; wakes on the next request
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: serverless HTTP services; no long-lived listening socket is documented
  - network_out.static_ip: no
  - network_out.ipv6: no
  - free_tier_kind: free-plan
  - ps.price: a user's own server storage
  - ps.durability: a user's own server
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.max_retention: as long as a user keeps it
  - net.out: yes
  - net.in: yes
  - net.ports: a user's own server
  - term: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: no plan fee; usage above the free allowances is billed or suspends the service
- evidence:
  - [3] 2026-10-02: 
  - [3] 2026-10-22: 'Compute: manageable own servers - servers you purchased and own elsewhere ... you can still manage them from the Zeabur dashboard - 1 / 3 / 10 / Unlimited', with 'Email: daily quota 0 / 100 / Unlimited' and 'Single file upload size limit 50 MB' on the free column, quoted
  - [1] 2026-10-24: quoted: 'The Free Plan is Zeabur's free tier, designed for personal exploration and learning. No credit card required — just sign up and start deploying.'
  - [1] 2026-10-24: quoted: 'Auto-sleep — Services on the Free Plan automatically sleep after a period of inactivity. They wake up on the next incoming request, which may cause a few seconds of cold-start latency.'
  - [3] 2026-10-24: quoted feature table: 'Single file upload size limit | 50 MB' on Free, 'Log retention | 48h', 'Manageable own servers | 1'
  - [4] 2026-10-24: quoted: 'Previously, the Free Plan generously provided a $5 monthly usage credit' and 'No more need to tether a payment method or manually extend your access.'
  - [2] 2026-11-03: overage price US$1 per 10 GB | capture: sha256:1b5d7675363fb8249f81249652c064634b1839d6d9111091d079e101e6147d03 | quote: We charge the network traffic for a basic free quota and usage based fees for traffic beyond the free quota. The price is US$1 / 10GB
  - [2] 2026-11-03: 100 GB free quota for developers and teams | capture: sha256:1b5d7675363fb8249f81249652c064634b1839d6d9111091d079e101e6147d03 | quote: There will be a free quota of 100GB network usage. You only have to pay the part beyond the free quota.
  - [5] 2026-11-03: a CLI exists | capture: sha256:2ea8cd67577e3935a3e7e0884b789a82276f812590b1850c672752b1c786dd8e | quote: Zeabur CLI lets you manage all Zeabur resources from your terminal — deploy services, view logs, manage projects, without opening the Dashboard.
- sources:
  - [1] https://zeabur.com/docs/en-US/pricing/free-plan
  - [2] https://zeabur.com/changelogs/introduction-of-network-traffic-fees
  - [3] https://zeabur.com/pricing
  - [4] https://zeabur.com/changelogs/say-hello-to-the-serverless-plan
  - [5] https://zeabur.com/docs/en-US/developer/cli

## Zeabur (free)

- `egress/zeabur` | fails-egress | evidence documented | binding volume-quota | category paas l4 port | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://zeabur.com/docs/en-US/pricing/free-plan
- price USD 0
- free tier: The Free Plan is Zeabur's free tier, designed for personal exploration and learning. No credit card required - just sign up and start deploying. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The Free Plan documentation states no monthly byte allowance; it lists only auto-sleep, no SLA, no Zeabur Email, and no backup or log forwarding.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: "No credit card required - just sign up and start deploying." | country: None
- interface: cli, rest
- limits:
  - volume-quota (binding): no published monthly byte allowance on the Free Plan [1]
- binding note: Transport fails first: cloud services offer HTTP or TCP only, and the Free Plan auto-sleeps idle services, which ends a tunnel.
- interface detail: Dashboard and CLI; ports declared per service with a type of HTTP or TCP.
- tooling: Dashboard, CLI, and templates; port type chosen per service port.
- composes with: Zeabur on a self-managed server could open UDP through that server's firewall; the free cloud tier cannot.
- reliability: Free Plan services auto-sleep when idle and wake on the next request; a sleeping service cannot hold a tunnel. Forwarded host and port may change.
- notes: The UDP evidence in Zeabur's own templates is tied to dedicated-server projects, i.e. a server rented elsewhere and attached. That is not a free platform port. Ports are also documented as possibly changing.
- evidence note: Whether the Free Plan may attach a TCP port at all is not stated; the plan page limits itself to sleep, SLA and feature exclusions.
- extras:
  - wg_path: none
  - wg_detail: TCP ports only on cloud services: "Port Type can be HTTP or TCP ... TCP ports can be accessed with an auto-assigned hostname and port (e.g., reg.clusters.zeabur.com:12345)". UDP appears only in templates running on dedicated-server projects.
  - ingress: tcp
  - volume_stated: The Free Plan documentation states no monthly byte allowance; it lists only auto-sleep, no SLA, no Zeabur Email, and no backup or log forwarding.
  - bytes_transit: yes
  - transit_note: Zeabur's cluster ingress forwards TCP to the service.
- evidence:
  - [1] 2026-10-23: Free Plan, no card, auto-sleep after inactivity, no SLA
  - [2] 2026-10-23: "Port Type can be HTTP or TCP" with TCP reachable at an auto-assigned hostname and port
  - [3] 2026-10-23: sync-udp 22000/UDP forwarded entry, but "On dedicated server projects this will be your server's public IP"
- sources:
  - [1] https://zeabur.com/docs/en-US/pricing/free-plan
  - [2] https://zeabur.com/docs/en-US/deploy/methods/custom-docker-image
  - [3] https://zeabur.com/templates/1NIQIX
