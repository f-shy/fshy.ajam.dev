# Ferr

> ferr.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ferr/ | JSON https://fshy.ajam.dev/api/v1/entity/ferr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ferr

- `compute/ferr` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- identity a placeholder: card and phone unknown | verified 2026-11-06T17:48:23.920Z (live) | stale on 2026-12-07
- url https://ferr.dev/
- free tier: up to 50 browser hours a month with 3 concurrent sessions on the free tier | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the page read states no egress allowance and no overage price per TB | metered: no | source: [1]
- identity: email | detail: unverified: behind a sign-up. The sign-up host https://app.ferr.dev/ did not resolve on 2026-11-06 (DNS failure), so the form's fields, and whether it asks for a card or a phone, were not read; https://docs.ferr.dev/ also did not resolve. The vendor's page states only 'Start For Free' and a browser-hour allowance (https://ferr.dev/). Country: not published at https://ferr.dev/.
- interface: rest
- limits:
  - request-rate (binding): 50 browser hours a month on the free tier; 3 concurrent sessions [1]
  - write-gated: the self-hosted CLI path runs the browser on the user's own machine and is a different product from the hosted hours. [1]
- interface detail: Sessions API, Chrome DevTools Protocol, SDKs for Python, Node, Rust and Go; a ferr CLI that runs the open-source browser on the user's own machine
- tooling: Sessions API plus CDP; Python, Node, Rust and Go SDKs
- composes with: not established
- reliability: no reliability event recorded
- notes: The free tier is metered in browser hours on the vendor's 'warm capacity', not on a machine the user supplies.
- evidence note: 50 hours a month represents 6.8% of a 730-hour month, enabling duty-cycle evaluation.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the month's 50 hours is the bound; sub-second cold starts mean a session need not be held open
  - free_tier_kind: allowance
  - ps.price: profiles store cookies and local storage and are reused across sessions
  - ps.durability: saved profile
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until the profile is deleted
  - net.out: yes
  - net.in: no
  - net.allowance: rotating consumer-connection proxies and an unmarked browser profile mode included
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start free, scale when you do' with 'Up to 50 browser hours / mo' and '3 concurrent sessions' on the free tier, and 'Sub-second cold starts on warm capacity', quoted
  - [1] 2026-11-03: the pricing section meters browser hours and states no egress allowance or overage price | capture: sha256:cccb413be4152e99ba64085a886b467e0c95e441b7cb300a852185951c91af3e | quote: Up to 50 browser hours / mo
  - [1] 2026-11-03: sessions are created over a Sessions API and driven by SDK or CDP | capture: sha256:cccb413be4152e99ba64085a886b467e0c95e441b7cb300a852185951c91af3e | quote: Create a session, get a live browser in the cloud, and drive it with the SDK or plain Chrome DevTools Protocol.
  - probe:https://app.ferr.dev/ 2026-11-04: the sign-up host did not resolve, so the form was not read | capture: sha256:213f11faf5cfae0ac7ada3bf46e61f6f2c90d6b4690bbb459c35eec2dc7469ee | quote: "status": null
  - [1] 2026-11-04: the free tier needs an account, whose form was not read | capture: sha256:b5a4b796ff5cebcf9ee9d5f3e01b3c402d4518602ec37deab22956260a7b8394 | quote: Create a free account and launch your first cloud browser in under a minute.
  - probe:https://app.ferr.dev/ 2026-11-06: the sign-up host did not resolve, so its form was not read | capture: sha256:2bc7c16f6c2b0bc951648a15472414ba369c800e55bafcad0b4d628538e13370 | quote: "status": null
  - [1] 2026-11-06: the free tier's only entry is a link to the sign-up host that does not resolve | capture: sha256:a33bdaf5a6f06263367620168fbf6709f2c0df4504a88bd4d79e5408efe6d9a3 | quote: Start For Free
  - [1] 2026-11-06: the free tier is 50 browser hours a month | capture: sha256:a33bdaf5a6f06263367620168fbf6709f2c0df4504a88bd4d79e5408efe6d9a3 | quote: Up to 50 browser hours / mo
  - probe:https://docs.ferr.dev/ 2026-11-06: the documentation host did not resolve either | capture: sha256:44f72858bc2a7a1da5c7b63b4a6b9dc8575e0252ea356e85f3a9bf871eebf69a | quote: "status": null
- sources:
  - [1] https://ferr.dev/
