# BytePlus AI

> byteplus.com | Inference, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/byteplus/ | JSON https://fshy.ajam.dev/api/v1/entity/byteplus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BytePlus ModelArk free inference quota

- `inference/byteplus-modelark-free-tokens` | trial-only | evidence documented | binding volume-quota | category inference API, one-time free tokens
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-03T11:30:35.839Z (live) | stale on 2026-12-04
- url https://ai.byteplus.com/ark/region:ap-southeast-1/docs/free-inference-quota
- free tier: A one-time free inference quota per model, 500K tokens per model, granted to new users on registration. It is calculated separately for each model and shared under the primary account, offsets pay-as-you-go online inference tokens only, and in Free Tokens Only mode the service is suspended near the quota so no fee accrues. The activity page states the quota does not expire but is subject to change | unit: tokens | metered on: request-count | read on: 2026-10-28 | source: [1] | note: one-time-quota
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: The sign-up form asks for email, username and password, or Google or GitHub sign-in. The quota page says to register and authenticate as a BytePlus user; the help centre says individual accounts reach a limited subset of products, business accounts need a business license and company details, and a valid credit card may be required to activate pay-as-you-go models; Free Tokens Only mode is open to identity-verified personal accounts and enterprise accounts; the campaign terms require enterprise information submission and judge uniqueness from email verification, ID documents, domain names, mobile numbers, devices and IP addresses. unverified: whether a card, phone number or identity verification is required before the quota is granted, which only an account shows
- interface: rest
- limits:
  - volume-quota (binding): 500K tokens per model, one-time; offsets online pay-as-you-go inference only, not batch inference, plugins, knowledge bases or context-cache storage [1]
  - request-rate: Model-list maximums per primary account (theoretical, subject to platform load; all endpoints of a base model share them), for the models the pricing page lists at 500k tokens: Seed 2.0 lite, mini, code-preview and pro 30K RPM and 1500K TPM; DeepSeek V4 pro and flash 260425 versions 15K RPM and 1500K TPM; DeepSeek V4 pro-ga and flash-ga 0.5K RPM and 1000K TPM; Seed 2.1 turbo 0.5K RPM and 1000K TPM (its free-quota row reads 500 tokens); retiring Seed 1.8 30K RPM and 1500K TPM, Seed 1.6 and Seed 1.6 flash 15K RPM and 800K TPM, DeepSeek V3.2 15K RPM and 1500K TPM. Skylark-pro has no row on the model list; which model version carries the quota is not stated [1]
