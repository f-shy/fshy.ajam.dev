# Specific

> specific.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/specific/ | JSON https://fshy.ajam.dev/api/v1/entity/specific.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Specific

- `compute/specific` | qualifies-with-caveat | evidence documented | binding request-rate | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:35.125Z (live) | stale on 2026-12-05
- url https://specific.dev/pricing
- free tier: Free with unlimited API requests and users but limited compute per service; $25 of usage credits arrives on the first paid tier, not on Free | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Services egress transfer $0.09 / GB; Postgres egress transfer $0.10 / GB; object storage egress transfer free; no free allowance is stated for services or Postgres | metered: yes | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): 'Limited compute per service' on Free, with no number published [1]
- interface detail: the specific CLI (`specific dev` builds a local environment); deploys also run directly from GitHub; a web dashboard exists at dashboard.specific.dev; documented on https://specific.dev/pricing
- tooling: the specific CLI (command `specific dev`); the page names no SDK or API library
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The free tier has no number at all: 'Limited compute per service' with no figure. That is a discretionary throttle, not a quota, and the record says so rather than inventing a CPU-second count
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free · Unlimited API requests · Unlimited users · Limited compute per service' and 'includes $25 usage credits' on the next tier, quoted
  - [1] 2026-11-04: services egress is $0.09 per GB | capture: sha256:4cdc5bf56f5ad14584dd46be4cbc6129bebe63c4c771a109fc136727b8d1bd5e | quote: | Egress transfer | $0.09 / GB |
  - [1] 2026-11-04: Postgres egress is $0.10 per GB | capture: sha256:4cdc5bf56f5ad14584dd46be4cbc6129bebe63c4c771a109fc136727b8d1bd5e | quote: | Egress transfer | $0.10 / GB |
  - [1] 2026-11-04: object storage egress is free | capture: sha256:4cdc5bf56f5ad14584dd46be4cbc6129bebe63c4c771a109fc136727b8d1bd5e | quote: | Egress transfer | Free |
  - [1] 2026-11-04: the specific CLI exists | capture: sha256:4cdc5bf56f5ad14584dd46be4cbc6129bebe63c4c771a109fc136727b8d1bd5e | quote: Use `specific dev` to build locally with your preferred coding agent and get a full local environment spun up automatically
  - [1] 2026-11-04: the pricing page documents the specific dev command | capture: sha256:5c3552c698411115faa7f6ab47dde236503e5e08e6caa7fb77f8e239b0b91ff8 | quote: Use `specific dev` to build locally with your preferred coding agent and get a full local environment spun up automatically
  - [1] 2026-11-04: the page names the specific dev command and no other client | capture: sha256:5c3552c698411115faa7f6ab47dde236503e5e08e6caa7fb77f8e239b0b91ff8 | quote: Use `specific dev` to build locally with your preferred coding agent and get a full local environment spun up automatically
- sources:
  - [1] https://specific.dev/pricing
