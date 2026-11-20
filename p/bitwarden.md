# Bitwarden Secrets Manager

> bitwarden.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bitwarden/ | JSON https://fshy.ajam.dev/api/v1/entity/bitwarden.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bitwarden Secrets Manager

- `dev-services/bitwarden-secrets-manager` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted developer secrets management, end-to-end encrypted vault with a web app, CLI and REST API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:28:50.540Z (live) | stale on 2026-12-20
- url https://bitwarden.com/products/secrets-manager
- free tier: Free subscription: unlimited secret storage with up to 2 users, up to 3 projects, and up to 3 machine accounts; a free 14-day trial is offered for the paid tiers | unit: unlimited | metered on: none | read on: 2026-11-19 | source: [1] | note: The headline quantity is unlimited secret storage. The free offer also caps users at 2, projects at 3 and machine accounts at 3. Paid Teams and Enterprise include up to 20 and 50 machine accounts and charge USD 1 for each additional machine account.
- per-object cap: unverified: no per-secret size limit is stated on the first-party pages read | source: [2]
- retention: stored secrets have no stated automatic expiry; on deletion a secret moves to Trash for 30 days and is then permanently deleted and cannot be recovered | source: [2] | note: The 30-day figure is the post-deletion Trash window, not an automatic lifetime for stored secrets. Event logs on paid tiers are retained indefinitely with a 367-day viewing window.
- egress: not a byte-transfer service: a secrets vault reached through the web app, the bws CLI and a REST API; the Public API returns 429 Too Many Requests when hit too quickly and the CLI warns that many sessions from one IP in a short span may hit rate limits. No per-GB egress charge is stated. | metered: no | source: [3]
- identity: email | detail: Email and a master password: the account page says 'Enter your Email address and choose your preferred server location', then 'Bitwarden will email you a verification link', and the free-account page states 'No credit card required!'. No phone number, ID document or institution is asked. Secrets Manager is then enabled inside an organization, and only owners can add it.
- interface: rest, cli
- limits:
  - volume-quota (binding): up to 2 users on Free [4]
  - volume-quota (binding): up to 3 projects on Free [4]
  - volume-quota (binding): up to 3 machine accounts on Free, USD 1 per additional machine account on paid tiers [5]
  - per-ip-shaping: many separate access-token sessions from the same IP address in a short span of time may encounter rate limits [6]
  - request-rate: Public API returns 429 Too Many Requests when hit too quickly; no numeric rate is stated [3]
