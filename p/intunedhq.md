# Intuned

> intunedhq.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/intunedhq/ | JSON https://fshy.ajam.dev/api/v1/entity/intunedhq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Intuned

- `compute/intuned` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone unknown, ID no, institution no | verified 2026-11-06T17:42:10.983Z (live) | stale on 2026-12-07
- url https://intunedhq.com/pricing
- free tier: the $0 plan includes 3 compute hours, a $5 AI trial credit, unlimited standalone runs and 7 days of data retention | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the page read states no egress allowance and no overage price per TB | metered: no | source: [1]
- identity: email | detail: The phone requirement is not published on https://intunedhq.com/docs/main/00-getting-started/quickstarts/scraper. Country: not published on https://intunedhq.com/docs/main/00-getting-started/quickstarts/scraper.
- interface: rest, cli
- limits:
  - request-rate (binding): 3 compute hours on the free plan, 100 on the $25 plan [1]
  - retention-clamped: run data is kept 7 days on free, 30 days on the $25 plan [1]
  - per-object-cap: the $5 AI credit is a trial balance, not a monthly allowance [1]
- interface detail: HTTP API for Web Tasks; Projects use the Intuned CLI and IDE
- tooling: API for Web Tasks; CLI and IDE for Projects
- composes with: not established
- reliability: no reliability event recorded
- evidence note: Retention is limited to 7 days.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 3 compute hours in total on free; the page states no per-run cap
  - free_tier_kind: allowance
  - burst_x: 1.0
  - ps.price: data retention only, 7 days on free
  - ps.durability: run data, discarded after the retention window
  - ps.on_stop: no
  - ps.on_destroy: no
  - ps.retention: 7 days
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '3 compute hours included' and '$5 trial AI credit' with '7-day data retention' on the $0 plan, against '100 compute hours included' and '30-day data retention' at $25, quoted
  - [1] 2026-11-03: overage is priced per compute hour and per run; no egress allowance or overage price per TB is stated | capture: sha256:6dff64cdc01d7f147d919caca29b7dbbefe3c88112cd862aad8f8af6381b1bee | quote: | Compute overage rate | -- | $0.12 / hour | $0.10 / hour | Volume pricing |
  - [2] 2026-11-03: Web Tasks are called over an API | capture: sha256:522fde4d76c4eb58c2a7bb242d51ea502ff63000fbee25082a6c7c38bfaf29e0 | quote: Describe a web task in plain English and call an API.
  - [3] 2026-11-04: an Intuned account is required and its free plan needs no credit card | capture: sha256:95c8d4805e063fe75ea7ae5e267b509bf35118d3021387d3222192a0575510d5 | quote: An active Intuned account (sign up here). No credit card required—Intuned has a free plan
  - [3] 2026-11-06: an Intuned account is required and its free plan needs no credit card | capture: sha256:95c8d4805e063fe75ea7ae5e267b509bf35118d3021387d3222192a0575510d5 | quote: An active Intuned account (sign up here). No credit card required—Intuned has a free plan
  - [4] 2026-11-06: an email address is the personal data collected for an account | capture: sha256:8254e4b9591eb8509c09f8395300970ce09d56da9c534e50a0eab99d59f5c2a8 | quote: Personally identifiable information may include, but is not limited to: (a) Email address
- sources:
  - [1] https://intunedhq.com/pricing
  - [2] https://docs.intunedhq.com/
  - [3] https://intunedhq.com/docs/main/00-getting-started/quickstarts/scraper
  - [4] https://intunedhq.com/docs/main/06-resources/privacy-policy
