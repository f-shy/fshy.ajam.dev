# TgDL.eu.org

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-opdlbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-opdlbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TgDL.eu.org (@OpDLBot)

- `debrid/telegram-opdl-bot` | dead | evidence documented | binding per-object-cap | category hosted bot (Telegram file to permanent link) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:47.479Z (live) | stale on 2026-12-26
- url https://t.me/OpDLBot
- free tier: Free, no account: 'The ultimate Bot for permanent Links to Telegram Files.' paired with a companion channel @OpenFileZ. No quota is published. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: Not published. Telegram's 2 GB per object is the only ceiling in evidence. | source: [2]
- retention: 'permanent Links' is the claim; no expiry is stated and none was tested. | source: [1] | note: 'permanent' is the operator's word, not a measured lifetime
- egress: Free HTTP links over the operator's session; no byte allowance is stated. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account to message the bot; no key or email.
- interface: rest
- limits:
  - per-object-cap (binding): 2 GB, Telegram's own object ceiling; the bot states none [2]
- binding note: Nothing tighter is published; the operator's rate limiting is unknown, so the platform ceiling is the only defensible binding.
- interface detail: A Telegram chat plus a link domain (tgdl.eu.org) named in the bot's title.
- tooling: Any Telegram client; the output is a URL.
- composes with: Parks a Telegram object behind a stable HTTP name, which is the only way a 2 GB file becomes fetchable by curl without a bot token.
- reliability: A single-operator service whose permanence claim is untested; the domain in the title is the single point of failure.
- notes: Grouped with @FileToLinkTGbot as a class: free file-to-URL bots that exist to defeat the 20 MB getFile cap. Abandon the pair together if either stops resolving, and prefer whichever states a real quota.
- evidence note: Description read. Whether a link survives a week is unverified.
- extras:
  - death.on: 2026-11-25
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-23: 'The ultimate Bot for permanent Links to Telegram Files.' and the @OpenFileZ companion
  - [1] 2026-11-25: the bot's own page still claims permanent links and names the @OpenFileZ companion | capture: sha256:98f1a15079d1b74fca52162e41171c5ff956f6d6f29d65272baa9711933405ce | quote: The ultimate Bot for permanent Links to Telegram Files.
  - probe:https://web.archive.org/web/20230110003344/https://tgdl.eu.org/ 2026-11-25: the archived tgdl.eu.org status page names the @OpDLBot bot, so the domain was this record's link-serving host | capture: sha256:05684d6dd59347b462a84a18a4be7647b53e9bd606819d238044b3072ed3ce81 | quote: "telegram_bot": "@OpDLBot"
  - probe:https://tgdl.eu.org 2026-11-25: a direct probe of the link host tgdl.eu.org failed DNS | capture: sha256:cc5f48309a5311ff3b4a89dca4e021044acd6ea1e9d2b4563ca13a179f82dd70 | quote: "error": "dns"
- sources:
  - [1] https://t.me/OpDLBot
  - [2] https://telegram.org/faq
