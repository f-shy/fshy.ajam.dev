# tilde.club

> tilde.club | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tilde/ | JSON https://fshy.ajam.dev/api/v1/entity/tilde.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tilde.club

- `compute/tilde-club` | qualifies-with-caveat | evidence documented | binding volume-quota | category shared shell | tier Member account
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:56:00.000Z (live) | stale on 2026-11-24
- url https://tilde.club/
- free tier: a shared Unix computer with a 1 GB soft and 3 GB hard disk quota per user; no price is stated anywhere on the site | unit: GB | metered on: stored-bytes | read on: 2026-10-24 | source: [1] | note: the FAQ says quota, not price; the site is donation-funded and states no fee
- per-object cap: not applicable
- retention: no expiry is published; the FAQ states a one-week grace period after exceeding the soft quota before the hard limit applies | source: [1] | note: no inactivity purge was found on the pages read
- egress: not published on the pages read | metered: no
- identity: email | detail: the signup form asks for a desired username, an email address, a sentence on what interests you, and an SSH public key. No card, no phone, no document. Approval is by a human reading the sentence: the form says 'Fill out this form and we'll get back to you with account info'.
- interface: rest, cli
- limits:
  - volume-quota (binding): 1 GB soft, 3 GB hard, with a one-week grace period above the soft limit [1]
- limits note: signup rejects gmail.com addresses, which is an identity gate rather than a quota
- binding note: 3 GB hard is the ceiling; above it writes fail, and there is no paid tier on the page read to lift it.
- interface detail: SSH on port 22
- tooling: SSH, screen or tmux, cron
- composes with: 3 GB of hard disk on a shared host is the largest pubnix quota verification found
- reliability: no reliability event recorded
- notes: No RAM, no CPU and no port allowance are published, so this is a place to keep files and run small jobs, not a machine to plan around. Approval is manual. Unverified: a probe on an account reading `ulimit -a` and `free -m`.
- evidence note: quota and signup fields are from the site's own FAQ and form read. The absence of a price is an observation about the pages read, not a quoted sentence.
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: tilde.club
  - port: 22
  - ms: 3687
  - ok: yes
  - banner: SSH-2.0-OpenSSH_10.0
  - peer: 142.44.150.184
- extras:
  - shape.disk_gib: 3
  - billing_model: free
  - session_cap.restart_required: no
  - session_cap.note: no session cap published
  - keep_rate.value: 0.0
  - keep_rate.basis: a free account costs nothing
  - keep_rate.source: https://tilde.club/
  - persistent_storage.included_gib: 3
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: home directory
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while active
  - network_out.allow_outbound: yes
  - network_out.ports: not published
  - free_tier_kind: always-free
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - shape_note: 3 GB is the hard quota in the vendor's own unit; no RAM or vCPU published
  - term: indefinite
  - price_arithmetic: no charge stated
- evidence:
  - probe:tilde.club:22 2026-10-22: TCP connect succeeded in 3.69 s to 142.44.150.184 and read banner SSH-2.0-OpenSSH_10.0
  - [1] 2026-10-22: soft limit 1 GB, hard limit 3 GB and a 1-week grace period, quoted from the FAQ's disk section
  - [1] 2026-10-24: quoted: 'Soft Limit: 1 GB', 'Hard Limit: 3 GB', 'Grace Period: 1 week'
  - [2] 2026-10-24: quoted: 'your desired username', 'email to contact you with account info', 'what interests you about tilde.club? we want to make sure you're a real human being', 'SSH public key'
  - [3] 2026-10-24: quoted: 'Tilde.club gives you access to a shared Unix computer where you can make web pages, learn, and share knowledge.'
- sources:
  - [1] https://tilde.club/wiki/faq.html
  - [2] https://tilde.club/signup/
  - [3] https://tilde.club/
