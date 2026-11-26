# Flagpool

> flagpool.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/flagpool/ | JSON https://fshy.ajam.dev/api/v1/entity/flagpool.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Flagpool

- `dev-services/flagpool` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted feature flags with local SDK evaluation, billed per project | tier Hobby
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:44:36.826Z (live) | stale on 2026-12-20
- url https://www.flagpool.io/en/pricing
- free tier: Hobby plan, free, no credit card required: one team member (owner only), one environment, up to 10 new flags per month, unlimited flag evaluations, unlimited clients; paid plans have a 14-day free trial | unit: mixed | metered on: object-count | read on: 2026-11-19 | source: [1] | note: Billing is per project, not per seat: the whole team is included within each plan's member limit. The pricing FAQ says flag evaluations are unlimited on every plan because flags are evaluated locally in the SDK. The public pricing page capture showed only the FAQ section, so the EUR 15 Starter monthly price published by third parties is not used here.
- per-object cap: unverified: no per-flag value size cap is stated on the pages read
- retention: unverified: no flag-data retention period is stated on the first-party pages read; a third party lists 7-day data retention on the free tier, which is not used as evidence here
- egress: not applicable: a flag service with locally evaluated flags and no per-evaluation charge or traffic allowance published | metered: no | source: [2]
- identity: email | detail: The register form asks for Full Name, Work Email, Password and Confirm Password; no card is required and cancellation is allowed at any time. No phone number or ID is requested on the form; whether a later step asks for one is unverified: behind a sign-up.
- interface: rest
- limits:
  - per-object-cap (binding): up to 10 new flags per month on Hobby [1]
  - per-object-cap (binding): one team member (owner only) and one environment on Hobby [3]
  - volume-quota: unlimited flag evaluations on every plan; no per-evaluation charge or throttling [2]
- limits note: Hobby has one member and one environment; Starter allows up to 5 and Pro up to 15 with extra seats as add-ons, per the access-control documentation. Analytics data from free-plan projects is silently discarded, per the official Python and React SDK documentation.
- binding note: The 10-new-flags-per-month creation cap and the single member and environment bind first; evaluations are unlimited, so traffic does not consume the free allowance.
- interface detail: The SDK initializes with a project ID, an environment-specific API key and a decryption key, then downloads configuration and evaluates flags locally with no network call per evaluation; a REST-style admin API is implied by the dashboard and SDK setup, but the exact endpoint is unverified on the pages read.
- tooling: Official SDKs for TypeScript, React, Python, Go, Java and C#; the free plan is limited to one team member.
- composes with: Evaluate flags locally in an app from one project using a single environment, staying within 10 newly created flags per month.
- reliability: Flag evaluation is local with no per-evaluation charge or throttling on any plan. Paid plans include a 14-day free trial with no card required; cancelling reverts the project to the free Hobby tier at the end of the billing period. Enforcement behaviour past the Hobby flag-creation cap is unverified on the pages read.
- notes: Revisit when a first-party page publishes the full plan price grid, the flag-data retention period or the over-cap enforcement behaviour.
- evidence note: Every value is quoted from first-party homepage, pricing FAQ, access-control documentation and register pages. No account was opened and no live flag evaluation was probed, so the record stays at documented rung. The detailed plan price grid and a per-flag value cap remain unverified on a first-party page.
- evidence:
  - [1] 2026-11-19: the free Hobby plan is for one team member, one environment and up to 10 flags per month | capture: sha256:0b68372b41fa039c2cdb792508db9278608cb512c2f6a29227334a1de52ff426 | quote: One team member, one environment, and up to 10 flags per month.
  - [1] 2026-11-19: no credit card is required to start | capture: sha256:0b68372b41fa039c2cdb792508db9278608cb512c2f6a29227334a1de52ff426 | quote: No credit card required
  - [1] 2026-11-19: flag evaluations are unlimited on every plan with no per-evaluation charges | capture: sha256:0b68372b41fa039c2cdb792508db9278608cb512c2f6a29227334a1de52ff426 | quote: From Hobby to Enterprise, without per-evaluation charges.
  - [2] 2026-11-19: flag evaluations are unlimited and there are no per-evaluation charges or throttling | capture: sha256:9539abd64f74beee3b967a86fe82bcb8697621bd111d7a909eb481aefd84763b | quote: Flags are evaluated locally in your application using our SDKs
  - [2] 2026-11-19: paid plans have a 14-day free trial with no card required | capture: sha256:9539abd64f74beee3b967a86fe82bcb8697621bd111d7a909eb481aefd84763b | quote: Starter and Pro plans include a 14-day free trial with full access to all features. No credit card required to start.
  - [2] 2026-11-19: cancelling reverts a project to the Hobby free tier | capture: sha256:9539abd64f74beee3b967a86fe82bcb8697621bd111d7a909eb481aefd84763b | quote: Your project will revert to the Hobby (free) tier at the end of the current billing period.
  - [3] 2026-11-19: Hobby allows one member (owner only) and team members are invited by email | capture: sha256:77a114869feab715e27a2c4f372e814a37659a29c739abbdc7e4901bc0aa2fdd | quote: Team members are invited by email and assigned a role that determines what they can do.
  - [3] 2026-11-19: the Hobby plan member limit is one, the owner only | capture: sha256:77a114869feab715e27a2c4f372e814a37659a29c739abbdc7e4901bc0aa2fdd | quote: | Hobby | 1 (owner only) |
  - [4] 2026-11-19: the register form asks for full name, work email and password | capture: sha256:71e2f8f186599fff27ecf323383c3df0dea6c22a0c0cced61bc2c74e1448ea6c | quote: Work Email
- sources:
  - [1] https://www.flagpool.io/en
  - [2] https://www.flagpool.io/en/pricing
  - [3] https://www.flagpool.io/docs/security/access-control
  - [4] https://www.flagpool.io/en/register
