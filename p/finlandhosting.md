# FinlandHosting

> finlandhosting.fi | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/finlandhosting/ | JSON https://fshy.ajam.dev/api/v1/entity/finlandhosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FinlandHosting

- `egress/finlandhosting-budget-small` | paid-only | evidence documented | binding volume-quota | category origin VM (paid VPS) | tier Budget SMALL (DDR3)
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.975Z (live) | stale on 2026-12-05
- url https://finlandhosting.fi/en/vps/
- price EUR 1.00 per extra TB as a monthly add-on; EUR 4.00 a month for 5 TB | parsed USD 0.9014/TB-mo
- free tier: no free plan: Budget SMALL (2 vCPU, 6 GB DDR3 RAM, 50 GB SSD) is EUR 4.00 a month with 5 TB of traffic a month | unit: TB | metered on: downloaded-bytes | read on: 2026-11-04 | source: [1] | note: Extra traffic is sold as monthly add-ons: +1 TB for EUR 1.00, +5 TB for EUR 3.00, +10 TB for EUR 5.00, +25 TB for EUR 10.00, +50 TB for EUR 15.00.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB of traffic a month on Budget SMALL, with IPv4 and IPv6 included; extra traffic is a fixed monthly add-on of EUR 1.00 per 1 TB; port speed and inbound UDP policy are not stated on the pages read | metered: yes | free allowance: 5 TB a month on Budget SMALL | price per TB: EUR 1.00 per extra TB as a monthly add-on | source: [1]
- identity: email | detail: unverified: the order form sits behind a billing portal and the terms were not read for what registration asks | country: None
- interface: ssh
- limits:
  - volume-quota (binding): 5 TB of traffic a month on Budget SMALL; +1 TB for EUR 1.00 a month [1]
- limits note: Port speed and the inbound port policy are not stated on the VPS page as read.
- binding note: at 1 TiB a month the 5 TB allowance is not passed; what registration asks is not read
- interface detail: SSH to the VPS public address
- tooling: wg-quick or any VPN daemon inside the guest
- composes with: a EUR 4.00 a month origin in Finland with 5 TB included; the domain finlandhosting.com is a parked page for sale and the storefront is finlandhosting.fi
- reliability: the vendor front page says new VPS orders are delayed while IPv4 addresses are short and are activated as more addresses become available
- notes: A third-party index lists the same plan at GBP 3.33 a month, the EUR 4.00 vendor price converted.
- evidence note: plan, allowance, add-on price and the IPv4 notice are quoted from vendor pages read on 2026-11-04; identity cost is unverified; no server was ordered
- extras:
  - wg_path: native-conf
  - wg_detail: a full Linux guest; wg-quick binds UDP natively unless a firewall is added; inbound UDP was not probed
  - ingress: unverified: no inbound port policy is stated on the pages read
  - volume_tib_month: 5
  - volume_stated: 5 TB a month; extra TB add-ons at EUR 1.00
  - bytes_transit: yes
  - transit_note: bytes leave through the VPS's own public address
- evidence:
  - [1] 2026-11-04: the Budget SMALL plan includes 5 TB of traffic a month | capture: sha256:c078dc60043405010b2a2cc544a5aa691207ec60a0cf5f0454648ea9172bd6aa | quote: - 5 TB traffic / month
  - [1] 2026-11-04: 1 TB of extra traffic is a EUR 1.00 a month add-on | capture: sha256:c078dc60043405010b2a2cc544a5aa691207ec60a0cf5f0454648ea9172bd6aa | quote: +1 TB€1.00 / mo
  - [1] 2026-11-04: the Budget SMALL plan is EUR 4.00 a month | capture: sha256:c078dc60043405010b2a2cc544a5aa691207ec60a0cf5f0454648ea9172bd6aa | quote: €4.00/mo
  - [1] 2026-11-04: an IPv4 address is included | capture: sha256:c078dc60043405010b2a2cc544a5aa691207ec60a0cf5f0454648ea9172bd6aa | quote: - IPv4 included
  - [2] 2026-11-04: the vendor reports a temporary IPv4 address shortage that delays new VPS orders | capture: sha256:391f998ebdf9157c403304361744264fbe943ad6abe0261ef23fe349326c012b | quote: Meillä on tällä hetkellä tilapäinen pula IPv4-osoitteista, mikä aiheuttaa viivästyksiä uusien VPS-palveluiden käyttöönotossa.
  - [3] 2026-11-04: the .com domain is a parked page for sale, not the storefront | capture: sha256:f301505367792d69a0724b52a84f6c59d1f56ce07e1efcb4c0c173dcf80c3530 | quote: ## might be available for sale
- sources:
  - [1] https://finlandhosting.fi/en/vps/
  - [2] https://finlandhosting.fi/
  - [3] https://www.finlandhosting.com/
