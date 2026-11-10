# Zerops

> zerops.io | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zerops/ | JSON https://fshy.ajam.dev/api/v1/entity/zerops.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zerops (Compute)

- `compute/zerops` | trial-only | evidence documented | binding volume-quota | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:26.171Z (live) | stale on 2026-12-05
- url https://docs.zerops.io/company/pricing
- free tier: The Lightweight Core project package is free, with 15 build hours, 5 GB of backup storage and 100 GB of egress a month, but CPU, RAM and disk are billed separately against account credit: shared CPU USD 0.60 per core per 30 days, RAM USD 0.75 per 0.25 GB per 30 days, disk USD 0.05 per 0.5 GB per 30 days. Signup grants USD 15 in promo credits with no card, and a USD 10 payment verification adds USD 50 for USD 65 total. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: promo-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Lightweight Core is Free with 15 hours build time, 5 GB backup storage and 100 GB egress per month; resource pricing Shared CPU USD 0.60 per CPU/30 days, RAM USD 0.75 per 0.25 GB/30 days, quoted | metered: yes | free allowance: 100 GB per month (Lightweight Core, free); 3 TB per month on Serious Core at USD 10 per month | price per TB: USD 20 per TB | source: [1]
- identity: email | detail: no card for the free credit: the quickstart states "sign up and get USD 15 in promo credits, no credit card needed", and an optional USD 10 payment verification adds USD 50 for USD 65 total, so the USD 10 is a purchase and not an authorisation hold. The record does not state whether signup asks for an email address or a GitHub account, nor whether debit or prepaid cards are accepted for the optional USD 10 payment
- interface: rest, cli
- limits:
  - volume-quota (binding): the USD 15 no-card credit is the whole free allowance: at the vendor's own estimate of USD 3-5 a month for a simple app with a database, that is about three to five months of one small project, and the free core package does not cover the containers. [1]
- limits note: the USD 15 no-card credit is the whole free allowance: at the vendor's own estimate of USD 3-5 a month for a simple app with a database, that is about three to five months of one small project, and the free core package does not cover the containers.
- binding note: the same as limits note
- interface detail: zCLI (Linux, macOS, Windows) and a REST API with Bearer personal access tokens and Swagger; no SSH or SDK read on the pages
- tooling: zCLI, the provider's command-line tool (Linux, macOS, Windows); the REST API (Bearer personal access token, Swagger) can also be called directly.
- composes with: USD 15 of credit with no card buys a container plus a managed Postgres for three to five months, which is enough to finish and measure a project; the 100 GB monthly egress on the free core outlives the credit, so a static or cached workload can stay after the compute is gone.
- reliability: no reliability event recorded
- notes: Zerops provides developer platform services with introductory promotional credits of USD 15 to USD 65 granted upon initial payment method verification (USD 10 initial top-up).
- extras:
  - facets.class: credit-programme
  - facets.free_tier_kind: promo-credit
- evidence:
  - [2] 2026-10-22: sign up and get USD 15 in promo credits, no credit card needed; verify with a USD 10 payment and get an additional USD 50 for USD 65 total; a simple app with a database costs roughly USD 3-5/month, quoted
  - [1] 2026-10-22: Lightweight Core is Free with 15 hours build time, 5 GB backup storage and 100 GB egress per month; resource pricing Shared CPU USD 0.60 per CPU/30 days, RAM USD 0.75 per 0.25 GB/30 days, quoted
  - [3] 2026-10-22: project core package Lightweight FREE 15 hrs build time 100 GB egress 5 GB backups; Serious USD 10/month, quoted
  - [4] 2026-11-03: free allowance 100 GB per month on Lightweight Core | capture: sha256:24732e731f9f9b59c8ddbce4dc699076e15bd7f7c30d926b6d700807a50d7c50 | quote: - Egress Traffic: 100 GB per month
  - [4] 2026-11-03: overage price USD 0.02 per GB | capture: sha256:24732e731f9f9b59c8ddbce4dc699076e15bd7f7c30d926b6d700807a50d7c50 | quote: | Extra Egress | $0.02 per GB | Data transfer out of your project beyond plan limits |
  - [5] 2026-11-03: a CLI exists | capture: sha256:986fa02e797ae056e99d7b0deb07e0a0938a77cfbe96729d3c8d49bb24125e10 | quote: zCLI is the command-line tool for Zerops that allows users to manage services, simplify interactions, and configure infrastructure directly from the terminal.
  - [6] 2026-11-03: a REST API exists | capture: sha256:e5e1d9fd37962f20e99b2cdb6700dec8dc1ac1d9ae3a95ebb9e1aa720778cd2a | quote: The Zerops REST API allows you to programmatically interact with Zerops platform by providing access to resources like projects, services, users, billing, and configurations.
  - [5] 2026-11-04: the provider's client is zCLI | capture: sha256:986fa02e797ae056e99d7b0deb07e0a0938a77cfbe96729d3c8d49bb24125e10 | quote: zCLI is the command-line tool for Zerops that allows users to manage services, simplify interactions, and configure infrastructure directly from the terminal.
