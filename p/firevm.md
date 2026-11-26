# FireVM

> firevm.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/firevm/ | JSON https://fshy.ajam.dev/api/v1/entity/firevm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FireVM

- `compute/firevm` | paid-only | evidence documented | binding none | category bare-metal GPU server rental | tier GPU bare-metal servers, month to month
- needs card no, phone no, ID yes, institution no | verified 2026-11-03T07:36:21.466Z (live) | stale on 2026-12-04
- url https://www.firevm.com/gpu-bare-metal-servers/
- free tier: No free allowance. Single-tenant bare-metal GPU servers rented month to month, from USD 349 a month. Per-GPU hourly equivalents printed on the page: Tesla T4 16 GB USD 0.48, L4 24 GB USD 0.62 (USD 449 a month), L40S 48 GB USD 1.09 (USD 799 a month), H100 NVL 94 GB USD 2.74 (USD 1999 a month). Not listed: A100 80 GB (an A30 24 GB is, at USD 0.82 per hour) and RTX 4090. Eight-GPU servers in the USA are pre-order with a USD 2500 deposit. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1] | note: each server is one physical machine with one to four GPUs; eight-GPU servers are pre-order
- retention: Month to month: no long contract, one flat monthly invoice per server. The server is built after payment and delivered within five business days. | source: [1] | note: the shortest rental is one month; no hourly meter
- egress: each server includes 30 TB of bandwidth a month on a 1 Gbps uplink; a 1 Gbps unmetered port is a paid upgrade at USD 199 a month | metered: yes | free allowance: 30 TB per month per server | source: [1]
- identity: national-id | detail: 'we verify the identity of every customer whose order is above $1000'; the online KYC takes 5-10 minutes and is done once after the first payment; smaller orders may be asked too. The page does not say which documents the check takes: unverified: behind a sign-up. Payment is made before the server is built.
- interface: unknown
- limits:
  - volume-quota: 30 TB bandwidth per month and a 1 Gbps uplink on each server [1]
- limits note: the wall is the one-month minimum rental and the identity check on larger orders, which the seven kinds do not name; the only numeric quota is 30 TB of bandwidth a month
- binding note: no usage quota binds before the price: the constraint is a one-month minimum rental with no hourly meter, and an online identity check on orders above USD 1000
- interface detail: the page states full root access on a bare-metal server and names no access method; not probed
- tooling: order a server from the pricing table; the server is built and handed over with access details. Support is by ticket, live chat and WhatsApp.
- composes with: billing is a flat month per server, so a short GPU job costs a full month; the per-GPU hourly figures are the vendor's monthly price divided down, for comparison with hourly clouds.
- reliability: unverified: no status page or incident history was read for this offer; the page publishes delivery within five business days for one to four GPUs and up to three months for pre-ordered eight-GPU servers
- notes: Listed by computeprices.com as a reserved bare-metal GPU rental (8 GPU models, 21 configurations, prices collected 2026-11-02). The H100 line is the NVL 94 GB card, not an SXM H100. The company also sells web hosting, VPS and dedicated servers.
- evidence:
  - [1] 2026-11-03: L4 24 GB at USD 449 a month, printed as USD 0.62 per hour | capture: sha256:1cb45971f9b1cc7591fc91d25a176c7eac3643d942d25a14304263f86310f85f | quote: L4 | Ada Lovelace | 24 GB VRAM • $449/month ($0.62/hour)
  - [1] 2026-11-03: L40S 48 GB at USD 799 a month, printed as USD 1.09 per hour | capture: sha256:1cb45971f9b1cc7591fc91d25a176c7eac3643d942d25a14304263f86310f85f | quote: L40S Ada | Ada Lovelace | 48 GB VRAM • $799/month ($1.09/hour)
  - [1] 2026-11-03: H100 NVL 94 GB at USD 1999 a month, printed as USD 2.74 per hour; no A100 80 GB or RTX 4090 section exists on the page | capture: sha256:1cb45971f9b1cc7591fc91d25a176c7eac3643d942d25a14304263f86310f85f | quote: H100 NVL | Hopper | 94 GB VRAM • $1999/month ($2.74/hour)
  - [1] 2026-11-03: cheapest server: Tesla T4 16 GB at USD 349 a month, USD 0.48 per hour | capture: sha256:1cb45971f9b1cc7591fc91d25a176c7eac3643d942d25a14304263f86310f85f | quote: Tesla T4 | Turing | 16 GB VRAM • $349/month ($0.48/hour)
  - [1] 2026-11-03: billing is monthly with no long contract | capture: sha256:1cb45971f9b1cc7591fc91d25a176c7eac3643d942d25a14304263f86310f85f | quote: - Month to month: No long contract. One flat monthly invoice.
  - [1] 2026-11-03: each server includes 30 TB of bandwidth a month and a 1 Gbps uplink | capture: sha256:1cb45971f9b1cc7591fc91d25a176c7eac3643d942d25a14304263f86310f85f | quote: Each server has:** 128 GB RAM • 2 x 1 TB NVMe SSD • Software RAID 1 • 30 TB bandwidth per mo • 1 Gbps network uplink
  - [1] 2026-11-03: an unmetered 1 Gbps port is a USD 199 a month upgrade | capture: sha256:1cb45971f9b1cc7591fc91d25a176c7eac3643d942d25a14304263f86310f85f | quote: 1 Gbps UNMETERED bandwidth (+199/mo)
  - [1] 2026-11-03: orders above USD 1000 go through a one-time online KYC check | capture: sha256:1cb45971f9b1cc7591fc91d25a176c7eac3643d942d25a14304263f86310f85f | quote: Identity verification (KYC): For orders above $1000, we start your online KYC, which takes around 5-10 minutes. It’s a one-time check, so repeat customers skip it.
  - [2] 2026-11-03:  | capture: sha256:bdded015113caedb64ace37238abb13f39da60ff8ea4478dbe0f01860c7b5ffb | quote: FireVM offers various GPU types including Tesla T4, Tesla T4, MI210, MI210, H100 NVL, H100 NVL, H100 NVL, H100 NVL, H100 NVL, A30, A30, H200 NVL, H200 NVL, H200 NVL, L40S, L40S, L4, L4, RTX PRO 6000, RTX PRO 6000, RTX PRO 6000.
- sources:
  - [1] https://www.firevm.com/gpu-bare-metal-servers/
  - [2] https://computeprices.com/providers/firevm
