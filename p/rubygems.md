# RubyGems.org

> rubygems.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rubygems/ | JSON https://fshy.ajam.dev/api/v1/entity/rubygems.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RubyGems.org

- `storage/rubygems-org` | qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://rubygems.org
- free tier: No documented per-gem size limit and no documented total quota. Per-gem size is exposed per version via the API; large gems (e.g. binaries) do get 413'd in practice. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Published version strings and gem package names are permanent. | source: [1] | note: not stated
- egress: Free and unmetered, Cloudflare-fronted. Probe: GET https://rubygems.org/downloads/rails-7.0.0.gem -> 200, Server: cloudflare, Cache-Control: max-age=31536000, Access-Control-Allow-Origin: *, Accept-Ranges: bytes. | metered: no | source: [2]
- identity: institution
- interface: rest
- limits note: Rate limits allow 400 push requests per hour per IP address, with failed pushes capped at 300 per 5 minutes and 600 per 25 hours. Package deletions allow 10 yanks per 10 minutes. No published per-gem byte cap in documentation or policy terms. Version strings and gem names are permanent.
- interface detail: rest
- tooling: POST /api/v1/gems with the .gem body (gem push); GET /downloads/<name>-<ver>.gem or /gems/<name>-<ver>.gem. First-class clients (gem push, bundler). Rate-limit config is public in the repo (rack_attack.rb: PUSH_LIMIT = 400 per 60 minutes).
- composes with: 400 pushes/hour is the most generous publish rate in the entire niche. 9,600 gems/day, i.e. ~2-9 TB/day if each gem were at a hypothetical 250 MB. If the undocumented size limit is anywhere near npm's, RubyGems becomes the highest-throughput package-registry store found. Confirm the size cap before relying on it.
- reliability: The unknown size cap is the risk. The one public 413 report (qtbindings) shows a hard limit exists and is enforced at the proxy, and it is not documented anywhere, so you discover it by probing. Rate limits are the best in class and clearly documented.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'POST /api/v1/gems has following two rate limits: 400 requests/1 hour; 300 requests/5 minutes and 600 requests/25 hours on failed requests'
  - [3] 2026-10-21: full policy page contains no storage quota or per-gem size limit
  - [4] 2026-10-21: PUSH_LIMIT = 400, PUSH_LIMIT_PERIOD = 60.minutes (live source)
  - [2] 2026-10-21: probe: GET -> 200, Content-Length: 6656, Server: cloudflare, Cache-Control: max-age=31536000
  - [5] 2026-10-21: 'Can't push new qtbindings release (413 error)' (confirms an undocumented size ceiling exists)
- sources:
  - [1] https://guides.rubygems.org/rubygems-org-rate-limits/
  - [2] https://rubygems.org/downloads/rails-7.0.0.gem
  - [3] https://rubygems.org/policies/acceptable-use
  - [4] https://github.com/rubygems/rubygems.org/blob/master/config/initializers/rack_attack.rb
  - [5] https://www.mail-archive.com/rubygems-developers@rubyforge.org/msg05277.html
