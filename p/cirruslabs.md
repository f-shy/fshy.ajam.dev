# Cirrus CI

> cirruslabs.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cirruslabs/ | JSON https://fshy.ajam.dev/api/v1/entity/cirruslabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cirrus CI

- `compute/cirrus-ci` | dead | evidence documented | binding request-rate | category CI runner
- needs card no, phone no, ID no, institution no | verified 2026-11-03T17:29:31.575Z (live) | stale on 2026-12-04
- url https://cirruslabs.org/
- duplicate of `ci-cd-runners/cirrus-ci`
- free tier: The allowance was real and is now gone. Quoted from the Cirrus Labs announcement dated 7 April 2026: 'Cirrus CI will shut down effective Monday, June 1, 2026.' Quoted from the docs before the shutdown: free for OSS up to 'a cap of 50 compute credits a month', equal to '10,000 CPU-minutes for Linux tasks or 500 minutes for macOS tasks which always use 4 CPUs', with per-platform concurrency of 16 CPUs Linux, 16 CPUs Arm Linux, 8 CPUs Windows, 8 CPUs FreeBSD and 4 CPUs with 1 VM on macOS, and a single task capped at 8 CPUs on Linux. Cutoff 'for a job that has a full runtime' was 2 hours per task. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: monthly-credit-cap
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): The service itself failed first: the shutdown date is 1 June 2026 and today is 2026-10-22, so the binding constraint is that the provider no longer exists and the allowance is zero, whatever the pages still cached in search indexes say. [1]
- limits note: The service itself failed first: the shutdown date is 1 June 2026 and today is 2026-10-22, so the binding constraint is that the provider no longer exists and the allowance is zero, whatever the pages still cached in search indexes say.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None. This is the row that stops the subsequent evaluation from spending a wave on it.
- reliability: on 2026-10-30 cirrus-ci.org did not resolve and cirrus-ci.com failed the TLS handshake, after the shutdown the vendor announced for June 1, 2026
- notes: Duplicate of ci-cd-runners/cirrus-ci. Cirrus CI has shut down; before then the free allowance was 50 compute credits a month, equal to 10,000 CPU-minutes for Linux tasks or 500 minutes for macOS tasks. Cirrus Runners is a separate paid product of the same vendor, recorded as compute/cirrus-runners.
- extras:
  - facets.class: ci-runner-capacity
  - facets.free_tier_kind: monthly-credit-cap
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.gpu_count: 0
  - death.on: 2026-06-01
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-22: announcement dated April 7th 2026: 'We are no longer accepting new customers for Cirrus Runners but will continue supporting the service for existing customers through their existing contract periods. Cirrus CI will shut down effective Monday, June 1, 2026.'
  - [2] 2026-10-22: 
  - [3] 2026-10-22: 'an upper monthly limit on free usage equal to 50 compute credits (which is equal to 10,000 CPU-minutes for Linux tasks or 500 minutes for macOS tasks which always use 4 CPUs)'; concurrency 16 CPUs Linux, 16 Arm, 8 Windows, 8 FreeBSD, 4 macOS 1 VM; 'a single task can't request more than 8 CPUs'
  - [4] 2026-10-22: '1000 minutes of 1 virtual CPU for Linux platform for 3 compute credits'; '2 CPU Linux task takes 5 minutes? Pay 3 cents'
  - [5] 2026-10-22: 'By default, a container is given 2 CPUs and 4 GB of memory'; 'Containers on Cirrus Cloud Cluster can use maximum 8.0 CPUs and up to 32 GB of memory', with memory tied to CPUs at 4 GB per CPU
  - [6] 2026-10-22: reported consequence: scipy's GPU runner job stopped working at the end of April 2026, and the project recorded that it had no email announcement of the timing
  - [1] 2026-10-22: 
  - [6] 2026-10-22: quoted vendor statement: 'We are no longer accepting new customers for Cirrus Runners but will continue supporting the service for existing customers'
  - [7] 2026-10-22: read 2026-10-22: the origin refused or dropped the request. This read confirms the shutdown; it is not the shutdown notice itself.
  - [1] 2026-10-30: the vendor shut Cirrus CI down effective 1 June 2026 | capture: sha256:2fcf1b3d8ce8a9ca14f6b6c131587adcce7033c13e5d145d570d384b1a974542 | quote: Cirrus CI will shut down effective Monday, June 1, 2026.
  - probe:https://cirrus-ci.org/faq/ 2026-10-30: on 2026-10-30 a GET to cirrus-ci.org/faq/ failed at DNS resolution | capture: sha256:398e4c29efa03108877a48894e22115625ee3bf9fca8ae0d762caf7f677d07af | quote: "error": "dns"
  - probe:https://cirrus-ci.com/ 2026-10-30: on 2026-10-30 a GET to cirrus-ci.com failed the TLS handshake | capture: sha256:e285923d4366b70aa4d4c6e4e97686a011a0b018fd3cd9701e7d88f32f7bac3e | quote: "error": "tls_error"
  - [8] 2026-11-03: before the shutdown the free usage of Cirrus CI was capped at 50 compute credits a month, equal to 10,000 Linux CPU-minutes or 500 macOS minutes (archived copy of 2026-04-19) | capture: sha256:29c7912f7f4fe59f6952d41c50dd8149da93e7b6befb5302baa69e977e88874d | quote: Additionally there is an upper monthly limit on free usage equal to 50 [compute credits](https://cirrus-ci.org/pricing/) (which is equal to 10,000 CPU-minutes for Linux tasks or 500 minutes for macOS tasks which always use 4 CPUs).
  - [1] 2026-11-03: the vendor shut Cirrus CI down effective 1 June 2026 | capture: sha256:2fcf1b3d8ce8a9ca14f6b6c131587adcce7033c13e5d145d570d384b1a974542 | quote: Cirrus CI will shut down effective Monday, June 1, 2026.
- sources:
  - [1] https://cirruslabs.org/
  - [2] https://cirrus-ci.org/
  - [3] https://raw.githubusercontent.com/cirruslabs/cirrus-ci-docs/master/docs/faq.md
  - [4] https://raw.githubusercontent.com/cirruslabs/cirrus-ci-docs/master/docs/pricing.md
  - [5] https://raw.githubusercontent.com/cirruslabs/cirrus-ci-docs/master/docs/guide/linux.md
  - [6] https://github.com/scipy/scipy/issues/24990
  - [7] https://cirrus-ci.org/blog/2023/07/17/limiting-free-usage-of-cirrus-ci/
  - [8] https://web.archive.org/web/20260419203508/https://cirrus-ci.org/faq/
