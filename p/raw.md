# fars.ee

> raw.githubusercontent.com | Compute, Storage; 6 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/raw/ | JSON https://fshy.ajam.dev/api/v1/entity/raw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hashbang

- `compute/hashbang` | qualifies-with-caveat | evidence documented | binding retention-clamped | category shared shell
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://raw.githubusercontent.com/hashbang/shell-etc/master/cron.daily/clean-lurkers
- free tier: a free shared shell account; per-user limits applied at login are 512 MB memory, 50% CPU quota and a soft 150 process cap | unit: none | metered on: none | read on: 2026-10-06 | source: [1] | note: the limits live in the operator's deployed configuration, not on a marketing page
- per-object cap: not applicable
- retention: a daily sweep terminates sessions for any user with no SSH login in 30 days unless ~/.keep-account exists | days: 30 | note: the sweep keys off lastlog, so a detached tmux does not keep it alive
- egress: not published | metered: no | source: [2]
- identity: email | detail: an account with a registered SSH key; no card
- interface: rest, cli
- limits:
  - retention-clamped (binding): sessions terminated after 30 days with no SSH login unless ~/.keep-account exists [1]
  - request-rate: 512 MB memory, 50% CPU quota, soft 150 and hard 200 processes per user at login
  - write-gated: an SSH public key must be registered with the provisioning API [2]
- limits note: LXC containers on Atlantic.net; the live node recorded by historical research records was de1.hashbang.sh in Nuremberg with maxusers 6175.
- binding note: the 30-day login sweep binds first, with a one-file opt-out
- interface detail: SSH on port 22; an SSH public key is registered with the provisioning API
- tooling: SSH, screen or tmux, cron
- composes with: a keepalive file is the cheapest way past the sweep, and it costs one touch
- reliability: no reliability event recorded
- notes: Account retention is enforced via scheduled cleanup routines.
- evidence note: reachability only: a probe proves the port answers, not the quota, so the per-user limits carry the documented rung and the record is not `measured`
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: hashbang.sh
  - port: 22
  - ms: 350
  - ok: yes
  - peer: 174.138.102.152
- extras:
  - shape.ram_gib: 0.5
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: 30-day login sweep; no session cap
  - keep_rate.value: 0.0
  - keep_rate.basis: a free account costs nothing
  - keep_rate.source: https://hashbang.sh
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: home directory
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: 30 days without a login unless opted out
  - network_out.allow_outbound: yes
  - network_out.static_ip: no
  - free_tier_kind: allowance
  - m10h_usd: 0.0
  - m24h_usd: 0.0
- evidence:
  - probe:hashbang.sh:22 2026-10-22: TCP connect succeeded in 0.35 s to 174.138.102.152; the host accepted the connection and sent no banner within 6 s
  - [1] 2026-10-22: the daily clean-lurkers script sets DAYS=30 and runs lastlog -b 30 -t 32 to terminate users with no login in 30 days
- sources:
  - [1] https://raw.githubusercontent.com/hashbang/shell-etc/master/cron.daily/clean-lurkers
  - [2] https://hashbang.sh

## arch user repository (aur)

- `storage/arch-user-repository` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://raw.githubusercontent.com/archlinux/aurweb/master/conf/config.defaults
- free tier: none reachable: Git only, PKGBUILDs and small aux files; hard 256,000-byte (250 KiB) per-blob limit enforced in aurweb's git hook. No binaries at all. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Git only, PKGBUILDs and small aux files; hard 256,000-byte (250 KiB) per-blob limit enforced in aurweb's git hook. No binaries at all.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Git only, PKGBUILDs and small aux files; hard 256,000-byte (250 KiB) per-blob limit enforced in aurweb's git hook. No binaries at all.
  - [2] 2026-10-21: cited as the basis of the rejection: Git only, PKGBUILDs and small aux files; hard 256,000-byte (250 KiB) per-blob limit enforced in aurweb's git hook. No binaries at all.
- sources:
  - [1] https://raw.githubusercontent.com/archlinux/aurweb/master/conf/config.defaults
  - [2] https://wiki.archlinux.org/title/AUR_submission_guidelines

## farcaster as a file store

- `storage/farcaster-as-a-file-store` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://raw.githubusercontent.com/farcasterxyz/protocol/main/docs/SPECIFICATION.md
- free tier: none reachable: Fails on first principles, not on a URL: the protocol stores no media. A cast embed is a URL to somebody else's host, and message acceptance is gated on rented storage units bought on… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Fails on first principles, not on a URL: the protocol stores no media. A cast embed is a URL to somebody else's host, and message acceptance is gated on rented storage units bought on…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Fails on first principles, not on a URL: the protocol stores no media. A cast embed is a URL to somebody else's host, and message acceptance is gated on rented storage units bought on…
- sources:
  - [1] https://raw.githubusercontent.com/farcasterxyz/protocol/main/docs/SPECIFICATION.md

## fars.ee (listed as a file host in the free-s3 research.md '0x0 family')

