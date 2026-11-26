# Toggled.dev

> toggled.dev | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/toggled/ | JSON https://fshy.ajam.dev/api/v1/entity/toggled.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Toggled.dev

- `dev-services/toggled-dev` | qualifies-with-caveat | evidence documented | binding per-object-cap | category multi-regional hosted feature toggle management | tier FREE
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:44:36.826Z (live) | stale on 2026-12-20
- url https://www.toggled.dev/
- free tier: Endless FREE plan, no credit card required: single project, unlimited clients, up to 10 feature toggles per project, up to 2 environments per project, 2 seats included, data residency, user segmentation, session stickiness, realtime notifications, unlimited MAU, RBAC, embedded analytics, client SDKs, webhooks, admin API, Google and GitHub SSO and 2FA | unit: mixed | metered on: object-count | read on: 2026-11-19 | source: [1] | note: The FREE plan is described as an endless free plan with the complete feature set. The next plan, PRO, is USD 49 a month for 3 projects, 10 seats and unlimited toggles per project. MAUs are unlimited on every plan.
- per-object cap: unverified: no per-toggle value size cap is stated on the pages read
- retention: unverified: no retention period for toggles, audit logs or analytics is stated on the first-party pages read
- egress: not applicable: a flag service with unlimited clients and MAUs and no traffic allowance or byte price published | metered: no | source: [1]
- identity: email | detail: SSO through Google and GitHub is offered on the sign-in page. No card is required for the free plan. No phone number or ID is requested on the form; whether a later step asks for one is unverified: behind a sign-up.
- interface: rest
- limits:
  - per-object-cap (binding): single project and up to 10 feature toggles per project on FREE [1]
  - per-object-cap (binding): up to 2 environments per project and 2 seats included on FREE [1]
  - volume-quota: unlimited clients and unlimited monthly active users on FREE [1]
- limits note: Unlimited clients and MAUs; the binding thresholds are workspace size (one project, 10 toggles, 2 environments, 2 seats). Enforcement behaviour past these limits is not stated on the pricing page: subscribe to PRO to increase service quotas.
- binding note: The single project, 10-toggle and 2-seat ceilings bind first for a growing app; clients and MAUs are unlimited, so user growth does not consume a plan allowance.
- interface detail: A JavaScript client SDK connects to a regional platform URL selected by account region (us-east-1, eu-central-1, ap-south-1) with a client key created in the project; it stores toggles in localStorage, synchronizes in the background at a configurable refresh interval and can bootstrap from local data. The site lists an admin API, generic webhooks and compatibility with other vendors' APIs.
- tooling: The Toggled JavaScript client SDK and regional platform URLs; the site states compatibility with many client SDKs and provides Slack and MS Teams integrations.
- composes with: Serve toggles to a single app from one project across up to two environments, using unlimited clients and MAUs and reading configuration through the regional client API.
- reliability: The plan is described as endless and free with no card; the page says to subscribe to PRO to increase service quotas but does not state what happens past the free ceilings. Data residency is offered through independent regions in North America, Europe and APAC. A system status page, an admin API and helpdesk are listed.
- notes: The Enterprise plan can deploy a dedicated environment in the reader's private AWS account; that is software the reader runs and is the last resort after the hosted FREE plan. No first-party retention period was published, so none is stated. Revisit when the pricing page states over-limit enforcement.
- evidence note: Every value is quoted from first-party pages: the pricing and plan content in the raw homepage fetch, the regional sign-up and sign-in pages, and the client SDK repository. No account was opened and no live toggle read was probed, so the record stays at documented rung. The plan wording was verified in the raw page fetch.
- evidence:
  - [1] 2026-11-19: the FREE plan is endless with the complete feature set and no card | capture: sha256:ff2ea0f7d1fdbe496a485c61d6db6d40d8efe8e39be052de3c981ff885264e3e | quote: We’re offering the endless FREE plan, including the complete set of Toggled.dev features. No credit card required.
  - [1] 2026-11-19: the FREE plan allows a single project | capture: sha256:ff2ea0f7d1fdbe496a485c61d6db6d40d8efe8e39be052de3c981ff885264e3e | quote: Single project
  - [1] 2026-11-19: the FREE plan allows unlimited clients | capture: sha256:ff2ea0f7d1fdbe496a485c61d6db6d40d8efe8e39be052de3c981ff885264e3e | quote: Unlimited Clients
  - [1] 2026-11-19: the FREE plan allows up to 10 feature toggles per project | capture: sha256:ff2ea0f7d1fdbe496a485c61d6db6d40d8efe8e39be052de3c981ff885264e3e | quote: Up to 10 feature toggles per project
  - [1] 2026-11-19: the FREE plan allows up to 2 environments per project | capture: sha256:ff2ea0f7d1fdbe496a485c61d6db6d40d8efe8e39be052de3c981ff885264e3e | quote: Up to 2 environments per project
  - [1] 2026-11-19: the FREE plan includes 2 seats | capture: sha256:ff2ea0f7d1fdbe496a485c61d6db6d40d8efe8e39be052de3c981ff885264e3e | quote: 2 seats included
  - [1] 2026-11-19: the FREE plan allows unlimited monthly active users | capture: sha256:ff2ea0f7d1fdbe496a485c61d6db6d40d8efe8e39be052de3c981ff885264e3e | quote: Unlimited MAU
  - [1] 2026-11-19: the FREE plan includes role-based access control | capture: sha256:ff2ea0f7d1fdbe496a485c61d6db6d40d8efe8e39be052de3c981ff885264e3e | quote: Role Based Access Control
  - [2] 2026-11-19: the sign-up form asks for full name, email address and company | capture: sha256:e67a420c5eaee99cab29a532e4ae3c9afba3912000e21bfb9f790b3b3d937a42 | quote: Full name Email address Company
  - [3] 2026-11-19: the sign-in page offers SSO through Google and GitHub | capture: sha256:b656c87b84dfafe39e12b85fcf0e2adb646e4c4940023e06da02068cdbb30b87 | quote: Google
  - [4] 2026-11-19: the client SDK initializes with a regional platform URL and a client key | capture: sha256:8dd89023190f4040a0196d10cdb8d174b7ada396ac963e9930029d6419acea37 | quote: url: TOGGLED_PLATFORM_URLS.EUC1,
  - [4] 2026-11-19: the SDK stores toggles in localStorage and synchronizes in the background | capture: sha256:8dd89023190f4040a0196d10cdb8d174b7ada396ac963e9930029d6419acea37 | quote: stores toggles relevant for the current user in `localStorage` and synchronizes with Toggled
- sources:
  - [1] https://www.toggled.dev/
  - [2] https://use1.saas.toggled.dev/sign-up
  - [3] https://use1.saas.toggled.dev/
  - [4] https://github.com/toggled-dev/toggled-client-js
