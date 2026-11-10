# StackBlitz WebContainers

> stackblitz.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stackblitz/ | JSON https://fshy.ajam.dev/api/v1/entity/stackblitz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StackBlitz WebContainers

- `compute/webcontainers` | qualifies-with-caveat | evidence documented | binding write-gated | category dev environment
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:14.688Z (live) | stale on 2026-12-05
- url https://stackblitz.com/pricing
- free tier: a free Personal plan with unlimited public projects and repositories; a GitHub account is needed to save work or collaborate | unit: unlimited | metered on: identity-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page and FAQ state no egress, bandwidth or data-transfer term | metered: no | source: [1]
- identity: email | detail: 'you do need a GitHub account to save your work or collaborate with others', quoted from stackblitz.com/pricing read 2026-10-22
- interface: unknown
- limits:
  - request-rate: unlimited public projects on the free Personal plan [1]
  - write-gated (binding): a GitHub account is required to save work or collaborate; anonymous use is view-and-edit only [1]
- interface detail: a JavaScript API (@webcontainer/api, npm) that boots the runtime inside a browser page; no REST API, CLI or SSH is documented on the pages read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: Pricing documentation read on 2026-10-22 confirms free plan terms and GitHub account requirements. Free usage permits unlimited projects subject to identity verification.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a WebContainer runs in the browser tab; closing it ends the session
  - free_tier_kind: allowance
  - ps.price: the project is the storage
  - ps.durability: the project in a GitHub repository
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the repository exists
  - net.out: no
  - net.in: no
  - net.ports: none: the container runs in the browser
  - net.static_ip: no
  - net.ipv6: no
  - net.allowance: network access is limited inside the WebContainer
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'The free Personal plan includes unlimited public StackBlitz projects and Github repositories.' and 'you do need a GitHub account to save your work or collaborate with others', quoted
  - [1] 2026-11-03: the pricing page states the free plan contents and gives no egress or bandwidth term | capture: sha256:8a18aadc0960324dc81a33cab9ea3f2268cd26567611a61380db8b083ca73eb2 | quote: What is included in the free Personal plan? The free Personal plan includes unlimited public StackBlitz projects and Github repositories.
  - [2] 2026-11-03: the runtime is driven through a JavaScript package that boots inside a browser page | capture: sha256:0bd4a106c0b3019688788807fa857faa42e5700c3c5919c1812c3a1650b0f135 | quote: npm i @webcontainer/api
- sources:
  - [1] https://stackblitz.com/pricing
  - [2] https://webcontainers.io/guides/quickstart
