# Moonshot

> kimi.ai | Coding subscriptions, Inference; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kimi-2/ | JSON https://fshy.ajam.dev/api/v1/entity/kimi-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kimi For Coding (kimi.ai)

- `coding-subs/kimi-code-plan-global` | paid-only | evidence documented | binding write-gated | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://www.kimi.ai/code/
- free tier: No free coding tier stated on the captured page. Kimi Code is available on desktop, CLI and IDE plugins under paid Kimi Code Plans; the model-doc route on kimi.ai returned broker-exit-1. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: a Kimi account plus a paid Kimi Code Plan; the captured home page does not enumerate signup fields
- interface: rest, cli
- limits:
  - write-gated (binding): new models and 1M context require higher membership tiers [1]
- endpoint: https://api.kimi.ai/coding/v1
- tooling: Kimi Code Desktop, CLI and VS Code extension; third-party tools use OpenAI or Anthropic-compatible endpoints
- composes with: Kimi Code Plans are the scarce link; a paid membership gates the newest models and 1M context
- reliability: the dedicated models.html doc route on kimi.ai was refused (broker-exit-1) on multiple attempts; the kimi.com mirror was used for the model detail
- notes: Paid-only. The doc URL (models.html) returned broker-exit-1 on two attempts including an alternate path; the kimi.ai apex was captured. No price invented.
- evidence:
  - [1] 2026-11-18: Kimi Code is a subscription product available only in Kimi Code Plans | capture: sha256:bc13a8121d03fcd2dd1d49c2ba661286b40b846d12267dca2cdb411b28705802 | quote: Kimi Code is available in the following plans
- sources:
  - [1] https://www.kimi.ai/code/

## Moonshot AI

- `inference/moonshotai` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://platform.kimi.ai/docs/pricing/chat.md
- free tier: No free model-text allowance: 'Model inference on the Kimi API platform is billed on a pay-as-you-go basis, with no subscription plan'; file content extraction and file storage are 'temporarily free'. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and API key from the Kimi API Platform; no card or phone gate stated
- interface: rest
- limits:
  - volume-quota (binding): per-token billing; no free text tier [1]
- endpoint: https://api.moonshot.ai/v1
- tooling: OpenAI SDK and Anthropic SDK against api.moonshot.ai/v1
- composes with: no free text tier; only the file APIs are temporarily free
- reliability: K2 series models are not available to newly registered users from 2026-10-31 and retire end of December 2026
- notes: No free text allowance; the 'temporarily free' file APIs are not text inference.
- evidence:
  - [1] 2026-11-18: Kimi model inference is pay-as-you-go with no subscription plan | capture: sha256:0bede5aae7e2be18879d6cf5dcbc4c9705da06c54fddf33af669d2bf6ce5c7b6 | quote: Model inference on the Kimi API platform is billed on a pay-as-you-go basis, with no subscription plan.
- sources:
  - [1] https://platform.kimi.ai/docs/pricing/chat.md

## Moonshot Kimi API Platform international

- `inference/moonshot-kimi-api-international` | paid-only | evidence documented | binding write-gated | category inference API, prepaid pay-as-you-go | tier International platform, pay-as-you-go
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:38:01.693Z (live) | stale on 2026-12-04
- url https://platform.kimi.ai/docs/pricing/limits.md
- free tier: no free credit is stated for a registration outside mainland China. The API needs a recharge of at least USD 1 first, and a USD 5 voucher is granted once cumulative recharge reaches USD 5. The mainland RMB 15 new-user voucher is a separate offer on a separate platform; accounts and keys of the two platforms are independent | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: the USD 5 voucher is a purchase-matched bonus, not a free grant; whether the console grants any other credit at sign-up is unverified: behind a sign-up. One page names 'vouchers granted from new-user verification' that cannot be used for Kimi K3 without saying who receives them or how much
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: sign-up uses an emailed verification code or a Google account; using the API needs a prior top-up of at least USD 1. The help page lists WeChat Pay and Alipay QR payments for individual top-ups and the terms name a credit or debit card as a payment method; which methods the international top-up page accepts is unverified: behind a sign-up
- interface: rest
- limits:
  - write-gated (binding): a recharge of at least USD 1 is required before the API can be used; kimi-k3.1-pro is unlocked by a successful top-up (minimum USD 1) [1]
  - request-rate: Tier0 (USD 1 cumulative recharge): concurrency 1, 3 RPM, 500,000 TPM, 1,500,000 TPD; Tier1 (USD 10): concurrency 15, 100 RPM, 2,000,000 TPM, unlimited TPD [2]
  - volume-quota: USD 5 voucher once cumulative recharge reaches USD 5; vouchers do not count towards the cumulative recharge total [1]
