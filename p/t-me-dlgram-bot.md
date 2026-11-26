# Files To Links Fast

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-dlgram-bot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-dlgram-bot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Files To Links Fast (@dlgram_bot)

- `debrid/telegram-dlgram-bot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (Telegram file to link, open source) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:47.479Z (live) | stale on 2026-12-26
- url https://t.me/dlgram_bot
- free tier: Free, no account: 'Files To Links Fast', with its implementation published at github.com/musa-42/streamer_file. No quota is stated. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: Not published. Telegram's 2 GB per object is the only documented ceiling. | source: [2]
- retention: Not stated. The file remains in its chat; the link's lifetime is the operator's. | source: [1]
- egress: Free HTTP links; no allowance stated. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account; no bot token needed to use the hosted instance.
- interface: rest
- limits:
  - per-object-cap (binding): 2 GB, Telegram's own object ceiling; the bot states none [2]
- binding note: Same reasoning as the other file-to-link bots: no published quota, and the platform ceiling is the only documented wall.
- interface detail: A Telegram chat; the source is public, so the bot can also be run locally instead of used hosted.
- tooling: Hosted bot today; the linked repository makes a self-run copy possible on a free VM.
- composes with: The only member of the file-to-URL class with public source, so a hosted outage has a fallback: run the same code on a free compute tier.
- reliability: Hosted by one operator; the public repository is the mitigation, not a guarantee that the hosted instance matches it.
- notes: Abandon if the repository is deleted or the bot stops resolving. This is the one record in the class where the fallback is verifiable, so it is the one to test first.
- evidence note: The description and the repository link are on the bot's page read. The repository's own limits were not read line by line.
- evidence:
  - [1] 2026-10-23: 'Files To Links Fast' with 'https://github.com/musa-42/streamer_file' in the description
  - [1] 2026-11-25: the bot's own page still links the public source repository | capture: sha256:e2c0ef9d106f558a53f0f4feaaec2635eb208ef98ce3ccad4f9822c98aac2a15 | quote: https://github.com/musa-42/streamer_file
  - [2] 2026-11-25: Telegram login uses a mobile phone number | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63
  - [2] 2026-11-25:  | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63 | quote: Send and receive files of any type, up to 2 GB in size each (or 4 GB with
- sources:
  - [1] https://t.me/dlgram_bot
  - [2] https://telegram.org/faq
