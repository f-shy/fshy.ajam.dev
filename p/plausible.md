# Plausible Analytics

> plausible.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/plausible/ | JSON https://fshy.ajam.dev/api/v1/entity/plausible.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Plausible Analytics

- `dev-services/plausible` | trial-only | evidence documented | binding retention-clamped | category hosted web analytics | tier Cloud trial
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:37:34.247Z (live) | stale on 2026-12-03
- url https://plausible.io/docs/trial
- free tier: No free plan on Plausible Cloud: every account starts with a free 30-day trial with Business plan features and limits and no credit card; the cheapest plan after it is Starter at EUR 9/month for up to 10k monthly pageviews and one site | unit: none | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: The trial does not convert to a paid subscription by itself, because no payment method is on file. Growth is EUR 14/month and Business, the plan with the Stats API, EUR 19/month, at the same 10k pageview tier.
- per-object cap: not applicable: billed by pageviews and custom events, not stored objects
- retention: When an unsubscribed trial ends, the dashboard is locked, new stats are no longer collected, and dashboards and stats are eventually deleted after an e-mail warning; paid plans state no retention limit | source: [1]
- egress: not applicable: a hosted dashboard; stats leave through the Stats API at 600 requests per hour per key, a Business plan feature that the trial includes | metered: no | source: [2]
- identity: email | detail: The registration form asks for a full name, an e-mail address and a password of at least 12 characters, behind a Friendly Captcha check; no credit card is asked for. The documented flow then sends a four-digit code by e-mail and starts the 30-day trial once it is verified, and Plausible's WordPress page states that registration asks only for a name and an e-mail address.
- interface: rest
- limits:
  - retention-clamped (binding): 30-day trial, then the dashboard is locked and new stats are not collected [1]
  - request-rate: 600 Stats API requests per hour per key [2]
  - volume-quota: Starter: up to 10k monthly pageviews, one site [3]
