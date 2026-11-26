# Fosshost

> bleepingcomputer.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bleepingcomputer/ | JSON https://fshy.ajam.dev/api/v1/entity/bleepingcomputer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fosshost

- `compute/fosshost` | dead | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.bleepingcomputer.com/news/technology/open-source-software-host-fosshost-shutting-down-as-ceo-unreachable/
- free tier: Free VPS, web hosting, mirror and AArch64 compute for about 250 open source projects including GNOME, Armbian, Debian and FSFE. Applications were suspended in September 2022 and the service reached end of life in December 2022. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous
- interface: unknown
- limits note: The provider no longer exists, so nothing binds; the failure mode was organisational, with the chief executive unreachable and co-location unpaid.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing. Documented so the subsequent evaluation does not apply.
- reliability: no reliability event recorded
- notes: The generalisable lesson is the failure mode, not the provider: a free VPS programme run by a volunteer nonprofit with one person holding the bank account died within months, and about 250 projects had to migrate. That is the reliability note to attach to any nonprofit free-compute offer, including the ones still running.
- extras:
  - facets.class: inverse-dead
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: report dated 2022-12-04 of the shutdown, the unreachable chief executive, and users told to back up and migrate
  - [2] 2026-10-22: volunteer statement that co-location costs could not be paid because only the chief executive had bank access, so servers would go offline
  - [3] 2026-10-22: the organisation's own post dated 2022-09-07 announcing that applications were suspended
- sources:
  - [1] https://www.bleepingcomputer.com/news/technology/open-source-software-host-fosshost-shutting-down-as-ceo-unreachable/
  - [2] https://news.ycombinator.com/item?id=33848529
  - [3] https://github.com/fosshostorg/fosshost.org/blob/main/src/posts/suspended-applications.md
