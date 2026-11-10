# LuluStream

> lulustream.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lulustream/ | JSON https://fshy.ajam.dev/api/v1/entity/lulustream.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LuluStream

- `debrid/lulustream` | qualifies-with-caveat | evidence documented | binding none | category ad-monetised video host (pay-per-view), free storage and streaming for publishers | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:40:52.506Z (live) | stale on 2026-11-23
- url https://lulustream.com/
- price USD 0
- free tier: "Unlimited storage" and "No Bandwidth Limitation" are listed as features of the free publishing account; the site's own pitch is "Make Money by sharing Videos online" with "Earn upto $35 per 10k Views". | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: Free hosting is funded by ads on the player and by the publisher's view earnings, not by a storage fee.
- per-object cap: Not stated on the page read. | source: [1]
- retention: Not stated on the page read. | source: [1] | note: The absence matters: every host in this class deletes inactive files, and this page does not say at what interval.
- egress: "No Bandwidth Limitation", HLS streaming, faster encoding. No allowance or price is printed. | metered: no | free allowance: unlimited, per the vendor | source: [1]
- identity: email | detail: A publishing account is required (the site is a publisher programme with earnings), and payouts imply a payment identity. The signup form was not read, so the exact email or KYC gate is unverified.
- interface: ftp, rest, unknown
- limits:
  - request-rate: unstated [1]
- limits note: The only published number is the earnings rate, not a capacity limit: '$35 per 10k Views (Counted 3 Views per 24 hours)'. A host that pays per view has an incentive to keep serving, which is a stronger retention signal than a promise.
- binding note: No counter is published, so none can bind as a number. What binds in practice is account action: a pay-per-view host closes an account that burns bandwidth without earning, and that enforcement is invisible until it happens.
- interface detail: "Upload via Browser, FTP, Remote, API & torrent" - four programme paths and a remote-URL pull, which is more than any other free video host among debrid providers documents on its front page.
- tooling: FTP plus an API means an existing upload pipeline can point at it without a wrapper. The site does not publish endpoint documentation on the page read, so the API would have to be discovered.
- composes with: Bulk video egress: a high-volume video service can put the long tail here at zero cost and keep only the hot set on a paid CDN. The remote-upload path also lets it pull from an existing host without a local copy.
- reliability: Pay-per-view hosting ties the account's survival to earnings: an account used purely as free CDN storage serves bandwidth the operator is not paid for. Expect throttling or deletion to arrive as an account decision, with no published quota to appeal to.
- notes: Documented as an egress surface, not a storage answer: the bytes are only useful if they are served, and this is a place that serves them for free while the vendor monetises the player.
- evidence note: The feature list, including the four upload paths, was read on the live page. The unlimited claims are the vendor's and were not measured; a deliberate large upload would be the test that matters.
- extras:
  - upload_paths: browser, FTP, remote URL, API, torrent
- evidence:
  - [1] 2026-10-23: 'Unlimited storage', 'No Bandwidth Limitation', 'Upload via Browser, FTP, Remote, API & torrent', HLS streaming and the '$35 per 10k Views' payout rate
- sources:
  - [1] https://lulustream.com/
