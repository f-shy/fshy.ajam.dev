# Docker Cloud

> docker.com | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/docker/ | JSON https://fshy.ajam.dev/api/v1/entity/docker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Docker Hub (free Personal plan, public repositories)

- `storage/docker-hub` | qualifies | evidence documented | binding per-ip-shaping | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:14.094Z (live) | stale on 2026-12-11
- url https://hub.docker.com
- free tier: Personal (authenticated): 200, Unlimited, Up to 1 | unit: mixed | metered on: stored-bytes | read on: 2026-11-09 | source: [1] | note: The table columns are pull rate limit per 6 hours, number of public repositories and number of private repositories.
- per-object cap: source: [1] | note: not stated
- retention: Pull count 100 per 6 hours anonymous or 200 per 6 hours authenticated per IP. Large download throughput requires few, large blobs rather than many small ones. | source: [1] | note: not stated
- egress: Free and unmetered per-GB; the gate is a pull COUNT, not bytes: 'Unauthenticated users: 100 per IPv4 address or IPv6 /64 subnet' and 'Personal (authenticated): 200' per 6 hours. Blobs are served by 307 redirect to a CDN, so one pull can be a multi-GB blob. | metered: no
- identity: anonymous
- interface: oci
- limits:
  - per-ip-shaping (binding): 200 pulls per 6 hours for Docker Personal users [1]
- limits note: Pull count is 100 per 6 hours anonymous or 200 per 6 hours authenticated per IP. No published per-layer size cap, but Docker distribution S3 drivers historically faced issues above 10 GB per layer, recommending shards around 5 GB. Excess request limits return HTTP 429.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: oci
- tooling: oras push / docker push; purpose-built wrapper: github.com/Androsh7/layerstash (chunks >5GB files into ~5GB layers, uploads to Docker Hub or GHCR; author reports 1.8TB personally stored), github.com/xausky/DockerRegisterCloud (654 stars, registry-as-netdisk client with Flutter GUI + direct-download server).
- composes with: Unlimited public repos per account, and the free account count itself is unlimited. Layer count per repo is not capped, so a single repo holds arbitrarily many blobs; layerstash's <base-tag>-<chunk_n> scheme makes one repo a striped volume of unlimited size.
- reliability: Storage is unpriced today but Docker reserves the right to add charges and has flip-flopped before (announced Mar 2025, cancelled Apr 2025); the 100-pull/6h IP limit will throttle any fetch fan-out from one host.
- notes: Storage Charges Delayed Indefinitely – Previously, we announced plans to introduce storage-based billing, but we have decided to indefinitely delay any storage charges.
- evidence note: the usage table states the Personal plan's figures
- evidence:
  - [1] 2026-10-21: read live: table has columns Pull rate limit / public repos / private repos only; Personal = Unlimited public repos, 200 pulls/6h; no storage row anywhere on the page
  - [2] 2026-10-21: read live: 'Storage Charges Delayed Indefinitely ... we have decided to indefinitely delay any storage charges', and 'We did not enforce the Docker Hub rate limit changes previously scheduled for April 1, 2025'
  - [3] 2026-10-21: probe: GET -> 200 (2698-char token); then GET registry-1.docker.io/v2/library/alpine/manifests/latest -> 200, 9218 bytes, anonymous, no account
  - [4] 2026-10-21: probe: POST -> 401 (anonymous push correctly refused; write requires an account, read does not)
  - [5] 2026-10-21: read live: 'I have stored a total of 1.8TB in a public repository on Docker Hub androsh7/archive'
  - [1] 2026-11-09: the usage table row for Personal (authenticated) gives 200, Unlimited and Up to 1 | capture: sha256:6fdd0586d1c96313389d7b53a1a39b24939f9ad8ecd97de52e5e5e244ad954ed | quote: | Personal (authenticated) | 200 | Unlimited | Up to 1 |
  - [1] 2026-11-09: the usage table columns are pull rate limit per 6 hours, number of public repositories and number of private repositories | capture: sha256:6fdd0586d1c96313389d7b53a1a39b24939f9ad8ecd97de52e5e5e244ad954ed | quote: | User type | Pull rate limit per 6 hours | Number of public repositories | Number of private repositories |
  - [2] 2026-11-09: the blog states the current pull limits are 100 per 6 hours unauthenticated and 200 per 6 hours for Docker Personal users | capture: sha256:b3651536b191c8dd81315ce7f3704d9dbae3ba94635928cb2d4df062d6e9ab01 | quote: The current limits—100 pulls per 6 hours for unauthenticated users and 200 pulls per 6 hours for Docker Personal users—will remain in place as we continue to evaluate developer feedback and identify appropriate long-term limits.
  - [2] 2026-11-09: the blog states storage-based billing is indefinitely delayed | capture: sha256:b3651536b191c8dd81315ce7f3704d9dbae3ba94635928cb2d4df062d6e9ab01 | quote: Storage Charges Delayed Indefinitely – Previously, we announced plans to introduce storage-based billing, but we have decided to indefinitely delay any storage charges.
