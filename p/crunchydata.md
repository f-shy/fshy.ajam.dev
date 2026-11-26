# CrunchyData

> crunchydata.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crunchydata/ | JSON https://fshy.ajam.dev/api/v1/entity/crunchydata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CrunchyData

- `databases-kv/crunchydata` | paid-only | evidence documented | binding none | category hosted managed Postgres (Crunchy Bridge) on AWS, Azure and GCP
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:19:24.768Z (live) | stale on 2026-12-20
- url https://www.crunchydata.com/pricing
- free tier: No free tier. The hosted Postgres offer starts at USD 10 per month; the smallest published instance, Hobby-0, is 2 cores and 0.5 GB memory at USD 9 per month, with storage at USD 0.10 per GB. The pricing calculator says a user can try Bridge free by keeping spend below a USD 5 minimum charge. | unit: none | metered on: none | read on: 2026-11-19 | source: [1] | note: There is no standing free allowance. USD 5 is a minimum charge, not a recurring free quota; keeping spend below it only avoids a bill.
- per-object cap: No per-object cap is published on the pricing, calculator or product pages read. Storage is billed at USD 0.10 per GB with no stated single-object ceiling. | source: [1]
- retention: Daily and WAL backups are included with point-in-time recovery at no cost. No retention period in days is published on the pages read. | source: [1]
- egress: Networking and data transfer are included in the base price with no separate per-GB charge. The product page states no additional costs for networking or ingress or egress. | metered: no | source: [2]
- identity: email | detail: the registration page asks for Full name, Email address and Password; no card is requested on that page. Sign Up with Google, Microsoft or OpenID Connect is also offered. No phone number or identity document is shown.
- interface: rest, cli
- limits:
  - volume-quota: storage billed at USD 0.10 per GB; smallest instance Hobby-0, 2 cores and 0.5 GB memory, from USD 9 per month [1]
- binding note: No free allowance exists, so no usage quota binds; the constraint is a paid floor (a monthly charge), which has no term in the binding vocabulary.
- interface detail: a web dashboard, an API to automate deployment and management, and the cb command line client
- tooling: psql and any Postgres client; the cb CLI; the Crunchy Bridge API
- composes with: an isolated single-tenant Postgres instance reachable by connection string over private networking, with VPC peering and Tailscale support
- reliability: billing is per minute and invoiced monthly; backups and point-in-time recovery are included in the base price, and networking and ingress and egress carry no separate charge
- notes: Crunchy Bridge is a hosted managed Postgres service with no free tier. Crunchy Data also sells Postgres software the reader can install, but that offer is not what this record prices. The only no-cost path published is keeping a Hobby-0 instance under a USD 5 minimum charge, which is not a recurring free allowance.
- evidence note: five first-party pages were captured and quoted on 2026-11-19: the pricing page, the pricing calculator, the product page and the registration page. The price figures and the signup fields come from those pages. No probe was run, so the rung stays documented.
- self hosted: no
- evidence:
  - [1] 2026-11-19: the hosted Postgres offer starts at USD 10 per month | capture: sha256:65d425a2992bd0c08e352b552929d8c2d598328d0f31f72a510d0ed75a0e47d7 | quote: Ready to launch on the provider of your choice (AWS, Azure, GCP) with plans starting at $10/mo.
  - [1] 2026-11-19: storage is billed at USD 0.10 per GB | capture: sha256:65d425a2992bd0c08e352b552929d8c2d598328d0f31f72a510d0ed75a0e47d7 | quote: Storage costs are $0.10 per GB. For example, 100 GB would be $10 per month.
  - [1] 2026-11-19: the smallest published instance is Hobby-0, 2 cores and 0.5 GB memory, at USD 9 per month | capture: sha256:65d425a2992bd0c08e352b552929d8c2d598328d0f31f72a510d0ed75a0e47d7 | quote: | Hobby-0 | 2 | .5GB | $9 |
  - [3] 2026-11-19: there is no free plan; the only free path is staying under a USD 5 minimum charge | capture: sha256:1997d5a0835ee4a59102185aae37890adcff8d4b9bba02eb80353b69949166aa | quote: Want to try out bridge for free? Use the hobby-0 instance and keep your spend below the $5 minimum charge.
  - [4] 2026-11-19: signup asks for a full name, an email address and a password; no card is shown | capture: sha256:f75c59bbfe9bd88b03b5b52d75874441a8e10d582f99a1bb90dee536335a062c | quote: Full name Email address Password
  - [2] 2026-11-19: networking and data transfer carry no separate per-GB charge | capture: sha256:9a593a06e2d23f6355b975dcdf1897efdf9763b17830f4b33dd118c253437d50 | quote: Billing by the minute for compute and storage, invoiced monthly, with no additional costs for networking or ingress/egress.
- sources:
  - [1] https://www.crunchydata.com/pricing
  - [2] https://www.crunchydata.com/products/crunchy-bridge
  - [3] https://www.crunchydata.com/pricing/calculator
  - [4] https://crunchybridge.com/register
