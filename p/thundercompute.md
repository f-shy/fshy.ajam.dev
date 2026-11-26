# Thunder Compute

> thundercompute.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thundercompute/ | JSON https://fshy.ajam.dev/api/v1/entity/thundercompute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Thunder Compute

- `compute/thunder-compute` | fails-identity | evidence documented | binding none | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T18:27:25.619Z (live) | stale on 2026-12-25
- url https://www.thundercompute.com/pricing
- free tier: No general free tier: on-demand instances bill per minute, with H100 SXM at $3.20/hr, A100 80GB at $1.09/hr, L40 at $0.79/hr and RTX A6000 at $0.35/hr; sandboxes bill per second. The first 100 GB of instance disk per GPU is included and data egress is $0.00/GB. A separate $20 student credit is limited to students enrolled at US universities and usable on A6000 or L40 GPUs. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: The pricing page lists "Data egress | No egress fees | $0.00/GB" for instances and for sandboxes; no per-GB charge or allowance is published. | metered: no | source: [1]
- identity: card | detail: An email address and a payment method are required for a normal account; the student credit instead requires enrolment at a US university and a university email. | country: US
- interface: ssh, cli
- limits:
  - request-rate: instances: $1.09/hr for an A100 80GB and $3.20/hr for an H100 SXM, billed per minute while running; sandboxes: $0.000819 a GPU-second for an H100 SXM and $0.000542 for an A100 80GB [1]
  - per-object-cap: the first 100 GB of instance disk per GPU is included and bills only while running; snapshots are $0.05 a GB-month [1]
  - per-ip-shaping: data egress is $0.00 a GB [1]
