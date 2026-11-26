# InstaTunnel

> instatunnel.my | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/instatunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/instatunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InstaTunnel

- `egress/instatunnel` | fails-egress | evidence documented | binding volume-quota | category http tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:23:43.556Z (live) | stale on 2026-12-26
- url https://instatunnel.my/pricing
- price USD 0 (Pro USD 5/month) | parsed USD 5/mo
- free tier: Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains. | unit: mixed | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Free plan: 2GB monthly bandwidth and 2,000 daily requests; ingress: http-only | metered: no | free allowance: 2GB monthly bandwidth | source: [1]
- identity: email | detail: 'Start Free' account; MCP endpoints need Pro. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 2GB monthly bandwidth on the free plan; sessions last 24 hours [1]
  - request-rate: 3 tunnels, 2,000 daily requests and 24-hour sessions on free [1]
- binding note: The free plan is capped at 2GB monthly bandwidth, 2,000 daily requests and 24-hour sessions.
- interface detail: npm install -g instatunnel.
- tooling: npm CLI.
- composes with: Webhook ingress only.
- reliability: Tunnels expire every 24 hours on free and the URL changes.
- notes: The 24-hour session beats ngrok's 2 hours, which is the vendor's whole pitch. Still HTTP.
- evidence note: The free plan publishes a 2GB monthly bandwidth figure; a TCP or UDP tunnel type would change the verdict.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: 2GB monthly bandwidth on the free plan
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: free column: 3 simultaneous tunnels, 24h sessions, FREE; no bandwidth figure
  - [1] 2026-11-25: the free plan publishes a 2GB monthly bandwidth figure | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: free bandwidth and request allowances are published | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: free bandwidth is published | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: the binding limit is a monthly byte allowance | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: allowance and session length | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: binding constraint is the monthly byte allowance | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: the caps that bind | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: tunnel, request and session caps | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: free plan contents | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: byte figure is published | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: Yes. Free has no time limit and includes 3 tunnels, 2GB monthly bandwidth, 2,000 daily requests, 24-hour sessions, and custom subdomains.
  - [1] 2026-11-25: no card is asked for on the free plan | capture: sha256:7dbd555be492b241b64df70aed06545b60637677792fcc174f61e3982112ff9b | quote: - No credit card required
- sources:
  - [1] https://instatunnel.my/pricing
