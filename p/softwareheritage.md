# Software Heritage

> softwareheritage.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/softwareheritage/ | JSON https://fshy.ajam.dev/api/v1/entity/softwareheritage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Software Heritage Archive (CAPI read side) + Save Code Now (anonymous crawl trigger)

- `storage/software-heritage-archive-save-code-now` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://archive.softwareheritage.org
- free tier: No storage quota is imposed on the depositor, because the depositor never uploads bytes. The archive stores content-addressed git objects from public repositories, deduplicated by sha1_git, and growth is the Foundation's problem, not yours. Live scale reference: the `torvalds/linux` origin is at visit 500 ('visit':500, date 2026-10-18). Deposit (push) is separate and capped: swh-deposit docs say 'upload limitation of 100Mib', and the source default in swh/deposit/config.py is "max_upload_size": 209715200 (200 MiB). | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap (deposit only): 100 MiB | bytes: 104857600 | source: [1] | note: not stated
- retention: list-rate-limited, and this is the binding constraint on reading a large tree (walking a repo = 1 call per directory). retention: permanent and intrinsic - this is a preservation archive, deletion is not part of the model; `visit_status: full` snapshots are retained per visit | source: [1] | note: not stated
- egress: Free and unmetered - no pricing page, no billing, a public research archive. Downloads are direct `GET .../raw/` byte streams from Varnish. Note there is no CDN requirement to satisfy: nothing to pay. | metered: no
- identity: institution
- interface: rest, git, rclone
- limits:
  - per-object-cap (binding): per-object-cap (deposit only): 100 MiB [1]
- limits note: per-object-cap (deposit only): 100 MiB documented, 200 MiB default in swh-deposit config. request-rate: SWH CAPI sends `X-Ratelimit-Limit: 120` / `X-Ratelimit-Remaining` / `X-Ratelimit-Reset` (observed 114->118 remaining across calls) - 120 requests per window per IP, i.e. list-rate-limited, and this is the binding constraint on reading a large tree (walking a repo = 1 call per directory). retention: permanent and intrinsic - this is a preservation archive, deletion is not part of the model; `visit_status: full` snapshots are retained per visit. Write access: /api/1/origin/save/ is open anonymously; deposit.softwareheritage.org returns 401 to anonymous PUT/POST.
- interface detail: rest
- tooling: Official Web API v1 (documented route index at https://archive.softwareheritage.org/api/1/); Python `swh.model`/`swh.web.client`; no rclone backend. Read paths: /api/1/origin/<url>/get/, /api/1/origin/<url>/visit/latest/, /api/1/snapshot/<id>/, /api/1/revision/<id>/, /api/1/directory/<id>/, /api/1/content/sha1_git:<h>/raw/.
- composes with: This is the strongest chaining object in the niche and it is NOT a place to upload - it is a place to make arbitrary public git content addressable and permanent. The mechanism: POST /api/1/origin/save/git/url/<URL>/ anonymously, with no account and no key, and it returns {"save_task_status":"pending","loading_task_id":422136312}. So: unlimited free git hosts (one repo each, any size) -> anonymous SWH crawl request per URL -> content permanently in SWH under a sha1_git you can fetch forever. The upload-to-SWH step costs zero bytes of your quota; the bytes live in the free git host and SWH becomes the durability + retrieval layer. Multiply by unlimited origins. Combine with round-1's GitHub Releases finding: the archive is a free permanence layer over storage you already have.
- reliability: Read path is reliable but rate-shaped: 120 req/window/IP will throttle a naive tree walk of a 20 TiB corpus - parallelise across IPs or batch directory listings. docs.softwareheritage.org sits behind Anubis PoW (proof-of-work bot wall) and returns a challenge page with upstream_status 200, so doc numbers must be taken from the GitHub source, not the docs site. Anonymous save requests are queued ('pending'), not instant - ingestion lag is hours to days.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
- evidence:
  - [2] 2026-10-21: probe: GET -> 200, {"visit":500,"date":"2026-10-18...","snapshot":"221b3be5a85f08858a1410e5987f88e77603adb1","status":"full","type":"git"}
  - withheld 2026-10-21: probe: GET /api/1/snapshot/221b3be5.../ -> 200, branches include HEAD + refs/heads/master + refs/pull/10/head (full graph, anonymous)
  - withheld 2026-10-21: probe: GET /api/1/content/sha1_git:010c587224224ba1254657b42b091a6c62c39e92/raw/ -> 200, Content-Length 6034, body begins 'Linux kernel\n============' - real original bytes, not a re-encode
  - [3] 2026-10-21: probe: POST /api/1/origin/save/git/url/ -> 200 {"id":2567968,"save_request_status":"accepted","save_task_status":"pending"} - anonymous, no credential
  - withheld 2026-10-21: probe: headers on /api/1/origin/.../get/ -> X-Ratelimit-Limit: 120, X-Ratelimit-Remaining: 114
  - [4] 2026-10-21: probe: POST (anon multipart) -> 401 (write gated)
- sources:
  - [1] https://docs.softwareheritage.org/user/deposit/references/limits.html
  - [2] https://archive.softwareheritage.org/api/1/origin/https://github.com/torvalds/linux/visit/latest/
  - [3] https://github.com/josephmisiti/awesome-machine-learning/
  - [4] https://deposit.softwareheritage.org/1/softwareheritage/

## software heritage deposit (swh-deposit, the push api)

- `storage/software-heritage-deposit` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://deposit.softwareheritage.org/1/softwareheritage/
- free tier: none reachable: Upload capped at 100 MiB documented / 200 MiB default in config, and requires HTTP Basic auth - anonymous POST to deposit.softwareheritage.org/1/<collection>/ returns 401. Only useful for… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Upload capped at 100 MiB documented / 200 MiB default in config, and requires HTTP Basic auth - anonymous POST to deposit.softwareheritage.org/1/<collection>/ returns 401. Only useful for…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Upload capped at 100 MiB documented / 200 MiB default in config, and requires HTTP Basic auth - anonymous POST to deposit.softwareheritage.org/1/<collection>/ returns 401. Only useful for…
  - [2] 2026-10-21: cited as the basis of the rejection: Upload capped at 100 MiB documented / 200 MiB default in config, and requires HTTP Basic auth - anonymous POST to deposit.softwareheritage.org/1/<collection>/ returns 401. Only useful for so
- sources:
  - [1] https://deposit.softwareheritage.org/1/softwareheritage/
  - [2] https://raw.githubusercontent.com/softwareheritage/swh-deposit/master/docs/api/api-documentation.rst
