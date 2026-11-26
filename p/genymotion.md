# Genymotion SaaS

> genymotion.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/genymotion/ | JSON https://fshy.ajam.dev/api/v1/entity/genymotion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Genymotion SaaS

- `compute/genymotion-saas` | qualifies-with-caveat | evidence documented | binding write-gated | category hosted Android virtual device farm | tier Pay as you Go (SaaS cloud virtual devices)
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T02:12:34.899Z (live) | stale on 2026-12-26
- url https://docs.genymotion.com/usage/saas/pricing/
- free tier: A free 60-minute trial is available on request: an individual applicant gets 60 free minutes and 2 simultaneous devices, and a company employee gets 1000 free minutes and up to 10 simultaneous devices. | unit: minutes | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The trial is not self-service: a request is reviewed within 5 business days for individuals and 2 business days for companies. The paid Pay-as-you-Go rate is USD 0.06 a minute per active virtual device; the company 1000-minute figure is a trial allowance, not a recurring tier.
- per-object cap: not applicable: the metered unit is a running virtual device-minute, not an object
- retention: not published on the pricing, quickstart or product pages read: no device-state or result retention period is stated for Genymotion SaaS | source: [2]
- egress: not published as a SaaS allowance: the pricing documentation bills running device-minutes and states no separate egress price or quota | metered: no | source: [2]
- identity: email | detail: Sign-up is by email address with a verification email, or through Google or GitHub single sign-on; disposable email providers are not allowed for registration. The trial request asks whether the applicant is an individual or a company, requires a valid personal email for an individual or a valid professional email and company details for a company, and is manually reviewed. The default subscription payment method is a credit card: Visa, Mastercard or American Express; prepaid cards are not accepted.
- interface: rest, cli, browser
- limits:
  - volume-quota: 60 free minutes for an individual trial; 1000 free minutes for a company trial; Pay-as-you-Go charges USD 0.06 a minute per active virtual device [2]
  - per-object-cap: 2 simultaneous devices on an individual trial and 10 on a company trial; Pay-as-you-Go defaults to 2 concurrent instances [1]
  - write-gated (binding): trial requires an account, a trial request and manual review within 5 business days for individuals or 2 business days for companies [1]
- limits note: Every started minute is billed as soon as the device is running; payments are processed weekly by default or when usage exceeds a default USD 150 threshold. Prepaid and virtual credit cards are not accepted.
- binding note: The trial must be requested and manually approved before any device can start, which binds ahead of the 60-minute allowance; a valid non-disposable email is mandatory.
- interface detail: A Platform HTTP API with an API token, the gmsaas command-line tool for creating and controlling devices and ADB connections, and a web dashboard for virtual devices.
- endpoint: https://api.geny.io
- tooling: gmsaas CLI, the SaaS HTTP API with an API token, ADB tunnelling, and CI integrations for GitHub Actions, CircleCI, Bitrise, Jenkins and Detox.
- composes with: A CI job starts hosted Android virtual devices through gmsaas or the HTTP API and runs instrumented tests in parallel; the paid continuation is USD 0.06 a minute per active device, with Pay-as-you-Go capped at 2 concurrent instances by default.
- reliability: Trials are manually reviewed and expire after the granted minutes; Pay-as-you-Go is limited to 2 concurrent instances by default and charges every started minute. Prepaid and virtual credit cards are not accepted for subscriptions.
- notes: Hosted Android virtual devices on the vendor's servers: Pay-as-you-Go is USD 0.06 a minute per active device with a 2-instance default cap, and a request-only 60-minute individual trial (1000 minutes for a company applicant). The Unlimited fixed monthly price is not published on the pages read; Genymotion Desktop, PaaS device images and self-hosted are separate offers and are not priced here.
- evidence note: The USD 0.06 per minute rate, concurrency cap, card terms, API and CLI access, and the trial allowances and gates are quoted from first-party Genymotion documentation read on 2026-11-25. The Unlimited plan's fixed price is not published on the pages read and is left unverified.
- self hosted: no
- extras:
  - shape.note: hosted Android virtual devices billed per running device-minute
  - billing_model: per-minute usage with weekly billing; fixed-rate Unlimited plan and custom Premium plan
  - free_tier_kind: request-only-trial
  - term: no commitment on Pay-as-you-Go; trial granted per request
  - network_out.allow_outbound: yes
  - network_out.ports: outgoing TCP 443 to cloud.geny.io and api.geny.io, TCP/UDP 443 to turn.genymotion.com and ws.geny.io
  - session_cap.restart_required: no
  - session_cap.note: every started minute is billed as soon as the device is running; no session length cap is stated on the pricing page
