# TestMu AI

> testmuai.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/testmuai/ | JSON https://fshy.ajam.dev/api/v1/entity/testmuai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TestMu AI (formerly LambdaTest), Free (HyperExecute test execution)

- `compute/testmu-ai` | trial-only | evidence documented | binding volume-quota | category browser and device testing cloud | tier Free (HyperExecute test execution)
- needs card no, phone no, ID no, institution no | verified 2026-11-24T10:11:15.113Z (live) | stale on 2026-12-25
- url https://www.testmuai.com/pricing/
- free tier: Free, USD 0, Free Forever: 300 minutes of testing, with up to 2 concurrent sessions on Windows or Linux VMs; 100 accessibility tests per organisation. The 100 minutes of Automation testing are a separate one-time allowance, valid for lifetime. | unit: minutes | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: The free HyperExecute minutes renew monthly and cap concurrency at 2 sessions; the free Automation allowance of 100 minutes is one-time and does not renew.
- per-object cap: not applicable: the unit is a browser or VM test session, not a stored object | source: [1] | note: A paid Test Manager plan states 10 GB of data storage per user; no per-object cap is published.
- retention: 30-day data retention on the testing plans; the paid plans offer custom data retention rules at Enterprise, and the free Smart UI tier states 1 month of build history. | days: 30 | source: [2] | note: The 30-day retention is stated on the Live Testing and paid Automation plans on the vendor's own pricing.md page.
- egress: unverified: no egress allowance, price or transfer quota for test results or artifacts is published on the pricing page read; the plan pages describe test minutes and parallel sessions, not network egress. | metered: no | source: [1]
- identity: email | detail: The sign-up page offers Continue with Google, Continue with Github, or Work email, then Continue; no card, phone or ID document is asked on that page, and the pricing FAQ states the free tier needs no credit card.
- interface: rest, browser, cli
- limits:
  - volume-quota (binding): 300 minutes of free test execution per month, up to 2 concurrent Windows or Linux VM sessions [1]
  - request-rate: 1 parallel test on the free plan; a parallel session is one test executing at a time [1]
  - retention-clamped: 30-day data retention on the paid non-enterprise plans [2]
  - volume-quota (binding): 100 minutes of web+mobile automation testing, one-time, valid for lifetime, with 2 parallel sessions [1]
- limits note: A free HyperExecute run is 300 minutes a month at 2 concurrent sessions; the Automation free tier is 100 minutes once, not a monthly refill. Lower tiers cap parallelism at 1 and exclude CI/CD integrations and auto-heal.
- binding note: The 300 monthly minutes at 2 concurrent sessions are what run out first for a recurring free workload; the 100 Automation minutes are one-time and the concurrency is capped at 2 sessions.
- interface detail: RESTful APIs for automating pipelines and screenshot APIs; Selenium, Cypress, Playwright, Puppeteer and Appium drive the grid; the Kane CLI and Rook CLI install from npm.
- tooling: Selenium, Playwright, Cypress, Puppeteer, Appium, TestNG, WebdriverIO; free npm CLIs @testmuai/kane-cli and @testmuai/rook; REST APIs and CI integrations with GitHub, GitLab and CircleCI.
- composes with: The free HyperExecute cloud runs browser and VM test sessions that compose with CI pipelines and object-storage records for logs and artifacts; the paid Automation and Real Device plans extend the same grid to mobile devices.
- reliability: Free Automation minutes are one-time and do not renew; free live sessions are limited to 2 minutes each and renew monthly; free tiers exclude CI/CD integrations, auto-heal, AI RCA and scheduled workflows; data retention on Live and paid plans is 30 days.
- notes: TestMu AI is the former LambdaTest, rebranded on 2026-01-12. The free capacity is time-boxed: HyperExecute gives 300 minutes a month at 2 concurrent sessions and Automation gives 100 minutes once. The Automation, Live, HyperExecute, SmartUI, Performance Testing and Test Manager free tiers are separate pools; the page does not say whether bundled allowances add to a product's own free minutes, so they are not summed. No egress price is published on the pages read.
- evidence note: The published rates, free minutes, concurrency caps, sign-up fields and retention line are quoted from the vendor's pricing page and pricing.md read on 2026-11-24; no egress price is published there.
- extras:
  - billing_model: per parallel session, per agent, per user or per scan depending on product
  - free_tier_kind: recurring-minutes plus one-time-minutes
  - term: monthly, free forever on the HyperExecute and Automation free tiers
  - products: KaneAI, Kane CLI, Test Manager, Agent Testing, Agent Assurance, Live Testing, Automation, HyperExecute, Performance Testing, Smart UI, Accessibility
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.egress_price: unverified: not published on the pricing page or pricing.md
  - session_cap.wall_clock_min: 40
  - session_cap.restart_required: no
  - session_cap.note: free Performance Testing caps a single test at 40 minutes; free live sessions are 2 minutes each
