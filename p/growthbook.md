# GrowthBook

> growthbook.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/growthbook/ | JSON https://fshy.ajam.dev/api/v1/entity/growthbook.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GrowthBook

- `dev-services/growthbook` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted feature flags, A/B testing and product analytics | tier Starter (Cloud)
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:37:55.411Z (live) | stale on 2026-12-03
- url https://www.growthbook.io/pricing
- free tier: Starter: free with no credit card; up to 3 users and 1 project, unlimited feature flags, experiments and traffic; 1M CDN requests and 5 GB CDN bandwidth a month; managed warehouse 1M events a month | unit: mixed | read on: 2026-10-30 | source: [1] | note: The plan is counted in seats (one login each), CDN requests, CDN gigabytes and warehouse events; no single unit term fits. End-user traffic is not counted. The CDN figures are soft guidelines: an outlier is notified and the UI shows a CDN usage exceeded warning. SSO on Starter is Google only and roles are admin only; sequential testing, CUPED and multi-arm bandits are not on Starter.
- per-object cap: unverified: no feature or payload size limit is stated on the pages read
- retention: unverified: no retention period for managed-warehouse events or audit history is stated on the pages read
- egress: CDN delivery of flag payloads: 1M requests and 5 GB of bandwidth a month on Starter as soft guidelines; paid overage is USD 10 per additional million CDN requests and USD 1 per additional… | metered: yes | free allowance: 1M CDN requests and 5 GB of CDN bandwidth a month | source: [1]
- identity: email | detail: The pricing page states no credit card is required and that every user needs an own login and password. The Cloud register form at app.growthbook.io asks for a First Name, a Work Email Address and a Password, or offers Sign up with Google, and lists no phone or card field; GrowthBook documents a role chosen during signup and an organization and a project named when the account is created. Whether a later step asks for a phone number, and whether an address at a public mail domain passes as a Work Email Address, is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 1M CDN requests and 5 GB CDN bandwidth a month (soft guideline) [2]
  - volume-quota (binding): managed warehouse: 1M events a month [1]
  - request-rate: REST API: 60 requests per minute [3]
