# smol cloud

> smolmachines.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/smolmachines/ | JSON https://fshy.ajam.dev/api/v1/entity/smolmachines.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## smol cloud

- `compute/smol-cloud` | qualifies-with-caveat | evidence documented | binding volume-quota | category managed microVM | tier standard
- needs card no, phone no, ID no, institution no | verified 2026-11-24T10:11:15.094Z (live) | stale on 2026-12-25
- url https://smolmachines.com/pricing
- free tier: New accounts receive USD 100.00 of one-time sign-up credit, no card needed to start. It is prepaid balance that does not reset monthly; whatever is left stays. Without a card an account can run up to 4 machines at once of up to 4 vCPU each. | unit: credits | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: The credit is granted once at signup, not monthly, and is held until the email address is verified. The standard plan has no monthly fee.
- per-object cap: not applicable: the unit is a Linux microVM, not an object; machine disk on the standard plan is not published | source: [1]
- retention: The machine filesystem persists across exec and stop/start; a stopped machine keeps its files and its held disk keeps billing. A recovery point is exported on an API or idle stop at no charge, but excludes /workspace. | source: [2]
- egress: USD 0.05 per GB out; an open outbound network or an allowCidrs list is set explicitly, and a stopped machine stops the base, CPU and memory meters while held disk keeps billing | metered: yes | price per TB: USD 50 per TB at the published USD 0.05 per GB rate | source: [1]
- identity: email | detail: An email-and-password sign-up holds the credit until the address is verified and creates nothing until then unless credit is added or auto-recharge is turned on; no card is needed to start. Adding a card lifts the 4-machine / 4-vCPU no-card ceiling once the account has paid or is a day old.
- interface: rest
- limits:
  - volume-quota (binding): USD 100.00 of one-time sign-up credit; standard plan allows 20 machines at once and 8 vCPU per machine [1]
  - per-ip-shaping: without a card an account can run up to 4 machines at once of up to 4 vCPU each; many accounts from the same email domain or network on one day create nothing until credit is added or auto-recharge is on [3]
  - retention-clamped: a machine with a published port and no autoStopSeconds can be stopped by the platform's idle default unless the plan includes always-on; /tmp and /run are emptied on each stop and start [2]
- limits note: Every machine bills a one-minute minimum at the size requested; longer runs bill to the second. A machine larger than the plan allows is refused at create time with the limit in the reply. Disk is billed around the clock, including while stopped.
- binding note: The one-time USD 100.00 credit binds first: at the USD 0.04 machine-hour plus USD 0.05 vCPU-hour plus USD 0.0162 GB-hour and USD 0.0001 GB-hour disk rates it funds a few thousand machine-hours, while the 20-machine standard-plan ceiling is a separate create-time refusal.
- interface detail: The dashboard uses the same REST API a caller can use from code, with a bearer token from /console/keys; the SDKs and CLI are named smol and smolvm.
- endpoint: https://api.smolmachines.com
- tooling: curl against the REST API with an SMOL_CLOUD_TOKEN, or the smol SDK and CLI; a saved key from smol auth login wins over the environment token.
- composes with: A managed VM with a REST control plane and S3-compatible remote mounts can be driven by an agent SDK and checkpointed to external object storage, while the same workload runs locally through smolvm.
- reliability: A machine with a published port can be stopped on the platform's idle default without an explicit autoStopSeconds; a node loss loses memory and writes since the last recovery point, and /workspace comes back empty on restore.
- notes: The hosted lane of smol machines' microVM engine: USD 100.00 of one-time credit at an email-only signup, no card needed to start, with usage-priced compute, memory, disk and egress. The one-minute billing minimum and the platform's idle stop of published-port machines are the practical clocks.
- evidence note: Every rate, the sign-up credit, the no-card ceiling and the idle behaviour are quoted from the vendor's own pricing, quick-start and lifecycle pages read on 2026-11-24. smolvm itself is separate self-hostable software; this record prices the hosted smol cloud lane only.
- self hosted: no
- extras:
  - shape.vcpu: 8
  - shape.ram_gib: 16
  - shape.note: standard plan ceiling of 8 vCPU and 16 GB per machine; the quick-start example creates 1 vCPU and 256 MB; no hosted GPU fields
  - billing_model: usage-based: base per machine-hour, vCPU-hour, GB-hour of active RSS, GB-hour of used disk, per GB egress
  - free_tier_kind: one-time-credit
  - term: no monthly fee on the standard plan; credit does not reset
  - price_arithmetic: USD 100.00 one-time credit; USD 0.04 per machine-hour plus USD 0.05 per vCPU-hour plus USD 0.0162 per GB-hour memory plus USD 0.0001 per GB-hour disk plus USD 0.05 per GB egress
  - status: hosted service
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: up to 16 published guest ports per machine, via authenticated connect route or login-free port links
  - network_out.per_session_bytes: USD 0.05 per GB out
  - session_cap.restart_required: no
  - session_cap.note: autoStopSeconds and ttlSeconds are set on create; the idle sweep runs every 15 seconds with an offset of up to about 75 seconds
