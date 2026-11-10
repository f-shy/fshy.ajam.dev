# Anything

> create.xyz | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/create/ | JSON https://fshy.ajam.dev/api/v1/entity/create.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Anything

- `compute/anything` | trial-only | evidence reported | binding request-rate | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-02T02:17:32.272Z (live) | stale on 2026-11-17
- url https://www.create.xyz/pricing
- free tier: Free plan is 3,000 credits with daily message limits and public-only projects; quoted from third-party reviews because the vendor page renders only the paid cards: "Free includes 3,000 credits with daily message limits" and "3,000 credits are one-time only" | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an Anything account: an email address or a Google or Apple sign-in, quoted 'Sign up with Google', 'Sign up with Apple' and 'Email'; the sign-up and log-in pages carry no card field and no phone field; no country restriction is stated on them
- interface: unknown
- limits:
  - request-rate (binding): the 3,000 credits are consumed and not refilled, and a daily message cap applies on top, so the free lane ends on whichever bound is reached first. [1]
- limits note: the 3,000 credits are consumed and not refilled, and a daily message cap applies on top, so the free lane ends on whichever bound is reached first.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: about USD 3 of generation is one app, not a pipeline; the value is that it publishes for free, so the output can be handed to a static host and kept after the credits are gone.
- reliability: no reliability event recorded
- notes: Sources disagree on whether the 3,000 credits are monthly or one-time: one review says monthly, two say one-time, and the vendor page does not render the free card at all. Classified as one-time because that is the majority and the more conservative reading. The credit-to-dollar rate is the vendor's, which makes this the only app builder in evaluated offerings that publishes its exchange rate.
- extras:
  - facets.class: trial
  - facets.free_tier_kind: one-time-credit
- evidence:
  - [1] 2026-10-22: the page renders Pro at USD 19 for 20K credits and USD 199 for 220K, and states "Everything in Free, plus" for each tier, so a Free tier exists but its card is not in the rendered page
  - [2] 2026-10-22: the vendor's own pricing change post fixes the exchange rate: "1k credits ~= $1", quoted, so 3,000 free credits is about USD 3 of generation
  - [3] 2026-10-22: "Free includes 3,000 credits with daily message limits" and the Free card lists 3,000 credits, daily message limits, free publishing and Anything branding, reported
  - [4] 2026-11-02: the log-in page asks for an email address or a Google or Apple login, and no card or phone | capture: sha256:ae4d0423262472e9b0ae35dd6056f8c80e9493371f79ebb806afa9f9b897562f | quote: Log in Sign in with Google Sign in with Apple Or Email
  - [5] 2026-11-02: the sign-up page offers a Google or Apple sign-in over an email form and carries no card or phone field | capture: sha256:87ead737794eb1db4339ffd2813fa30bf2773ffd0aef22f61455d037c31954cf
- sources:
  - [1] https://www.create.xyz/pricing
  - [2] https://www.anything.com/blog/credits-pricing
  - [3] https://www.therundown.ai/tools/create
  - [4] https://www.anything.com/login
  - [5] https://www.anything.com/signup
