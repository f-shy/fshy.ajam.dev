# Docker Cloud

> docker.com | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/docker/ | JSON https://fshy.ajam.dev/api/v1/entity/docker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Docker Hub (free Personal plan, public repositories)

- `storage/docker-hub` | qualifies | evidence reported | binding per-ip-shaping | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hub.docker.com
- free tier: Unlimited public repositories on the free Personal plan; NO documented storage cap on public repositories. Docker's own limits table lists only pull-rate and repository counts, with no storage row. Docker's Feb 2025 policy post says storage-based billing is 'indefinitely delayed' with a promised six-month notice. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Pull count 100 per 6 hours anonymous or 200 per 6 hours authenticated per IP. Large download throughput requires few, large blobs rather than many small ones. | source: [1] | note: not stated
- egress: Free and unmetered per-GB; the gate is a pull COUNT, not bytes: 'Unauthenticated users: 100 per IPv4 address or IPv6 /64 subnet' and 'Personal (authenticated): 200' per 6 hours. Blobs are served by 307 redirect to a CDN, so one pull can be a multi-GB blob. | metered: no
- identity: anonymous
- interface: oci
- limits:
  - per-ip-shaping (binding): 1TiB/day [1]
- limits note: Pull count is 100 per 6 hours anonymous or 200 per 6 hours authenticated per IP. No published per-layer size cap, but Docker distribution S3 drivers historically faced issues above 10 GB per layer, recommending shards around 5 GB. Excess request limits return HTTP 429.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: oci
- tooling: oras push / docker push; purpose-built wrapper: github.com/Androsh7/layerstash (chunks >5GB files into ~5GB layers, uploads to Docker Hub or GHCR; author reports 1.8TB personally stored), github.com/xausky/DockerRegisterCloud (654 stars, registry-as-netdisk client with Flutter GUI + direct-download server).
- composes with: Unlimited public repos per account, and the free account count itself is unlimited. Layer count per repo is not capped, so a single repo holds arbitrarily many blobs; layerstash's <base-tag>-<chunk_n> scheme makes one repo a striped volume of unlimited size.
- reliability: Storage is unpriced today but Docker reserves the right to add charges and has flip-flopped before (announced Mar 2025, cancelled Apr 2025); the 100-pull/6h IP limit will throttle any fetch fan-out from one host.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: read live: table has columns Pull rate limit / public repos / private repos only; Personal = Unlimited public repos, 200 pulls/6h; no storage row anywhere on the page
  - [2] 2026-10-21: read live: 'Storage Charges Delayed Indefinitely ... we have decided to indefinitely delay any storage charges', and 'We did not enforce the Docker Hub rate limit changes previously scheduled for April 1, 2025'
  - [3] 2026-10-21: probe: GET -> 200 (2698-char token); then GET registry-1.docker.io/v2/library/alpine/manifests/latest -> 200, 9218 bytes, anonymous, no account
  - [4] 2026-10-21: probe: POST -> 401 (anonymous push correctly refused; write requires an account, read does not)
  - [5] 2026-10-21: read live: 'I have stored a total of 1.8TB in a public repository on Docker Hub androsh7/archive'
- sources:
  - [1] https://docs.docker.com/docker-hub/usage/
  - [2] https://www.docker.com/blog/revisiting-docker-hub-policies-prioritizing-developer-experience/
  - [3] https://auth.docker.io/token?service=registry.docker.io&scope=repository:library/alpine:pull
  - [4] https://registry-1.docker.io/v2/library/alpine/blobs/uploads/
  - [5] https://github.com/Androsh7/layerstash

## Docker Cloud Sandboxes

- `compute/docker-cloud-sandboxes` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:47.746Z (live) | stale on 2026-11-22
- url https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/
- free tier: no free tier: compute bills per second from $0.07 an hour for 1 vCPU and 2 GiB, and a paused sandbox costs nothing; volumes and egress are free | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.07 an hour for Micro at 1 vCPU and 2 GiB, up to $1.12 for XL at 16 vCPU and 32 GiB [1]
  - retention-clamped: a paused sandbox costs nothing; egress and volumes are not metered [1]
  - per-object-cap: the page states no disk cap per sandbox; it says hosting public images and Kits is free [1]
- interface detail: Access interface not documented in published terms.
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
- sources:
  - [1] https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/
