# Akeyless

> akeyless.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/akeyless/ | JSON https://fshy.ajam.dev/api/v1/entity/akeyless.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Akeyless

- `dev-services/akeyless` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted secrets management, encryption keys and certificates (SaaS or hybrid SaaS with a customer-side gateway) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:33:38.483Z (live) | stale on 2026-12-20
- url https://www.akeyless.io/pricing
- free tier: Free plan at USD 0: 5 Clients, 500 Static Secrets, 5 Dynamic Secrets, 5 Rotated Secrets, 3 Targets, 1 OIDC App, 1 SSH Cert Issuer, 1 PKI Cert Issuer, 1 Encryption Key (DFC/Classic), 1 Gateway Cluster, 3 days of Audit Logs Retention; enterprise features such as Zero Knowledge Mode, HSM Integration and SAML/OIDC/LDAP authentication are marked X | unit: objects | metered on: object-count | read on: 2026-11-19 | source: [1] | note: The headline unit is the Client: a human user, application or server that starts a remote session; multiple instances of one application and multiple authentication methods for one user count once. Static Secrets are counted separately from Clients. The paid tier is Enterprise with a custom quote.
- per-object cap: unverified: the Secrets Management plan table states counts of secrets, not a size limit per secret | source: [1]
- retention: Audit Logs Retention is 3 days on the Free plan; no expiry for stored secrets is stated on the pages read | days: 3 | source: [1] | note: The 3-day value applies to audit logs, not to secret values. No automatic expiry of stored secrets is stated on the pages read.
- egress: not applicable: a secrets management API; the pricing page names no traffic allowance or per-GB charge, and the API is reached over HTTPS at api.akeyless.io | metered: no | source: [1]
- identity: email | detail: The sign-up page offers Google, Github or Email and an Email field, with acceptance of the End User License Agreement and a reCAPTCHA; the first-party quickstart lists an email address you can access as the prerequisite and describes email verification before the account is active. No card, phone number or ID document is asked for on the sign-up page. Fields shown only after account creation are unverified: behind a sign-up.
- interface: rest, cli
- limits:
  - volume-quota (binding): 5 Clients on the Free plan [1]
  - volume-quota (binding): 500 Static Secrets on the Free plan [1]
  - volume-quota (binding): 5 Dynamic Secrets and 5 Rotated Secrets on the Free plan [1]
  - request-rate: 1K transactions per day on the Free plan [1]
  - retention-clamped: 3 days of Audit Logs Retention on the Free plan [1]
  - write-gated: Zero Knowledge Mode, HSM Integration, Log/Event Forwarding and SAML/OIDC/LDAP, Universal Identity and certificate-based authentication are marked X on the Free plan [1]
