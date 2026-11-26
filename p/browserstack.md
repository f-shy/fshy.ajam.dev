# BrowserStack App Automate

> browserstack.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/browserstack/ | JSON https://fshy.ajam.dev/api/v1/entity/browserstack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BrowserStack App Automate

- `compute/browserstack-app-automate` | trial-only | evidence documented | binding volume-quota | category mobile device cloud | tier App Automate - Device Cloud (1 parallel test)
- identity a placeholder: card and phone unknown | verified 2026-11-25T11:55:06.479Z (live) | stale on 2026-12-26
- url https://www.browserstack.com/app-automate
- free tier: 100 minutes of automated mobile application testing on different mobile devices, given at signup as part of the BrowserStack Free Trial; not a recurring monthly allowance. The signup page also lists 100 mins of automated mobile app testing among what is included. | unit: minutes | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: one-time trial allowance of 100 minutes, not a monthly pool; the signup FAQ on the free trial is the page that states the number
- per-object cap: not applicable: the unit is a hosted test device session, not a stored object | source: [2]
- retention: not published on the pages read: the App Automate page and the trial FAQ state no retention period for test logs, videos or screenshots | source: [2]
- egress: not published on the pages read: the pricing page, the product page and the trial FAQ state no egress allowance or price for device sessions | metered: no | source: [3]
- identity: email | detail: unverified: the sign-up page offers only 'Sign up with Google' and role and discovery dropdowns; no email field, email, card or phone text appears on it, and an original and a fresh read of the page both showed only Google OAuth. The email/password form is rendered by JavaScript and is not in the captured text, so the exact identifier gate is not established from the sign-up page. The sign-in page does show 'Enter your business email' and 'Enter your password' for an existing account, but that is not a sign-up gate.
- interface: rest
- limits:
  - volume-quota (binding): 100 minutes of automated mobile app testing in the Free Trial, a one-time allowance rather than a recurring monthly pool [1]
  - request-rate: 1 parallel test at USD 199 per month billed annually; the pricing page lists 1, 2 and 5 parallel-test tiers but publishes no per-tier price above 1 parallel test [3]
- limits note: Access is by concurrent App Automate sessions, not by a per-minute meter on the paid tier; unlimited testing minutes are listed as included in the paid device plans.
- binding note: The 100 trial minutes are spent once and do not renew, so that one-time allowance is what runs out first before any paid subscription begins.
- interface detail: Automated mobile app tests driven by Appium, Espresso, XCUITest and EarlGrey against physical iOS and Android devices; REST API to mark statuses and fetch session logs; vendor SDK and CI/CD integrations.
- endpoint: https://www.browserstack.com/app-automate
- tooling: Appium, Espresso, XCUITest and EarlGrey test suites with BrowserStack SDKs and a REST API; integrations with Jenkins, GitHub, GitLab, CircleCI, Jira and Slack; no rclone or generic shell access, the device is reached through the test automation frameworks.
- composes with: A hosted real-device lab for running mobile test suites in CI without owning handsets; 100 free minutes at signup sizes a first suite, and at scale the 1-parallel device tier costs USD 199 a month billed annually, so the paid tier is a subscription rather than a per-minute meter.
- reliability: No reliability event observed on the pages read; the trial allowance is a one-time 100 minutes and the page gives no SLA for the free trial.
- notes: A hosted real-device cloud for mobile app automation: Appium, Espresso, XCUITest and EarlGrey tests run on physical iOS and Android devices. The free trial is 100 one-time minutes of App Automate, not a recurring allowance; the paid App Automate Device Cloud tier is USD 199 a month billed annually for one parallel device test, and the next listed tier is USD 249 a month billed annually. No general-purpose shell VM is offered; the compute is a managed device session. The signup page's only visible identity gate is OAuth; an email-and-password field appears on the sign-in page, but the exact registration identifier is not established from the sign-up capture.
- evidence note: The trial minutes, the App Automate tier price and the signup gate were read from first-party BrowserStack pages on 2026-11-25; the price came from the pricing page's plan comparison table.
- extras:
  - shape.note: hosted physical iOS and Android devices; per-device hardware specification not stated on the pages read
  - billing_model: monthly subscription per parallel device test
  - free_tier_kind: one-time-trial-minutes
  - term: monthly or annual billing; the annual rate is USD 199/month and the monthly rate USD 249
  - price_arithmetic: USD 199 / month billed annually / 730 hours = USD 0.273 per hour for 1 parallel real device
  - derived: USD 199 / 730 hours = USD 0.273 per hour
  - network_out.note: no egress allowance or price stated on the pages read
  - session_cap.note: the pages read give no per-session wall-clock cap for App Automate; the trial allowance is 100 minutes total
