# Harness CI Free plan

> harness.io | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/harness/ | JSON https://fshy.ajam.dev/api/v1/entity/harness.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Harness CI Free plan (Harness Cloud)

- `ci-cd-runners/harness-ci-free` | fails-identity | evidence documented | binding request-rate | category CI runner | tier Free
- needs card no, phone no, ID no, institution yes | verified 2026-11-04T06:00:39.389Z (live) | stale on 2026-12-05
- url https://developer.harness.io/continuous-integration/troubleshooting-and-resources/ci-subscription-mgmt
- free tier: Free plans receive 2,000 Harness Cloud credits every month, and unused credits expire at month end; Linux xsmall (2 cores, 7 GB) costs 1 credit a minute and Linux small (4 cores, 15 GB) 2 credits a minute | unit: credits | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: the pricing page's Free plan lists Harness Open Source, Litmus Chaos and community support and names no CI module or Harness Cloud allowance; the Harness Cloud product page and the CI documentation state the 2,000 a month
- per-object cap: on the Free plan a stage times out at 1 hour and a pipeline at 2 hours; each CI stage runs in a new ephemeral VM | source: [2]
- retention: unverified: no log or artifact retention period for the Free plan was found in the pages read; cache above the 2 GB Free limit evicts the oldest caches | source: [1]
- egress: network transfer from Harness Cloud to customer-managed storage is limited to 1 GB on Free, 5 GB on Startup and 10 GB on Enterprise | metered: yes | free allowance: 1 GB of network transfer to customer-managed storage | source: [1]
- identity: institution | detail: Harness Cloud on the Free plan is limited to business email domains, with Gmail, Hotmail, Yahoo and other unverified domains blocked, and Free plans require credit card validation to use it; the Harness Cloud product page says 'No credit card required', which the CI documentation contradicts
- interface: git
- limits:
  - request-rate (binding): 2,000 credits a month on Free, unused credits expire; Linux xsmall (2 cores, 7 GB) 1 credit a minute, Linux small (4 cores, 15 GB) 2 credits a minute [1]
  - request-rate (binding): 2 concurrent pipeline executions per account on the Free plan, not editable; 2 concurrent steps or stages within one execution [2]
  - request-rate (binding): Harness Cloud concurrent stages on Free: Linux 20, Windows 1, macOS 1 [1]
  - per-object-cap: stage timeout 1 hour and pipeline timeout 2 hours on the Free plan [2]
  - volume-quota: 1 GB of network transfer from Harness Cloud to customer-managed storage on Free [1]
