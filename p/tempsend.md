# TempSend

> tempsend.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tempsend/ | JSON https://fshy.ajam.dev/api/v1/entity/tempsend.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TempSend

- `debrid/tempsend` | qualifies-with-caveat | evidence documented | binding per-object-cap | category temporary file host (anonymous, curl-friendly) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://tempsend.com/
- free tier: Free, no signup and no API key; files up to 500 MB, expiring after a chosen 1 second to 7 days. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 500 MB per file | source: [1]
- retention: chosen expiry from 1 second to 7 days; 604800 seconds maximum | days: 7 | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: No signup, no JavaScript and no API key are needed; the site states it is funded by its administrator.
- interface: rest, cli
- limits:
  - per-object-cap (binding): 500 MB per file [1]
  - retention-clamped: expiry from 1 second to 7 days [1]
- binding note: A 500 MB ceiling and a 7-day maximum clock make this a hand-off drop and not storage.
- interface detail: POST /send with a multipart form (file and expire in seconds); the response is a 302 with the share URL in Location.
- tooling: curl or any HTTP client; the same form the home page uses.
- composes with: The anonymous upload is a single curl POST; the share link can also delete the file.
- reliability: Anyone with the share link can delete the file from its download page.
- notes: The vendor llms.txt states 500 MB per file; an aggregator list shows 2 GB, which the vendor pages do not state.
- evidence note: Cap and expiry read on the vendor llms.txt page.
- evidence:
  - [1] 2026-11-03: the per-file cap is 500 MB | capture: sha256:0387cb574b4da0b485010162f9e5244aa8181013f89adaa1c84257fdf579e6a7 | quote: Max file size: 500 MB
  - [1] 2026-11-03: expiry is 1 second to 7 days | capture: sha256:0387cb574b4da0b485010162f9e5244aa8181013f89adaa1c84257fdf579e6a7 | quote: Expiration: 1 second to 7 days
  - [1] 2026-11-03: no account or key is needed | capture: sha256:0387cb574b4da0b485010162f9e5244aa8181013f89adaa1c84257fdf579e6a7 | quote: There is no signup, no JavaScript requirement, and no API key.
  - [2] 2026-11-03: free with no registration | capture: sha256:aea81ed6fd5cc17eeab28f38d04bd9a3f32b3ca3d7283187c5ebe23066051c00 | quote: No ads. No sign up or registration required. Funded by the site administrator as a public service.
- sources:
  - [1] https://www.tempsend.com/llms.txt
  - [2] https://tempsend.com/