- binding note: The 5-Client count fills first at a small team scale, since one Client is a distinct human user, application or server; the 1K daily transaction cap then bounds API-driven workloads.
- interface detail: An OpenAPI 3.0 REST API at api.akeyless.io with operations such as get-secret-value and get-dynamic-secret-value. The Akeyless CLI retrieves a secret with akeyless get-secret-value --name <secret name>; SDKs, Kubernetes, Jenkins and Azure integrations are also documented.
- endpoint: https://api.akeyless.io
- tooling: the Akeyless CLI, the REST API at api.akeyless.io, Akeyless SDKs, and the web console
- composes with: Secrets are served to applications, Kubernetes and CI through the CLI, REST API or SDKs; the Free plan includes 1 Gateway Cluster for hybrid connections to private infrastructure.
- reliability: The Free plan keeps audit logs for 3 days and states no automatic expiry of stored secrets on the pages read; no throttle or data-loss event is stated there.
- evidence note: All plan limits, the vendor's Client definition, the API and the sign-up fields are quoted from first-party Akeyless pricing, documentation and registration pages. No account was opened; any value visible only after registration is unverified.
- evidence:
  - [1] 2026-11-19: the Free plan allows 5 Clients | capture: sha256:b3bb8aa9fe3e6ea6d2b0b7629d789aa040a679fbf108c7818f97c1f9ec21a92a | quote: | Clients | 5 | V |
  - [1] 2026-11-19: the Free plan allows 500 Static Secrets | capture: sha256:b3bb8aa9fe3e6ea6d2b0b7629d789aa040a679fbf108c7818f97c1f9ec21a92a | quote: | Static Secret | 500 | V |
  - [1] 2026-11-19: the Free plan allows 5 Dynamic Secrets | capture: sha256:b3bb8aa9fe3e6ea6d2b0b7629d789aa040a679fbf108c7818f97c1f9ec21a92a | quote: | Dynamic Secret | 5 | V |
  - [1] 2026-11-19: the Free plan allows 1K transactions per day | capture: sha256:b3bb8aa9fe3e6ea6d2b0b7629d789aa040a679fbf108c7818f97c1f9ec21a92a | quote: | Transaction | 1K per day | V |
  - [1] 2026-11-19: the Free plan keeps audit logs for 3 days and includes 1 Gateway Cluster | capture: sha256:b3bb8aa9fe3e6ea6d2b0b7629d789aa040a679fbf108c7818f97c1f9ec21a92a | quote: | Audit Logs Retention | 3 days | V |
  - [1] 2026-11-19: the Free plan includes 1 Gateway Cluster | capture: sha256:b3bb8aa9fe3e6ea6d2b0b7629d789aa040a679fbf108c7818f97c1f9ec21a92a | quote: | Gateway Clusters | 1 Cluster | V |
  - [1] 2026-11-19: a Client is a human user, application or server that starts a remote session, counted once across instances and authentication methods | capture: sha256:b3bb8aa9fe3e6ea6d2b0b7629d789aa040a679fbf108c7818f97c1f9ec21a92a | quote: Clients are human users, applications, or servers that initiate a remote session with Akeyless services.
  - [1] 2026-11-19: email access is available on the Free plan | capture: sha256:b3bb8aa9fe3e6ea6d2b0b7629d789aa040a679fbf108c7818f97c1f9ec21a92a | quote: | Email Access | V | V |
  - [2] 2026-11-19: the sign-up page offers Google, Github or Email and asks for an email address with terms acceptance and reCAPTCHA, with no card or phone field | capture: sha256:16d4d30f98806195b7d524d6137eaa7636917f9aa7d117f839aae9e716abeb33 | quote: Sign up using Google Github
  - [3] 2026-11-19: an email address is a prerequisite and the account activates after email verification | capture: sha256:64c3894f2b24274e08a2b5d13c9897d1a957cc464a114743e8b2da6547261ce9 | quote: An email address you can access
  - [4] 2026-11-19: a secret value is retrieved through the Akeyless CLI | capture: sha256:7755e88d393b6855aa6ef057a10b5228834ef10e72b6ec9cd1bc52df6f06bb01 | quote: akeyless get-secret-value --name <secret name> --version <version number>
  - [4] 2026-11-19: SDKs and integrations such as Kubernetes, Jenkins and Azure can retrieve secrets | capture: sha256:7755e88d393b6855aa6ef057a10b5228834ef10e72b6ec9cd1bc52df6f06bb01 | quote: with the help of any of our SDKs
  - [5] 2026-11-19: a REST API is published at api.akeyless.io | capture: sha256:6c2b617da0ef9d080acbc1c87acd92d2f97ecac4dd4f1086123d2db16781c88f | quote: "url": "https://api.akeyless.io"
- sources:
  - [1] https://www.akeyless.io/pricing
  - [2] https://console.akeyless.io/registration
  - [3] https://docs.akeyless.io/docs/account-quickstart
  - [4] https://docs.akeyless.io/docs/retrievestatic
  - [5] https://docs.akeyless.io/reference/getdynamicsecretvalue
