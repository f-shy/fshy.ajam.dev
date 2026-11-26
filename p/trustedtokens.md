# TrustedTokens

> trustedtokens.eu | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trustedtokens/ | JSON https://fshy.ajam.dev/api/v1/entity/trustedtokens.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TrustedTokens

- `inference/trustedtokens` | fails-identity | evidence documented | binding write-gated | category inference gateway (sovereign EU)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://trustedtokens.eu/tryout
- free tier: Have a voucher code? Get instant, fully-approved access. Otherwise, sign up for a €10 trial — your account will need a quick manual approval before you can make API calls. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an email and either a voucher or a EUR 10 trial plus a quick manual approval before API access
- interface: rest
- limits:
  - write-gated (binding): EUR 10 trial; EUR 50 a month Starter plan with EUR 50 usage credit [1]
- endpoint: https://api.trustedtokens.eu/v1
- composes with: No standing free tier: the trial is paid and gated by manual approval, and the voucher path is invitation-like.
- reliability: API access does not turn on until a person approves the account
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: TrustedTokens requires a EUR 10 trial and manual approval, or a voucher, before API calls are allowed | capture: sha256:b0ed4a471cc75e52bda4f9504217c3669b0d762cc08c808d5dd9ed5e252f3117 | quote: Otherwise, sign up for a €10 trial — your account will need a quick manual approval before you can make API calls.
  - [2] 2026-11-18: TrustedTokens Starter plan costs EUR 50 per month and includes a EUR 50 usage credit per month | capture: sha256:5711a10894cdcf9ed272a6a0754f5b74c267e5cc49105e9025a5707514b0fd18 | quote: StarterIndividual developers €50/month - €50 usage credit / month
- sources:
  - [1] https://trustedtokens.eu/tryout
  - [2] https://trustedtokens.eu/pricing
