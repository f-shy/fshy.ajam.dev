# CloudAxis

> cloudaxis.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudaxis/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudaxis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudAxis

- `compute/cloudaxis` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:20.761Z (live) | stale on 2026-12-05
- url https://cloudaxis.ai/pricing/
- free tier: Free at $0 with 50 AI credits, 10 cloud browser minutes and 10 web searches a month, no card and no API keys; a hard cap with no overage | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://cloudaxis.ai/pricing/ states no data-transfer allowance or overage price; plans have hard monthly caps with no overages | metered: no | source: [1]
- identity: email | detail: 'No credit card. No API keys.' quoted from cloudaxis.ai/pricing read 2026-10-22
- interface: unknown
- limits:
  - request-rate (binding): 50 AI credits, 10 cloud browser minutes and 10 web searches a month on Free [1]
  - per-object-cap: hard caps with no overage: the page says so as the reason a monitoring agent can run 24/7 [1]
- interface detail: a web desktop app reached after email sign-up; no REST API, CLI or SSH is documented on the pages read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the Free tier's three monthly caps and the paid ladder as of 2026-09-01. Ten browser minutes a month is the number that decides it, and it was not in the record
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 10 browser minutes a month on Free; 500 on the $29 tier
  - free_tier_kind: allowance
  - net.out: yes
  - net.in: no
  - net.static_ip: no
  - net.allowance: 10 web searches a month on Free
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'List prices are live as of 1 September 2026. Growth $29, Pro $59, Max $199. Free stays $0.' with the Free tier's '50 AI credits / month', '10 cloud browser minutes / month', '10 web searches / month', and 'No credit card. No API keys. Hosted frontier models included.', quoted
  - [1] 2026-11-03: no overage price exists; the page publishes no transfer allowance | capture: sha256:2613317a87f6961237ebc53552858ede1ebb2b464d943568b9643ce938ee5dc7 | quote: Hard caps stay — no overages.
  - [2] 2026-11-03: access is a web desktop after email sign-up | capture: sha256:d7d5a8063d92dab71e17b09feb2cdc4cb8b75e3c83cac65218f79fda3aa8d148 | quote: Sign up with email. No card. No API keys. You’re in the desktop in seconds.
- sources:
  - [1] https://cloudaxis.ai/pricing/
  - [2] https://cloudaxis.ai/