- sources:
  - [1] https://docs.docker.com/docker-hub/usage/
  - [2] https://www.docker.com/blog/revisiting-docker-hub-policies-prioritizing-developer-experience/
  - [3] https://auth.docker.io/token?service=registry.docker.io&scope=repository:library/alpine:pull
  - [4] https://registry-1.docker.io/v2/library/alpine/blobs/uploads/
  - [5] https://github.com/Androsh7/layerstash

## Docker Cloud Sandboxes

- `compute/docker-cloud-sandboxes` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T11:17:39.908Z (live) | stale on 2026-12-26
- url https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/
- free tier: new accounts get $250 in free Cloud Sandboxes credit for a limited time; after that compute bills per second from $0.07 an hour for Micro at 1 vCPU and 2 GiB, a paused sandbox costs nothing, and volumes, egress, and hosting public images and Kits are free | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: egress and volumes are free; compute by the second is the only meter and a paused sandbox costs nothing | metered: no | free allowance: egress is free | source: [1]
- identity: card | detail: email and card: a Docker account signs in to the Agentic Platform console and checkout asks for billing and payment details; the promotion states a valid credit card is required, with no phone or ID document named
- interface: cli, rest, browser
- limits:
  - request-rate (binding): $0.07 an hour for Micro at 1 vCPU and 2 GiB, up to $1.12 for XL at 16 vCPU and 32 GiB [1]
  - retention-clamped: a sandbox expires after one hour by default; expiration cannot be extended beyond 24 hours from creation; a paused sandbox costs nothing [1]
  - per-object-cap: the page states no disk cap per sandbox; it says hosting public images and Kits is free [1]
