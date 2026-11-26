# Audiomack

> audiomack.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/audiomack/ | JSON https://fshy.ajam.dev/api/v1/entity/audiomack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Audiomack

- `storage/audiomack` | qualifies-with-caveat | evidence documented | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T13:25:54.292Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://audiomack.com
- free tier: Unlimited everything - for Free | unit: unlimited | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: unverified: no per-file cap stated by Audiomack | source: [1] | note: No per-file cap is stated on the creator page.
- retention: source: [1] | note: Deleting an upload is permanent; no automatic expiry is stated in the help article.
- egress: Every upload creates a free embeddable player placeable on third-party sites; the creator page states unlimited hosting for free. | metered: no
- identity: email | detail: The join form asks for an email address, a username and a password; no phone number or card is shown on the form.
- interface: browser
- limits:
  - per-object-cap (binding): unverified: no per-file cap stated by Audiomack [1]
- limits note: 250 MB per file (medium confidence. Audiohostings.com's October 2026 table, not Audiomack's own page); no published storage or bandwidth total.
- interface detail: wrapper-only
- tooling: Creator dashboard and mobile app; no public upload API found.
- composes with: The creator page states unlimited hosting for free; no provider-stated per-file cap is published.
- reliability: Streaming-only platform: no original-file download path was found, so the payload is retrievable only as a transcode or not at all. The 'limitless' claim is about upload count, not about giving you a URL to your bytes.
- notes: Unlimited uploads, free forever: 'Audiomack is a FREE, limitless music sharing and discovery platform'; 'Whether you have 1 song or 1,000, Audiomack lets you host it all for free. No premium creator accounts ever!'. Per-file cap 250 MB (third-party spec sheet, not vendor-confirmed).
- evidence note: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Audiomack is a FREE, limitless music sharing and discovery platform'; 'No Premium Creator Accounts - Completely Free'; 'Whether you have 1 song or 1,000, Audiomack lets you host it all for free'
  - [2] 2026-10-21: Oct 2026 table: Audiomack max file size 250 MB, registration required (third-party)
  - [2] 2026-11-09: the table says registration is required but names no credential | capture: sha256:c0fc04707595cc5f844d4cfc877ddb32a0c5f92626c0b7a9457b47228df340f2 | quote: | Audiomack[Audiomack review »](https://www.audiohostings.com/audiohost/audiomack) | 250 MB | yes |
  - [1] 2026-11-09: the creator page states unlimited hosting for free | capture: sha256:7db6acce1876c2cb4fcfaa4b21b6d530570c42f2e595b9d1e84eabdc261ce9ed | quote: Unlimited everything - for Free
  - [3] 2026-11-25: the documented upload flow uses a web page after login | capture: sha256:87d75234f072fcc0d794e5207b47bfffbe4a961d7d0bd082be331775ac1b7826 | quote: Click on the "Upload" button in the upper right corner of the page.
  - [4] 2026-11-25: deletion is permanent | capture: sha256:48b146273b3796369529c94b574b130f6e7ce7f75dbabbfad3d1e7dfd8054ca3 | quote: Deleting an upload is permanent
  - [1] 2026-11-25: a free embed player is provided for every upload and can be placed on third-party sites | capture: sha256:7db6acce1876c2cb4fcfaa4b21b6d530570c42f2e595b9d1e84eabdc261ce9ed | quote: Every upload on Audiomack creates a free, customizable embed player which can be placed on any 3rd party blog, platform, or site.
  - [1] 2026-11-25: the creator page states unlimited hosting for free and gives no file-size figure | capture: sha256:7db6acce1876c2cb4fcfaa4b21b6d530570c42f2e595b9d1e84eabdc261ce9ed | quote: including unlimited hosting, advanced stats, powerful scheduling and content sharing tools, and monetization - completely free.
  - [1] 2026-11-25: the creator page states unlimited hosting for free | capture: sha256:7db6acce1876c2cb4fcfaa4b21b6d530570c42f2e595b9d1e84eabdc261ce9ed | quote: Unlimited everything - for Free
  - [5] 2026-11-25: the join form asks for a username alongside email and password | capture: sha256:b7185e6105a22454bd0a84c9ee54d2d38dc7751d17769bf999da2648fd6e37ad | quote: Choose a Username \*
  - [2] 2026-11-25: a third-party comparison table reports a 250 MB per-file cap | capture: sha256:d65cf82c421165b8ee42413417053f64c95913e0bfd2a1b8da584bfc085d43c2 | quote: | Audiomack[Audiomack review »](https://www.audiohostings.com/audiohost/audiomack) | 250 MB | yes |
- sources:
  - [1] https://creators.audiomack.com/about
  - [2] https://www.audiohostings.com/
  - [3] https://audiomack.zendesk.com/hc/en-us/articles/6941905981594-How-do-I-upload-my-songs-using-a-computer
  - [4] https://audiomack.zendesk.com/hc/en-us/articles/360014026171-How-do-I-delete-an-upload
  - [5] https://audiomack.com/join
