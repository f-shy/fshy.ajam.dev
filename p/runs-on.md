# RunsOn

> runs-on.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runs-on/ | JSON https://fshy.ajam.dev/api/v1/entity/runs-on.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RunsOn

- `compute/runs-on` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:35.123Z (live) | stale on 2026-12-05
- url https://runs-on.com/pricing/
- free tier: A free licence is provided for non-commercial open-source use in exchange for a public link back. Commercial licences cost EUR 300 to EUR 1,800 annually, with AWS compute instances billed directly at spot rates with no markup. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published by RunsOn: https://runs-on.com/pricing/ read 2026-11-04 states the control plane, S3 cache bucket and data transfer run in the user's AWS region and bill to the user's AWS account, with no egress to a third party | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): the free licence requires non-commercial, open-source or non-profit use and a public link back to runs-on.com [1]
  - request-rate: commercial licences are sized by jobs a month: under 50k at EUR 300 a year, to under 500k at EUR 1,800 [1]
  - per-object-cap: instances bill to self-hosted AWS account at spot prices with no markup [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the free licence's terms and the commercial ladder. The compute is self-hosted AWS bill, so the free half is a licence rather than capacity, and the licence has a condition
- self hosted: yes
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a job runs on an ephemeral AWS instance and is destroyed at the end; the page states no idle clock because there is nothing to keep
  - free_tier_kind: allowance
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.price: a gp3 root volume is part of the AWS bill
  - ps.durability: the instance's ephemeral root volume
  - ps.on_stop: no
  - ps.on_destroy: no
  - ps.retention: the job's lifetime
  - net.out: yes
  - net.in: yes
  - net.ports: the runner is reachable from AWS
  - net.allowance: egress bills on a user's AWS account
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'AWS bills you for the instances at spot prices, with no markup. You pay us one license a year per company, sized by the jobs you run: no seats, no minute-metering.' with 'Free non-commercial EUR 0, OSS, non-profits' and 'Starter < 50k jobs/mo EUR 300/yr', quoted
  - [1] 2026-11-04: the control plane and its data transfer run in the user's AWS account; RunsOn publishes no egress allowance or overage price of its own | capture: sha256:cf3df6e4d10116d5b362c456acacede6b61fc3584f5c17013d2fad2b27018f9f | quote: From about $7 a month; no egress to a third party.
- sources:
  - [1] https://runs-on.com/pricing/
