# tilde.team

> tilde.team | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tilde-6/ | JSON https://fshy.ajam.dev/api/v1/entity/tilde-6.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tilde.team

- `compute/tilde-team` | dead | evidence documented | binding none | category shared shell | tier Member account
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:56:00.000Z (live) | stale on 2026-11-24
- url https://tilde.team/
- free tier: a shared Linux account on Ubuntu with tilde tools, mail, gemini and gopher; the site's own news states SSH access is currently disabled after a root compromise | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: no quota is published on the pages read
- per-object cap: not applicable
- retention: the host was rebuilt after 'rm -rf /'; the site says daily backups of the VM were taken, so 'we lost at most a couple hours of files' | source: [1] | note: this is a recovery statement, not a retention policy
- egress: not published on the pages read | metered: no
- identity: email | detail: signup at tilde.team/signup, which the site describes as a script the admins run to make accounts. The form fields were not read; no card or phone appears on the pages read.
- interface: ssh
- limits note: The account is approved by a human who reads the statement of interest, and the host it lands on is mid-rebuild after a root compromise, so the first thing that fails is the operator's availability rather than any quota.
- binding note: the binding constraint is availability, not a quota: SSH is disabled as of the August 2026 news post.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- reliability: no reliability event recorded
- notes: Tilde.team public access Unix system has suspended new public shell account registrations while maintenance is underway.
- evidence note: the outage and the disabled SSH are quoted from the site's own news post read. The quota is not published anywhere read, so it is absent rather than estimated.
- extras:
  - facets.class: pubnix-shell
  - facets.free_tier_kind: perpetual
  - facets.shape.gpu_count: 0
  - billing_model: free
  - term: unknown
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: no charge stated
  - free_tier_kind: always-free
  - network_out.ports: unknown
  - session_cap.restart_required: yes
  - session_cap.note: shell access disabled at the time of reading
- evidence:
  - [2] 2026-10-22: 'tilde.team got hacked. Someone was able to gain a root shell and ran rm -rf /', 'ssh access is currently disabled in the meantime', 'I'm still evaluating what to do with IRC, XMPP, email, nextcloud, and a few others', quoted; the item is dated August 2026
  - [1] 2026-10-22: A listening sshd is not the same as an enabled user host and the news page says the user host is disabled [receipt: ssh://tilde.team:22]
  - [3] 2026-10-22: signup asks for a username, an email, a statement of interest and an SSH public key, with 'you must be at least 13 years or older' and 'do NOT use temporary or forwarding email services to signup', quoted
  - [1] 2026-10-24: quoted: 'tilde.team got hacked. Someone was able to gain a root shell and ran `rm -rf /`.' and 'ssh access is currently disabled in the meantime.'
- sources:
  - [1] https://tilde.team/
  - [2] https://tilde.team/news/036_outage
  - [3] https://tilde.team/signup/
