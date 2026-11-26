# Servera

> servera.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/servera/ | JSON https://fshy.ajam.dev/api/v1/entity/servera.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Servera

- `compute/servera` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-07T17:40:53.068Z (live) | stale on 2026-12-08
- url https://servera.sh/
- price parsed USD 3.23/mo
- free tier: EUR 3.16 per month on a 12-month term (EUR 37.90 for the year) for Linux VPS S: 1 vCPU, 2 GB RAM, 25 GB NVMe, in Warsaw or Stockholm on AMD EPYC 7003 with DDR4 and a 2 Gbit/s port. The plan cards print yearly-billed rates: EUR 1.70 for XS (1 vCPU / 1 GB / 10 GB NVMe), EUR 2.87 for S, EUR 5.39 for M (2 vCPU / 4 GB / 50 GB) and EUR 9.89 for L (4 vCPU / 8 GB / 100 GB), each 'when pay yearly'; Warsaw costs 10 percent more, which puts S at 12 months in Warsaw at EUR 3.16. Terms run 1, 6, 12 and 24 months with 0, 5, 10 and 15 percent off; the 1-month rate is computed in JavaScript and is not printed in the server-rendered page. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited, with a per-plan high-speed allowance on a 2 Gbit/s port and 10 Mbps after it: 1 TB on XS, 2 TB on S, 4 TB on M and 6 TB on L | metered: no | free allowance: 2 TB per month on S (1 TB on XS, 4 TB on M, 6 TB on L), then 10 Mbps | source: [1]
- identity: any-phone | detail: the register form asks for a first name, a last name, an email address, a password and a phone number, and is protected by reCAPTCHA; no card or ID field
- interface: rest
- limits:
  - per-ip-shaping (binding): The stated wall is the port: a plan runs at 2 Gbit/s up to its allowance (1 TB on XS, 2 TB on S, 4 TB on M, 6 TB on L) and then continues at 10 Mbps. [1]
