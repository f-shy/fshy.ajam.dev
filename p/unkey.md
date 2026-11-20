# Unkey

> unkey.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unkey/ | JSON https://fshy.ajam.dev/api/v1/entity/unkey.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Unkey

- `dev-services/unkey` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted API key management, key verification and rate limiting (API Management); a separate paid Compute product exists | tier Free (API Management)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:17:12.856Z (live) | stale on 2026-12-20
- url https://www.unkey.com/docs/platform/billing/limits
- free tier: Free API Management at USD 0 a month: 150,000 valid requests a month, 1,000 API keys, unlimited APIs, 7 days of request log retention and 30 days of audit log retention; team members need a paid API tier or Compute Pro or Business | unit: requests | metered on: request-count | read on: 2026-11-19 | source: [1] | note: Only valid key verifications and rate limit checks count. Rejected verifications do not count. A card is on file only to upgrade; the Free tier starts at USD 0. Compute is a separate paid product and is not part of this free allowance.
- per-object cap: unverified: no per-key or per-request size cap is stated on the pricing, plans or limits pages read
- retention: Request logs are kept 7 days and audit logs 30 days on the Free API Management tier; a paid API tier owns both retention values (90 days each) | days: 7 | source: [2] | note: The 7 days is request log retention. Audit log retention on Free is 30 days. Log drains are included on no plan.
- egress: not applicable to API Management: the free offer is a key verification and rate limiting service reached over its HTTPS API, and no data egress quota is stated for it | metered: no | source: [3]
- identity: email | detail: The sign-in form shows an Email field with a Continue with email button and Continue with Google and Continue with GitHub options; no phone or card is asked for to enter. The billing pages state a card is needed before upgrading, and the Free tier is USD 0. Whether a later dashboard step asks for a phone number is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 150,000 valid requests per month on Free [2]
  - volume-quota (binding): 1,000 API keys on Free [2]
  - retention-clamped: 7 days of request logs and 30 days of audit logs on Free [2]
  - request-rate: If a workspace is still on Free 5 days after passing the quota, requests to the Unkey API are limited to 5 per minute until it upgrades [2]
  - write-gated: Team members are not included on the Free API tier; they need a paid API tier or Compute Pro or Business [1]
- binding note: The 150,000 valid requests a month fills first for a live API; passing it emails the admins and a workspace still on Free 5 days later is cut to 5 API requests a minute. The Free tier also holds one user, since team members need a paid tier, and request logs are kept only 7 days.
- interface detail: Every API endpoint is an HTTP POST to api.unkey.com/v2/{service}.{procedure} with a root key in an Authorization Bearer header; /v2/liveness is a GET health route. An OpenAPI document is served at /openapi.yaml and a browsable reference at /reference. SDKs exist for TypeScript, Go and other languages.
- endpoint: https://api.unkey.com/v2/keys.verifyKey
- tooling: The @unkey/api TypeScript SDK, the unkeyed Go SDK, HTTP POST calls to api.unkey.com and the dashboard at app.unkey.com
- composes with: Issue keys and verify them from any service over HTTPS; combine with a separate API gateway or with Unkey Compute for deployment, which is a paid product outside the free allowance.
- reliability: Requests are not blocked on passing the quota immediately; admins are emailed and, if the workspace stays on Free 5 days later, the API is limited to 5 requests a minute until upgrade. Logs on Free are retained 7 days, so older failed verifications cannot be inspected.
- notes: Unkey bills API Management and Compute separately. This record covers the hosted, free API Management tier; Compute is a paid product. The open-source status is unverified and no self-hosted offer is asserted for API Management.
- evidence note: Quotas, retention and the over-quota throttle are quoted from first-party billing and limits pages. The sign-in fields come from the first-party sign-in page. Any gate shown only after registration is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-19: the Free API Management tier includes 150,000 billable operations a month | capture: sha256:356948791c13c204e321fa72082faef8fbd2689c9a401c64078ce2cf7fb23bdc | quote: 150,000 billable operations per month
  - [1] 2026-11-19: the Free tier keeps request logs 7 days | capture: sha256:356948791c13c204e321fa72082faef8fbd2689c9a401c64078ce2cf7fb23bdc | quote: 7 days of request log retention
  - [1] 2026-11-19: a card is required to upgrade but is not stated as needed to start Free | capture: sha256:356948791c13c204e321fa72082faef8fbd2689c9a401c64078ce2cf7fb23bdc | quote: You need a card on file before you can upgrade.
  - [2] 2026-11-19: the limits table gives 150,000 valid requests a month on Free | capture: sha256:e35af3a88a761b09af9d651e91140fac58e776003b52261b07a979dc2e4c29fe | quote: | Valid requests per month | 150,000 | 250,000 to 100,000,000 | Custom |
  - [2] 2026-11-19: the Free tier allows 1,000 API keys | capture: sha256:e35af3a88a761b09af9d651e91140fac58e776003b52261b07a979dc2e4c29fe | quote: | API keys | 1,000 | 1,000,000 | Custom |
  - [2] 2026-11-19: the Free tier keeps audit logs 30 days | capture: sha256:e35af3a88a761b09af9d651e91140fac58e776003b52261b07a979dc2e4c29fe | quote: | Audit log retention | 30 days | 90 days | Custom |
  - [2] 2026-11-19: a workspace still on Free 5 days after passing the quota is cut to 5 requests a minute | capture: sha256:e35af3a88a761b09af9d651e91140fac58e776003b52261b07a979dc2e4c29fe | quote: requests to the Unkey API are limited to 5 per minute until you upgrade
  - [3] 2026-11-19: the pricing page lists 150K valid requests a month on the Free plan | capture: sha256:932bbd0b32216aec33da897e3392193d041e6048d2f2bf1656996c5df391ab63 | quote: 150K valid requests / mo
  - [4] 2026-11-19: the sign-in form offers an email path with no card or phone field | capture: sha256:277aac3b077186fb06367792c0348eeb083d29ea95b8bb044b2e6c080b229280 | quote: Continue with email
- sources:
  - [1] https://www.unkey.com/docs/platform/billing/plans
  - [2] https://www.unkey.com/docs/platform/billing/limits
  - [3] https://unkey.com/pricing
  - [4] https://app.unkey.com/sign-up
