# orkestr Sandboxes

> orkestr.eu | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/orkestr/ | JSON https://fshy.ajam.dev/api/v1/entity/orkestr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## orkestr Sandboxes

- `compute/orkestr` | qualifies-with-caveat | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:26.616Z (live) | stale on 2026-12-05
- url https://orkestr.eu/sandboxes
- free tier: free to start with no credit card, on per-second CPU and memory billing with no minimums and no platform fee; a sandbox's rootfs is dropped on terminate | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Three per-sandbox network modes: off (default, no outbound), restricted (allowlist) and open (full egress, paid tier with verified billing); no egress allowance or overage price is published on the sandbox pages. | metered: no | source: [1]
- identity: email | detail: 'Free to start, no credit card', quoted from orkestr.eu/sandboxes read 2026-10-22
- interface: rest
- limits:
  - request-rate: per-second CPU and memory, with no minimums, no per-request charge and no platform fee [1]
  - retention-clamped (binding): terminating drops the rootfs; snapshot storage is billed on the same invoice [1]
  - per-object-cap: each sandbox gets its own kernel and rootfs, with hardware-virtualised isolation [1]
- interface detail: REST API at https://api.orkestr.eu/v1 with a Bearer token minted in the orkestr console, documented at orkestr.eu/docs/sandboxes/api-reference; Python and JS SDKs wrap it.
- tooling: the orkestr Python SDK and JS SDK (docs at orkestr.eu/docs/sandboxes/python-sdk and /js-sdk), or the REST API directly from any language.
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the sandboxes page was read on 2026-10-22 and states the no-card start, the per-second model and what terminate does. The free amount is not published, so the record does not invent one
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: cold boot in roughly 150 ms and under 30 ms from a warm pool; the page states no idle reap, and a terminated sandbox loses its rootfs
  - free_tier_kind: allowance
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.price: snapshot storage billed per second on the same bill
  - ps.durability: rootfs, dropped on terminate; a snapshot survives
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until the snapshot is deleted
  - net.out: yes
  - net.in: yes
  - net.ports: port previews; the page states none
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free to start, no credit card. Spin up your first sandbox in seconds.' with 'Per-second pricing, no minimums. Pay for the CPU and memory you use, by the second. No charge per request, no monthly platform fee. Snapshot storage is on the same bill.' and 'each sandbox gets its own kernel and rootfs, dropped on terminate', quoted
  - [2] 2026-11-03: a REST API exists | capture: sha256:a72f684c2eee4ba10497f775de25f08f039f98dcf8a2f993f9ebb6db3f10e1f4 | quote: - `POST /v1/sandboxes` - create a sandbox
  - [1] 2026-11-03: open egress is a paid-tier mode; no price | capture: sha256:b151c62423b71b5e031e5f953c5baa43d676a8184d7e6e1a025cb0809f726227 | quote: open (full egress, paid tier with verified billing)
  - [2] 2026-11-04: the provider documents a REST API at api.orkestr.eu/v1 | capture: sha256:a72f684c2eee4ba10497f775de25f08f039f98dcf8a2f993f9ebb6db3f10e1f4 | quote: The sandbox REST API lives at `https://api.orkestr.eu/v1`.
  - [2] 2026-11-04: the provider documents Python and JS SDKs | capture: sha256:a72f684c2eee4ba10497f775de25f08f039f98dcf8a2f993f9ebb6db3f10e1f4 | quote: Use it directly from any language, or pick the [Python](https://orkestr.eu/docs/sandboxes/python-sdk) or [JS](https://orkestr.eu/docs/sandboxes/js-sdk) SDK
- sources:
  - [1] https://orkestr.eu/sandboxes
  - [2] https://orkestr.eu/docs/sandboxes/api-reference
