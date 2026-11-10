# AaITR

> aaitr.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aaitr/ | JSON https://fshy.ajam.dev/api/v1/entity/aaitr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AaITR

- `ip-proxy/aaitr-static-residential-vps` | paid-only | evidence reported | binding volume-quota | category ISP-registered VPS | tier US static residential VPS (AT&T line and Verizon line)
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T07:35:31.081Z (live) | stale on 2026-11-18
- url https://www.aaitr.com/
- free tier: No free tier. The product page lists a dedicated static AT&T (AS7018) line and a dedicated static Verizon (AS5650) line, each with 2 vCPU, 2 GB RAM, 25 GB SSD, 100 Mbps peak and 2000 GB of two-way traffic, in 'California, multiple cities and segments at random'. A third-party review reports the price as CNY 149 per month for both lines, both showing sold out with a pre-order queue. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The price is reported by a third-party review and was not in the first-party page text that could be read.
- per-object cap: not applicable: an address or a traffic quota, not an object | source: [1]
- retention: not applicable: a proxy session or a rented address, not stored bytes | source: [1]
- egress: 2000 GB of two-way traffic per month and 100 Mbps peak, both configurable at extra cost; overage behaviour is unstated. | metered: yes | free allowance: 2000 GB two-way per month | source: [1]
- identity: email | detail: The vendor writes '静态IP系列产品无需实名认证' (the static IP series needs no real-name verification). The WHMCS registration asks for a personal profile and a billing address and offers CNY or USD. The shared dynamic NAT line needs a real-name phone check, per a third-party review.
- interface: ssh
- limits:
  - volume-quota (binding): 2000 GB two-way traffic per month on the static VPS [1]
  - per-ip-shaping: 100 Mbps peak [1]
- limits note: The vendor states the line is a real home broadband line laid locally with IP purity not guaranteed, that IPs are recycled, and that there is no free IP replacement. A shared dynamic NAT line (CNY 149 per month) is a separate product that, per the same review, needs real-name verification by phone number; the static line does not.
- binding note: 2000 GB a month is the only quota the vocabulary can express; stock is the practical limit, since both static lines showed sold out with a pre-order queue per a third-party review.
- interface detail: A rented VPS with a dedicated static IPv4 address; the buyer runs any proxy daemon on it. The vendor sells the address and the machine, not a proxy endpoint.
- tooling: An SSH client plus a proxy daemon that the user installs and runs on the VPS (a rented machine, not owned hardware). The vendor publishes no proxy endpoint or API for the static line.
- composes with: A host-side hop connects to the VPS's static IPv4 and the VPS makes the upstream request, so the upstream sees an address in AS7018 (AT&T) or AS5650 instead of the caller's address.
- reliability: The vendor's page labels the second static line 'Verizon (AS5650)'; a RIPE Stat lookup returns FRONTIER-FRTR - Frontier Communications of America, Inc. as the holder of AS5650, so the Verizon label does not match the registry holder of that ASN. AS7018 resolves to ATT-INTERNET4 - AT&T Enterprises, LLC. No live exit address was looked up (rung 5).
- notes: Named on a Chinese-language proxy forum as 'AaITR Frontier/Verizon 静态家宽 149元/月'. A VPS that carries one residential line, the same shape as the novixlink record.
- evidence note: The ASNs, the no-real-name statement and the specification are first-party; the price, stock and NAT-line identity come from a third-party review, which is the weakest rung used.
- extras:
  - rung: 5
  - rung_note: The product is a claim about how an address is registered; two ASN holders were looked up, no live exit address.
- evidence:
  - [1] 2026-11-03: The static IP series needs no real-name verification. | capture: sha256:826fbd7d93d597158d4df43a0f1fd25d504ce1b976607dfc21c748bc01ca55b7 | quote: 静态IP系列产品无需实名认证
  - [1] 2026-11-03: The AT&T line is one dedicated static address under AS7018. | capture: sha256:826fbd7d93d597158d4df43a0f1fd25d504ce1b976607dfc21c748bc01ca55b7 | quote: 独享静态 AT&T (AS7018) x 1
  - [1] 2026-11-03: The second line is labelled Verizon with AS5650. | capture: sha256:826fbd7d93d597158d4df43a0f1fd25d504ce1b976607dfc21c748bc01ca55b7 | quote: 独享静态 Verizon (AS5650) x 1
  - [2] 2026-11-03: The vendor guarantees only a real home broadband line, not purity, and has no free IP replacement. | capture: sha256:d6fe000e67d124ad707b00400f4d0df1e7f47a03122eeb05a0333084790d1a39 | quote: 只保证IP是真家宽，不保证纯净度，无免费更换IP的政策
  - [3] 2026-11-03: A third-party review reports CNY 149 per month from for the first two product lines. | capture: sha256:b34dc42c81bbb9001791c1529a1e2f262bcf6fb1a642b9c929e36877a7bc740d | quote: 前两条线目前都是 ¥149/月起，价格一致
  - [3] 2026-11-03: A third-party review reports the NAT line needs a phone-number real-name check. | capture: sha256:b34dc42c81bbb9001791c1529a1e2f262bcf6fb1a642b9c929e36877a7bc740d | quote: 需要手机号实名认证（官方注明作弊封号不退款）
  - probe:https://stat.ripe.net/data/as-overview/data.json?resource=AS5650 2026-11-03: RIPE Stat lists Frontier Communications as the holder of AS5650, not Verizon. | capture: sha256:a195261a1addbbe4682c556441f14a41d19f64037fcf82db9248794b42d83a5a | quote: "holder":"FRONTIER-FRTR - Frontier Communications of America, Inc."
  - probe:https://stat.ripe.net/data/as-overview/data.json?resource=AS7018 2026-11-03: RIPE Stat lists AT&T Enterprises as the holder of AS7018. | capture: sha256:6538256d95f32be8a90580801fe23182c20952b7d9907d4acfc266e8ba9143db | quote: "holder":"ATT-INTERNET4 - AT&T Enterprises, LLC"
- sources:
  - [1] https://www.aaitr.com/cart.php
  - [2] https://www.aaitr.com/link.php?id=8
  - [3] https://homeiphub.com/providers/aaitr/
