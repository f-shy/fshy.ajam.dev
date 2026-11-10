# Telegram

> telegram.org | Storage, Debrid; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/telegram/ | JSON https://fshy.ajam.dev/api/v1/entity/telegram.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Telegram — MTProto user account + unlimited channels as the volume

- `storage/telegram-mtproto-user-account-unlimited-channels-as-the` | qualifies-with-caveat | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://telegram.org
- free tier: No total storage cap, quoted from Telegram: 'you can ... share an unlimited number of photos, videos and files (doc, zip, mp3, etc.) of up to 2 GB each'. Per-file 2 GB free, 4 GB with Premium. Per-account volume is effectively unbounded because you can hold up to 500 channels/supergroups (1000 with Premium) and create up to 50 channels per day, and each channel is a separate unbounded blob store. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file 2 GB | bytes: 2000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and unmetered. Telegram charges nothing for downloads and imposes no transfer quota; the only egress cost is Telegram's own speed shaping. Downloads are free even for files uploaded by Premium users: 'any user can download large 2+ GB files uploaded by premium users'. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-ip-shaping: speed is throttled for non-Premium by an explicit server error, FLOOD_PREMIUM_ [1]
  - per-ip-shaping: speed is limited because the current account does not have a Premium subscri [1]
  - per-object-cap (binding): Per-file 2 GB [1]
- limits note: Per-file 2 GB free / 4 GB Premium. Verified against Telegram's own config, not a blog: upload_max_fileparts_default = 4000 and upload_max_fileparts_premium = 8000, times the max part size 524288 bytes = 2,097,152,000 B and 4,194,304,000 B. Upload speed is throttled for non-Premium by an explicit server error, FLOOD_PREMIUM_WAIT_X, which signals 'upload speed is limited because the current account does not have a Premium subscription'; upload_premium_speedup_upload = 10, i.e. Premium is ~10x faster. No published daily byte cap exists — Telegram documents none, and the empirical field report (Teldrive issue #561) is 10-50 GB/day for one user, with a maintainer answering 'I have seen user posting that they upload 400-500gb daily no issues. It depends on how many bots you have.' Treat 20 GB/day as folklore: no primary source found.
- interface detail: rest
- tooling: Strongest tooling of any provider in this whole research area. MTProto clients: TDLib (github.com/tdlib/td, 9.2k stars, pushed 2026-10-21), MadelineProto (github.com/danog/MadelineProto, 3.5k stars, pushed 2026-10-21, alive). Field-proven storage layer: Teldrive (github.com/tgdrive/teldrive, 3.1k stars) with its own rclone backend (github.com/tgdrive/rclone). CAUTION: Telethon (12.1k) and Pyrogram (4.6k) are both ARCHIVED (Telethon read-only since 2026-02-21, Pyrogram since 2024-12-23). Do not start a new build on either.
- composes with: Unbounded by construction: 1 account x 500 channels x unlimited posts = unlimited. A second account carries a second read allowance, not a second storage allowance. Teldrive adds its own layer: 'channel-part-limit: 500000' parts per channel with 'auto-channel-create: true'. It opens a NEW channel automatically when the active one fills, so the sharding is already automated. A 2 GB file is 4000 x 512KB parts, so one channel holds ~250 TB of max-size files before rotation.
- reliability: Throttling is the real risk, not deletion: FLOOD_PREMIUM_WAIT_X caps non-Premium throughput and FLOOD_WAIT_X backs off per method. Files persist indefinitely in practice, but a closed account takes its channels with it, and Teldrive's own README warns accounts and stored files 'can become unavailable', so a store that spans several accounts loses only the parts one account holds.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'share an unlimited number of photos, videos and files ... of up to 2 GB each' (line 77) and 'files of any type, up to 2 GB in size each (or 4 GB with Premium)' (line 338)
  - [2] 2026-10-21: live JSON: upload_max_fileparts_default=4000, upload_max_fileparts_premium=8000; descriptions state max file size = value x 524288
  - [3] 2026-10-21: FLOOD_PREMIUM_WAIT_X: 'upload speed is limited because the current account does not have a Premium subscription ... upload_premium_speedup_upload times'
