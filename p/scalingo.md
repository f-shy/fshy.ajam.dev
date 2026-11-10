# Scalingo

> scalingo.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scalingo/ | JSON https://fshy.ajam.dev/api/v1/entity/scalingo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scalingo

- `compute/scalingo` | trial-only | evidence documented | binding retention-clamped | category platform host | tier 30-day trial then per-container billing
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T02:24:35.124Z (live) | stale on 2026-12-05
- url https://scalingo.com/pricing
- free tier: no perpetual free tier: 'start free for 30 days', then containers bill by the minute; containers never sleep on any plan | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable: the unit is a container
- retention: not applicable to a free tier; there is none
- egress: a TCP Gateway with unlimited traffic is free and a Scalingo OpenVPN option with unlimited traffic is EUR 30.00; no container egress allowance or overage price is printed on https://scalingo.com/pricing read 2026-11-04 | metered: no | free allowance: unlimited on the TCP Gateway | source: [1]
- identity: card | detail: a card at signup; the price page states prices VAT excluded and bills monthly
- interface: cli, ssh
- limits:
  - retention-clamped (binding): the 30-day trial is the whole free allowance [1]
  - write-gated: a card is required to start the trial [1]
- limits note: the 30-day trial is the whole free allowance; after it the smallest container bills per minute for as long as it exists.
- binding note: day 31 ends it, and there is no sleep to extend it.
- interface detail: Scalingo CLI, which talks to api.<region>.scalingo.com on port 443 over HTTPS and to ssh.<region>.scalingo.com on port 22 over SSH; documented at doc.scalingo.com/cli
- tooling: Scalingo CLI (precompiled binaries for each operating system)
- composes with: 30 days of a never-sleeping container is a migration testbed, not a home for a service; the value is the measurement of whether the code runs, and the run must then move to a tier that does not sleep.
- reliability: no reliability event recorded
- notes: Confirms documented records row. Worth keeping for one reason: it is the only provider among documented hosts that states plainly that its containers do not sleep, which is the trade the free tiers make in the other direction.
- evidence note: 'start free for 30 days' and 'containers never sleeps' were read on the pricing page
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: trial
  - billing_model: per-minute
  - term: monthly
  - price_arithmetic: not computed: the page renders container prices through a selector and prints no figure in the text read
  - free_tier_kind: trial-only
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: the container port plus a free TCP Gateway
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: 'containers never sleeps'
- evidence:
  - [1] 2026-10-22: page description reads 'start free for 30 days'; the pricing body lists containers, databases and network with no zero-price plan, quoted
  - [1] 2026-10-22: 'Always included: custom domains, automatic Let's Encrypt SSL certificates, performance metrics, unlimited collaborators, unlimited logs archives, containers never sleeps', quoted
  - [1] 2026-10-24: quoted: 'Always included: custom domains, automatic Let's Encrypt SSL certificates, performance metrics, unlimited collaborators, unlimited logs archives, containers never sleeps.'
  - [1] 2026-10-24: quoted page description: 'Optimize hosting costs, start free for 30 days, and scale when you'
  - [1] 2026-11-04: Scalingo OpenVPN with unlimited traffic is 30.00 EUR | capture: sha256:cce0459f68e2fe18804e73bd30c3cc7b6aee27e6c13d1c38c2b31c0285de0554 | quote: 50\.00 €, Scalingo OpenVPN, Unlimited traffic, 30\.00 €
  - [2] 2026-11-04: Scalingo ships a CLI | capture: sha256:bc913a73e0e38dc1428fd45a59c0102bab3d63b673a7ea653314b9f685225950 | quote: We provide a command line interface (CLI) tool to interact with the platform.
  - [2] 2026-11-04: an SSH endpoint exists on port 22 | capture: sha256:bc913a73e0e38dc1428fd45a59c0102bab3d63b673a7ea653314b9f685225950 | quote: `ssh.<REGION NAME>.scalingo.com:22`
  - [1] 2026-11-04: the TCP Gateway has unlimited traffic at no charge | capture: sha256:cce0459f68e2fe18804e73bd30c3cc7b6aee27e6c13d1c38c2b31c0285de0554 | quote: Network, Description, Price¹, TCP Gateway, Unlimited traffic, Free, Scalingo Docker Image
  - [2] 2026-11-04: the CLI documents HTTPS API and SSH endpoints | capture: sha256:bc913a73e0e38dc1428fd45a59c0102bab3d63b673a7ea653314b9f685225950 | quote: The port `443` will receive HTTPS stream. The port `22` is for SSH.
  - [2] 2026-11-04: the provider ships a named CLI | capture: sha256:bc913a73e0e38dc1428fd45a59c0102bab3d63b673a7ea653314b9f685225950 | quote: We provide a command line interface (CLI) tool to interact with the platform.
- sources:
  - [1] https://scalingo.com/pricing
  - [2] https://doc.scalingo.com/cli
