# Gladiolus

> vm.gl | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vm/ | JSON https://fshy.ajam.dev/api/v1/entity/vm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gladiolus (vm.gl)

- `compute/gladiolus-vm-gl` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-30T17:54:18.843Z (live) | stale on 2026-11-30
- url https://vm.gl/
- free tier: 'Virtual machines for people building things that deserve to exist. Offered freely, without conditions or calendars.' 'Linux VMs: Full root access. Run containers, host services, build what you need.' 'No invoices: Not "free tier." Not "trial." Actually free. We don't want your credit card or your growth metrics.' 'No expiration: Keep it running as long as you need it.' 'Human review: We read every request.' | unit: none | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: perpetual-free
- per-object cap: not applicable | source: [1] | note: the ceiling that matters is the machine shape
- retention: 'No expiration: Keep it running as long as you need it.' No inactivity or deletion term is stated. | source: [1] | note: a machine record: what is lost is the running process
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a request read by a human; no card is asked for, and the page states no conditions
- interface: ssh
- limits:
  - write-gated (binding): a human reads every request, so the gate is a decision by one person and not a quota; the number of VMs is not published [1]
- limits note: a human reads every request, so the gate is a decision by one person and not a quota; the number of VMs is not published
- binding note: the same as limits note
- interface detail: full root access to a Linux VM; the access route is not otherwise stated
- tooling: a Linux VM with root access; no client is named on the page
- composes with: a machine with root access and no invoice composes with the free always-on lane as a second address, and with a CI runner as the deploy target
- reliability: On 2026-10-30 vm.gl accepted no TCP connection on port 443 or on its HTTP port from one vantage point, and an HTTPS GET of the page timed out; the page text was returned by a third-party reader the same day.
- notes: The machine shape, the egress term and the number of machines are not published, so the record carries no numbers rather than estimates. A human reviews each request, which makes the gate a judgement and therefore unpredictable in a way a quota is not. The page names two sites, Highland, Illinois, and Sandefjord, Norway, the second marked 'Coming soon'.
- extras:
  - facets.class: perpetual-vps
- evidence:
  - [1] 2026-10-22: 'Offered freely, without conditions or calendars' and 'Linux VMs - Full root access. Run containers, host services, build what you need.', quoted from the page read on 2026-10-22
  - [1] 2026-10-30: the page states the VMs are free with no invoice and no card, not a free tier or a trial | capture: sha256:0a44080d650f5315e07901f69934a7d6229902073b9ef2c5a418d3efea917aa9 | quote: Not "free tier." Not "trial." Actually free. We don't want your credit card or your growth metrics.
  - [1] 2026-10-30: the page states the VM has no expiration | capture: sha256:0a44080d650f5315e07901f69934a7d6229902073b9ef2c5a418d3efea917aa9 | quote: Keep it running as long as you need it.
  - probe:vm.gl:443 2026-10-30: a TCP connection to vm.gl port 443 timed out on 2026-10-30 | capture: sha256:502ec93954a589557f8209f195d5d28d39d80201465ed62c81a91c28864f00a4 | quote: "err": "TimeoutError('timed out')"
  - probe:vm.gl:80 2026-10-30: a TCP connection to vm.gl port 80 timed out on 2026-10-30 | capture: sha256:fda505dc2afd166c374b99d031316fe7862802ad129f723e58cd626acec63f49 | quote: "err": "TimeoutError('timed out')"
  - probe:https://vm.gl/ 2026-10-30: an HTTPS GET of https://vm.gl/ failed with a connect timeout on 2026-10-30 | capture: sha256:e6ed860854992c4d1c938e0e310ca42a9d5a951914e4dcc316a7a0b45dcfd204 | quote: "error": "timeout"
  - probe:vm.gl:443 2026-10-30: a second TCP connection to vm.gl port 443, about 12 minutes after the first, also timed out | capture: sha256:1ad5f933865cf9cf2dbae17118574db267a6b8c8e5877ea5a7d3d21e0598134f | quote: "err": "TimeoutError('timed out')"
  - probe:https://1.1.1.1/dns-query?name=vm.gl&type=A 2026-10-30: vm.gl still resolves on 2026-10-30, to 128.254.226.29, so the name has not lapsed | capture: sha256:c0bb47afd45570af7f83c9115425347ee88b8d5ea58144b58663434707f867a6 | quote: "data":"128.254.226.29"
  - [1] 2026-10-30: the Norway site is not yet open; the Illinois site is the one in service | capture: sha256:0a44080d650f5315e07901f69934a7d6229902073b9ef2c5a418d3efea917aa9 | quote: A retired nuclear bunker on the Norwegian coast. Cold war infrastructure, repurposed for something more hopeful. Coming soon.
  - [1] 2026-10-30: every request is read by a person; no quota or number of VMs is stated | capture: sha256:0a44080d650f5315e07901f69934a7d6229902073b9ef2c5a418d3efea917aa9 | quote: We read every request. If your project makes the internet a little better, we'll find room for it.
  - [1] 2026-10-30: the VM gives full root; the page's whole text names no traffic or egress term | capture: sha256:0a44080d650f5315e07901f69934a7d6229902073b9ef2c5a418d3efea917aa9 | quote: Full root access. Run containers, host services, build what you need.
- sources:
  - [1] https://vm.gl/
