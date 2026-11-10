# tacs.cloud

> tacs.cloud | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tacs/ | JSON https://fshy.ajam.dev/api/v1/entity/tacs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tacs.cloud (TA Consulting & Services GmbH)

- `ip-proxy/tacs-cloud-ipv4-lease` | paid-only | evidence documented | binding volume-quota | category prefix lease (RIPE LIR) | tier IPv4 lease by the /24
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:35:33.762Z (live) | stale on 2026-12-04
- url https://tacs.cloud/lease-ipv4/
- free tier: No free tier. The site's IP calculator states the lease rate per address: 'Lease per IP per month: RIPE $0.38, ARIN $0.32, APNIC $0.40', in 'USD per IP, excl. VAT', and the lease page says 'Lease prices depend on block size, registry and term.' | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The rates are the calculator's published per-address figures; the final price 'depends on the block, its reputation and the terms', and a lease is a quote request, not a checkout. The lease terms, minimum duration and any setup fee are not on the pages read.
- per-object cap: not applicable: an address block, not an object; the smallest lease unit is a /24 | source: [2] | note: The home page states 'Smallest unit we lease: /24' and the lease page sells 'Clean IPv4 space by the /24'.
- retention: not applicable: a leased block, not stored bytes | source: [3] | note: The lease page says 'for as long as you need it' and lists a signed lease contract as step 3 of 5; no term, notice or minimum duration is stated. unverified: the contract terms, which come with the offer.
- egress: not applicable: the vendor leases address space announced from the lessee's ASN; it does not carry the traffic. | metered: no | free allowance: not applicable: no traffic is carried by the lease | source: [3]
- identity: email | detail: unverified: a lease starts as a quote request. The contact form asks for name, email and a topic ('We use your details only to answer your request.'), and the process then goes request, offer, agreement ('Lease contract signed') and setup. Whether the contract needs company documents, a KYC or a card was not readable: behind a sign-up. The lease is announced 'from your ASN', so an ASN of the lessee is required.
- interface: unknown
- limits:
  - volume-quota (binding): smallest lease unit is a /24: 'Smallest unit we lease: /24'; at the RIPE rate of $0.38 per IP per month a /24 is 256 addresses [2]
- limits note: The vocabulary has no kind for a minimum block size or a required ASN; volume-quota is the nearest for the /24 minimum, and the ASN requirement is stated in tooling and identity. Rates differ by registry (RIPE $0.38, ARIN $0.32, APNIC $0.40 per IP per month).
- binding note: The /24 minimum is the smallest purchase, and the lease announces from the lessee's ASN, which a reader without an ASN does not have; the limit vocabulary has no kind for an ASN requirement.
- interface detail: A quote request form on the contact page and an IP calculator; no portal, API or client tool is shown on the pages read.
- tooling: The lessee's own BGP session: the lease page says the space is 'Announced from your ASN, with ROA and reverse DNS set up' and includes an LOA to announce the block from the ASN, a ROA, delegated reverse DNS and a reputation report. The vendor does not state that it announces the block for a lessee.
- composes with: A leased /24 is 256 addresses in one prefix and one registry object, so it is one rung-3 unit, and the lessee needs an ASN of its own to announce it. The vendor is itself a RIPE NCC LIR, so a RIPE lease is the vendor's own registry space; no delivered block was inspected.
- reliability: unverified: no delivered block, test address or registry object is published. The vendor states a reputation report for the block 'before handover' and describes itself as a RIPE NCC LIR.
- evidence note: Documented: the per-address rates, the /24 minimum, the ASN-announcement model and the RIPE LIR status are stated on the vendor's pages, captured 2026-11-03. The contract terms, identity checks beyond the contact form and the registry object of a delivered block are unverified.
- extras:
  - role: RIPE LIR that buys, sells and leases blocks and also leases out on behalf of owners at a 15% commission
  - min_prefix: /24
  - price_per_address_month: USD 0.38 (RIPE), USD 0.32 (ARIN), USD 0.40 (APNIC), excluding VAT
  - price_derived: USD 0.38 x 256 = USD 97.28 per month for a RIPE /24; USD 0.32 x 256 = USD 81.92 for ARIN; USD 0.40 x 256 = USD 102.40 for APNIC, before VAT
  - registries: RIPE NCC, ARIN, APNIC
  - needs_own_asn: yes
  - rung: 3
  - rung_note: One /24 is one rung-3 unit; rung 5 is unverified until a delivered block's registry object is read.