- sources:
  - [1] https://telegram.org/faq
  - [2] https://core.telegram.org/api/config
  - [3] https://core.telegram.org/api/files

## Telegram Premium

- `debrid/telegram-premium` | paid-only | evidence documented | binding per-object-cap | category account subscription (upload tier) | tier premium
- needs card yes, phone unknown, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
- url https://telegram.org/faq_premium
- free tier: Not free. Premium's feature list carries '4 GB File Uploads' and 'Faster Download Speed'; the free account stays at 2 GB per file. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the free tier of the same product is recorded at storage/telegram-mtproto-user-account-unlimited-channels-as-the
- per-object cap: 4 GB per file, against 2 GB on a free account. | source: [1] | note: no byte-exact boundary is published; the FAQ says '4 GB'
- retention: Cloud chat media is kept until deleted. Telegram's FAQ: 'you can keep all your media in the cloud without deleting things'. | source: [2] | note: no retention window is stated for cloud chats; secret chats are excluded from the cloud entirely
- egress: 'Subscribing lifts any media download speed limits from your account on Telegram's side.' Non-subscribers can still fetch a Premium user's 2 GB+ file: 'any user can download large 2+ GB files uploaded by premium users.' | metered: no | free allowance: no byte allowance; the throttle is speed, not volume | source: [1]
- identity: card | detail: A paid subscription. The FAQ says the first payment's currency and price follow 'the country code of the phone number of your Telegram account', so the price is country-specific and was not read as a number.
- interface: rest
- limits:
  - per-object-cap (binding): 4 GB per file (2 GB free) [1]
  - per-ip-shaping: media download speed limits are lifted only for subscribers [1]
- binding note: 1 TiB/month at 4 GB is 256 objects; the object ceiling is still the first wall, and flood control is unreachable at that count.
- interface detail: Purchased and managed through the user or @PremiumBot; the upload ceiling applies to the account, not to an API.
- tooling: Any MTProto client or TDLib-based tool inherits the account's tier; Bot API bots do not, because a bot has no Premium tier of its own.
- composes with: Turns 2 GB objects into 4 GB objects for a TDLib or MTProto client, halving the object count of 1 TiB of monthly transfer; it does not lift any bot's 20 MB/50 MB limit.
- reliability: A free account downloading large media is speed-limited on Telegram's side; a Premium lapse returns the account to 2 GB objects and the speed limit immediately.
- notes: The price is a live gap: the FAQ defers it to the phone number's country, and @PremiumBot is the only quoter. Abandon the record if the 4 GB figure moves; re-check t.me/premium/5 at the same time.
- evidence note: Features and the speed sentence are on the Premium FAQ read. The price is deliberately not stated because the page states no figure.
- evidence:
  - [1] 2026-10-23: feature list lines '[4 GB File Uploads](https://t.me/premium/5)' and '[Faster Download Speed](https://t.me/premium/7)'
  - [1] 2026-10-23: 'Subscribing lifts any media download speed limits from your account on Telegram's side.'
  - [1] 2026-10-23: 'This also applies to files: any user can download large 2+ GB files uploaded by premium users.'
  - [2] 2026-10-23: 'Send and receive files of any type, up to 2 GB in size each (or 4 GB with Premium)'
- sources:
  - [1] https://telegram.org/faq_premium
  - [2] https://telegram.org/faq

## telegram cloud bot api alone (api.telegram.org)

- `storage/telegram-cloud-bot-api-alone` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://core.telegram.org/bots/api/methods/getfile
- free tier: none reachable: Hard 20 MB download ceiling via getFile and 50 MB multipart upload. getFile links also expire: 'It is guaranteed that the link will be valid for at least 1 hour.' Unusable as a storage API… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: retention
  - dead_end.why: Hard 20 MB download ceiling via getFile and 50 MB multipart upload. getFile links also expire: 'It is guaranteed that the link will be valid for at least 1 hour.' Unusable as a storage API…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Hard 20 MB download ceiling via getFile and 50 MB multipart upload. getFile links also expire: 'It is guaranteed that the link will be valid for at least 1 hour.' Unusable as a storage API…
- sources:
  - [1] https://core.telegram.org/bots/api/methods/getfile
