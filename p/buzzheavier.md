# buzzheavier paid

> buzzheavier.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/buzzheavier/ | JSON https://fshy.ajam.dev/api/v1/entity/buzzheavier.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Buzzheavier

- `storage/buzzheavier` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://buzzheavier.com
- free tier: Storage explicitly unlimited ('Upload whatever size you want'); no per-file cap; no bandwidth cap. Free files start with an 8-day life, +2 days per download up to 60d, and become permanent at 30+ downloads every 60 days (live pricing page, 2026-08-24 capture; the 2026-10 live page is 404 to non-browser fetchers). | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: no per-file cap | source: [1] | note: not stated
- retention: Free files start with an 8-day life, +2 days per download up to 60d, and become permanent at 30+ downloads every 60 days (live pricing page, 2026-08-24 capture; the 2026-10 live page is 404 to non-browser fetchers) | days: 8 | source: [1] | note: not stated
- egress: Unmetered. Help page: 'Bandwidth Limits? None. Go wild.' Downloads are served through Cloudflare with a Turnstile/hx gate but no transfer meter. Hotlinking historically allowed per 2024 FAQ. | metered: no
- identity: card
- interface: rest, cli
- limits:
  - per-object-cap (binding): no per-file cap [1]
- limits note: No per-file cap (docs: 'name max 500 chars' is the only field limit). Upload rate: 2 req/s and 10 concurrent uploads per IP observed on FileDitch-class peers; Buzzheavier returned no rate headers in probes. Download path is Cloudflare-Turnstile gated: a plain curl GET of a file page returns 403 'Just a moment', and /{id}/download?t=... returns HTTP 204 + 'Hx-Redirect' back to the file page unless the browser completes the human-verification step. Retention: 8d base / +2d per download / 60d cap / permanent at 30 downloads per 60 days; older policy was 15d/+3d/45d/15 downloads.
- interface detail: rest
- tooling: PUT upload to https://w.buzzheavier.com/{name} (anonymous) or /{parentId}/{name} with 'Authorization: Bearer <ACCOUNT_ID>'. Bash CLI github.com/Ognisty321/buzzheavier-cli; uploader modules in anasty17/mirror-leech-telegram-bot (PR #1938/#1939) and SilentDemonSD/WZML-X (PR #418); download resolver in towerwatchman/Atlas electron/downloads/hosts/buzzheavier.js.
- composes with: Anonymous PUT needs no account at all, so the ceiling is not per-account: it is 'as many files as you can push'. Account IDs are free, non-recoverable, email-less, and unlimited. The 45-day inactivity expiry resets when the same client re-downloads its own file (>10% or the download endpoint), and the same bytes may sit under 2-3 identifiers. Docs also expose ?expiry= and ?burner= for self-expiring uploads.
- reliability: Storage costs adjusted to approximately EUR 5-6 per TB per month after upstream provider changes. Free-tier retention shortened to 8 days base lifetime. Downloads enforce Cloudflare challenges requiring browser headers or htmx interaction.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Paid accounts: Permanent storage EUR 18 / TB / Month'
  - [2] 2026-10-21: 'Buzzheavier was running on borrowed time using storage exploits. Yeah, we managed to get storage costs down to about $1/TB/month... after the recent police raid, our provider caught on. Game over.' followed by 'we're now paying actual market rates - around 5-6 euros per terabyte per month'. The quoted words mean the operator obtained storage below market cost, and the upstream host was seized
  - [3] 2026-10-21: 'File Size Limit? Upload whatever size you want.' / 'Bandwidth Limits? None. Go wild.'
  - [4] 2026-10-21: probe: PUT -> 201 Created, {"id":"g8zb77txsh79","locationId":"5urmb0o0baxx","size":34,"expiry":"2026-10-25T16:05:50Z","sha256":...,"md5":...} — anonymous upload works with zero auth
  - [5] 2026-10-21: probe: GET ... -> 204 No Content + Hx-Redirect (challenge), and GET of the file page without a browser -> 403 cf-mitigated:challenge
  - [6] 2026-10-21: probe: GET -> 200 {"data":[{"id":"g65gmc5rfv2c","name":"Asia-Pacific"},{"id":"m8sx6tb1ngx0","name":"Western Europe"},{"id":"5urmb0o0baxx","name":"Eastern Europe"},{"id":"3eb9t1559lkv","name":"Central Europe"},{"id":"12brteedoy0f","name":"Eastern US"},{"id":"95542dt0et21","name":"Western US"}]}
- sources:
  - [1] https://buzzheavier.com/pricing
  - [2] https://buzzheavier.com/blog/fresh_start
  - [3] https://buzzheavier.com/help
  - [4] https://w.buzzheavier.com/e2probe.txt
  - [5] https://buzzheavier.com/g8zb77txsh79/download?t=
  - [6] https://buzzheavier.com/api/locations

## buzzheavier paid tier

- `storage/buzzheavier-paid-tier` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://buzzheavier.com/upgrade
- free tier: none reachable: Endpoint buzzheavier.com/upgrade returned HTTP 404 on 2026-10-21. Published post-mortem 'The Real Cost of Storage: A Fresh Start' documents discontinuation of the paid tier. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Cannot be checked at all: buzzheavier.com/upgrade returns 404.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cannot be checked at all: buzzheavier.com/upgrade returns 404.
- sources:
  - [1] https://buzzheavier.com/upgrade