- binding note: The trial ends after 30 days and the dashboard locks, before any pageview or API limit matters.
- interface detail: Stats API: a read-only HTTP interface, POST /api/v2/query with an API key in the Authorization header, 600 requests per hour by default; on the Business plan and during the trial. The Sites API is Enterprise-only.
- endpoint: https://plausible.io/api/v2/query
- tooling: the tracking script on the site, and any HTTP client with a Stats API key
- composes with: A 30-day window to evaluate privacy-focused web analytics, then EUR 9 a month; there is no free allowance to build on.
- reliability: After an unsubscribed trial, collection stops and dashboards and stats are deleted permanently after an e-mail warning.
- notes: Plausible Cloud has no recurring free allowance. Last resort, after every hosted offer: Plausible Community Edition, the same software under the AGPL, is free to self-host, and the user installs and runs the server on a rented or free machine and maintains it.
- evidence note: The trial terms, plan prices and API limits are quoted from first-party pages. No account was opened.
- evidence:
  - [1] 2026-10-30: every account starts with a free 30-day trial | capture: sha256:0805a3434e0f0d7eb823265ed703088d620df9c6eb45b40c4765f7414f38bd28 | quote: Every Plausible account starts with a free 30-day trial.
  - [1] 2026-10-30: registration asks for no credit card | capture: sha256:0805a3434e0f0d7eb823265ed703088d620df9c6eb45b40c4765f7414f38bd28 | quote: We don't ask for a credit card when you [register](https://plausible.io/docs/register-account).
  - [1] 2026-10-30: the dashboard locks when the trial ends without a subscription | capture: sha256:0805a3434e0f0d7eb823265ed703088d620df9c6eb45b40c4765f7414f38bd28 | quote: If you haven't subscribed by the end of the trial, your dashboard is locked.
  - [1] 2026-10-30: without a subscription collection stops and stats are eventually deleted | capture: sha256:0805a3434e0f0d7eb823265ed703088d620df9c6eb45b40c4765f7414f38bd28 | quote: If you don't subscribe, we'll stop collecting new stats and eventually delete your dashboards and all their stats permanently.
  - [4] 2026-10-30: all plans include a 30-day trial without a card | capture: sha256:e0d27cc99df39d9c93194ad3d3256a3c6e549c7bfefc5cb093ef394069dacf77 | quote: All plans include a 30-day free trial, no credit card required.
  - [4] 2026-10-30: the trial has Business plan features and limits | capture: sha256:e0d27cc99df39d9c93194ad3d3256a3c6e549c7bfefc5cb093ef394069dacf77 | quote: During the trial you have access to all Business plan features and limits
  - [5] 2026-10-30: Starter is EUR 9 a month | capture: sha256:fe7e2ce2118f8a3b3082d8a9401f791259876fe5e8832beb4016c8d3757a2f8c | quote: €9 /month
  - [5] 2026-10-30: the price shown is for up to 10k monthly pageviews | capture: sha256:fe7e2ce2118f8a3b3082d8a9401f791259876fe5e8832beb4016c8d3757a2f8c | quote: Up to 10k monthly pageviews
  - [5] 2026-10-30: Starter covers one site | capture: sha256:fe7e2ce2118f8a3b3082d8a9401f791259876fe5e8832beb4016c8d3757a2f8c | quote: One site
  - [5] 2026-10-30: paid plans state no retention limit | capture: sha256:fe7e2ce2118f8a3b3082d8a9401f791259876fe5e8832beb4016c8d3757a2f8c | quote: No retention limit
  - [5] 2026-10-30: Growth is EUR 14 a month | capture: sha256:fe7e2ce2118f8a3b3082d8a9401f791259876fe5e8832beb4016c8d3757a2f8c | quote: €14 /month
  - [5] 2026-10-30: Business is EUR 19 a month | capture: sha256:fe7e2ce2118f8a3b3082d8a9401f791259876fe5e8832beb4016c8d3757a2f8c | quote: €19 /month
  - [5] 2026-10-30: the Business plan includes the Stats API at 600 requests per hour | capture: sha256:fe7e2ce2118f8a3b3082d8a9401f791259876fe5e8832beb4016c8d3757a2f8c | quote: Stats API (600 requests per hour)
  - [2] 2026-10-30: the Stats API takes POST queries at /api/v2/query | capture: sha256:3536f727f4889db659d97c2027a80bab752c08f857b75f894c91c45c5d6e0196 | quote: The `/api/v2/query` endpoint accepts simple and complex stats queries in the POST request body and returns the metrics as JSON.
  - [2] 2026-10-30: API keys allow 600 requests per hour by default | capture: sha256:3536f727f4889db659d97c2027a80bab752c08f857b75f894c91c45c5d6e0196 | quote: API keys have a rate limit of 600 requests per hour by default.
  - [4] 2026-10-30: the Sites API is an Enterprise feature | capture: sha256:e0d27cc99df39d9c93194ad3d3256a3c6e549c7bfefc5cb093ef394069dacf77 | quote: Sites API: create and manage sites programmatically.
  - [6] 2026-10-30: the registration form asks for no card | capture: sha256:000b5044b5da0ad8aa03e6fa30e04d15dcc538704ca4bf428e947736160212e9 | quote: No credit card required. Cancel anytime.
  - [6] 2026-10-30: the registration form asks for a full name | capture: sha256:000b5044b5da0ad8aa03e6fa30e04d15dcc538704ca4bf428e947736160212e9 | quote: Full name
  - [6] 2026-10-30: the password needs at least 12 characters | capture: sha256:000b5044b5da0ad8aa03e6fa30e04d15dcc538704ca4bf428e947736160212e9 | quote: At least 12 characters
  - [6] 2026-10-30: the registration form is behind a Friendly Captcha check | capture: sha256:000b5044b5da0ad8aa03e6fa30e04d15dcc538704ca4bf428e947736160212e9 | quote: Friendly Captcha
  - [7] 2026-10-30: Plausible Community Edition is free, self-hosted and AGPL-licensed | capture: sha256:4e1656c4d91166675d5b585cf42a0c576e0dfa1068ce714bcd012496e5a7763f | quote: is the free, self-hosted, AGPL-licensed release: you run it on your own server and manage everything yourself.
  - [8] 2026-11-01: Plausible states that registration asks only for a name and an e-mail address | capture: sha256:fd11c0e977ce0b7c623a7ee0ab69a0363208b35d4081ecccd0036d4b11202f5a | quote: We only ask for your name and email, and the 30-day trial needs no credit card.
  - [9] 2026-11-01: an e-mailed four-digit code activates the account | capture: sha256:8f9036b3cbd965a68e19275695fcc42ea68f63b26d723cf7997b20929aaf557f | quote: Please enter the four digit code that we sent to you through email to activate your Plausible Analytics account.
  - [9] 2026-11-01: the 30-day trial starts as soon as the e-mailed code is verified | capture: sha256:8f9036b3cbd965a68e19275695fcc42ea68f63b26d723cf7997b20929aaf557f | quote: Once verified, your 30-day trial starts immediately.
  - [9] 2026-11-01: the registration form takes a full name, an e-mail address and a password | capture: sha256:8f9036b3cbd965a68e19275695fcc42ea68f63b26d723cf7997b20929aaf557f | quote: Fill in your full name and email address, choose your account password and click on the Start my free trial button.
- sources:
  - [1] https://plausible.io/docs/trial
  - [2] https://plausible.io/docs/stats-api
  - [3] https://plausible.io/
  - [4] https://plausible.io/docs/subscription-plans
  - [5] https://plausible.io/#pricing
  - [6] https://plausible.io/register
  - [7] https://plausible.io/self-hosted-web-analytics
  - [8] https://plausible.io/wordpress-analytics-plugin
  - [9] https://plausible.io/docs/register-account
