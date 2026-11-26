# Kling AI

> kling.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kling/ | JSON https://fshy.ajam.dev/api/v1/entity/kling.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kling AI

- `compute/kling-ai` | fails-quota | evidence unverified | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-06T15:56:55.348Z (live) | stale on 2026-11-21
- url https://kling.ai/pricing
- free tier: A free plan is claimed at 66 credits a day, and it is not confirmable from the vendor: three routes to the price list failed on 2026-10-22. Third-party accounts conflict. One review states 'The free plan gives all logged-in users 66 daily credits that expire after 24 hours' with a 5-second 720p clip at 30 credits. Another, dated 2026-09-26, states the opposite: 'the 66 free credits a day figure repeated across the web does not appear on any official Kling page we checked' and quotes Kling's own credits policy as granting daily credits to 'subscribers ... during the event (as shown in the interface)'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: unverified-event-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): if the 66-a-day allowance exists it is capped by resolution and watermark rather than by volume: the free tier is reported at 360p to 540p with a forced watermark and no commercial rights, so two clips a day at 30 credits each is the whole budget. [1]
- limits note: if the 66-a-day allowance exists it is capped by resolution and watermark rather than by volume: the free tier is reported at 360p to 540p with a forced watermark and no commercial rights, so two clips a day at 30 credits each is the whole budget.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: no chain can be proposed on an unverified allowance. Where the 66-a-day claim holds, two five-second clips a day is a slow storyboard feed; where it does not, is paid-only and Runway's 125-credit trial recorded in this record is the comparable entry.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The record exists to stop the next reader chasing a number that half the web repeats and no official page confirms. The global site moved from klingai.com to kling.ai and the new site publishes no credits table either: /pricing and /membership return marketing copy, app.klingai.com/pricing renders the app home, and kling.ai/dev/pricing redirects to a Kuaishou SSO login that does not load. The membership page of a logged-in free account is the only place the credit balance is published, and the balance before and after one generation is the measurement that decides the figure.
- extras:
  - facets.class: credit-too-small-for-a-workload
  - facets.free_tier_kind: unverified-event-allowance
  - facets.shape.gpu_count: 0
- evidence:
  - [2] 2026-10-22: 
  - [1] 2026-10-22: the pricing path served marketing copy and no credits table
  - [1] 2026-10-22: the nearest Wayback capture is 20260722194448 with status 446, a blocked capture of 654 bytes, so the archived price list is unreadable
  - [3] 2026-10-22: 'The free plan gives all logged-in users 66 daily credits that expire after 24 hours' with 'VIDEO 3.0, a 5-second 720p clip ... 30 credits', reported
  - [4] 2026-10-22: 'the 66 free credits a day figure repeated across the web does not appear on any official Kling page we checked on September 26, 2026', and Kling's credits policy restricts daily login credits to subscribers during events, reported
  - [1] 2026-11-06: the record's URL now serves a migration notice to the new global site | capture: sha256:ce1fc3d995374daf74e52767f652ec40a8cc1d7f3f983790558b472d383d6d7a | quote: Kling's global website has officially migrated to kling.ai.
  - [1] 2026-11-06: the vendor's own notice names kling.ai as the successor site | capture: sha256:ce1fc3d995374daf74e52767f652ec40a8cc1d7f3f983790558b472d383d6d7a | quote: Kling's global website has officially migrated to kling.ai.
  - [5] 2026-11-06: the new pricing path answers with marketing copy and no credits table | capture: sha256:9c561f317d7bf545a9fda9668132c73581871d6d4dab36bdbfd434d8099cee91 | quote: Cannes-Winning AI Short Film: L’Ultimo Uomo Reale
  - [2] 2026-11-06: the app pricing path renders the app home, 24,992 bytes, with no credits table | capture: sha256:1546e11782e77cc355ddb5f9bf0aa4a1e3614e15015703827032ebf1278515f1 | quote: Create Videos, Images and More in One Workspace
  - [6] 2026-11-06: the developer pricing link redirects to id.kling.ai/pass/ksi18n/login/passToken, a Kuaishou SSO login, and the page fails to load | capture: sha256:7d355ba5c242f5c395185932f60590b00b022f9df0b5f6fd9140b1aba84c85df | quote: This site can’t be reached
- sources:
  - [1] https://klingai.com/pricing
  - [2] https://app.klingai.com/pricing
  - [3] https://www.eesel.ai/blog/kling-ai-pricing
  - [4] https://www.kensa.cc/blog/ai-video-generator-free-credits
  - [5] https://kling.ai/pricing
  - [6] https://kling.ai/dev/pricing
