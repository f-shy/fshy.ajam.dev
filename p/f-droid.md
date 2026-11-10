# F-Droid

> f-droid.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/f-droid/ | JSON https://fshy.ajam.dev/api/v1/entity/f-droid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## F-Droid (f-droid.org/repo APK archive)

- `storage/f-droid` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://f-droid.org
- free tier: No published total or per-app byte quota. The archive is large and browsable: index-v2.json is 66,480,070 bytes and a single APK (org.fdroid.fdroid) is 12,426,276 bytes. Builds are produced by F-Droid's own build farm from source in fdroiddata; the 24-48 h publish latency is due to human keystore signing. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: per-object-cap: none documented for the published APK; the build environment is documented in GB terms (1000 MB container, 800 MB build, 4000 MB for the large path) which caps what can be built. retention: indefinite - F-Droid keeps all published versions | source: [1] | note: not stated
- egress: Free. Mirrored via f-droid.org and third-party mirrors. No billing. | metered: no
- identity: email
- interface: rest, rclone, cli
- limits note: per-object-cap: none documented for the published APK; the build environment is documented in GB terms (1000 MB container, 800 MB build, 4000 MB for the large path) which caps what can be built. retention: indefinite - F-Droid keeps all published versions. request-rate: not documented on the docs page read.
- interface detail: rest
- tooling: `fdroid` CLI (fdroidserver), the repo is a plain signed index (index-v2.json / index-v2.jar) with APKs at /repo/<pkg>_<vc>.apk. Clients: `fdroid`, vanilla Android F-Droid client. No rclone backend.
- composes with: unlimited apps x unlimited versions (every published version stays in /repo, keyed by versionCode). Multiply by unlimited GitLab/Codeberg source repos and unlimited forks. But each app is reviewed and built by F-Droid's farm - so this is a per-app, human-gated store, not an arbitrary-blob host.
- reliability: Fully programmatic on the read side (static index + APKs, range-capable in principle), but the write side is a merge request into fdroiddata built on F-Droid's farm with human keystore signing - 24-48 h latency. Cannot store arbitrary blobs; must be an Android app build.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published total or per-app byte quota. The archive is large and browsable: index-v2.json is 66,480,070 bytes and a single APK (org.fdroid.fdroid) is 12,426,276 bytes. Builds are produced by F-Droid's own build farm from source in fdroiddata; the 24-48 h publish latency is due to human keystore signing.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: probe: GET -> 200, 66,480,070 bytes (full repo index, anonymous)
  - [3] 2026-10-21: probe: GET -> 200, 12,426,276 bytes
  - [1] 2026-10-21: build environment sizes 60/75/1000/800/4000 MB; 'around 24 to 48 hours' from merge to appearance
- sources:
  - [1] https://f-droid.org/docs/Submitting_to_F-Droid_Quick_Start_Guide/
  - [2] https://f-droid.org/repo/index-v2.json
  - [3] https://f-droid.org/repo/org.fdroid.fdroid_1023051.apk
