# MemCachier

> memcachier.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/memcachier/ | JSON https://fshy.ajam.dev/api/v1/entity/memcachier.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MemCachier

- `databases-kv/memcachier` | qualifies-with-caveat | evidence documented | binding volume-quota | category managed Memcached cache | tier Developer
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:19:24.795Z (live) | stale on 2026-12-20
- url https://www.memcachier.com/pricing
- free tier: Totally free forever. Try it out. See what it can do. Always $0 25MB 1 Proxy | unit: MB | metered on: stored-bytes | read on: 2026-11-19 | source: [1] | note: The free Developer plan is 25 MB of cache, one proxy server and 10 connections, with no end date stated (the price column reads 'Always').
- per-object cap: no per-item size cap is published on the pricing page; the plan's 25 MB is the whole cache | source: [1]
- retention: data lives in the Memcached cache until evicted or the cache is restarted; no automatic expiry schedule is stated on the pricing page | source: [1] | note: Memcached is an in-memory cache; retention is governed by eviction, not a published day count.
- egress: no egress allowance or per-GB price is published on the pricing page | metered: no | source: [1]
- identity: email | detail: The sign-up form asks for Email address and Password and is protected by reCAPTCHA. No card, phone or ID document is requested on the free sign-up page.
- interface: unknown
- limits:
  - volume-quota (binding): 25 MB of cache storage on the Developer plan [1]
  - request-rate: 10 connections on the Developer plan [1]
  - request-rate: 1 proxy server on the Developer plan [1]
- binding note: the 25 MB cache size fills well before the 10-connection limit for a single application, so storage binds first
- interface detail: the Memcached text protocol is the service interface; the pricing and signup pages checked do not publish an API reference, so the programmatic interface is documented from the product category and not from a captured protocol page
- tooling: standard Memcached clients that speak the Memcached text protocol, connecting to the single proxy
- composes with: a free MemCachier cache can sit in front of a separate free database to offload reads; the 25 MB cache and 10 connections bound any chain immediately
- reliability: the free Developer plan has one proxy server and no high availability, so the single proxy is the availability of the cache; basic analytics only
- notes: 25 MB and 10 connections make this a cache for a single small application, not a general key-value store. The interface is set to unknown because the pages captured name the product as a managed Memcached service but publish no protocol or API reference; the true interface is the Memcached text protocol and an open_question records the vocabulary gap.
- evidence note: the plan numbers and sign-up fields are from first-party pages read; no probe was run, so the rung stays documented
- evidence:
  - [1] 2026-11-19: the Developer plan is a permanent free offer, not a trial | capture: sha256:1e17949efdf46aeedbd58af0b23f8a0159d384b8858a804a3bde1a6c387dc963 | quote: Totally free forever. Try it out. See what it can do.
  - [1] 2026-11-19: the free Developer plan includes 25 MB of cache | capture: sha256:1e17949efdf46aeedbd58af0b23f8a0159d384b8858a804a3bde1a6c387dc963 | quote: 25MB
  - [1] 2026-11-19: the free Developer plan is limited to 10 connections | capture: sha256:1e17949efdf46aeedbd58af0b23f8a0159d384b8858a804a3bde1a6c387dc963 | quote: 10 Connections
  - [1] 2026-11-19: the free Developer plan runs a single proxy server | capture: sha256:1e17949efdf46aeedbd58af0b23f8a0159d384b8858a804a3bde1a6c387dc963 | quote: 1 Proxy Server
  - [2] 2026-11-19: the sign-up form asks for an email address | capture: sha256:843346b77ba081196373f2d6539cc174305933d74db1b1cc65862a8646b9dc1b | quote: Email address
  - [2] 2026-11-19: signup is guarded by a reCAPTCHA, with a password field and no card request | capture: sha256:843346b77ba081196373f2d6539cc174305933d74db1b1cc65862a8646b9dc1b | quote: protected by reCAPTCHA
- sources:
  - [1] https://www.memcachier.com/pricing
  - [2] https://www.memcachier.com/users/signup
