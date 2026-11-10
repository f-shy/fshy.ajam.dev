# Bytebot

> bytebot.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bytebot/ | JSON https://fshy.ajam.dev/api/v1/entity/bytebot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bytebot

- `compute/bytebot` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T15:51:56.486Z (live) | stale on 2026-12-05
- url https://www.bytebot.ai/
- free tier: the software is free and open source under Apache 2.0 with no licensing fee, subscription or usage limit; the only cost is the machine it runs on and the model API key | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not applicable: the software runs in Docker on infrastructure the user supplies, so the vendor meters no traffic and states no allowance or overage | metered: no | source: [1]
- identity: anonymous | detail: none at Bytebot, which issues no account: the stack is run by the user from Docker Compose and its prerequisites are Docker, Docker Compose, memory and an 'AI API key from one of these providers'. The site states 'no credit card required' and 'Bytebot itself is completely free and open source under the Apache 2.0 license'. The model provider behind the key does need an account of its own.
- interface: rest
- limits:
  - write-gated (binding): the free product is a repository run in Docker with its own model API key; there is no hosted capacity [1]
- interface detail: a REST API and a task API
- tooling: the user installs and runs the Docker compose stack on a rented or free machine and supplies a model API key; the REST API drives tasks
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the Apache 2.0 licence and that there is no usage limit. 'No usage limit' is a claim about an absent sentence, and the record keeps it as the unit unlimited rather than multiplying it
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the container runs locally; no vendor clock
  - free_tier_kind: allowance
  - ps.price: local disk
  - ps.durability: the local machine
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.max_retention: as long as it is kept
  - net.out: yes
  - net.in: no
  - net.ports: a local desktop and API
  - net.static_ip: no
  - net.ipv6: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Bytebot itself is completely free and open source under the Apache 2.0 license. Your only costs are:' ... 'There are no Bytebot licensing fees, subscription costs, or usage limits.' and 'no credit card required', quoted
  - [2] 2026-11-04: a REST API exists | capture: sha256:87cebcbbd06b625d3bff25f5d5ef75c6c81595254a49a9dfe6abd9cb58e8310b | quote: * REST APIs for programmatic control
  - [1] 2026-11-04: Bytebot runs on infrastructure the user supplies | capture: sha256:b0ccce2811dc514ff65c7a8df9d31cfab728a7003673fc31f67ed87f5dfac9ab | quote: Bytebot is completely self-hosted on your own infrastructure, meaning your data never leaves your servers.
  - [3] 2026-11-04: the only credential the stack needs is a model provider's API key; Bytebot itself issues no account | capture: sha256:7f4079b54164be68d3fa4b7fee52f31e80249589508fd27450f6d36179186866 | quote: AI API key from one of these providers
  - [1] 2026-11-04: the start page names no card requirement | capture: sha256:b0ccce2811dc514ff65c7a8df9d31cfab728a7003673fc31f67ed87f5dfac9ab | quote: no credit card required.
  - [1] 2026-11-04: the software is a free open-source download with no licence account | capture: sha256:b0ccce2811dc514ff65c7a8df9d31cfab728a7003673fc31f67ed87f5dfac9ab | quote: Bytebot itself is completely free and open source under the Apache 2.0 license.
- sources:
  - [1] https://www.bytebot.ai/
  - [2] https://docs.bytebot.ai
  - [3] https://docs.bytebot.ai/quickstart.md
