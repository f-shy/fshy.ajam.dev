# Blinkenshell

> blinkenshell.org | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blinkenshell/ | JSON https://fshy.ajam.dev/api/v1/entity/blinkenshell.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blinkenshell

- `compute/blinkenshell` | fails-identity | evidence documented | binding write-gated | category shared shell | tier Free account
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T11:17:45.491Z (live) | stale on 2026-12-26
- url https://blinkenshell.org/docs/signup-process/
- free tier: a free account with SSH & SFTP access, a 100 MB disk quota, 128 MB memory limit and detached GNU Screen or tmux, with a Free! monthly price; listening on a custom TCP/UDP port is supporter-only, from EUR 3 a month | unit: MB | metered on: stored-bytes | read on: 2026-10-24 | source: [1] | note: the free column of the account table marks 'Listen TCP/UDP port (custom server)' blank and supporter-only
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
  - [1] 2026-11-25: the Free column of the account table lists SSH & SFTP, a 100 MB disk quota, a 128 MB memory limit, detach and a Free! monthly price, and leaves the custom TCP/UDP port to the supporter column at From 3€/mo | capture: sha256:1431416826ac3e23ee1580e17364225936bfc8b0b0046cf305e53a4639a7b404 | quote: | SSH & SFTP Access | ✔ | ✔ | | [Disk Quota](https://blinkenshell.org/docs/disk-quota) | 100 MB[(x4~)](https://blinkenshell.org/docs/disk-quota) | 1000 MB [(x4~)](https://blinkenshell.org/docs/disk-quota) | | [Memory limit](https://blinkenshell.org/docs/resource-limits) | 128 MB | 256 MB | | Detach (GNU Screen, tmux) | ✔ | ✔ | | Listen TCP/UDP port (custom server) | | ✔ | | Monthly Price | Free! | [From 3€/mo](https://blinkenshell.org/docs/supporter) |
- sources:
  - [1] https://blinkenshell.org/
  - [2] https://blinkenshell.org/docs/signup-process/
  - [3] https://blinkenshell.org/docs/resource-limits/

## blinkenshell / sdf / free shell accounts (the 'tilde' route)

- `storage/blinkenshell-sdf-free-shell-accounts` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:57.622Z (live) | stale on 2026-12-04
- url https://blinkenshell.org/
- free tier: none reachable: Free SSH shell accounts exist and are charming, but the disk is 100 MB (Blinkenshell 'Disk Quota 100 MB', x4 on Supporter at EUR 3/mo). SDF's MetaARPA tier gives '20GB OS images' but… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on the Blinkenshell or SDF pages | source: [1] | note: not stated on the Blinkenshell or SDF pages
- retention: not stated on the Blinkenshell or SDF pages | source: [1] | note: not stated on the Blinkenshell or SDF pages
- egress: not stated on the Blinkenshell or SDF pages | metered: no
- identity: email
- interface: ssh, sftp, browser
- interface detail: SSH and SFTP shell accounts with static HTTPS web hosting
- tooling: SSH and SFTP clients; inbound ssh, ftp and sftp connections on SDF
- composes with: files live in a shell account home directory and are served over SSH/SFTP and static HTTPS web hosting
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
  - [1] 2026-11-19: the free shell disk quota is 100 MB and the supporter quota is 1000 MB | capture: sha256:1431416826ac3e23ee1580e17364225936bfc8b0b0046cf305e53a4639a7b404 | quote: | [Disk Quota](https://blinkenshell.org/docs/disk-quota) | 100 MB[(x4~)](https://blinkenshell.org/docs/disk-quota) | 1000 MB [(x4~)](https://blinkenshell.org/docs/disk-quota) |
  - [2] 2026-11-19: the MetaARPA tier offers persistent 20 GB OS images | capture: sha256:816fd48f02286ccf1b4578b6657253549dc33f1a9e896498ef33b25d571f4a4f | quote: - 20GB OS images are persistent and can be interchanged
  - [1] 2026-11-19: the interface is SSH and SFTP with static HTTPS web hosting | capture: sha256:1431416826ac3e23ee1580e17364225936bfc8b0b0046cf305e53a4639a7b404 | quote: Secure remote login and file transfers via [SSH](https://blinkenshell.org/dictionary/ssh) and [SFTP](https://blinkenshell.org/dictionary/sftp).
  - [1] 2026-11-19: each account gets static HTTPS web hosting | capture: sha256:1431416826ac3e23ee1580e17364225936bfc8b0b0046cf305e53a4639a7b404 | quote: [Webhosting](https://blinkenshell.org/docs/webhosting) `https://<username>.u.blinkenshell.org`
  - [2] 2026-11-19: SDF also accepts inbound ssh, ftp and sftp connections | capture: sha256:816fd48f02286ccf1b4578b6657253549dc33f1a9e896498ef33b25d571f4a4f | quote: inbound ssh, ftp and sftp connections
  - [1] 2026-11-19: the disk quota is shared across home directory, website and mail | capture: sha256:1431416826ac3e23ee1580e17364225936bfc8b0b0046cf305e53a4639a7b404 | quote: 100/1000 MiB Disk quota (shared for home directory, website and mail)
  - [2] 2026-11-19: the paid VPS tier gives persistent OS images, not a per-object cap | capture: sha256:816fd48f02286ccf1b4578b6657253549dc33f1a9e896498ef33b25d571f4a4f | quote: 20GB OS images are persistent and can be interchanged
  - [1] 2026-11-19: the pages give no guaranteed retention term | capture: sha256:1431416826ac3e23ee1580e17364225936bfc8b0b0046cf305e53a4639a7b404 | quote: This is a hobby project!
  - [1] 2026-11-19: the pages describe connectivity but state no egress price or traffic quota | capture: sha256:1431416826ac3e23ee1580e17364225936bfc8b0b0046cf305e53a4639a7b404 | quote: Static IPs, Reverse DNS, [IPv6](https://blinkenshell.org/docs/ipv6)
- sources:
  - [1] https://blinkenshell.org/
  - [2] https://sdf.org/?join
