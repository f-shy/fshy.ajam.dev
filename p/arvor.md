# Arvoris

> arvor.is | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arvor/ | JSON https://fshy.ajam.dev/api/v1/entity/arvor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Arvoris

- `egress/arvoris` | fails-egress | evidence documented | binding none | category game L4/L7 reverse proxy (Minecraft) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://arvor.is/
- price USD 0
- free tier: Free: 15 players, $0/mo, 1 network, 1 backend, Strict L4/L7 DDoS mitigation, Real client IPs (PROXY protocol) | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Bandwidth to backend per month: Fair use on Free, Unlimited on Budget and above. No byte figure is given for fair use.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'free plan, no card required'; an account at beta-panel.arvoris.net/register. The register form was not opened, so its fields are unread. | country: None
- interface: rest
- limits:
  - volume-quota: Fair use, no number published [1]
  - per-ip-shaping: free plan caps at 15 players [1]
- binding note: No numeric fair-use byte limit is published, and public documentation offers no UDP port forwarding.
- interface detail: Self-serve panel at beta-panel.arvoris.net; setup is a single DNS record on every plan.
- tooling: one DNS record, self-serve
- composes with: DNS in front of a public origin, so it hides an address but does not create one.
- reliability: Free tier is capped at 15 players and community support; the fair-use bandwidth term has no published threshold.
- notes: Budget brand of papyrus.vip with Cloudflare Spectrum protection. Product documentation describes hostname-routed Minecraft Java over TCP; no Bedrock or generic UDP line item is listed in published plan tables.
- evidence note: The plan table and FAQ are first-party and were read in full. The negative on UDP comes from the landing page and the plan comparison table only, and an absence is weaker than a statement.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard offering and no UDP port on any tier.
  - ingress: tcp
  - volume_stated: Bandwidth to backend per month: Fair use on Free, Unlimited on Budget and above. No byte figure is given for fair use.
  - bytes_transit: yes
  - transit_note: Arvoris edge on Cloudflare Spectrum capacity proxies the traffic
- evidence:
  - [1] 2026-10-23: Free plan at $0/mo: 15 players, 1 network, 1 backend, strict L4/L7, real client IPs, 24-hour analytics; no card required
  - [1] 2026-10-23: Bandwidth to backend per month is 'Fair use' on Free and 'Unlimited' from Budget up; every tier routes by DNS record and speaks Minecraft hostnames
  - [1] 2026-10-23: The stack is described as Cloudflare Spectrum powered with a hostname-aware L7 engine, which is a TCP-with-SNI shape rather than a per-customer UDP IP
- sources:
  - [1] https://arvor.is/
