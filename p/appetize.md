# Appetize. io

> appetize.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/appetize/ | JSON https://fshy.ajam.dev/api/v1/entity/appetize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Appetize. io

- `compute/appetize-io` | qualifies-with-caveat | evidence documented | binding write-gated | category hosted mobile-device streaming | tier Free (trial) plan
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.899Z (live) | stale on 2026-12-26
- url https://appetize.io/pricing
- free tier: Free plan at USD 0 a month: a single user, up to 2 active devices, 30 minutes refilled monthly, and a 3-minute session limit; usage is throttled capacity. | unit: minutes | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: Streaming time runs from the start of a stream until the user leaves the page or the session times out. The Starter plan is USD 59 a month billed annually (USD 89 monthly) with 500 minutes included then USD 0.06 a minute.
- per-object cap: not applicable: the metered unit is streaming minutes, not an object
- retention: Sessions run in isolated environments and clear when they end; no separate retention period is stated on the pricing or homepage. | source: [2]
- egress: not published as a streaming allowance: the pricing page bills streaming minutes rather than traffic and states no egress price or per-session byte cap | metered: no | source: [1]
- identity: email | detail: The sign-up page shows an email input and offers Sign Up with Google and Sign Up with GitHub. The login page offers email and password, Google and GitHub. No card is asked on the sign-up page; the free plan needs no payment method, while paid plans take Visa, Mastercard or American Express through Stripe.
- interface: rest, cli, browser
- limits:
  - volume-quota: 30 streaming minutes a month on Free; 500 minutes then USD 0.06 a minute on Starter [1]
  - per-object-cap: 2 active devices at once on Free; 3 on Starter and 16 on Premium [1]
  - write-gated (binding): 3-minute session limit on Free, unlimited on paid plans, and throttled capacity on Free [1]
- limits note: API Access is listed only on the paid plans in the comparison table; the Free column leaves that feature unchecked. Payment methods accepted are Visa, Mastercard and American Express through Stripe.
- binding note: The 3-minute session limit and throttled capacity cut a Free session short before the 30 monthly minutes are used, and the comparison table leaves API access off the Free plan.
- interface detail: An Appetize CLI and REST API at api.appetize.io/v1 with X-API-KEY authentication, plus a JavaScript SDK and embeddable browser streaming links.
- tooling: Appetize CLI, the v1 REST API with an organization API token, the JavaScript SDK, and Playwright-based automation (AppRecorder) against streamed devices.
- composes with: A user uploads an APK or build and streams an iOS simulator or Android emulator in the browser, or drives it from a coding agent through the CLI or REST API; the paid continuation is USD 0.06 a minute after 500 included minutes on Starter.
- reliability: Free sessions are capped at 3 minutes and run at throttled capacity; sessions clear when they end. The pricing page states a 99.9% uptime SLA, which is an enterprise-level commitment rather than a Free-plan guarantee.
- notes: Hosted iOS simulators and Android emulators streamed to the browser: Free gives 30 minutes a month at 2 active devices and a 3-minute session cap, with API access left to paid plans; Starter is USD 59 a month billed annually with 500 minutes then USD 0.06 a minute. On-premises and private clouds are an enterprise option and are not the hosted offer priced here.
- evidence note: Prices, limits, sign-up fields and API terms are quoted from first-party Appetize pages read on 2026-11-25.
- extras:
  - shape.note: hosted iOS simulators and Android emulators priced in streaming minutes
  - billing_model: monthly free minute allowance, per-minute overage on paid plans
  - free_tier_kind: recurring-allowance
  - term: no commitment on Free; Starter billed monthly or annually
  - network_out.allow_outbound: yes
  - session_cap.wall_clock_min: 3
  - session_cap.restart_required: no
  - session_cap.note: a Free session ends after 3 minutes; streaming time ends when the user leaves the page or the session times out
- evidence:
  - [1] 2026-11-25: the Free plan has 30 minutes refilled monthly | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: 30 minutes refilled monthly
  - [1] 2026-11-25: the Starter plan includes 500 minutes then charges USD 0.06 a minute | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: 500 minutes included, then $0.06/min
  - [1] 2026-11-25: Free sessions are limited to 3 minutes while paid plans are unlimited | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: | Session limit | 3 minutes | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-25: API access is a paid-plan feature, not part of Free | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: | API Access | | | | |
  - [1] 2026-11-25: paid plans take Visa, Mastercard and American Express through Stripe | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: We accept Visa, Mastercard and American Express via our payments provider Stripe.com.
  - [3] 2026-11-25: sign-up asks for an email address | capture: sha256:d91cbe48149fdbf84506d38f5839b463c888d05a2a267c353b3363d90234a65d | quote: name="email" id="id-:R1cktd6:" type="email"
  - [3] 2026-11-25: sign-up also offers Google and GitHub accounts | capture: sha256:d91cbe48149fdbf84506d38f5839b463c888d05a2a267c353b3363d90234a65d | quote: Sign Up with GitHub
  - [4] 2026-11-25: the login page asks for email and password and offers Google and GitHub login | capture: sha256:949a170cb13a1507eb2cde9a3739c6e368aeb8288e4b982aa260da7ba6467b1c | quote: aria-label="Email" autoComplete="username" required=""
  - [5] 2026-11-25: the REST API is reachable with an API token in the X-API-KEY header | capture: sha256:fe14ec10f903748e37bf66d154245e85d738aa1f4c206f726192a69cc77f3d19 | quote: curl -X GET https://api.appetize.io/v1/apps
  - [2] 2026-11-25: coding agents drive the hosted devices through the CLI or REST API | capture: sha256:1a78efae964c65b2dc0dc28ab0856c829f6c38e93e80ba3c6ac57c0d39026a61 | quote: Appetize provides on-demand devices through the Appetize CLI or REST API.
  - [1] 2026-11-24: the free plan's monthly minutes, device count and single user | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: Single user 2 active devices maximum 30 minutes refilled monthly
  - [1] 2026-11-24: the free plan's three-minute session limit against unlimited on paid plans | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: | Session limit | 3 minutes | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-24: the monthly minute allowance and overage price on paid plans | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: | Minutes per month | 30 | 500, then $0.06/minute | 500, then $0.06/minute | Custom |
  - [1] 2026-11-24: API access and automation are plan features | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: | API Access | | | | |
  - [1] 2026-11-24: streaming time is the metered unit, counted until the user leaves or the session times out | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: We bill every month based on the total amount of streaming time for all of your uploaded apps.
  - [1] 2026-11-24: free capacity is throttled and users are queued when no device is available | capture: sha256:ad39c748141fe6cf337efb965b16d235aa3bf0d2b3efa42c9995057c4778707a | quote: If no devices are available on your account, the user will be put in a queue to wait until a new device becomes available.
  - [3] 2026-11-24: the sign-up form asks for a Work Email and offers Google and GitHub sign-up | capture: sha256:a18b18372767580e43f12b77bddcaf031051545f8f5c263ddf848568bc84ab50 | quote: Verify email address
- sources:
  - [1] https://appetize.io/pricing
  - [2] https://appetize.io/
  - [3] https://appetize.io/signup
  - [4] https://appetize.io/account
  - [5] https://docs.appetize.io/rest-api