- evidence:
  - [1] 2026-11-03: the lease price per address per month by registry: RIPE $0.38, ARIN $0.32, APNIC $0.40 | capture: sha256:3bb16c331f4bb16835df81122d0732473185056d037646544b1c0bdf533b490c | quote: Lease per IP per month: RIPE $0.38, ARIN $0.32, APNIC $0.40; leasing out pays the owner these rates minus our 15%.
  - [1] 2026-11-03: the prices are in US dollars per address and exclude VAT | capture: sha256:3bb16c331f4bb16835df81122d0732473185056d037646544b1c0bdf533b490c | quote: Prices in USD per IP, excl. VAT.
  - [2] 2026-11-03: the smallest block leased is a /24, routed with a ROA and rDNS | capture: sha256:ad616f06e0ef38996840ddd746de9ed3535bace4a3d4a378e36abf40ba3b2652 | quote: Smallest unit we lease: /24 Routed with ROA & rDNS
  - [3] 2026-11-03: leases are by the /24 and are announced from the lessee's ASN, with ROA and reverse DNS | capture: sha256:74a88de91b351eaafeec7fa4e9e211dc8c82e76878a80ecba05e04e4b8ed1c62 | quote: Clean IPv4 space by the /24, for as long as you need it. Announced from your ASN, with ROA and reverse DNS set up.
  - [3] 2026-11-03: the final lease price depends on block size, registry and term and is quoted on request | capture: sha256:74a88de91b351eaafeec7fa4e9e211dc8c82e76878a80ecba05e04e4b8ed1c62 | quote: Lease prices depend on block size, registry and term. Get an estimate in the [IP calculator](https://tacs.cloud/ip-calculator/) or ask for a quote.
  - [3] 2026-11-03: a lease contract is signed before setup | capture: sha256:74a88de91b351eaafeec7fa4e9e211dc8c82e76878a80ecba05e04e4b8ed1c62 | quote: Lease contract signed.
  - [4] 2026-11-03: the vendor is a RIPE NCC Local Internet Registry | capture: sha256:bb81022597f68334a1d0957c2eed3b7c5fa9675b2f6631f53399f2ba85ddf9ee | quote: TA Consulting & Services GmbH is an IT consultancy and a RIPE NCC Local Internet Registry.
  - [5] 2026-11-03: the contact form collects details only to answer a request; a lease starts as a quote request | capture: sha256:b36768e5f9be3e2e5885ebb70aab6bc0234436eef77c71e4920c55342e60e7a0 | quote: We use your details only to answer your request.
  - [3] 2026-11-03: the lease includes an LOA to announce the block from the lessee's ASN | capture: sha256:74a88de91b351eaafeec7fa4e9e211dc8c82e76878a80ecba05e04e4b8ed1c62 | quote: LOA to announce the block from your ASN.
  - [3] 2026-11-03: a reputation report for the leased block is delivered before handover | capture: sha256:74a88de91b351eaafeec7fa4e9e211dc8c82e76878a80ecba05e04e4b8ed1c62 | quote: Reputation report for the leased block before handover.
- sources:
  - [1] https://tacs.cloud/ip-calculator/
  - [2] https://tacs.cloud/
  - [3] https://tacs.cloud/lease-ipv4/
  - [4] https://tacs.cloud/about/
  - [5] https://tacs.cloud/contact/?topic=ip
