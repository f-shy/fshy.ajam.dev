# Appish

> appi.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/appi/ | JSON https://fshy.ajam.dev/api/v1/entity/appi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Appish

- `compute/appish` | qualifies-with-caveat | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T11:01:13.169Z (live) | stale on 2026-12-05
- url https://appi.sh/pricing
- free tier: Free plan, quoted: '1 slot', '4 hours each, extend with one click any time', 'public URL', 'shared resources', 'best for hackathons, README demos, one-off shares'. Paid: 'Paid App Slot USD 5/month per slot' with 'Custom expiry configuration', 'Stays online while your subscription is active' and 'better resource limits'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: a free slot expires after 4 hours, extendable by hand, so nothing survives an unattended overnight run. | source: [1]
- egress: not published: the page read states no egress allowance and no overage price; https://appi.sh/pricing read 2026-11-03 | metered: no | source: [1]
- identity: email
- interface: oci
- limits:
  - retention-clamped (binding): a free slot expires after 4 hours, extendable by hand, so nothing survives an unattended overnight run. [1]
- limits note: a free slot expires after 4 hours, extendable by hand, so nothing survives an unattended overnight run.
- binding note: the same as limits note
- interface detail: docker buildx build --push to push.to.appi.sh/<push-id>/app:port_3000; the page documents no REST API, CLI or SSH access
- tooling: Docker, per https://appi.sh/: "`docker push` it once and get a shareable URL. Free Docker container hosting with no repo, no YAML, no CI/CD, no new CLI to learn.".
- composes with: no repository is needed, only an image, so a built image can be published for a third party to open inside the 4-hour window without touching a git host or a CI minutes budget.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says 'Host Docker containers for demos with just a docker push. Free tier includes 1 slot with 2-hour sessions.' The slot count is right and the session length is wrong: the vendor prices the free slot at 4 hours, and it is extendable by hand. The aggregator also omits that CPU and memory are shared and unspecified on the free slot, so the shape is left null here rather than guessed.
- extras:
  - facets.free_tier_kind: free-forever
- evidence:
  - [1] 2026-10-22: 'Free USD 0/mo - 1 slot - 4 hours each, extend with one click any time - public URL - shared resources', quoted
  - [1] 2026-10-22: 'Paid App Slot USD 5/month per slot' with 'Custom expiry configuration' and 'Stays online while your subscription is active', quoted
  - [2] 2026-10-22: 'docker push it once and get a shareable URL - free Docker container hosting with no repo, no YAML, no CI/CD', with the tag convention 'port_3000' setting the listening port, quoted
  - [1] 2026-11-03: the free plan page lists no egress allowance or overage price | capture: sha256:834b2336574ba2b2fb011989c778da2fb1dab05efdd3b31527103b3c5c1e5b57 | quote: - shared resources
  - [2] 2026-11-03: the slot is reached by pushing an image to a registry host with docker; no git repository is involved | capture: sha256:9a0278d9cbed30479e1960817c0eff49c42257d08765c7db650219b7b23addc1 | quote: `docker push` it once and get a shareable URL — free Docker container hosting with no repo, no YAML, no CI/CD, no new CLI to learn.
  - [2] 2026-11-04: the page names docker push as the way in and no new CLI | capture: sha256:9a0278d9cbed30479e1960817c0eff49c42257d08765c7db650219b7b23addc1 | quote: `docker push` it once and get a shareable URL — free Docker container hosting with no repo, no YAML, no CI/CD, no new CLI to learn.
- sources:
  - [1] https://appi.sh/pricing
  - [2] https://appi.sh/
