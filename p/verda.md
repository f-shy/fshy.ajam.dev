# Verda

> verda.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/verda/ | JSON https://fshy.ajam.dev/api/v1/entity/verda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Verda (formerly DataCrunch)

- `compute/verda` | paid-only | evidence documented | binding request-rate | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:03:48.362Z (live) | stale on 2026-12-26
- url https://verda.com/pricing
- free tier: True pay-as-you-go pricing on multi-node clusters. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: Sign in with Google, Microsoft or GitHub, or with email and password; the console is protected by reCAPTCHA. No card or phone number is stated on the sign-in page.
- interface: rest, cli
- limits:
  - request-rate (binding): priced per GPU-hour on instances, clusters and serverless containers, with no commitment and no minimum on pay-as-you-go; reserved discounts run from 1 month to 2 years [1]
- interface detail: Provision and manage with a UI console, Terraform, SDK and API; the inference gateway uses an OpenAI-compatible API.
- tooling: the user installs and runs Terraform or an SDK against the Verda API; the console manages deployments without installed tooling
- composes with: GPU instances, CPU instances, instant clusters, serverless containers and storage are all priced on one page; spot is a discount off the paid on-demand rate and reserved terms run from one month to two years
- reliability: no reliability event recorded
- notes: Paid-only stands: the page lists no free tier, and spot is a discount off a paid meter. Content-creation credits are discretionary and publish no amount, so they are not a countable free lane. Verda now also publishes token-priced inference; the content-credit route needs a published amount from the operator.
- evidence note: the pricing page was read on 2026-10-22 and states the pay-as-you-go model per GPU. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.note: priced per GPU with specs shown per row
  - session_cap.restart_required: no
  - session_cap.note: a cluster runs for an hour or months; the page states no reap
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'True pay-as-you-go pricing on multi-node clusters. Spin up for an hour or months - no commitments, no minimums. Specs and price are shown per GPU.' quoted
  - [1] 2026-11-25: the multi-node cluster offer is pay-as-you-go | capture: sha256:539a0b612b63f21ff087b28bb647efcdd2e2dde0e4445c6d6b59d73ddcde6798 | quote: True pay-as-you-go pricing on multi-node clusters.
  - [1] 2026-11-24: the page offers only paid capacity tiers | capture: sha256:539a0b612b63f21ff087b28bb647efcdd2e2dde0e4445c6d6b59d73ddcde6798 | quote: - Full-stack, AI Lab-backed - Pay-as-you-go, spot, or reserved
  - [2] 2026-11-24: email/password registration is offered alongside the social logins | capture: sha256:6c71c68b4c1dc7aeef5c72717d2c63bced0a8b839f545d633e2638f05c319ce8 | quote: or continue with email
  - [1] 2026-11-24: the platform is managed through an API and Terraform as well as the console | capture: sha256:539a0b612b63f21ff087b28bb647efcdd2e2dde0e4445c6d6b59d73ddcde6798 | quote: Provision and manage with UI console, Terraform, SDK, or API.
  - [1] 2026-11-24: an OpenAI-compatible inference API is published | capture: sha256:539a0b612b63f21ff087b28bb647efcdd2e2dde0e4445c6d6b59d73ddcde6798 | quote: Frontier open-weight models through one OpenAI compatible API, billed per token.
  - [1] 2026-11-24: reserved discounts are published by commitment length | capture: sha256:539a0b612b63f21ff087b28bb647efcdd2e2dde0e4445c6d6b59d73ddcde6798 | quote: | 1 month | 2% off on-demand |
  - [1] 2026-11-24: pay-as-you-go has no commitment | capture: sha256:539a0b612b63f21ff087b28bb647efcdd2e2dde0e4445c6d6b59d73ddcde6798 | quote: Pay-as-you-go pricing. Start and end deployments at any time, without long-term commitments.
  - [1] 2026-11-24: the pay-as-you-go model and absence of a free tier are unchanged | capture: sha256:539a0b612b63f21ff087b28bb647efcdd2e2dde0e4445c6d6b59d73ddcde6798 | quote: True pay-as-you-go pricing on multi-node clusters. Spin up for an hour or months — no commitments, no minimums. Specs and price are shown per GPU.
  - [1] 2026-11-24: the on-demand and spot prices for one H100 are published | capture: sha256:539a0b612b63f21ff087b28bb647efcdd2e2dde0e4445c6d6b59d73ddcde6798 | quote: | 1x H100 SXM5 80GB | 30 | 120 GB | 80 GB | $5.619/h | $2.810/h |
  - [1] 2026-11-24: token-priced inference is a separate product on the same page | capture: sha256:539a0b612b63f21ff087b28bb647efcdd2e2dde0e4445c6d6b59d73ddcde6798 | quote: | Kimi K3.1 Pro | 1M | $2.00 | $0.20 | $10.00 |
  - [3] 2026-11-24: a bare GET to the inference gateway URL is not an endpoint | capture: sha256:29e505e46afd6ead652e3a337816ec12e926084cd0756bb6dba31e9862e60b3e | quote: "message":"GET /v1 is not an endpoint of this gateway"
- sources:
  - [1] https://verda.com/pricing
  - [2] https://console.verda.com/signin
  - [3] https://inference.verda.com/v1
