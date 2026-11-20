# Permit.io

> permit.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/permit/ | JSON https://fshy.ajam.dev/api/v1/entity/permit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Permit.io

- `dev-services/permit-io` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted authorization as a service (RBAC, ReBAC, ABAC) with a managed Cloud PDP and a cloud control plane; self-hosted Edge and Nexus PDP options also exist | tier Community (Free Forever)
- needs card no, phone unknown, ID no, institution no | verified 2026-11-20T04:15:45.452Z (live) | stale on 2026-12-21
- url https://www.permit.io/pricing
- free tier: Community plan, labeled Free Forever: up to 1,000 monthly active users (MAU), 20 tenants, no limit on authorization queries, 25 roles, 50 resource types, 3 environments, no limit on projects or PDP instances, and 14 days of log retention; the pricing table lists its pricing model as Free | unit: users | metered on: identity-count | read on: 2026-11-19 | source: [1] | note: The meter is monthly active users, not check calls: authorization queries have no limit on the Community plan. The named plan on the payment page is Community FREE FOREVER at USD 0. The managed Cloud PDP is the hosted decision point; the Edge and Nexus PDPs are containers the user runs and are not this hosted offer.
- per-object cap: unverified: no per-object byte size cap is stated; the Community plan caps object counts at 2,000 role assignments, 2,000 resource instances and 2,000 relationship tuples, with 25 roles and 50 resource types | source: [1]
- retention: Logs retention is 14 days on the Community plan; the paid Pro plan lists 14-day audit-log retention as extendable | days: 14 | source: [1] | note: The 14-day figure is from the Community column of the first-party pricing table. Decision logs appear on the Audit Log screen.
- egress: not applicable to authorization decisions: the Cloud PDP answers checks over HTTPS at cloudpdp.api.permit.io, and no data egress quota is stated for the Community plan | metered: no | source: [2]
- identity: email | detail: The first-party quickstart says to sign up at app.permit.io and states users can sign in with a Google, GitHub or Microsoft account, or use enterprise SSO; an email address underlies those sign-ins. The Community pricing table lists its pricing model as Free. Whether the sign-up form asks for a phone number is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 1,000 monthly active users (MAU) on Community [1]
  - volume-quota (binding): 20 tenants, 25 roles, 50 resource types and 3 environments on Community [1]
  - volume-quota (binding): 2,000 role assignments, 2,000 resource instances and 2,000 relationship tuples on Community [1]
  - per-ip-shaping: Cloud PDP: 1000 req/min for /allowed, 3000 req/min across all requests, per client IP over a 1-minute window; over-limit requests get HTTP 429 [2]
  - request-rate: Cloud PDP: 200 req/min for /allowed/bulk and 500 req/min for /user-permissions and /authorized_users per client IP [2]
  - retention-clamped: 14 days of logs retention on Community [1]
