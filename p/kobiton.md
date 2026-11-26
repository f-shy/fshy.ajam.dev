# Kobiton

> kobiton.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kobiton/ | JSON https://fshy.ajam.dev/api/v1/entity/kobiton.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kobiton

- `compute/kobiton` | trial-only | evidence documented | binding volume-quota | category real-device mobile testing cloud | tier Startup, with free account trial
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.925Z (live) | stale on 2026-12-26
- url https://kobiton.com/pricing/
- free tier: A free account includes 300 testing minutes on real iOS and Android devices with no credit card required; the Startup plan starts at $83/month and includes 500 minutes a month. | unit: minutes | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The $83/month Startup plan buys 500 testing minutes, which is $9.96 an hour at the included-minute rate. Accelerate starts at $399/month for 3,000 minutes a month.
- per-object cap: not applicable: the unit is a real-device testing session, not an object | source: [2]
- retention: unverified: the pricing and signup pages read do not state how long screenshots, videos and network logs are kept | source: [2]
- egress: not published: the pages read state no egress allowance or price for traffic from the hosted devices | metered: no | source: [2]
- identity: email | detail: The free-account page offers Google, GitHub or email signup, asks for a work email and states no credit card is required; no phone or ID document is requested on that page.
- interface: rest, browser
- limits:
  - volume-quota (binding): 300 testing minutes on the free account; 500 minutes a month on Startup [1]
- limits note: Public cloud access is included on Startup, Accelerate and Scale; hosted private device slots have a 5-device minimum on higher plans. Enterprise pricing is by request.
- binding note: The 300 free testing minutes, then the 500 a month on the cheapest paid plan, bind first for a single user.
- interface detail: Manual testing in the browser and scripted automation with Appium, Selenium, Espresso and XCUITest on the public cloud; the signup page promises AI-generated Appium scripts.
- endpoint: unverified: no API endpoint is stated on the pages read
- tooling: A user drives the public cloud from the browser or submits Appium, Selenium, Espresso or XCUITest scripts; the Enterprise tier also offers hosted private device slots and on-premises devices.
- composes with: A mobile test suite can run against public real devices and collect screenshots, videos and network logs without the user owning the devices.
- reliability: unverified: the pages read state no ban, throttle or data-loss behaviour for the free account
- notes: A free account gets 300 testing minutes with no card. The cheapest recurring offer is Startup at $83/month for 500 minutes, which is $9.96 an hour at the included-minute rate. Retention and API endpoint are unverified on the pages read.
- evidence note: Price and included minutes are quoted from Kobiton's own pricing and free-account pages read on 2026-11-25; retention and reliability pages were not available.
- extras:
  - billing_model: monthly plan with included testing minutes
  - free_tier_kind: one-time signup allowance
  - term: monthly
  - price_arithmetic: $83/month ÷ 500 minutes = $9.96 an hour at the included-minute rate
  - session_cap.note: not stated on the pages read
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - other_plans: Accelerate from $399/month for 3,000 minutes; Scale $9000/year for 7,500 minutes a month; Enterprise by request
- evidence:
  - [2] 2026-11-25: the Startup plan starts at $83 a month | capture: sha256:62204a569515e17c36971b876255c304b106574798c480bbe5ac2ba682e06327 | quote: Starting at $83/month
  - [2] 2026-11-25: the Startup plan includes 500 minutes a month | capture: sha256:62204a569515e17c36971b876255c304b106574798c480bbe5ac2ba682e06327 | quote: 500 mins / month
  - [1] 2026-11-25: a free account includes 300 testing minutes on real devices | capture: sha256:e31b41ed7c30cd1689d79a5eebca2a73613532f57b099bf9806128b00f2159df | quote: - 300 testing minutes
  - [1] 2026-11-25: signup offers Google, GitHub or email and asks for a work email | capture: sha256:e31b41ed7c30cd1689d79a5eebca2a73613532f57b099bf9806128b00f2159df | quote: Or sign up with email
  - [1] 2026-11-25: the work-email recommendation appears on the free-account form | capture: sha256:e31b41ed7c30cd1689d79a5eebca2a73613532f57b099bf9806128b00f2159df | quote: We recommend using work email to keep work and life separate.
  - [3] 2026-11-25: the free account does not require a card | capture: sha256:31401f9efdeb685edc237ec084aea8738ea66b0c7e22b7a574f12bab4f23791c | quote: No credit card required
  - [2] 2026-11-25: the Startup plan uses the public real-device cloud for manual and scripted testing | capture: sha256:62204a569515e17c36971b876255c304b106574798c480bbe5ac2ba682e06327 | quote: * Manual Testing on Real Devices
  - [2] 2026-11-24: the self-serve Startup plan starts at $83 a month | capture: sha256:62204a569515e17c36971b876255c304b106574798c480bbe5ac2ba682e06327 | quote: Starting at $83/month
  - [2] 2026-11-24: the Startup plan includes 500 testing minutes a month on public cloud access | capture: sha256:62204a569515e17c36971b876255c304b106574798c480bbe5ac2ba682e06327 | quote: 500 mins / month
  - [2] 2026-11-24: the Accelerate plan starts at $399 a month and includes 3,000 minutes a month | capture: sha256:62204a569515e17c36971b876255c304b106574798c480bbe5ac2ba682e06327 | quote: Starting at $399/month
  - [2] 2026-11-24: the Scale plan is annual only and grants 7,500 testing minutes a month | capture: sha256:62204a569515e17c36971b876255c304b106574798c480bbe5ac2ba682e06327 | quote: 7,500 mins / month
  - [2] 2026-11-24: the Compare Plans table prices the Scale tier at $9000 a year | capture: sha256:62204a569515e17c36971b876255c304b106574798c480bbe5ac2ba682e06327 | quote: $9000
  - [1] 2026-11-24: the free sign-up grants 300 testing minutes | capture: sha256:d4fbd6749e7639c5a167e5393aa81ef7f91ae94456967cabc5511d1c0c56f755 | quote: 300 testing minutes
  - [1] 2026-11-24: sign-up uses Google, GitHub or an email address and asks for a work email | capture: sha256:d4fbd6749e7639c5a167e5393aa81ef7f91ae94456967cabc5511d1c0c56f755 | quote: Or sign up with email
  - [1] 2026-11-24: the trial does not require a credit card | capture: sha256:d4fbd6749e7639c5a167e5393aa81ef7f91ae94456967cabc5511d1c0c56f755 | quote: No credit card required
  - [4] 2026-11-24: the trial period is thirty days and the vendor disclaims warranties and support for trials | capture: sha256:af66a157624a39c0cee3cf6d2bf38ec595ad556ad4d01ad3641784c198720017 | quote: Trial Subscriptions are permitted solely for Customer’s use to determine whether to purchase a paid subscription to the Services.
- sources:
  - [1] https://kobiton.com/freetrial
  - [2] https://kobiton.com/pricing/
  - [3] https://portal.kobiton.com/register
  - [4] https://kobiton.com/service-subscription-agreement/
