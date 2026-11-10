# Quay.io public repositories

> quay.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/quay/ | JSON https://fshy.ajam.dev/api/v1/entity/quay.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Quay.io public repositories (Red Hat)

- `storage/quay-io-public-repositories` | qualifies | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://quay.io
- free tier: "We offer unlimited storage and serving of public repositories". Red Hat's own support article. Every paid plan is priced only by private-repo count and lists 'Unlimited public repos'; a free account gets unlimited public repos, private repos require a 30-day trial then a paid plan. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Every paid plan is priced only by private-repo count and lists 'Unlimited public repos'; a free account gets unlimited public repos, private repos require a 30-day trial then a paid plan | days: 30 | source: [1] | note: not stated
- egress: Included in 'unlimited storage and serving of public repositories'. No per-GB line item exists for public repos on any plan. Served over quay.io's own CDN edge. | metered: no
- identity: anonymous
- interface: oci
- limits note: Requires a Red Hat SSO account to push (anonymous pull only). Quay is a shared hosted registry: pull QPS and total storage are subject to undisclosed fair use; the paid tiers exist purely to buy private repos, which signals public storage is deliberately not metered.
- interface detail: oci
- tooling: oras push / docker push / skopeo; Cosign/notation signing supported natively.
- composes with: N public repos x N free Red Hat accounts. Repos are namespaced per user/org, so one account already gives effectively unbounded blob count; orgs are free to create.
- reliability: Hosted multitenancy means a noisy-neighbour throttle is possible but not documented; no data-expiry policy on public repos, so blobs persist indefinitely.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: read live: 'Can I use Quay for free? Yes! We offer unlimited storage and serving of public repositories.'
  - [2] 2026-10-21: read live: every tier lists 'Unlimited public repos'; Developer is $15/mo for 5 private repos, i.e. no free private tier, 30-day trial only
  - [3] 2026-10-21: probe: GET -> 401 with WWW-Authenticate: Bearer realm="https://quay.io/v2/auth",service="quay.io" (correct challenge); then GET https://quay.io/v2/prometheus/busybox/manifests/latest -> 200, 736 bytes anonymous
  - [4] 2026-10-21: probe: POST -> 404 (anonymous write refused)
- sources:
  - [1] https://access.redhat.com/articles/quayio-help
  - [2] https://quay.io/plans/
  - [3] https://quay.io/v2/
  - [4] https://quay.io/v2/probe/blobs/uploads/
