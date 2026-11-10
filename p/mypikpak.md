# PikPak

> mypikpak.com | Storage, Debrid, Netdisk and pan; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mypikpak/ | JSON https://fshy.ajam.dev/api/v1/entity/mypikpak.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PikPak

- `storage/pikpak` | qualifies-with-caveat | evidence reported | binding write-gated | category private cloud drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://mypikpak.com/
- price $0.50/TB/mo on US Premium ($4.99/mo for 10 TB); $1.00/TB/mo on Global Premium ($9.99/mo) — but capped at 5 GB/day of egress through rclone, which dominates the economics | parsed USD 0.5/TB-mo
- free tier: 6 GB free. Premium includes 10 TB base storage (expandable for purchase). No free route to >=500 GB: the free tier is 6 GB flat. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered twice over. Free accounts have a daily downstream quota; every account, free or paid, has a monthly Basic Transfer Quota, and 'Connected Apps share 25% of this daily allowance — up to 5 GB per day for all Connected Apps combined'. Downstream counts playback and previews, not just downloads. | metered: yes
- identity: email | detail: email
- interface: rest, rclone
- limits:
  - per-ip-shaping: 20 GB/day [1]
  - per-ip-shaping: 5 GB/day [1]
  - write-gated (binding): reviews and online playback burn downstream quota, so scrape-style read patterns drain [1]
- limits note: per-ip-shaping / pull-count hybrid: 20 GB/day downstream on free, 5 GB/day for all Connected Apps combined, monthly transfer quota on top. Free tier 6 GB storage. This provider is the cleanest illustration that quota and egress must be scored separately.
- interface detail: rest
- tooling: Tier 1 rclone backend since v1.62, read-only for uploads? No. Backend supports read and write per rclone's table (ModTime R, hash md5). This is the crucial detail: rclone is classified as a 'Connected App', so it inherits the 5 GB/day cap.
- composes with: Paid accounts offer up to 10 TB storage. Transfer limits restrict downloads to 5 GB per day via connected applications and 20 GB per day general downstream. Multiple accounts scale storage capacity while egress remains bound to individual daily quotas.
- reliability: Transfer accounting is aggressive: previews and online playback burn downstream quota, so scrape-style read patterns drain it without any download. Price differs by region (US $4.99/mo Premium, Japan JPY 700, 'Global Premium' $9.99/mo).
- notes: the same as the free tier
- extras:
  - price_verbatim: $0.50/TB/mo on US Premium ($4.99/mo for 10 TB); $1.00/TB/mo on Global Premium ($9.99/mo) — but capped at 5 GB/day of egress through rclone, which dominates the economics
- evidence:
  - [1] 2026-10-21: 'Free accounts include 6 GB of storage, and Premium includes 10 TB'
  - [2] 2026-10-21: 'Premium includes 10 TB of base storage. You can purchase additional storage on PikPak Web'
  - [3] 2026-10-21: 'a daily downstream limit of 20 GB... Apps share 25% of this daily allowance — up to 5 GB per day for all Connected Apps combined'
  - [4] 2026-10-21: 'Downstream quota covers all data delivered from PikPak to your device or Connected Apps, including online playback, previews, and file downloads'; separate 'Monthly Basic Transfer Quota'
  - [5] 2026-10-21: native backend, added v1.62, Tier 1
  - [6] 2026-10-21: Premium monthly USD 4.99 US; Global Premium USD 9.99 per apppriceatlas.com
  - [7] 2026-10-21: 'started for free with 6GB of storage... An email address for registration and verification... No credit card'
- sources:
  - [1] https://mypikpak.com/en-US/help-center/file_management/space/insufficient_cloud_storage_space
  - [2] https://mypikpak.com/en-US/help-center/premium/premium_features/space_expansion
  - [3] https://mypikpak.com/en-US/connect-apps-faq
  - [4] https://mypikpak.com/en-US/help-center/transfer_quota/transfer_quota_basics/why-limit
  - [5] https://rclone.org/pikpak/
  - [6] https://apppricelens.com/app/pikpak-cloud-storage-saver-1616861537
  - [7] https://pikpak.jp/en/blog-free-trial.html

## PikPak - free account (cloud download plus downstream)

