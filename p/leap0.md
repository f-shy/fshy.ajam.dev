# Leap0

> leap0.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leap0/ | JSON https://fshy.ajam.dev/api/v1/entity/leap0.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leap0

- `compute/leap0` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-24T13:20:55.904Z (live) | stale on 2026-12-25
- url https://leap0.dev/
- free tier: Free during public preview — no credit card required; published rates $0.0504 per vCPU-hour and $0.0162 per GB-hour apply when billing goes live. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: A sandbox has a 10 GiB disk rather than an object cap; the maximum request or response is 10 MiB. | source: [1]
- retention: A sandbox has a 10 GiB disk and a 10 MiB maximum request or response; disk durability across stops and deletions is not published. | source: [1]
- egress: Sandbox egress is restricted by a per-sandbox firewall to allowed domains (allow_domains) or ranges (allow_cidrs); outbound TCP, DNS and CIDR access are refused by default; no volume allowance or price is published. | metered: no | source: [1]
- identity: email | detail: unverified: no credit card is required for the free public preview; dashboard sign-in fields are not published
- interface: rest
- limits:
  - per-ip-shaping (binding): egress is restricted by a per-sandbox allowlist of domains or ranges; outbound TCP, DNS and CIDR access are refused by default [1]
  - request-rate: sandbox timeout is configurable from 1 minute to 8 hours with a 5 minute default [1]
- limits note: The sandbox timeout ranges from 1 minute to 8 hours with a 5 minute default; the API rate limit is 1000 requests per 60s; an idle-reap clock is not published.
- interface detail: REST API authenticated with an API key in the authorization or leap0-authorization header; Execute, File, Git and Desktop APIs are listed.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the spin-up time and the egress policy. The page publishes no plan or price, so the free-tier claim cannot be settled; the network answer is what it does establish
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.wall_clock_min: 5
  - session_cap.idle_reap_s: 300
  - session_cap.restart_required: no
  - session_cap.note: the timeout defaults to 5 minutes and is configurable from 1 minute to 8 hours; auto-pause uses the same knob
  - free_tier_kind: allowance
  - burst_x: 1.0
  - net.out: yes
  - net.in: no
  - net.ports: egress only, by domain allowlist; outbound TCP restricted
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Give every agent its own machine. Spin up in 100ms, run code, tear down.' and 'Lock down network egress with domain allowlists. Block data exfiltration and reverse shells.' with the demo showing 'Egress restricted' and 'Outbound TCP restricted', quoted
  - [1] 2026-11-03: egress is restricted by domain allowlist | capture: sha256:e250664dcad41630207658aabd2434385eda2cc2c3c055aafba1b66f9aa35bbe | quote: Lock down network egress with domain allowlists. Block data exfiltration and reverse shells.
  - [1] 2026-11-03: a domain outside the allowlist is refused | capture: sha256:e250664dcad41630207658aabd2434385eda2cc2c3c055aafba1b66f9aa35bbe | quote: ✗ Error: Domain not in allow_domains
  - [1] 2026-11-04: egress is controlled by a per-sandbox allowlist of domains or ranges; the page states no TCP block, egress volume or price | capture: sha256:e250664dcad41630207658aabd2434385eda2cc2c3c055aafba1b66f9aa35bbe | quote: Leap0 supports per-sandbox firewall controls so you can allow only the domains or ranges your workflow actually needs.
  - [2] 2026-11-18:  | capture: sha256:d1cc2bbf387bd2f58644b6c5cb4ed934e35f8d33390374f87fc11811c4007921 | quote: Timeout | 1 min - 8 hours (default 5 min)
  - [1] 2026-11-24: the homepage offers a free preview with no card and says rates apply when billing goes live | capture: sha256:e250664dcad41630207658aabd2434385eda2cc2c3c055aafba1b66f9aa35bbe | quote: Free during public preview — no credit card required. The rates below apply when billing goes live.
  - [1] 2026-11-24: network egress is controlled by a per-sandbox domain or range allowlist | capture: sha256:e250664dcad41630207658aabd2434385eda2cc2c3c055aafba1b66f9aa35bbe | quote: Leap0 supports per-sandbox firewall controls so you can allow only the domains or ranges your workflow actually needs.
  - [3] 2026-11-24: the platform has an authenticated programmatic API | capture: sha256:358f67bd4c121e0447ab84f398de1af7384610a780cd3f6cd822e66139e238bd | quote: API keys authenticate all requests to the Leap0 API.
  - [2] 2026-11-24: the sandbox timeout range and default | capture: sha256:d1cc2bbf387bd2f58644b6c5cb4ed934e35f8d33390374f87fc11811c4007921 | quote: Timeout | 1 min - 8 hours (default 5 min)
  - [2] 2026-11-24: the sandbox disk ceiling | capture: sha256:d1cc2bbf387bd2f58644b6c5cb4ed934e35f8d33390374f87fc11811c4007921 | quote: Disk | 10 GiB
  - [2] 2026-11-24: the per-request size ceiling | capture: sha256:d1cc2bbf387bd2f58644b6c5cb4ed934e35f8d33390374f87fc11811c4007921 | quote: Max request/response | 10 MiB
- sources:
  - [1] https://leap0.dev/
  - [2] https://leap0.dev/docs/limits
  - [3] https://leap0.dev/docs/api-keys
