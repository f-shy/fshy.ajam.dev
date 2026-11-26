# WonderPush

> wonderpush.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wonderpush/ | JSON https://fshy.ajam.dev/api/v1/entity/wonderpush.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WonderPush

- `dev-services/wonderpush` | trial-only | evidence documented | binding volume-quota | category hosted push notification service for iOS, Android and the web (a Brevo company) | tier Push notifications
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:19:24.791Z (live) | stale on 2026-12-20
- url https://www.wonderpush.com/pricing
- free tier: 0 subscribers is free; a 14-day free trial gives all features with no credit card. From 1 subscriber the push plan is EUR 1 per month for 1-1000 subscribers, EUR 2 for 1001-2000 and EUR 3 for 2001-3000, plus EUR 1 for every further 1000. | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: The unit stated by the vendor is a subscriber: a unique device and application or website combination. There is no ongoing free tier at any positive subscriber count, only the 14-day trial.
- per-object cap: not stated: no per-payload or per-message size cap is published on the pricing or billing pages read | source: [1]
- retention: By default navigation data is kept for 3 months; the user decides what data is stored and for how long. If payment fails after the trial, sending is blocked but project and subscriber data is kept for 90 days, after which it is deleted from the servers. | days: 90 | source: [2] | note: The 90-day figure is the unpaid-account deletion window; the navigation figure of 3 months is a separate default and is stated on the pricing page.
- egress: not metered per message or per byte: push sending is unlimited on the plan and the bill is based on subscriber count | metered: no | source: [1]
- identity: email | detail: The sign-up form asks for an email address, a password and a confirmation password with a reCAPTCHA, and offers Brevo, Google, GitHub, Facebook and Shopify sign-in. The pricing page states that the 14-day trial needs no credit card. Payment details are taken only when the plan starts, through Stripe.
- interface: rest, browser
- limits:
  - volume-quota (binding): 0 subscribers is free; EUR 1 per month for 1-1000 subscribers, EUR 2 for 1001-2000, EUR 3 for 2001-3000, plus EUR 1 per further 1000 [1]
  - retention-clamped: a 14-day free trial with no credit card; after it, sending is blocked until payment is supplied and unpaid data is deleted after 90 days [2]
