# freifunk

> freifunk.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freifunk/ | JSON https://fshy.ajam.dev/api/v1/entity/freifunk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## freifunk (as a storage provider)

- `storage/freifunk` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:31.557Z (live) | stale on 2026-11-18
- url https://freifunk.net/en/
- free tier: No storage allowance is published on the pages read: the initiative is a set of community wireless networks in which participants provide routers for data transfer, not a storage service | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- binding note: no storage allowance exists to measure: the offering is network access between participants, not capacity
- interface detail: not documented
- tooling: no hosted storage offer; the user installs and runs the Freifunk firmware (a Linux distribution) on a WLAN router
- composes with: not recorded
- reliability: Non-commercial community wireless networks; services on them are set up by individual participants, so no central capacity or quota exists to measure
- notes: the same as reliability
- evidence note: the 2026-11-03 read covered https://freifunk.net/en/what-is-it-about/, which describes a non-commercial wireless network initiative and no storage service; the absence of a storage offer is read from that page and is not a stated vendor claim
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: A federated set of German community WiFi projects whose stated purpose is free communication and open routers. No storage service, no quota, no API - the contribution model is 'make your…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: A federated set of German community WiFi projects whose stated purpose is free communication and open routers. No storage service, no quota, no API - the contribution model is 'make your…
  - [2] 2026-11-03: the offering is network transfer between participants, with no storage service described | capture: sha256:913b07ea87e768f49a07a105639bbaf70c6ecd31f7c72ec0f5865d73806c819d | quote: Every user in the free wireless network provides his or her wireless LAN router for data transfer to other participants.
  - [2] 2026-11-03: the initiative is a wireless networking project | capture: sha256:913b07ea87e768f49a07a105639bbaf70c6ecd31f7c72ec0f5865d73806c819d | quote: freifunk is a non-commercial initiative for free wireless networks.
  - [2] 2026-11-03: participation is by running Freifunk firmware on a router | capture: sha256:913b07ea87e768f49a07a105639bbaf70c6ecd31f7c72ec0f5865d73806c819d | quote: We use our own freifunk firmware a special Linux distribution, on our WLAN routers.
  - [2] 2026-11-03: the offering is network transfer between participants | capture: sha256:913b07ea87e768f49a07a105639bbaf70c6ecd31f7c72ec0f5865d73806c819d | quote: Every user in the free wireless network provides his or her wireless LAN router for data transfer to other participants.
- sources:
  - [1] https://freifunk.net/en/
  - [2] https://freifunk.net/en/what-is-it-about/