- evidence:
  - [1] 2026-11-24: the free HyperExecute tier is USD 0, 300 minutes of testing, Free Forever | capture: sha256:3b407f9c37e80cd6ebfebd44e56c1c57757bcdf7a26777b15020ae233a2b3d32 | quote: 300 minutes of testing Free Forever
  - [1] 2026-11-24: the free tier runs up to 2 concurrent sessions on Windows or Linux VMs | capture: sha256:3b407f9c37e80cd6ebfebd44e56c1c57757bcdf7a26777b15020ae233a2b3d32 | quote: 300 minutes of testing, with up to 2 concurrent sessions
  - [1] 2026-11-24: the paid HyperExecute public cloud is USD 159 per month billed annually | capture: sha256:3b407f9c37e80cd6ebfebd44e56c1c57757bcdf7a26777b15020ae233a2b3d32 | quote: ## HyperExecute - Public Cloud ## $159 /month billed annually
  - [1] 2026-11-24: parallel session means one test at a time; the cloud bills by concurrency | capture: sha256:3b407f9c37e80cd6ebfebd44e56c1c57757bcdf7a26777b15020ae233a2b3d32 | quote: A parallel session is one test executing at a time - HyperExecute bills by concurrency, not minutes or users.
  - [1] 2026-11-24: the grid is reachable over REST APIs from CI pipelines | capture: sha256:3b407f9c37e80cd6ebfebd44e56c1c57757bcdf7a26777b15020ae233a2b3d32 | quote: Restful APIs for automating pipelines
  - [2] 2026-11-24: the Automation free tier is 100 minutes once, valid for lifetime | capture: sha256:523f273f72e9edf5459b6c3ddeb63e08b74377bbf1767d18a31d1b29fcfe1464 | quote: Free - 100 minutes of 2-parallel web+mobile automation testing, valid for lifetime. 100 accessibility tests per org.
  - [2] 2026-11-24: the free HyperExecute tier is 300 minutes at up to 2 concurrent sessions | capture: sha256:523f273f72e9edf5459b6c3ddeb63e08b74377bbf1767d18a31d1b29fcfe1464 | quote: Free - 300 minutes, up to 2 concurrent sessions (Windows or Linux VMs)
  - [2] 2026-11-24: data retention is 30 days on the paid non-enterprise testing plans | capture: sha256:523f273f72e9edf5459b6c3ddeb63e08b74377bbf1767d18a31d1b29fcfe1464 | quote: All paid non-enterprise plans have 30-day data retention.
  - [3] 2026-11-24: sign-up offers Google, GitHub or a work email and no card or phone field is shown | capture: sha256:ed52721c9344eb18af1db9ba25b1273df78c5ba971b09b86783d380a71b7e09e | quote: Continue with Google
- sources:
  - [1] https://www.testmuai.com/pricing/
  - [2] https://www.testmuai.com/pricing.md
  - [3] https://www.testmuai.com/register/

## TestMu AI (formerly LambdaTest), testmu ai real device automation

- `compute/testmu-ai-real-device-automation` | trial-only | evidence documented | binding volume-quota | category mobile device cloud | tier Real Device Plus Automation Cloud (1 parallel test)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:55:06.479Z (live) | stale on 2026-12-26
- url https://www.testmuai.com/pricing/
- free tier: 100 free minutes of 2 parallel web+mobile automation testing, valid for lifetime, on all browsers and OS for selenium, playwright, puppeteer, cypress or JavaScript based automation tests. The Live Testing freemium plan separately gives 5 free sessions of up to 2 minutes each on real devices every month; no credit card required. | unit: minutes | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: the 100 automation minutes are a one-time lifetime allowance, not a monthly pool; the real-device live sessions (5 x 2 minutes per month) do renew monthly but are interactive live sessions, not automation capacity
- per-object cap: not applicable: the unit is a hosted test device session, not a stored object | source: [1]
- retention: Test execution data on the VM or real device is deleted as soon as the test completes; logs, videos and screenshots generated during a test are stored encrypted for 30 days by default. | days: 30 | source: [2]
- egress: metered: no | source: [1]
- identity: email | detail: The registration page offers 'Work email' with Continue, or 'Continue with Google' and 'Continue with Github'; no card, phone number, ID document or institution is asked for at signup, and the pricing page FAQ states 'no credit card required' for the free plan.
- interface: rest
- limits:
  - volume-quota (binding): 100 free automation minutes, one-time and valid for lifetime, with 2 parallel sessions [1]
  - request-rate: 1 parallel test at USD 199 per month billed annually for Real Device Plus Automation Cloud [1]
  - retention-clamped: logs, videos and screenshots retained 30 days by default; test execution data deleted when the test completes [2]
