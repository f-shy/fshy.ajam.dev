# DuckDNS

> duckdns.org | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/duckdns/ | JSON https://fshy.ajam.dev/api/v1/entity/duckdns.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DuckDNS

- `domains-dns/duckdns` | qualifies-with-caveat | evidence measured | binding per-object-cap | category free dynamic subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-02T10:17:37.731Z (live) | stale on 2027-02-01
- url https://www.duckdns.org/spec.jsp
- free tier: subdomains under duckdns.org with a token API, IPv4, IPv6 and TXT support | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: the number of subdomains per account is about 5, a third-party figure; DuckDNS publishes no number
- retention: a record persists until updated or cleared with clear=true, provided the account is used | source: [1]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: Google, GitHub or Reddit OAuth
- interface: rest
- limits:
  - per-object-cap (binding): about 5 subdomains, a third-party figure; DuckDNS publishes no number [1]
- interface detail: a single HTTPS GET per update; the token is a query parameter
- tooling: curl, any DDNS client, a router's built-in DuckDNS provider
- composes with: a name for a home IP or a tunnel endpoint, and nothing else: no certificate automation and no proxying
- reliability: a bad token returns HTTP 200 with the body KO, so a status-only check reports success on a failed update
- notes: A DuckDNS name cannot be a Cloudflare zone, so it cannot carry a Tunnel, Email Routing or Universal SSL. It is a dynamic-DNS tool, not a name a service can live on.
- evidence note: the update endpoint was called today with an empty token and answered 200 KO, which proves both the endpoint and the failure shape. The subdomain cap is third-party.
- evidence:
  - probe:https://www.duckdns.org/update?domains=example&token=&ip= 2026-10-22: 200 with a two-byte body 'KO'. A 200 is not success; the rejection is in the body
  - [1] 2026-10-22: the update URL, IPv4 and IPv6 parameters, the TXT form, and clear=true to delete records; a TXT record applies to all sub-subdomains under the name
  - [1] 2026-11-02: the update is a single HTTPS GET to DuckDNS | capture: sha256:e44c623b17f38e48ed7e76eb9c55006a3474059f47c69f325427ad54cdedb50f | quote: You can update your domain(s) with a single HTTPS get to DuckDNS
  - [1] 2026-11-02: clear=true makes the update call clear the IPv4 and IPv6 values of the named subnames instead of setting them | capture: sha256:e44c623b17f38e48ed7e76eb9c55006a3474059f47c69f325427ad54cdedb50f | quote: clear - OPTIONAL - if set to true, the update will ignore all ip's and clear both your records
  - [1] 2026-11-02: the update call is a GET to duckdns.org/update with the subnames and the account token as query parameters | capture: sha256:e44c623b17f38e48ed7e76eb9c55006a3474059f47c69f325427ad54cdedb50f | quote: https://www.duckdns.org/update?domains={YOURVALUE}&token={YOURVALUE}[&ip={YOURVALUE}][&ipv6={YOURVALUE}][&verbose=true][&clear=true]
- sources:
  - [1] https://www.duckdns.org/spec.jsp
