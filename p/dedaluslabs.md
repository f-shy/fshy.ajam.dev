# Dedalus Labs

> dedaluslabs.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dedaluslabs/ | JSON https://fshy.ajam.dev/api/v1/entity/dedaluslabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dedalus Labs

- `compute/dedalus-labs` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T15:51:59.407Z (live) | stale on 2026-12-05
- url https://www.dedaluslabs.ai/pricing
- free tier: $20 of one-time sign-up credit with up to 4 vCPU, 16 GiB of RAM and 10 GiB of storage per machine | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: email: sign-up is held by Clerk and accepts an email address, Google or GitHub, with no phone number field and a password required; a first and last name are required fields, and the dashboard issues the API key. The Hobby offer states that no card is required, and no identity document is named.
- interface: rest, cli, ssh
- limits:
  - request-rate (binding): $0.04536 a vCPU-hour and $0.01458 a GiB-hour, billed only for active compute [1]
  - per-object-cap: 4 vCPU, 16 GiB of RAM and 10 GiB of storage per machine on the free plan [1]
  - retention-clamped: the $20 is one-time on the free plan; only the paid tier refills it monthly [1]
- interface detail: REST API at https://dcs.dedaluslabs.ai, a CLI, SDKs (TypeScript, Python, Go) and temporary SSH access
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and distinguishes the one-time $20 from the recurring $20 a month on the paid tier. The record carried the credit without the distinction, which is the difference between a trial and a tier
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 4
  - shape.ram: 16
  - shape.disk: 10
  - shape.note: the free plan's ceiling per machine
  - session_cap.restart_required: no
  - session_cap.note: billed only for active compute; the page states no session clock
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
  - ps.gib: 10
  - ps.price: 10 GiB free per machine on the free plan, 20 GiB on the paid one
  - ps.durability: machine storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$20 one-time sign-up credit.' on the free plan with 'vCPU / Machine Up to 4', 'RAM / Machine Up to 16 GiB' and 'Storage / Machine 10 GiB free', against '$20 of compute included every month' on the paid tier, quoted
  - [2] 2026-11-03: the machines are controlled through an HTTP API, a CLI and SDKs | capture: sha256:b32410d04fea25048cb1b616dc1047718fbb63831f1b6497c4fb7d805dfe4bf7 | quote: Use the production API at `https://dcs.dedaluslabs.ai` to control Machines. The command-line interface (CLI) and software development kits (SDKs) add `/v1` to that base URL
  - [2] 2026-11-03: SSH access to a machine is documented | capture: sha256:b32410d04fea25048cb1b616dc1047718fbb63831f1b6497c4fb7d805dfe4bf7 | quote: [SSH](https://docs.dedaluslabs.ai/dcs/dm/ssh.md): Open temporary Secure Shell (SSH) access.
  - [3] 2026-11-04: the sign-up form identifies a person by an email address, a GitHub account or a Google account | capture: sha256:110fc3417c9b8c2c4f6404465997b37e2c0058e759c8e1f42f152f895edfa1bb | quote: "identification_requirements":[["email_address","oauth_github","oauth_google"]
  - [3] 2026-11-04: the sign-up form has no phone number field | capture: sha256:110fc3417c9b8c2c4f6404465997b37e2c0058e759c8e1f42f152f895edfa1bb | quote: "phone_number":"off"
  - [1] 2026-11-04: the Hobby tier grants the credit with no card | capture: sha256:9d04b5825a8c4a9ece5f4cf6f042cd9e55a7cde55b1a111d5909ce9024c027b0 | quote: "description":"$20 one-time sign-up credit. No credit card required."
  - [1] 2026-11-04: the credit is granted at sign-up, to the account the sign-up form creates | capture: sha256:9d04b5825a8c4a9ece5f4cf6f042cd9e55a7cde55b1a111d5909ce9024c027b0 | quote: $20 one-time sign-up credit.
- sources:
  - [1] https://www.dedaluslabs.ai/pricing
  - [2] https://docs.dedaluslabs.ai/llms.txt
  - [3] https://clerk.dedaluslabs.ai/v1/environment
