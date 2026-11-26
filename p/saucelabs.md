# Sauce Labs

> saucelabs.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/saucelabs/ | JSON https://fshy.ajam.dev/api/v1/entity/saucelabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sauce Labs (compute/sauce-labs)

- `compute/sauce-labs` | trial-only | evidence documented | binding volume-quota | category browser and mobile device testing cloud | tier Live Testing plan, with 28-day free trial
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.925Z (live) | stale on 2026-12-26
- url https://saucelabs.com/pricing
- duplicate of `compute/sauce-labs-free-trial`
- free tier: A free 28-day trial includes 60 Automated and Live Testing minutes, 3 virtual machines in parallel, and real devices and mobile emulators; the Live Testing plan is $39 a month billed annually or $49 month to month. | unit: minutes | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: $39 a month divided by 730 hours is about $0.053 an hour; the plan includes one parallel test and unlimited live testing minutes. No card is required for the free trial.
- per-object cap: not applicable: the unit is a browser or device test session, not an object | source: [2]
- retention: unverified: the pricing and signup pages read state no retention period for test videos and screenshots | source: [2]
- egress: A secure local tunnel (Sauce Connect) is included on the Live Testing plan; no separate egress allowance or price is stated on the pages read. | metered: no | source: [2]
- identity: email | detail: Signup offers Google, GitHub or email signup and states that no credit card is required for the free account; the paid plan is charged to a card at purchase.
- interface: rest, browser
- limits:
  - volume-quota (binding): 60 Automated and Live Testing minutes in the 28-day free trial; the Live Testing plan has unlimited live testing minutes with 1 parallel test [1]
  - request-rate: 1 parallel test on the base Live Testing plan; 3 virtual machines in parallel on the free trial [2]
- limits note: The Virtual Device Cloud ($149/month billed annually) and Real Device Cloud ($199/month billed annually) plans add automated testing minutes and 1 to 5 concurrent sessions; Enterprise adds private device cloud and SSO.
- binding note: The 60 trial minutes, and then the single parallel test on the $39 plan, bind before any other limit for one user.
- interface detail: REST API access is included on the Live Testing plan; tests run from browsers, real devices, emulators and simulators with a live view.
- endpoint: unverified: the endpoint is not stated on the pages read
- tooling: A user drives live tests from the browser or automates them with the REST API and Sauce Connect; higher plans add virtual and real device automation.
- composes with: A test suite can use real devices, emulators and browser/OS combinations with a local tunnel, and collect videos and screenshots of a run.
- reliability: Secure, single-use VMs are included on the paid plans; no ban, throttle or data-loss behaviour is stated on the pages read.
- notes: Live Testing is a hosted manual browser/device testing plan at $39 a month billed annually, about $0.053 an hour divided by 730 hours; the 28-day free trial gives 60 minutes with no card. Virtual Device Cloud and Real Device Cloud are materially different offers priced at $149 and $199 a month billed annually.
- evidence note: Plan prices, trial minutes and signup gate are quoted from Sauce Labs' own pricing and signup pages read on 2026-11-25.
- extras:
  - billing_model: monthly plan with unlimited live testing minutes and a parallel-test count
  - free_tier_kind: time-boxed trial with minute allowance
  - term: monthly or annual
  - price_arithmetic: $39/month ÷ 730 hours = $0.053/hour
  - session_cap.note: not stated on the pages read
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: not stated
  - network_out.tunnel: Sauce Connect secure local tunneling
  - other_plans: Virtual Device Cloud $149/month billed annually ($199 monthly); Real Device Cloud $199/month billed annually ($249 monthly)
