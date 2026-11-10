# EFN

> efn.lt | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/efn/ | JSON https://fshy.ajam.dev/api/v1/entity/efn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EFN

- `compute/efn` | qualifies-with-caveat | evidence documented | binding retention-clamped | category shared shell
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:20.285Z (live) | stale on 2026-12-05
- url https://shells.efn.lt/start
- free tier: A free UNIX shell across Linux, BSD and Solaris hosts with a dated 60-day inactivity disable: quoted 'any shell account that has not been logged into for 60 consecutive days will be automatically disabled', with a disk quota of 500 MB, a 256 MB memory limit, 3 background processes and a listenable TCP/UDP port. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: The 60-day login clock is the only reaper in this set with a published date on it, so a monthly login defeats it and nothing else does; the account is disabled rather than deleted and reactivation is 'subject to availability'. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: ssh, sftp
- limits:
  - retention-clamped (binding): The 60-day login clock is the only reaper in this set with a published date on it, so a monthly login defeats it and nothing else does; the account is disabled rather than deleted and reactivation is 'subject to availability'. [1]
- limits note: The 60-day login clock is the only reaper in this set with a published date on it, so a monthly login defeats it and nothing else does; the account is disabled rather than deleted and reactivation is 'subject to availability'.
- binding note: the same as limits note
- interface detail: SSH shell account, with SFTP access on the free plan, documented at shells.efn.lt/services
- tooling: any SSH or SFTP client; the services page names no specific client
- composes with: 500 MB with three background processes and a listenable port is the cheapest always-on place for an IRC bouncer or a small TCP daemon, and the port is the part most pubnixes withhold.
- reliability: no reliability event recorded
- notes: The 60-day policy is dated 2026-10-06, which is 16 days before this read, so this is a reaper that was introduced recently and is the single most useful thing in the record. The FAQ states registration is blocked in some countries; which countries is on a page not read here, and that matters for an international registrant. Two open questions. One, whether 'login' means an interactive SSH session or any authentication, which decides whether a cron inside the host counts. Two, whether the TCP port is reachable from outside, because the services page lists it as a feature but no page states an inbound firewall rule. The host did not answer on 22 from this vantage, which is a routing fact and not a verdict.
- extras:
  - facets.class: pubnix-shell
  - facets.free_tier_kind: perpetual
  - facets.shape.ram_gib: 0.25
  - facets.shape.gpu_count: 0
  - facets.shape.disk_mib: 500
- evidence:
  - [1] 2026-10-22: '2026.10.06 - Important Update: Inactive Accounts Will Be Disabled After 60 Days', 'any shell account that has not been logged into for 60 consecutive days will be automatically disabled', and the VIP exception: 'Users who donate will receive VIP status and be added to the exception list', quoted
  - [2] 2026-10-22: the free tier table: 'Disk Quota 500 MB', 'Memory limit 256 MB', 'Background Processes 3', 'Simultaneous Processes 20', 'Listen TCP/UDP port (custom server)' checked, 'Monthly Fee $0.00', quoted
  - [2] 2026-10-22: 
  - [1] 2026-10-22: '2026.07.28 - Registration restrictions in selected regions' because of 'abuse, automated activity, and infrastructure load', quoted
  - [1] 2026-10-22: TCP connect timed out at 32376 ms from this host; recorded as no TCP answer from this host and not as a dead provider [receipt: ssh://shells.efn.lt:22]
  - [2] 2026-11-03: the free plan includes SSH and SFTP access | capture: sha256:cc1150c72587e81162adc056fb1bc22edebea2b5e4af15d54ee1c38c68d5fc95 | quote: | SSH & SFTP Access | ✔ |
  - [2] 2026-11-04: SSH and SFTP access are on the free plan | capture: sha256:cc1150c72587e81162adc056fb1bc22edebea2b5e4af15d54ee1c38c68d5fc95 | quote: | SSH & SFTP Access | ✔ |
  - [2] 2026-11-04: the shell is reached by SSH | capture: sha256:cc1150c72587e81162adc056fb1bc22edebea2b5e4af15d54ee1c38c68d5fc95 | quote: a personal shell on a Unix-based server (Linux, BSD, Solaris) that you can connect to via [SSH](https://shells.efn.lt/ssh).
- sources:
  - [1] https://shells.efn.lt/start
  - [2] https://shells.efn.lt/services
