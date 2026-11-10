# Nintendo Switch

> nintendo.com | Netdisk and pan, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nintendo/ | JSON https://fshy.ajam.dev/api/v1/entity/nintendo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nintendo Switch Online Save Data Cloud (Netdisk and pan)

- `netdisk-pan/nintendo-switch-online-save-data-cloud` | fails-quota | evidence reported | binding per-object-cap | category console cloud saves
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:20:56.364Z (inherited) | stale on 2026-11-19
- url https://support.nintendo.com/sg/nso/services/savedata-backup/index.html
- free tier: No pool at all: one save slot per supported game title. A personal subscription covers one account and a family plan covers eight | unit: none | metered on: object-count | read on: 2026-10-21 | source: [1]
- per-object cap: One save data file per software title for each Nintendo Account. There is no aggregate cap and no way to store non-save bytes | source: [1]
- retention: Backed-up saves are not usable once the subscription ends, and are accessible again if the subscription is renewed within 180 days | days: 180 | source: [1]
- egress: Console-mediated only. There is no HTTP API, so there is no egress path at all | metered: no | source: [1]
- identity: email | detail: a Nintendo Account and a paid subscription
- interface: unknown
- limits:
  - per-object-cap (binding): one save file per supported title per account [1]
  - write-gated: an active Nintendo Switch Online membership is required, and the only client is the console [2]
- binding note: The advertised absence of a storage limit is bound to one save file per title, so the per-object cap is the whole quota. There is no pool to measure.
- tooling: none public. The switch's own backup menu is the only client
- composes with: Nothing to multiply: there is no capacity number to shard, and the practical ceiling is titles owned times per-title save size, which is tens of gigabytes at most
- reliability: Multiple games are excluded from backup entirely, and saves are not usable once the subscription lapses (accessible again on renewal within 180 days). The console is the only client, so there is no programmatic read or write path
- notes: Documentation advertises 'no limit to the amount of storage space' alongside 'one save data file per software title'. Access is restricted strictly to console hardware with no web, mobile, or programmatic API endpoints.
- extras:
  - access_mode: registration-gated
  - api: none, console only
  - aliases: Nintendo Switch Online Save Data Cloud
  - cross_topic_record: storage/nintendo-switch-online-save-data-cloud
  - cross_topic_note: the storage topic carries the same provider from the game-save angle; this record is scoped to whether it is a pan
- evidence:
  - [1] 2026-10-21: 'You can only back up one save data file per software title for each Nintendo Account' and 'There is no limit to the amount of storage space or number of software titles that can be backed up'
  - [2] 2026-10-21: backup requires an active Nintendo Switch Online membership
  - [3] 2026-10-21: 'Nintendo Switch Online: title-by-title, not a storage pool'
  - [1] 2026-11-03: after the subscription ends the backed-up saves are not usable; renewing within 180 days restores access | capture: sha256:187249e4267aaa57beeb14f7abeed1dc3bb55360e25495ee3ac0f07495c388fb | quote: if you re-subscribe within 180 days, you will be able to access the save data that was backed up during your previous subscription period.
  - [1] 2026-11-03: one save data file per title per account | capture: sha256:187249e4267aaa57beeb14f7abeed1dc3bb55360e25495ee3ac0f07495c388fb | quote: You can only back up one save data file per software title for each Nintendo Account.
  - [1] 2026-11-03: no aggregate storage limit is stated | capture: sha256:187249e4267aaa57beeb14f7abeed1dc3bb55360e25495ee3ac0f07495c388fb | quote: There is no limit to the amount of storage space or number of software titles that can be backed up.
  - [1] 2026-11-03: backup needs a Nintendo Switch Online subscription | capture: sha256:187249e4267aaa57beeb14f7abeed1dc3bb55360e25495ee3ac0f07495c388fb | quote: Only users (Nintendo Accounts) that have a subscription to Nintendo Switch Online can back up save data.
  - [2] 2026-11-03: a family membership covers up to 8 people | capture: sha256:5695a6c83bf751dccb384daca7e4d7d50d2545f3933bf69aac398e14c60cd5ea | quote: A family membership provides the Nintendo Switch Online service to everyone in the purchaser's Nintendo Account family group (up to 8 people).
- sources:
  - [1] https://support.nintendo.com/sg/nso/services/savedata-backup/index.html
  - [2] https://www.nintendo.com/en-gb/Support/Nintendo-Account/Nintendo-Switch-Online-FAQ-1442566.html
  - [3] https://tech-insider.org/cloud-save-storage-ps-plus-xbox-steam-switch-2026/

## nintendo switch online save data cloud (Storage)

- `storage/nintendo-switch-online-save-data-cloud` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://support.nintendo.com/sg/nso/services/savedata-backup/index.html
- free tier: none reachable: Advertises 'no limit to the amount of storage space' but binds it to 'only one save data file per software title for each Nintendo Account', and the only client is the console. No HTTP API, | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Advertises 'no limit to the amount of storage space' but binds it to 'only one save data file per software title for each Nintendo Account', and the only client is the console. No HTTP API,
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Advertises 'no limit to the amount of storage space' but binds it to 'only one save data file per software title for each Nintendo Account', and the only client is the console. No HTTP API
- sources:
  - [1] https://support.nintendo.com/sg/nso/services/savedata-backup/index.html
