# M-Lab

> measurementlab.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/measurementlab/ | JSON https://fshy.ajam.dev/api/v1/entity/measurementlab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## M-Lab (host a measurement site)

- `storage/m-lab` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category bandwidth-sharing co-op / academic testbed
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.measurementlab.net/contribute/
- free tier: contribute servers, not consume storage; host-managed deployment onboarding is 'almost entirely automated' for 'any reasonably modern, high-performance, and well-connected physical or virtual server' | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: you supply it; M-Lab supplies an API key and measurement-server config | metered: no
- identity: institution | detail: institution
- interface: unknown
- limits note: This is a contribution programme, not an allocation programme - joining gives you no compute and no disk, only the right to run measurement containers. The data M-Lab produces is free and open (and genuinely large), but it is measurement data, not storage you can put your 20 TiB in. Second pilot phase, organisations rather than individuals.
- interface detail: Docker-based measurement slices; BigQuery for the resulting data
- tooling: M-Lab host-managed docs, docker, API key
- composes with: none for storage
- reliability: Node is a public measurement vantage point; your bandwidth is consumed by other people's tests.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: contribute servers, not consume storage; host-managed deployment onboarding is 'almost entirely automated' for 'any reasonably modern, high-performance, and well-connected physical or virtual server'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Host or Sponsor an M-Lab Measurement Site ... allowing any reasonably modern, high-performance, and well-connected physical or virtual server to be added to M-Lab's fleet'; 'We are now accepting new host organizations in a second pilot phase'; 'M-Lab will provide successful applicants with an API key'
  - [2] 2026-10-21: 'Measure the Internet, save the data, and make it universally accessible and useful' - the deliverable is measurement data, not storage
- sources:
  - [1] https://www.measurementlab.net/contribute/
  - [2] https://www.measurementlab.net/