- `debrid/pikpak-free-download` | qualifies-with-caveat | evidence documented | binding volume-quota | category private cloud drive with a cloud-download engine | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:15:33.000Z (live) | stale on 2026-11-23
- url https://mypikpak.com/en-US/faq
- price USD 0
- free tier: 'Free accounts include 6 GB of storage, and Premium includes 10 TB.' Downstream is metered on every account: 'Free PikPak accounts have a daily Downstream limit of 20 GB, which resets at 0:00 Singapore Time. All Connected Apps together can use up to 25% of this daily limit, or 5 GB per day.' | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: Two counters, not one: 20 GB/day for the official apps and 5 GB/day for anything programmatic (WebDAV, CLI, MCP, personal access tokens). The 6 GB store is what the downloaded bytes must pass through, exactly as CloudPipe's 450 GB must pass through a 15 GB Google Drive.
- per-object cap: not stated. No per-object number is published; the limits that bite on a free account are the 6 GB store and three Cloud Download tasks a day. | source: [1] | note: A 20 GiB object cannot be held in a 6 GB store at all, so the object cap is the store, not a published file limit.
- retention: files stay in the account until deleted, and the free account holds 6 GB, so retention is bounded by capacity rather than by a day count. Non-Premium accounts with no login for 12 consecutive months may be deleted. | source: [1]
- egress: Metered in three dimensions per calendar month: cloud download 40 TB, downstream 4 TB, upload 1 TB, then a separate free-account daily downstream cap of 20 GB. 'All Connected Apps together can use up to 25% of this daily limit, or 5 GB per day.' Over the limit 'Downstream traffic slows to about 100 KB/s' and 'New Cloud Download tasks are blocked'. | metered: yes | free allowance: 20 GB/day downstream in the official apps; 5 GB/day for Connected Apps | source: [1]
- identity: email | detail: Registration is by email. No card and no phone is named on the help-centre pages read; the signup form itself was not opened, so this is the published gate rather than an observed one.
- interface: webdav, cli, rest
- limits:
  - volume-quota (binding): 6 GB of storage on a free account [2]
  - volume-quota (binding): 20 GB/day downstream for the whole free account, resets at 0:00 Singapore Time [1]
  - volume-quota (binding): 5 GB/day downstream for all Connected Apps together (25% of the daily cap) [1]
  - request-rate: three Cloud Download tasks a day on a free account [1]
- limits note: The monthly 4 TB downstream quota is not the binding number for a free account; the daily cap is, by a factor of 120.
- binding note: At 5 GB/day a programmatic client gets 150 GB/month and at 20 GB/day an app-only client gets 600 GB/month. Both are below every other group-1 step except Bitport, and both require deleting through a 6 GB store.
- interface detail: official apps plus WebDAV, an official CLI, an MCP server and personal access tokens, all grouped by the vendor as 'Connected Apps' and all subject to the 5 GB/day cap
- tooling: rclone over WebDAV or the CLI; both land in the Connected Apps bucket and take the quarter allowance
- composes with: Adds 150 GB a month to a no-card ladder for one email address, making it the largest per-signup free step that is not CloudPipe. Its counter resets daily, so it repeats in month two.
- reliability: Over the daily cap downstream slows to about 100 KB/s and new cloud-download tasks are blocked while running ones continue; a free account with no login for 12 months may be deleted.
- notes: The number that matters to the ladder is 150 GB/month programmatic, not 600: the service is driven with a script, and the vendor caps every programmatic path at 25% of the daily allowance.
- evidence note: Both counters are vendor sentences read.
- extras:
  - gb_month_programmatic: 150
  - gb_month_app_only: 600
  - daily_reset_sentence: yes
  - existing_records: netdisk-pan/pikpak; storage/pikpak; scratch (removed)
- evidence:
  - [1] 2026-10-23: 'Free PikPak accounts have a daily Downstream limit of 20 GB, which resets at 0:00 Singapore Time. All Connected Apps together can use up to 25% of this daily limit, or 5 GB per day.' Also the 40 TB / 4 TB / 1 TB monthly tab and the 12-month inactivity deletion.
  - [2] 2026-10-23: 'Free accounts include 6 GB of storage, and Premium includes 10 TB.'
- sources:
  - [1] https://mypikpak.com/en-US/faq
  - [2] https://mypikpak.com/en-US/help-center/file_management/space/insufficient_cloud_storage_space

## PikPak Global Premium (10 TB)

- `storage/pikpak-global-premium` | fails-egress | evidence reported | binding per-ip-shaping | category cloud drive / BT saver
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://mypikpak.com/drive/payment
- price $0.833/TB/mo at 10 TB ($99.99/yr Global Premium). Usable programmatic egress is 1 TB/month (25% × 4 TB downstream). Effective cost per TB actually retrievable per month is fine, but the ceiling makes it unusable for serving… | parsed USD 0.833/TB-mo
- free tier: 10 TB storage on Premium; additional storage purchasable | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: HARD METERED, and worse for programmatic use. Verbatim from help centre: base quotas are 'Cloud Download: 40 TB per month. Downstream: 4 TB per month, including playback, previews, and downloads. Upload: 1 TB per month.' And 'Connected Apps share a combined transfer quota limit equal to 25% of your monthly Transfer Quota, across all three traffic dimensions.' So rclone/WebDAV/CLI. The only programmatic paths. Get 25% of 4 TB = 1 TB/month downstream. | metered: yes | free allowance: 40 TB per month
- identity: card | detail: email + card (or App Store IAP)
- interface: webdav, rclone, cli
- limits:
  - per-ip-shaping (binding): 20 GB/day [1]
  - per-ip-shaping (binding): 33 GB/day [1]
