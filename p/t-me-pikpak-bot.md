# Save to PikPak

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-pikpak-bot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-pikpak-bot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Save to PikPak (@PikPak_Bot)

- `debrid/telegram-pikpak-bot` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted bot (Telegram to cloud drive) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
- url https://t.me/PikPak_Bot
- free tier: The bot's page: 'Fast and safely collect files from Telegram with up to 10TB Private Cloud. Full support for torrent, magnet and more.' 25 096 monthly users. The 10 TB is the paid tier: PikPak's help centre says 'Free accounts include 6 GB of storage, and Premium includes 10 TB.' | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: 6 GB free storage; 3 cloud-download tasks a day on a free account
- per-object cap: No per-object cap is stated for the bot. The binding free limits are the 6 GB account store and 'three Cloud Download tasks per day'. | source: [2]
- retention: Files stay in the PikPak account until deleted or until the account lapses; a free account has 6 GB, so retention of a large library is a paid feature. | source: [3]
- egress: Downloading out of PikPak is metered per account: 'Free PikPak accounts have a daily Downstream limit of 20 GB, which resets at 0:00 Singapore Time. All Connected Apps together can use up to 25% of this daily limit, or 5 GB per day.' Upgrading to Premium removes that limit. | metered: yes | free allowance: 20 GB/day downstream on a free account | source: [3]
- identity: email | detail: PikPak registration is by email: 'An email address for registration and verification... No credit card is needed to start the basic free plan.' The bot then needs the account linked.
- interface: rest
- limits:
  - volume-quota (binding): 6 GB stored on a free account [1]
  - request-rate: 3 cloud-download tasks/day on a free account [2]
  - per-ip-shaping: 20 GB/day downstream on a free account; connected apps 5 GB/day [3]
- binding note: 6 GB of storage fails first: 1 TiB of monthly transfer cannot be stored on a free account at all, and the 3-task/day count fails alongside it.
- interface detail: A Telegram chat that acts as a remote control for a PikPak account. The file moves Telegram -> PikPak, so Telegram is the source and PikPak the store.
- tooling: Any Telegram client. Forwarding a channel post or sending a magnet/HTTP/Twitter/TikTok link is the whole interface.
- composes with: Sweeps files and magnets out of Telegram into a 6 GB free cloud store with a 20 GB/day egress meter; the reverse of a Telegram-as-drive path, and the only hosted bot found that moves bytes out of Telegram at scale.
- reliability: Free accounts are metered on both storage and downstream; reaching either daily or monthly connected-app limit slows traffic to about 100 KB/s rather than failing it.
- notes: Abandon if the 6 GB/3-task free tier changes. The 10 TB in the bot description is marketing for the paid tier and must not be read as a free number.
- evidence note: Bot description and user count from t.me; every number from PikPak's own help centre and FAQ. The mapping 'bot transfer counts as a cloud download task' is inferred, not stated.
- evidence:
  - [4] 2026-10-23: 'Fast and safely collect files from Telegram with up to 10TB Private Cloud. Full support for torrent, magnet and more.' with '25 096 monthly users'
  - [1] 2026-10-23: 'Free accounts include 6 GB of storage, and Premium includes 10 TB.'
  - [2] 2026-10-23: 'Free accounts include 6 GB of storage and three Cloud Download tasks per day.'
  - [3] 2026-10-23: 'Free PikPak accounts have a daily Downstream limit of 20 GB, which resets at 0:00 Singapore Time.' and the 5 GB/day connected-apps share
  - [5] 2026-10-23: third-party restatement: 'The free storage quota is 6GB' and no card needed; consistent with the vendor's own help centre
- sources:
  - [1] https://mypikpak.com/en-US/help-center/file_management/space/insufficient_cloud_storage_space
  - [2] https://mypikpak.com/en-US/help-center/referral_program/referral_reward/code-no-reward
  - [3] https://mypikpak.com/en-US/faq
  - [4] https://t.me/PikPak_Bot
  - [5] https://pikpak.jp/en/blog-free-trial.html
