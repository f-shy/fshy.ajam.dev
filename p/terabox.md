# TeraBox

> terabox.com | Storage, Netdisk and pan; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/terabox/ | JSON https://fshy.ajam.dev/api/v1/entity/terabox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TeraBox (Baidu / Flextech)

- `storage/terabox` | qualifies | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.terabox.com
- disagrees on identity_kind: `storage/terabox` says institution, `storage/terabox-2` says email
- disagrees on verdict: `storage/terabox` says qualifies, `storage/terabox-2` says fails-identity
- free tier: 1024 GB free ('Network disk capacity limited to 1024GB' on the free column; '1TB Free Cloud Storage for Basic & 2TB Storage for Pro'); Premium/Pro 2048 GB | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GB/file | bytes: 4000000000 | source: [1] | note: not stated
- retention: ~4 GB/file free; ~7-day share-link life; one concurrent download; first-party web login carries a jsToken automated-traffic filter layer | days: 7 | source: [1] | note: not stated
- egress: Direct share links, no per-GB fee; free accounts throttled (~2-5 GB/day measured by third parties) and one download at a time | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 4 GB/file [1]
- limits note: ~4 GB/file free; ~7-day share-link life; one concurrent download; first-party web login carries a jsToken automated-traffic filter layer
- interface detail: rest
- tooling: Unofficial web API (app_id=250528, jsToken) + rclone fork bclone / gulp79/rclone-extra (upstream PR #8508 still open); official Open Platform OAuth is partner-gated
- composes with: 1 TB per account, and a second account carries a second allowance; email/SSO signup keeps identity cost low, but the 4 GB/file free cap forces splitting
- reliability: no official rclone backend; free-tier daily download cap makes it archive-shaped, and the web API breaks when the client changes
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Network disk capacity limited to 1024GB' free column; title '1TB Free Cloud Storage for Basic & 2TB Storage for Pro'
  - [2] 2026-10-21: and /thai/ and /vietnamese/ and /indonesian/ — all show '1024 GB' free, 2048 GB paid; the '5GB ... gratuito' strings belong to the OneDrive/Google Drive comparison rows
  - [3] 2026-10-21: crawl render shows 'Sign in with Google', 'Phone or Email', 'Registered with phone No.?'; raw HTML carries thirdLoginSdk {apple, kakao, google, line, facebook} and a dial-code phone widget
  - [4] 2026-10-21: probe: GET -> {"errmsg":"user not login","errno":-6}
- sources:
  - [1] https://www.terabox.com/cloud-storage-pricing-plans
  - [2] https://www.terabox.com/portuguese/cloud-storage-pricing-plans
  - [3] https://www.terabox.com/login
  - [4] https://dm.1024terabox.com/api/quota?...&app_id=250528

## TeraBox (terabox.com)

- `netdisk-pan/terabox` | qualifies-with-caveat | evidence reported | binding per-object-cap | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T00:21:08.723Z (live) | stale on 2026-11-19
- url https://www.terabox.com/
- free tier: 1024 GB of free cloud storage on registration | unit: GB | metered on: stored-bytes | read on: 2026-10-22 | source: [1] | note: the official site title and the app store listing both state 1024GB free
- per-object cap: 128 GB per upload is stated for Premium users on the vendor page; the free plan's per-file upload cap is unverified: not stated on the page read | source: [2] | note: 128 GB is the sharing figure the app listing states; it is not established as the upload figure
- retention: Unpublished in accessible landing pages. | source: [1]
- egress: Unpublished on public pricing documentation. Defaults to unmetered in the absence of explicit per-gigabyte bandwidth fees or caps. | metered: no | source: [1]
- identity: email | detail: registration is stated to be by email or phone through the app
- interface: rest
- limits:
  - per-object-cap (binding): 128 GB per shared file as stated in the app listing [2]
- binding note: The 1 TiB quota is not the constraint; the absence of a documented programmatic interface and of a readable limits page is, because neither the cap nor the retention could be established first-hand.
- tooling: no official public API documented; the OpenList project ships a reverse-engineered TeraBox driver that authenticates with a browser session cookie and is not maintained, so a reverse-engineered client mounts it with…
- composes with: 1 TiB free is the largest single-tier free quota in the consumer set, but every route to it is either an app or an undocumented API
- reliability: Automated HTTP retrieval received verification challenge pages on 2026-10-22, preventing direct first-hand inspection of the web dashboard.
- notes: 1024 GB free is stated by the official site title and by the app store listing. The per-file cap of 128 GB is the app listing's sharing figure and is not the same thing as an upload cap. What could not be established: retention, egress terms, and whether an anonymous or email-only registration produces a usable account. The site returned a verification interstitial to the reader on 2026-10-22, so this is `reported` and not `documented`.
- extras:
  - access_mode: registration-gated
  - official_api: not documented
  - third_party_drivers: Cloudreve; AList/OpenList
- evidence:
  - [1] 2026-10-22: the page title and meta description returned by the reader were 'TeraBox - Free Cloud Storage Up To 1 TB, Send Large Files Online', and the final URL was /simple-verify with the body 'Verification code was entered incorrectly', so the landing page itself was not served
  - [2] 2026-10-22: '1024GB of FREE Cloud Storage' on registration, and 'Upload, store, and share big files up to 128 GB seamlessly'
  - [1] 2026-11-03: the vendor landing page, read through a firecrawl pin, states 1024 GB of cloud storage | capture: sha256:476fe1d864de41c12f801bc37154d465d11bd243f430fe93c2ee476b0540e399 | quote: 1024GB Cloud Storage
  - [1] 2026-11-03: the 128 GB upload figure applies to Premium users, so it is not the free plan's cap | capture: sha256:476fe1d864de41c12f801bc37154d465d11bd243f430fe93c2ee476b0540e399 | quote: Premium users can upload files up to 128 GB at a time.
  - [3] 2026-11-03: the OpenList TeraBox driver is reverse-engineered and not actively maintained | capture: sha256:ce3286ea214026071ec8a91caf6aeb136ad5179c2d9722a71fbbc1ff19ff0b6f | quote: This interface is a reverse-engineered interface based on legacy products.
- sources:
  - [1] https://www.terabox.com/
  - [2] https://play.google.com/store/apps/details?hl=en_US&id=com.dubox.drive
  - [3] https://doc.oplist.org/guide/drivers/terabox

## terabox (kr/id/jp localisation)

- `storage/terabox-2` | fails-identity | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.terabox.com/indonesian
- disagrees on identity_kind: `storage/terabox` says institution, `storage/terabox-2` says email
- disagrees on verdict: `storage/terabox` says qualifies, `storage/terabox-2` says fails-identity
- free tier: none reachable: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub…
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub…
  - [2] 2026-10-21: cited as the basis of the rejection: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub, a
  - [3] 2026-10-21: cited as the basis of the rejection: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub, a
- sources:
  - [1] https://www.terabox.com/indonesian
  - [2] https://www.terabox.com/english
  - [3] https://bokgoon.com/free-cloud-storage-services/