- limits note: Connected-Apps cap = 25% of monthly quota; free accounts also have a 20 GB/day downstream limit
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: WebDAV (read-only, premium-only, 'experimental'), official CLI, rclone backend
- tooling: rclone 'pikpak' backend exists; WebDAV is read-only and flagged incomplete by the vendor
- composes with: rclone; CLI; NOT a general object store
- reliability: The storage price is a decoy; the product is a BT/magnet cache.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 TB storage on Premium; additional storage purchasable
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $0.833/TB/mo at 10 TB ($99.99/yr Global Premium). Usable programmatic egress is 1 TB/month (25% × 4 TB downstream). Effective cost per TB actually retrievable per month is fine, but the ceiling makes it unusable for serving or bulk restore. Reject on egress, not on price.
- evidence:
  - [2] 2026-10-21: 'Cloud Download: 40 TB per month. Downstream: 4 TB per month, including playback, previews, and downloads. Upload: 1 TB per month.'
  - [3] 2026-10-21: 'Connected Apps share a combined transfer quota limit equal to 25% of your monthly Transfer Quota, across all three traffic dimensions … When your Connected Apps reach this limit, their requests will be throttled'; 'Free PikPak accounts have a daily downstream limit of 20 GB'
  - [4] 2026-10-21: 'Global Premium Yearly … $99.99 per year'
  - [5] 2026-10-21: PikPak's WebDAV is read-only and premium-only
- sources:
  - [1] https://mypikpak.com/drive/payment
  - [2] https://mypikpak.com/en-US/help-center/play_and_download/transfer_quota/meaning
  - [3] https://mypikpak.com/en-US/connect-apps-faq
  - [4] https://apppriceatlas.com/subscriptions/pikpak-cloud-storage-saver-global-premium-yearly-yearly/countries/us/
  - [5] https://blog.hentioe.dev/posts/pikpak-webdav-rclone.html

## PikPak (mypikpak.com)

- `netdisk-pan/pikpak` | fails-quota | evidence unverified | binding per-object-cap | category consumer-pan
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:21:08.723Z (live) | stale on 2026-11-19
- url https://mypikpak.com/
- free tier: no free storage quota is stated on the landing page; the product is sold as a private cloud drive with a cloud-download engine | unit: none | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not established; the pricing page is served as a non-HTML body that the reader refused | source: [1]
- retention: not established | source: [1]
- egress: not established; recorded as metered:false because no per-GB price or cap was found, which is an absence of evidence and not evidence of absence | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): not established [1]
- binding note: Nothing numeric could be established first-hand, so the record names the cap as the thing that would decide and records it as unestablished.
- tooling: unofficial drivers only: an rclone pikpak backend (username and password) and an OpenList PikPak driver that can simulate the Android client; both mount a personal drive, and download links are bound to the requesting address. The product's value is server-side torrent and magnet download into the drive
- composes with: a cloud-download engine rather than a store: it fetches a magnet to its own disk, which is useful for acquiring a corpus and not for holding one
- reliability: The pricing page is served as a binary body, so its plan table could not be read through the reader; the landing page states the cloud-download speed claim without a quota.
- notes: The landing page advertises high-speed cloud transfer to drive storage. Detailed quota, retention, and transfer pricing terms are unconfirmed because mypikpak.com/en/price returned non-HTML dynamic content to automated HTTP requests.
- extras:
  - access_mode: registration-gated
  - blocked: pricing page served as a binary body
- evidence:
  - [1] 2026-10-22: the landing page describes a private cloud drive with a cloud-download server and claims 'more than 80% of the files can be downloaded to your PikPak private Cloud Drive within a few seconds'; it states no storage quota
  - [2] 2026-10-22: the page reader refused the page as 'not-html:binary' and a second fetch returned a compressed binary body, so the plan table could not be read
  - [3] 2026-11-03: the OpenList PikPak driver emulates the Android client, so a reverse-engineered client reaches the drive | capture: sha256:64460cf2ca973ca80ee1a67708c30c97e0f847d929bda7835af441d8c3a3a325 | quote: If you choose `android`, it will simulate the Android client for access.
  - [1] 2026-11-03: the landing page offers cloud download of torrent, magnet and URL links into the drive and states no storage quota | capture: sha256:596c21157cb12b144d3ff71f74e67aebc9f6eecf3b14b4a0908fa36a127e60bc | quote: Torrent · Magnet · URL
  - [1] 2026-11-03: the landing page presents a cloud-download drive and states no storage quota | capture: sha256:596c21157cb12b144d3ff71f74e67aebc9f6eecf3b14b4a0908fa36a127e60bc | quote: Torrent · Magnet · URL
- sources:
  - [1] https://mypikpak.com/
  - [2] https://mypikpak.com/en/price
  - [3] https://doc.oplist.org/guide/drivers/pikpak