- limits note: The stated wall is the port: a plan runs at 2 Gbit/s up to its allowance (1 TB on XS, 2 TB on S, 4 TB on M, 6 TB on L) and then continues at 10 Mbps.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: configurator with OS choice and region choice; no API documented on the page read
- composes with: 2 GB of RAM on 25 GB of NVMe for EUR 3.16 in Warsaw or Stockholm is the cheapest European shape among documented hosts that states its post-allowance throttle rather than leaving it unknown
- reliability: no reliability event recorded
- notes: Source: vps.today index row ('Servera | 10 GB NVMe | 1 GB | 1 x 2.45 GHz | 2 000 Mbit/s | KVM IPv6 | 172 .'), then the vendor page. The index row and the vendor row are different shapes (10 GB / 1 GB against 25 GB / 2 GB), so the index may be quoting a smaller plan the configurator did not show. Rendering and provenance: currency written as EUR.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 25
  - monthly_price: not printed in the server-rendered page: the 1-month rate is computed in JavaScript; the cards print yearly-billed rates of EUR 1.70 (XS), EUR 2.87 (S), EUR 5.39 (M) and EUR 9.89 (L)
  - annual_price: EUR 2.87 per month for S billed yearly (EUR 34.44 for the 12 months, Stockholm base); the configurator prints EUR 37.90 for 12 months in Warsaw
  - renewal_price: not published: no page read prints a renewal price
  - billing_term: 1, 6, 12 and 24 month terms with 0, 5, 10 and 15 percent off
  - stock: no stock state is printed on the page; every plan shows a live Deploy button
  - cart_price: unverified: behind a sign-up - the billing host answered HTTP 530 to a direct probe (probe:https://bill.servera.sh/); the register page asks for name, email, password and phone behind reCAPTCHA
  - price_on_page: EUR 2.87/month for Linux VPS S when pay yearly
  - renewal_usd: not published: the cards print term prices only; no renewal figure appears
- evidence:
  - [1] 2026-10-23: configurator summary quoted: 'Linux VPS S - 1 vCPU / 2 GB RAM / 25 GB NVMe', '🇵🇱 Warsaw, Poland · 12 months (-10%)', '€3.16 /month', '€37.90 / 12 mo'
  - [1] 2026-10-23: traffic term quoted: 'Traffic is unlimited: each plan includes a high-speed traffic allowance on a 2 Gbit/s port, then continues at 10 Mbps.'; locations 'Stockholm and Warsaw'; hardware 'AMD EPYC 7003'
  - [1] 2026-11-07: the S card prints EUR 2.87 per month when pay yearly | capture: sha256:c4739fc0800f14bc63b9850808c49d4ddffb4e036449ceb3b42cac43a9c7dece | quote: data-testid="plan-price-s">€<!-- -->2.87</span>
  - [1] 2026-11-07: the S card names its allowance: first 2 TB at 2 Gbit/s, then 10 Mbps | capture: sha256:c4739fc0800f14bc63b9850808c49d4ddffb4e036449ceb3b42cac43a9c7dece | quote: First <!-- -->2 TB<!-- --> at 2 Gbit/s, then <!-- -->10 Mbps
  - [1] 2026-11-07: the S card names the allowance and the post-allowance speed | capture: sha256:c4739fc0800f14bc63b9850808c49d4ddffb4e036449ceb3b42cac43a9c7dece | quote: First <!-- -->2 TB<!-- --> at 2 Gbit/s, then <!-- -->10 Mbps
  - [1] 2026-11-07: the S card names the allowance and the throttle | capture: sha256:c4739fc0800f14bc63b9850808c49d4ddffb4e036449ceb3b42cac43a9c7dece | quote: First <!-- -->2 TB<!-- --> at 2 Gbit/s, then <!-- -->10 Mbps
  - [2] 2026-11-07: the register form requires a phone number | capture: sha256:d1914901e81454aee5e53964a7dac21c896c5da789218802606a054bbde34d70 | quote: First name\* Last name\* Email\* Password\* Phone\*
  - [2] 2026-11-07: the register form's required fields and its reCAPTCHA notice, read 2026-11-07 | capture: sha256:d1914901e81454aee5e53964a7dac21c896c5da789218802606a054bbde34d70
  - [1] 2026-11-07: the cards label their only printed rates as when pay yearly | capture: sha256:c4739fc0800f14bc63b9850808c49d4ddffb4e036449ceb3b42cac43a9c7dece | quote: when pay yearly
  - [1] 2026-11-07: the configurator prints EUR 37.90 for the 12-month Warsaw term | capture: sha256:9b707ca42df45dd3d9c4f2f1ebd0bad38575df8e61b3f6e438865d4ea1cf701e | quote: €37.90 / 12 mo
  - [1] 2026-11-07: the cards print term prices only; no renewal figure appears | capture: sha256:c4739fc0800f14bc63b9850808c49d4ddffb4e036449ceb3b42cac43a9c7dece | quote: when pay yearly
  - [1] 2026-11-07: the billing toggle prints the terms and their discounts | capture: sha256:c4739fc0800f14bc63b9850808c49d4ddffb4e036449ceb3b42cac43a9c7dece | quote: 12 months<span class="block text-[10px] font-mono mt-0.5 text-emerald-400">-<!-- -->10<!-- -->%</span>
  - [1] 2026-11-07: the configurator renders a live total and a Deploy Now button | capture: sha256:9b707ca42df45dd3d9c4f2f1ebd0bad38575df8e61b3f6e438865d4ea1cf701e | quote: €37.90 / 12 mo
  - probe:https://bill.servera.sh/ 2026-11-07: the billing host answers HTTP 530 to a direct probe | capture: sha256:9241cd3701f303a627dd929f49eac9a0e331e6bb55cda24d896db0f61a25331a | quote: "status": 530
  - [1] 2026-11-07: the configurator's 12-month Warsaw total is unchanged on 2026-11-07 | capture: sha256:9b707ca42df45dd3d9c4f2f1ebd0bad38575df8e61b3f6e438865d4ea1cf701e | quote: €37.90 / 12 mo
  - [1] 2026-11-07: the S plan card prints EUR 2.87 as its yearly-billed monthly rate | capture: sha256:c4739fc0800f14bc63b9850808c49d4ddffb4e036449ceb3b42cac43a9c7dece | quote: data-testid="plan-price-s">€<!-- -->2.87</span>
- sources:
  - [1] https://servera.sh/
  - [2] https://bill.servera.sh/register
