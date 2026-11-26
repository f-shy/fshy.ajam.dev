# WangPan netdisk bot

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-wangpanbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-wangpanbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WangPan netdisk bot (@WangPanBOT)

- `debrid/telegram-wangpan-bot` | dead | evidence documented | binding none | category hosted bot (Telegram-native netdisk) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:48.488Z (live) | stale on 2026-12-26
- url https://t.me/WangPanBOT
- free tier: Dead. The handle no longer resolves to a bot: t.me/WangPanBOT returns 'Telegram: Contact @WangPanBOT' with a Send Message action and no Start Bot action, so the username now belongs to a user account. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: Not applicable: the bot is gone. When it lived it advertised mounts and share links, not a size. | source: [2] | note: the directory entry is the only surviving description
- retention: Not applicable: no service to retain anything. | source: [1]
- egress: Not applicable. | metered: no | source: [1]
- identity: any-phone | detail: Was a Telegram account; the handle now resolves to a user, not a bot.
- interface: unknown
- limits note: No live limit exists to name.
- binding note: Nothing binds because nothing is served.
- interface detail: Was a Telegram chat bot. Now a Telegram user account at @WangPan.
- tooling: None: nothing to point a client at.
- composes with: Nothing. Preserved so the subsequent audit does not spend a wave looking for it.
- reliability: The failure mode this record documents: a username can be reassigned to a user account, so a bot's handle is not a durable identifier.
- notes: Do not re-open unless the @WangPan handle is seen running as a bot again. The class it represented (a hosted Telegram-native netdisk with mounts) has no living hosted member found on 2026-10-23.
- evidence note: The t.me page was read and shows a Contact action with no Start action and no description. That is the death certificate for the bot form of the handle.
- evidence:
  - [1] 2026-10-23: the page title is 'Telegram: Contact @WangPan' with no Start Bot action and an empty description - the username resolves to a user, not a bot
  - [3] 2026-10-23: the Chinese bot directory (post 73) described it as 'WangPan netdisk bot ... free, safe, anonymous ... supports full mounts, link sharing, transfer, search'
  - [1] 2026-11-25: the handle offers a contact action and no Start Bot action, so it is a user account, not a bot | capture: sha256:334e02245161e6c174ef595fd358f28d2350e88858b094fe261d8a9d9ffd0911 | quote: If you have Telegram, you can contact [@WangPanBOT](tg://resolve?domain=WangPanBOT) right away.
  - [1] 2026-11-25: the page is a user contact, not a launchable bot | capture: sha256:334e02245161e6c174ef595fd358f28d2350e88858b094fe261d8a9d9ffd0911 | quote: Telegram: Contact @WangPanBOT
  - probe:https://t.me/WangPanBOT 2026-11-25:  | capture: sha256:25c43df80b2e8d42af51ac52739c0ae1bde8342acca84e3b261da276ac6f57ee | quote: "error": "timeout"
- sources:
  - [1] https://t.me/WangPanBOT
  - [2] https://t.me/bot_zh
  - [3] https://t.me/bot_zh/