- binding note: the per-model 500K token quota is the only stated cap
- tooling: not stated
- composes with: each model carries its own quota, so one account holds several separate pools; Free Tokens Only mode stops service at the quota and cannot accrue a charge
- reliability: a separate Data Collaboration Rewards Campaign advertising 5M tokens daily per model behind real-name verification: the campaign page calls it an ongoing benefit while the activity page carries an earlier stated end date; daily resource pack distribution for 18 models, among them Seed 2.0 pro, lite and mini, Seed 1.6, 1.8, DeepSeek V3.2 and V4 pro and flash GA, ended on October 8, 2026
- notes: the quota is per model and per primary account; the free-trial page lists DeepSeek V3.1 and GPT-OSS-120B among the 500K-token models
- evidence note: quota size and scope are documented; the identity requirement is unverified beyond the quoted terms
- evidence:
  - [1] 2026-10-28: new users receive a free inference trial quota | capture: sha256:bdd3ccfbd3d7380bddce592db7a52659680f90b35e99c31e30c73181221750a8 | quote: ModelArk offers new users a free inference trial quota, allowing them to get started at no cost.
  - [1] 2026-10-28: Free Tokens Only mode consumes only the 500k token platform quota | capture: sha256:bdd3ccfbd3d7380bddce592db7a52659680f90b35e99c31e30c73181221750a8 | quote: In the Free Tokens Only Mode, when you call the inference API, you only consume the 500k token free quota presented by the platform.
  - [1] 2026-10-28: the quota is per model and shared under the primary account | capture: sha256:bdd3ccfbd3d7380bddce592db7a52659680f90b35e99c31e30c73181221750a8 | quote: Free inference quota is calculated separately for different models and shared under the primary account.
  - [2] 2026-10-28: the free-trial page lists 500K free tokens per model for DeepSeek V3.1 and GPT-OSS-120B | capture: sha256:926bfb9f1279297e72305b11505e59f6df2d7eb1efbc7764ce26e0b173a1bf0f | quote: 500K free tokens per model
  - [2] 2026-10-28: the activity page states the free quota does not expire but can change | capture: sha256:926bfb9f1279297e72305b11505e59f6df2d7eb1efbc7764ce26e0b173a1bf0f | quote: The free quota does not expire, but is subject to change. Available for eligible customers.
  - [3] 2026-10-28: the free-token campaign terms require account registration and enterprise information submission | capture: sha256:44f4fe6fe386373ffb15ca8541a1b999b9c0c0afe823c873cab0520333f52dac | quote: Eligibility for this Campaign requires the completion of BytePlus account registration and enterprise information submission as required by BytePlus.
  - [2] 2026-10-28: a separate daily-token campaign behind corporate verification had a stated end date of March 31, 2026 | capture: sha256:926bfb9f1279297e72305b11505e59f6df2d7eb1efbc7764ce26e0b173a1bf0f | quote: Earn up to 5M tokens daily per model! Join the Data Collaboration Rewards Campaign by March 31, 2026. Complete corporate verification to claim.
  - [4] 2026-11-03: seed-2-0-lite lists Max RPM 30K and Max TPM 1500K | capture: sha256:4452dcc8ba21795da9f0b8abb1d3c4fae69e9ceb0246d095f5114331d29c77fd | quote: | ^^ | [`seed-2-0-lite-260428`](https://ai.byteplus.com/ark/region:ap-southeast-1/model/detail?Id=seed-2-0-lite) | 256K | 224K | 128K | 128K | 30K | 1500K |
  - [4] 2026-11-03: deepseek-v4-pro 260425 lists 15K RPM and 1500K TPM | capture: sha256:4452dcc8ba21795da9f0b8abb1d3c4fae69e9ceb0246d095f5114331d29c77fd | quote: | ^^ | [`deepseek-v4-pro-260425`](https://ai.byteplus.com/ark/region:ap-southeast-1/model/detail?Id=deepseek-v4-pro) | 1024K | 1024K | 384K | 128K | 15K | 1500K |
  - [4] 2026-11-03: deepseek-v4-pro-ga lists 0.5K RPM and 1000K TPM | capture: sha256:4452dcc8ba21795da9f0b8abb1d3c4fae69e9ceb0246d095f5114331d29c77fd | quote: | ^^ | [`deepseek-v4-pro-ga-260813`](https://ai.byteplus.com/ark/region:ap-southeast-1/model/detail?Id=deepseek-v4-pro-ga) | 1024K | 1024K | 384K | 128K | 0.5K | 1000K |
  - [4] 2026-11-03: dola-seed-2-1-turbo lists 0.5K RPM and 1000K TPM | capture: sha256:4452dcc8ba21795da9f0b8abb1d3c4fae69e9ceb0246d095f5114331d29c77fd | quote: | ByteDance | [`dola-seed-2-1-turbo-260628`](https://ai.byteplus.com/ark/region:ap-southeast-1/model/detail?Id=dola-seed-2-1-turbo) | 256K | 256K | 256K | 256K | 0.5K | 1000K |
  - [4] 2026-11-03: retiring seed-1-6 lists 15K RPM (800K TPM on the next row) | capture: sha256:4452dcc8ba21795da9f0b8abb1d3c4fae69e9ceb0246d095f5114331d29c77fd | quote: | [`seed-1-6-250915`](https://ai.byteplus.com/ark/region:ap-southeast-1/model/detail?Id=seed-1-6) | `dola-seed-2-0-lite-260428` | * Deep reasoning | * Context: 256K | * Max RPM: 15K | \
  - [4] 2026-11-03: retiring deepseek-v3-2 lists 15K RPM (1500K TPM on the next row) | capture: sha256:4452dcc8ba21795da9f0b8abb1d3c4fae69e9ceb0246d095f5114331d29c77fd | quote: | [`deepseek-v3-2-251201`](https://ai.byteplus.com/ark/region:ap-southeast-1/model/detail?Id=deepseek-v3-2) | `deepseek-v4-flash-ga-260731` | * Deep reasoning | * Context: 128K | * Max RPM: 15K | \
  - [4] 2026-11-03: the listed rates are theoretical maxima that vary with platform load | capture: sha256:4452dcc8ba21795da9f0b8abb1d3c4fae69e9ceb0246d095f5114331d29c77fd | quote: The rate limits in this document are theoretical maximum values. Actual limits depend on platform load and the invocation method.
  - [5] 2026-11-03: the pricing page lists DeepSeek-V4-pro at 500k free tokens | capture: sha256:0c21ca3ab362ae20e289f20c844404a451e6a89aae477ce7db6b0c6f68561e42 | quote: | DeepSeek-V4-pro | 500k tokens |
  - [5] 2026-11-03: the pricing page lists Dola-Seed-2.1-turbo free quota as 500 tokens | capture: sha256:0c21ca3ab362ae20e289f20c844404a451e6a89aae477ce7db6b0c6f68561e42 | quote: | Dola-Seed-2.1-turbo | 500 tokens |
  - [5] 2026-11-03: Skylark-pro is listed at 500k free tokens | capture: sha256:0c21ca3ab362ae20e289f20c844404a451e6a89aae477ce7db6b0c6f68561e42 | quote: | Skylark-pro | 500k tokens |
  - [6] 2026-11-03: the sign-up form lists email, username and password fields | capture: sha256:7f72d1d5ca43ca8b6adcd6fdb67d750770aada74cc264d4dc212fff8bb6555bc | quote: Email Username Password
  - [6] 2026-11-03: the sign-up form offers Google sign-in | capture: sha256:7f72d1d5ca43ca8b6adcd6fdb67d750770aada74cc264d4dc212fff8bb6555bc | quote: Continue with Google
  - [1] 2026-11-03: the quota page says to register and authenticate as a BytePlus user | capture: sha256:bdd3ccfbd3d7380bddce592db7a52659680f90b35e99c31e30c73181221750a8 | quote: [Register and authenticate](https://console.byteplus.com/auth/signup) as a BytePlus user.
  - [7] 2026-11-03: Free Tokens Only mode is open to identity-verified personal and enterprise accounts | capture: sha256:f83a88050792368328ac696be5582be26c01789e3ca5825963fac1a483dae9f8 | quote: Accounts that have not activated model services and have never enabled or disabled Free Tokens Only mode (including both identity-verified personal accounts and enterprise accounts) are eligible to enable this mode.
  - [8] 2026-11-03: business accounts need a business license and company details | capture: sha256:6d4001c206c95c399caca3a7573476e20df7774b8fa77616a2dffc5db77f0b22 | quote: Business accounts typically need to provide a valid business license and company details, while accepted verification methods and required documents depend on your account type and region.
  - [9] 2026-11-03: individual accounts reach a limited subset of products | capture: sha256:127bb0b9b3112df454f3a61be1cb7b557e68221c1b30e7bd0efc41df47ef4d60 | quote: BytePlus offers two account types: individual accounts, which can access a limited subset of products, and business (enterprise) accounts, which can order the full product catalog and are required for most cloud services.
  - [10] 2026-11-03: a valid credit card may be required to activate pay-as-you-go models | capture: sha256:dadb5c4e65ef35ad896d0c4d0b29fe10ec7b50013f89413de7f31c12ca4a124b | quote: Some payment methods (for example, certain wallet or PayPal balances) cannot activate pay-as-you-go models, so a valid credit card may be required.
  - [3] 2026-11-03: the campaign terms require enterprise information submission | capture: sha256:44f4fe6fe386373ffb15ca8541a1b999b9c0c0afe823c873cab0520333f52dac | quote: Eligibility for this Campaign requires the completion of BytePlus account registration and enterprise information submission as required by BytePlus.
  - [11] 2026-11-03: daily distribution for 18 models ended on October 8, 2026 | capture: sha256:b3f1abf22b24caef90894dfc28e28c7fc69fb9eef198342e3e289febd30d5579 | quote: Starting October 8, 2026, daily resource pack distribution for the 18 models listed below will end as they exit the ModelArk Collaboration Reward Program.
  - [11] 2026-11-03: the campaign page calls the 5M daily tokens an ongoing benefit | capture: sha256:b3f1abf22b24caef90894dfc28e28c7fc69fb9eef198342e3e289febd30d5579 | quote: > Ongoing Benefit: Enjoy 5,000,000 tokens free every day!
  - [11] 2026-11-03: the campaign requires real-name authentication | capture: sha256:b3f1abf22b24caef90894dfc28e28c7fc69fb9eef198342e3e289febd30d5579 | quote: * Step 1: You can go to the [BytePlus ModelArk Model Activation Page](https://ai.byteplus.com/ark/region:ap-southeast-1/openManagement?LLM=%7B%7D&advancedActiveKey=modeland) click "Verify Now" to enter the "Real Name Verification" page to complete real-name authentication.
  - [2] 2026-11-03: the activity page still states March 31, 2026 for the campaign | capture: sha256:97dce388ebef556bae0e72006e56382efe0f6addc1e9261c439b41a06e406b60 | quote: Earn up to 5M tokens daily per model! Join the Data Collaboration Rewards Campaign by March 31, 2026. Complete corporate verification to claim.
  - [1] 2026-11-03: the quota is per model and shared under the primary account | capture: sha256:bdd3ccfbd3d7380bddce592db7a52659680f90b35e99c31e30c73181221750a8 | quote: Free inference quota is calculated separately for different models and shared under the primary account.
- sources:
  - [1] https://ai.byteplus.com/ark/region:ap-southeast-1/docs/free-inference-quota
  - [2] https://www.byteplus.com/en/activity/free
  - [3] https://docs.byteplus.com/en/docs/legal/termsandconditions_modelark_free-token_campaign
  - [4] https://ai.byteplus.com/ark/region:ap-southeast-1/docs/model-list
  - [5] https://www.byteplus.com/en/product/modelark/pricing
  - [6] https://console.byteplus.com/auth/signup
  - [7] https://ai.byteplus.com/ark/region:ap-southeast-1/docs/free-tokens-only-mode
  - [8] https://ai.byteplus.com/en/help/article/what-identity-verification-real-name-kyc-is-required-and-what-documents-do-i-need
  - [9] https://ai.byteplus.com/en/help/article/what-is-the-difference-between-individual-and-business-accounts-and-can-i-change-the-type-after-registration
  - [10] https://ai.byteplus.com/en/help/article/why-cant-i-bind-my-credit-card-and-can-a-card-be-unbound-or-moved-to-another-account
  - [11] https://ai.byteplus.com/ark/region:ap-southeast-1/docs/collaboration-reward-program

## BytePlus AI Cloud

- `compute/byteplus-ai-cloud` | paid-only | evidence reported | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.byteplus.com/en/solutions/ai-cloud-native-sandbox
- free tier: Serverless microVM sandboxes that the vendor says start in under 150 ms, scale to tens of thousands created concurrently and to millions of vCPUs, support stateful long-running sandboxes, ship preconfigured templates, and bill at millisecond granularity with no charge while nothing is executing. Templates, large-scale image distribution, arbitrary specifications and MCP, API and SDK access are listed. No free tier is published. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: unverified: no page stating the signup requirement was read; the record's evidence covers the sandbox mechanics (sub-150 ms starts, millisecond billing with no charge while idle, MCP/API/SDK access), a third-party rate of USD 0.0351 per vCPU-hour and USD 0.0081 per GiB-hour, and a BytePlus billing page that returned only its navigation shell. Whether a personal account can create a sandbox at all was not established.
- interface: rest
- limits:
  - write-gated (binding): The rate card and the signup gate are both behind an account: the public documentation renders as a script shell, so the only published numbers are third-party, and whether a personal account can create a sandbox at all was not established. [1]
- limits note: The rate card and the signup gate are both behind an account: the public documentation renders as a script shell, so the only published numbers are third-party, and whether a personal account can create a sandbox at all was not established.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A microVM that bills only while executing is the right shape for evaluation fan-out, where a thousand short sandboxes each live a few seconds; it is the wrong shape for a service that must stay up, because the published selling point is that idle costs nothing precisely by not being a persistent host.
- reliability: no reliability event recorded
- notes: Routes tried: the product solution page (read, product facts only), docs.byteplus.com/en/docs/faas/Billing_overview (navigation shell, no table), docs.byteplus.com/en/docs/faas/Overview_of_cloud_sandbox (same shell), and a broad search that returned only third-party comparison tables. Identity is left null rather than guessed: BytePlus sells to enterprises, and whether a personal account can top up without a company was not established. This is the one provider where the door is more likely to be the finding than the price.
- extras:
  - facets.class: regional-sandbox-unpriced
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: 'sandboxes can start within 150ms and can be created concurrently at a scale of tens of thousands'; 'up to millions of vCPUs'; 'millisecond-level billing with no charges when not executing'; each sandbox is a microVM; MCP, API and SDK access
  - [2] 2026-10-22: a third-party comparison lists USD 0.0351 per vCPU-hour and USD 0.0081 per GiB-hour with no free tier, which is a claim about a third party and not a reading of BytePlus's own rate card
  - [3] 2026-10-22: the billing overview page returns only its navigation shell with no rate table, so the vendor's own numbers could not be read
- sources:
  - [1] https://www.byteplus.com/en/solutions/ai-cloud-native-sandbox
  - [2] https://boxyard.dev/providers/byteplus-cloud-sandbox
  - [3] https://docs.byteplus.com/en/docs/faas/Billing_overview
