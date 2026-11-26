# RubyGems.org

> rubygems.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rubygems/ | JSON https://fshy.ajam.dev/api/v1/entity/rubygems.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RubyGems.org

- `storage/rubygems-org` | qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:20.739Z (live) | stale on 2026-12-10
- url https://rubygems.org
- free tier: No documented per-gem size limit and no documented total quota. Per-gem size is exposed per version via the API; large gems (e.g. binaries) do get 413'd in practice. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: The gem push route /api/v1/gems has a 500 MiB request limit.
- retention: Published version strings and gem package names are permanent. | source: [1] | note: Uploaded gems may be hosted indefinitely under the terms.
- egress: Free and unmetered, Cloudflare-fronted. Probe: GET https://rubygems.org/downloads/rails-7.0.0.gem -> 200, Server: cloudflare, Cache-Control: max-age=31536000, Access-Control-Allow-Origin: *, Accept-Ranges: bytes. | metered: no | source: [2]
- identity: institution
- interface: rest
- limits note: 400 requests/1 hour
- interface detail: rest
- tooling: POST /api/v1/gems with the .gem body (gem push); GET /downloads/<name>-<ver>.gem or /gems/<name>-<ver>.gem. First-class clients (gem push, bundler). Rate-limit config is public in the repo (rack_attack.rb: PUSH_LIMIT = 400 per 60 minutes).
- composes with: 400 pushes/hour is the most generous publish rate in the entire niche. 9,600 gems/day, i.e. ~2-9 TB/day if each gem were at a hypothetical 250 MB. If the undocumented size limit is anywhere near npm's, RubyGems becomes the highest-throughput package-registry store found. Confirm the size cap before relying on it.
- reliability: The unknown size cap is the risk. The one public 413 report (qtbindings) shows a hard limit exists and is enforced at the proxy, and it is not documented anywhere, so you discover it by probing. Rate limits are the best in class and clearly documented.
- notes: the same as the free tier
- evidence note: the rate-limits guide states a 400 requests per hour limit on gem push
- evidence:
  - [1] 2026-10-21: 'POST /api/v1/gems has following two rate limits: 400 requests/1 hour; 300 requests/5 minutes and 600 requests/25 hours on failed requests'
  - [3] 2026-10-21: full policy page contains no storage quota or per-gem size limit
  - [4] 2026-10-21: PUSH_LIMIT = 400, PUSH_LIMIT_PERIOD = 60.minutes (live source)
  - [2] 2026-10-21: probe: GET -> 200, Content-Length: 6656, Server: cloudflare, Cache-Control: max-age=31536000
  - [5] 2026-10-21: 'Can't push new qtbindings release (413 error)' (confirms an undocumented size ceiling exists)
  - [1] 2026-11-09: the rate-limits guide states a 400 requests per hour limit on gem push | capture: sha256:b438592f00e6a8bfc0f8cac6cd7dc51f69fe02de6eaf74044d042c9ced1f1637 | quote: 400 requests/1 hour
  - [6] 2026-11-25: the gem push route has a 500 MiB request limit | capture: sha256:cdc6ac5d7eecd7dca1164d5553ffdb258f9ecee802aa5ff80545ad473ca772f8 | quote: /api/v1/gems[.json|.yaml] → 500 MiB request limit
  - [7] 2026-11-25: the terms allow uploaded gems to be hosted indefinitely | capture: sha256:5958391c24272a6adbeb11c04ea613cb4d3ccedee96a4be2bb884193cf53a4b4 | quote: we may host gems that you upload indefinitely pursuant to Section 3(c) above.
  - [3] 2026-11-25: gem owners cannot delete their gems unilaterally | capture: sha256:d140062aac01bdb0af2a5c32463334939ba117202b75208c92962dfd0e321d19 | quote: In line with our goal of a reliable immutable registry, we do not permit gem owners to delete their gems unilaterally.
- sources:
  - [1] https://guides.rubygems.org/rubygems-org-rate-limits/
  - [2] https://rubygems.org/downloads/rails-7.0.0.gem
  - [3] https://rubygems.org/policies/acceptable-use
  - [4] https://github.com/rubygems/rubygems.org/blob/master/config/initializers/rack_attack.rb
  - [5] https://www.mail-archive.com/rubygems-developers@rubyforge.org/msg05277.html
  - [6] https://github.com/rubygems/rubygems.org/pull/7051
  - [7] https://rubygems.org/policies/terms-of-service