- interface detail: the sbx CLI with the --cloud flag, the Cloud Sandboxes API and the web console at agentic-platform.docker.com
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the announcement page was read on 2026-10-22 and states the per-second metering, the paused-sandbox behaviour and the size ladder. The USD 25 credit the record carried is not on it, so the verdict moves to paid-only on what the page does say
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 2
  - shape.ram: 4
  - shape.note: Small is the default at 2 vCPU and 4 GiB for $0.14 an hour
  - session_cap.restart_required: no
  - session_cap.note: a paused sandbox costs nothing, so stopping is a pause rather than a loss; the page describes running an agent for hours with the laptop closed
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.price: volumes are free
  - ps.durability: volume
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.ports: published ports
  - net.allowance: egress is free
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Cloud Sandboxes are pay-as-you-go. We meter compute by the second, and nothing else. A paused sandbox costs nothing. Volumes, egress, and hosting public images and Kits are free.' with sizes from Micro at $0.07 an hour (1 vCPU, 2 GiB) to XL at $1.12 (16 vCPU, 32 GiB)…
  - [1] 2026-11-25: new accounts get $250 in free Cloud Sandboxes credit for a limited time | capture: sha256:d635812629000baf4c0643fbb3f7adf6ecf0128e26e5d5741dd8b3ae337b1a33 | quote: For a limited time, new accounts **get $250 in free Cloud Sandboxes credit. [Claim it here](https://www.docker.com/c/sbx-promo/).**
  - [1] 2026-11-25: compute bills by the second, a paused sandbox costs nothing, and volumes, egress and public images and Kits are free | capture: sha256:d635812629000baf4c0643fbb3f7adf6ecf0128e26e5d5741dd8b3ae337b1a33 | quote: Cloud Sandboxes are pay-as-you-go. We meter compute by the second, and nothing else. A paused sandbox costs nothing. Volumes, egress, and hosting public images and Kits are free.
  - [1] 2026-11-25: Micro is 1 vCPU and 2 GiB at $0.07 per hour | capture: sha256:d635812629000baf4c0643fbb3f7adf6ecf0128e26e5d5741dd8b3ae337b1a33 | quote: | Size | vCPUs | Memory | Per hour | | --- | --- | --- | --- | | Micro | 1 | 2 GiB | $0.07 |
  - [1] 2026-11-25: the page states the $250 new-account credit, the by-the-second metering, the free paused sandbox and volumes, egress and public images, and the $0.07 Micro rate at 1 vCPU and 2 GiB | capture: sha256:d635812629000baf4c0643fbb3f7adf6ecf0128e26e5d5741dd8b3ae337b1a33 | quote: For a limited time, new accounts **get $250 in free Cloud Sandboxes credit. [Claim it here](https://www.docker.com/c/sbx-promo/).** ... Cloud Sandboxes are pay-as-you-go. We meter compute by the second, and nothing else. A paused sandbox costs nothing. Volumes, egress, and hosting public images and Kits are free. ... | Size | vCPUs | Memory | Per hour | | --- | --- | --- | --- | | Micro | 1 | 2 GiB | $0.07…
  - [1] 2026-11-24: compute is the only meter; paused sandboxes, volumes, egress and public image hosting are free | capture: sha256:d635812629000baf4c0643fbb3f7adf6ecf0128e26e5d5741dd8b3ae337b1a33 | quote: Cloud Sandboxes are pay-as-you-go. We meter compute by the second, and nothing else. A paused sandbox costs nothing. Volumes, egress, and hosting public images and Kits are free.
  - [2] 2026-11-24: new accounts get a $250 promotional credit and a card is required | capture: sha256:bf79700da75aa6f3867c8e785eb885563dc4eb4d8f3b43518c0a282fc7f04c76 | quote: Get $250 in compute credit when you sign up for Docker Agentic Platform till 1/31/2027. Credit card required at signup. Terms Apply.
  - [2] 2026-11-24: the $250 credit is a one-time sign-up credit | capture: sha256:bf79700da75aa6f3867c8e785eb885563dc4eb4d8f3b43518c0a282fc7f04c76 | quote: New Docker Agentic Platform signups receive a one-time $250 compute credit in lieu of the standard $25 credit. Limit one per user and account.
  - [3] 2026-11-24: cloud access requires a pay-as-you-go checkout with billing and payment details | capture: sha256:d0f6173e390fc0f2b30292aa41c4621bd189c882492200c5afc12061c5f742de | quote: If your account doesn't have access, follow the redirect to Docker Billing. Review the Docker Agentic Platform pay-as-you-go plan, provide the requested billing and payment details, and complete checkout.
  - [2] 2026-11-24: a valid credit card is required at signup | capture: sha256:bf79700da75aa6f3867c8e785eb885563dc4eb4d8f3b43518c0a282fc7f04c76 | quote: Valid credit card required at signup; the card will be charged only for usage beyond the credit.
  - [4] 2026-11-24: the interface is the sbx CLI and the Cloud Sandboxes API | capture: sha256:b0c8b446b8ca7215ef0e44a82696f8932966faa6998832854cc6355f68747309 | quote: Cloud sandboxes use the same `sbx` CLI as local sandboxes. Add the global `--cloud` flag to send a supported command to the Cloud Sandboxes API:
  - [5] 2026-11-24: the default sandbox lifetime is one hour | capture: sha256:4f5dab2febe1e386054b886aca443bbfb5d27f1f9e89b4b71b9369d3833663e1 | quote: A cloud sandbox expires after one hour by default. On expiration, the service stops sandboxes that can be resumed and deletes the rest. See
  - [5] 2026-11-24: expiration can never extend past 24 hours | capture: sha256:4f5dab2febe1e386054b886aca443bbfb5d27f1f9e89b4b71b9369d3833663e1 | quote: Extensions cannot move expiration beyond 24 hours from creation:
  - [1] 2026-11-24: the XL shape is $1.12 an hour | capture: sha256:d635812629000baf4c0643fbb3f7adf6ecf0128e26e5d5741dd8b3ae337b1a33 | quote: | XL | 16 | 32 GiB | $1.12 |
- sources:
  - [1] https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/
  - [2] https://www.docker.com/c/sbx-promo/
  - [3] https://docs.docker.com/agentic-platform/signup/
  - [4] https://docs.docker.com/ai/sandboxes/cloud/
  - [5] https://docs.docker.com/ai/sandboxes/cloud/usage/