- limits note: Each secret belongs to a single project at a time, and a machine account sees only secrets in projects it can access.
- binding note: Secret storage is unlimited, so the free-tier count ceilings of 3 machine accounts, 3 projects and 2 users bind before any storage quantity.
- interface detail: A REST Public API compatible with OpenAPI Specification 3 with a published swagger.json, at https://api.bitwarden.com or https://api.bitwarden.eu for cloud, authenticating with OAuth2 client credentials bearer tokens. The bws CLI reads and writes secrets through machine-account access tokens and injects them as environment variables. The SDK has a Rust core with C++, C#, Go, Java, JS, PHP, Python and Ruby wrappers. A web vault exists for setup, but programmatic access is through the REST API and CLI.
- endpoint: part of interface detail
- tooling: The bws CLI, installed with curl https://bws.bitwarden.com/install | sh or run as the ghcr.io/bitwarden/bws Docker image, the Bitwarden SDK wrappers (Python, Java, Go, C#, JS, PHP, Ruby, C++, Rust) and the Public REST API
- composes with: Store CI/CD and application credentials in an end-to-end encrypted hosted vault and inject them at runtime through the bws CLI or an SDK using scoped machine-account access tokens.
- reliability: An access token appears once at creation and cannot be retrieved later. The Public API returns 429 when hit too quickly and CLI sessions sharing an IP in a short span may be rate limited. No data loss or ban is stated on the pages read.
- notes: A hosted service: the vendor runs the vault, while the bws CLI and SDK are clients the user runs. The free tier stores unlimited secrets but caps users, projects and machine accounts, and enabling the product is gated to organization owners. The per-secret size limit is unverified.
- evidence note: All values are quoted from first-party pricing, help and signup pages captured on 2026-11-19. No probe was run, so the read path is documented rather than measured. The per-secret size cap is unverified and no account was opened.
- evidence:
  - [1] 2026-11-19: the free subscription gives unlimited secret storage and caps users at 2, projects at 3 and machine accounts at 3 | capture: sha256:0270dea4efa52810f2602e601afe3d57099107a4ae7949772ec3b161e3fe968f | quote: Bitwarden Secrets Manager offers a free subscription with unlimited secret storage and up to 2 users, 3 projects, and 3 machine accounts.
  - [4] 2026-11-19: the Free plan limits are 2 users, 3 projects and 3 machine accounts | capture: sha256:ba0c746d767eff53d882cb681b3640f6fb59ec86b0697d87f95afc0a637e7cd9 | quote: - Up to 2 users - Up to 3 [projects](https://bitwarden.com/help/projects/) - Up to 3 [machine accounts](https://bitwarden.com/help/machine-accounts/)
  - [5] 2026-11-19: paid tiers include 20 or 50 machine accounts and charge USD 1 for each additional machine account | capture: sha256:9a37fb3aa88e093fad635776f2967f946071c840385c913b84408a13734fb758 | quote: Up to 20 machine accounts, $1 per additional machine account
  - [2] 2026-11-19: a deleted secret stays in Trash for 30 days before permanent deletion | capture: sha256:ddf384c2e0d42173bd14fde0a0c9cfd3bde3f8d686047f966acfe1cb337c228d | quote: When you delete a secret, it moves to Trash for 30 days. After that time, it will be permanently deleted.
  - [2] 2026-11-19: a secret belongs to one project at a time | capture: sha256:ddf384c2e0d42173bd14fde0a0c9cfd3bde3f8d686047f966acfe1cb337c228d | quote: Each secret can only be associated with a single project at a time.
  - [6] 2026-11-19: CLI sessions sharing an IP in a short span may encounter rate limits | capture: sha256:db6529ab8fb67b87419dc58411e17b54d4b440a6da2753c4323b73111483aaf7 | quote: If your workflow uses many separate sessions (where each use of an access token to authenticate constitutes a "session") to make requests from the same IP address in a short span of time, you may encounter rate limits.
  - [3] 2026-11-19: the Public API answers 429 Too Many Requests when hit too quickly | capture: sha256:b8fc42d0271961a4ffdc23f2e0745e317af7253c9ba6c6f43e307ace13d9def9 | quote: | `429 Too Many Requests` | Too many requests hit the API too quickly. We recommend scaling back the number of requests. |
  - [3] 2026-11-19: the cloud-hosted Public API endpoints are api.bitwarden.com and api.bitwarden.eu | capture: sha256:b8fc42d0271961a4ffdc23f2e0745e317af7253c9ba6c6f43e307ace13d9def9 | quote: For cloud-hosted, `https://api.bitwarden.com` or `https://api.bitwarden.eu`.
  - [7] 2026-11-19: account creation asks for an email address and a server location and verifies by email | capture: sha256:e25d7ca904e24ddbabf4eec317864fef301087a4148894ad487a64c256afae7c | quote: Enter your Email address and choose your preferred server location
  - [8] 2026-11-19: the free account needs no credit card | capture: sha256:9644258feeeffe2594e918261137fd53ef2725e6a2d3c76b432f005186552a59 | quote: Generate, protect, and securely share unlimited passwords for free. No credit card required!
  - [1] 2026-11-19: the programmatic clients named are the web app and the CLI | capture: sha256:0270dea4efa52810f2602e601afe3d57099107a4ae7949772ec3b161e3fe968f | quote: Secrets Manager is tailored for infrastructure secrets and is supported only by the web app and CLI clients.
  - [9] 2026-11-19: enabling Secrets Manager is gated to organization owners | capture: sha256:08e69e001e151e070be22438988fd7471e258980ce1bb94bc85cd475ca716fcf | quote: Only owners can add Secrets Manager to their organization.
  - [9] 2026-11-19: the access token is shown once and cannot be retrieved later | capture: sha256:08e69e001e151e070be22438988fd7471e258980ce1bb94bc85cd475ca716fcf | quote: Copy your token to somewhere safe before closing this window, as your token** cannot be retrieved later**
  - [10] 2026-11-19: the SDK has a Rust core with bindings for several languages | capture: sha256:600576a2613f28025b7ec706f732c11fd9a695ecec723d84b35927346698e6aa | quote: The core SDK, [found here](https://github.com/bitwarden/sdk-sm/), is written in Rust and provides Rust API, CLI, and Node-API bindings.
  - [1] 2026-11-19: a free 14-day trial exists for the paid Secrets Manager tiers | capture: sha256:0270dea4efa52810f2602e601afe3d57099107a4ae7949772ec3b161e3fe968f | quote: Sign-up for a for a [free 14-day trial of Secrets Manager](https://bitwarden.com/go/start-secrets-enterprise-trial/) today.
- sources:
  - [1] https://bitwarden.com/help/secrets-manager-faqs
  - [2] https://bitwarden.com/help/secrets
  - [3] https://bitwarden.com/help/public-api
  - [4] https://bitwarden.com/help/secrets-manager-plans
  - [5] https://bitwarden.com/products/secrets-manager
  - [6] https://bitwarden.com/help/secrets-manager-cli
  - [7] https://bitwarden.com/help/create-bitwarden-account
  - [8] https://bitwarden.com/go/start-free-plan
  - [9] https://bitwarden.com/help/secrets-manager-quick-start
  - [10] https://bitwarden.com/help/secrets-manager-sdk
