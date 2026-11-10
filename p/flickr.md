# Flickr

> flickr.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/flickr/ | JSON https://fshy.ajam.dev/api/v1/entity/flickr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Flickr

- `storage/flickr` | fails-quota | evidence documented | binding volume-quota | category media
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:38.758Z (live) | stale on 2026-12-04
- url https://www.flickr.com
- free tier: Free: at most 1,000 items, of which at most 50 may be non-public. Pro (paid): unlimited storage, full-res uploads with no monthly cap; $11 per month, $82 per year or $148 per two years in domestic USD (third-party price report). | unit: objects | metered on: object-count | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and unmetered for public images (staticflickr.com CDN). Non-public content on free accounts is capped at 50 and at risk of deletion, so egress is real only for public photos. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - volume-quota (binding): 1,000 items in total; 50 non-public items [1]
- limits note: 1,000 items; 50 non-public items; free accounts limited to Safe content.
- binding note: the free plan stops at 1,000 items (50 non-public); an item count with no byte figure, so the nearest kind is volume-quota
- interface detail: rest
- tooling: Flickr API (OAuth1), flickr-sync; no native rclone backend; ShareX and Lightroom publish plugins.
- composes with: Unlimited free accounts x 1,000 items. This is a per-record cap, not a byte cap. But 1,000 items x 200 MB max = ~200 GB/account at absolute best, and item 1,001 is deleted.
- reliability: Enforcement is real and documented: over-limit accounts are suspended or have content deleted. Pro is required for any bulk use.
- notes: FREE TIER IS 1,000 ITEMS, NOT 1 TB. The famous 1 TB was killed on 2019-01-08. Free = 1,000 photos/videos total, of which max 50 may be non-public. Pro (paid) = unlimited storage, full-res, no monthly cap.
- evidence note: the 2026-11-03 read covered the Flickr free-account limits article (the Flickr help article on free-account limits and enforcement on www.flickrhelp.com: 1,000 items, 50 non-public, suspension or deletion over the limits) and the plan-selection page (https://www.flickr.com/registration/plan-selection: Pro with no monthly cap); the Pro price is from a third-party page, https://www.toolsurf.com/flickr-pricing-2026/
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: FREE TIER IS 1,000 ITEMS, NOT 1 TB. The famous 1 TB was killed on 2019-01-08. Free = 1,000 photos/videos total, of which max 50 may be non-public. Pro (paid) = unlimited storage, full-res, no monthly cap.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Store more than 50 Non-Public photos or videos'; 'Upload over 1,000 items'; 'Content that exceeds these limits is at risk of suspension or deletion'
  - [2] 2026-10-21: the 2018 announcement ending 1 TB for free accounts, effective Jan 8 2019
  - [3] 2026-10-21: paid tier still advertises 'Unlimited storage... Full-res uploads with no monthly cap' (Pro only)
  - [4] 2026-11-03: Pro price in domestic USD (third-party report) | capture: sha256:c96efeccb7c9688a875a4c6b425ba20cfdf4af455a1c4cb8717d1c991222c719 | quote: Flickr Pro costs $11/month, $82/year, or $148 for two years in domestic USD at the time of writing (September 2026).
  - [1] 2026-11-03: free accounts may not upload more than 1,000 items | capture: sha256:4d82bfef89186e221507e5c439b9acd5c28313959be0ad533ea9707ae95eb7a5 | quote: Upload over 1,000 items.
  - [1] 2026-11-03: free accounts may hold at most 50 non-public items | capture: sha256:4d82bfef89186e221507e5c439b9acd5c28313959be0ad533ea9707ae95eb7a5 | quote: Store more than 50 Non-Public photos or videos.
  - [1] 2026-11-03: over-limit content is at risk of suspension or deletion | capture: sha256:4d82bfef89186e221507e5c439b9acd5c28313959be0ad533ea9707ae95eb7a5 | quote: Content that exceeds these limits is at risk of suspension or deletion.
  - [3] 2026-11-03: Pro advertises unlimited storage with no monthly cap | capture: sha256:87be991df9f328e9ee1f537a89af24f24b5dd3bff69b83a53d6a1afaee2fb610 | quote: Full-res uploads with no monthly cap
- sources:
  - [1] https://www.flickrhelp.com/hc/en-us/articles/13690320471060-Free-account-limits-and-enforcement
  - [2] https://blog.flickr.net/en/2018/11/01/changing-flickr-free-accounts-1000-photos/
  - [3] https://www.flickr.com/registration/plan-selection
  - [4] https://www.toolsurf.com/flickr-pricing-2026/
