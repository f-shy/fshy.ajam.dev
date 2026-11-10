# NYC Mesh

> nycmesh.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nycmesh/ | JSON https://fshy.ajam.dev/api/v1/entity/nycmesh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NYC Mesh

- `storage/nyc-mesh` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category community mesh network
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.nycmesh.net/
- free tier: a network connection plus the ability to host services on it; no storage quota because there is no storage product | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: donated transit from upstream peers; the wiki is explicit that NYC Mesh cannot detect or prevent traffic monitoring by those upstreams | metered: no
- identity: email | detail: email
- interface: s3
- limits note: Cost is $240 equipment plus $50 install ($290 total), or $110 plus $50 subsidized ($160 total), plus a voluntary monthly donation. Community ISP network providing symmetric bandwidth and routable IP in the New York City metropolitan area without hosted storage.
- interface detail: a routed internet connection; you run your own server behind it
- tooling: standard Linux/nginx/S3 behind your own router
- composes with: member-hosted services are a stated goal - 'we allow for fast uploads as well as downloads, so members of our community can host content and services rather than only consume them'
- reliability: Depends on donated upstream transit and volunteer installers; no SLA and no redundancy.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: a network connection plus the ability to host services on it; no storage quota because there is no storage product
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'We allow for fast uploads as well as downloads, so members of our community can host content and services rather than only consume them from centralized hosts'; 'Average Equipment Cost: $240 ... Install Leader Expenses: $50 ... Total: $290'; subsidised '$110 ... Total: $160'; 'The NYC Mesh network depends on donated transit bandwidth from upstream individuals and companies ... NYC Mesh is unable to detect or prevent traffic monitoring by our upstream providers'
  - [2] 2026-10-21: 'Join our community network!'
- sources:
  - [1] https://wiki.nycmesh.net/books/1-introduction/page/frequently-asked-questions
  - [2] https://www.nycmesh.net/
