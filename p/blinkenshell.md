# Blinkenshell

> blinkenshell.org | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blinkenshell/ | JSON https://fshy.ajam.dev/api/v1/entity/blinkenshell.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blinkenshell

- `compute/blinkenshell` | fails-identity | evidence documented | binding write-gated | category shared shell | tier Free account
- needs card no, phone yes, ID no, institution no | verified 2026-10-24T01:56:00.000Z (live) | stale on 2026-11-24
- url https://blinkenshell.org/docs/signup-process/
- free tier: 100 MB disk quota, 128 MB memory limit, SSH and SFTP, detached screen or tmux; listening on a custom TCP or UDP port is a supporter-only feature | unit: MB | metered on: stored-bytes | read on: 2026-10-24 | source: [1] | note: the free column of the account table marks 'Listen TCP/UDP port (custom server)' blank and supporter-only
- per-object cap: not applicable
- retention: no expiry is published for an active account; the signup process warns that you are expected to visit the IRC channel once in a while after you get your account | source: [2] | note: activity is policed by the community rather than by a published purge rule
- egress: not published on the pages read | metered: no
- identity: any-phone | detail: five steps, and step five is 'IRL Verification. Enter your personal cell/mobile phone number to receive an SMS with a verification code.' Before that: email verification, a 20-question quiz, an IRC NickServ registration, and two existing users must vouch for you, which cannot happen within one hour of creating the signup account. No card.
- interface: rest, cli
- limits:
  - volume-quota: 100 MB disk quota on the free account [1]
  - request-rate: 128 MB memory limit per free account [1]
  - write-gated (binding): listening on a TCP or UDP port requires a supporter account from EUR 3 a month [1]
- limits note: the port-22 assumption is what hid this class: the host answers on 2222
- binding note: the port allowance is the feature that would make it a machine, and it is behind the paid tier; the disk quota is secondary.
- interface detail: SSH on port 2222
- tooling: SSH, screen or tmux, 2 background processes
- composes with: a screen host with no inbound port and a 128 MB memory ceiling
- reliability: no reliability event recorded
- notes: The cleanest rejection in evaluated offerings: a mobile number and two human vouches, for 100 MB. A supporter account at EUR 3 a month skips the queue but still requires the SMS step, per the same page.
- evidence note: all five steps and the account table are quoted from Blinkenshell's own pages read.
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: blinkenshell.org
  - port: 2222
  - ms: 16194
  - ok: no
  - note: the saved run this record cites: a timeout on both ports
- extras:
  - shape.disk_gib: 100
  - billing_model: free
  - session_cap.restart_required: no
  - session_cap.note: no session cap published; detach with screen or tmux is allowed
  - keep_rate.value: 0.0
  - keep_rate.basis: a free account costs nothing
  - keep_rate.source: https://blinkenshell.org/
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: home directory
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while active
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: supporter only
  - network_out.ipv6: yes
  - free_tier_kind: always-free
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - probe_result: port 2222 timed out twice
  - shape_note: 100 MB and a 128 MB memory limit, both in the vendor's MB
  - term: indefinite while active
  - price_arithmetic: no charge for the free account; supporter is from EUR 3 a month
- evidence:
  - probe:blinkenshell.org:2222 2026-10-22: TCP connect to port 2222 timed out at 16.4 s and again at 30 s from this host, so reachability is not established from here
  - [3] 2026-10-06: the Free column caps memory at 128 MB, processes at 100, SSH sessions at 6 and background processes at 2
  - [2] 2026-10-24: quoted: '5. IRL Verification. Enter your personal cell/mobile phone number to receive an SMS with a verification code.'
  - [2] 2026-10-24: quoted: '4. Get two registered users to vouch (approve) you.' and 'It will take atleast 1 hour before your free account can be activated.'
  - [1] 2026-10-24: quoted: 'Disk Quota 100 MB', 'Memory limit 128 MB', and 'Listen TCP/UDP port (custom server)' checked only in the Supporter column
- sources:
  - [1] https://blinkenshell.org/
  - [2] https://blinkenshell.org/docs/signup-process/
  - [3] https://blinkenshell.org/docs/resource-limits/

## blinkenshell / sdf / free shell accounts (the 'tilde' route)

- `storage/blinkenshell-sdf-free-shell-accounts` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://blinkenshell.org/
- free tier: none reachable: Free SSH shell accounts exist and are charming, but the disk is 100 MB (Blinkenshell 'Disk Quota 100 MB', x4 on Supporter at EUR 3/mo). SDF's MetaARPA tier gives '20GB OS images' but… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Free SSH shell accounts exist and are charming, but the disk is 100 MB (Blinkenshell 'Disk Quota 100 MB', x4 on Supporter at EUR 3/mo). SDF's MetaARPA tier gives '20GB OS images' but…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free SSH shell accounts exist and are charming, but the disk is 100 MB (Blinkenshell 'Disk Quota 100 MB', x4 on Supporter at EUR 3/mo). SDF's MetaARPA tier gives '20GB OS images' but…
  - [2] 2026-10-21: cited as the basis of the rejection: Free SSH shell accounts exist and are charming, but the disk is 100 MB (Blinkenshell 'Disk Quota 100 MB', x4 on Supporter at EUR 3/mo). SDF's MetaARPA tier gives '20GB OS images' but require
- sources:
  - [1] https://blinkenshell.org/
  - [2] https://sdf.org/?join
