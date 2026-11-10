# StepFun Step

> stepfun.ai | Inference, Coding subscriptions; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stepfun/ | JSON https://fshy.ajam.dev/api/v1/entity/stepfun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StepFun Open Platform (platform.stepfun.ai)

- `inference/stepfun-open-platform` | trial-only | evidence documented | binding request-rate | category inference API, free preview models
- identity a placeholder: card and phone unknown | verified 2026-11-03T11:30:43.060Z (live) | stale on 2026-12-04
- url https://platform.stepfun.ai/
- free tier: No standing token allowance. Billing draws from free credit first and then from the paid balance, free credit can expire, and no credit amount is published on the pages read. The preview speech models stepaudio-3-realtime-preview and stepaudio-3-chat-preview are listed Free (limited time). Text reasoning is paid: step-3.5-flash is USD 0.10 per 1M cache-miss input and USD 0.30 per 1M output | unit: mixed | metered on: unstated | read on: 2026-10-28 | source: [1] | note: free-preview-models
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: unverified: the overseas documentation (platform.stepfun.ai) states individual accounts must complete identity verification first and names no document or country scope; the mainland sibling platform (platform.stepfun.com) documents an individual real-name check of the holder's name and ID card number with an Alipay face-recognition scan, and it is not stated that the overseas platform uses the same check
- interface: rest
- limits:
  - request-rate (binding): tier V0 for cumulative top-up under USD 15: concurrency 5, 100 RPM, 500,000 TPM; the tier rises only with cash top-ups, and vouchers do not count [1]
- binding note: rate tier follows cumulative cash top-up; an account with no top-up starts at the lowest tier
- tooling: not stated
- composes with: the limited-time free audio preview models are the only zero-priced rows; text reasoning models are paid per token
- reliability: text-to-image models step-2x-large and step-image-edit-2 were retired on October 10, 2026 and stopped serving requests
- evidence note: the free preview rows are read from the vendor pricing page; the platform terms say limited-time Trial Credits may be given to new users with validity set when issued, and no vendor page states an amount or expiry; the identity document of the overseas platform is unverified
- evidence:
  - [1] 2026-10-28: a speech chat preview model is listed Free (limited time) | capture: sha256:d09376206e90e63192fca3540bae3690e6d47dbbe70fc0fc480700cde3206877 | quote: | `stepaudio-3-chat-preview` | N/A | N/A | N/A | N/A | Free (limited time) |
  - [1] 2026-10-28: step-3.5-flash list price per 1M tokens in USD | capture: sha256:d09376206e90e63192fca3540bae3690e6d47dbbe70fc0fc480700cde3206877 | quote: | `step-3.5-flash` | 1M tokens | \$0.10 | \$0.02 | \$0.30 |
  - [1] 2026-10-28: individual accounts need identity verification before a rate tier is assigned | capture: sha256:d09376206e90e63192fca3540bae3690e6d47dbbe70fc0fc480700cde3206877 | quote: Individual accounts must complete identity verification first. Tiers are assigned by cumulative top-up amount:
  - [1] 2026-10-28: the lowest tier has concurrency 5, 100 RPM and 500,000 TPM | capture: sha256:d09376206e90e63192fca3540bae3690e6d47dbbe70fc0fc480700cde3206877 | quote: | V0 | Under \$15 | 5 | 100 | 500,000 |
  - [2] 2026-10-28: free credit is consumed before the paid balance and can expire | capture: sha256:14b45b030a9acee8a5347082b5d4d2da56dc178260279f39cb1e728bb1a23984 | quote: Fees are deducted as `tokens used × model unit price`, drawing from free credit first, then paid balance. Free credit can expire, so please use it promptly.
  - [3] 2026-11-03: the mainland sibling platform asks for the holder's name and ID card number | capture: sha256:1ad695d11cb40e1d6efdfbaf6cbb9ed0e5fc9ff2b37fe03bb9eef2bfd29be888 | quote: 在实名认证一行点击认证，选择个人实名认证，填写本人姓名和身份证号。
  - [4] 2026-11-03: the platform terms allow limited-time trial credits for new users, with no amount stated | capture: sha256:fe9a2ee80534d537cca7a398c89117a97d21cb30eeb340174456a76ae9fa8529 | quote: The Platform may from time to time provide limited-time Trial Credits to new users for service testing and evaluation.
  - [5] 2026-11-03: a user reported a USD 100 voucher at account creation; reported, not vendor-confirmed, and another user in the thread saw none | capture: sha256:3e3b45933eadee599ec34336f84d4cb0549a7a7d61725594b2e2d95b1533c839 | quote: 100$ free when you create the account, but limited to 10 requests/hour if you don't top up at least 15$
  - [6] 2026-11-03: the Step Plan free trial promotion ended on August 24, 2026 | capture: sha256:e17695af1fa2fc6d1b6dd83620ee960918ad5c25ce85830463471730ee32d021 | quote: Ends on August 24, 2026, at 23:59 UTC
  - [3] 2026-11-03: the mainland sibling platform completes verification by Alipay face recognition | capture: sha256:1ad695d11cb40e1d6efdfbaf6cbb9ed0e5fc9ff2b37fe03bb9eef2bfd29be888 | quote: 用支付宝扫码完成人脸识别，返回平台查看结果。
  - [7] 2026-11-03: on the mainland sibling platform free-plan users must complete real-name verification and every user before paying | capture: sha256:c961f11ceae808ad062f6f10551810f8040411256088c5a5b4728d063a72f90f | quote: 使用免费套餐的用户需要完成实名认证才能继续使用。所有用户在付费前都需要完成实名认证。
  - [1] 2026-11-03: the overseas platform requires identity verification of individual accounts and names no document | capture: sha256:6daaf65ec793230b80184ed145862ed6b20ff333b915296d14bfa1689efd45d8 | quote: Individual accounts must complete identity verification first. Tiers are assigned by cumulative top-up amount:
  - [1] 2026-11-03: the lowest tier has concurrency 5, 100 RPM and 500,000 TPM | capture: sha256:6daaf65ec793230b80184ed145862ed6b20ff333b915296d14bfa1689efd45d8 | quote: | V0 | Under \$15 | 5 | 100 | 500,000 |
