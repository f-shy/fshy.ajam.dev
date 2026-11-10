# DartNode Open Source

> dartnode.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dartnode/ | JSON https://fshy.ajam.dev/api/v1/entity/dartnode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DartNode Open Source

- `compute/dartnode-open-source` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-11-02T02:17:33.710Z (live) | stale on 2026-12-03
- url https://dartnode.com/open-source
- free tier: A free KVM VPS for any public GitHub repository with 1,000 or more stars and at least 90 days of age: quoted 'Eligible projects have a public GitHub repository with 1,000+ stars that is at least 90 days old (no forks or archived repos)', auto-approved once a verification code is in the README, on a plan shaped 1 vCPU, 1 GB RAM, 10 GB SSD with IPv4 and IPv6 in Houston. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: A DartNode account and a qualifying public repository. The offer page states the account gate: 'Please log in or register to apply.' The registration form asks for a first name, a last name, an email address and a password, with Google and Discord sign-up offered, and no phone, card, country or ID-document field. The institution gate is the eligibility rule: 'Eligible projects have a public GitHub repository with 1,000+ stars that is at least 90 days old (no forks or archived repos).' A verification code is then added to the repository README to prove maintenance. The human identity is an email address; what qualifies is the project. | country: a public GitHub repository with 1,000+ stars, at least 90 days old, not a fork or an archived repository
- interface: unknown
- limits:
  - write-gated (binding): The 1,000-star repository is a hard gate that a new developer cannot satisfy tonight, and the operator has raised the threshold from 100 stars in June 2025 and has suspended issued boxes without stated cause, so the first thing that fails is the eligibility check and the second is the operator's discretion afterwards. [1]
- limits note: The 1,000-star repository is a hard gate that a new developer cannot satisfy tonight, and the operator has raised the threshold from 100 stars in June 2025 and has suspended issued boxes without stated cause, so the first thing that fails is the eligibility check and the second is the operator's discretion afterwards.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A real KVM box with a routable IPv4 and no sleep is the only row in the OSS-sponsorship lane that gives a public address without NAT, which makes it the origin for a Cloudflare-fronted service rather than a jump host.
- reliability: no reliability event recorded
- notes: ⛔ The page returned 403 through the probe with a Cloudflare challenge signature ('enable javascript and cookies to continue'), and the body came through automated retrieval's provider route instead, so the shape is documented and not measured. This row is ranked low despite being the largest shape in evaluated offerings, because 1,000 stars is not obtainable tonight. The published rule is automatic, which is the interesting part: the gate is reputation measured in stars rather than a human reviewer, so the failure is a number and not a person. Two things to settle. One, whether the 1,000-star floor is still 1,000 today, since the only first-party text is a page that a challenge wall hides from a plain fetch. Two, whether suspension without cause is systematic or was a single event; the Chinese forum reports one case and the sponsor wall lists 1,201 supported projects, which is not a mass-suspension pattern.
- extras:
  - facets.class: sponsored-vps-oss
  - facets.free_tier_kind: perpetual
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
  - facets.shape.disk_gib: 10
- evidence:
  - [1] 2026-10-22: 'Eligible projects have a public GitHub repository with 1,000+ stars that is at least 90 days old (no forks or archived repos)', 'Our checks run automatically', 'Projects Sponsored 1201+', quoted
  - [1] 2026-10-22: the application requires adding a DartNode badge to the project README and a verification code in an HTML comment, which is the write gate, quoted
  - [2] 2026-10-22: the paid ladder beside it prices the same shape: 'VPS-1 $3.95/mo - 1 vCPU Cores - 1 GB RAM - 10 GB SSD - IPv4 + IPv6 - 1 Gbps Unmetered', quoted, so the free box is worth about USD 47 a…
  - [1] 2026-11-02: eligibility is an institution-shaped gate on a public GitHub repository of 1,000 or more stars, 90 or more days old | capture: sha256:f0ace065beae7479b5dd23b493b752baffca6611d5acfd1d509dab676f69ef49 | quote: Eligible projects have a public GitHub repository with 1,000+ stars that is at least 90 days old (no forks or archived repos).
  - [3] 2026-11-02: the account form asks for names, an email address and a password, and no phone, card, country or ID-document field | capture: sha256:da21a290c791eb3537555837ec821fbb5fd808f9230f767045cd5f99e5c52474 | quote: First Name Last Name Email Address Password Confirm Password
- sources:
  - [1] https://dartnode.com/open-source
  - [2] https://dartnode.com/vps
  - [3] https://app.dartnode.com/gateway/join