- limits note: 3 users and 1 project on Starter; the vocabulary has no kind for a seat count.
- binding note: Flag payloads are served from the CDN, so 1M CDN requests a month is the first ceiling for an app with traffic; it is enforced by notice, not a hard stop.
- interface detail: REST API at https://api.growthbook.io/api with a Secret Key or Personal Access Token over HTTP Basic or Bearer auth, 60 requests per minute (a GET /api/v1/features without a key answered 400 Missing Authorization header); an MCP server hosted for GrowthBook Cloud at https://mcp.growthbook.io/mcp, with sign-in through OAuth.
- endpoint: part of interface detail
- tooling: 24+ SDKs, the setup wizard (npx @growthbook/wizard), an MCP server, or any HTTP client against the REST API.
- composes with: Flags and experiments for apps on free compute, analysed in a warehouse the user already has or in the managed warehouse at 1M events a month.
- reliability: Usage above the CDN guidelines triggers a notice and a CDN usage exceeded warning in the UI rather than a stop.
- notes: Pro is USD 40 per seat a month with 2M CDN requests and 20 GB of CDN bandwidth included. GrowthBook is also open-source software that the user can install and run on a rented or free machine, with unlimited users; that is the last resort after the hosted Starter plan.
- evidence note: The REST API host was probed and answered 400 Missing Authorization header without a key. The identity kind rests on the login-and-password sentence and on the register form of the Cloud app as rendered in text.
- evidence:
  - [1] 2026-10-30: Starter is free with no card, up to 3 users, 1 project, unlimited flags, experiments and traffic | capture: sha256:f4f9de55fae56c5cb578cad8a8a4bc39d66201113e392f6fcfd48fd2fa8000b4 | quote: Free No credit card required - Up to 3 users - 1 project - Unlimited feature flags - Unlimited experiments - Unlimited traffic
  - [1] 2026-10-30: Starter is free for up to three users on the cloud platform | capture: sha256:f4f9de55fae56c5cb578cad8a8a4bc39d66201113e392f6fcfd48fd2fa8000b4 | quote: Yes. The Starter plan is free for up to three users and includes unlimited feature flags and experiments on GrowthBook's cloud platform
  - [1] 2026-10-30: each user needs an own login and password | capture: sha256:f4f9de55fae56c5cb578cad8a8a4bc39d66201113e392f6fcfd48fd2fa8000b4 | quote: A seat equals a user. All users of the GrowthBook platform must have their own login/password.
  - [1] 2026-10-30: exceeding CDN usage shows a warning | capture: sha256:f4f9de55fae56c5cb578cad8a8a4bc39d66201113e392f6fcfd48fd2fa8000b4 | quote: You will see a "CDN usage exceeded" warning in the UI.
  - [1] 2026-10-30: paid overages are USD 10 per million CDN requests and USD 1 per GB | capture: sha256:f4f9de55fae56c5cb578cad8a8a4bc39d66201113e392f6fcfd48fd2fa8000b4 | quote: Overages apply only after you exceed included usage: CDN Requests at $10 per additional million requests, CDN Bandwidth at $1 per additional GB
  - [1] 2026-10-30: a free self-hosted plan with unlimited users exists | capture: sha256:f4f9de55fae56c5cb578cad8a8a4bc39d66201113e392f6fcfd48fd2fa8000b4 | quote: The free self-hosted plan has unlimited users.
  - [1] 2026-10-30: Starter includes 1M CDN requests a month | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: | CDN Requests | 1M/mo | 2M/mo (then $10/M) | Custom |
  - [1] 2026-10-30: Starter includes 5 GB of CDN bandwidth a month | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: | CDN Bandwidth | 5GB/mo | 20GB/mo (then $1/GB) | Custom |
  - [1] 2026-10-30: the managed warehouse includes 1M events a month on Starter | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: | Managed Warehouse | 1M events/mo | 2M events/mo (then $30/M) | Custom |
  - [1] 2026-10-30: Starter SSO is Google only | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: | SSO | Google Only | Google Only | Custom OIDC |
  - [1] 2026-10-30: Starter roles are admin only | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: | Roles | Admin only | Basic roles | Custom roles |
  - [1] 2026-10-30: sequential testing is not on Starter | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: | Sequential Testing | - | | |
  - [1] 2026-10-30: CUPED is not on Starter | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: | CUPED / Variance Reduction | - | | |
  - [1] 2026-10-30: multi-arm bandits are not on Starter | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: | Multi-arm Bandits | - | | |
  - [1] 2026-10-30: Pro is USD 40 per seat a month | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: $40 / seat / month
  - [1] 2026-10-30: 24+ SDKs are available | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: 24+ SDKs
  - [1] 2026-10-30: an MCP server is available | capture: sha256:df1bc0b3945b899f0aa6db551ff74768313a554e4f283aa0dd55f79554b13c5c | quote: MCP Server
  - [2] 2026-10-31: free organizations are expected to stay within 1M CDN requests and 5 GB | capture: sha256:34460a4a2fd5adce76eac22d40c5beaa8a6c217bc6fb36843d7af28892b6508e | quote: Organizations on Free plans are expected to use up to 1 million CDN requests and consume up to 5GB of CDN bandwidth.
  - [2] 2026-10-31: outlier usage is notified | capture: sha256:34460a4a2fd5adce76eac22d40c5beaa8a6c217bc6fb36843d7af28892b6508e | quote: We will notify you if your usage is an outlier.
  - [2] 2026-10-31: end-user traffic is not limited | capture: sha256:34460a4a2fd5adce76eac22d40c5beaa8a6c217bc6fb36843d7af28892b6508e | quote: Furthermore we do not have any limits on the amount of traffic you get per month (MTU/MAU).
  - [4] 2026-10-31: Starter is USD 0, no card, 3 users in 1 project | capture: sha256:261fc7ff3b05e3b90d76bd63ff665f5172f710475cf1f1ad59c92f0e541b2de6 | quote: The current cloud Starter plan costs $0, requires no credit card, and supports up to 3 GrowthBook users in 1 project.
  - [3] 2026-10-31: the API base URL is api.growthbook.io/api | capture: sha256:3e0b5c641949e7ebc50c94f3e8a18b9b1b7e211531bd34ed3f8d3c0557f626d3 | quote: The API base URL for GrowthBook Cloud is `https://api.growthbook.io/api`.
  - [3] 2026-10-31: the API takes HTTP Basic or Bearer auth | capture: sha256:3e0b5c641949e7ebc50c94f3e8a18b9b1b7e211531bd34ed3f8d3c0557f626d3 | quote: We support both the HTTP Basic and Bearer authentication schemes for convenience.
  - [3] 2026-10-31: the REST API allows 60 requests a minute | capture: sha256:3e0b5c641949e7ebc50c94f3e8a18b9b1b7e211531bd34ed3f8d3c0557f626d3 | quote: You exceeded the rate limit of 60 requests per minute
  - [5] 2026-10-31: a setup wizard exists | capture: sha256:1f98eb8ad7eff8c309ae5f03b0b7fe7aa8bacde1e75a038388ed2ba6980abb1e | quote: run `npx @growthbook/wizard` from your project directory
  - probe:https://api.growthbook.io/api/v1/features 2026-10-31: api.growthbook.io answers a request without a key with Missing Authorization header | capture: sha256:6822ec1eb9ff38d2d71d6dc7095a65c72a3e35c7b00be161ef926fd00949efa3 | quote: {"message":"Missing Authorization header"}
  - [6] 2026-11-01: the Cloud register form lists First Name, Work Email Address and Password | capture: sha256:019823a11d0bcee1628cd3b70c1234d2297721c22f121fcd48fd2230ec744fc4 | quote: First Name Work Email Address Password
  - [7] 2026-11-01: a second render of the Cloud app lists the same register fields | capture: sha256:cbc47ab5223722758acef4569569585319247abe1788bdfd3fd91d6e95d67ae7 | quote: First Name Work Email Address Password
  - [6] 2026-11-01: the register form offers Sign up with Google | capture: sha256:019823a11d0bcee1628cd3b70c1234d2297721c22f121fcd48fd2230ec744fc4 | quote: Sign up with Google
  - [8] 2026-11-01: the signup lets the creator of an organization select a role | capture: sha256:ae1d3b25b463fe6342babb836f4141c4fbc44129a2e8b323b5c548707632624b | quote: GrowthBook currently shows this setup flow only for organizations whose creator selected Engineering as their role during signup.
  - [9] 2026-11-01: creating a Cloud Starter account names an organization and a project | capture: sha256:db5fec04c3be7a898279d3d8945b8a1e99d6bd523079aa4a225a5e0a8b95795d | quote: Name the organization and project after the real product rather than this one flag.
  - [9] 2026-11-01: a GrowthBook seat is an individual platform user, not an end user who receives flags | capture: sha256:db5fec04c3be7a898279d3d8945b8a1e99d6bd523079aa4a225a5e0a8b95795d | quote: Seats are individual platform users; application end users who receive flags do not use seats.
  - [10] 2026-11-01: GrowthBook Cloud has a hosted MCP server that signs in through OAuth | capture: sha256:90163e1991072802977f32816403d5dca3a1c19b9deaa2394f8304b2eacc7b81 | quote: If you use [GrowthBook Cloud](https://app.growthbook.io), connect your MCP client to the hosted server. You sign in with OAuth in the browser — no API key in the MCP config.
  - [10] 2026-11-01: the hosted MCP endpoint of GrowthBook Cloud is https://mcp.growthbook.io/mcp | capture: sha256:90163e1991072802977f32816403d5dca3a1c19b9deaa2394f8304b2eacc7b81 | quote: | `https://mcp.growthbook.io/mcp` | Skills + API read/write (recommended) |
- sources:
  - [1] https://www.growthbook.io/pricing
  - [2] https://www.growthbook.io/legal/fair-use-policy
  - [3] https://docs.growthbook.io/api
  - [4] https://www.growthbook.io/insights/growthbook-starter-plan
  - [5] https://docs.growthbook.io/quick-start
  - [6] https://app.growthbook.io/
  - [7] https://app.growthbook.io/login
  - [8] https://docs.growthbook.io/integrations/ai-agents/wizard
  - [9] https://www.growthbook.io/insights/first-feature-flag
  - [10] https://docs.growthbook.io/integrations/mcp