- sources:
  - [1] https://platform.stepfun.ai/docs/en/guides/pricing/details
  - [2] https://platform.stepfun.ai/docs/en/guides/pricing/intro.md
  - [3] https://platform.stepfun.com/docs/zh/quickstart/real-name-verification
  - [4] https://platform.stepfun.ai/docs/en/agreement/userservice.md
  - [5] https://www.answeroverflow.com/m/1509957427003523202
  - [6] https://platform.stepfun.ai/step-plan/trial-rules
  - [7] https://platform.stepfun.com/docs/zh/faq/common-questions

## StepFun Step Plan

- `coding-subs/stepfun-step-plan` | paid-only | evidence documented | binding retention-clamped | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-10T01:55:59.601Z (live) | stale on 2026-12-11
- url https://platform.stepfun.ai/docs/en/step-plan/overview.md
- price parsed USD 6.99/mo
- free tier: no free tier. Four paid tiers: Flash Mini 400M Credits at USD 6.99 a month, Flash Plus 1,600M at USD 9.99, Flash Pro 8,000M at USD 29, Flash Max 40,000M at USD 99. Credits convert at approximately USD 1 = 7M Credits | unit: credits | metered on: request-count | read on: 2026-10-22 | source: [1] | note: the allowance is denominated in Credits, and the page states the conversion.
- per-object cap: not applicable
- retention: monthly Credits are cleared at the end of the month and do not roll over; booster-pack Credits expire on their own 30-day cycle | days: 30 | source: [1]
- egress: not applicable | metered: no
- identity: card | detail: registration takes an email address with an emailed verification code, or a Google account; the platform sign-in form offers 'Continue with Google' and 'Email verification code login', and a phone number is not required. There is no free route: use needs a paid subscription, and the checkout offers 'Pay with Stripe' (credit or debit card; the Step Plan page FAQ names Visa and Mastercard, the console subscription page FAQ names Alipay, UnionPay, Visa and Mastercard, plus corporate bank transfer for enterprises) or 'Pay with balance' (the account balance, topped up by credit or debit card). Whether the checkout asks for a billing address, a country or an identity check: unverified: behind a sign-up
- interface: rest, cli
- limits:
  - request-rate: no time-window or request-frequency limit; the page states Step Plan is not subject to the platform's tiered RPM and TPM limits, and usage is governed by the monthly Credit allowance of the subscribed tier [1]
  - retention-clamped (binding): monthly Credits are cleared at the end of the month and do not roll over; the full month's Credits are issued at once on subscribing [1]
