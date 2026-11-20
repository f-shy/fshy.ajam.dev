# Butter

> butter.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/butter/ | JSON https://fshy.ajam.dev/api/v1/entity/butter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Butter

- `compute/butter` | self-hosted, last resort | verdict paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-30T00:03:24.484Z (live) | stale on 2026-11-30
- url https://butter.dev
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no hosted service is offered: the runtime embeds in the user's own process, so there is no capacity to rent. [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Paid-only rather than dead: the product is sold and reachable. Self-hosted: the bVisor runtime embeds in the user's own local process, with no VM or remote infrastructure.
- evidence note: the site was read on 2026-10-22 and offers a local runtime rather than hosted compute. There is no plan and no price, which is the record's claim, and the reason is that the product is not a host
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the sandbox's lifetime is the client process's lifetime
  - network_out.in: no
  - network_out.ports: none
  - network_out.static_ip: no
  - network_out.ipv6: no
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Butter is building bVisor, an incredibly lightweight sandbox runtime for AI agents. It embeds directly into your local process, providing a safe bash environment without the overhead of VMs or remote infra.' quoted; no hosted service or price is offered
  - [1] 2026-10-29: the bVisor sandbox runtime embeds in the client's local process, with no remote infrastructure | capture: sha256:de31a70de0f66453b8cc8bf88d22aee69147d632a82e2d64094f26e42a6a758b | quote: It embeds directly into your local process, providing a safe bash environment without the overhead of VMs or remote infra.
- sources:
  - [1] https://butter.dev