- evidence:
  - [2] 2026-11-25: the Live Testing plan is $39 a month billed annually or $49 month to month | capture: sha256:dafee9226da549cf9ab516d716463587fcf5ed63d78e5c45547ad97c47404ff8 | quote: $39
  - [2] 2026-11-25: Live Testing includes unlimited live testing minutes | capture: sha256:dafee9226da549cf9ab516d716463587fcf5ed63d78e5c45547ad97c47404ff8 | quote: Unlimited live testing minutes
  - [2] 2026-11-25: Live Testing covers manual cross-browser and mobile app testing on browsers, real devices and emulators | capture: sha256:dafee9226da549cf9ab516d716463587fcf5ed63d78e5c45547ad97c47404ff8 | quote: Manual cross-browser and mobile app testing on 1000s of desktop browsers, real mobile devices, emulators and simulators
  - [2] 2026-11-25: card plans are charged at purchase | capture: sha256:dafee9226da549cf9ab516d716463587fcf5ed63d78e5c45547ad97c47404ff8 | quote: Credit-card plans are charged at purchase — your invoice is ready in Billing within an hour.
  - [1] 2026-11-25: the free account needs no card and offers Google, GitHub or email signup | capture: sha256:b81647058681d694fdc4390fb8e77882b05c3d0a3e63c8f88a16fffb7089ae4d | quote: Get your free account today. No credit card required
  - [1] 2026-11-25: the free trial lasts 28 days | capture: sha256:b81647058681d694fdc4390fb8e77882b05c3d0a3e63c8f88a16fffb7089ae4d | quote: ### Your free 28-day trial includes
  - [1] 2026-11-25: the free trial includes 60 Automated and Live Testing minutes and 3 parallel virtual machines | capture: sha256:b81647058681d694fdc4390fb8e77882b05c3d0a3e63c8f88a16fffb7089ae4d | quote: - 60 Automated and Live Testing minutes
- sources:
  - [1] https://saucelabs.com/sign-up
  - [2] https://saucelabs.com/pricing

## Sauce Labs, Free Trial (28 days)

- `compute/sauce-labs-free-trial` | trial-only | evidence documented | binding volume-quota | category browser and device test cloud | tier Free Trial (28 days)
- needs card no, phone no, ID no, institution no | verified 2026-11-24T10:11:15.073Z (live) | stale on 2026-12-25
- url https://saucelabs.com/pricing
- free tier: 28-day free trial with 60 automated and live testing minutes, 3 virtual machines in parallel, 50 AI authoring and insights queries, real devices and emulators/simulators, no credit card | unit: minutes | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: The minutes are a single allowance shared by automated and live testing; paid plans instead state unlimited testing minutes with a parallel-test count.
- per-object cap: an artifact size cap is not published on the pricing, sign-up or terms pages read | source: [2] | note: The plan's published limit is a count of concurrent sessions, not an object size.
- retention: Customer Data less than thirty (30) days old is not intentionally deleted; data not retrieved within thirty (30) days after termination may be deleted | days: 30 | source: [3] | note: The 30-day figure is a post-termination download window.
- egress: test assets are retrieved through the Job Assets API or the saucectl artifacts download command; an egress volume allowance is not published | metered: no | source: [2]
- identity: email | detail: Sign-up offers Google, GitHub or email registration and states no credit card is required; the paid plans are credit-card plans.
- interface: rest, cli, browser
- limits:
  - volume-quota (binding): 60 automated and live testing minutes over a 28-day trial [1]
  - request-rate: 3 virtual machines in parallel on the trial; paid Live Testing starts with 1 parallel test and adds more [1]
  - request-rate: 50 queries across AI Test Authoring and AI Insights on the trial [1]
  - write-gated: a Sauce Labs account is needed before the REST API can be called [4]
