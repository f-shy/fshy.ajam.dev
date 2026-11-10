# Zencastr

> zencastr.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zencastr/ | JSON https://fshy.ajam.dev/api/v1/entity/zencastr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zencastr — free hosting

- `storage/zencastr-free-hosting` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://zencastr.com
- free tier: Advertised as no cap: 'No episode caps, no storage limits, no upcharging as your show grows. Unlimited hosting, included in every plan', plus 'Up to 5 shows for free'. No numeric storage or per-file figure is published anywhere in their docs. The pricing comparison table exposes rows only as 'Unlimited' with no labels in the extracted DOM. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered in any published doc; hosting and publishing show 'Unlimited' in the plan comparison. | metered: yes
- identity: anonymous
- interface: unknown
- limits note: Per-episode file size is NOT published. This is the risk. Zencastr also sells a recording product whose free tier is separately capped at '2 hours of audio and video recording per month' with 'Recording masters storage of up to 31 days' (2023 change), which is easy to confuse with hosting; hosting is the uncapped part, recording masters are not.
- interface detail: wrapper-only
- tooling: No public upload API found; dashboard upload only. RSS out is standard.
- composes with: 5 shows per free account x unlimited episodes x unpublished per-file cap. Multiple accounts = 5 shows each.
- reliability: No independent confirmation of transcode behaviour and no live enclosure probe possible without an account. Their 2023 free-plan reduction shows the free tier is a moving target.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Podcast hosting with no limits. No episode caps, no storage limits, no upcharging as your show grows. Unlimited hosting, included in every plan'; 'Up to 5 shows for free'
  - [2] 2026-10-21: Hosting & Publishing rows show 'Unlimited'
  - [3] 2026-10-21: precedent that the free tier can be cut: 2023 reduced recording to '2 hours ... per month' with masters kept '31 days'
- sources:
  - [1] https://zencastr.com/feature/hosting
  - [2] https://zencastr.com/pricing
  - [3] https://zencastr.ghost.io/announcing-changes-to-the-free-plan/
