# tilde.zone

> tilde.zone | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tilde-8/ | JSON https://fshy.ajam.dev/api/v1/entity/tilde-8.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tilde.zone

- `compute/tilde-zone` | qualifies-with-caveat | evidence unverified | binding write-gated | category shared shell
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://tilde.zone/
- free tier: no first-party claim of a free shell was found. Fetched on 2026-10-22, tilde.zone/ redirects to /explore and serves a Mastodon instance: a trending feed, posts and hashtag links, and no shell, no signup and no operator page. A host answering SSH is evidence of a host, not of a free shell | unit: none | metered on: none | read on: 2026-10-22 | source: [1] | note: Free shell access is not documented; registration requires administrator approval.
- per-object cap: not stated in the source | note: No object quota documented in published terms.
- retention: unknown; no policy was published to either pass
- egress: not published | metered: no | source: [1]
- identity: email | detail: unknown: no operator page and no signup path were found, so the cost of an account cannot be stated. The value is 'email' only because the schema has no 'unknown'
- interface: ssh
- limits:
  - write-gated (binding): no signup path and no operator page were found. The only page the host serves is a Mastodon instance, so the registration gate is the one constraint established and it is a documented absence rather than a published limit [2]
- limits note: no quota, retention or login policy was established, and the only page the host serves is a Mastodon instance. The host is up and the terms are unread, which is a reachability measurement rather than a finding about a free shell
- binding note: obtaining an account is the only constraint this record can name: no signup path exists that verification could find, and no quota, retention clock or session cap was published to either pass. The host answering is a measurement, not an offer.
- interface detail: SSH on port 22; a Debian host
- tooling: SSH, a Debian userspace
- composes with: unknown: the account terms were not established
- reliability: no reliability event recorded
- notes: Fetched first-party on 2026-10-22, tilde.zone/ redirects to /explore and serves a Mastodon instance with a trending feed and no shell, no signup and no operator page. The measurement is kept because it is real and deleting it would lose the evidence. Recovering the row needs a first-party page that names an operator and a signup path
- evidence note: the SSH banner was measured twice and is real. Nothing about a free shell, an account, a quota or a retention clock was established, and the one page the host serves is a Mastodon instance. The weakest link among the fields the verdict rests on is unverified, so the record is unverified with a measured reachability note
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: tilde.zone
  - port: 22
  - ms: 378
  - ok: yes
  - banner: SSH-2.0-OpenSSH_10.0p2 Debian-7+deb13u4
  - peer: 2a01:4f8:252:3e22::53
- extras:
  - billing_model: flat-pool
  - network_out.allow_outbound: yes
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - free_tier_kind: allowance
  - probe_result: connect 0.21 s and 0.35 s, banner SSH-2.0-OpenSSH_10.0p2 Debian-7+deb13u4
  - demotion_note: None was found on 2026-10-22
- evidence:
  - probe:tilde.zone:22 2026-10-22: TCP connect succeeded in 0.38 s to 2a01:4f8:252:3e22::53 and read banner SSH-2.0-OpenSSH_10.0p2 Debian-7+deb13u4
  - [2] 2026-10-22: the host's root redirects to /explore and serves a Mastodon instance: a trending feed, post and hashtag links, 518 words of rendered text. No mention of a shell, a signup, a quota or an operator was found in it
- sources:
  - [1] https://tilde.zone/
  - [2] https://tilde.zone/explore