- sources:
  - [1] https://docs.zerops.io/company/pricing
  - [2] https://docs.zerops.io/quickstart
  - [3] https://zerops.io/pricing
  - [4] https://docs.zerops.io/billing/pricing
  - [5] https://docs.zerops.io/references/cli
  - [6] https://docs.zerops.io/references/api

## Zerops (free)

- `egress/zerops` | fails-quota | evidence documented | binding volume-quota | category paas l4 port | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://docs.zerops.io/guides/public-access
- price USD 0
- free tier: Lightweight Core - Free. Included resources: Build Time: 15 hours per month, Backup Storage: 5 GB, Egress Traffic: 100 GB per month. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Lightweight Core - Free: Egress Traffic: 100 GB per month.; ingress: tcp+udp | metered: yes | free allowance: Lightweight Core - Free: Egress Traffic: 100 GB per month. | source: [2]
- identity: email | detail: Sign up at app.zerops.io; "You get $15 in promo credits on signup, no credit card needed." Verifying with a $10 payment is optional and adds $50. | country: None
- interface: rest, cli
- limits:
  - volume-quota (binding): 100 GB per month on the Lightweight Core [1]
- binding note: At 1 TiB/month the free core's 100 GB/month egress is exceeded 11 times over; extra egress is $0.02/GB. The port itself costs nothing.
- interface detail: GUI, import YAML, and a REST API; "Direct Port Access ... Protocols: TCP, UDP".
- tooling: wg-quick on the service; the port is configured in the Zerops GUI or import YAML.
- composes with: Zerops direct UDP port plus a wg-quick peer gives a tunnel endpoint; the 100 GB/month cap means it carries control traffic and fallback, not bulk transfer.
- reliability: Firewall rules are per port, blacklist or whitelist. No ban or throttle documented for direct ports.
- notes: Cloud platform providing container runtimes with public IPv6 networking. IPv4 addressing requires paid add-ons at USD 3 monthly.
- evidence note: A live UDP probe of a Zerops direct port, sending a WireGuard handshake and reading the reply, would raise this to measured.
- extras:
  - wg_path: inside-udp
  - wg_detail: Direct Port Access: any port 10-65435, Protocols: TCP, UDP, mapped to an internal service port. wg-quick listens on that external port. IPv6 works without an add-on; a Unique IPv4 address is a $3.00/month add-on.
  - ingress: tcp+udp
  - volume_tib_month: 0.0909
  - volume_stated: Lightweight Core - Free: Egress Traffic: 100 GB per month.
  - bytes_transit: yes
  - transit_note: Zerops public ingress carries the datagrams to the runtime container.
- evidence:
  - [2] 2026-10-23: Direct Port Access: port range 10-65435, protocols TCP and UDP, IPv6 first or Unique IPv4 add-on
  - [1] 2026-10-23: Lightweight Core - Free includes 100 GB per month egress; Dedicated IPv4 $3.00 per month; extra egress $0.02 per GB
  - [3] 2026-10-23: $15 in promo credits on signup, no credit card needed
- sources:
  - [1] https://docs.zerops.io/company/pricing
  - [2] https://docs.zerops.io/guides/public-access
  - [3] https://docs.zerops.io/quickstart.md
