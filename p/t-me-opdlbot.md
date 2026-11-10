# TgDL.eu.org

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-opdlbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-opdlbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TgDL.eu.org (@OpDLBot)

- `debrid/telegram-opdl-bot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (Telegram file to permanent link) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
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
- evidence:
  - [1] 2026-10-23: 'The ultimate Bot for permanent Links to Telegram Files.' and the @OpenFileZ companion
- sources:
  - [1] https://t.me/OpDLBot
  - [2] https://telegram.org/faq
