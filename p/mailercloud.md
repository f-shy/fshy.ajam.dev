# Mailercloud

> mailercloud.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mailercloud/ | JSON https://fshy.ajam.dev/api/v1/entity/mailercloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mailercloud

- `email/mailercloud` | qualifies-with-caveat | evidence documented | binding volume-quota | category email marketing sender and campaign API
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T00:19:24.838Z (live) | stale on 2026-12-20
- url https://www.mailercloud.com/pricing
- free tier: Free forever: 12,000 emails per month to 1,000 contacts, no credit card required | unit: requests | metered on: request-count | read on: 2026-11-19 | source: [1] | note: This is the Marketing Platform free plan. The platform also sells a separate Email API for transactional sending from USD 10/month, opened by a 14-day free trial with 100 emails per signup and no card; the two products are billed separately.
- per-object cap: not applicable: an outbound email sender
- retention: unverified: the free Marketing Platform plan's activity retention period is not stated on the first-party pricing page | source: [1] | note: The paid Email API states 7 days of activity retention on Basic and 30 days on Pro, but no retention figure is published for the free Marketing Platform plan.
- egress: not applicable: an outbound email sender; the free tier's 12,000 monthly sends are counted, not billed per GB | metered: no | source: [1]
- identity: any-phone | detail: The signup form asks for first name, last name, email, a phone number with a country selector, and a password; Google and Microsoft single sign-on are offered as alternatives. No card is required at signup. Sending needs a verified sender domain.
- interface: rest
- limits:
  - volume-quota (binding): 12,000 emails per month on the free Marketing Platform plan [1]
  - volume-quota (binding): 1,000 contacts on the free Marketing Platform plan [1]
  - per-ip-shaping: 50 requests per second per client IP, sliding one-second window, on the Marketing API [2]
- binding note: 12,000 sends a month to 1,000 contacts is the first ceiling a free sender reaches; the 50 request-per-second per-IP shaping then binds on the Marketing API
- interface detail: the Marketing API at cloudapi.mailercloud.com/v1 (campaigns, contacts, lists, segments, webhooks, automations), plus the web app; a separate Email API at email-api.mailercloud.com handles transactional sends on paid plans
- endpoint: https://cloudapi.mailercloud.com/v1
- tooling: any HTTP client against the Marketing API with an API key in the Authorization header; the web app sends campaigns and automations
- composes with: a 12,000-send monthly free sender driven from the Marketing API or web app, with a 50 request per second per-IP shaping on the API; pair it with the paid Email API when transactional sends are needed
- reliability: The Marketing API shapes requests per client IP; exceeding 50 per second returns HTTP 429 with no Retry-After header, so clients must back off on their own. No public read path exists for an outbound sender, so no probe was run.
- notes: A free-forever Marketing Platform sender with a 12,000 monthly send ceiling and a 50 request-per-second per-IP shaping on its REST API. The separate transactional Email API is a 14-day trial with 100 emails, not a free-forever tier. Free-plan activity retention is not published.
- evidence note: Quota, identity, interface and limits come from first-party pricing, signup and API pages. No send was made, so delivery is not measured; a measured rung would need an account and a send.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-11-19: the free Marketing Platform plan is free forever, allows 12,000 emails a month to 1,000 contacts, and needs no card | capture: sha256:139da042366cc4d8a66552c5ed40127fb3aae525f4c86eb90991c265ae9e3709 | quote: Yes. The Free plan is free forever with 12,000 emails a month to 1,000 contacts, and no credit card is required to start.
  - [1] 2026-11-19: the comparison table confirms the 12,000 monthly send ceiling on the free plan | capture: sha256:139da042366cc4d8a66552c5ed40127fb3aae525f4c86eb90991c265ae9e3709 | quote: | Emails per month | 12,000 | Unlimited | Unlimited |
  - [1] 2026-11-19: the comparison table confirms the 1,000 contact ceiling on the free plan | capture: sha256:139da042366cc4d8a66552c5ed40127fb3aae525f4c86eb90991c265ae9e3709 | quote: | Contacts | 1,000 | 1,000 | Custom |
  - [2] 2026-11-19: the Marketing API shapes requests per client IP at 50 per second in a sliding one-second window | capture: sha256:5f95d5833960bf9b7f784f11b125d6ec289f28e4b15a4b894e002b43fb487546 | quote: Requests are rate-limited per client IP using a sliding one-second window of 50 requests per second (higher limits can be arranged for specific IPs — contact support).
  - [2] 2026-11-19: a 429 carries no server-provided retry time, so clients must implement their own backoff | capture: sha256:5f95d5833960bf9b7f784f11b125d6ec289f28e4b15a4b894e002b43fb487546 | quote: The API does not currently send `X-RateLimit-*` or `Retry-After` headers. Clients — especially AI agents doing batch work — should treat any `429` as a signal to back off exponentially rather than expecting a server-provided retry time.
  - [3] 2026-11-19: the signup form requires first name, last name, email and a phone number; no card field is present | capture: sha256:540379204b160a9bdbc9a6228d60fc4895b3819a16a64838ec877bb1d2e5dea3 | quote: Or Sign up in with email First name\* Last name\* Email\* Phone\*
  - [4] 2026-11-19: a documented REST Marketing API is the programmatic access path | capture: sha256:5f0725a4993e1aa2e8ae30d5e75136d657361827e8f137314c7c35dff120e32c | quote: | Marketing API — campaigns, contacts, lists, segments, webhooks, automations | `https://cloudapi.mailercloud.com/v1` | [Marketing API](https://apidoc.mailercloud.com/api-reference) |
  - [5] 2026-11-19: the API needs an API key in the Authorization header | capture: sha256:8d00ce377438461c58b7779cc766a54db048ec47dc985c12a7417f9cc4c60b17 | quote: To use this API, you need an API key for authentication.
  - [6] 2026-11-19: the separate transactional Email API is opened by a 14-day trial with 100 emails and no card | capture: sha256:3a24e1e17dc7163e63553d929fbeaf1a6afd5c77158b4261b222d73620f6dd52 | quote: No card required. Every plan starts with a 14-day free trial, and each signup includes 100 emails to test your integration before you commit.
- sources:
  - [1] https://www.mailercloud.com/pricing
  - [2] https://apidoc.mailercloud.com/rate-limits.md
  - [3] https://app.mailercloud.com/register
  - [4] https://apidoc.mailercloud.com/
  - [5] https://help.mailercloud.com/en/articles/155-mailercloud-email-api-help-guide
  - [6] https://www.mailercloud.com/pricing/api