- binding note: The 1,000 MAU cap binds before the per-IP rate limits for a growing application: authorization queries are unlimited, so the count is active users, not checks. The Cloud PDP also shapes requests per client IP at 1000 req/min on /allowed, and logs are kept only 14 days.
- interface detail: The managed Cloud PDP serves HTTPS check endpoints /allowed, /allowed/bulk, /user-permissions and /authorized_users plus the AuthZen evaluation and search endpoints; SDKs exist for Node.js, Go, .NET, Java, Python and Ruby. The control plane is configured through the dashboard, an API, SDKs, a Terraform provider and GitOps.
- endpoint: https://cloudpdp.api.permit.io/allowed
- tooling: The permitio SDKs for Node.js, Go, .NET, Java, Python and Ruby, the Permit API, the Permit CLI and the dashboard at app.permit.io; an SDK points at the Cloud PDP by setting its PDP URL
- composes with: Applications call permit.check() against the managed Cloud PDP; policy is authored in the cloud control plane. The self-hosted Edge PDP and Nexus PDP are alternatives for ABAC or in-network decisions and are not the hosted free offer.
- reliability: The managed Cloud PDP applies per-IP rate limits over a 1-minute window and returns HTTP 429 with an error body of rate_limited when a client exceeds them; a large deployment behind a shared public IP can be affected. Cloud uptime is stated as best effort on the Community plan.
- notes: The Community plan is the hosted offer. Permit also publishes open-source PDP components and self-hosted Edge and Nexus PDPs, which are last-resort options and are not counted as this hosted record. The sign-in page at app.permit.io was login-walled; its gate was read from the first-party quickstart instead. unverified: behind a sign-up — the later steps of the sign-up form were not visible in a keyless read on 2026-11-20, so a card or phone requirement at those steps cannot be stated.
- evidence note: Quotas, object counts and retention are quoted from the first-party pricing tables; rate limits and the check endpoint come from first-party PDP documentation; sign-in options come from the first-party quickstart. Registration gates beyond the documented sign-in options are unverified: behind a sign-up.
- self hosted: no
- evidence:
  - [1] 2026-11-19: the Community plan allows 1,000 monthly active users | capture: sha256:0c36fa474f43af4360fe9de88dfcd6905b113b32382d20b4dde9576ad57a2cb2 | quote: MAU | 1000
  - [1] 2026-11-19: authorization queries are unlimited on Community, so the meter is users not checks | capture: sha256:0c36fa474f43af4360fe9de88dfcd6905b113b32382d20b4dde9576ad57a2cb2 | quote: Authorization Queries | No Limit
  - [1] 2026-11-19: the Community plan retains logs 14 days | capture: sha256:0c36fa474f43af4360fe9de88dfcd6905b113b32382d20b4dde9576ad57a2cb2 | quote: Logs Retention | 14 days
  - [1] 2026-11-19: the Community plan places no limit on PDP instances | capture: sha256:0c36fa474f43af4360fe9de88dfcd6905b113b32382d20b4dde9576ad57a2cb2 | quote: PDP Instances | No Limit
  - [3] 2026-11-19: the payment page labels the free Community plan with 1,000 MAU and 20 tenants | capture: sha256:d7059e9c62d6b4e18ea0b1879e281e54b7876e6d4ae71b4f56038b189856e734 | quote: 1000 MAU , 20 Tenants
  - [3] 2026-11-19: the free Community plan is labeled Free Forever | capture: sha256:d7059e9c62d6b4e18ea0b1879e281e54b7876e6d4ae71b4f56038b189856e734 | quote: FREE FOREVER
  - [2] 2026-11-19: the managed Cloud PDP shapes checks per client IP at 1000 and 3000 requests a minute | capture: sha256:50205b0dbce02b375dfb410c60787c787d8c311955a3e0d9fca488f15be3fec1 | quote: 1000 req/min for `/allowed`, and 3000 req/min across all requests
  - [2] 2026-11-19: the Cloud PDP is a hosted decision point reached over HTTPS | capture: sha256:50205b0dbce02b375dfb410c60787c787d8c311955a3e0d9fca488f15be3fec1 | quote: Managed by Permit, served over HTTPS at `https://cloudpdp.api.permit.io`.
  - [4] 2026-11-19: registration uses a social or enterprise identity rather than a card | capture: sha256:44319e973669016befba5c977a7d9d7aad97e2265a31798c254ef5ffdc25a303 | quote: You can sign in with a Google, GitHub, or Microsoft account.
  - [4] 2026-11-20: a first-party page was read on 2026-11-20; the sign-up gate keeps later form steps unverified | capture: sha256:44319e973669016befba5c977a7d9d7aad97e2265a31798c254ef5ffdc25a303 | quote: Sign up at [app.permit.io](https://app.permit.io/). You use the account to configure and manage the authorization layer of your application.
- sources:
  - [1] https://www.permit.io/pricing
  - [2] https://docs.permit.io/concepts/pdp/cloud-pdp-capabilities
  - [3] https://payment.permit.io/
  - [4] https://docs.permit.io/getting-started/quickstart/
