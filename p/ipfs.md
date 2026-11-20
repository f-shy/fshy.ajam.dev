# IPFS Foundation

> ipfs.tech | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipfs/ | JSON https://fshy.ajam.dev/api/v1/entity/ipfs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPFS Foundation public gateways (ipfs.io / dweb.link / trustless-gateway.link)

- `storage/ipfs-foundation-public-gateways` | fails-egress | evidence reported | binding none | category p2p
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:03.169Z (live) | stale on 2026-12-04
- url https://docs.ipfs.tech/concepts/public-utilities/
- free tier: No storage at all. Gateway only. And the gateway itself is being retired: ipfs.io/dweb.link return HTTP 429 with 'Retry-After: 900' and 'Sunset: Mon, 21 Sep 2026', and redirect browsers to inbrowser.link. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Rate-limited to the point of unusability from a datacenter IP: 10/10 requests returned 429 on a cold burst, and a single request after a 5 s pause also returned 429. Published posture: 'Rate limiting has begun on ipfs.io and dweb.link for hotlinked and backend traffic, and will be increasing.' Docs: 'no SLA, no support, and shared rate limits that can throttle or block your traffic at any time, without notice.' | metered: no
- identity: email
- interface: rest
- limits note: 429 + Retry-After 900 observed on the first request; Range requests capped at 5 GiB (Cloudflare CDN limit); Sunset header 2026-09-21.
- interface detail: rest
- tooling: curl/any HTTP client; path gateway at ipfs.io, subdomain at dweb.link; trustless subset at trustless-gateway.link.
- composes with: none. The three hostnames are one backend: 'They are not three separate services... sharing the same cache, the same connections to the IPFS network, and the same rate limits.' Rotating hostnames burns the same budget.
- reliability: This is the single most important measurement in the slot: the 'free IPFS CDN' that every tutorial assumes is (a) gone as of 2026-09-21 and (b) already 429-ing datacenter IPs before that date. Any architecture that depends on ipfs.io/dweb.link for serving is dead on arrival.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: No storage at all — gateway only. And the gateway itself is being retired: ipfs.io/dweb.link return HTTP 429 with 'Retry-After: 900' and 'Sunset: Mon, 21 Sep 2026', and redirect browsers to inbrowser.link.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: probe: GET -> HTTP/1.1 429, Retry-After: 900, Link: rel="sunset", Sunset: Mon, 21 Sep 2026; 10/10 subsequent requests 429
  - [3] 2026-10-21: probe: GET -> 429, Retry-After: 900 (identical body, 188 bytes)
  - [4] 2026-10-21: (2026-08-25) — 'Rate limiting has begun on ipfs.io and dweb.link for hotlinked and backend traffic, and will be increasing.'
  - [1] 2026-10-21: 'these pauses keep growing until it retires for good on September 21 (UTC)'
  - [1] 2026-11-19: the public gateways retired on 21 September | capture: sha256:37c85e3683de9f77c4e941df443b0f9706e137a031e608d506c411153e4b9e7c | quote: these pauses keep growing until it retires for good on September 21 (UTC).
  - [4] 2026-11-19: the Foundation documents rate limiting on ipfs.io and dweb.link | capture: sha256:150ae99888dfabbf7e6cf9b5caa685fb598d8eac8548006c259ca5349cdf2bdf | quote: - Rate limiting has begun on ipfs.io and dweb.link for hotlinked and backend traffic, and will be increasing.
  - [5] 2026-11-19: the three gateway hostnames share one backend and one rate-limit budget | capture: sha256:4db3ac35b4d8bb0520e42b3200204df0c6b494c009db19b4eeae8f43c89d995b | quote: The three hostnames are served by the same pool of servers, sharing the same cache, the same connections to the IPFS network, and the same rate limits.
  - probe:https://ipfs.io/ipfs/bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi 2026-11-19: a live GET to the ipfs.io gateway answered HTTP 429 on 2026-11-19 | capture: sha256:85c630767ffa4e9371ea9bb779afc1b279d1025b4934b2b50cb11b66f3feaa95 | quote: "status": 429
- sources:
  - [1] https://gatewaychanges.ipfs.io/
  - [2] https://ipfs.io/ipfs/bafybei...5u4
  - [3] https://dweb.link/ipfs/bafybei...5u4
  - [4] https://blog.ipfs.tech/2026-08-beyond-sponsored-gateways/
  - [5] https://docs.ipfs.tech/concepts/public-utilities/

## Self-hosted Kubo/Rainbow gateway (own VPS)

- `storage/self-hosted-kubo-rainbow-gateway` | self-hosted, last resort | verdict fails-egress | evidence reported | binding per-ip-shaping | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.ipfs.tech/how-to/replace-public-gateways-with-self-hosted-ipfs/
- free tier: Storage and egress are whatever your VPS/host allows. No provider quota exists. The cost moves to the host's bandwidth allowance. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Host bandwidth is paid directly to the server provider. IPFS documentation recommends fronting gateways with caching CDNs using standard Cache-Control, ETag, and X-Ipfs-Roots headers to minimize origin bandwidth consumption. | metered: no
- identity: email
- interface: rest, webdav, rclone
- limits:
  - per-ip-shaping (binding): 1 TiB/day [1]
- limits note: Bandwidth of the VPS; DHT lookup latency on cold CIDs; no excess-use protection by default ('Unlike ipfs.io, a self-hosted gateway has no abuse protection by default').
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: Kubo (go-ipfs), Rainbow (github.com/ipfs/rainbow), Someguy for delegated routing, Helia in-browser; rclone can talk to the Kubo RPC API via a webdav/MFS shim but there is no first-class rclone backend.
- composes with: Does not multiply free storage. It only re-serves content you already paid to pin. Combined with a free pinning service it can turn 5 GB of free pinning into unmetered-looking reads, but only for 5 GB of content.
- reliability: This is the honest answer to 'does self-hosting change the economics?': it changes who meters you, not whether you are metered. It just moves the bill to the VPS or CDN.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Storage and egress are whatever your VPS/host allows. No provider quota exists — the cost moves to the host's bandwidth allowance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Put a CDN like Cloudflare in front of the IPFS gateway'; 'a self-hosted gateway has no abuse protection by default' (the vendor means it applies no excess-use protection)
  - [2] 2026-10-21: 'Ensure that you are correctly returning HTTP cache headers... Consider leveraging the list of CIDs in X-Ipfs-Roots'
- sources:
  - [1] https://docs.ipfs.tech/how-to/replace-public-gateways-with-self-hosted-ipfs/
  - [2] https://docs.ipfs.tech/how-to/gateway-best-practices/
