# AirProxy

> airproxy.io | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/airproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/airproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AirProxy

- `ip-proxy/airproxy-mobile` | fails-identity | evidence documented | binding per-ip-shaping | category mobile proxy, 4G modem exit | tier paid
- needs card no, phone yes, ID yes, institution no | verified 2026-11-04T00:12:40.650Z (live) | stale on 2026-12-05
- url https://airproxy.io/en/
- price no comparable per-TB figure: the product is priced per proxy, EUR 67 per proxy per 30 days, and a 72-hour trial costs EUR 9.90.
- free tier: No free tier. The vendor's /en/ page lists a 72-hour trial at EUR 9.90 and a plan at EUR 67 per proxy per 30 days. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The trial is a short paid plan, not a free allowance.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a rented exit address, not stored bytes | source: [1]
- egress: No traffic sentence was found on any reachable page. The facts carry no vendor statement on bandwidth, byte allowance or a per-GB price, and the pages that would carry one returned 404 while the purchase page is behind signup. metered is false because no byte price was found and the product is sold per address, which is the reading of a price model rather than a quoted promise; a reader should treat the traffic position as unstated. | metered: no | free allowance: unstated: no allowance or cap published on a reachable page | source: [2]
- identity: national-id | detail: Vendor's own words: 'we recommend to verify your identity by submitting valid id proof and selfie'. Italian customers must supply a VAT number or fiscal code. The recommendation is worded as advice and the tax identifier is worded as a requirement. The pair is recorded as national-id because the mandatory half is an Italian tax identifier, not an email address or a phone number. | country: IT
- interface: unknown
- limits:
  - per-ip-shaping (binding): 1,200+ Italian 4G modems, one dedicated SIM per exit: the ceiling is one SIM's throughput and one address's reputation, not a byte allowance [1]
- limits note: The vendor's /en/ page publishes the price (EUR 67 per proxy per 30 days, 72-hour trial at EUR 9.90) and lists 'Unlimited Bandwith' in the plan; it publishes no request-rate, volume or write constraint, so limits[] carries the one constraint the vendor states. The identity gate is recorded in identity_cost and the price in free_tier and extras; neither is a kind in this vocabulary.
- binding note: About 599,000 requests and 45 GB a month is a low request rate, so no rate limit or byte quota would fail first; the exit is one dedicated SIM, shaped by its carrier and carrying every request made through it, so per-address throughput decides the design. The identity wall arrives before any capacity constraint, which is why the verdict is fails-identity and not fails-quota.
- interface detail: The vendor sells a proxy endpoint. The specific communication protocol is not stated in documentation, and no API, SDK, or port number is published. The protocol is classified as unknown.
- tooling: An account, then a client that speaks the endpoint's protocol, which was not established. No SDK, rclone backend or documented API is recorded. The absent wrapper is a note about tooling, not a verdict: it is a weekend of work against capacity that already exists.
- composes with: The proxy would be the exit for traffic the gateway sends out. It fixes the country and carrier of the source address and supplies no storage or compute of its own, so it combines with any service that judges a request by the nationality of the exit.
- reliability: No reliability observation was recorded: no endpoint was reached, so throttle behaviour, rotation interval and drop rate are unverified.
- notes: The wording separates them, 'we recommend' against 'must supply', and the record follows the wording rather than the stronger reading, which is why confidence_note names 'recommend' as the soft spot; The facts do not record which of the two URLs carried the identity sentence, so it is attributed to the purchase page because the tax-identifier clause beside it is a billing clause; that attribution is an inference from one sample of each page. The class claim, dedicated SIMs on four named carriers in three rooms, is the vendor's own sentence and was not probed, so 1,200+ is the vendor's count and one request through an endpoint would turn it from documented to measured.
- evidence note: The verdict rests on identity alone, which is quoted from the vendor's own page, so the record is documented. Egress and interface were not established and say so; neither can move the verdict, because without an account neither is reachable. Measured would need an account and a request through an endpoint, and neither was attempted. The soft spot is the word 'recommend': the ID and selfie clause is advice, and the mandatory clause is the tax identifier.
- extras:
  - rung: 5
  - rung_note: The barrier is a registration class rather than a session, a single address, a subnet or an ASN: the gate is an ID document with a selfie plus an Italian tax identifier, and nothing below rung 5 describes it.
  - modems: 1,200+
  - carriers: Vodafone, TIM, WindTre, Fastweb
  - server_rooms: three, between Padova and Vicenza
  - trial: 72 hours for EUR 9.90
  - price_reported: EUR 67 per proxy per 30 days, vendor-documented at https://airproxy.io/en/ (Pricing section)
  - price_paths_404: /pricing, /en/pricing, /en/4g-proxy
  - identity_sentence: we recommend to verify your identity by submitting valid id proof and selfie
  - identity_second_gate: Italian customers must supply a VAT number or fiscal code
  - price_monthly: EUR 67 per proxy per 30 days