- limits note: Session cap, idle-reap and network policy are not documented. GPU only.
- binding note: No limits[] row holds a write gate; the student credit is blocked by US university enrolment, which the record states in identity_cost and in the verdict, so no capacity limit binds first.
- interface detail: The CLI connects with SSH to a running instance; the console and VS Code extension launch instances, and files move with tnr scp.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Paid-only read only the pricing page, which lists no signup credit, and missed the students page, which publishes USD 20 of credit for A6000 or L40 use. The gate is a US university enrolment rather than a card, so the capacity exists and fails identity.
- evidence note: the pricing page was read on 2026-10-22 and publishes per-second rates per resource, the included disk and the zero egress fee. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.vcpu: 6
  - shape.ram: 48
  - shape.disk: 100
  - shape.gpu_class: RTX A6000
  - shape.gpu_count: 1
  - shape.note: 48 GB of VRAM, 6 vCPU included and up to 8, 48-64 GB of RAM and 100-500 GB of disk
  - session_cap.restart_required: no
  - session_cap.note: instances bill per minute and sandboxes per second, only while running; the page states that instances and sandboxes are never preempted and states no reap and no minimum bill
  - free_tier_kind: none
  - ps.gib: 100
  - ps.price: $0.219 a GB-month past the first 100 GB
  - ps.durability: instance disk and snapshots
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - net.allowance: no egress fees
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Billed per second for each resource' with '| RTX A6000 | 48 GB | 6 included · 8 max | $0.35/hr |', 'H100 SXM 80 GB $3.20/hr', 'Instance disk: First 100 GB per GPU included; billed only while running, $0.219/GB/mo', and 'Data egress: No egress fees, $0.00/GB', quoted
  - [2] 2026-10-22: 'Only students enrolled at US universities qualify. Sign up with your university email; credit is added automatically.' and 'Student credit $20.00', quoted
  - [1] 2026-11-03: instances bill per minute while running; the sandbox per-second rate is a separate section of the page | capture: sha256:69cb665e7f187d4e290d949add24477a502f78981bf40409da686e114572c2cf | quote: Instances, including extra vCPUs and disk, are billed per minute only while running.
  - [1] 2026-11-03: the per-second H100 SXM rate belongs to the sandbox table | capture: sha256:69cb665e7f187d4e290d949add24477a502f78981bf40409da686e114572c2cf | quote: | H100 SXM | $0.000819/GPU-sec |
  - [1] 2026-11-03: no preemption is stated | capture: sha256:69cb665e7f187d4e290d949add24477a502f78981bf40409da686e114572c2cf | quote: No. Instances and sandboxes are never preempted. They run until you stop them or, for sandboxes, their TTL ends.
  - [1] 2026-11-03: A100 80GB is listed at $1.09/hr with 80 GB of VRAM | capture: sha256:69cb665e7f187d4e290d949add24477a502f78981bf40409da686e114572c2cf | quote: | A100 80GB | 80 GB | 8 included · 16 max | 64–⁠128 GB | 100–⁠500 GB | $1.09/hr
  - [1] 2026-11-03: H100 SXM is listed at $3.20/hr | capture: sha256:69cb665e7f187d4e290d949add24477a502f78981bf40409da686e114572c2cf | quote: | H100 SXM | 80 GB | 4 included · 16 max | 32–⁠128 GB | 100–⁠500 GB | $3.20/hr
  - [1] 2026-11-03: the listed rates are the on-demand rates; reserved terms are quoted by sales | capture: sha256:69cb665e7f187d4e290d949add24477a502f78981bf40409da686e114572c2cf | quote: Teams can reserve dedicated GPUs for a fixed term at a lower rate than on-demand
  - [1] 2026-11-24: the H100 SXM instance lists 80 GB VRAM and an on-demand rate of USD 3.20 per hour | capture: sha256:a5bdd739701e1bd9fe70a7d9bc0db1df80069420b3adcbd1f7b3c69977e09bed | quote: | H100 SXM | 80 GB | 4 included · 16 max | 32–⁠128 GB | 100–⁠500 GB | $3.20/hr |
  - [1] 2026-11-24: instances, CPUs and disk bill per minute only while running | capture: sha256:69cb665e7f187d4e290d949add24477a502f78981bf40409da686e114572c2cf | quote: Instances, including extra vCPUs and disk, are billed per minute only while running.
  - [1] 2026-11-24: the pricing page states no egress fee and zero dollars per GB | capture: sha256:a5bdd739701e1bd9fe70a7d9bc0db1df80069420b3adcbd1f7b3c69977e09bed | quote: | Data egress | No egress fees | $0.00/GB |
  - [3] 2026-11-24: a normal account requires an email address | capture: sha256:1b6cc6ff9fa9e00fcd692fc2b6fbbd2ff4830d18d4bb088a2821ec2992a19dea | quote: Navigate to the [Thunder console](https://console.thundercompute.com/signup) and create an account with your email.
  - [3] 2026-11-24: a payment method is added to the account | capture: sha256:1b6cc6ff9fa9e00fcd692fc2b6fbbd2ff4830d18d4bb088a2821ec2992a19dea | quote: In the console, [add a payment method](https://console.thundercompute.com/settings/billing) to your account.
  - [4] 2026-11-24: the CLI opens an SSH shell on the instance | capture: sha256:cee71f05f99da2e5780aba61462c7d923e1b65fc3f00cdc1e6fe6f05278a2c59 | quote: The CLI will set up SSH access, open the connection, and drop you into a shell on the instance.
  - [4] 2026-11-24: the console SSH workflow is documented alongside the CLI connection | capture: sha256:cee71f05f99da2e5780aba61462c7d923e1b65fc3f00cdc1e6fe6f05278a2c59 | quote: Use the console SSH workflow
  - [2] 2026-11-24: the student credit is limited to students at US universities who sign up with a university email | capture: sha256:52553dde06fb70004c65f21fbb97673bf58b986005f0cb42476d000d02f8f8b8 | quote: Only students enrolled at US universities qualify. Sign up with your university email; credit is added automatically.
  - [2] 2026-11-24: the students page states a USD 20.00 student credit | capture: sha256:52553dde06fb70004c65f21fbb97673bf58b986005f0cb42476d000d02f8f8b8 | quote: Student credit $20.00
  - [2] 2026-11-24: student credit is restricted to A6000 and L40 GPUs | capture: sha256:52553dde06fb70004c65f21fbb97673bf58b986005f0cb42476d000d02f8f8b8 | quote: Use on A6000 or L40 GPUs
- sources:
  - [1] https://www.thundercompute.com/pricing
  - [2] https://www.thundercompute.com/students
  - [3] https://www.thundercompute.com/docs/console/quickstart
  - [4] https://www.thundercompute.com/docs/cli/operations/connecting-to-instances
