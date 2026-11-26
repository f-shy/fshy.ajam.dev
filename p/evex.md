# evex storage

> evex.land | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/evex/ | JSON https://fshy.ajam.dev/api/v1/entity/evex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## evex storage (storage.evex.land)

- `storage/evex-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:36.465Z (inherited) | stale on 2026-12-04
- url https://storage.evex.land/upload
- free tier: Unlimited storage stated on the service's own page; the upload form posts to /upload and no byte quota is published. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Genuine unknown that turned out broken. A Hono service whose own page says 'Unlimited storage', with a published SDK (raicdev/evex-storage-sdk). But the upload endpoint refuses every form I.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Genuine unknown that turned out broken. A Hono service whose own page says 'Unlimited storage', with a published SDK (raicdev/evex-storage-sdk) — but the upload endpoint refuses every form…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Genuine unknown that turned out broken. A Hono service whose own page says 'Unlimited storage', with a published SDK (raicdev/evex-storage-sdk) — but the upload endpoint refuses every form…
  - [2] 2026-10-21: cited as the basis of the rejection: Genuine unknown that turned out broken. A Hono service whose own page says 'Unlimited storage', with a published SDK (raicdev/evex-storage-sdk) — but the upload endpoint refuses every form I
  - [3] 2026-10-21: cited as the basis of the rejection: Genuine unknown that turned out broken. A Hono service whose own page says 'Unlimited storage', with a published SDK (raicdev/evex-storage-sdk) — but the upload endpoint refuses every form I
  - probe:https://storage.evex.land/ 2026-11-19: the service's own page states unlimited storage | capture: sha256:a7df62ea82243224c1e8d2bd7586002c1f1d64526de15e321d11519fa0232ff2 | quote: <h1 class="css-717032843"><span class="css-3143954287">Evex Storage</span><span class="css-1692308125">Unlimited storage</span></h1>
  - probe:https://storage.evex.land/ 2026-11-19: the first-party page is live and still states unlimited storage | capture: sha256:a7df62ea82243224c1e8d2bd7586002c1f1d64526de15e321d11519fa0232ff2 | quote: <h1 class="css-717032843"><span class="css-3143954287">Evex Storage</span><span class="css-1692308125">Unlimited storage</span></h1>
  - probe:https://storage.evex.land/upload 2026-11-19: a bare GET of the upload endpoint answered HTTP 404; the page's upload form posts a file to it | capture: sha256:816fb4a7888576125d97439b55209b9adb1125cd9f728fcfd83a5cd97566f918 | quote: "status": 404
- sources:
  - [1] https://storage.evex.land/upload
  - [2] https://storage.evex.land/
  - [3] https://github.com/raicdev/evex-storage-sdk
