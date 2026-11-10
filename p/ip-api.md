# ip-api

> ip-api.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ip-api/ | JSON https://fshy.ajam.dev/api/v1/entity/ip-api.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ip-api

- `data-apis/ip-api` | qualifies | evidence documented | binding request-rate | category IP geolocation API | tier Free endpoint
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://ip-api.com/docs/api:json
- free tier: free endpoint with no API key: 45 requests a minute per IP address on /json (15 a minute on /batch, up to 100 IPs a batch), plain HTTP only | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: HTTPS and API keys need the Pro plan, EUR 13.3 a month when paid for 12 months
- per-object cap: a batch request takes up to 100 IP addresses | source: [2]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: no account and no key on the free endpoint
- interface: rest
- limits:
  - request-rate (binding): 45 requests a minute per IP address on /json; 15 a minute on /batch [1]
  - per-object-cap: up to 100 IPs per batch request [2]
- interface detail: GET http://ip-api.com/json/{ip} (also xml, csv, line, php), POST http://ip-api.com/batch with a JSON array of up to 100 IPs; the same path over HTTPS answers HTTP 403 SSL unavailable for this endpoint
- endpoint: part of interface detail
- tooling: any HTTP client; the X-Rl and X-Ttl headers give the remaining requests and the seconds to the window reset
- composes with: 45 lookups a minute from one address with no key, or 15 batches of 100 a minute; part of the data falls back to MaxMind GeoLite2. Bulk path: the batch endpoint; no download
- reliability: past the per-minute limit the API answers HTTP 429; repeated overruns ban the IP address for up to 1 hour; no HTTPS on the free endpoint
- notes: Free requests: 45 a minute per IP on /json, 15 batches of up to 100 IPs a minute on /batch, no key. Rate limit: HTTP 429, then a ban of up to 1 hour on repeated overruns. Bulk path: the batch endpoint; no database download.
- evidence note: the JSON and batch documentation, the plans page and the terms page were quoted on 2026-10-30; a keyless HTTP lookup answered HTTP 200 and the HTTPS form answered HTTP 403 SSL unavailable. The rate limit was not exhausted to observe it.
- extras:
  - bulk_path: POST /batch with up to 100 IPs, 15 a minute
  - free_requests: 45 a minute per IP
- evidence:
  - [1] 2026-10-30: the free endpoint needs no key | capture: sha256:b153d250e79b40034deb4dbb4f66ab0d9aac099aabfbd41b5c20e7e39aaaef91 | quote: There is no API key required.
  - [1] 2026-10-30: the JSON endpoint allows 45 requests a minute per IP | capture: sha256:b153d250e79b40034deb4dbb4f66ab0d9aac099aabfbd41b5c20e7e39aaaef91 | quote: This endpoint is limited to 45 requests per minute from an IP address.
  - [1] 2026-10-30: overruns get HTTP 429 and repeated overruns a 1-hour ban | capture: sha256:b153d250e79b40034deb4dbb4f66ab0d9aac099aabfbd41b5c20e7e39aaaef91 | quote: If you go over the limit your requests will be throttled (`HTTP 429`) until your rate limit window is reset. If you constantly go over the limit your IP address will be banned for 1 hour.
  - [1] 2026-10-30: the free API has no HTTPS | capture: sha256:b153d250e79b40034deb4dbb4f66ab0d9aac099aabfbd41b5c20e7e39aaaef91 | quote: 256-bit SSL encryption is not available for this free API.
  - [2] 2026-10-30: a batch takes up to 100 IPs | capture: sha256:7d6533586c0055e2aa1c624f462eb7c1df5bb931d05128c52cc23d6b6cc22e22 | quote: A request needs to formatted as a JSON array, containing up to 100 IP addresses or objects.
  - [2] 2026-10-30: the batch endpoint allows 15 requests a minute | capture: sha256:7d6533586c0055e2aa1c624f462eb7c1df5bb931d05128c52cc23d6b6cc22e22 | quote: This endpoint is limited to 15 requests per minute from an IP address.
  - [3] 2026-10-30: the plans page repeats 45 a minute | capture: sha256:ea6ececff05ca39baae448d63f55fb3444f97416908d5ab2fd0a1bcbde913cb2 | quote: The free endpoint is limited to 45 requests / minute
  - [3] 2026-10-30: Pro is EUR 13.3 a month | capture: sha256:ea6ececff05ca39baae448d63f55fb3444f97416908d5ab2fd0a1bcbde913cb2 | quote: €13.3
  - [3] 2026-10-30: the Pro price is for yearly payment | capture: sha256:ea6ececff05ca39baae448d63f55fb3444f97416908d5ab2fd0a1bcbde913cb2 | quote: per month, when paying for 12 months
  - [4] 2026-10-30: the terms page states the block and the ban of up to 1 hour | capture: sha256:0000b0a51705858b84d62ef6b7986c2d2ebcc10207136a378b207c8fb951c16f | quote: If you exceed the usage limit of 45 requests per minute your access to the API will be temporarily blocked. Repeatedly exceeding the limit will result in your IP address being banned for up to 1 hour.
  - [4] 2026-10-30: some ranges fall back to GeoLite2 data | capture: sha256:0000b0a51705858b84d62ef6b7986c2d2ebcc10207136a378b207c8fb951c16f | quote: For some IP ranges we fallback to GeoLite2 data created by MaxMind
  - probe:http://ip-api.com/json/8.8.8.8 2026-10-30: a keyless HTTP lookup succeeded | capture: sha256:0a43ff54117e6c0a1f04c9c2398e970b131fadff75b9662a51e6bf5de09db19d | quote: "status":"success"
  - probe:https://ip-api.com/json/8.8.8.8 2026-10-30: the HTTPS form of the free endpoint is refused | capture: sha256:61fd702060224daad1fa949b448fcbebb9d3bc8628ffb942b44e8fa63dbd4c87 | quote: SSL unavailable for this endpoint
- sources:
  - [1] https://ip-api.com/docs/api:json
  - [2] https://ip-api.com/docs/api:batch
  - [3] https://members.ip-api.com/
  - [4] https://ip-api.com/docs/legal