- limits note: Paid plans bill a monthly fee and a parallel-test count; the page did not state a per-minute rate beyond the plan price.
- binding note: The 60 testing minutes end before the 28-day trial window or the three parallel VMs become relevant.
- interface detail: a REST API with a base URL per data center, the saucectl CLI, and a browser for live manual sessions
- endpoint: https://api.us-west-1.saucelabs.com/
- tooling: REST API with Basic Auth or short-lived access tokens, saucectl, Sauce Connect Proxy tunnels, and Selenium, Appium, Cypress and Playwright integrations
- composes with: a hosted browser and device lab for running tests from a CI job; screenshots and videos come back through the Job Assets API into other storage
- reliability: The trial expires after 28 days and support ends with it; test assets must be downloaded within thirty (30) days after termination.
- notes: The free allowance is a 28-day trial, not a recurring tier. Paid Live Testing is USD 39 monthly billed annually or USD 49 month to month with one parallel test included.
- evidence note: Pricing, trial allowance, registration options, REST interface, asset download path and retention window were read and quoted on 2026-11-24; no account or job was created.
- evidence:
  - [2] 2026-11-24: the paid Live Testing plan lists USD 39 a month billed annually or USD 49 month to month | capture: sha256:dafee9226da549cf9ab516d716463587fcf5ed63d78e5c45547ad97c47404ff8 | quote: $39 Per month, billed annually or $49 month to month
  - [2] 2026-11-24: the paid plan includes unlimited live minutes and unlimited users, and starts from one parallel test | capture: sha256:dafee9226da549cf9ab516d716463587fcf5ed63d78e5c45547ad97c47404ff8 | quote: Unlimited users Unlimited live testing minutes
  - [2] 2026-11-24: REST API access is a listed plan feature | capture: sha256:dafee9226da549cf9ab516d716463587fcf5ed63d78e5c45547ad97c47404ff8 | quote: REST API Access
  - [1] 2026-11-24: the free trial is 28 days and includes 60 testing minutes, 3 parallel VMs and 50 AI queries, with no card | capture: sha256:b81647058681d694fdc4390fb8e77882b05c3d0a3e63c8f88a16fffb7089ae4d | quote: Your free 28-day trial includes - Instant access to real devices - 60 Automated and Live Testing minutes - Local testing with Sauce Connect - Error Reporting with Backtrace - 3 Virtual Machines in parallel - 50 queries across AI Test Authoring and AI Insights
  - [1] 2026-11-24: registration asks for no credit card and offers Google, GitHub and email sign-up | capture: sha256:b81647058681d694fdc4390fb8e77882b05c3d0a3e63c8f88a16fffb7089ae4d | quote: Get your free account today. No credit card required
  - [4] 2026-11-24: the platform has a REST API and requires an account with a username and access key | capture: sha256:767c3fe36939e923674470dbc0107c95ca03dd4b46ab0358aceb99819defcbb0 | quote: The Sauce Labs APIs are REST-based.
  - [5] 2026-11-24: recorded screenshots and videos are downloaded through the Job Assets API | capture: sha256:f8164713377ecc48d1cbdce9f6aea5327e0907e4928694bb912b560e9a0ac3c9 | quote: can be accessed and downloaded through the Job Assets API endpoints
  - [6] 2026-11-24: support ends when the 28-day trial expires | capture: sha256:eae5949a6458640ddce70620c073e638a433bfd17fbd177cb32f670da6151eac | quote: If your 28-day trial has expired, Sauce Labs will be unable to provide Customer Support.
  - [3] 2026-11-24: Customer Data is kept for at least thirty days and a 30-day download window follows termination | capture: sha256:35c7aec52c1d0ab9d56364b042cdc990bf875d945cce55944d65024b9b1204cc | quote: Sauce Labs does not provide a data/content archiving service. Sauce Labs agrees only that it shall not intentionally delete any Customer Data which is less than thirty (30) days old.
- sources:
  - [1] https://saucelabs.com/sign-up
  - [2] https://saucelabs.com/pricing
  - [3] https://saucelabs.com/terms-of-service
  - [4] https://docs.saucelabs.com/dev/api/
  - [5] https://docs.saucelabs.com/dev/cli/saucectl/
  - [6] https://saucelabs.com/doc/support-policy
