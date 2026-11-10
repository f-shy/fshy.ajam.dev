# deSEC

> desec.io | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/desec/ | JSON https://fshy.ajam.dev/api/v1/entity/desec.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## deSEC

- `domains-dns/desec` | qualifies | evidence reported | binding write-gated | category managed authoritative DNS with a full REST API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:20:29.067Z (live) | stale on 2026-11-19
- url https://desec.io/
- free tier: free managed DNS with anycast, a full REST API, DNSSEC and no published query cap; the number of domains an account may hold is a per-account limit_domains value that deSEC does not publish as a fixed number: unless set explicitly it grows with the domains delegated to deSEC with DNSSEC enabled | unit: objects | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: no published record count cap; the binding limits are the domain count per account and the RRset change rate per domain
- retention: zones persist while the account is active; a domain not renewed is deleted after a grace period | source: [1]
- egress: no query cap is published; the metered quantity is API requests | metered: no | source: [2]
- identity: email | detail: email signup; a token per account
- interface: rest
- limits:
  - request-rate: RRset create, delete or modify: 2 per second, 15 per minute, 100 per hour, 300 per day, per domain [2]
  - request-rate: any authenticated or unauthenticated activity: 2,000 per day per account or per IP [2]
  - request-rate: dynDNS updates: 2 per 2 minutes per domain [2]
  - write-gated (binding): no fixed number is published: the per-account maximum is the read-only limit_domains field of the account object (the API reference example shows 15) and, unless deSEC has set a limit for the account explicitly, it grows with the domains delegated to deSEC with DNSSEC enabled; Names under dedyn.io are limited to 1 per account. A new account is reported to start at one, and a deSEC staff reply gives the formula max(1, s + round(sqrt(s))) for s DNSSEC-delegated domains [3]
- limits note: DNS reads are 10/s and 50/min; domain creation and deletion are 10/s, 300/min and 1,000/h; account actions with external effects are 3/min; a 429 carries Retry-After and the windows slide
- binding note: the change rate is generous for steady state. The domain counter is what stops a multi-zone scheme: it is not published, a new account is reported to begin at one domain, and raising it is a support request with a person in the queue.
- interface detail: a REST API with token authentication; the API speaks RRsets rather than individual records, and an empty subname is the zone apex
- tooling: the deSEC API directly, DNSControl, certbot and acme.sh with a DNS-01 hook, Terraform
- composes with: one small zone with a real API, and a support request per additional domain; the domain counter is what constrains a multi-zone scheme, not the change rate
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: The 300 changes a day per domain is generous for steady state and painful for provisioning: a 500-record import takes two days. Bulk endpoints exist and the docs recommend them, which is the alternative route. The domain counter is the constraint that is often recorded as 'no published cap', which is a different claim: deSEC publishes no fixed number, and its own forum gives one. The cap binds before the rate table does, and only a signup shows the number an account actually receives.
- evidence note: the API, the rate table and the account reference are first-party. The account reference documents the per-account domain limit (limit_domains) and how it grows with DNSSEC-delegated domains, and the domains reference documents the 403 on reaching it, but neither states a fixed number; the initial value of one and the staff formula come from deSEC's forum and an independent write-up, at the reported rung. free_tier.unit is objects, not unlimited, because the domain count is capped.
- evidence:
  - probe:https://desec.io/api/v1/domains/ 2026-10-22: 401, 58 bytes, 'Authentication credentials were not provided.', with WWW-Authenticate: Token and Allow: GET, POST, HEAD, OPTIONS. The endpoint exists and is token-authenticated
  - probe:https://desec.io/api/v1/auth/login/ 2026-10-22: 400 with '{"email":["This field is required."],"password":["This field is required."]}', a live DRF login endpoint
  - [2] 2026-10-22: dns_api_per_domain_expensive 2/s 15/min 100/h 300/day for RRset creation, deletion and modification per domain; user 2,000/day; dyndns 2/2min per domain; throttled requests return 429 with Retry-After
  - [4] 2026-10-22: 'If subname is empty, this is equal to {name}.' so the apex is addressable; a wildcard component is allowed once at the beginning of the name
  - [5] 2026-10-22: a deSEC staff reply: 'the limit is max(1, s + round(sqrt(s))), were s is the number of domains delegated to us with DNSSEC enabled', giving 6 for s=4
  - [6] 2026-10-22: 'New accounts are limited to one domain and there is a note when you add a domain: Contact support to apply for a higher limit.'
  - [7] 2026-10-22: an independent account: 'there is an initial limit of 1 domain per account. Right below is the note Contact support to apply for a higher limit.'
  - [8] 2026-10-22: the signup form says only 'Your first domain (you can add more later)', which is the closest thing to a published statement and gives no number
  - [3] 2026-11-03: the per-account domain limit (limit_domains) is not a fixed published number: it grows with the DNSSEC-delegated domains unless deSEC sets it explicitly | capture: sha256:ff57a1a792e0a7cf6ae782ca2b96401625088d13e90ab1bcf30b76f28827f425 | quote: Unless we have set a limit for your account explicitly, this number grows with the domains you have delegated to us securely (with DNSSEC enabled).
  - [3] 2026-11-03: limit_domains is a read-only per-account field in the account object, the maximum number of domains the user can create | capture: sha256:ff57a1a792e0a7cf6ae782ca2b96401625088d13e90ab1bcf30b76f28827f425 | quote: Maximum number of domains the user can create.
  - [9] 2026-11-03: the API enforces a per-account maximum and answers 403 when it is reached | capture: sha256:6506f0790ed2b9a146b4c09ccaf796724a72402c43e0cc9b9b6887cf22612257 | quote: If you have reached the maximum number of domains for your account, the API responds with `403 Forbidden`.
  - [9] 2026-11-03: names under dedyn.io are limited to 1 per account | capture: sha256:6506f0790ed2b9a146b4c09ccaf796724a72402c43e0cc9b9b6887cf22612257 | quote: Domains that we offer for registration ourselves, such as those directly under `dedyn.io`, are limited to one per account.
- sources:
  - [1] https://desec.io/
  - [2] https://desec.readthedocs.io/en/latest/rate-limits.html
  - [3] https://desec.readthedocs.io/en/latest/auth/account.html
  - [4] https://desec.readthedocs.io/en/latest/dns/rrsets.html
  - [5] https://talk.desec.io/t/feedback-about-recent-limit-changes/1834
  - [6] https://talk.desec.io/t/how-to-apply-for-a-spot/1370
  - [7] https://yepoleb.at/blog/2025/10/27/my-experience-with-desec/
  - [8] https://desec.io/signup
  - [9] https://desec.readthedocs.io/en/latest/dns/domains.html
