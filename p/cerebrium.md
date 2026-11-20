# Cerebrium

> cerebrium.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cerebrium/ | JSON https://fshy.ajam.dev/api/v1/entity/cerebrium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cerebrium

- `compute/cerebrium` | qualifies-with-caveat | evidence documented | binding request-rate | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-09T13:13:24.511Z (live) | stale on 2026-12-10
- url https://cerebrium.ai/pricing
- free tier: a Free tier priced as 'Free + compute a month' with 500 containers and 5 concurrent GPUs, plus the first 100 GB of storage free at $0.05 a GB a month past it | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: included: the pricing page states that the price includes orchestration, networking and the serverless platform, so no separate egress line is published and no per-gigabyte charge is stated | metered: no | source: [1]
- identity: email | detail: The signup form offers Sign Up With GitHub and Sign Up With Google, or a first name, a last name and a work email with a password; it carries no phone field and no card field, so an email account reaches the free tier. No country limit is stated on the form.
- interface: unknown
- limits:
  - request-rate (binding): the Free tier carries no platform fee but compute bills per second: CPU at $0.00000655 a vCPU-second, T4 at $0.000164 a second, H100 at $0.000944 a second [1]
  - per-object-cap: the first 100 GB of storage is free at $0.05 a GB a month [1]
  - request-rate (binding): 500 containers and 5 concurrent GPUs on the free tier [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and lists the per-second GPU and CPU rates, the 100 GB storage allowance and a free tier with no container charge. The free tier's compute is not free, which the page's own wording says
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.disk: 100
  - shape.gpu_class: T4 through B200
  - shape.gpu_count: 5
  - shape.note: per-second rates from T4 at $0.000164 to B200 at $0.00167; 5 concurrent GPUs on the free tier
  - session_cap.restart_required: no
  - session_cap.note: compute scales with demand and bills per second; the page states no session clock
  - free_tier_kind: allowance
  - ps.gib: 100
  - ps.price: $0.05 a GB a month past the first 100 GB
  - ps.durability: storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while billed
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Cerebrium charges based on actual compute time, measured in seconds' and 'CPU Only $0.00000655 /vCPU/s', 'Storage $0.05 /GB/mo', '*First 100GB storage free', and a 'Free + compute / month' entry with '500 containers + 5 Concurrent GPUs', quoted
  - [2] 2026-11-02: the signup form asks for GitHub or Google, or a first name, last name and work email, with no phone and no card field | capture: sha256:2a8052cd6f989241a4ea2595bff165a9b6ab47a880a3e7d4337eefcb39c7b18e | quote: Sign Up With GitHub Sign Up With Google OR First name First name Last name Last name Work email
  - [3] 2026-11-02: the terms require a payment method and a card only to pay for a subscription | capture: sha256:6f68131a56ea52e86b8a0bb584ac981e2f018dff5da9491f8406f854ca9ed861 | quote: A valid payment method, including a credit card, is required to process the payment for your subscription.
  - [2] 2026-11-02: the signup needs an email account and carries no phone or card field | capture: sha256:2a8052cd6f989241a4ea2595bff165a9b6ab47a880a3e7d4337eefcb39c7b18e | quote: Sign Up With GitHub Sign Up With Google OR First name First name Last name Last name Work email
  - [1] 2026-11-09: the page states that networking is inside the price, so no separate egress charge is published | capture: sha256:ddb0da4f8fccaeff7aa113f6d39c2826daa6c714872f3f74c2d293517c467097 | quote: Our pricing also includes orchestration, networking, and the serverless platform required to run AI workloads in production
  - [1] 2026-11-09: the page states that networking is inside the price | capture: sha256:ddb0da4f8fccaeff7aa113f6d39c2826daa6c714872f3f74c2d293517c467097 | quote: Our pricing also includes orchestration, networking, and the serverless platform required to run AI workloads in production
- sources:
  - [1] https://cerebrium.ai/pricing
  - [2] https://dashboard.cerebrium.ai/signup
  - [3] https://www.cerebrium.ai/terms-of-service
