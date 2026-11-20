# Neustar

> digicert.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/digicert/ | JSON https://fshy.ajam.dev/api/v1/entity/digicert.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Neustar

- `domains-dns/neustar` | paid-only | evidence documented | binding write-gated | category managed authoritative DNS (UltraDNS) | tier UltraDNS (enterprise, sales-quoted)
- needs card unknown, phone unknown, ID no, institution yes | verified 2026-11-19T01:43:56.218Z (live) | stale on 2026-12-20
- url https://www.digicert.com/dns
- free tier: no self-serve free tier found; UltraDNS is an enterprise managed authoritative DNS platform sold through a sales contact, with flexible plans based on domains, queries, users and advanced features | unit: none | metered on: unstated | read on: 2026-11-19 | source: [1] | note: unverified: the former Neustar DNS pages at home.neustar answered HTTP 404 on 2026-11-19; the Neustar Security Services DNS line is now sold as Vercara / DigiCert UltraDNS, with no public free allowance. A historical free recursive DNS product is reported discontinued by a third party, not confirmed by a first-party page.
- per-object cap: no per-record or per-zone object cap published on the first-party pages read; the platform is quoted on request | source: [1]
- retention: unverified: no retention or expiry period published on the first-party pages read; zones are managed under an enterprise agreement | source: [1]
- egress: a managed authoritative DNS service; the platform is stated to handle up to 150 billion authoritative DNS queries per day, but no free query allowance or per-query price is published | metered: yes | source: [1]
- identity: institution | detail: the sales-led motion is aimed at organizations: the page says Talk to an expert and describes plans for organizations that require reliable, scalable and secure DNS infrastructure. No self-serve signup page was found, and the exact registration fields, card requirement and phone requirement are unverified: behind a sign-up and a sales contact.
- interface: rest, cli
- limits:
  - write-gated (binding): access is through a sales contact and an enterprise agreement; no public self-serve sign-up or free allowance is offered [1]
  - volume-quota: the platform is stated to manage up to 150 billion authoritative DNS queries per day at scale; this is a capacity figure, not an allowance for a single account [1]
- binding note: the DNS offer is an enterprise sales-quoted platform with no self-serve free tier, so the sales and contract gate binds before any query capacity or quota is relevant
- interface detail: a REST API and portal for DNS records; an UltraDNS Terraform provider automates DNS changes. API credentials are configured through the vendor console.
- endpoint: https://www.digicert.com/dns
- tooling: the UltraDNS Terraform provider, the UltraDNS API, a vendor portal; CertCentral integrates with UltraDNS for DNS domain control validation
- composes with: an enterprise authoritative DNS platform with traffic steering, failover, DNSSEC and an independent secondary Anycast network (UltraDNS 2); no self-serve free tier exists, so a free hosted DNS service is the path for a no-cost stack
- reliability: a 100 percent resolution availability SLA, 24/7 support and built-in DDoS protection are stated; no suspension, throttle or data-loss event was found on the pages read
- notes: Documented from first-party successor pages. The historical free Neustar recursive DNS product is reported discontinued by third parties but not confirmed first-party, so it is not used as a value here. No public read path was probed, so the rung stays documented.
- evidence note: the first-party DigiCert DNS page and the Neustar landing page were captured and quoted. The former home.neustar DNS URLs and the Vercara product and news URLs answered HTTP 404 on 2026-11-19, so the old Neustar DNS pages themselves could not be read; the current offer is documented through the successor DigiCert page. No public read path was probed, so the rung stays documented.
- self hosted: no
- evidence:
  - [1] 2026-11-19: the DNS offer is an enterprise managed authoritative DNS platform | capture: sha256:e615ec0298ea99d64fd0144f42b78d49bafef8a888292ae30e8f82eb8cf68b87 | quote: DigiCert UltraDNS is an enterprise-grade authoritative DNS platform built for high availability, performance, and resilience.
  - [1] 2026-11-19: plans are flexible and based on domains, queries and users, with no published free tier | capture: sha256:e615ec0298ea99d64fd0144f42b78d49bafef8a888292ae30e8f82eb8cf68b87 | quote: No. UltraDNS offers flexible plans based on the number of domains, DNS queries, users, and advanced features needed to support growth.
  - [1] 2026-11-19: access is through a sales contact rather than self-serve sign-up | capture: sha256:e615ec0298ea99d64fd0144f42b78d49bafef8a888292ae30e8f82eb8cf68b87 | quote: Talk to an expert
  - [1] 2026-11-19: the stated platform capacity for authoritative queries per day | capture: sha256:e615ec0298ea99d64fd0144f42b78d49bafef8a888292ae30e8f82eb8cf68b87 | quote: Manage up to 150 billion authoritative DNS queries per day
  - [1] 2026-11-19: enterprise support and SLA backing | capture: sha256:e615ec0298ea99d64fd0144f42b78d49bafef8a888292ae30e8f82eb8cf68b87 | quote: Get 24/7 support backed by enterprise SLAs
  - [2] 2026-11-19: the Neustar brand has been split and moved to other owners | capture: sha256:a4a30e5f8f77934c9f160fc267bf8263ee6c1077874262bab83f7962d0bd56bd | quote: Neustar's Marketing, Fraud, and Communications offerings are now a part of TransUnion's newly unified B2B portfolio of solutions.
  - [3] 2026-11-19: UltraDNS is reachable programmatically through API credentials | capture: sha256:b5179cfb957ac37ee5255279f6037d496830fa8e7fe6019219e9701676154bde | quote: CertCentral connects to UltraDNS using secure API credentials configured in the CertCentral console.
- sources:
  - [1] https://www.digicert.com/dns
  - [2] https://home.neustar/
  - [3] https://www.digicert.com/integrations/ultradns
