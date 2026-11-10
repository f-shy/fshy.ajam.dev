# Cursor request-based

> cursor.com | Coding subscriptions; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cursor/ | JSON https://fshy.ajam.dev/api/v1/entity/cursor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cursor

- `coding-subs/cursor` | qualifies-with-caveat | evidence documented | binding request-rate | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-03T17:29:12.673Z (live) | stale on 2026-12-04
- url https://cursor.com/docs/models-and-pricing
- free tier: Free: USD 0, 'Agent and Chat with limited usage'; third-party models not available | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1] | note: the plan ladder was replaced by The X Subscription; Free states 'Limited' included usage with no number and no window, while the paid plans carry a weekly pool; legacy plans keep two monthly usage pools
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: email | detail: a Cursor or X account
- interface: cli
- limits:
  - request-rate (binding): one weekly usage pool for Cursor models; legacy plans keep two monthly pools [2]
- interface detail: the Cursor editor and its CLI; the usage pool covers agent, CLI and cloud agents
- tooling: Cursor editor, Cursor CLI
- composes with: the weekly pool is shared with Grok and the X apps, so Cursor usage is not a standalone budget
- reliability: no reliability event recorded
- notes: This is the largest drift found in the topic. See the history entry.
- evidence note: the restructure is quoted from the vendor's own documentation today. The size of any pool is unpublished in every tier, so no capacity claim is possible.
- evidence:
  - [1] 2026-10-22: The X Subscription is Free USD 0, Plus USD 8, Premium USD 30, Super USD 100, Ultra USD 200; one weekly pool shared across Grok and Cursor; third-party models billed at API list price from prepaid credit on Premium and above
  - [2] 2026-10-22: legacy Hobby free, Pro USD 20, Pro+ USD 60, Ultra USD 200, Teams Standard USD 40 per user, Teams Premium USD 120 per user; on-demand usage billed in arrears on legacy individual plans
  - [3] 2026-10-22: 
  - [1] 2026-10-30: Free is still USD 0 with Agent and Chat at limited usage and no third-party models | capture: sha256:e3f6aee695446630790f73553110b5ff11d605a66a39d42ffc5e93f0489b5ce2 | quote: Free. Agent and Chat with limited usage.
  - [1] 2026-10-30: the paid usage pool for Cursor models is still one weekly pool | capture: sha256:e3f6aee695446630790f73553110b5ff11d605a66a39d42ffc5e93f0489b5ce2 | quote: It refreshes weekly, so one heavy day doesn't use up your month.
  - [1] 2026-11-03: Free is USD 0 with Limited included usage and no third-party models | capture: sha256:e3f6aee695446630790f73553110b5ff11d605a66a39d42ffc5e93f0489b5ce2 | quote: | Free | $0 | Limited | Not available
  - [1] 2026-11-03: Free is unchanged: Agent and Chat with limited usage | capture: sha256:e3f6aee695446630790f73553110b5ff11d605a66a39d42ffc5e93f0489b5ce2 | quote: Free. Agent and Chat with limited usage.
  - [1] 2026-11-03: legacy plans (Pro, Pro+, Ultra, Teams) keep two monthly pools, which is why the record says two monthly pools | capture: sha256:e3f6aee695446630790f73553110b5ff11d605a66a39d42ffc5e93f0489b5ce2 | quote: They keep working as they are, with two monthly usage pools and on-demand usage.
- sources:
  - [1] https://cursor.com/docs/models-and-pricing
  - [2] https://cursor.com/docs/account/pricing/legacy-cursor-plans
  - [3] https://cursor.com/pricing

## Cursor request-based plans

- `coding-subs/cursor-legacy-request-plans` | dead | evidence documented | binding request-rate | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-10-22T04:31:20.000Z (live) | stale on 2026-11-22
- url https://cursor.com/docs/account/pricing/request-based-legacy
- free tier: a third, older generation counted usage in requests; superseded | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: email | detail: a Cursor account
- interface: cli
- limits:
  - request-rate (binding): usage counted in requests rather than tokens [1]
- interface detail: the same editor, with usage counted in requests rather than tokens
- tooling: Cursor editor
- composes with: a plan generation that a reader may still be paying for and that no current table prices
- reliability: no reliability event recorded
- notes: Closed to new accounts. New customers are routed to The X Subscription, and the request-based page states that an existing holder is migrated to usage-based pricing at their next renewal. Existing holders keep access until renewal.
- evidence note: the existence of the third generation is documented; its ladder was not read.
- evidence:
  - [1] 2026-10-22: request-based plans are 'an older generation still', linked from the legacy-plans page as a separate document
  - [2] 2026-10-22: 'If you're on a legacy request-based plan, you can continue using it until your next renewal. At renewal, you'll be migrated to the usage-based pricing model.' The page describes the model in the past tense and states the migration, which is the evidence that no new account can buy it
- sources:
  - [1] https://cursor.com/docs/account/pricing/legacy-cursor-plans
  - [2] https://cursor.com/docs/account/pricing/request-based-legacy
