# Zylora open

> zylora.dev | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zylora/ | JSON https://fshy.ajam.dev/api/v1/entity/zylora.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zylora open source

- `compute/zylora-open-source` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://zylora.dev/free-gpu-credits/
- free tier: USD 500 of GPU credits for startups pre-Series A, academic research, or open source projects. Open source qualification is a public ML library, model or tool with a meaningful GitHub presence of 200 or more stars. The page prices what the award buys: H100 SXM 4.6h at USD 3.49/hr, A100 80GB 6.9h at USD 2.49/hr, L40S 13.9h at USD 1.49/hr, RTX 4090 and A10G listed as unlimited. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-shot-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: An open source maintainer path needs no company and no academic email; the academic path does require an academic email, which is stated as an exception-free rule. The open source path needs a public repository with 200 or more stars.
- interface: unknown
- limits:
  - write-gated (binding): The 200-star repository fails first for a new maintainer, and the amount, under 5 hours of an H100, is too small to be capacity even when granted. [1]
- limits note: The 200-star repository fails first for a new maintainer, and the amount, under 5 hours of an H100, is too small to be capacity even when granted.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The vendor's own arithmetic is the finding: USD 500 is under five hours of one H100, so the award demonstrates an hour-rate rather than funding a run. It composes with the CloudRift grant only as two small separate awards to different accounts.
- reliability: no reliability event recorded
- notes: Zylora provides cloud compute sponsorships for open-source projects, offering discounted or credited instance allocations for public repositories.
- extras:
  - facets.class: open-source-sponsorship
  - facets.free_tier_kind: one-shot-credit
  - facets.shape.gpu_class: H100 SXM / A100 80GB / L40S / RTX 4090 / A10G
- evidence:
  - [1] 2026-10-22: 'USD 500 free GPU credits' with qualification by open source projects having 'a meaningful GitHub presence (200+ stars)', quoted
  - [1] 2026-10-22: the page's own price table converts USD 500 into 4.6h of H100 SXM, 6.9h of A100 80GB and 13.9h of L40S, quoted
- sources:
  - [1] https://zylora.dev/free-gpu-credits/

## Zylora startup GPU

- `compute/zylora-startup-gpu` | trial-only | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:24:50.431Z (live) | stale on 2026-12-05
- url https://zylora.dev/startups/
- free tier: Explorer: 'USD 25 one-time credits', instant, 'Card on file required.' Builder: 'USD 100 one-time credits', after a 'Quick 5-min review'. 'Credits expire 6 months after grant.' | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: egress is billed at normal rates, not covered by credits; no allowance and no per-GB price published on the startups, home or pricing pages | metered: no | source: [1]
- identity: card | detail: Explorer requires a card on file; Builder requires a live website or public GitHub repo plus a form asking for company, website, GitHub and funding stage
- interface: unknown
- limits:
  - volume-quota (binding): USD 25 instantly with a card, USD 100 after review, both one time [1]
  - retention-clamped: credits expire 6 months after grant [1]
- limits note: one grant per person and per company
- binding note: USD 25 is the amount an individual can claim without a review, and GPU rates on the same site are unpublished
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 100 of GPU time at consumer prices is a few hours of a single card, so it composes as a way to test whether a workload runs at all, not as capacity. The card requirement makes it a payment relationship for a trivial amount.
- reliability: no reliability event recorded
- notes: Two further tiers exist at $500 and $2,500 for funded or open-source projects. No per-GPU rate is published on the page read, so the credit cannot be sized in hours.
- evidence note: the startups page was read on 2026-10-23 and states both amounts, the gate for each and the six-month expiry
- extras:
  - facets.class: startup-credit
  - facets.free_tier_kind: one-shot-credit
- evidence:
  - [1] 2026-10-23: quoted: 'Explorer ... $25 one-time credits ... Card on file required', 'Builder ... $100 one-time credits', 'Credits expire 6 months after grant'
  - [1] 2026-11-03: egress is billed but no allowance or price appears on the page | capture: sha256:09d633d25f241ac7ff763e54823dbff4f6531760cbd79b68b28e7567941ce3f0 | quote: Credits apply to compute usage only. Seat fees, storage, and egress are billed normally.
- sources:
  - [1] https://zylora.dev/startups/
