# Surge.sh

> surge.sh | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/surge/ | JSON https://fshy.ajam.dev/api/v1/entity/surge.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Surge.sh

- `storage/surge-sh` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:33.171Z (live) | stale on 2026-11-25
- url https://surge.sh
- free tier: Unlimited projects and domains, with publishing under rate limits that apply to every plan | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Projects are limited to 10,100 files and 450 MB; a larger project is refused before anything is published. | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No bandwidth quota or metering is documented anywhere on the free plan; every project is served from all 10 of Surge's own edge nodes ('Every project. Free or paid. Serves from all of them'). | metered: no
- identity: anonymous
- interface: rest, cli
- limits:
  - per-ip-shaping: 240 per 15 minutes per IP address [1]
  - write-gated: Application too large') [1]
  - per-object-cap (binding): no per-file cap documented but it inherits the project cap [1]
- limits note: 450 MB and 10,100 files per project (hard: 'Aborted - Unable to publish. Application too large'); no bandwidth figure published; no per-file cap documented but it inherits the project cap. Re-publishing replaces the whole project (full-sync deploy), so appending one file re-uploads the directory.
- interface detail: rest
- tooling: Official `surge` CLI (npm, ~free) and a documented raw REST deploy API: PUT /:domain with Basic auth, Content-Type: application/gzip, a gzipped tarball body plus file-count and project-size headers. That is directly scriptable, no CLI needed.
- composes with: Allows unlimited projects per account with each project capped at 450 MB. Free accounts register via command-line without payment credentials. Sharding divides data across independent project directories.
- reliability: Deploy is full-replace, not incremental. A slow link makes each publish expensive. Free tier has no stated SLA and no published bandwidth ceiling, so behaviour at 1 TiB/day is unproven.
- notes: Free plan: unlimited projects and unlimited publishes; each project capped at 450 MB and 10,100 files. No account-level byte quota.
- evidence:
  - [1] 2026-10-21: 'Projects are limited to 10,100 files and 450 MB.'
  - [2] 2026-10-21: 'The core of Surge costs nothing, without trial windows or project caps: Unlimited projects and publishes'
  - [3] 2026-10-21: 'PUT /:domain ... The body is a gzipped tar archive ... file-count / project-size headers'
  - [4] 2026-10-21: probe: curl -D - -> HTTP/1.1 200, Server: cloudflare, Accept-Ranges: bytes (edge is CF-fronted)
  - [2] 2026-11-09: the plans page states unlimited projects and domains on the free plan, with publishing rate limits on every plan | capture: sha256:b00cde60d35e90b5760286b523f35f3f316ee3755a640945512f56b5e881c0c9 | quote: Unlimited projects and domains, with publishing under rate limits that apply to every plan
  - [1] 2026-11-09: the publishing page states the 10,100-file and 450 MB project limit and that a larger project is refused before publishing | capture: sha256:260e6c40050150810b3d753c280d8a404b66e287bf1de9a8f0a24b43dfd2dfca | quote: Projects are limited to 10,100 files and 450 MB; a larger project is refused before anything is published.
  - [1] 2026-11-09: the rate-limit table gives 240 requests per 15 minutes per IP address | capture: sha256:260e6c40050150810b3d753c280d8a404b66e287bf1de9a8f0a24b43dfd2dfca | quote: | Limit | Per 15 minutes | Per 24 hours | |-------|----------------|--------------| | Each domain | 30 | 200 | | Each account | 60 | 500 | | Each IP address | 240 | — |
- sources:
  - [1] https://surge.sh/docs/cli/publishing
  - [2] https://surge.sh/docs/platform/plans
  - [3] https://surge.sh/docs/api/deploys
  - [4] https://surge.sh/

## surge.sh as a bulk archive (naive)

- `storage/surge-sh-as-a-bulk-archive` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:28.470Z (live) | stale on 2026-12-04
- url https://surge.sh/docs/cli/publishing
- free tier: none reachable: 450 MB / 10,100 files per project; 'Only changed files travel. For projects over 1 MB, files the domain's live revision already has are carried over rather than uploaded again, so republishing a large project with a small change is quick.' | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: 450 MB / 10,100 files per project; publishes carry only changed files, with files a live revision already has carried over rather than re-uploaded.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 450 MB / 10,100 files per project and every publish is a full gzipped-tarball replace, so a 450 MB project costs 450 MB of upload per change. Only viable if projects are written once and…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 450 MB / 10,100 files per project and every publish is a full gzipped-tarball replace, so a 450 MB project costs 450 MB of upload per change. Only viable if projects are written once and…
  - [2] 2026-10-21: cited as the basis of the rejection: 450 MB / 10,100 files per project and every publish is a full gzipped-tarball replace, so a 450 MB project costs 450 MB of upload per change. Only viable if projects are written once and sha
  - [1] 2026-11-19: the 450 MB / 10,100 file per-project limit is still stated | capture: sha256:260e6c40050150810b3d753c280d8a404b66e287bf1de9a8f0a24b43dfd2dfca | quote: Projects are limited to 10,100 files and 450 MB; a larger project is refused before anything is published.
  - [1] 2026-11-19: only changed files are uploaded and existing files are carried over, contradicting the full-tarball-replace claim | capture: sha256:260e6c40050150810b3d753c280d8a404b66e287bf1de9a8f0a24b43dfd2dfca | quote: Only changed files travel. For projects over 1 MB, files the domain's live revision already has are carried over rather than uploaded again, so republishing a large project with a small change is quick.
  - [1] 2026-11-19: republishes do not re-upload every file of a large project | capture: sha256:260e6c40050150810b3d753c280d8a404b66e287bf1de9a8f0a24b43dfd2dfca | quote: Only changed files travel. For projects over 1 MB, files the domain's live revision already has are carried over rather than uploaded again, so republishing a large project with a small change is quick.
- sources:
  - [1] https://surge.sh/docs/cli/publishing
  - [2] https://surge.sh/docs/api/deploys
