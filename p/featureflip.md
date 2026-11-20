# Featureflip

> featureflip.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/featureflip/ | JSON https://fshy.ajam.dev/api/v1/entity/featureflip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Featureflip

- `dev-services/featureflip` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted feature flags with flat per-plan pricing | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:44:36.826Z (live) | stale on 2026-12-20
- url https://featureflip.io/pricing
- free tier: Free plan, USD 0 a month, free forever, no credit card: 10 flags per project, 2 environments per project, 1 project, up to 3 team members, 7-day audit logs, 1 webhook endpoint, Management API access, community support; unlimited flag evaluations | unit: objects | metered on: object-count | read on: 2026-11-19 | source: [1] | note: The plan is a flat monthly price with none of seats, monthly active users or evaluations metered. Flags per project is the count of active flags; archiving a flag frees its place. The next plan, Team, is USD 49 a month (USD 39 annual) for 5 members, 3 projects and unlimited flags.
- per-object cap: unverified: no per-flag value size cap is stated on the pricing or plans-and-limits pages read
- retention: 7-day audit log retention on Free; 30 days on Team and Pro; 90 days on Business; 365 days on Enterprise | days: 7 | source: [2] | note: Audit entries older than 7 days are removed in the next daily cleanup on Free. No retention period for flag values is stated on the pages read.
- egress: not applicable: a flag service with flat pricing and no metered evaluations or traffic allowance published | metered: no | source: [1]
- identity: email | detail: The sign-up form asks for Name, Email, Password, Organization Name and URL Slug, then a plan choice; the pricing page states the Free plan needs no credit card. Sign-in with Google or GitHub is available on every plan. No phone number or ID is requested on the form; whether a later step asks for one is unverified: behind a sign-up.
- interface: rest
- limits:
  - per-object-cap (binding): 10 active flags per project on Free [2]
  - per-object-cap (binding): 1 project, 2 environments per project and up to 3 team members on Free [1]
  - retention-clamped: 7-day audit log retention on Free [2]
  - volume-quota: 1 webhook endpoint on Free [2]
- limits note: Everything else is on Free, including targeting rules, segments, percentage rollouts, all 14 SDKs, the Management API and the audit log. Over a plan ceiling, creating a new flag or project is blocked while existing flag evaluation continues. Team members include pending invitations.
- binding note: The 10 active flags per single project bind first for a growing app; evaluations are unlimited, so traffic does not consume a plan allowance.
- interface detail: A Management API for flag and project operations, with an MCP server and a Terraform provider; client SDKs stream flag configuration to the application and evaluate flags locally with percentage rollouts, targeting rules and kill switches. Sign-in with Google or GitHub is available on every plan.
- tooling: 14 official SDKs, the Management API, the MCP server and the Terraform provider
- composes with: Run flags for a small staging and production setup in one project, using local SDK evaluation with no per-evaluation charge and no traffic meter.
- reliability: Over a plan ceiling, the creation of new flags or projects is blocked while existing flag evaluation continues without interruption. Scheduled changes and required two-factor authentication begin on the Team plan. The Enterprise plan is arranged with the team and adds on-premise deployment, which is software the reader runs and is the last resort.
- notes: Revisit when the pricing page changes the free flag, project or seat caps or the audit-log window.
- evidence note: Every value is quoted from the first-party pricing page, plans-and-limits documentation and sign-up page. No account was opened and no live flag evaluation was probed, so the record stays at documented rung.
- evidence:
  - [1] 2026-11-19: the Free plan is USD 0 a month, free forever, built for production | capture: sha256:a881bf045b6b17a80ee9eeee43ea115ad099f2e7b02ed86d5533de0c98e0b135 | quote: Free forever, and built to run in production
  - [1] 2026-11-19: Free includes 10 flags, 2 environments, 1 project and up to 3 team members | capture: sha256:a881bf045b6b17a80ee9eeee43ea115ad099f2e7b02ed86d5533de0c98e0b135 | quote: - 10 flags per project - 2 environments per project - 1 project - Up to 3 team members
  - [1] 2026-11-19: Free includes a 7-day audit log and 1 webhook endpoint | capture: sha256:a881bf045b6b17a80ee9eeee43ea115ad099f2e7b02ed86d5533de0c98e0b135 | quote: - 7-day audit logs - 1 webhook endpoint
  - [1] 2026-11-19: the Free plan needs no credit card | capture: sha256:a881bf045b6b17a80ee9eeee43ea115ad099f2e7b02ed86d5533de0c98e0b135 | quote: Free never expires, needs no credit card and is meant for production
  - [1] 2026-11-19: there are no per-seat or per-evaluation fees | capture: sha256:a881bf045b6b17a80ee9eeee43ea115ad099f2e7b02ed86d5533de0c98e0b135 | quote: Start free, scale as you grow. No per-seat fees, no hidden costs.
  - [1] 2026-11-19: past the Free 10-flag limit an eleventh flag is refused while existing evaluation keeps working | capture: sha256:a881bf045b6b17a80ee9eeee43ea115ad099f2e7b02ed86d5533de0c98e0b135 | quote: Existing flag evaluation keeps working without interruption, and your users see no difference. The limit only applies to creating more: on the Free plan, with its 10-flag limit, an eleventh flag is refused until you upgrade or delete one.
  - [2] 2026-11-19: the limits table lists 3 members, 10 flags, 1 webhook and 7-day audit retention on Free | capture: sha256:d15de5cd37d06e2cac075eb2066f7c18348c6f28511d5dabdc8e561deb2b3647 | quote: | Team members | 3 | 5 | 10 | 25 | Unlimited |
  - [2] 2026-11-19: Free includes 10 flags per project and 7-day audit retention | capture: sha256:d15de5cd37d06e2cac075eb2066f7c18348c6f28511d5dabdc8e561deb2b3647 | quote: | Audit log retention | 7 days | 30 days | 30 days | 90 days | 365 days |
  - [2] 2026-11-19: all 14 SDKs, the Management API, MCP server and Terraform provider are on Free | capture: sha256:d15de5cd37d06e2cac075eb2066f7c18348c6f28511d5dabdc8e561deb2b3647 | quote: Everything else is on every plan, Free included: targeting rules, segments, percentage rollouts, prerequisites, all 14 SDKs, the Management API
  - [3] 2026-11-19: the sign-up form asks for name, email, password and organization details | capture: sha256:ec76ba595a3ecc9c261877d3f24b518238572550375398b3b6eb3550e8a7662d | quote: ### Your Information Name Email Password ### Organization Details Organization Name URL Slug
- sources:
  - [1] https://featureflip.io/pricing
  - [2] https://featureflip.io/docs/concepts/plans-and-limits/
  - [3] https://app.featureflip.io/signup