- binding note: nothing is callable before a paid recharge of at least USD 1; the USD 5 voucher only matches paid recharge
- tooling: OpenAI-compatible REST at https://api.moonshot.ai/v1, with Chat Completions, Responses and an Anthropic-compatible Messages interface; a console Playground; a balance API
- composes with: top up USD 1 to unlock the API, then USD 5 cumulative for a USD 5 voucher; usage deducts half from cash and half from vouchers; the voucher does not count towards the rate-limit tier
- reliability: not assessed: no request was sent to the endpoint. A Tier0 account runs one request at a time
- evidence note: the USD 1 minimum, the USD 5 voucher, the tier table, the sign-in methods and the regional separation are quoted from the vendor's international docs; the console sign-up and top-up pages are behind a login and were not read, so any further sign-up grant and the accepted payment methods are unverified
- evidence:
  - [1] 2026-11-03: a recharge of at least USD 1 is required before the API can be used, and a USD 5 voucher follows once cumulative recharge reaches USD 5 | capture: sha256:03011d4aea7452d87c631f14ef791f7a9717371c384d7ac39452b9526fdf44db | quote: To prevent abuse, a minimum recharge of \$1 is required to start using the API; when your cumulative recharge reaches \$5, you receive a \$5 voucher.
  - [1] 2026-11-03: the voucher does not raise the rate-limit tier | capture: sha256:03011d4aea7452d87c631f14ef791f7a9717371c384d7ac39452b9526fdf44db | quote: Vouchers do not count towards the cumulative recharge total.
  - [2] 2026-11-03: the USD 1 tier allows concurrency 1, 3 RPM, 500,000 TPM and 1,500,000 TPD | capture: sha256:b658a72917a32c8f814b0a0d8716e3ff2658664a7185b85ef704790b10edc54d | quote: | Tier0 | $1 | 1 | 3 | 500,000 | 1,500,000 | 1 |
  - [2] 2026-11-03: the USD 10 tier allows concurrency 15, 100 RPM, 2,000,000 TPM and no daily token cap | capture: sha256:b658a72917a32c8f814b0a0d8716e3ff2658664a7185b85ef704790b10edc54d | quote: | Tier1 | $10 | 15 | 100 | 2,000,000 | Unlimited | 3 |
  - [3] 2026-11-03: sign-in on the international platform works with an emailed verification code | capture: sha256:1cfc19073ed9d8e060e314fbe75229c6e78cd7b746690ef1fe63328ce0ee8f6b | quote: Email sign-in: Receive a verification code at your email address.
  - [3] 2026-11-03: a Google account is the other sign-in method | capture: sha256:1cfc19073ed9d8e060e314fbe75229c6e78cd7b746690ef1fe63328ce0ee8f6b | quote: Sign in with Google: Authorize Kimi Platform through Google's OAuth sign-in flow.
  - [4] 2026-11-03: the flagship model needs a successful top-up of at least USD 1 | capture: sha256:29ccc9b807740dc7b6272cb50541e0828db640f7b3f995c68d5dfb3fbd52e520 | quote: Kimi K3.1 Pro is unlocked after a successful top-up (minimum \$1).
  - [4] 2026-11-03: platform.kimi.ai is the platform for registrations outside mainland China | capture: sha256:29ccc9b807740dc7b6272cb50541e0828db640f7b3f995c68d5dfb3fbd52e520 | quote: Kimi Open Platform provides separate regional platforms. For users outside mainland China, use platform.kimi.ai.
  - [4] 2026-11-03: an international account is separate from a mainland account, so a mainland voucher does not carry over | capture: sha256:29ccc9b807740dc7b6272cb50541e0828db640f7b3f995c68d5dfb3fbd52e520 | quote: Accounts and keys from different regional platforms are independent and cannot be mixed.
  - [4] 2026-11-03: the vendor points to a console Playground for testing before a top-up | capture: sha256:29ccc9b807740dc7b6272cb50541e0828db640f7b3f995c68d5dfb3fbd52e520 | quote: You can run a minimal test in the [Playground](https://platform.kimi.ai/playground) to confirm whether a model and prompt fit your scenario
  - [5] 2026-11-03: the help page lists WeChat Pay and Alipay QR payments for individual top-ups | capture: sha256:fef0f65d2e1cc760934c300c09368dadf91a6de16101a52bf1e5532c507c0e08 | quote: Online top-ups support WeChat Pay and Alipay QR code payments.
  - [6] 2026-11-03: the platform terms name a credit or debit card as a payment method | capture: sha256:4b25fe7e6307a8fad6738cb801e0195763ec5b862dcd310b6e94ca2cd2181e98 | quote: By providing a payment method (such as a credit or debit card), Customer authorizes Moonshot AI and its payment processors to charge such payment method on a recurring and/or usage-based basis
  - [6] 2026-11-03: an individual account needs the age of 18 or the local minimum age of consent | capture: sha256:4b25fe7e6307a8fad6738cb801e0195763ec5b862dcd310b6e94ca2cd2181e98 | quote: To use the Services as an individual, you must be at least 18 years old or the minimum age required by your country to consent to such use.
  - [7] 2026-11-03: usage is deducted half from cash balance and half from vouchers | capture: sha256:8dad4aea9bc88c1e871eaf876593de2b413d194f76cec49a899dafd363dd5906 | quote: Account usage is now deducted at a uniform ratio of 50% cash and 50% vouchers.
  - [8] 2026-11-03: kimi-k3.1-pro is priced at USD 2.00 per MTok input and USD 10.00 per MTok output | capture: sha256:dd97f99bb5e26b50410fc7ae66756d2ede29719067705c7dc8ace0b0706aebce | quote: | [kimi-k3.1-pro](https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart) | $2.00 / MTok | $10.00 / MTok | $0.20 / MTok | $2.00 / MTok | $4.00 / MTok |
  - [9] 2026-11-03: a new-user verification voucher, if granted, does not cover Kimi K3 | capture: sha256:c09501d5a9e27c58ae6cb6a0c88938e3cb4171177ad7034ab8aa3faec5a98680 | quote: Kimi K3 requires available balance in your account; vouchers granted from new-user verification cannot be used for Kimi K3.
- sources:
  - [1] https://platform.kimi.ai/docs/pricing/limits.md
  - [2] https://platform.kimi.ai/docs/pricing/limits
  - [3] https://platform.kimi.ai/docs/guide/account-security-and-sign-in.md
  - [4] https://platform.kimi.ai/docs/guide/troubleshooting.md
  - [5] https://platform.kimi.ai/docs/guide/account-and-payments.md
  - [6] https://platform.kimi.ai/docs/agreement/modeluse.md
  - [7] https://platform.kimi.ai/docs/platform-changelog.md
  - [8] https://platform.kimi.ai/docs/pricing/chat
  - [9] https://platform.kimi.ai/docs/guide/open-code.md