- limits note: booster packs are available to active subscribers only and run on their own 30-day cycle: Small USD 6.99 for 400M Credits, Large USD 9.99 for 1,600M
- binding note: the monthly clearance binds before any request rate does, because there is no request rate to bind: an unused allowance is lost at month end rather than carried
- interface detail: two documented Base URLs: https://api.stepfun.ai/step_plan for the Claude Code and Anthropic SDK shape, and https://api.stepfun.ai/step_plan/v1 for OpenAI SDK Chat Completions. The page states these are client configuration URLs and not full request URLs
- tooling: Claude Code, the Anthropic SDK, the OpenAI SDK, Trae, Cursor and OpenClaw are named on the page as supported clients
- composes with: pairs with any Anthropic-shaped or OpenAI-shaped agent; the monthly Credit allowance is the scarce link, and it is spent by the Step Plan Base URL rather than by the standard API channel, which has its own separate quota
- reliability: on 2026-10-30 the Step Plan page and the console subscription page showed every tier (Mini, Plus, Pro, Max) as 'Out of stock'; the vendor's notice states that Plan purchase quotas are released in limited daily batches adjusted to real-time service capacity, and that new free trials are closed. A subscription can be unavailable to buy on a given day
- notes: This record carried verdict: trial-only and confidence: unverified until 2026-10-22T04:14Z, on a 396-byte shell from www.stepfun.com/pricing. At USD 9.99 for 1,600M Credits, or about USD 228.6 of model usage, this is the cheapest plan in the market per unit of work and the strongest counter-example to the topic's 'nothing under USD 20 carries a usable allowance' conclusion.
- evidence note: the four tiers, the Credit allowances, the conversion rate, the two Base URLs and the no-rate-limit statement are all quoted from the vendor's own documentation page, read 2026-10-22 at 200 with 9444 bytes. No subscription was bought, so the allowance is the vendor's number and not a measurement.
- extras:
  - monthly_usd: 6.99
