# GratisVPS

> gratisvps.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gratisvps/ | JSON https://fshy.ajam.dev/api/v1/entity/gratisvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GratisVPS

- `compute/gratisvps` | fails-identity | evidence reported | binding none | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://gratisvps.net/
- free tier: Site claim, quoted: "2 vCPU and 2 GB RAM", "KVM", "No card, no trial that expires into a bill", three regions, since 2013. Multiple independent reports describe an SMS-verification wall and an ad-click requirement with no credentials issued. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: any-phone | detail: no card, but a phone wall: the site claims "No card, no trial that expires into a bill", while users report an SMS verification step after the VPS is created, one of them producing a machine but never a password, and reviews describe a requirement to click advertising links to activate. The record does not state which numbers the SMS check accepts, which is why the kind is any-phone rather than country-phone; no hold or authorisation is stated, and debit or prepaid do not arise because no card is taken
- interface: ssh
- limits note: Independent reports say the deployment never yields a root password after the SMS step, so the capacity exists only as a claim; the site also asks users to click advertising links to activate service.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing, because the machine is not issued. Any chain through it fails at provisioning.
- reliability: no reliability event recorded
- notes: The site's own page is well written and states the parameters plainly, which is why it keeps appearing in listicles. Two independent user reports plus a review site plus a hidden WHOIS is enough to record it as non-delivering rather than to repeat 2 vCPU as capacity. One testimonial blog claims a 30-day run with a live Discord bot; it is unverifiable and reads as promotional.
- extras:
  - facets.class: refutation-non-delivering
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
- evidence:
  - [1] 2026-10-22: front page advertises 2 vCPU and 2 GB RAM KVM with no card and root SSH, quoted, and states the model is advertising-funded
  - [2] 2026-10-22: users report being asked for SMS verification after creating a VPS, and one reports that the deployment produced a machine but never a password
  - [3] 2026-10-22: reviews describe being required to click advertising links to activate the service
  - [4] 2026-10-22: a 2023 review calls the site an ad farm that requests significant personal information
  - [5] 2026-10-22: the owner identity is hidden in WHOIS and negative reviews were detected, though the site is rated probably not a scam
- sources:
  - [1] https://gratisvps.net/
  - [2] https://www.nodeloc.com/t/topic/29849
  - [3] https://www.trustpilot.com/review/gratisvps.net
  - [4] https://www.preeez.com/2023/07/unveiling-truth-behind-free-vps-scams.html
  - [5] https://scamadviser.com/check-website/gratisvps.net
