# Media.cm

> media.cm | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/media/ | JSON https://fshy.ajam.dev/api/v1/entity/media.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Media.cm

- `debrid/media-cm` | qualifies-with-caveat | evidence documented | binding none | category free video hosting and HLS streaming host (ad-free), player-embed model | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:44.527Z (live) | stale on 2026-12-26
- url https://media.cm/
- price EUR 0
- free tier: "Free and unlimited storage - Stream all your videos freely; we offer endless bandwidth at no charge, and your videos never expire." Also ad-free for free users, and "Unlimited uploads: No limits on size or length." | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The strongest free claim among debrid providers and the least independently verifiable: three separate unlimiteds (storage, bandwidth, file size) on one page.
- per-object cap: "Unrestricted video uploads: No limits on size or length." | source: [1] | note: Documented as the vendor's claim. No upload was attempted, so a hidden limit above a few GB would not have been seen.
- retention: "your videos never expire" | source: [1] | note: No inactivity clause is printed, unlike every other video host in this set.
- egress: "we offer endless bandwidth at no charge". Streaming is HLS, with 'Stream in 4K Ultra HD ... up to 2160p at 60 frames per second' and optional HLS encryption. | metered: no | free allowance: unlimited, per the vendor | source: [1]
- identity: email | detail: An account is implied by 'your videos' and the upload flow; the signup form was not read, so the exact gate (email versus OAuth) is unverified.
- interface: browser
- limits:
  - per-ip-shaping: unstated; no rate, connection or daily-volume limit is published [1]
- limits note: Three unlimited claims and no numbers at all. The only premium figure is the paid tier's '10 TB of bandwidth and storage for a simple EUR 10/month', which is smaller than the free tier claims, so the free tier is not a trial of the paid one.
- binding note: No counter is published, so no counter can be named as binding.
- interface detail: The page read describes the player, the upload form and embedding only. No API, FTP or CLI is mentioned on the homepage; the premium page path /premium returns 404, so the paid tier's terms were not read.
- tooling: Browser upload and an embed code. No API was found, which here is a tooling note and not a verdict: the page's own HTTP endpoints would have to be reversed or driven by a browser session.
- composes with: An egress surface rather than a retrieval one: it takes 500 GB to 1 TB of served video a day off a paid CDN and puts it on a free host that monetises somewhere else. It pairs with a downloader front end that never touches the bytes.
- reliability: The economics do not add up on the page: unlimited free bandwidth with no ads and no expiry is funded by something the site does not disclose, and the paid tier's 10 TB is a cap the free tier claims not to have. Expect the free claim to be enforced by account action rather than by a published limit.
- notes: Video hosting service advertising unlimited free HLS bandwidth and 4K streaming. No programmatic path found: The page read describes the player, the upload form and embedding only. No API, FTP or CLI is mentioned on the homepage; the premium page path /premium returns 404, so the paid tier's terms were not read.
- evidence note: Every claim here is the vendor's sentence, read. None was measured; a 10 GB upload would be the cheapest way to test whether 'no limits on size' survives contact. Until then the record states the claim and says it is a claim.
- extras:
  - ad_free: explicitly ad-free even for free users, which is unusual for the video-host model and is the reason the bandwidth claim is worth testing
- evidence:
  - [1] 2026-10-23: the four claims verbatim: free unlimited storage, endless bandwidth at no charge, videos never expire, unlimited uploads with no size or length limit; plus the premium tier at EUR 10/month for 10 TB
  - [2] 2026-10-23: there is no /premium route (404 'Not Found'), so the paid terms are only those summarised on the homepage
  - [1] 2026-11-25: the free storage, bandwidth and no-expiry claims are unchanged | capture: sha256:5889da8a4b198f9264b15b5079c9bbc6331d2ea539a74a6e1e8707b1fc8acb8b | quote: Stream all your videos freely; we offer endless bandwidth at no charge, and your videos never expire.
  - [1] 2026-11-25: a free user tier exists; the sign-up page itself was not read | capture: sha256:5889da8a4b198f9264b15b5079c9bbc6331d2ea539a74a6e1e8707b1fc8acb8b | quote: Ad-free Enjoy an ad-free streaming experience, even as a free user—your videos will always be free of ads.
- sources:
  - [1] https://media.cm/
  - [2] https://media.cm/premium
