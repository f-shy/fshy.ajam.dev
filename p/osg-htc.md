# OSPool

> osg-htc.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/osg-htc/ | JSON https://fshy.ajam.dev/api/v1/entity/osg-htc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OSPool

- `compute/ospool` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://osg-htc.org/services/ospool/
- free tier: "The OSPool is a source of computing capacity that is accessible to any researcher affiliated with a US academic institution." The page reports one day of operation as 831K jobs completed, placed by 56 research projects, consuming 844K core hours, from capacity contributed by 68 institutions. The documented ideal job is 1 CPU per job, under 10 hours walltime, a few GB of RAM, 1 GPU per job, with expected throughput of "1000s concurrent cores" per user. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: opportunistic-throughput
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): Eligibility is an affiliation with a US-based academic, government or non-profit institution or project; an unaffiliated person cannot obtain a full OSPool account, and the guest notebook is the only route that does not ask for one. [1]
- limits note: Eligibility is an affiliation with a US-based academic, government or non-profit institution or project; an unaffiliated person cannot obtain a full OSPool account, and the guest notebook is the only route that does not ask for one.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The guest notebook is the only part reachable without an affiliation, and it composes into a benchmark: it submits real HTCondor jobs, so a full 844K-core-hour pool can be measured on a handful of jobs before any affiliation exists, but the capacity beyond that stays behind the institutional door.
- reliability: no reliability event recorded
- notes: Three routes exist for an unaffiliated user. (1) A full OSPool account via the OSG Portal is closed to them by the eligibility sentence above. (2) The OSPool guest notebook, which the documentation says needs no account and accepts Google or Microsoft sign-in, so this is a real trial route with an email-level identity and is the one route that would move this record to a reachable verdict. (3) Joining somebody else's project, which requires that project's PI to add the user and therefore does not remove the affiliation requirement. The throughput numbers are the page's own counters for one day and are not a quota; no per-user allocation limit is published anywhere read, which is why binding is recorded as the eligibility gate rather than a request rate.
- extras:
  - facets.class: open-science-grid
  - facets.free_tier_kind: opportunistic-throughput
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: "The OSPool is a source of computing capacity that is accessible to any researcher affiliated with a US academic institution", quoted
  - [1] 2026-10-22: daily totals for 21 October: 831K jobs, 56 projects, 12M file transfers, 844K core hours, 68 institutions, quoted from the page counters
  - [1] 2026-10-22: ideal job table: 1000s concurrent cores per user, CPU 1 per job, walltime under 10 hours, RAM under a few GB, GPU 1 per job, quoted
  - [1] 2026-10-22: "The OSPool is made up of mostly opportunistic capacity - contributing clusters may interrupt jobs at any time", quoted
  - [2] 2026-10-22: "You can do so with an OSPool notebook - and you don't even need an account!"; the sign-in step offers Google or Microsoft when the institution is not listed, quoted
- sources:
  - [1] https://osg-htc.org/services/ospool/
  - [2] https://portal.osg-htc.org/documentation/overview/test-drive-ospool/
