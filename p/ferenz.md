# Ferenz

> ferenz.com.br | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ferenz/ | JSON https://fshy.ajam.dev/api/v1/entity/ferenz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ferenz

- `compute/ferenz` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:06.322Z (live) | stale on 2026-12-08
- url https://www.ferenz.com.br/produtos/servidor-vps
- price parsed USD 10.89/mo
- free tier: The first plan card on the vendor's own VPS page: R$ 54,90 per month for 1 GB RAM DDR4, 1 vCore (2.4 GHz+), 30 GB of SSD in Raid10, a 500 MB/FULL port, traffic stated as unlimited, and 1 IPv4 with IPv6 support. The next cards are R$ 89,90 for 2 GB and 60 GB, R$ 109,90 for 2 GB and 2 vCores and 80 GB, and R$ 154,90 for 4 GB and 120 GB. Regions offered: Santa Catarina, Sao Paulo and Ceara. The tracker lists the entry plan at R$ 54.90 per month in Sao Paulo and Fortaleza with 51,200 GB a month on a 0.49 Gbps port. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the card states the traffic is unlimited on a 500 MB/FULL port; no fair-use policy or overage price was found on the page read | metered: no | source: [1]
- identity: email | detail: not stated
- interface: ssh, rest
- limits:
  - volume-quota (binding): the two sources disagree: the tracker states a 51,200 GB monthly allowance, the vendor card states the traffic is unlimited at a 500 Mbps full-duplex port, so in practice the 500 Mbps port is the wall and the byte cap is unverified [1]
- limits note: the two sources disagree: the tracker states a 51,200 GB monthly allowance, the vendor card states the traffic is unlimited at a 500 Mbps full-duplex port, so in practice the 500 Mbps port is the wall and the byte cap is unverified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: Linux or Windows VPS on a Brazilian provider; SSH and a client area. No API documented on the page read
- composes with: a Brazil-region node at R$ 54,90 is cheap for South American crawling or for reaching Brazilian sites that throttle foreign addresses; 30 GB and 1 GB of RAM rule out the archive index
- reliability: no reliability event recorded
- notes: The vendor's unlimited-traffic claim and the tracker's 51,200 GB figure are the same kind of disagreement seen on Elende; the tracker's number looks derived from the port speed rather than read off the card, which is why the vendor's own wording is recorded first.
- extras:
  - facets.class: price-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 30
  - price_on_page: BRL 54.90/month: the 1 GB VPS
  - renewal_note: not published: the vendor's own VPS page read on 2026-11-07 prints a monthly price per card and no renewal price
- evidence:
  - [1] 2026-10-22: first plan card quoted: 'R$ 54,90 /mes', '1 GB RAM DDR4', '1 vCore (2.4 GHz+)', '30 GB de Disco SSD (Raid10)', '500 MB/FULL', '1 IPv4 / Suporte a IPv6', with the traffic line stating the traffic is unlimited
  - [1] 2026-10-22: region selector offers Santa Catarina, Sao Paulo and Ceara, with test points at Xaxim SC, Sao Paulo SP and Fortaleza CE
  - [2] 2026-10-22: row quoted from the Cheapest VPSs table: 'R$ 54.90 / month', '1 Intel Cores (shared)', '1,024 MB RAM', '30 GB SSD', '51,200 GB/month bandwidth', '0.49 Gbps port speed', 'Sao Paulo Brazil'
  - [1] 2026-11-07: the first plan card prices the 1 GB VPS at R$ 54,90 a month | capture: sha256:026b80e6c120b020bb3d06e81931caaf732842578cea11c27d252968098f4132 | quote: R$ 54,90/mês
- sources:
  - [1] https://www.ferenz.com.br/produtos/servidor-vps
  - [2] https://vpspricetracker.com/provider/Ferenz/vps