- evidence:
  - [1] 2026-11-25: the signup free trial gives 100 minutes of App Automate automated mobile testing | capture: sha256:0e876d2d14dd332bf61d0045de1321fd6784de7150f8ccf7eef2c10ee4efe186 | quote: - App Automate: 100 minutes of automated mobile application testing on different mobile devices.
  - [4] 2026-11-25: the signup page lists 100 minutes of automated mobile app testing as included and offers a free account with Google sign-in | capture: sha256:935b6279926a04afda17fe3b1933be34d55145ccf00fe41f6ae627762e2d2ef2 | quote: - 100 mins of automated mobile app testing
  - [4] 2026-11-25: the signup gate shows only Google OAuth and no email field, card or phone text | capture: sha256:935b6279926a04afda17fe3b1933be34d55145ccf00fe41f6ae627762e2d2ef2 | quote: [Sign up with Google](https://www.browserstack.com/users/auth/google_oauth2?state=eyJ2NF9hdXRoX3BhZ2VfZXhwIjpmYWxzZX0=)
  - [4] 2026-11-25: a fresh read of the signup page again shows only Google OAuth and no email field, card or phone text | capture: sha256:34f4488159a1b350b3a2b0a581f4dd33f1ac0e20285d8ff85a386524a531f7ec | quote: [Sign up with Google](https://www.browserstack.com/users/auth/google_oauth2?state=eyJ2NF9hdXRoX3BhZ2VfZXhwIjpmYWxzZX0=)
  - [5] 2026-11-25: the sign-in page for an existing account takes a business email and a password alongside Google sign-in | capture: sha256:bcdf2ddd12d62eb6b58b6582fca636af64a48ec7d1a0375afe0cd72421153245 | quote: Enter your business email
  - [3] 2026-11-25: the App Automate Device Cloud tier is USD 199 per month billed annually for 1 parallel test | capture: sha256:35b034dd60dad08b0fab807bb4dff28106b86d2d9f40d714a310dc0340968d3d | quote: | ### Feature List<br>![App Automate Icon](https://www.browserstack.com/images/static/simplification/sidenav/products/grey/app-automate-grey.svg)<br>App Automate | ### Device Cloud<br>$199/month<br>(billed annually)
  - [2] 2026-11-25: the product is a hosted real-device automation cloud with 30,000+ devices running a million tests daily | capture: sha256:1e42a2653530233e2fc2061b3ce3f5208e12f5222d042d1f7af31605e795d126 | quote: Scale effortlessly for AI-driven development with 30,000+ real devices and infrastructure running 1 million tests daily.
  - [3] 2026-11-24: the App Automate Device Cloud entry tier is USD 199 per month billed annually and is metered in parallel tests | capture: sha256:52584efb5d9e7e5e0a90ac0fdd72f0f1fd994eb2a00e18229cdd791acae5f9ff | quote: 199
  - [3] 2026-11-24: the entry App Automate tier includes one parallel test and higher tiers offer two, five or more than five | capture: sha256:52584efb5d9e7e5e0a90ac0fdd72f0f1fd994eb2a00e18229cdd791acae5f9ff | quote: Parallel tests indicate the number of automated tests that can be run simultaneously.
  - [3] 2026-11-24: the paid tier includes unlimited users and testing minutes and over 30,000 real iOS and Android devices | capture: sha256:52584efb5d9e7e5e0a90ac0fdd72f0f1fd994eb2a00e18229cdd791acae5f9ff | quote: Unlimited Users & testing minutes
  - [3] 2026-11-24: the automation frameworks supported include Appium, Espresso, XCUITest, Maestro and Flutter | capture: sha256:52584efb5d9e7e5e0a90ac0fdd72f0f1fd994eb2a00e18229cdd791acae5f9ff | quote: Integrate with testing Frameworks like Espresso, XCUITest, Maestro and Flutter
  - [1] 2026-11-24: the free trial grants 100 minutes of automated mobile application testing | capture: sha256:1817957da1d3f97e33773fd6e8099b22c031f9a0bab61670efd06fb9ad218126 | quote: App Automate: 100 minutes of automated mobile application testing on different mobile devices.
  - [6] 2026-11-24: certain Automate plans are subject to fair usage | capture: sha256:bd776429e3d7689fcec24779ee4e4c017c21f28407bea042df703f4de5ddf35c | quote: certain Automate plans are subject to Fair Usage
  - [4] 2026-11-24: registration offers a Google sign-up and an email-and-password form, and the trial includes 100 minutes of automated mobile app testing | capture: sha256:0114ff07ff24a8d42d967b8aee6cb404b6d2bdb4b5c532a0a1627e52760e655f | quote: Sign up with Google
  - [4] 2026-11-24: the sign-up page states the trial's automated mobile app testing allowance | capture: sha256:0114ff07ff24a8d42d967b8aee6cb404b6d2bdb4b5c532a0a1627e52760e655f | quote: 100 mins of automated mobile app testing
  - [7] 2026-11-24: the pricing comparison lists a REST API for test status, session info and logs | capture: sha256:18a4c5359b0503277f333255561ea93b96d841cf492fd6a40a01be2f2902a69d | quote: REST API light info icon Mark test statuses, access session info, view logs, and more
  - [2] 2026-11-24: the App Automate product page advertises real-device automation and Appium support | capture: sha256:789172c4b41ce3e19698a336d315549f9c82d85cf61de2b3b554064449aaa8d1 | quote: Appium
  - [3] 2026-11-25: the pricing page names the parallel-test tiers and publishes a price only for 1 parallel test at USD 199 per month billed annually | capture: sha256:35b034dd60dad08b0fab807bb4dff28106b86d2d9f40d714a310dc0340968d3d | quote: 1 parallel test2 parallel tests5 parallel testsMore than 5 parallel tests
  - [3] 2026-11-25: the pricing page lists USD 249 per month billed annually as the next tier above the USD 199 tier | capture: sha256:35b034dd60dad08b0fab807bb4dff28106b86d2d9f40d714a310dc0340968d3d | quote: $249/month
- sources:
  - [1] https://www.browserstack.com/support/faq/plans-pricing/plans/what-do-i-get-with-a-free-trial
  - [2] https://www.browserstack.com/app-automate
  - [3] https://www.browserstack.com/pricing?product=app-automate
  - [4] https://www.browserstack.com/users/sign_up
  - [5] https://www.browserstack.com/users/sign_in
  - [6] https://www.browserstack.com/support/faq/plans-pricing/usage-plans-pricing/is-usage-limited-and-if-so-what-are-those-limits
  - [7] https://www.browserstack.com/pricing