- limits note: 2 GB of CI Intelligence cache storage on Free, with the oldest caches evicted beyond it; use beyond the credits continues and is invoiced in arrears
- binding note: identity binds before any limit: Harness Cloud on Free needs card validation and a business email domain. Among the limits, the 2,000 monthly credits are 2,000 xsmall minutes, about 33 hours (2,000 / 60); the 1-hour stage timeout binds first for any single long job
- interface detail: a Harness pipeline built in the visual editor or YAML, with a CI stage on Harness Cloud infrastructure and a Git connector to the repository
- tooling: Harness-managed VMs: Linux AMD64 and ARM64 from 2 to 96 cores, Windows, and macOS on Apple M4; Ubuntu 22.04 or 24.04 images with preinstalled tools; steps run on the VM or in a Docker container. The local runner, which the user installs and runs on a machine of their own, rented or free, has no build limit and needs no card; it comes after the hosted offer
- composes with: 2,000 Linux xsmall minutes a month behind a card check and a business email domain; the 1 GB transfer limit to outside storage makes it a place to run work rather than to ship large outputs
- reliability: credits used beyond the allowance are invoiced in arrears, and Harness may suspend Harness Cloud executions when they are not paid
- notes: The allowance is real on paper, 2,000 credits a month with 20 concurrent Linux stages, but the account-wide limit of 2 concurrent pipeline executions and the 1-hour stage timeout make it small, and the gate in front of it is a business email domain plus card validation. The Developer 360 post (updated 2026-09-30) lists Continuous Integration among the Free plan modules and the CI documentation still states the 2,000 credits, although the pricing page's Free plan names no CI module; whether a new Free account receives the credits, and whether a custom-domain address passes the business-domain check, is unverified: behind a sign-up.
- evidence note: the CI subscription, Harness Cloud and pipeline settings documentation, the pricing page and the Harness Cloud product page were read and quoted on 2026-10-30; the sign-up gate itself is a single-page app and was not passed. Raised by a sign-up outcome with a generic and a custom-domain address.
- evidence:
  - [1] 2026-10-30: 2,000 free credits a month on Free, expiring at month end | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: Free plans receive 2000 free credits every month. Any free credits that are unused at the end of the month expire automatically and do not roll over from one month to the next.
  - [1] 2026-10-30: Linux xsmall is 2 cores and 7 GB with a minute multiplier of 1 | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: | Linux | AMD64 | xsmall | 2 | 7 | 1 | $0.005 |
  - [1] 2026-10-30: Linux small costs 2 credits a minute | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: 1,000 minutes on a Linux, 4-core (small) machine = 2,000 cloud credits (1,000 minutes × 2).
  - [1] 2026-10-30: Harness Cloud runs 20 concurrent Linux stages on Free | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: | Linux | 20 | 40 | 60 |
  - [1] 2026-10-30: network transfer to customer-managed storage is 1 GB on Free | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: Free: 1 GB
  - [1] 2026-10-30: CI Intelligence cache storage is 2 GB on Free | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: Free: 2 GB
  - [1] 2026-10-30: old caches are evicted beyond the limit | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: once you reach your storage limit, Harness continues to save new caches while automatically evicting old caches.
  - [1] 2026-10-30: use beyond the credits is invoiced in arrears | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: Harness will allow you to continue using Harness Cloud even if you do not have enough credits in your account to cover your total execution time, but Harness will invoice you in arrears for all credits owed.
  - [3] 2026-10-30: 2,000 free Harness Cloud credits a month on Free | capture: sha256:7c796cf76eadde1a106bd40dd1e4a5fd8720f6260a00f0c51f20c7af6f795fa2 | quote: Free plans get 2000 free Harness Cloud credits each month.
  - [3] 2026-10-30: Harness Cloud on Free needs card validation | capture: sha256:7c796cf76eadde1a106bd40dd1e4a5fd8720f6260a00f0c51f20c7af6f795fa2 | quote: Free plans require credit card validation to use Harness Cloud.
  - [3] 2026-10-30: Harness Cloud is limited to business email domains | capture: sha256:7c796cf76eadde1a106bd40dd1e4a5fd8720f6260a00f0c51f20c7af6f795fa2 | quote: Harness now limits the use of the Harness Cloud build infrastructure to business domains and block general-use domains, like Gmail, Hotmail, Yahoo, and other unverified domains.
  - [3] 2026-10-30: each stage runs in a new ephemeral VM | capture: sha256:7c796cf76eadde1a106bd40dd1e4a5fd8720f6260a00f0c51f20c7af6f795fa2 | quote: When a build runs on Harness Cloud, Harness runs each CI stage in a new, ephemeral VM.
  - [3] 2026-10-30: builds on the user's own infrastructure have no limit | capture: sha256:7c796cf76eadde1a106bd40dd1e4a5fd8720f6260a00f0c51f20c7af6f795fa2 | quote: There are no limitations on builds using your own infrastructure.
  - [2] 2026-10-30: 2 concurrent pipeline executions per account on Free, not editable | capture: sha256:bececc2360add93084dadce3df0a9e8787d788756e64de6a7ef7fa7bad3e5dfe | quote: | Free plan and Team/Enterprise trials | 2 | 2 | No | Account |
  - [2] 2026-10-30: a stage times out at 1 hour on Free | capture: sha256:bececc2360add93084dadce3df0a9e8787d788756e64de6a7ef7fa7bad3e5dfe | quote: | Stage timeout | 1 hr | 1 hr | 30 days | 35 days |
  - [2] 2026-10-30: a pipeline times out at 2 hours on Free | capture: sha256:bececc2360add93084dadce3df0a9e8787d788756e64de6a7ef7fa7bad3e5dfe | quote: | Pipeline timeout | 2 hr | 4 hr | 30 days | 35 days |
  - [4] 2026-10-30: the Free plan on the pricing page names no CI module | capture: sha256:24a2bde6cc98216794a0951af2a6505cd48ae6dd7ed8bdf9af90831fd29489c9 | quote: For individual developers and small teams. Includes Harness Open Source, Litmus Chaos and community support.
  - [5] 2026-10-30: the product page states 2,000 build minutes a month and no card | capture: sha256:8aecb6335408a106f1834a6b3428f9a7a88a2dae79bcc2f2783008b18889378b | quote: Free plan includes 2,000 build minutes per month on Harness Cloud. No credit card required.
  - [1] 2026-11-02: the CI documentation still gives Free plans 2,000 credits a month, unused credits expiring at month end | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: Free plans receive 2000 free credits every month. Any free credits that are unused at the end of the month expire automatically and do not roll over from one month to the next.
  - [3] 2026-11-02: the documentation still limits Harness Cloud on Free to business domains and blocks general-use domains | capture: sha256:aec8ac869f48a77375d04eac7424d6a36b3a2075795fdfb2da4f9a3a197ac778 | quote: Harness now limits the use of the Harness Cloud build infrastructure to business domains and block general-use domains, like Gmail, Hotmail, Yahoo, and other unverified domains.
  - [3] 2026-11-02: the Harness Cloud page still states 2,000 Harness Cloud credits a month on Free | capture: sha256:aec8ac869f48a77375d04eac7424d6a36b3a2075795fdfb2da4f9a3a197ac778 | quote: Free plans get 2000 free Harness Cloud credits each month.
  - [6] 2026-11-02: the Developer 360 post, last updated 2026-09-30, lists Continuous Integration among the modules available on Harness Free Plans | capture: sha256:f00c425b2af32c3f014d453156fbfb99340045fadaf317b98defc91b60ed37ce | quote: - [Continuous Integration](https://www.harness.io/products/continuous-integration?tag=true)
  - [7] 2026-11-02: the CI product page offers Harness Cloud on a free start with no credit card, which the CI documentation contradicts | capture: sha256:87fde00f584ee5ff3986c63ff153e27a1fac0589e6e411188a0b7d0dd28c3a4c | quote: Try Harness Software Delivery Agent free — no credit card. Full access to Test Intelligence, Build Intelligence, Docker Layer Caching, and Harness Cloud for continuous integration at scale.
  - [8] 2026-11-02: Flex Pricing, in limited availability, gives a Free account 1,000 HSUs a month and does not mention the 2,000 Harness Cloud credits | capture: sha256:3a4c77d784b9983e3256aadf88deb2385d668a702fe396c4d8d244c4a891faf8 | quote: Every Free account receives 1,000 free HSUs per month at no cost.
  - [1] 2026-11-04: 2000 credits a month on Free | capture: sha256:f51619de1354b58aed11152ce145a1692d450b12186e93402262c8b27926d5c9 | quote: Free plans receive 2000 free credits every month.
  - [2] 2026-11-04: Free plan pipeline timeout 2 hr | capture: sha256:bbaeb51077690c2381ec2d0b2f87fcc52ea551713a085e632710958588e826c6 | quote: | Pipeline timeout | 2 hr | 4 hr | 30 days | 35 days |
  - [3] 2026-11-04: card validation on Free | capture: sha256:aec8ac869f48a77375d04eac7424d6a36b3a2075795fdfb2da4f9a3a197ac778 | quote: Free plans require credit card validation to use Harness Cloud.
- sources:
  - [1] https://developer.harness.io/continuous-integration/troubleshooting-and-resources/ci-subscription-mgmt
  - [2] https://developer.harness.io/harness-platform/use-harness-platform/pipelines/pipeline-settings
  - [3] https://developer.harness.io/docs/continuous-integration/use-ci/set-up-build-infrastructure/use-harness-cloud-build-infrastructure/
  - [4] https://www.harness.io/pricing
  - [5] https://www.harness.io/products/continuous-integration/harness-cloud
  - [6] https://www.harness.io/blog/introducing-developer-360-pricing-by-harness
  - [7] https://www.harness.io/products/continuous-integration
  - [8] https://developer.harness.io/harness-ai/subscriptions-and-licenses/flex-pricing
