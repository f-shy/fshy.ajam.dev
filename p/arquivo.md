# Arquivo.pt

> arquivo.pt | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arquivo/ | JSON https://fshy.ajam.dev/api/v1/entity/arquivo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Arquivo.pt

- `crawler-scraper/arquivo` | qualifies-with-caveat | evidence documented | binding request-rate | category archive
- needs card no, phone no, ID no, institution no | verified 2026-10-30T11:10:03.630Z (live) | stale on 2026-11-30
- url https://arquivo.pt/
- free tier: keyless CDX server, full-text and URL search API, Memento API, image search and replay of the Portuguese web archive, each limited per IP address | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1]
- per-object cap: not applicable: the unit is a capture | source: [2]
- retention: no expiry stated | source: [2]
- egress: not applicable: the archived body | metered: no | source: [2]
- identity: anonymous | detail: keyless; the limits are counted per IP address
- interface: rest
- limits:
  - request-rate (binding): CDX server and the full-text and URL search API 250 requests a minute per IP address; Memento and image search 400 a minute; replay at /wayback 4,000 a minute [1]
  - request-rate (binding): an IP address over any of these limits is blocked permanently; a 429 answer means slow down [1]
- binding note: 250 CDX requests a minute per IP address, and a permanent block past the limit
- interface detail: CDX server answering JSON lines, the Arquivo.pt API for full-text and URL search, the Memento API, image search, replay at /wayback and /noFrame/replay, and CDXJ index files for bulk access
- tooling: plain HTTP with no key; the CDX server takes output=json and limit parameters
- composes with: Acts as a fallback archive behind the Wayback Machine. It lacks a closest operation and answers only URL listings.
- reliability: the CDX endpoint answered 200 with a capture row and no key, with x-ratelimit-policy 250;w=60
- notes: It holds fewer pages than the Wayback Machine but more of the non-English web. Exceeding the rate limit results in a permanent IP block, requiring bounded request budgets.
- evidence note: per-IP limits read on the vendor's API page; the CDX endpoint read with no key
- evidence:
  - withheld 2026-10-22: probe ok at 2026-10-22T01:40Z, 0 consecutive failures
  - [1] 2026-10-30: the CDX server allows 250 requests a minute from one IP address | capture: sha256:ad20a6a219fc6b73becdd0eea0acb0e887f92da37f673a1cce621363af1e97b4 | quote: - [CDX-server API (URL search)](https://github.com/arquivo/pwa-technologies/wiki/URL-search:-CDX-server-API): 250 requests/60s from the same IP address
  - [1] 2026-10-30: an IP address over the limits is blocked permanently | capture: sha256:ad20a6a219fc6b73becdd0eea0acb0e887f92da37f673a1cce621363af1e97b4 | quote: IP addresses that exceed these limits will be permanently blocked from using Arquivo.pt.
  - [1] 2026-10-30: CDXJ index files are offered for bulk access beside the APIs | capture: sha256:ad20a6a219fc6b73becdd0eea0acb0e887f92da37f673a1cce621363af1e97b4 | quote: - [CDXJ index files are available to support bulk access](https://sobre.arquivo.pt/en/cdxj-index-files-are-available-to-suppport-bulk-access/)
  - [3] 2026-10-30: a keyless CDX answer carries a rate limit scoped to the IP address | capture: sha256:b38ed2dbc6afd9e1390f008b9e07604126fb33bdb322a49ea8b216c09e2bf07f | quote: x-ratelimit-scope: ip
  - [3] 2026-10-30: a keyless CDX query answered 200 with one JSON line and a 250-a-minute policy header | capture: sha256:b38ed2dbc6afd9e1390f008b9e07604126fb33bdb322a49ea8b216c09e2bf07f | quote: x-ratelimit-policy: 250;w=60
  - [3] 2026-10-30: a keyless CDX query with output=json returned a JSON line with its collection | capture: sha256:b38ed2dbc6afd9e1390f008b9e07604126fb33bdb322a49ea8b216c09e2bf07f | quote: "collection": "AWP5"
  - [1] 2026-10-30: replay at /wayback allows 4,000 requests a minute from one IP address | capture: sha256:ad20a6a219fc6b73becdd0eea0acb0e887f92da37f673a1cce621363af1e97b4 | quote: - [https://arquivo.pt/wayback](https://arquivo.pt/wayback): 4000 requests/60s from the same IP address
- sources:
  - [1] https://github.com/arquivo/pwa-technologies/wiki/APIs
  - [2] https://arquivo.pt/
  - [3] https://arquivo.pt/wayback/cdx?url=example.com&output=json&limit=1
