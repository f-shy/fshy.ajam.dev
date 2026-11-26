# ProxyScrape

> proxyscrape.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxyscrape/ | JSON https://fshy.ajam.dev/api/v1/entity/proxyscrape.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ProxyScrape

- `ip-proxy/proxyscrape-free-list` | dead | evidence measured | binding request-rate | category public proxy list | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-24T10:07:11.000Z (live) | stale on 2026-11-24
- url https://proxyscrape.com/free-proxy-list
- free tier: Free, no account: the page states 20,000+ live proxies. The format=text endpoint returned exactly 2,000 rows on 2026-10-24, so the offer that can actually be pulled is 2,000 addresses per response: 1,357 SOCKS5, 409 HTTP, 234 SOCKS4. | unit: requests | metered on: none | read on: 2026-10-24 | source: [1] | note: The 2,000 is a per-response row cap, not a metered allowance: nothing is charged and nothing is metered. Two pulls five minutes apart were both served, with no refusal observed in either.
- per-object cap: not applicable | source: [2] | note: The nearest thing to an object cap is the 2,000-row response ceiling, recorded in limits[] as request-rate.
- retention: not applicable: a live proxy address, not stored bytes | source: [2] | note: An address is not durable. The payload rate moved from 32 of 100 to 30 of 100 across two runs five minutes apart, so the set a pull returns does not hold its working fraction even within one session.
- egress: ProxyScrape publishes public proxy lists without charging fees or imposing explicit bandwidth quotas. Network traffic traverses third-party host endpoints whose individual upstream terms are unpublished. | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: No account, key or email: the format=text endpoint answered an unauthenticated GET on 2026-10-24 and the 2,000-row body was used as returned.
- interface: rest
- limits:
  - request-rate (binding): 2,000 rows per response on format=text, against the page's claim of 20,000+ live proxies: the body was exactly 2,000 lines [2]
- limits note: Two further constraints were found that name no vocabulary kind, so they are kept here rather than forced into one. First, yield: of 100 sampled addresses, 38 completed a handshake and 32 carried a payload, and five minutes later 34 and 30, so about 70% of the list cannot move a byte at the moment it is pulled. Second, attribution: the response carries no ASN field, so there is no way to know whose network an address belongs to without spending a request on it. That absence is what puts rung 5 out of reach before the first use.
- binding note: The response is capped at 2,000 rows against an advertised 20,000+, so the ceiling that can be reached is the size of one response, not the size of the published pool; that cap arrives before any byte quota, which does not exist, and before any per-address shaping, which no evidence here shows. The 30% payload rate then cuts the working set to roughly 600 addresses, which is the figure that actually decides the gateway, but it is a yield property of the addresses rather than a limit the vendor sets.
- interface detail: One unauthenticated HTTP GET on api.proxyscrape.com/v4/free-proxy-list/get, which returned Content-Type text/plain with Transfer-Encoding chunked. The addresses it returns speak socks5, http and socks4 (1,357 / 409 / 234 of the 2,000 rows). The schema's interface enum has no token for a proxy protocol, so the three protocols are named here rather than in the array.
- endpoint: https://api.proxyscrape.com/v4/free-proxy-list/get (format=text)
- tooling: A single curl, or any HTTP client, pulls the list; no account, key, SDK or wrapper is involved. Using an address afterwards needs a client that speaks the protocol it is published under (SOCKS5, SOCKS4, or HTTP CONNECT), which curl and rclone both do natively.
- composes with: It is a supply of last-resort egress addresses for the Workers AI gateway: a request a Worker cannot make from its own address is retried through a published address, at roughly a 30% payload rate and with an exit network nobody has identified.
- reliability: The addresses are open proxies of unknown ownership: 32 of 100 sampled carried a payload and 30 of 100 five minutes later, the response publishes no ASN field, and the exit network is therefore unknown until an address is actually used.
- notes: Operational characteristics and reliability measurements for the ProxyScrape free proxy list. While website marketing claims over 20,000 proxies, API endpoints return a fixed cap of 2,000 rows per request. Responses contain raw host and port entries without ASN or network metadata annotations. Payload yield testing on 2026-10-24: across repeated samples of 100 endpoints taken five minutes apart, 30 percent successfully delivered HTTP payloads. Failed connections exhibited connection resets, EOFs, and TLS handshake failures. The list exhibits high rates of stale and unresponsive endpoints. Protocol support includes HTTP, SOCKS4, and SOCKS5 as documented in interface_detail and limits_note.
- evidence note: The 2,000-row cap, the protocol split and the two payload rates were each measured from the endpoint's own output on 2026-10-24, and the measurement is what contradicts the page's 20,000+ claim. Moving up one would need a sample larger than 100 and runs spread across a day, so that a diurnal effect can be told apart from a dead list.
- extras:
  - rung: 2
  - rung_note: The product is a supply of single addresses rather than a subnet or an ASN block, so rung 2 is the furthest reachable before spending a request on an address.
  - protocol_split.socks5: 1357
  - protocol_split.http: 409
  - protocol_split.socks4: 234
  - protocol_split.total: 2000
  - payload_rate_run1: 32 of 100
  - payload_rate_run2: 30 of 100
  - handshake_rate_run1: 38 of 100
  - handshake_rate_run2: 34 of 100
  - asn_field: no
  - advertised_count: 20,000+ live proxies
  - served_count: 2000
  - sample_size: 100 addresses per run, two runs five minutes apart
- evidence:
  - [1] 2026-10-24: The vendor's own figure for the free list is 20,000+ live proxies, which the measured 2,000-row format=text response contradicts.
  - [2] 2026-10-24: format=text answered an unauthenticated GET with exactly 2,000 lines: 1,357 socks5, 409 http, 234 socks4, served as text/plain with Transfer-Encoding chunked. No ASN field appears in the response.
  - probe:kept-privately 2026-10-24: First run over 100 sampled addresses: 38 completed a handshake and 32 carried a payload, 32%, with the failures logged as connection resets, EOFs and wrong-version TLS errors.
  - probe:kept-privately 2026-10-24: Second run five minutes later over 100 sampled addresses: 34 handshakes and 30 payloads, 30%, so the low yield repeats rather than being a single bad sample.
- sources:
  - [1] https://proxyscrape.com/free-proxy-list
  - [2] https://api.proxyscrape.com/v4/free-proxy-list/get
