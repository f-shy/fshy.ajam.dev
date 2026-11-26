# Safelinking

> safelinking.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/safelinking/ | JSON https://fshy.ajam.dev/api/v1/entity/safelinking.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Safelinking

- `debrid/safelinking` | dead | evidence reported | binding none | category link container / link protector with a public HTTP API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:50.031Z (live) | stale on 2026-12-10
- url https://safelinking.net/
- price USD 0
- free tier: A protect API is published with no account field: POST https://safelinking.net/api with 'links-to-protect' mandatory and optional captcha, password, title, provider and mirror fields, plus rsdf/dlc/rtc/cnl2 container output. No price list or quota appears on the API page or the front page. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The front page is the same form with 'Mirrors', 'Package details' and 'Security Options' (captcha, package password, IP filtering). Nothing on it names a limit.
- per-object cap: not applicable: it protects link lists; the linked host's cap applies when the file is fetched. | source: [1]
- retention: unverified: no retention statement found. Old links (a 2018 post cites two) were still being discussed, but none was fetched successfully. | source: [2]
- egress: No egress of its own: a package page sends the visitor to the host links. | metered: no | free allowance: none: no service-side bytes | source: [2]
- identity: anonymous | detail: The documented protect call has no credential field, but the same API page documents a separate Auth mode with a username and password parameter that returns an api_hash.
- interface: rest
- limits:
  - write-gated: captcha is optional but on by default in the form (recaptcha or fancy captcha) [2]
  - request-rate: unstated [1]
- limits note: No byte quota, no account quota and no per-day generation count is published.
- binding note: Nothing in the vocabulary binds at 1 TiB/month because no bytes pass through Safelinking; the only gate is its optional captcha on creation.
- interface detail: Two documented HTTP endpoints: POST /api to protect (returns the package URL) and GET /check?link=<package>&output=JSON|XML for a link_status check. Container exports: RSDF, DLC, CCF and CNL2. Short links on sflk.in.
- endpoint: part of the free tier
- tooling: Any HTTP client; the API is form-encoded and documented in the project's GitHub README. JDownloader has a safelinking decrypter.
- composes with: It is the indirection half of a pipeline: protect a set of host links, then hand the package URL to a downloader. It does not resolve to direct links and does not bypass any host limit.
- reliability: The domain did not complete a TCP connection from this host: two probes timed out after 21 s (connect error 10060) while network requests returned a provider snapshot of the same page. Treat reachability as location-dependent, not as uptime.
- notes: Answers half the sector question negatively: it will mint a protected link anonymously over HTTP, but it does not resolve anything to a direct link and it adds a captcha rather than removing one. If a wrapper is wanted, the API exists and is documented; if direct links are wanted, this is not it.
- evidence note: The API documentation is a first-party GitHub page; a live origin read returned a domain-parking page and a direct probe failed. The hosted service was not reached, so the rung stays reported.
- extras:
  - api_endpoints: POST https://safelinking.net/api; GET https://safelinking.net/check?link=<package>&output=JSON
  - short_domain: sflk.in
  - reachability: timeout from this host
  - death.on: 2026-11-25
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-23: the protect API at https://safelinking.net/api with 'links-to-protect' mandatory and no credential field; the /check?link=&output=JSON|XML status endpoint; rsdf/dlc/rtc/cnl2 outputs
  - [2] 2026-10-23: the live form: Mirrors block, Package details, Security Options with captcha, package password and IP filtering
  - probe:https://safelinking.net/check?link=https://safelinking.net/s64aTFQ&output=JSON 2026-10-23: the API host did not answer this network: timeout after 21151.8 ms, 0 bytes, error 'timeout'
  - probe:https://safelinking.net/s64aTFQ 2026-10-23: the package host also timed out: 21133.5 ms, 0 bytes, error 'timeout'
  - [1] 2026-11-25: the API documentation includes a username credential parameter in its Auth mode | capture: sha256:3b9b169d2d2c739f8deb3e2b864cf7470db792180d4cd93d604cfdc24b59f085 | quote: username | Username of the user. | Input
  - [1] 2026-11-25: the protect API takes a mandatory links-to-protect field with no registration field | capture: sha256:3b9b169d2d2c739f8deb3e2b864cf7470db792180d4cd93d604cfdc24b59f085 | quote: The links you wish to protect, separated by line breaks or "%0A" (MANDATORY).
  - [2] 2026-11-25: the safelinking.net domain now shows a Namecheap domain-parking page rather than the link protection service | capture: sha256:db4c773775c3a27a26ec0b0407e360a07f0076fdd66df358637e1b1179ff4073 | quote: has been recently registered with namecheap.com
  - [2] 2026-11-25: the origin domain now serves a parking page rather than the service | capture: sha256:db4c773775c3a27a26ec0b0407e360a07f0076fdd66df358637e1b1179ff4073 | quote: has been recently registered with namecheap.com
- sources:
  - [1] https://github.com/safelinking/Safelinking
  - [2] https://safelinking.net/