- evidence:
  - [1] 2026-10-24: The pool is 1,200+ Italian 4G modems on Vodafone, TIM, WindTre and Fastweb, in three server rooms between Padova and Vicenza; a dedicated SIM per exit is the class claim.
  - [2] 2026-10-24: The 72-hour trial is EUR 9.90, Italian customers must supply a VAT number or fiscal code, and the purchase flow sits behind signup. The identity sentence 'we recommend to verify your identity by submitting valid id proof and selfie' was read on the vendor's own pages this date, but the facts do not record which of the two URLs carried it; re-read both before citing this entry for it.
  - [3] 2026-10-24: Returned 404, so no price page exists at this path and the monthly price is a documented absence rather than an unread page.
  - [4] 2026-10-24: Returned 404, the second of three price paths that carry nothing.
  - [5] 2026-10-24: Returned 404, so the product page path carries no price and no traffic allowance either.
  - [1] 2026-11-02: The raw HTML of the vendor's /en/ page lists the monthly plan in its Pricing section at EUR 67 per proxy per 30 days. | capture: sha256:17d42e5a786d0cdd3f6c67acd67dfbeac5bada008e93dcd15e3983664461dab5 | quote: <h2><sup>€</sup><span>67</span> <small class="text-muted">/ proxy / 30 days</small></h2>
  - [1] 2026-11-02: The raw HTML of the vendor's /en/ page lists a 72-hour trial at 9.90 EUR and a plan at EUR 67 per proxy per 30 days. | capture: sha256:17d42e5a786d0cdd3f6c67acd67dfbeac5bada008e93dcd15e3983664461dab5 | quote: Try it for 72 hours at 9.90€ ... <span>67</span> <small class="text-muted">/ proxy / 30 days</small>
  - [1] 2026-11-02: The raw HTML of the vendor's /en/ page sells the 72-hour trial at 9.90 EUR with a Buy 3-Day Trial button, so the trial is a paid plan. | capture: sha256:17d42e5a786d0cdd3f6c67acd67dfbeac5bada008e93dcd15e3983664461dab5 | quote: Try it for 72 hours at 9.90€ ... Buy 3-Day Trial
  - [1] 2026-11-02: The raw HTML of the vendor's /en/ page lists a 72-hour trial at 9.90 EUR. | capture: sha256:17d42e5a786d0cdd3f6c67acd67dfbeac5bada008e93dcd15e3983664461dab5 | quote: Try it for 72 hours at 9.90€
  - [1] 2026-11-03: the vendor's /en/ page itself states the 72-hour trial at 9.90 EUR that free_tier.stated restates | capture: sha256:39287db29e4bf9e076bc30319a1884a4992650e081a2df47e37833b660ba3f8b | quote: Try it for 72 hours at 9.90€
  - [1] 2026-11-03: the /en/ page, read on this date, lists the plan at EUR 67 per proxy per 30 days | capture: sha256:39287db29e4bf9e076bc30319a1884a4992650e081a2df47e37833b660ba3f8b | quote: <h2><sup>€</sup><span>67</span> <small class="text-muted">/ proxy / 30 days</small></h2>
  - [1] 2026-11-03: the plan lists unlimited bandwidth and the page states a price, so no volume constraint is published and the price is published | capture: sha256:39287db29e4bf9e076bc30319a1884a4992650e081a2df47e37833b660ba3f8b | quote: <div class="pricing-item bg">Unlimited Bandwith</div>
  - [1] 2026-11-03: the vendor's own page lists EUR 67 per proxy per 30 days | capture: sha256:39287db29e4bf9e076bc30319a1884a4992650e081a2df47e37833b660ba3f8b | quote: <h2><sup>€</sup><span>67</span> <small class="text-muted">/ proxy / 30 days</small></h2>
  - [1] 2026-11-03: the plan price and trial on the /en/ page are unchanged | capture: sha256:39287db29e4bf9e076bc30319a1884a4992650e081a2df47e37833b660ba3f8b | quote: <h2><sup>€</sup><span>67</span> <small class="text-muted">/ proxy / 30 days</small></h2>
- sources:
  - [1] https://airproxy.io/en/
  - [2] https://airproxy.io/en/accounts/profile/purchase/
  - [3] https://airproxy.io/en/pricing
  - [4] https://airproxy.io/pricing
  - [5] https://airproxy.io/en/4g-proxy
