# Cohere trial keys

> cohere.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cohere/ | JSON https://fshy.ajam.dev/api/v1/entity/cohere.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cohere trial keys

- `compute/cohere-trial-keys` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:38:56.189Z (live) | stale on 2026-12-05
- url https://docs.cohere.com/docs/rate-limits
- free tier: A trial (evaluation) key is free but limited in usage: 'Trial keys (and prod keys on newer Chat model variants) are limited to 1,000 API calls a month.' Chat is 20 req / min per model on a trial key. Embed runs at 2,000 inputs / min on a trial key, the same as production, and Rerank at 10 req / min. The other trial limits are Audio Transcriptions 5 req / min, Embed (Images) 5 inputs / min, EmbedJob 5 req / min, Tokenize 100 req / min and Parse 500 req / min; anything not listed defaults to 500 req / min. The page does not say whether the 1,000 calls are counted per key or across the account. | unit: requests | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-monthly-request-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an account created on the sign-up page, which offers Continue with Google, Continue with Github, or an Email and Password; no phone or card field appears on that page. unverified: any step after sign-up
- interface: rest
- limits:
  - request-rate (binding): 1,000 calls a month binds at any real volume: at 20 rpm the whole month's allowance is spent in 50 minutes of traffic, so the limit rewards one call carrying many items over many calls carrying one. [1]
- limits note: 1,000 calls a month binds at any real volume: at 20 rpm the whole month's allowance is spent in 50 minutes of traffic, so the limit rewards one call carrying many items over many calls carrying one.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the asymmetry is the useful part: Embed on a trial key is 2,000 inputs a minute against a 1,000-calls-a-month cap, so embedding a corpus in batches of 96 inputs is 1,000 calls for 96,000 chunks, which is the only shape where 1,000 calls is not the binding number.
- reliability: no reliability event recorded
- notes: unverified: whether one counter is shared by Chat, Embed and Rerank, and whether it counts per key or per account; the first-party pages state only 'limited to 1,000 API calls a month' for trial keys.
- extras:
  - facets.class: capacity-shape
  - facets.free_tier_kind: recurring-monthly-request-allowance
- evidence:
  - [1] 2026-10-22: 'Trial keys (and prod keys on newer Chat model variants) are limited to 1,000 API calls a month', quoted
  - [1] 2026-10-22: trial rate limits: Chat 20 req/min per model, Embed 2,000 inputs/min, Rerank 10 req/min, quoted
  - [2] 2026-10-22: 'trial API key usage is free' and covers all models and APIs, quoted
  - [3] 2026-10-28: trial keys are limited to 1,000 API calls a month; the tables give the per-endpoint trial rates | capture: sha256:83e5955a25c6cefb2f523bce797ee99d2537766da1edea468d78cb3a39a6411d | quote: > Trial keys (and prod keys on newer Chat model variants) are limited to 1,000 API calls a month.
  - [4] 2026-10-28: the sign-up page offers Google, Github or email and password and shows no phone or card field | capture: sha256:1d581c2711a3574cf4ae7ae3f8a2783f5eeb69bfb741e149d8155f63435b57ce | quote: Continue with Google
  - [3] 2026-10-28: the Chat table gives 20 req / min on a trial key for every listed model | capture: sha256:83e5955a25c6cefb2f523bce797ee99d2537766da1edea468d78cb3a39a6411d | quote: | Command A | 20 req / min | 500 req / min |
  - [1] 2026-11-03: the monthly cap is stated for trial keys, with no statement of per-key or per-account counting or of a shared counter across endpoints | capture: sha256:83e5955a25c6cefb2f523bce797ee99d2537766da1edea468d78cb3a39a6411d | quote: Trial keys (and prod keys on newer Chat model variants) are limited to 1,000 API calls a month.
  - [5] 2026-11-03: an account gets a trial key automatically; the page does not say whether further trial keys have their own counter | capture: sha256:950def4bad1f77e94af203c33fc4f298222032bbb2e1dd820f8305466fc30ad3 | quote: When an account is created, we automatically create an Trial API key for you.
- sources:
  - [1] https://docs.cohere.com/docs/rate-limits
  - [2] https://docs.cohere.com/v2/docs/how-does-cohere-pricing-work
  - [3] https://docs.cohere.com/v2/docs/rate-limits
  - [4] https://dashboard.cohere.com/welcome/register
  - [5] https://cohere.com/pricing
