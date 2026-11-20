# torrent magnet leecher

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-torgetbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-torgetbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## torrent magnet leecher (@torgetbot)

- `debrid/telegram-torget-bot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (magnet to Telegram file) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
- url https://t.me/torgetbot
- free tier: 'torgetbot is magnet leecher telegram bot . user can be search from piratebay , Limetorrents & 1337X.' Free, with no quota on the page. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: Not published. Telegram's 2 GB free-account ceiling is the only documented wall. | source: [2]
- retention: Delivered into the requesting chat; no storage window is stated. | source: [1]
- egress: Free; the operator's host does the swarm traffic and the upload. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account; no key.
- interface: rest
- limits:
  - per-object-cap (binding): 2 GB, Telegram's own ceiling; the bot states none [2]
- binding note: No other published limit; the platform object ceiling is the only constraint that can be named from evidence.
- interface detail: A Telegram chat with a built-in search over three public trackers.
- tooling: Any Telegram client.
- composes with: Search and leech in one chat: a magnet found by name becomes a Telegram file without a client, a VPN or a seedbox.
- reliability: An anonymous single-operator bot with no channel, no status page and no published capacity; a silent death is the expected failure mode.
- notes: Abandon if the page stops resolving. Documented as the minimal example of the class: no channel, no docs, no quota, and therefore nothing to hold the vendor to.
- evidence note: Description read. Capacity and liveness of the backend are unverified: a Start action proves the account exists, not that it answers.
- evidence:
  - [1] 2026-10-23: 'torgetbot is magnet leecher telegram bot . user can be search from piratebay , Limetorrents & 1337X.'
- sources:
  - [1] https://t.me/torgetbot
  - [2] https://telegram.org/faq
