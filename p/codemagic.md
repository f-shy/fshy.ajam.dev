# Codemagic artifacts

> codemagic.io | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codemagic/ | JSON https://fshy.ajam.dev/api/v1/entity/codemagic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Codemagic (mobile CI)

- `compute/codemagic` | qualifies-with-caveat | evidence documented | binding request-rate | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:41.665Z (live) | stale on 2026-12-05
- url https://codemagic.io/pricing/
- free tier: the managed hosted Patch service is free below 100,000 monthly active users; egress and storage are included | unit: users | metered on: identity-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Egress traffic and data storage are included in Codemagic Patch pricing, with no bandwidth fees | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): free below 100,000 monthly active users of the user's own app. [1]
  - write-gated: the trial and custom plans are arranged through sales, not self-serve [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The free tier is metered on monthly active users rather than machine execution time.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the free tier is bounded by a user's own MAU, not by a build or session clock
  - free_tier_kind: allowance
  - granularity.min_billed_s: 60
  - burst_x: 1.0
  - net.out: yes
  - net.in: yes
  - net.allowance: egress included
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Is a free tier available? Yes. If you have under 100K monthly active users you can use our managed hosted Patch service for free.' and 'Egress traffic and data storage are included in Codemagic Patch pricing'…
  - [1] 2026-11-03: egress traffic is included in Patch pricing | capture: sha256:9c3c529a8ee7d60d10b6278f19fb167117d2c3756084a0b6c7e8222a5f7781f8 | quote: No. Egress traffic and data storage are included in Codemagic Patch pricing.
  - [1] 2026-11-03: no bandwidth fees | capture: sha256:9c3c529a8ee7d60d10b6278f19fb167117d2c3756084a0b6c7e8222a5f7781f8 | quote: There are no hidden infrastructure or bandwidth fees.
- sources:
  - [1] https://codemagic.io/pricing/

## Codemagic artifacts

- `storage/codemagic-artifacts` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://codemagic.io
- free tier: 500 free build minutes/month on macOS M2 (individuals). No free storage allowance advertised. Artifact retention is per-team policy; Enterprise default is 1 year. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free via api.codemagic.io artifact URLs; 'No expiration' download links are a documented option. | metered: no
- identity: email
- interface: rest
- limits note: 500 min/month free. 'No expiration' applies to the LINK, not the artifact. Retention policy still deletes the file (explicit in their KB). Build dashboards give only 24-hour artifact links.
- interface detail: rest
- tooling: POST /artifacts/:secureFilename/public-url with expiresAt, returning a public URL; GET /artifacts/:secureFilename. API token required (`x-auth-token`).
- composes with: Unlimited accounts x 500 free minutes; artifact volume is bounded by what you can build in 500 min/month. 'No expiration' links mean the URL outlives nothing. The artifact is still deleted by team retention policy.
- reliability: 'No expiration' is a misleading label: the link persists but the artifact is removed by retention policy, so links rot. 500 min/month is a hard build ceiling.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: 500 free build minutes/month on macOS M2 (individuals). No free storage allowance advertised. Artifact retention is per-team policy; Enterprise default is 1 year.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'the artifact itself is still subject to your team's artifact retention policy ... Enterprise plan users have a default artifact retention period of 1 year'
  - [3] 2026-10-21: public-url creation API
  - [1] 2026-10-21: '500 free minutes per month on macOS M2'
  - [4] 2026-10-21: probe: curl -> 404; random artifact path -> 401 (no anonymous enumeration)
- sources:
  - [1] https://docs.codemagic.io/billing/pricing/
  - [2] https://help.codemagic.io/articles/1948706793-how-does-the-no-expiration-artifact-download-link-option-work
  - [3] https://docs.codemagic.io/rest-api/artifacts/
  - [4] https://api.codemagic.io/artifacts/
