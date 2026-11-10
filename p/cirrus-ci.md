# Cirrus CI

> cirrus-ci.com | CI runners, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cirrus-ci/ | JSON https://fshy.ajam.dev/api/v1/entity/cirrus-ci.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cirrus CI (CI runners)

- `ci-cd-runners/cirrus-ci` | dead | evidence documented | binding per-object-cap | category CI runner
- needs card no, phone no, ID no, institution no | verified 2026-11-03T17:29:31.571Z (live) | stale on 2026-12-04
- url https://cirrus-ci.com/
- free tier: none: Cirrus CI shut down effective June 1, 2026 | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: a hard 2-hour limit on a free task; 16 CPUs on Linux and 8 CPU per task | source: [2]
- retention: credits reset monthly; task artifacts follow the repository configuration | source: [2]
- egress: no charge published | metered: no | source: [2]
- identity: email | detail: a GitHub account with the Cirrus app installed
- interface: git, cli
- limits:
  - per-object-cap (binding): 2 hours per free task [2]
  - request-rate: 50 credits a month, equal to 10,000 Linux CPU-minutes [2]
  - per-object-cap (binding): 16 CPUs on Linux; 8 CPU per task [2]
- interface detail: a .cirrus.yml pipeline; GitHub App installation is the onboarding
- tooling: Linux, Windows, macOS and FreeBSD images; any shell
- composes with: the same as the free tier
- reliability: on 2026-10-30 cirrus-ci.org did not resolve and cirrus-ci.com and api.cirrus-ci.com failed the TLS handshake, after the shutdown the vendor announced for June 1, 2026
- notes: Cirrus Labs announced on April 7th, 2026 that it is joining OpenAI and that Cirrus CI will shut down effective June 1, 2026. The free allowance for public repositories ended with the service. Cirrus Runners, a separate product of the same vendor, stopped accepting new customers in the same announcement.
- evidence note: the shutdown is stated on the vendor's own announcement page, and the unreachable hosts are measured by probe
- extras:
  - death.on: 2026-06-01
  - death.cause: dead-service
- evidence:
  - probe:https://cirrus-ci.org/faq/ 2026-10-22: NXDOMAIN from 1.1.1.1 on 2026-10-22; cirrus-ci.com resolves to 34.117.12.6 but the TLS handshake fails
  - [3] 2026-10-22: the 2026-04-19 capture states 50 compute credits a month for public repositories, equal to 10,000 CPU-minutes for Linux tasks or 500 minutes for macOS tasks which always use 4 CPUs; a hard 2-hour limit on free tasks; 16 CPUs on Linux and 8 CPU per task
  - [1] 2026-10-30: the vendor shut Cirrus CI down effective 1 June 2026 | capture: sha256:2fcf1b3d8ce8a9ca14f6b6c131587adcce7033c13e5d145d570d384b1a974542 | quote: Cirrus CI will shut down effective Monday, June 1, 2026.
  - probe:https://cirrus-ci.org/faq/ 2026-10-30: on 2026-10-30 a GET to cirrus-ci.org/faq/ failed at DNS resolution | capture: sha256:398e4c29efa03108877a48894e22115625ee3bf9fca8ae0d762caf7f677d07af | quote: "error": "dns"
  - probe:https://cirrus-ci.com/ 2026-10-30: on 2026-10-30 a GET to cirrus-ci.com failed the TLS handshake | capture: sha256:e285923d4366b70aa4d4c6e4e97686a011a0b018fd3cd9701e7d88f32f7bac3e | quote: "error": "tls_error"
  - probe:https://api.cirrus-ci.com/graphql 2026-10-30: on 2026-10-30 a GET to api.cirrus-ci.com/graphql failed the TLS handshake | capture: sha256:9112d3100095a3b6902b29ae7205389414c2a31968a7d547fb9400af2676f913 | quote: "error": "tls_error"
  - [1] 2026-10-30: the same announcement closes Cirrus Runners to new customers, a separate product of the vendor | capture: sha256:2fcf1b3d8ce8a9ca14f6b6c131587adcce7033c13e5d145d570d384b1a974542 | quote: We are no longer accepting new customers for Cirrus Runners but will continue supporting the service for existing customers through their existing contract periods.
  - [3] 2026-11-03: before the shutdown the free usage of Cirrus CI was capped at 50 compute credits a month, equal to 10,000 Linux CPU-minutes or 500 macOS minutes (archived copy of 2026-04-19) | capture: sha256:29c7912f7f4fe59f6952d41c50dd8149da93e7b6befb5302baa69e977e88874d | quote: Additionally there is an upper monthly limit on free usage equal to 50 [compute credits](https://cirrus-ci.org/pricing/) (which is equal to 10,000 CPU-minutes for Linux tasks or 500 minutes for macOS tasks which always use 4 CPUs).
  - probe:https://cirrus-ci.org/faq/ 2026-11-03: on 2026-11-03 a GET to cirrus-ci.org/faq/ failed at DNS resolution | capture: sha256:c63be63ed475be97dd24c4af74d847315ecfa0e4d1f48e704851592fad342b0f | quote: "error": "dns"
  - probe:https://cirrus-ci.com/ 2026-11-03: on 2026-11-03 a GET to cirrus-ci.com failed the TLS handshake | capture: sha256:f2892d9931cfb47cdfd1dd49e33624ff80f78265d0a5dc3010c97eea90b00fd5 | quote: "error": "tls_error"
  - [1] 2026-11-03: the vendor shut Cirrus CI down effective 1 June 2026 | capture: sha256:2fcf1b3d8ce8a9ca14f6b6c131587adcce7033c13e5d145d570d384b1a974542 | quote: Cirrus CI will shut down effective Monday, June 1, 2026.
- sources:
  - [1] https://cirruslabs.org/
  - [2] https://cirrus-ci.org/faq/
  - [3] https://web.archive.org/web/20260419203508/https://cirrus-ci.org/faq/

## cirrus ci (Storage)

- `storage/cirrus-ci` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T01:28:29.331Z (inherited) | stale on 2026-11-18
- url https://api.cirrus-ci.com/v1/task/1/artifacts
- free tier: none reachable: Could not verify: the API host failed TLS negotiation from this environment, and the docs/pricing pages returned no extractable artifact-storage terms. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Could not verify: the API host failed TLS negotiation from this environment, and the docs/pricing pages returned no extractable artifact-storage terms.
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-06-01
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Could not verify: the API host failed TLS negotiation from this environment, and the docs/pricing pages returned no extractable artifact-storage terms.
  - [2] 2026-10-21: cited as the basis of the rejection: Could not verify: the API host failed TLS negotiation from this environment, and the docs/pricing pages returned no extractable artifact-storage terms.
  - [3] 2026-11-03: the vendor shut the Cirrus CI service down effective 2026-06-01, which ends its artifact storage | capture: sha256:2fcf1b3d8ce8a9ca14f6b6c131587adcce7033c13e5d145d570d384b1a974542 | quote: Cirrus CI will shut down effective Monday, June 1, 2026.
  - [3] 2026-11-03: the vendor shut the Cirrus CI service down effective 2026-06-01 | capture: sha256:2fcf1b3d8ce8a9ca14f6b6c131587adcce7033c13e5d145d570d384b1a974542 | quote: Cirrus CI will shut down effective Monday, June 1, 2026.
- sources:
  - [1] https://api.cirrus-ci.com/v1/task/1/artifacts
  - [2] https://cirrus-ci.org/pricing
  - [3] https://cirruslabs.org/