- evidence:
  - [1] 2026-11-24: New accounts start with USD 100.00 of free credit | capture: sha256:b6f3273ce757840b1bb9b89de5a7b14979d3dc8e773766588c1cb971718acabb | quote: New accounts start with $100.00 of free credit.
  - [1] 2026-11-24: the sign-up credit is granted once and is prepaid balance that does not reset monthly | capture: sha256:b6f3273ce757840b1bb9b89de5a7b14979d3dc8e773766588c1cb971718acabb | quote: Sign-up credit is granted once. New accounts receive $100.00 of credit when they are created. It is ordinary prepaid balance: it is drawn down as you use the platform, it does not reset monthly, and whatever is left stays yours.
  - [1] 2026-11-24: the published rates for base, compute, memory, disk and network egress | capture: sha256:b6f3273ce757840b1bb9b89de5a7b14979d3dc8e773766588c1cb971718acabb | quote: | Network egress | per GB out | $0.05 |
  - [1] 2026-11-24: the standard plan has no monthly fee and allows 20 machines of up to 8 vCPU each | capture: sha256:b6f3273ce757840b1bb9b89de5a7b14979d3dc8e773766588c1cb971718acabb | quote: | Monthly fee | $0 | $20 + usage | $150 + usage | custom |
  - [3] 2026-11-24: the signup is email-and-password with no card needed and the no-card ceiling is 4 machines of up to 4 vCPU | capture: sha256:edbe61253260a8f4bc56d7e8d4a9eae185f1b757bb62b18162b118db3503c4fc | quote: New accounts get a one-time sign-up credit, no card needed to start. An email-and-password sign-up holds it until the address is verified, and creates nothing until then unless credit is added or auto-recharge is turned on. Without a card an account can run up to 4 machines at once of up to 4 vCPU each.
  - [4] 2026-11-24: the console states USD 100 of free usage with no card required | capture: sha256:1debfba995d2534db6e0ee83731f6129d42ea308f844667d77149ee806714084 | quote: Free to start: $100 of free usage, no card required.
  - [2] 2026-11-24: a machine with a published port and no explicit idle timeout can still be stopped by the platform's default idle timeout | capture: sha256:9f3d44ac34ed0e07ceadca16402c2eef17778ee412e21592843d4e6a3dd75399 | quote: A machine that publishes a port and sets no `autoStopSeconds` can still be stopped when idle by the platform's default timeout, unless its plan includes always-on.
  - [5] 2026-11-24: smol cloud is the managed service while smolvm is the self-hostable local engine, and this record prices the hosted lane | capture: sha256:8e64209aed78642a4bc6ffab4e589f4c0ed0ae71ef9b43cfd1c438ad0f136de6 | quote: smolvm is the open-source engine and CLI for running isolated Linux virtual machines locally. smol cloud is the managed service for running smolvm-based workloads in the cloud.
- sources:
  - [1] https://smolmachines.com/pricing
  - [2] https://smolmachines.com/docs/cloud/lifecycle-storage-networking
  - [3] https://smolmachines.com/docs/cloud
  - [4] https://smolmachines.com/console
  - [5] https://smolmachines.com/faq

## smol machines

- `compute/smol-machines` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-18T04:45:11.647Z (live) | stale on 2026-12-19
- url https://smolmachines.com/pricing
- free tier: $100 of one-time credit that behaves as ordinary prepaid balance and does not expire; a running machine costs $0.04 an hour as a base plus $0.05 a vCPU-hour and $0.0162 a GB-hour of memory | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.04 a machine-hour as a base for the isolated slot, plus $0.05 a vCPU-hour and $0.0162 a GB-hour of memory [1]
  - per-object-cap: an accounting model on active RSS and used disk, not on provisioned size: disk is $0.0001 a GB-hour used [1]
  - per-ip-shaping: network egress is $0.05 a GB [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The pricing page read on 2026-10-22 documents a one-time signup credit that does not expire and a base-plus-usage billing model.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 8
  - shape.ram: 16
  - shape.note: the free plan allows 8 vCPU and 16 GB per machine; the disk limit is stated as not published
  - session_cap.restart_required: no
  - session_cap.note: no session clock published; idle apps scale to zero with no published interval
  - free_tier_kind: one-time-credit
  - granularity.min_billed_s: 60
  - burst_x: 1.0
  - ps.price: $0.0001 a GB-hour used, about $0.073 a GB-month
  - ps.durability: disk billed on bytes used
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the machine exists
  - net.out: yes
  - net.in: yes
  - net.allowance: $0.05 a GB of egress
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Sign-up credit is granted once. New accounts receive $100.00 of credit when they are created. It is ordinary prepaid balance: it is drawn down as you use the platform, it does not reset monthly, and whatever is left stays yours.' with 'Base (running machine) per machine-hour running (1-minute minimum) $0.04' and 'Memory (active RSS) per GB-hour in use $0.0162', quoted
  - [1] 2026-11-18:  | capture: sha256:17e2441ae6df2566088e7e35241ae1254489f30ca09c35d86e583235c6cda115 | quote: Sit idle and the consumption lines fall to near zero; stop the machine and even the base fee stops.
- sources:
  - [1] https://smolmachines.com/pricing
