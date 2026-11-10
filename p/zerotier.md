# ZeroTier

> zerotier.com | Egress and tunnels, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zerotier/ | JSON https://fshy.ajam.dev/api/v1/entity/zerotier.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZeroTier

- `egress/zerotier-free` | qualifies-with-caveat | evidence documented | binding request-rate | category mesh network
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.zerotier.com/pricing/
- free tier: 10 devices, 1 network, 1 administrator | unit: users | metered on: identity-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable | source: [1]
- egress: signalling; peer-to-peer once connected, with a relay fallback whose rate is not published | metered: no | source: [1]
- identity: email | detail: a ZeroTier account
- interface: cli
- limits note: counts of things, not rates, so no vocabulary kind names them: 10 devices on the free plan
- interface detail: zerotier-cli join
- tooling: zerotier-one
- composes with: signalling for a small private mesh; it composes with a private set of devices and carries no bytes once they connect.
- reliability: the free plan caps devices, not bytes
- notes: 2026-10-23: no public ingress, in the vendor's own words. The hosting guide says ZeroTier 'enables private networking between devices, allowing you to host a website locally and serve it securely to peers on the same ZeroTier network'. Its UDP 9993 listener is for peer transport, not for a reader, so the free plan's cap on devices is the only meter and there is no 1 TiB/month to spend.
- extras:
  - stale_after_days: 180
  - bytes_transit: conditional
  - transit_note: peer-to-peer once connected, with a relay fallback at an unpublished rate
- evidence:
  - [1] 2026-10-22: 10 devices, 1 network and 1 admin on the free plan
  - [2] 2026-10-23: 'ZeroTier enables private networking between devices, allowing you to host a website locally and serve it securely to peers on the same ZeroTier network.'
- sources:
  - [1] https://www.zerotier.com/pricing/
  - [2] https://docs.zerotier.com/website/

## ZeroTier free (Personal)

- `storage/zerotier-free` | fails-quota | evidence reported | binding none | category mesh-control-plane
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.zerotier.com/llms-full.txt
- free tier: 10 devices, 1 network. Vendor table effective 20 Oct 2026: 'Personal | Free | 10 | Not available'. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free, peer-to-peer; relaying only when the path fails. | metered: no
- identity: email | detail: email
- interface: rest, cli
- limits note: device count, not bandwidth. Data flows peer-to-peer so there is no byte meter.
- interface detail: virtual L2/L3 overlay, REST API, Terraform provider, CLI.
- tooling: zerotier-one agent; central controller is now separately licensed (the default `make` build no longer includes it).
- composes with: 10 devices is workable as a private mesh but not as a shard farm, and the controller is no longer in the open-source build by default.
- reliability: Free tier has been cut twice (50 -> 25 -> 10 devices). Docs at docs.zerotier.com/start/ still say 'up to 25 devices' while the vendor's own llms-full.txt says 10. Trust the vendor table, not the docs page.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 devices, 1 network. Vendor table effective 20 Oct 2026: 'Personal | Free | 10 | Not available'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Prices below are in USD, billed monthly, effective 20 October 2026... | Personal | Free | 10 | Not available'
  - [2] 2026-10-21: 'ZeroTier Central is free for personal and small business use (up to 25 devices across all networks)' — CONTRADICTS the vendor table; the docs page is stale
  - [3] 2026-10-21: 'The default `make` build no longer includes the controller'
  - [4] 2026-10-21: historic '25 Nodes' basic tier
- sources:
  - [1] https://www.zerotier.com/llms-full.txt
  - [2] https://docs.zerotier.com/start/
  - [3] https://www.hivebook.wiki/wiki/zerotier-global-peer-to-peer-virtual-ethernet-over-curve25519
  - [4] https://web.archive.org/web/20230401122634/https:/www.zerotier.com/pricing/

## zerotier free as a storage mesh

- `storage/zerotier-free-as-a-storage-mesh` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.zerotier.com/llms-full.txt
- free tier: none reachable: Cut to 10 devices / 1 network, non-commercial, and the self-hostable controller was removed from the default open-source build. Cannot host a shard farm. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- self hosted: no
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Cut to 10 devices / 1 network, non-commercial, and the self-hostable controller was removed from the default open-source build. Cannot host a shard farm.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cut to 10 devices / 1 network, non-commercial, and the self-hostable controller was removed from the default open-source build. Cannot host a shard farm.
  - [2] 2026-10-21: cited as the basis of the rejection: Cut to 10 devices / 1 network, non-commercial, and the self-hostable controller was removed from the default open-source build. Cannot host a shard farm.
- sources:
  - [1] https://www.zerotier.com/llms-full.txt
  - [2] https://www.hivebook.wiki/wiki/zerotier-global-peer-to-peer-virtual-ethernet-over-curve25519
