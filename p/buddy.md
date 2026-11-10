# Buddy Sandboxes

> buddy.works | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/buddy/ | JSON https://fshy.ajam.dev/api/v1/entity/buddy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Buddy Sandboxes

- `compute/buddy` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T15:51:56.486Z (live) | stale on 2026-12-05
- url https://buddy.works/pricing
- free tier: a free tier with 2 concurrency slots, 1 seat and $1 a month of usage credit for compute and storage | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page lists seats, concurrents, a $1 monthly usage credit and a pay-as-you-go rate per CPU-minute and GB-minute, with no egress allowance or overage | metered: no | source: [1]
- identity: email | detail: an email address and a full name at registration, 'Your work email' and 'Full Name', or a GitHub, GitLab, Google or Bitbucket sign-in. The free start is advertised with 'No credit card required.', and the form asks for no phone number.
- interface: rest, cli, ssh
- limits:
  - request-rate (binding): 2 concurrent pipelines on Free, with no option to buy more [1]
  - per-object-cap: 1 seat and $1 a month of usage credit covering compute and storage [1]
- interface detail: web UI, the bdy CLI, a TypeScript SDK, a REST API, YAML pipeline definitions and SSH from an IDE
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the free tier's three limits and the $1 monthly credit. The record's USD 5 does not match the $1 the page shows
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a pipeline runs to completion; the $1 monthly credit is the bound
  - free_tier_kind: recurring-credit
  - burst_x: 1.0
  - ps.price: $0.00024 per GB-minute from the credit
  - ps.durability: workspace storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the workspace exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '2 concurrents (no extra concurrents)' with a '$1/mo. usage credit (compute & storage)' and '1 seat', against 'Pay-as-you-go usage (from $0.00024 per CPU-minute / GB-minute)', quoted
  - [2] 2026-11-04: Sandboxes have a REST API | capture: sha256:cd60e701b06bc8b0ee9b94ddad63caf87b2ea9144e78b63ed4e2c48f108febd5 | quote: | REST API | Any language, any automation | [API reference](https://buddy.works/docs/api/sandboxes) |
  - [2] 2026-11-04: Sandboxes are reachable over SSH | capture: sha256:cd60e701b06bc8b0ee9b94ddad63caf87b2ea9144e78b63ed4e2c48f108febd5 | quote: - Remote development - reachable over SSH from your IDE.
  - [1] 2026-11-04: usage is priced per CPU-minute and GB-minute, with no network row | capture: sha256:8ada3ee74545ff56db005f3b3eb18602471f26f355872143575d33eb6bc36023 | quote: Pay-as-you-go usage (from $0.00024 per CPU-minute / GB-minute)
  - [3] 2026-11-04: the registration form collects an email address | capture: sha256:a7d0ecfe4b9af372ddd2c20df9e0c604b6fdcd31d21bf09de8d43c2af51fa239 | quote: Your work email
  - [4] 2026-11-04: the free start is advertised without a card | capture: sha256:d3b7e04f0ccd791efeabf3330ac0bc63dbf718e6de4fc3392c79e67b1cacf03b | quote: No credit card required.
  - [3] 2026-11-04: four OAuth sign-ins sit beside the email form | capture: sha256:a7d0ecfe4b9af372ddd2c20df9e0c604b6fdcd31d21bf09de8d43c2af51fa239 | quote: GitHub GitLab Google Bitbucket
- sources:
  - [1] https://buddy.works/pricing
  - [2] https://buddy.works/docs/sandboxes/introduction
  - [3] https://buddy.works/sign-up
  - [4] https://buddy.works/react
