# SparkCloud

> sparkden.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sparkden/ | JSON https://fshy.ajam.dev/api/v1/entity/sparkden.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SparkCloud

- `compute/sparkcloud` | fails-identity | evidence documented | binding write-gated | category platform host
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://sparkden.org/cloud
- free tier: SparkCloud publishes a six-part free stack on one account: root Linux containers on Ubuntu 24.04 with real SSH, auto-hibernating browser dev Spaces, managed Postgres 16 with daily backups, static hosting with custom domains, an OpenAI-compatible endpoint fronting Claude, GPT and Gemini, and object storage with global edge caching. The page states 'Free forever, no credit card' and 'Free for every teen, no credit card, because a nonprofit covers the cost', run by a 501(c)(3). The registration page states 'Sparkden is for teenagers. Every account is age-verified.' No credit figure, container shape, or monthly hour allowance is published on either page read. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: no card and no hold; membership of a youth programme instead. Quoted: 'free for every teen, no credit card' and 'minimum age to join 13+'. The account is 'built for under-18 users from the ground up'.
- interface: ssh
- limits:
  - write-gated (binding): The age verification is the binding constraint and it is a gate rather than a quota: 'Every account is age-verified', so an adult outside the stated range cannot reach any of the six components, and no amount of usage planning changes that. [1]
- limits note: The age verification is the binding constraint and it is a gate rather than a quota: 'Every account is age-verified', so an adult outside the stated range cannot reach any of the six components, and no amount of usage planning changes that.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Supplies database, object store, static hosting, AI endpoints, and virtual machine capacity under a single identity with no credit card required. Eligibility requires youth age verification.
- reliability: no reliability event recorded
- notes: The quota is unknown, which matters if the age policy ever widens; the page publishes no credit number, no container shape and no monthly hour allowance, so a reader who found the door open would still not know what was behind it. FreeTierWatch and a Hacker News thread both discuss Oracle's halving in the same week, which is how this lead was found.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: allowance
- evidence:
  - [1] 2026-10-22: 'Free forever, no credit card' and 'Free for every teen, no credit card, because a nonprofit covers the cost', quoted; the six components are listed as containers, spaces, databases, tiles, AI and agents, and CDN storage
  - [2] 2026-10-22: 'Sparkden is for teenagers. Every account is age-verified', quoted, and the page description states 'Teenagers 13+ get free project hosting'
  - [3] 2026-10-22: the console is live and serves 'a real cloud, free for teens' with a sign-up path, which establishes the product is operating rather than announced
  - [1] 2026-10-24: quoted: 'Real Linux servers with root and SSH ... Free for every teen, no credit card, because a nonprofit covers the cost' and 'Containers ubuntu 24.04 · root · real ssh'
  - [1] 2026-10-24: quoted on the reap: 'Spaces hibernate when you close the tab, so idle time never costs you credits'
  - [4] 2026-10-24: quoted on the gate: 'give teenagers (13+) everywhere the free cloud hosting', 'free for every teen', 'minimum age to join 13+'
  - [4] 2026-10-24: quoted on the allowance: 'Every teen account gets a standing monthly allotment, granted automatically' and 'Your allotment resets at the start of each month'
- sources:
  - [1] https://sparkden.org/cloud
  - [2] https://sparkden.org/register
  - [3] https://cloud.sparkden.org/
  - [4] https://sparkden.org/
