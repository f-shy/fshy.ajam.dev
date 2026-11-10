# Token Harbor

> tokenharbor.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tokenharbor/ | JSON https://fshy.ajam.dev/api/v1/entity/tokenharbor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Token Harbor

- `inference/token-harbor` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway, free plan with a rolling 7-day allowance on :free model ids
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://tokenharbor.ai/pricing
- free tier: a $0 Free plan with a free allowance that resets on a rolling 7-day period, spent on :free model ids (DeepSeek V4.1 Flash, MiMo V2.6 Flash, TH-Rudder at the time read); the allowance amount is not printed on the pages read | unit: mixed | metered on: unstated | read on: 2026-11-04 | source: [1] | note: TH-Rudder text chat in Webchat is free and unlimited during a limited-time campaign and does not draw on the allowance; the allowance size is unverified: not printed
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the sign-in page offers Continue with GitHub and Continue with Google; the pricing page says no card is required for the Free plan
- interface: rest
- limits:
  - volume-quota (binding): free allowance resetting on a rolling 7-day period; the amount is not printed on the pages read; unverified: behind a sign-up [1]
  - request-rate: unverified: no free-plan request rate is printed on the pages read [2]
- binding note: the rolling 7-day free allowance is the stated bound; its size is unpublished
- tooling: OpenAI-compatible client; free routes carry an explicit :free model id
- composes with: Free plan, then wallet top-ups per token, or an optional Pass from $1.99 a month
- reliability: free models are promotional and the set changes as models are added or retired; free-route conversations may be read by staff and used by the serving providers
- notes: the allowance amount needs the dashboard, which is behind a sign-up
- evidence:
  - [1] 2026-11-04: the free allowance resets on a rolling 7-day period | capture: sha256:5f4a90d2e133a69f267690ca6ffb89c461500de64b50488c279fa14a76593d0e | quote: Resets on a rolling 7-day period
  - [1] 2026-11-04: the Free plan needs no card | capture: sha256:5f4a90d2e133a69f267690ca6ffb89c461500de64b50488c279fa14a76593d0e | quote: No card required.
  - [2] 2026-11-04: free models are promotional | capture: sha256:c5bc035959d8c3f60ceddc27ec0a1a7a9cfa831b4eb3ea01678dc68dcaba7a3b | quote: Yes. Token Harbor may provide free access to selected frontier models as part of promotional programs and community initiatives.
  - [3] 2026-11-04: free model ids draw on the free allowance and are never billed | capture: sha256:f7ee59688b7dcd00fb6e986d79b9bc3e7f542ac602509f95f082d313d2fa94df | quote: Each :free model ID uses Token Harbor's free allowance and is never billed
  - [4] 2026-11-04: the sign-in page offers GitHub sign-in | capture: sha256:31a93f3ca257c26356b2a04e55aea3f4d5b291c3f9fc481447109ee586a6c79e | quote: Continue with GitHub
  - [4] 2026-11-04: the sign-in page offers Google sign-in | capture: sha256:31a93f3ca257c26356b2a04e55aea3f4d5b291c3f9fc481447109ee586a6c79e | quote: Continue with Google
  - [1] 2026-11-04: the allowance resets on a rolling 7-day period; its size is not on the public pages | capture: sha256:5f4a90d2e133a69f267690ca6ffb89c461500de64b50488c279fa14a76593d0e | quote: Resets on a rolling 7-day period
- sources:
  - [1] https://tokenharbor.ai/pricing
  - [2] https://tokenharbor.ai/faq
  - [3] https://tokenharbor.ai/blog/3-best-free-ai-apis-for-coding-and-agents-in-2026
  - [4] https://tokenharbor.ai/signup
