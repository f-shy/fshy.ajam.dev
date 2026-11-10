# ServeTheWorld

> stw.no | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stw/ | JSON https://fshy.ajam.dev/api/v1/entity/stw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ServeTheWorld

- `compute/servetheworld` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:39.722Z (live) | stale on 2026-12-08
- url https://stw.no/no/ssd-vps/
- free tier: GP32 at NOK 79/month list price (NOK 39/month for the first three months under the page's 50 percent introductory discount): 1 vCPU, 2 GB RAM, 60 GB NVMe, 100 Mbit/s port, 25 TB traffic per month, Oslo Norway. GP34 is NOK 159/month with 2 vCPU, 4 GB RAM, 120 GB and a 200 Mbit/s port; extra traffic is NOK 10 per TB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: at least 25 TB per VM per month; extra traffic is billed per TB at the standard rate of NOK 10, and the page states the network port is never throttled below the plan's stated speed | metered: yes | free allowance: 25 TB per month per VM | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 25 TB a month with overage billed at NOK 10 per TB, so the meter does not stop the machine; the 100 Mbit/s port on GP32 caps a day's transfer long before the monthly allowance is reached [1]
- limits note: 25 TB a month with overage billed at NOK 10 per TB, so the meter does not stop the machine; the 100 Mbit/s port on GP32 caps a day's transfer long before the monthly allowance is reached
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: Proxmox and Ceph platform; Linux and Windows images with a plan comparison table, no API mentioned on the page read
- composes with: the only entry among documented hosts that publishes a per-TB overage price, so it is the one that can absorb a burst rather than being cut off at the allowance
- reliability: no reliability event observed; the page states ports are never throttled below the plan's stated speed
- notes: The tracker's NKr39.50 is the introductory rate; the list price on the vendor page is NOK 79 and both are recorded rather than averaged. Norwegian-language page, and the quotes above are transliterated from it without accents in the evidence line. The offer is priced in NOK and no conversion is made. Unverified: whether the introductory rate renews at NOK 79 after three months, which the table implies and the page does not say.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 60
- evidence:
  - [1] 2026-10-22: GP32 row of the Linux VPS table: 1 vCPU, 2 GB, 60 GB, 100 Mbit/s, 25TB, '79 NOK' list and '39 NOK' discounted, quoted from the plan table
  - [1] 2026-10-22: traffic note: 'Du far minst 25 TB data per VM hver maned. Ekstra trafikk belastes per TB til standardpris pa 10 NOK' (at least 25 TB per VM per month, extra traffic at NOK 10 per TB)…
  - [2] 2026-10-22: tracker row 'NKr39.50 / month, 1 Epyc Cores (shared), 2,048 MB RAM, 60 GB NVMe, 25,000 GB/month bandwidth, 0.1 Gbps port speed, IPv4, Oslo Norway'
  - [1] 2026-11-07: the GP3 table still prices GP32 at NOK 79 list with the 50 percent introductory rate at NOK 39 for the first three months | capture: sha256:685579619deefbd53ab1f065729a1bd6e1dd52f95d0d47567494dc52ca45e403 | quote: 79 NOK39 NOK
- sources:
  - [1] https://stw.no/no/ssd-vps/
  - [2] https://vpspricetracker.com/provider/ServeTheWorld/vps
