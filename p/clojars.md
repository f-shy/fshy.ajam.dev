# Clojars

> clojars.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clojars/ | JSON https://fshy.ajam.dev/api/v1/entity/clojars.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Clojars (repo.clojars.org)

- `storage/clojars` | fails-quota | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://clojars.org
- free tier: No published byte quota on the site pages read. A 2020 project commit records an 81 MB artifact rejected as 'too large for clojars', and a later commit adds a client-side size guard. There is a per-artifact ceiling historically around 100 MB. Treat the cap as approximately 100 MB and unverified. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: ~100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: per-object-cap: ~100 MB, from third-party evidence only (81 MB jar rejected). retention: indefinite (Maven-layout artifacts are immutable once deployed) | source: [1] | note: not stated
- egress: Free. repo.clojars.org is S3/CloudFront-backed ('Server: ... NoSuchKey' XML errors expose S3 origin) and serves without metering. | metered: no
- identity: country-phone
- interface: rest, rclone
- limits:
  - per-object-cap (binding): per-object-cap: ~100 MB [1]
- limits note: per-object-cap: ~100 MB, from third-party evidence only (81 MB jar rejected). retention: indefinite (Maven-layout artifacts are immutable once deployed). request-rate: not documented. Write path is authenticated `lein deploy` with a Clojars token.
- interface detail: rest
- tooling: `lein deploy clojars`, `clj -T:build deploy` / deps-deploy, `mvn deploy` with the clojars repo, and plain HTTPS/Maven layout GETs. No rclone backend.
- composes with: unlimited artifacts (group/artifact/version) x unlimited versions x unlimited Clojars accounts (signup with an SSH key, free). At ~100 MB/artifact that is 100 MB x N; 20 TiB would need ~200,000 artifacts. Trivially repeatable in principle, brutally inefficient.
- reliability: Read path serves real jars (verified 3,224 and 16,324 bytes on real artifacts). The cap is the story and it is poorly documented - the only hard numbers come from a 2020 project commit and forum traffic. Confirming the current number would need an authenticated deploy probe.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published byte quota on the site pages read. A 2020-era project commit records an 81 MB uberjar being rejected as 'too large for clojars', and a later commit adds a client-side 'uberjar size guard' - so there is a per-artifact ceiling in the tens-of-MB, historically around 100 MB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: probe: GET -> 200, 3,224 bytes
  - [3] 2026-10-21: probe: GET -> 200, 16,324 bytes
  - [4] 2026-10-21: 'the uberjar task produced an 81MB jar file which was too large for clojars'
  - [5] 2026-10-21: 'add uberjar size guard to deploy'
- sources:
  - [1] https://clojars.org
  - [2] https://repo.clojars.org/metosin/reitit/0.7.2/reitit-0.7.2.jar
  - [3] https://repo.clojars.org/hiccup/hiccup/1.0.5/hiccup-1.0.5.jar
  - [4] https://github.com/IntraCel/core/commit/568d4758f5994ac0aa4b7d015af7ed6caef7916b
  - [5] https://github.com/pokle/clojr/commit/7c8b2b9b755f751b2f50cbe9e1fa97d43188a8c9
