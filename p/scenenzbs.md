# SceneNZBs

> scenenzbs.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scenenzbs/ | JSON https://fshy.ajam.dev/api/v1/entity/scenenzbs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SceneNZBs

- `debrid/scenenzbs` | dead | evidence measured | binding write-gated | category Usenet indexer (renamed) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://scenenzbs.com/
- free tier: None under this name: every request is redirected to a mover notice, 'SceneNZBs is now called Treasure Maps. You can find us at our new address.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable: the name no longer serves an index | source: [1]
- egress: none: the name serves a one-paragraph notice | metered: no | source: [1]
- identity: email | detail: Accounts were carried across: 'Your access still works' on the successor site.
- interface: rest
- limits:
  - write-gated (binding): the name is retired: every path lands on the mover notice probe:https://scenenzbs.com/
- binding note: The name itself is the constraint: no query reaches an index. The successor record carries the live limits.
- interface detail: The host answers HTML only; there is no API under this domain any more.
- endpoint: https://scenenzbs.com/
- tooling: An existing Prowlarr or NZBHydra2 entry pointed at scenenzbs.com still resolves, so the old host stays configured and the index is silently lost; the fix is to edit the URL to treasure-maps.com.
- composes with: Retired in favour of treasure-maps.com; nothing else.
- reliability: A rename with no redirect of the API path: an automation client pointed at the old host fails at search time, not at config time.
- notes: Inactive indexer domain redirecting to successor service NZB-Life.
- evidence note: The notice was fetched and the final URL recorded. That the successor is Treasure Maps is the vendor's own sentence.
- extras:
  - price: moved
  - successor: treasure-maps
- evidence:
  - probe:https://scenenzbs.com/ 2026-10-23: 200, final URL https://scenenzbs.com/scenenzbs-moved.html, 45 words: 'We have moved! SceneNZBs is now called Treasure Maps. You can find us at our new address.' with a link to treasure-maps.com
  - [2] 2026-10-23: the successor confirms: 'SceneNZBs now sails under a new flag - Treasure Maps. Your access still works.'
- sources:
  - [1] https://scenenzbs.com/
  - [2] https://treasure-maps.com/
