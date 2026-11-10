# tilde.institute

> tilde.institute | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tilde-5/ | JSON https://fshy.ajam.dev/api/v1/entity/tilde-5.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tilde.institute

- `compute/tilde-institute` | qualifies-with-caveat | evidence documented | binding write-gated | category shared shell | tier pubnix account
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:32:00.000Z (live) | stale on 2026-11-24
- url https://tilde.institute/
- free tier: A free OpenBSD shell account on a pubnix: SSH, a home directory served over HTTP at tilde.institute/~user, mail in maildir, IRC clients, and a wiki. No disk quota, RAM figure or traffic allowance is published on the home page, the FAQ or the signup page. | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: no quota of any kind is stated on the pages read; that is a documented absence, not a documented limit
- per-object cap: not applicable: the unit is a home directory, not an object
- retention: not stated: no inactivity clock or deletion policy appears on the news page, the FAQ or the signup page | source: [1] | note: a documented absence
- egress: not stated: no traffic volume or bandwidth figure appears on any page read | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: No card, no hold, no phone, no document. Joining is an IRC conversation: 'Please join the IRC network and hang out for a while. You'll be able to request an account from there. Connection details: institute.tilde.chat, Port 6697, TLS required.' There is no signup form to read, so what the account request itself asks for is not established.
- interface: ssh
- limits:
  - write-gated (binding): there is no form: 'Please join the IRC network and hang out for a while. You'll be able to request an account from there.' [2]
  - volume-quota: no disk, memory or process quota is published anywhere read [1]
- binding note: the account is granted by an admin on IRC after the applicant has spent time in the channel, and no quota is published to plan against even once granted
- interface detail: SSH on the default port to an OpenBSD host; web space at https://tilde.institute/~user; git hosting at git.tilde.institute from the home directory; mail in maildir; IRC via the tilde.chat network
- tooling: any SSH client; a shell on OpenBSD; the site's wiki
- composes with: a free OpenBSD shell with a web directory and mail, which is a place to run a small script or publish a page, and is currently at risk of losing SSH access
- reliability: the operator's news of 2026-10-22 states: 'PHP has been removed entirely. I will either be setting aside time to rebuild this whole thing on OpenBSD 8.0 soon, or I will need to turn off SSH access until I can make time.' That is a live statement that SSH access may be switched off
- notes: Tilde Institute provides public access Unix shell environments on OpenBSD systems for educational and community use. Resource allocations are shared among active users.
- evidence note: the joining procedure, the services and the at-risk notice are quoted from first-party pages read; the quota is a documented absence; no account was requested
- extras:
  - billing_model: free
  - term: perpetual
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: no price: the service is free and there is no form that could collect payment
  - free_tier_kind: perpetual
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - session_cap.restart_required: no
  - session_cap.note: none published
  - at_risk: news of 2026-10-22 states SSH access may be turned off pending an OpenBSD 8.0 rebuild
  - platform: OpenBSD
- evidence:
  - [2] 2026-10-24: quoted: 'Please join the IRC network and hang out for a while. You'll be able to request an account from there.' with 'institute.tilde.chat', 'Port 6697', 'TLS required'
  - [1] 2026-10-24: quoted, dated 2026 October 22: 'PHP has been removed entirely. I will either be setting aside time to rebuild this whole thing on OpenBSD 8.0 soon, or I will need to turn off SSH access until I can make time.'
  - [1] 2026-10-24: quoted, dated 2023 April 03: 'Also, re-enabled the signup form.' - the signup form was a thing that existed and was later replaced by the IRC procedure now on /signup
  - [3] 2026-10-24: the FAQ answers shell changes, site index pages and similar operational questions; it states no quota, no retention rule and no traffic allowance
  - [4] 2026-10-24: tilde.institute is listed as a member tilde of the tildeverse, alongside blinkenshell, ctrl-c.club, envs.net, sdf.org and others
  - [5] 2026-10-24: quoted: '### tilde.institute - A public-access UNIX system running OpenBSD - sysadmins: gbmor, kneezle - os: openbsd - channel: #institute - created: Thu Nov 22nd, 2018'
  - [1] 2026-10-24: quoted, dated 2023 April 03: 'Also, re-enabled the signup form.' — the signup form was a thing that existed and was later replaced by the IRC procedure now on /signup
  - [5] 2026-10-24: quoted: '### tilde.institute — A public-access UNIX system running OpenBSD — sysadmins: gbmor, kneezle — os: openbsd — channel: #institute — created: Thu Nov 22nd, 2018'
- sources:
  - [1] https://tilde.institute/
  - [2] https://tilde.institute/signup
  - [3] https://tilde.institute/faq
  - [4] https://list.tilde.link/
  - [5] https://tildeverse.org/members/