- evidence:
  - [2] 2026-11-25: Pay-as-you-Go is USD 0.06 a minute per active virtual device | capture: sha256:a0ceef4910641d6418d957427e6db6f47147799fcc90c8cdb0084e8b7e74b31f | quote: After subscribing, your organization can start virtual devices at a $0.06/minute rate per active virtual device.
  - [2] 2026-11-25: Pay-as-you-Go is capped at 2 concurrent instances by default | capture: sha256:a0ceef4910641d6418d957427e6db6f47147799fcc90c8cdb0084e8b7e74b31f | quote: With the Pay-As-You-Go plan, you are limited to a maximum of 2 concurrent instances.
  - [2] 2026-11-25: the default subscription payment method is a credit card and prepaid cards are rejected | capture: sha256:a0ceef4910641d6418d957427e6db6f47147799fcc90c8cdb0084e8b7e74b31f | quote: Prepaid cards are not supported.
  - [2] 2026-11-25: the accepted card brands are Visa, Mastercard and American Express | capture: sha256:a0ceef4910641d6418d957427e6db6f47147799fcc90c8cdb0084e8b7e74b31f | quote: The default payment method is credit card: Visa, Mastercard, American Express.
  - [1] 2026-11-25: an individual trial gives 60 free minutes and 2 simultaneous devices | capture: sha256:f5a5629eadae49ffab515095215963d762fd82dfc7c2741b716da2d9bb3f4044 | quote: Note that, as an individual, you will get 60 free minutes and a limit of 2 simultaneous devices.
  - [1] 2026-11-25: a company trial gives 1000 free minutes and up to 10 simultaneous devices | capture: sha256:f5a5629eadae49ffab515095215963d762fd82dfc7c2741b716da2d9bb3f4044 | quote: Please note that, as a company employee, you will benefit from 1000 free minutes and up to 10 simultaneous devices.
  - [1] 2026-11-25: a personal email is mandatory for an individual trial request | capture: sha256:f5a5629eadae49ffab515095215963d762fd82dfc7c2741b716da2d9bb3f4044 | quote: A valid personal email address is mandatory.
  - [3] 2026-11-25: a free 60-minute trial is available only on request | capture: sha256:cc56473fbc07e00656cd572ea2610bb9a6a3b8421dcb07f1ab15d0ed25c3c4d1 | quote: A free 60 minutes trial is available on request.
  - [3] 2026-11-25: registration uses an email address with verification or Google/GitHub SSO, and disposable addresses are rejected | capture: sha256:cc56473fbc07e00656cd572ea2610bb9a6a3b8421dcb07f1ab15d0ed25c3c4d1 | quote: Temporary email (also known as disposable) providers are not allowed for registration.
  - [4] 2026-11-25: the sign-in page offers Google and GitHub accounts alongside email and password | capture: sha256:04b3be8071f9e7fcd7d549e3eb841d91f095d01104d4065aeb476851f60b283e | quote: Continue with GoogleContinue with GitHub
  - [5] 2026-11-25: the SaaS includes a CLI for creating, controlling and connecting devices to ADB | capture: sha256:cd19fd05e38dc9366eeb9273bd65cf4d2ed5b6f676d06e33d04bfed3cc88d70d | quote: Integrated CLI
  - [6] 2026-11-24: the Pay-As-You-Go cloud plan is USD 0.06 per minute per running virtual device | capture: sha256:455aff116bee8fd4f1279e55240b6f90513c5d15e14346732520159ed70dfff5 | quote: $ 0.06 / minute per running virtual device
  - [6] 2026-11-24: the Unlimited cloud plan is USD 219 per month per virtual device on monthly billing | capture: sha256:455aff116bee8fd4f1279e55240b6f90513c5d15e14346732520159ed70dfff5 | quote: $ 219 / month per virtual device
  - [7] 2026-11-24: Pay-As-You-Go is limited to a maximum of 2 concurrent instances | capture: sha256:7b4a3411261299616bce2f5844ad43284301413e32a49118f261bbe624e183fc | quote: With the Pay-As-You-Go plan, you are limited to a maximum of 2 concurrent instances.
  - [7] 2026-11-24: plans require a Visa, Mastercard or American Express credit card and reject prepaid cards | capture: sha256:7b4a3411261299616bce2f5844ad43284301413e32a49118f261bbe624e183fc | quote: The default payment method is credit card: Visa, Mastercard, American Express. Prepaid cards are not supported.
  - [8] 2026-11-24: an individual free trial grants 60 minutes and 2 simultaneous devices | capture: sha256:f5a5629eadae49ffab515095215963d762fd82dfc7c2741b716da2d9bb3f4044 | quote: Note that, as an individual, you will get 60 free minutes and a limit of 2 simultaneous devices.
  - [8] 2026-11-24: a company free trial grants 1000 minutes and up to 10 simultaneous devices | capture: sha256:f5a5629eadae49ffab515095215963d762fd82dfc7c2741b716da2d9bb3f4044 | quote: Please note that, as a company employee, you will benefit from 1000 free minutes and up to 10 simultaneous devices.
  - [9] 2026-11-24: signup rejects disposable email addresses and accepts Google or GitHub SSO | capture: sha256:cc56473fbc07e00656cd572ea2610bb9a6a3b8421dcb07f1ab15d0ed25c3c4d1 | quote: Temporary email (also known as disposable) providers are not allowed for registration.
  - [10] 2026-11-24: the signup form offers Google and GitHub SSO or an email and password pair | capture: sha256:5f1e3ce46d1ccc90732a1abeb34d8640a8142c5870b12dc622a1b271738a3fea | quote: Continue with GoogleContinue with GitHub
  - [11] 2026-11-24: the account offers gmsaas, an HTTP API and a JavaScript SDK, with at most 25 API tokens | capture: sha256:13018bfd06a4c5f34e96f6d6ad26fd46d59c500bc5661380958526eadc43589c | quote: You can only have up to 25 tokens
  - [12] 2026-11-24: gmsaas manages device lifecycle and connects to ADB with an API token | capture: sha256:2cacc7d67fc9f594818b974d47ff5a008169e28e1ce0b6b3931416b97b44d07f | quote: With gmsaas CLI tool, you can use Genymotion SaaS to run automated tests in your continuous integration pipeline, regardless of your framework or continuous integration server.
  - [13] 2026-11-24: a browser logout does not stop a device, which runs until a frontend inactivity timeout or maximum run duration | capture: sha256:7fae5802487ffb2a7b1966be219bd8573de2268e67ce73446e969d18b08ceff0 | quote: Closing your web browser or logging out will not stop your running virtual devices. They have to be stopped manually or they will keep running until the Frontend inactivity timeout or the maximum run duration are reached.
  - [14] 2026-11-24: the organization can set a maximum run duration that shuts down an active device | capture: sha256:3d1bcf887b78b92ce59d4c23cace58dd39b30916191958d2a461bff29b5b7e2d | quote: The Maximum run duration setting allows you to configure the maximum duration time of your virtual devices. They will automatically shutdown after the specified duration is reached, whether or not they are active.
  - [9] 2026-11-24: the service requires outbound 443 to its cloud, API, TURN and websocket hosts | capture: sha256:cc56473fbc07e00656cd572ea2610bb9a6a3b8421dcb07f1ab15d0ed25c3c4d1 | quote: - Outgoing TCP port 443 on cloud.geny.io - Outgoing TCP port 443 on api.geny.io - Outgoing TCP/UDP port 443 on turn.genymotion.com
- sources:
  - [1] https://support.genymotion.com/hc/en-us/articles/17982644496157-How-do-I-get-the-free-trial-for-Genymotion-Cloud-SaaS
  - [2] https://docs.genymotion.com/usage/saas/pricing/
  - [3] https://docs.genymotion.com/quickstart/saas_quickstart/
  - [4] https://account.geny.io/signin
  - [5] https://www.genymotion.com/product-cloud/
  - [6] https://www.genymotion.com/pricing/
  - [7] https://docs.genymotion.com/saas/03_1_Pricing/
  - [8] https://support.genymotion.com/hc/en-us/articles/17982644496157
  - [9] https://docs.genymotion.com/saas/
  - [10] https://account.geny.io/signup
  - [11] https://docs.genymotion.com/usage/saas/basic_steps/
  - [12] https://docs.genymotion.com/usage/saas/automation/
  - [13] https://docs.genymotion.com/usage/saas/first_steps/
  - [14] https://docs.genymotion.com/usage/saas/admin_interface/
