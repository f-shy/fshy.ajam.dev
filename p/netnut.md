# NetNut

> netnut.io | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netnut/ | JSON https://fshy.ajam.dev/api/v1/entity/netnut.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NetNut

- `ip-proxy/netnut-seized` | dead | evidence documented | binding none | category residential proxy network | tier none
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:28:51.269Z (live) | stale on 2026-11-30
- url https://netnut.io/
- free tier: nothing reachable: both https://netnut.io/ and https://netnut.com/ returned an FBI seizure notice on every path tried, including /pricing/ and /robots.txt, on 2026-10-24, so no offer, allowance or price could be read | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: Eight paths across the two domains were fetched: the roots, /robots.txt, /pricing/ and /api on netnut.io, and the roots, /robots.txt, /pricing/ and /status on netnut.com. All eight returned HTTP 200 with exactly 297,312 bytes.
- per-object cap: not applicable | source: [2] | note: no stored object exists to cap. What a residential proxy sells is traffic through an address, and the traffic figure is the one no page would state.
- retention: not applicable: a live proxy session, not stored bytes | source: [2]
- egress: unverified: no traffic term could be read. Both https://netnut.io/ and https://netnut.com/ served the seizure notice on every path tried on 2026-10-24, including /robots.txt. The metered flag is false because no published meter was found to record, not because traffic was free. | metered: no | source: [2]
- identity: email | detail: unverified: netnut.io and netnut.com answer every path, /robots.txt included, with the HTML page titled 'Seized by the Federal Bureau of Investigation', so no signup page or registration requirement can be read; the email kind is not an observed gate.
- interface: unknown
- limits note: No constraint of any kind could be read: both domains serve the seizure notice on every path, so there is no rate, cap, quota or shaping figure to record. The event that ends the offer is the seizure of the domains, and it is in reliability_note because it is not one of the vocabulary kinds.
- binding note: No limit kind binds: the offer ended with the seizure of NetNut's domains by the FBI, which Alarum Technologies says it learned of on 2026-07-02, and a seizure is an event, not a limit kind.
- interface detail: unknown because nothing is served: both domains answer every path with the seizure notice, so no API, proxy endpoint or web UI could be observed. A residential proxy is consumed by pointing a SOCKS5- or HTTP-proxy-capable client at an endpoint the vendor issues; that is the category's normal shape and it was not observed here.
- tooling: Nothing to point a client at: the domains answer with an HTML page titled 'Seized by the Federal Bureau of Investigation', even on /robots.txt, instead of a proxy endpoint or a credential, so the missing part is the endpoint, not a client.
- composes with: Nothing to chain: the domains answer HTTP 200 with an HTML page titled 'Seized by the Federal Bureau of Investigation', even on /robots.txt, instead of a proxy handshake, so there is no endpoint to route a request through.
- reliability: Domains seized by the FBI: netnut.io and netnut.com returned the same 297,312-byte page on every path tried, including /robots.txt and /pricing/, on 2026-10-24, so no proxy endpoint, credential or status page answers.
- notes: Alarum Technologies, the parent of NetNut Ltd., states in Exhibit 99.2, its press release of July 3, 2026, that on July 2, 2026 the company and NetNut 'became aware that certain domains associated with NetNut had been seized by the U.S. Federal Bureau of Investigations (“FBI”)', that 'additional domains associated with NetNut have also been seized', and that 'the Company is currently experiencing disruptions to a portion of its services'. The exhibit gives no date for a return of the domains or of the service.
- evidence note: Documented: the verdict rests on a first-party statement, Alarum Technologies' Exhibit 99.2, that certain domains associated with NetNut were seized by the FBI.
- extras:
  - rung: 2
  - rung_note: A residential network is bought to present a different single address, which is rung 2 and the cheapest rung to clear, and it is the category that also reaches rung 5 through eyeball-registered prefixes, but no page read here established a registration class and nothing is purchasable now.
  - provider_as_written: NetNut (Alarum Technologies)
  - domains_checked: netnut.io and netnut.com, eight paths, all HTTP 200 at 297,312 bytes on 2026-10-24
- evidence:
  - [2] 2026-10-24: The body holds one embedded base64 JPEG and no other text, so the title is the only machine-readable statement the page makes and the notice's own wording is not quotable from the HTML.
  - [3] 2026-10-24: the same 297,312-byte seizure page rather than a robots.txt, so the notice is served on every path and not only on the site root; this is what rules out a vendor challenge page or a single broken route.
  - [4] 2026-10-24: HTTP 200, 297,312 bytes, the same title: the second domain carries the same notice, so there is no alternate hostname to fall back to.
  - [1] 2026-10-24: HTTP 200, 297,312 bytes, the seizure page: the pricing route that would have carried the offer returns the notice, which is why free_tier records nothing reachable.
  - [5] 2026-10-24: Alarum Technologies Exhibit 99.2, a press release issued 2026-07-03: 'As previously disclosed, on July 2, 2026, the Company and its subsidiary, NetNut Ltd. ("NetNut"), became aware that certain domains associated with NetNut had been seized by the U.S. Federal Bureau of Investigations ("FBI").' The same exhibit adds that 'additional domains associated with NetNut have also been seized' and that 'the Company is currently experiencing disruptions to a portion of its services.'
  - [5] 2026-10-30: Alarum Technologies states that on July 2, 2026 it and its subsidiary NetNut Ltd. learned that NetNut domains had been seized by the FBI | capture: sha256:816766e5cd9f8117ff417bdc11d28d29d78b6023f7569fd1fd8f7e31a46d2aba | quote: As previously disclosed, on July 2, 2026, the Company and its subsidiary, NetNut Ltd. (“NetNut”), became aware that certain domains associated with NetNut had been seized by the U.S. Federal Bureau of Investigations (“FBI”).
  - [3] 2026-10-30: netnut.io answers /robots.txt with HTTP 200 and the HTML seizure page instead of a robots file or a proxy service | capture: sha256:d140d6d17ae9469ab61eb6a219aec63e23d4feeac1b24e049ef640ef1846edd5 | quote: <title>Seized by the Federal Bureau of Investigation</title>
  - [6] 2026-10-30: netnut.com answers /status with HTTP 200 and the same HTML seizure page, so the second domain serves no status page either | capture: sha256:ab20ab48d7ac7b5b3f80dc19ce37d615e243f8442d3c4ae27b6571bd0cdc7477 | quote: <title>Seized by the Federal Bureau of Investigation</title>
- sources:
  - [1] https://netnut.io/pricing/
  - [2] https://netnut.io/
  - [3] https://netnut.io/robots.txt
  - [4] https://netnut.com/
  - [5] https://www.sec.gov/Archives/edgar/data/1725332/000121390026075170/ea029706002ex99-2.htm
  - [6] https://netnut.com/status
