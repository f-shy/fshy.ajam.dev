# SocketLabs

> socketlabs.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/socketlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/socketlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SocketLabs

- `email/socketlabs` | trial-only | evidence documented | binding retention-clamped | category transactional email sender and SMTP relay | tier Core 40k Free Trial
- needs card no, phone unknown, ID no, institution no | verified 2026-11-19T00:19:24.920Z (live) | stale on 2026-12-20
- url https://www.socketlabs.com/pricing/
- free tier: No permanent free tier. After an account is created and verified, a free trial gives Core plan access for one month, or a set amount of credits, with no credit card required. The Core plan allows 40,000 emails per month and costs USD 39.95 per month after the trial. | unit: requests | metered on: request-count | read on: 2026-11-19 | source: [1] | note: This is a one-month trial, not a continuing free tier. At the end of the trial the account loses platform access and can no longer send unless it upgrades to a paid plan. Public email accounts such as Gmail are not accepted at signup, so a work or private domain email is needed.
- per-object cap: not applicable: an outbound transactional sender | source: [2]
- retention: Free trial access lasts one month, after which platform access and sending stop without a paid upgrade. The exact reporting-history day windows are unverified: the first-party pricing page renders its feature table without day values. | source: [3] | note: The API docs state that returned data is limited to the Detailed Reporting History date range of the plan, but give no day counts. Day counts found on third-party pages were not used.
- egress: not applicable: an outbound email sender; volume is counted in emails sent, not in bytes transferred | metered: no | source: [3]
- identity: email | detail: It refuses public domains: 'Public accounts such as Gmail are not accepted'. Account creation passes a two-step review, with an automated analysis and then a human review; the approval guidance asks to 'Provide a valid phone number where you can be reached' and requires a publicly accessible business website. A phone number appears in the review guidance, but whether it is a mandatory form field is unverified: behind a sign-up.
- interface: rest
- limits:
  - retention-clamped (binding): the free trial is one month of Core access; sending stops at the end of the trial without a paid plan [3]
  - volume-quota: 40,000 emails per month on the Core trial plan [1]
  - request-rate: the SocketLabs API is limited to 100 requests within 60 seconds; excess requests return an error; the /reports/message* endpoints are limited to 30 requests per 60 seconds [4]