- `storage/fars-ee` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://raw.githubusercontent.com/hoangvu12/free-s3/master/RESEARCH.md
- free tier: None reachable: Not a file host at all. It is a `ptpb/pb` text pastebin and warns 'do NOT post large files'. A useful warning about the catalog itself: one of its 19 rows is wrong, so verify each row befor. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Not a file host at all — it is a `ptpb/pb` text pastebin and warns 'do NOT post large files'. A useful warning about the catalog itself: one of its 19 rows is wrong, so verify each row…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Not a file host at all — it is a `ptpb/pb` text pastebin and warns 'do NOT post large files'. A useful warning about the catalog itself: one of its 19 rows is wrong, so verify each row…
- sources:
  - [1] https://raw.githubusercontent.com/hoangvu12/free-s3/master/RESEARCH.md

## nostr relays as a byte store (including base64-in-event tricks)

- `storage/nostr-relays-as-a-byte-store` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://raw.githubusercontent.com/nostr-protocol/nips/master/94.md
- free tier: none reachable: NIP-94 is metadata only, and the relay event size ceiling (~64 KB) caps any inline payload at roughly 48 KB after base64 expansion. Chainable as an index for Blossom, worthless as storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: not-storage
  - dead_end.why: NIP-94 is metadata only, and the relay event size ceiling (~64 KB) caps any inline payload at roughly 48 KB after base64 expansion. Chainable as an index for Blossom, worthless as storage.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: NIP-94 is metadata only, and the relay event size ceiling (~64 KB) caps any inline payload at roughly 48 KB after base64 expansion. Chainable as an index for Blossom, worthless as storage.
- sources:
  - [1] https://raw.githubusercontent.com/nostr-protocol/nips/master/94.md

## tableland

- `storage/tableland-see-candidate-entry` | fails-quota | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:43.357Z (live) | stale on 2026-12-05
- url https://raw.githubusercontent.com/tablelandnetwork/docs/main/docs/fundamentals/limits.md
- free tier: No file storage: limits are 500000 rows and 24 columns per table and 1kb per cell (open-beta limits), about 12 GB of cell data per table at most; the docs say to store pointers to IPFS, Filecoin or Arweave instead. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Reads go through an unauthenticated REST call to a gateway; no meter is stated. | metered: no
- identity: email | detail: unverified: no sign-up page was read; writes are onchain operations, so a wallet on a supported chain is needed.
- interface: unknown
- limits:
  - volume-quota (binding): 500000 rows and 24 columns per table [1]
  - per-object-cap: 1kb per cell [1]
- limits note: Mutating queries are onchain operations paying the chain's gas; query size is limited to 35kb (14.5kb on Ethereum mainnet).
- binding note: about 12 GB of cell data per table at most, far below 500 GB.
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: tableland.xyz and docs.tableland.xyz redirect (HTTP 302) to the Recall Labs wind-down notice of 2026-10-30 on 2026-11-03; the notice names the Recall Network, not Tableland, so the service status is unverified.
- notes: 500k rows / 24 columns per table. Their own docs tell you to put large media on IPFS and store the CID. A pointer store cannot hold 500 GB.
- evidence note: re-read on 2026-11-03: the vendor docs limits page https://raw.githubusercontent.com/tablelandnetwork/docs/main/docs/fundamentals/limits.md (row, column and cell limits, unauthenticated REST reads, not a file storage solution) and the Recall Labs wind-down post on x.com (RecallLabs_) that tableland.xyz and docs.tableland.xyz redirect to; identity and service status are unverified
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 500k rows / 24 columns per table. Their own docs tell you to put large media on IPFS and store the CID. A pointer store cannot hold 500 GB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 500k rows / 24 columns per table. Their own docs tell you to put large media on IPFS and store the CID. A pointer store cannot hold 500 GB.
  - [1] 2026-11-03: a table is limited to 500000 rows | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: | Rows | 500000 |
  - [1] 2026-11-03: each cell holds 1 kb | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: Each cell limit is 1kb.
  - [1] 2026-11-03: the query size limit | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: Query size is limited to a maximum of 35kb.
  - [1] 2026-11-03: reads are unauthenticated REST calls | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: All table reads must happen through an offchain interaction using an unauthenticated REST API call to a Tableland validator node's gateway.
  - [1] 2026-11-03: the docs describe pointer storage, not file storage | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: Tableland is _not a file storage_ solution. Instead, use pointers to solutions like IPFS, Filecoin, & Arweave to enable large file integrations and store the pointers in table cells.
  - probe:docs.tableland.xyz 2026-11-03: the docs page ends on the Recall Labs notice | capture: sha256:4a9a6d32ff4dd317073b922d0b4b4ce90155a3cf5b94edef5b161be47f6ae018 | quote: "final_url": "https://x.com/RecallLabs_/status/2116235386582426069"
  - [2] 2026-11-03: the notice that the Tableland domains redirect to | capture: sha256:2194fd0ed6b74b82e6205c1576bc1797cf7e824f89c2ca393cfc4cd8758fac58 | quote: We’ve made the decision to wind down Recall Labs.
  - [1] 2026-11-04: the vendor docs state the network is not file storage | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: Tableland is _not a file storage_ solution.
- sources:
  - [1] https://raw.githubusercontent.com/tablelandnetwork/docs/main/docs/fundamentals/limits.md
  - [2] https://x.com/RecallLabs_/status/2116235386582426069
