# nanoHUB

> nanohub.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nanohub/ | JSON https://fshy.ajam.dev/api/v1/entity/nanohub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nanoHUB

- `compute/nanohub` | qualifies-with-caveat | evidence documented | binding request-rate | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://nanohub.org/kb/registration/how-to-create-a-free-nanohub-account
- free tier: "Each free nanoHUB account comes with 10 GB of free storage space, and three app sessions can be run simultaneously. Each session can have many runs, and persist over multiple days so long as you remain active with them." Accounts are created with "your existing Google account, an email account, or your own institution's account if it is a member of InCommon", and the catalogue holds over 600 simulation apps whose "computational power is provided by nanoHUB [...] these are provided by servers or supercomputer clusters". | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-open-registration
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): Three simultaneous app sessions is the ceiling, so throughput is bounded by session count rather than by jobs or core-hours, and sessions lapse when the user stops being active. [1]
- limits note: Three simultaneous app sessions is the ceiling, so throughput is bounded by session count rather than by jobs or core-hours, and sessions lapse when the user stops being active.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: nanoHUB composes with a batch programme rather than replacing one: an app can be pointed at an external cluster allocation, so a client holding any of the allocations in documented records could front it with a nanoHUB interface, though the reverse, using nanoHUB as a general compute backend, does not work.
- reliability: no reliability event recorded
- notes: Registration requires email or Google authentication without requiring university credentials. nanoHUB provides online simulation tools and scientific application engines (such as MATLAB and nanotechnology simulations) rather than raw shell access. Per-application core and memory allocations are configured per tool.
- extras:
  - facets.class: open-science-platform
  - facets.free_tier_kind: perpetual-open-registration
- evidence:
  - [1] 2026-10-22: "There are 3 ways to connect: use your existing Google account, an email account, or your own institution's account if it is a member of InCommon", quoted
  - [2] 2026-10-22: "Each free nanoHUB account comes with 10 GB of free storage space, and three app sessions can be run simultaneously", quoted
  - [2] 2026-10-22: "The computational power is provided by nanoHUB. Depending on the app, these are provided by servers or supercomputer clusters"; "you can view a list of all of the over 600 apps", quoted
  - [2] 2026-10-22: a user may "build an app that connects to your own supercomputer cluster allocation", quoted
  - [3] 2026-10-22: "Registration and online compute resources are free of charge" for the tool workshop series, quoted
- sources:
  - [1] https://nanohub.org/kb/registration/how-to-create-a-free-nanohub-account
  - [2] https://nanohub.org/groups/chem/simulations
  - [3] https://nanohub.org/resources/38690
