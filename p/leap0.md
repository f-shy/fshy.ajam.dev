# Leap0

> leap0.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leap0/ | JSON https://fshy.ajam.dev/api/v1/entity/leap0.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leap0

- `compute/leap0` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T06:20:47.729Z (live) | stale on 2026-12-05
- url https://leap0.dev/
- free tier: machines that spin up in 100 ms and tear down; egress is restricted by domain allowlist, with outbound TCP and DNS exfiltration blocked by default | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Sandbox egress is restricted by a per-sandbox firewall that allows only the allowed domains (allow_domains) or ranges (allow_cidrs); outbound TCP is restricted, not stated as blocked; no volume allowance or price is published on the page read | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - per-ip-shaping (binding): egress is restricted by domain allowlist: outbound TCP and DNS exfiltration are refused by default [1]
  - request-rate: a machine spins up in 100 ms and is torn down after the run [1]
- limits note: Session cap, idle-reap and network policy are not documented. Prelaunch only.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the spin-up time and the egress policy. The page publishes no plan or price, so the free-tier claim cannot be settled; the network answer is what it does establish
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a machine is created per run and torn down; the page states no idle clock
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
- sources:
  - [1] https://leap0.dev/
