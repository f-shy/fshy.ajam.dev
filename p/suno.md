# Suno

> suno.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/suno/ | JSON https://fshy.ajam.dev/api/v1/entity/suno.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Suno

- `compute/suno` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://suno.com/pricing
- free tier: Free plan at USD 0: the vendor's own help centre states 'The Free plan offers 50 credits that replenish daily. This is enough to make 10 songs per day', and the site FAQ repeats 'create up to 10 songs a day, no credit card required'. The plan comparison limits the free row to 'Best free model (v6-mini)' with '4 in a Shared queue' concurrent generations, no add-on credits, and no commercial rights. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-daily-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card and no payment method: the site FAQ states the free plan lets you 'create up to 10 songs a day, no credit card required', so no hold exists. The evidence does not say which identifier the account is created with, so whether an email alone suffices is not stated; debit and prepaid acceptance are not stated
- interface: unknown
- limits:
  - request-rate (binding): 50 credits a day that expire the same day: 'Credits included in subscriptions do not carry over from day to day or month to month', so 10 short songs is the ceiling and a 100-track project takes ten days and cannot be accelerated by saving up. [1]
- limits note: 50 credits a day that expire the same day: 'Credits included in subscriptions do not carry over from day to day or month to month', so 10 short songs is the ceiling and a 100-track project takes ten days and cannot be accelerated by saving up.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 50 songs a week of generated audio is a usable synthetic audio set for a classifier, and it composes with a free runner to script prompts; what breaks is that the free plan carries no commercial rights and the model is pinned to v6-mini, so a dataset built here describes the cheapest model and not the current one.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The credit number comes from the vendor's help centre, because the pricing page renders its plan table client side and the extracted text carried the row labels without the numbers. The help article is dated 2025-12-19 in the search index, so the 50-credit figure could have moved; the site FAQ's '10 songs a day' on 2026-10-22 corroborates it independently. Not established: whether the daily grant is exactly 50 today rather than enough for 10 songs, which are not the same statement.
- extras:
  - facets.class: perpetual-free-allowance
  - facets.free_tier_kind: recurring-daily-allowance
  - facets.shape.gpu_count: 0
- evidence:
  - [2] 2026-10-22: 'The Free plan offers 50 credits that replenish daily. This is enough to make 10 songs per day!', quoted from the vendor help centre article 'What type of plan do I have?'
  - [3] 2026-10-22: 'Yes. Suno is a free AI music generator that lets you create up to 10 songs a day, no credit card required', quoted from the site FAQ as rendered in the search index
  - [1] 2026-10-22: the plan table prints 'Free Plan ... Best free model (v6-mini)' and '4 in a Shared queue' against 10 in a priority queue for paid plans, quoted
  - [1] 2026-10-22: 'Credits included in subscriptions do not carry over from day to day or month to month', quoted
- sources:
  - [1] https://suno.com/pricing
  - [2] https://help.suno.com/en/articles/2410049
  - [3] https://suno.com/