- binding note: The free access is one month, after which sending stops without a paid plan, so the trial window fails before the 40,000-email monthly allowance or the 100 requests per 60 seconds API rate is reached.
- interface detail: The primary access path is SMTP relay on ports 25, 2525, 465 (SSL) and 587 (TLS), plus the HTTP Injection API. The schema has no SMTP interface term, so rest is used as the nearest term for the HTTP Injection API.
- tooling: any SMTP client, the HTTP Injection API, or first-party SDKs in C#, PHP, Node.js, Python, Go, Java and Ruby
- composes with: an outbound transactional sender with no inbound storage, used by an application that sends over SMTP or HTTP injection; the one-month trial window and the 40,000-email monthly Core allowance bound any sustained stack
- reliability: New accounts are throttled during an automatic warm-up period over the first weeks of service; by default a server that exceeds its monthly allowance by more than double is temporarily suspended.
- notes: SocketLabs has no permanent free tier. The only no-cost access is a one-month Core trial after account verification; public email domains are refused at signup and all new accounts pass a two-step review that may ask for a phone number. The exact reporting-history day windows are unverified on the first-party pages.
- evidence note: Every number comes from first-party SocketLabs pages captured: the signup form, the pricing FAQ, the API docs, the integration page and the help center. Delivery is not measured; no probe was run.
- evidence:
  - [1] 2026-11-19: the Core free trial allows 40,000 emails per month | capture: sha256:ef24ca293fa2239c90ac23291bd6e6fe4ddef7f06a05bafbb3a018cf3c6c0bd3 | quote: Core 40k Free Trial 40,000 emails per month
  - [1] 2026-11-19: the free first month needs no card; after it the Core plan costs USD 39.95 per month and sending stops without an upgrade | capture: sha256:ef24ca293fa2239c90ac23291bd6e6fe4ddef7f06a05bafbb3a018cf3c6c0bd3 | quote: Your first month is free and no credit card is required to get started. To continue services after your trial ends you will need to add payment details for $39.95/month.
  - [1] 2026-11-19: the signup refuses public email domains such as Gmail, so a work or private domain email is required | capture: sha256:ef24ca293fa2239c90ac23291bd6e6fe4ddef7f06a05bafbb3a018cf3c6c0bd3 | quote: Public accounts such as Gmail are not accepted
  - [1] 2026-11-19: the signup form states that no card is required and calls for a full name, a company name and a company email | capture: sha256:ef24ca293fa2239c90ac23291bd6e6fe4ddef7f06a05bafbb3a018cf3c6c0bd3 | quote: Set up is fast, easy, and no credit card is required!
  - [3] 2026-11-19: the free trial gives one month of Core access after the account is verified | capture: sha256:d958bcf961d1e9cb9d156e666919cdb392906f4e8375ca958239da49c97b7ae0 | quote: Once you create and verify your account, you have access to a Core plan for one month OR you will receive a set amount of credits to use.
  - [3] 2026-11-19: no card is required and platform access and sending end when the trial ends without an upgrade | capture: sha256:d958bcf961d1e9cb9d156e666919cdb392906f4e8375ca958239da49c97b7ae0 | quote: We do not require a credit card or payment method, but you will lose access to the platform and will no longer be able to send mail at the end of your trial if you do not upgrade to a paid plan.
  - [4] 2026-11-19: the SocketLabs API is rate-limited to 100 requests per 60 seconds | capture: sha256:0a9483b3ee8acd55ddca5f2a17941e7ca37d866ecfcebf75828679148ea21755 | quote: All requests against the SocketLabs Api are limited to 100 requests within 60 seconds. Requests made in excess to this limit will result in an error.
  - [4] 2026-11-19: the reporting endpoints are limited to 30 requests per 60 seconds | capture: sha256:0a9483b3ee8acd55ddca5f2a17941e7ca37d866ecfcebf75828679148ea21755 | quote: 30 requests/60 seconds
  - [4] 2026-11-19: reporting-history depth is plan-dependent and no day count is given on this page | capture: sha256:0a9483b3ee8acd55ddca5f2a17941e7ca37d866ecfcebf75828679148ea21755 | quote: Data returned by the SocketLabs API is limited to the dates allowed by the Detailed Reporting History date range for your SocketLabs plan.
  - [2] 2026-11-19: SocketLabs offers SMTP and an HTTP API with first-party SDKs in seven languages | capture: sha256:109c5848d294b84cb82e4794d4f61722d36ba4a6245f19d8a948de866dfb64dc | quote: Send email via SMTP or our flexible API, available in C#, PHP, Node.js, Phython, GoLang, Java, and Ruby
  - [5] 2026-11-19: all new accounts pass an automated check and then a human review | capture: sha256:a246c0fcdbd20de5a270b474802e9528b7326c8953b7b9a0dd8b0dfa03cc1ec7 | quote: The second step for all new account requests is a human review process.
  - [5] 2026-11-19: the approval guidance asks for a valid phone number as part of the review | capture: sha256:a246c0fcdbd20de5a270b474802e9528b7326c8953b7b9a0dd8b0dfa03cc1ec7 | quote: Provide a valid phone number where you can be reached. We might reach out with any questions we have about your intended use of our services.
  - [6] 2026-11-19: new accounts are throttled during an automatic warm-up period | capture: sha256:c7fdfbc9a56ab1284915d11271ccb2da77b6ccc854278d7e1c4e8f0d00350958 | quote: To do this, we will initially throttle the rate at which we deliver your email.
  - [6] 2026-11-19: servers that exceed the monthly allowance by more than double are suspended by default | capture: sha256:c7fdfbc9a56ab1284915d11271ccb2da77b6ccc854278d7e1c4e8f0d00350958 | quote: By default, servers that exceed their allowances by more than double will be temporarily suspended.
- sources:
  - [1] https://signup.socketlabs.com/
  - [2] https://www.socketlabs.com/hub/api-smtp
  - [3] https://www.socketlabs.com/pricing/
  - [4] https://docs.socketlabs.com/
  - [5] https://help.socketlabs.com/docs/why-is-my-request-for-a-new-account-still-pending
  - [6] https://help.socketlabs.com/docs/quick-start-guide