- evidence:
  - [1] 2026-10-22: the four-tier ladder with monthly, quarterly and yearly prices: Flash Mini 400M Credits USD 6.99 / 18.99 / 69.99, Flash Plus 1,600M USD 9.99 / 26.99 / 95.99, Flash Pro 8,000M USD 29 / 79 / 289, Flash Max 40,000M USD 99 / 269 / 989; 'Credits convert to payment at approximately USD 1 = 7M Credits'; 'no time-window or request-frequency limits'; and the two Base URLs
  - [2] 2026-10-22: a 2262-byte shell at HTTP 200 with no plan name and no price. This is the route the previous record used, and it is a marketing page that does not carry the documentation's ladder. It is a route note, not the finding
  - [3] 2026-10-30: registration takes an email address or a Google account; no phone number is named for account creation | capture: sha256:4f8803613e409dde83114c0e39910a3eb4f357a1a54fa2fbdf7d8e96c1f8f40a | quote: When you use our Services, you may create an account with your email address or Google Account to complete the registration and become our user.
  - [4] 2026-10-30: the platform sign-in form (English strings of the site bundle) offers Google sign-in or an email verification code, with no phone field | capture: sha256:39c69d5b3143d73a3897c1cb9ee7d09ce242c659246e0ef36c3d44dca43bcc5c | quote: "google-login":"Continue with Google","email-verification-code-login":"Email verification code login","please-enter-the-email":"Please enter the email"
  - [3] 2026-10-30: account verification at registration is a verification code sent to the email address | capture: sha256:4f8803613e409dde83114c0e39910a3eb4f357a1a54fa2fbdf7d8e96c1f8f40a | quote: We may verify your identity by sending a verification code.
  - [5] 2026-10-30: the paid subscription is activated by registering an account, choosing a plan and completing payment | capture: sha256:5e5aa0ff953e663efaae813a63ca10a43e497e1c161ba21c017b1aafb94ff9fc | quote: By registering and logging into your platform account, selecting a specific plan on the subscription page, and completing payment, you are deemed to have activated the relevant paid…
  - [6] 2026-10-30: the Step Plan checkout's Stripe channel takes a credit or debit card | capture: sha256:30b6db94f610b890dee82d379ec17adc841621a1759a48f6ffa0760d4ecaa415 | quote: Secure credit and debit card checkout via Stripe.
  - [6] 2026-10-30: the Step Plan checkout's second channel pays from the account balance | capture: sha256:30b6db94f610b890dee82d379ec17adc841621a1759a48f6ffa0760d4ecaa415 | quote: Your available balance will be used for this payment.
  - [7] 2026-10-30: the documentation names two payment routes for a subscription: Stripe, or the account balance | capture: sha256:0171869dc8e3a3da509347c75d4011d66c650576e3d393d9ef8c1c7cb8cc5677 | quote: Subscriptions can be paid through Stripe, or redeemed using your account balance (top-up funds).
  - [8] 2026-10-30: the Step Plan page FAQ (English) names Visa and Mastercard credit cards, and corporate bank transfer for enterprises | capture: sha256:fb3ec002d80a878bfe969021c54a34d591448801397c7e0dfb994993c3fe20d3 | quote: answer:"We accept Credit Cards (Visa, Mastercard). Enterprise users can also choose corporate bank transfers."
  - [9] 2026-10-30: the console subscription page FAQ names Alipay, UnionPay, Visa and Mastercard, and corporate bank transfer for enterprises | capture: sha256:d5881172ea7fb46311056b81596197d0a0ecd9ccb55c6717f955acb3f458ec84 | quote: We accept major payment methods including Alipay, UnionPay, and Credit Cards (Visa, Mastercard). Enterprise users can also choose corporate bank transfers.
  - [4] 2026-10-30: an account-balance top-up is paid by credit or debit card | capture: sha256:39c69d5b3143d73a3897c1cb9ee7d09ce242c659246e0ef36c3d44dca43bcc5c | quote: "please-use-your-credit-card-or-debit-card-to-complete-payment":"Please use your credit card or debit card to complete payment"
  - [10] 2026-10-30: the rendered Step Plan page showed each of the four plan cards as Out of stock on 2026-10-30 | capture: sha256:109955a38e5a2a31592d7203c1173c772c83ba651871be76e17a4ecd08a2306e | quote: Out of stock
  - [8] 2026-10-30: the Step Plan page notice states purchase quotas are released in limited daily batches and new free trials are closed | capture: sha256:fb3ec002d80a878bfe969021c54a34d591448801397c7e0dfb994993c3fe20d3 | quote: we are closing the channel for claiming new free trials and releasing Plan purchase quotas in limited daily batches.
  - [8] 2026-10-30: the daily purchase quota follows service capacity | capture: sha256:fb3ec002d80a878bfe969021c54a34d591448801397c7e0dfb994993c3fe20d3 | quote: These quotas may be adjusted dynamically based on real-time service capacity.
  - [10] 2026-10-30: a second rendering of the Step Plan page on 2026-10-30 also showed all four plan cards as Out of stock | capture: sha256:6bca8ffe386d7cd15480f2e5e8eedef356530ab427b6f8e6dccad3fbea857109 | quote: Out of stock
  - [9] 2026-10-30: the console subscription page (Compare Plans) showed Mini, Plus, Pro and Max as Out of stock on 2026-10-30 | capture: sha256:d5881172ea7fb46311056b81596197d0a0ecd9ccb55c6717f955acb3f458ec84 | quote: Out of stock
  - [10] 2026-10-30: the free-trial channel is closed; the only offer is the paid four-tier ladder, so no free allowance exists | capture: sha256:109955a38e5a2a31592d7203c1173c772c83ba651871be76e17a4ecd08a2306e | quote: To prioritize the experience of our paying subscribers given current service capacity, we are closing the channel for claiming new free trials.
  - [7] 2026-10-30: the allowance is denominated in one unit, Credits | capture: sha256:0171869dc8e3a3da509347c75d4011d66c650576e3d393d9ef8c1c7cb8cc5677 | quote: Step Plan uses Credits as its unified billing unit.
  - [7] 2026-10-30: the four-tier ladder, Credit allowances, conversion rate, month-end clearance, booster packs, no-RPM statement and the two Base URLs are unchanged on 2026-10-30 | capture: sha256:0171869dc8e3a3da509347c75d4011d66c650576e3d393d9ef8c1c7cb8cc5677 | quote: | Flash Plus | Daily productivity | 1,600M | \$9.99 | \$26.99 | \$95.99 |
  - [1] 2026-11-10: the page states the plan table prices Flash Mini at USD 6.99 a month | capture: sha256:f34b855cfb7a52579f5e6faf2fb4479aa86d53591e2e0800c4e264e18b39ddcd | quote: | Flash Mini | Getting started with AI | 400M | \$6.99
- sources:
  - [1] https://platform.stepfun.ai/docs/en/step-plan/overview.md
  - [2] https://www.stepfun.com/pricing
  - [3] https://platform.stepfun.ai/docs/en/agreement/userprivacy.md
  - [4] https://platform.stepfun.ai/_next/static/chunks/app/layout-41354ddad23de804.js
  - [5] https://platform.stepfun.ai/docs/en/step-plan/paid-service-agreement.md
  - [6] https://platform.stepfun.ai/_next/static/chunks/8979-74ebcf993cc3dae7.js
  - [7] https://platform.stepfun.ai/docs/en/step-plan/overview
  - [8] https://platform.stepfun.ai/_next/static/chunks/5412-f823cf7b36c5d1c8.js
  - [9] https://platform.stepfun.ai/plan-subscribe
  - [10] https://platform.stepfun.ai/step-plan
