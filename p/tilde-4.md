# ~horse

> tilde.horse | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tilde-4/ | JSON https://fshy.ajam.dev/api/v1/entity/tilde-4.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ~horse (tilde.horse)

- `compute/tilde-horse-free` | qualifies-with-caveat | evidence documented | binding volume-quota | category shell-account | tier shell account
- needs card no, phone no, ID no, institution no | verified 2026-10-24T04:12:03.000Z (live) | stale on 2026-11-24
- url https://tilde.horse/signup
- free tier: 'tilde.horse is a digital community built upon a shared Alpine Linux server.' Access requires an SSH key: 'Shell access requires an SSH key - password authentication over SSH is disabled.' Signup asks for a username, an email, a public key and a note of at least 50 characters, then 'We'll email you after review.' | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not published: no disk quota or process cap is stated on the signup, manual or security pages read. The security page states only that 'Process and memory caps (limits.conf) prevent fork bombs and runaway memory allocation' without giving the numbers.
- retention: not published: no inactivity sweep or expiry is stated on any page read. Signup is manually reviewed, and the operator says 'We'll email you after review'.
- egress: not published: no traffic allowance appears on the pages read | metered: no | source: [2]
- identity: email | detail: no card and no payment data: signup asks for an email address, a username, an SSH public key and a written reason of at least 50 characters. No phone and no document. A human reviews the application.
- interface: ssh, sftp
- limits:
  - volume-quota (binding): not published; limits.conf caps processes and memory without stating the numbers [3]
  - write-gated: manual review of an application that includes a 50-character note [1]
- binding note: An undisclosed memory and process cap on a shared box binds first, and because the number is not published there is no ceiling to design against.
- interface detail: SSH on port 22 over clearnet, Yggdrasil, Tor and I2P; SFTP; a static web directory at ~/public_www served over HTTPS; mail, XMPP, IRC via soju, git hosting and a file-sharing service, all tied to the same PAM credentials
- tooling: any SSH client with an ed25519 or RSA key; no password auth
- composes with: A shared Alpine box that answers on port 22 and runs a cron, with mail and XMPP beside it. It is not a VPS and cannot be one: static hosting only, no sudo, and a process cap.
- reliability: no reliability event observed. The site states '/signup is rate-limited against automated scripts'.
- notes: Tilde.horse provides shared Alpine Linux shell accounts with static web hosting, cron execution, mail, and XMPP upon email registration and SSH public key submission.
- evidence note: The signup fields, the SSH-key-only rule and the isolation measures are quoted from the project's own pages read. Quota, retention and egress are all unpublished, so those fields are documented absences rather than limits and cannot be used in arithmetic.
- extras:
  - billing_model: free
  - term: not published
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: no charge and no published rate; nothing to multiply
  - free_tier_kind: free-forever
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: no user-level listening port stated; SSH in on 22 and static HTTPS out
  - session_cap.restart_required: no
  - session_cap.note: no expiry published; a shared box rather than a per-user machine
- evidence:
  - [1] 2026-10-24: quoted: 'Apply with your email, SSH public key, and a short note. We'll email you after review.'; fields 'Username', 'Email address', 'SSH public key', 'Why do you want to join? - Minimum 50 characters'
  - [2] 2026-10-24: quoted: 'Shell access requires an SSH key - password authentication over SSH is disabled.'; 'The shell is reachable over multiple networks. All use port 22.'; Clearnet, Yggdrasil, Tor and I2P endpoints listed; services 'mail, XMPP, IRC via soju, git hosting, and secure temporary file sharing'
  - [3] 2026-10-24: quoted: 'Process and memory caps (limits.conf) prevent fork bombs and runaway memory allocation'; 'User sites (~/public_www/) are strictly static. No user-level PHP or dynamic server-side scripts run under the webserver.'; 'General shell users have no elevated privileges'
  - [4] 2026-10-24: quoted: 'tilde.horse is a digital community built upon a shared Alpine Linux server.'; a list of 21 current members is published and 'updated every 15 minutes'
- sources:
  - [1] https://tilde.horse/signup
  - [2] https://tilde.horse/manual.html
  - [3] https://tilde.horse/security.html
  - [4] https://tilde.horse/
