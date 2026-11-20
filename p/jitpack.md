# JitPack

> jitpack.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jitpack/ | JSON https://fshy.ajam.dev/api/v1/entity/jitpack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JitPack (jitpack.io) - build-on-demand Maven from git

- `storage/jitpack-build-on-demand-maven-from-git` | fails-quota | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:06.407Z (live) | stale on 2026-12-04
- url https://jitpack.io
- free tier: Bounded by the size of the git repo it builds from, not by a storage quota: a build fails with 'Git error. Max repo size 250MB exceeded'. JitPack builds any public git repo on demand and serves the resulting Maven artifacts at com.github.<user>.<repo>:<tag>. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 250 MB | bytes: 250000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Artifacts served from jitpack.io CDN with no billing. | metered: no
- identity: institution
- interface: rest, rclone, cli
- limits:
  - per-object-cap (binding): per-object-cap: 250 MB [1]
- limits note: per-object-cap: 250 MB repo size (hard build error). request-rate: builds are queued per-IP (anonymous builds are rate limited; the API exposes per-tag build state). retention: build artifacts are cached but a failing/expired build is rebuilt on demand - not durable storage.
- interface detail: rest
- tooling: Any Maven/Gradle resolver pointed at https://jitpack.io; JitPack build API at /api/builds/<group>/<artifact> (open, returns build status per tag). No dedicated CLI beyond Maven/Gradle; no rclone backend.
- composes with: unlimited public git repos x unlimited tags/commits x 250 MB repo each. Because artifacts are derived, storage is the repo's, and the same content is rebuilt per tag - so it amplifies, it does not multiply storage. 250 MB x N repos is the honest ceiling.
- reliability: Build service, not storage: artifacts can be evicted and rebuilt, and repo size is hard-capped at 250 MB. Read path live and public (verified /api/builds/com.github.jitpack/maven-simple returning ok states across dozens of tags).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Bounded by the size of the git repo it builds from, not by a storage quota: a build fails with 'Git error. Max repo size 250MB exceeded'. JitPack builds any public git repo on demand and serves the resulting Maven artifacts at com.github.<user>.<repo>:<tag>.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Build issue Max repo size 250MB exceeded'; 'Git error. Max repo size 250MB exceeded'
  - [2] 2026-10-21: probe: GET -> 200 JSON, dozens of tag/commit entries with status 'ok'
  - [3] 2026-10-21: build-on-demand model
  - [1] 2026-11-19: the 250 MB per-repository build cap still applies | capture: sha256:ddab6136f6ac33b238291136d879bc007bfd66196a8b5321ba337652138f2760 | quote: Git error. Max repo size 250MB exceeded
  - [3] 2026-11-19: JitPack publishes from a git repository build file on demand | capture: sha256:c2c7b51814a66691845a22f0fd015e5d028bf9f9ab1d520afd1f7063d7a6e8f4 | quote: In order to publish your library on JitPack you just need a working build file in your Git repository.
- sources:
  - [1] https://github.com/jitpack/jitpack.io/issues/4898
  - [2] https://jitpack.io/api/builds/com.github.jitpack/maven-simple
  - [3] https://docs.jitpack.io/building/
