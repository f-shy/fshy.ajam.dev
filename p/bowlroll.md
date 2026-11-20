# BowlRoll

> bowlroll.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bowlroll/ | JSON https://fshy.ajam.dev/api/v1/entity/bowlroll.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BowlRoll (bowlroll.net)

- `storage/bowlroll` | fails-quota | evidence inferred | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://bowlroll.net
- free tier: Not published on any page reachable without login; the front page now opens with a funding appeal ('BowlRollでは、継続的な運用のため資金面でのご支援が必要です') asking users to support it via PixivFANBOX. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unknown. | metered: no
- identity: anonymous
- interface: rest
- limits note: Unverified: /user/rule returns HTTP 422 and /faq is empty through the reader. The site is alive but in a donations-or-die state.
- interface detail: rest
- tooling: Web only; no documented API.
- composes with: Unknown. Cannot chain what cannot be measured.
- reliability: Long-running Japanese MMD/UTAU asset host now publicly fundraising for survival. Alive today, structurally fragile. A strong candidate to be gone by the next round.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Not published on any page reachable without login; the front page now opens with a funding appeal ('BowlRollでは、継続的な運用のため資金面でのご支援が必要です') asking users to support it via PixivFANBOX.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'ご支援のお願い / 継続的な運用のため資金面でのご支援が必要です' with a PixivFANBOX link
  - withheld 2026-10-21: probe: GET /user/rule -> 422; /faq returned an empty extraction
- sources:
  - [1] https://bowlroll.net/
