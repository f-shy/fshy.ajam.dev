# Zencastr

> zencastr.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zencastr/ | JSON https://fshy.ajam.dev/api/v1/entity/zencastr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zencastr — free hosting

- `storage/zencastr-free-hosting` | qualifies-with-caveat | evidence documented | binding none | category media
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:36.119Z (live) | stale on 2026-12-11
- url https://zencastr.com
- free tier: No episode caps, no storage limits, no upcharging as your show grows. Unlimited hosting, included in every plan. | unit: unlimited | metered on: stored-bytes | read on: 2026-11-10 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered in any published doc; hosting and publishing show 'Unlimited' in the plan comparison. | metered: no
- identity: email | detail: sign-up is a Create Account form with first name, last name, username, email and password; no card or phone field is shown.
- interface: unknown
- limits note: Per-episode file size is NOT published. This is the risk. Zencastr also sells a recording product whose free tier is separately capped at '2 hours of audio and video recording per month' with 'Recording masters storage of up to 31 days' (2023 change), which is easy to confuse with hosting; hosting is the uncapped part, recording masters are not.
- interface detail: wrapper-only
- tooling: No public upload API found; dashboard upload only. RSS out is standard.
- composes with: 5 shows per free account x unlimited episodes x unpublished per-file cap. Multiple accounts = 5 shows each.
- reliability: No independent confirmation of transcode behaviour and no live enclosure probe possible without an account. Their 2023 free-plan reduction shows the free tier is a moving target.
- notes: Up to 5 shows are included on the free plan.
- evidence note: the hosting page states no episode caps and no storage limits, and that unlimited hosting is included in every plan.
- evidence:
  - [1] 2026-10-21: 'Podcast hosting with no limits. No episode caps, no storage limits, no upcharging as your show grows. Unlimited hosting, included in every plan'; 'Up to 5 shows for free'
  - [2] 2026-10-21: Hosting & Publishing rows show 'Unlimited'
  - [3] 2026-10-21: precedent that the free tier can be cut: 2023 reduced recording to '2 hours ... per month' with masters kept '31 days'
  - [1] 2026-11-10: the hosting page states no episode caps, no storage limits and unlimited hosting on every plan | capture: sha256:d0d7884f9939e73eef94dd6da1a5ce8e06435ef2f67704514d2acb2b1effd75a | quote: No episode caps, no storage limits, no upcharging as your show grows. Unlimited hosting, included in every plan.
  - [1] 2026-11-10: downloads have no monthly limit, so the offer is not metered on egress | capture: sha256:d0d7884f9939e73eef94dd6da1a5ce8e06435ef2f67704514d2acb2b1effd75a | quote: With Zencastr, you can enjoy unlimited audio hosting with no monthly limits on episode uploads, downloads, or storage.
  - [4] 2026-11-10: the create-account form asks for an email address and a password, and shows no card or phone field | capture: sha256:0af0c0aa70d9e9e8d249b44fb4322ccc4149c6d2bf346c1f94a5b46091bf231b | quote: First Name Last Name Username Email Password Confirm Password
  - [1] 2026-11-10: the free plan allows up to 5 shows | capture: sha256:d0d7884f9939e73eef94dd6da1a5ce8e06435ef2f67704514d2acb2b1effd75a | quote: Launch a second podcast or a spinoff, up to 5 shows, all on the free plan.
- sources:
  - [1] https://zencastr.com/feature/hosting
  - [2] https://zencastr.com/pricing
  - [3] https://zencastr.ghost.io/announcing-changes-to-the-free-plan/
  - [4] https://zencastr.com/signup/plan/price_1ThCaEEp649wfj6R7JTfzgro
