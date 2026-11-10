# DigitalOcean student

> github.com | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-github-education-resources/ | JSON https://fshy.ajam.dev/api/v1/entity/github-github-education-resources.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## digitalocean spaces via github student pack

- `storage/digitalocean-spaces-via-github-student-pack` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/github-education-resources/Student-Developer-Pack-Current-Partners-FAQ/blob/main/SDP-changelog.md
- free tier: none reachable: The $100-$200 student credit was removed. Changelog: 'DigitalOcean is leaving the Student Developer Pack, and their student credit offer for $200 of platform credit will no longer be… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The $100-$200 student credit was removed. Changelog: 'DigitalOcean is leaving the Student Developer Pack, and their student credit offer for $200 of platform credit will no longer be…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The $100-$200 student credit was removed. Changelog: 'DigitalOcean is leaving the Student Developer Pack, and their student credit offer for $200 of platform credit will no longer be…
- sources:
  - [1] https://github.com/github-education-resources/Student-Developer-Pack-Current-Partners-FAQ/blob/main/SDP-changelog.md

## DigitalOcean student credit

- `compute/digitalocean-student-credit` | dead | evidence documented | binding none | category dev environment
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://github.com/github-education-resources/Student-Developer-Pack-Current-Partners-FAQ/blob/main/SDP-changelog.md
- free tier: The pack's cloud-credit headline is gone. Quoted from the official pack changelog dated July 7, 2026: "DigitalOcean is leaving the Student Developer Pack, and their student credit offer for $200 of platform credit will no longer be available after July 31, 2026." Any remaining credits expired on 2026-08-01. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits note: Two doors close: the USD 200 DigitalOcean credit ended on 2026-07-31, and the whole pack requires verified full-time student status at an accredited institution.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing durable. What remains in the pack is a set of one-shot coupons, mostly software licences rather than compute, and each starts a clock when redeemed.
- reliability: no reliability event recorded
- notes: Classified as dead for the compute credit rather than for the pack, which still exists. The DigitalOcean offer page now redirects to the homepage and a new account gets USD 5 for 90 days, which is the trial that replaced USD 200. This is a refutation twice over: the credit is gone, and the pack was never open to a developer without an institution.
- extras:
  - facets.class: refutation-identity-gated
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: entry dated 2026-07-07: the DigitalOcean USD 200 student credit ends after 2026-07-31 and remaining credits expire on 2026-08-01, quoted
  - [2] 2026-10-22: a 2026 tracker records DigitalOcean as discontinued and calls the USD 200 credit claim stale
  - [3] 2026-10-22: on 2026-09-06 the offers page no longer listed DigitalOcean, and the author notes GitHub's own docs say some partner offers cannot renew
- sources:
  - [1] https://github.com/github-education-resources/Student-Developer-Pack-Current-Partners-FAQ/blob/main/SDP-changelog.md
  - [2] https://studentdevguide.dev/github-student-pack-cloud-hosting-database/
  - [3] https://www.santoshpaudel.me/blog/github-student-pack-free-vs-trial
