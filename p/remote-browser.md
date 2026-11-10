# Remote Browser

> remote-browser.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/remote-browser/ | JSON https://fshy.ajam.dev/api/v1/entity/remote-browser.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Remote Browser

- `compute/remote-browser` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:20.763Z (live) | stale on 2026-12-05
- url https://remote-browser.dev/pricing
- free tier: 1 browser-hour a month on Free with no card; $4.90/mo buys 30 browser-hours | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://remote-browser.dev/pricing meters active browser-hours and lists no data-transfer allowance or price | metered: no | source: [1]
- identity: email | detail: 'No card required', quoted from the pricing page read 2026-10-22
- interface: rest
- limits:
  - request-rate (binding): 1 browser-hour a month on Free; 30 browser-hours a month on the $4.90 tier [1]
- interface detail: a REST API (POST create session, GET status) that returns a CDP WebSocket URL for Playwright, Puppeteer or browser-use, plus a console
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The free allowance is one browser-hour a month, which at a 24/7 duty cycle is 0.14% of the month - the figure that decides it
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: the free allowance is one browser-hour in total a month, so a single session cannot exceed it
  - free_tier_kind: allowance
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'No card required. Includes 1 browser-hour every month.' and 'Included runtime 1 browser-hour / month 30 browser-hours / month', quoted
  - [1] 2026-11-03: metering is browser-hours; no transfer figure is listed | capture: sha256:ef1b400a0547b1ff5921accec7cd855e14024c2465150d475939cc53afed917f | quote: Remote Browser pricing is based on active browser-hours: the time a cloud Chromium session is alive and available to your agent or automation script.
  - [2] 2026-11-03: a REST API creates sessions | capture: sha256:166dd3c5c407005150136f760c45690dd9d13edc517c5c5370a288f64a240cbc | quote: POST a browser request with API-key auth and the runtime options your workflow needs.
  - [2] 2026-11-03: API plus CDP | capture: sha256:166dd3c5c407005150136f760c45690dd9d13edc517c5c5370a288f64a240cbc | quote: Remote Browser exposes hosted Chromium as an API: create a session, connect over CDP, watch it live, reuse profile state, and terminate it when your job completes.
- sources:
  - [1] https://remote-browser.dev/pricing
  - [2] https://remote-browser.dev/cloud-browser-api
