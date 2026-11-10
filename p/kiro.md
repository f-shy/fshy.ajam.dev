# Kiro

> kiro.dev | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kiro/ | JSON https://fshy.ajam.dev/api/v1/entity/kiro.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kiro

- `coding-subs/kiro` | qualifies-with-caveat | evidence documented | binding request-rate | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T17:29:12.673Z (live) | stale on 2026-12-04
- url https://kiro.dev/pricing/
- free tier: Kiro Free: USD 0 per month, 50 credits a month, access to open weight models and Claude Sonnet 4.5 'with limits'; add-on credits are not available on Free | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1] | note: a credit is the metering unit; the pricing page says usage limits reset at the start of each billing month with no rollover. The unit is credits, not requests (open question)
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: email | detail: social login or an AWS Builder ID for the IDE sign-in; paid plans need a valid credit card. Enterprise and AWS GovCloud have no Free tier
- interface: cli
- limits:
  - request-rate (binding): 50 credits a month on Free; 1,000 on Pro at USD 20; 2,000 on Pro+ at USD 40; 5,000 on Pro Max at USD 100; 10,000 on Power at USD 200 [1]
- interface detail: the Kiro IDE; sign-in is by social login or an AWS Builder ID
- tooling: Kiro IDE and Kiro CLI; Kiro Web is available to paid plans only
- composes with: the Free tier is the same account and the same model set as Pro, so a measurement taken today stays valid if the account is later upgraded
- reliability: no reliability event recorded
- notes: 50 credits a month against 1,000 on a USD 20 plan is 5 per cent of the paid allowance, which is the smallest free-to-paid ratio in the class.
- evidence note: the ladder is quoted from the vendor page read. The credit-to-token conversion is unpublished, so capacity in tokens is unverified.
- evidence:
  - [1] 2026-10-22: Free USD 0 with 50 credits; Pro USD 20 with 1,000; Pro+ USD 40 with 2,000; Pro Max USD 100 with 5,000; Power USD 200 with 10,000; add-on credits USD 0.04 each
  - [1] 2026-11-03: the Free tier has 50 credits and includes open weight models and Claude Sonnet 4.5 with limits | capture: sha256:04895484957ac7946bedcd25493af723fc21d0f804caba4f2909d11a143892e7 | quote: New users can start with the perpetual Kiro Free tier, which includes 50 credits. The Free Tier includes access to open weight models and Claude Sonnet 4.5, with limits.
  - [1] 2026-11-03: the allowance window is a billing month with no rollover | capture: sha256:04895484957ac7946bedcd25493af723fc21d0f804caba4f2909d11a143892e7 | quote: Usage limits reset at the start of each billing month. Unused credits do not roll over to the next month.
  - [1] 2026-11-03: a card is needed only to upgrade to a paid plan | capture: sha256:04895484957ac7946bedcd25493af723fc21d0f804caba4f2909d11a143892e7 | quote: Upgrading to a paid subscription requires a valid credit card.
  - [1] 2026-11-03: subscriptions work with the IDE, CLI, Web, Crew and ACP compatible IDEs | capture: sha256:04895484957ac7946bedcd25493af723fc21d0f804caba4f2909d11a143892e7 | quote: Kiro subscriptions can be used with Kiro IDE, Kiro CLI, Kiro Web, Kiro Crew, ACP compatible IDEs, and automation in software development
  - [1] 2026-11-03: Free still includes Claude Sonnet 4.5 and open weight models, with limits | capture: sha256:04895484957ac7946bedcd25493af723fc21d0f804caba4f2909d11a143892e7 | quote: The Free Tier includes access to open weight models and Claude Sonnet 4.5, with limits.
  - [2] 2026-11-03: the credit ladder 50, 1,000, 2,000, 5,000 and 10,000 is unchanged | capture: sha256:1a77ce688ee1b3cbe742f47213296b2e511f438402abca17eb15c4be6bc14761 | quote: | Pro Max | 5,000 | Available to purchase |
  - [1] 2026-11-03: the perpetual Free tier still has 50 credits | capture: sha256:04895484957ac7946bedcd25493af723fc21d0f804caba4f2909d11a143892e7 | quote: New users can start with the perpetual Kiro Free tier, which includes 50 credits.
- sources:
  - [1] https://kiro.dev/pricing/
  - [2] https://kiro.dev/docs/billing/
