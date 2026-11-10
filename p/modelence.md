# Modelence

> modelence.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/modelence/ | JSON https://fshy.ajam.dev/api/v1/entity/modelence.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Modelence

- `compute/modelence` | qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T06:29:28.300Z (live) | stale on 2026-12-05
- url https://modelence.com
- free tier: a free tier for hobby projects and prototypes, with paid plans adding resources and monitoring; the stack runs on standard AWS primitives in the vendor's account | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://modelence.com/pricing defines cloud usage as resource cost billed by the hour and lists no data-transfer allowance or price | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): the free tier is described as for hobby projects and prototypes, with no published resource figure; paid plans raise the limits [1]
- interface detail: web dashboard at cloud.modelence.com with a repository connection, plus a modelence.config.json file in the repository that a coding agent writes; a CLI run through npx (`npx modelence@latest deploy`, `setup` and `dev`) opens the browser for sign-in; no REST API or SSH was found on the pages read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The underlying platform is AWS.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 'Modelence operates your app 24/7' with crashed processes restarted, so there is no idle reap; the free tier's bound is unstated
  - free_tier_kind: allowance
  - ps.price: included in the plan
  - ps.durability: persistent backend on AWS primitives
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the app is deployed
  - net.out: yes
  - net.in: yes
  - net.ports: HTTP
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'You can deploy hobby projects and prototypes for free. Paid plans give you additional resources, monitoring, higher usage limits, and priority support.' and 'Modelence entirely runs using standard AWS primitives', quoted
  - [2] 2026-11-03: cloud usage is billed on instance size by the hour; no egress term is listed | capture: sha256:9facc3ec94d8cad0dc031797fb67fef8794eb480f236c9f344a686f1b2e75536 | quote: Cloud usage is the cost of the resources your apps run on, billed by the hour based on their size.
  - [3] 2026-11-03: deployment is through the dashboard with a repository connection or a coding agent | capture: sha256:1c6c201a6f42cdab4e527f8a243c886beff8aac9bb1039fe67d9378b503af47f | quote: You can also sign up at [cloud.modelence.com](https://cloud.modelence.com) and connect your
  - [4] 2026-11-04: deployment has a CLI command, npx modelence@latest deploy | capture: sha256:cc59a1910416c8d53fd3d1e3f30e983b0c0a9a58715fcd9a2a9c82118e632bd4 | quote: Run `npx modelence@latest deploy` in the project directory yourself, with a timeout of at
  - [5] 2026-11-04: a setup CLI command exists | capture: sha256:e9e1f837b22f4bcc577d599bcbf0efc98c69445256bdf0634c43804064067a42 | quote: Run `npx modelence@latest setup` in the project root, with a timeout of at least 10 minutes.
- sources:
  - [1] https://modelence.com
  - [2] https://modelence.com/pricing
  - [3] https://docs.modelence.com
  - [4] https://docs.modelence.com/deploy/setup.md
  - [5] https://docs.modelence.com/setup.md