- limits note: Live Testing freemium gives 5 real-device sessions of up to 2 minutes each per month, renewed monthly; it is interactive live testing and not automation capacity. Paid plans meter by parallel session and include unlimited testing minutes.
- binding note: The 100 automation minutes are one-time and do not renew, so that lifetime allowance is what runs out first before paid concurrency is needed.
- interface detail: Automation Cloud driven by Selenium, Playwright, Cypress, Puppeteer and Appium, Espresso and XCUITest against real iOS and Android devices; a Lambda Tunnel reaches locally hosted apps; REST APIs and SDKs for pipelines.
- endpoint: https://www.testmuai.com/pricing/
- tooling: Selenium, Playwright, Cypress, Puppeteer, Appium, Espresso and XCUITest suites via hosted grids; REST APIs including a Screenshot API; CI integrations with GitHub, GitLab and CircleCI; Lambda Tunnel for private apps; no shell-level device access or rclone backend.
- composes with: A hosted real-device cloud for running mobile and web test suites in CI without owning handsets; the 100 lifetime minutes size a first suite, and at scale the Real Device Plus Automation Cloud tier is USD 199 a month billed annually for one parallel device, billed by concurrency rather than by minutes.
- reliability: VMs and real devices are cleaned between runs: test execution data is deleted as soon as a test completes and a device is returned to the public pool only after cleanup; generated logs, videos and screenshots expire after 30 days by default.
- notes: A hosted real-device cloud for web and mobile app automation: Selenium, Playwright, Cypress, Puppeteer and Appium, Espresso and XCUITest tests run on physical iOS and Android devices. The free plan gives 100 lifetime minutes with 2 parallel sessions; the paid Real Device Plus Automation Cloud tier is USD 199 a month billed annually for one parallel real device, which the operator's list converts to USD 0.273/h over 730 hours. No general-purpose shell VM is offered; the compute is a managed device session. Formerly branded LambdaTest; the company states it rebranded to TestMu AI on 2026-01-12.
- evidence note: The free minutes, the USD 199 real-device automation tier, the signup gate and the retention period were read from first-party TestMu AI pricing, registration and privacy pages on 2026-11-25.
- extras:
  - shape.note: hosted physical iOS and Android devices; per-device hardware specification not stated on the pages read
  - billing_model: monthly subscription per parallel device test
  - free_tier_kind: one-time-trial-minutes
  - term: monthly or annual billing; the annual rate is USD 199/month for the real-device automation tier
  - price_arithmetic: USD 199 / month billed annually / 730 hours = USD 0.273 per hour for 1 parallel real device
  - derived: USD 199 / 730 hours = USD 0.273 per hour
  - network_out.note: no egress allowance or price stated on the pages read
  - session_cap.wall_clock_min: 2
  - session_cap.note: the free Live real-device sessions are capped at 2 minutes each; no per-session wall-clock cap for paid automation is stated on the pages read
- evidence:
  - [1] 2026-11-25: the Automation free plan gives 100 free minutes of testing with 2 parallel sessions | capture: sha256:977a2363bf1f47810f43142339b402a20be3eef16dad787fd91a3e047bc01b16 | quote: 100 free minutes testing
  - [1] 2026-11-25: the 100 automation minutes are a lifetime allowance, not a monthly one | capture: sha256:977a2363bf1f47810f43142339b402a20be3eef16dad787fd91a3e047bc01b16 | quote: 100 Minutes of access to all browsers and OS for running selenium, playwright, puppeteer, cypress or JavaScript based automation tests, valid for lifetime
  - [1] 2026-11-25: the free plan needs no credit card and the 100 minutes do not renew monthly | capture: sha256:977a2363bf1f47810f43142339b402a20be3eef16dad787fd91a3e047bc01b16 | quote: Yes. The free plan gives 100 lifetime minutes (not monthly) with 2 parallel sessions, no credit card required. It suits evaluation and a first suite, not continuous integration - once those minutes run out, continued execution requires a paid plan.
  - [1] 2026-11-25: the Live freemium plan gives 5 real-device sessions of 2 minutes each per month | capture: sha256:977a2363bf1f47810f43142339b402a20be3eef16dad787fd91a3e047bc01b16 | quote: Get 5 sessions up to 2 minutes each, every month
  - [1] 2026-11-25: the Real Device Plus Automation Cloud tier costs USD 199 per month billed annually | capture: sha256:977a2363bf1f47810f43142339b402a20be3eef16dad787fd91a3e047bc01b16 | quote: ## Real Device Plus Automation Cloud ### $199 /month billed annually
  - [1] 2026-11-25: the real-device automation plan supports Appium, Espresso and XCUITest | capture: sha256:977a2363bf1f47810f43142339b402a20be3eef16dad787fd91a3e047bc01b16 | quote: Support for Appium, Espresso and XCUITest
  - [3] 2026-11-25: the signup gate asks for a work email or offers Google and GitHub OAuth, with no card or phone asked | capture: sha256:4629057df2fcbd233320d37365d5a11bcf7273c1e0be789ea621a7197b33a62c | quote: Work emailContinue
  - [2] 2026-11-25: generated logs, videos and screenshots are stored 30 days by default | capture: sha256:0d3b7a2c41d177c6305750526434e9cde95f3528e3104181ea733f0b862b2f22 | quote: TestMu stores the encrypted Test execution data, such as logs, videos, and screenshots that are actually generated while running the test at TestMu for 30 days by default.
- sources:
  - [1] https://www.testmuai.com/pricing/
  - [2] https://www.testmuai.com/legal/privacy/
  - [3] https://www.testmuai.com/register/