- limits note: A maximum monthly budget can be set; when it is reached the service stops signing up new users while other activity continues. Push sending is unlimited and no per-message price is published.
- binding note: The subscriber count sets the price from the first subscriber, so the 0-subscriber free state ends as soon as one device opts in.
- interface detail: A documented RESTful API sends notifications from a backend or CMS, and the Management API automates sends; iOS, Android and web SDKs register devices, and an online dashboard designs notifications and reads real-time analytics. Web and iOS web push register through the browser service worker.
- endpoint: unverified: the API base URL is not stated on the pricing or billing pages read
- tooling: The vendor runs the hosted service; the user adds an iOS, Android or web SDK, calls the REST or Management API, and uses the web dashboard. No software is installed to run the push service itself.
- composes with: A hosted service with a REST API, web dashboard and SDKs for iOS, Android and the web; no machine is supplied by the user. Self-hosted push servers are a separate option and are considered after this hosted offer.
- reliability: The vendor states a push delivery speed of 350k messages per second. Three failed payment collections suspend sending until invoices are paid; unpaid project and subscriber data is deleted after 90 days. European user data is stored in Europe.
- notes: WonderPush is hosted software run by the vendor and has no ongoing free tier at a positive subscriber count: the free state is 0 subscribers and a 14-day trial needs no card. Sign-up asks for an email address and a password and needs no card before the trial ends.
- evidence note: The price, subscriber definition, trial, retention windows and payment terms are read on the first-party pricing page and billing documentation; the sign-up fields are read from the first-party sign-up form. No account was opened and no payment was made.
- evidence:
  - [1] 2026-11-19: the push plan starts at EUR 1 per month plus EUR 1 for every further 1000 subscribers | capture: sha256:ac1965123e8f69a13cee02e1dc4abbf79f590c818b7c511996de3816f50b6d05 | quote: starting €1 / month
  - [1] 2026-11-19: the price table tiers subscribers at EUR 1 for 1-1000, EUR 2 for 1001-2000 and EUR 3 for 2001-3000 | capture: sha256:ac1965123e8f69a13cee02e1dc4abbf79f590c818b7c511996de3816f50b6d05 | quote: | €1 | 1-1000 |
  - [1] 2026-11-19: a 14-day free trial is offered with no credit card | capture: sha256:ac1965123e8f69a13cee02e1dc4abbf79f590c818b7c511996de3816f50b6d05 | quote: Start your 14-day free trial
  - [1] 2026-11-19: no credit card is required for the trial | capture: sha256:ac1965123e8f69a13cee02e1dc4abbf79f590c818b7c511996de3816f50b6d05 | quote: No credit card required
  - [1] 2026-11-19: push sending is unlimited on the plan | capture: sha256:ac1965123e8f69a13cee02e1dc4abbf79f590c818b7c511996de3816f50b6d05 | quote: Unlimited Push
  - [1] 2026-11-19: a maximum monthly budget stops new sign-ups when the limit is reached | capture: sha256:ac1965123e8f69a13cee02e1dc4abbf79f590c818b7c511996de3816f50b6d05 | quote: Set a max monthly budget When you reach your limit, we'll let you know and just stop signing up new users.
  - [1] 2026-11-19: by default navigation data is kept for 3 months | capture: sha256:ac1965123e8f69a13cee02e1dc4abbf79f590c818b7c511996de3816f50b6d05 | quote: By default, navigation data is kept for 3 months.
  - [1] 2026-11-19: the plan bills monthly 30 days after sign-up | capture: sha256:ac1965123e8f69a13cee02e1dc4abbf79f590c818b7c511996de3816f50b6d05 | quote: Monthly subscription billed 30 days after you sign up
  - [2] 2026-11-19: the service is paid, with a 14-day trial that needs no credit card | capture: sha256:7a4c852d374c6890e994167c781a02523270be5aad1d2e8a0339ab1dad72a2e6 | quote: No, WonderPush is a paying platform that offers a free trial period of 14 days. During that time, you can use all the features for free and without filling any credit card.
  - [2] 2026-11-19: the price is EUR 1 per 1000 subscribers per month | capture: sha256:7a4c852d374c6890e994167c781a02523270be5aad1d2e8a0339ab1dad72a2e6 | quote: With WonderPush, you pay €1 per 1000 subscribers, per month.
  - [2] 2026-11-19: a subscriber is a unique device and application or website combination, and the table lists 0 subscribers as free | capture: sha256:7a4c852d374c6890e994167c781a02523270be5aad1d2e8a0339ab1dad72a2e6 | quote: | 0 | FREE |
  - [2] 2026-11-19: unpaid project and subscriber data is kept for 90 days and then deleted | capture: sha256:7a4c852d374c6890e994167c781a02523270be5aad1d2e8a0339ab1dad72a2e6 | quote: your data (project, subscribers) will be kept for 90 days. Beyond this period, your data is automatically and completely deleted from our servers.
  - [3] 2026-11-19: the sign-up form creates an account with an email address and a password | capture: sha256:7e392aa2ff72f3c3b0d2484c1a0c9c0af96bdca719f3e5565aaf4648bcebb8bb | quote: Please enter your details to create your account
  - [3] 2026-11-19: the sign-up form asks for an email address | capture: sha256:7e392aa2ff72f3c3b0d2484c1a0c9c0af96bdca719f3e5565aaf4648bcebb8bb | quote: class="sib-input-label">Email</label>
- sources:
  - [1] https://www.wonderpush.com/pricing
  - [2] https://docs.wonderpush.com/docs/billing
  - [3] https://dashboard.wonderpush.com/account/signup
