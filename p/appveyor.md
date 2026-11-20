# appveyor artifacts

> appveyor.com | CI runners, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/appveyor/ | JSON https://fshy.ajam.dev/api/v1/entity/appveyor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AppVeyor

- `ci-cd-runners/appveyor` | qualifies-with-caveat | evidence documented | binding per-object-cap | category CI runner
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:00:42.533Z (live) | stale on 2026-12-05
- url https://www.appveyor.com/pricing/
- free tier: an Open-source plan at USD 0 listing 'Unlimited public projects', 1 concurrent job and 5 self-hosted jobs, with a 60-minute maximum build; the page states no monthly minute allowance for that plan, and does not use the word unlimited for builds or minutes | unit: objects | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: 60 minutes per build on the free plan; one concurrent job | source: [1]
- retention: build artifacts and history are retained per project settings | source: [1]
- egress: no egress charge published | metered: no | source: [1]
- identity: email | detail: email or GitHub OAuth
- interface: git, cli
- limits:
  - per-object-cap (binding): 60 minutes per build; one concurrent job on Free [1]
- interface detail: an appveyor.yml or the web UI; a REST API
- tooling: Windows and Linux images; MSBuild, Visual Studio, and the usual package managers
- composes with: the cheapest way to get a real Windows build, which no other free tier here offers at this cap
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: Sixty minutes and one job at a time is a build system for a small project. It is not general compute, and the concurrency of one is the number that ends that idea.
- evidence note: the pricing page was read on 2026-10-22. The page's unlimited claim is about the number of public projects, not about the number of builds, which the page does not state.
- evidence:
  - [1] 2026-10-22: public open-source projects build without a minute cap, with one concurrent job and a 60-minute maximum build
  - [1] 2026-11-04: the Open-source plan lists unlimited public projects; the page names no minute allowance | capture: sha256:92b3fc44cde9f11429500f0678c8211db9725f57164237f4f1a1dba0a0ac1d3c | quote: <strong>Unlimited</strong> public projects
  - [1] 2026-11-04: the Open-source plan runs 1 concurrent job | capture: sha256:92b3fc44cde9f11429500f0678c8211db9725f57164237f4f1a1dba0a0ac1d3c | quote: <strong>1</strong> concurrent job
  - [1] 2026-11-04: every plan caps a build job at 60 minutes | capture: sha256:2697e53f1fcee2f3591a1e60fbb56d82d22cf449376de2ada38313790b34ffe8 | quote: All plans have maximum build job execution time of 60 minutes.
  - probe:https://www.appveyor.com/pricing/ 2026-11-04: the pricing page answered HTTP 200 on 2026-11-04 | capture: sha256:39468c67198cc56a29a7fc8a00090a1a132291e763ccd19012bf02bef84dc33e | quote: "status": 200
- sources:
  - [1] https://www.appveyor.com/pricing/

## appveyor artifacts

- `storage/appveyor-artifacts` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:55.370Z (live) | stale on 2026-12-04
- url https://www.appveyor.com/pricing/
- free tier: None reachable: 14-day free trial only, no perpetual free tier. Artifacts are stored in 'AppVeyor cloud storage' but fetching them by URL requires authentication. No anonymous public artifacts. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the pricing page states no per-object size cap for build artifacts | source: [1] | note: not applicable
- retention: stated-absent: the pricing page states a 60-minute maximum build job execution time but no artifact retention period | source: [1]
- egress: stated-absent: the pricing page states no byte egress allowance; it describes a 14-day trial with no card required at signup | metered: no
- identity: email | detail: email: no credit card is required to sign up for the 14-day trial
- interface: unknown
- interface detail: stated-absent: the pricing page names build artifacts fetched by URL but gives no storage client interface token; artifacts require authentication to fetch
- tooling: not documented
- composes with: stated-absent: the pricing page states no way to chain build artifacts into a general store; artifacts are consumed inside CI and fetching them by URL requires authentication
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 14-day free trial only, no perpetual free tier. Artifacts are stored in 'AppVeyor cloud storage' but fetching them by URL requires authentication — no anonymous public artifacts.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 14-day free trial only, no perpetual free tier. Artifacts are stored in 'AppVeyor cloud storage' but fetching them by URL requires authentication — no anonymous public artifacts.
  - [2] 2026-10-21: cited as the basis of the rejection: 14-day free trial only, no perpetual free tier. Artifacts are stored in 'AppVeyor cloud storage' but fetching them by URL requires authentication — no anonymous public artifacts.
  - [3] 2026-10-21: cited as the basis of the rejection: 14-day free trial only, no perpetual free tier. Artifacts are stored in 'AppVeyor cloud storage' but fetching them by URL requires authentication — no anonymous public artifacts.
  - [1] 2026-11-19: the first-party pricing page still offers only a 14-day trial, not a perpetual free tier | capture: sha256:d84bdd4a58eec48ebc2632ba921a869b3b2d564454b8478b92b9162015bbfe92 | quote: 14-day free trial
  - [2] 2026-11-19: the first-party docs confirm fetching artifacts by URL still requires authentication | capture: sha256:7ad755eab6bd78969a2ab77c934063be98ffab92476a0dc3b7035c72f9fcc934 | quote: Artifacts may be fetched by URL, bear in mind authentication is required
  - [1] 2026-11-19: the signup gate does not ask for a card | capture: sha256:d84bdd4a58eec48ebc2632ba921a869b3b2d564454b8478b92b9162015bbfe92 | quote: No credit card required to sign up
  - [1] 2026-11-19: the pricing page describes a 14-day trial with no card and names no storage client interface | capture: sha256:f09c2717f97163c0832f219ceeccd021b1a48ec54c3f40414de27d804fe2f234 | quote: You can use the service for free during the 14 day trial. No credit card required to sign up. Cancel at any time.
  - [1] 2026-11-19: the 60-minute figure is a build-time limit, not a byte-retention term | capture: sha256:f09c2717f97163c0832f219ceeccd021b1a48ec54c3f40414de27d804fe2f234 | quote: All plans have maximum build job execution time of 60 minutes.
  - [1] 2026-11-19: artifacts belong to CI builds and the page states no byte-storage chaining | capture: sha256:f09c2717f97163c0832f219ceeccd021b1a48ec54c3f40414de27d804fe2f234 | quote: Every push to the repository starts a new build with a single or multiple jobs.
  - [1] 2026-11-19: the signup gate does not ask for a card; no phone or ID requirement is stated | capture: sha256:f09c2717f97163c0832f219ceeccd021b1a48ec54c3f40414de27d804fe2f234 | quote: No credit card required to sign up.
- sources:
  - [1] https://www.appveyor.com/pricing/
  - [2] https://www.appveyor.com/docs/packaging-artifacts/
  - [3] https://ci.appveyor.com/api/projects/appveyor/ci/artifacts
