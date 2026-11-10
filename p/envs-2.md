# envs.net

> envs.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/envs-2/ | JSON https://fshy.ajam.dev/api/v1/entity/envs-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## envs.net

- `compute/envs-net` | qualifies-with-caveat | evidence documented | binding request-rate | category shared shell | tier Shell user account
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:56:00.000Z (live) | stale on 2026-11-24
- url https://envs.net/
- free tier: a shell account on a Debian 13 host with 200 processes or threads, 1024 MB soft and 1536 MB hard storage, 1 GiB of /tmp, and a 250 MB mailbox | unit: MB | metered on: stored-bytes | read on: 2026-10-24 | source: [1] | note: the site states 'will always be free to use'; no price appears
- per-object cap: not applicable
- retention: files in /tmp are temporary and may be removed after 10 days of inactivity; home storage has no published expiry | source: [1] | note: no inactivity purge of the account itself was found
- egress: not published on the pages read | metered: no
- identity: email | detail: the form asks for a username, an email address and confirmation, a sentence on what interests you, and an OpenSSH public key, plus an age declaration of at least 16. No card and no phone. Approval is manual: 'fill out this form and i'll get back to you with your account informations.'
- interface: ssh
- limits:
  - request-rate (binding): 200 processes/threads at a time [1]
  - volume-quota: 1024 MB soft, 1536 MB hard on home storage; 1 GiB /tmp with 100,000 inodes [1]
  - volume-quota: 250 MB mailbox [1]
- limits note: No idle-expiry policy appears on the terms, privacy or code-of-conduct pages, so the first thing that binds is the 200-process cap and the 1.5 GiB home, not the clock; an absence of a stated reaper is recorded as absence, not as a promise.
- binding note: 200 processes is generous for scripts and fatal for anything that forks per connection; the 1.5 GB disk binds second.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A shell with mosh and a mailbox is the cheapest place to hold a key, a bouncer or a cron that does not need a public port; the operator also runs a DoH resolver, a ntfy instance and a gitea on the same account, which is a free notification path for a job running elsewhere.
- reliability: no reliability event recorded
- notes: High port listening capability remains unverified by active probe.
- evidence note: quota and process limits quoted from the site's own help page; signup fields from the form itself, both read.
- extras:
  - facets.class: pubnix-shell
  - facets.free_tier_kind: perpetual
  - facets.shape.gpu_count: 0
  - facets.shape.disk_mib_soft: 1024
  - facets.shape.disk_mib_hard: 1536
  - shape.disk_gib: 1.5
  - shape_note: 1536 MB hard quota stated by the vendor; no RAM or vCPU published
  - billing_model: free
  - term: indefinite
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: no charge
  - free_tier_kind: always-free
  - network_out.allow_outbound: yes
  - network_out.ports: not published
  - session_cap.restart_required: no
  - session_cap.note: the cap is concurrent processes, not session time
- evidence:
  - [2] 2026-10-22: 'envs.net is a minimalist, non-commercial shared linux system and will always be free to use', quoted; system info reports Debian GNU/Linux 13 (trixie)
  - [1] 2026-10-22: 'terminal connection over ssh and mosh', '200 process/threads at a time', 'soft 1024mb / hard 1536mb limit on storage', 'e-mail (250mb mailbox storage)', quoted
  - [3] 2026-10-22: signup asks for a username, an email address, a statement of interest, an optional SSH public key and an age declaration of 16 or over; no card and no phone field, quoted
  - [2] 2026-10-22: 
  - [4] 2026-10-22: 'online: 6 | total: 1567', quoted, so the host is live with a real population rather than a placeholder
  - [1] 2026-10-24: quoted: '200 process/threads at a time', 'soft 1024mb / hard 1536mb limit on storage', '1 GiB soft / hard limit on temporary /tmp storage (100,000 inodes)', 'e-mail (250mb mailbox storage)'
  - [3] 2026-10-24: quoted: 'desired username', 'e-mail for account informations', 'openssh public key', 'i am at least 16 years old.'
  - [2] 2026-10-24: quoted: 'envs.net is a minimalist, non-commercial shared linux system and will always be free to use.'
- sources:
  - [1] https://help.envs.net/
  - [2] https://envs.net/
  - [3] https://envs.net/signup/
  - [4] https://envs.net/users/
