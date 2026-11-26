# Telebit

> telebit.cloud | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/telebit/ | JSON https://fshy.ajam.dev/api/v1/entity/telebit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Telebit

- `egress/telebit` | fails-egress | evidence documented | binding none | category http/tcp tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:05.297Z (live) | stale on 2026-12-20
- url https://telebit.cloud/
- price USD 0
- free tier: No price or allowance appears on the landing page; documentation specifies a TCP path: 'For Debugging with TCP ... ~/telebit tcp 9000'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Nothing published on the page read.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: The quickstart claims a device by email: 'Just confirm your email address'; no card, phone or identity document is shown on the page. | country: None
- interface: cli
- binding note: Nothing countable is published and the project shows no activity, so the first failure is availability rather than a quota. TCP only, no UDP.
- interface detail: telebit CLI, installed with 'curl https://get.telebit.io/ | bash'; commands shown: telebit http 3000, telebit ssh auto, telebit tcp 9000.
- tooling: telebit CLI.
- composes with: Unknown.
- reliability: The landing page's last-modified header is 29 May 2024, and the site has no pricing page. Relay availability is unverified: no status page was found.
- notes: The aggregator says the code lives at git.coolaj86.com and a user is JS.
- evidence note: First-party landing page documents a TCP forwarding path and email device claiming; no byte allowance or pricing is published.
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: Nothing published on the page read.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: landing page lists webhook testing and a TCP example; no price, plan or status information
  - [1] 2026-11-03: the quickstart claims a device by an emailed confirmation link; no card or phone is shown | capture: sha256:d601afd446267bb5fa2aa364ea0dcdc343889085f30b15f210a4acc28f2565dc | quote: Just confirm your email address:
  - [1] 2026-11-03: the quickstart installs a user with a shell one-liner from get.telebit.io | capture: sha256:d601afd446267bb5fa2aa364ea0dcdc343889085f30b15f210a4acc28f2565dc | quote: curl https://get.telebit.io/ | bash
  - probe:telebit.cloud 2026-11-03: the landing page answers 200 with a last-modified header of 29 May 2024 | capture: sha256:8cd90c42ccba34027e42a155aeb3ce42c115708c1d958a6f6be8df5d5a594daf | quote: "last-modified": "Wed, 29 May 2024 23:00:22 GMT"
  - probe:telebit.cloud/pricing 2026-11-03: the /pricing path answers 404, so the site has no pricing page there | capture: sha256:06bdb1d41e13bdb4dbd103e73d61b62e669d4e15cd5e01cc3b984a99e1e94ef4 | quote: "status": 404
  - [1] 2026-11-04: the quickstart claims a device by an emailed confirmation | capture: sha256:d601afd446267bb5fa2aa364ea0dcdc343889085f30b15f210a4acc28f2565dc | quote: Just confirm your email address:
  - probe:telebit.cloud 2026-11-04: the landing page still answers 200 on 2026-11-04 with the same last-modified date | capture: sha256:7aa74431156399e596028b5aee36151e9cfbab8eebdfa72491a728e3b6a46614 | quote: "last-modified": "Wed, 29 May 2024 23:00:22 GMT"
  - [1] 2026-11-19: the first-party landing page documents a TCP forwarding path and no published byte allowance or pricing | capture: sha256:d601afd446267bb5fa2aa364ea0dcdc343889085f30b15f210a4acc28f2565dc | quote: For Debugging with TCP
  - [1] 2026-11-19: the first-party landing page claims a device by email confirmation and shows no pricing or byte allowance | capture: sha256:d601afd446267bb5fa2aa364ea0dcdc343889085f30b15f210a4acc28f2565dc | quote: Just confirm your email address:
  - [1] 2026-11-19: the first-party landing page shows the CLI install and forwarding commands the user runs | capture: sha256:d601afd446267bb5fa2aa364ea0dcdc343889085f30b15f210a4acc28f2565dc | quote: curl https://get.telebit.io/ | bash
- sources:
  - [1] https://telebit.cloud/
