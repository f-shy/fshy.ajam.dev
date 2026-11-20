# Isle

> tryisle.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tryisle/ | JSON https://fshy.ajam.dev/api/v1/entity/tryisle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Isle

- `compute/isle` | qualifies-with-caveat | evidence documented | binding write-gated | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-03T01:29:48.708Z (live) | stale on 2026-12-04
- url https://www.tryisle.com/
- free tier: Free plan at $0 per month: 5 environment-hours/month, 30 minute environment runtime, 1 concurrent environment, KiCad and FreeCAD (https://www.tryisle.com/, read 2026-10-30) | unit: hours | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: The Developer plan at $29 per month includes 100 environment-hours/month, no per-session runtime cap and 5 concurrent environments; stopping an environment archives it with its files and pauses billing.
- per-object cap: Individual uploads and downloads are limited to 4 MiB. | bytes: 4194304 | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: Sign-up is the login page that the Free plan's 'Start free' button opens: 'Continue with GitHub', or an email address with a sign-in code; the page has no card or phone field. An API key is then created in the dashboard. Whether a card or a phone number is asked after sign-in is unverified: behind a sign-up.
- interface: rest
- limits:
  - write-gated (binding): the Free plan allows 1 concurrent environment, each running for at most 30 minutes; access is through the Python SDK or the REST API with an API key [1]
- interface detail: a REST API authenticated with a Bearer API key on every request, and the Python SDK isle-sdk over it, with screenshot, mouse, keyboard and file-transfer calls
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the home page and the documentation were read on 2026-10-30: the home page publishes a Free plan of 5 environment-hours a month with a 30 minute runtime and 1 concurrent environment, and the documentation gives GitHub or email sign-up and access by API key
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.wall_clock_min: 30
  - session_cap.restart_required: no
  - session_cap.note: the Free plan's environment runtime is 30 minutes and the Developer plan has no per-session runtime cap; artifact checkpoints restore state
  - persistent_storage.price: not stated
  - persistent_storage.durability: artifact checkpoint
  - persistent_storage.on_stop: yes
  - persistent_storage.on_destroy: no
  - persistent_storage.max_retention: the checkpoint
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Save an artifact checkpoint before important actions, then restore it when needed' and 'Isle keeps that work in one desktop session, with screenshots and results returned to the agent after each step', quoted; the page publishes no plan or price
  - [1] 2026-10-30: the Free plan includes 5 environment-hours a month | capture: sha256:f55afdd403f14371dcae8d89df86052206c328884451935d6c5662e4e1e51cae | quote: 5 environment-hours/month
  - [1] 2026-10-30: the Developer plan includes 100 environment-hours a month | capture: sha256:f55afdd403f14371dcae8d89df86052206c328884451935d6c5662e4e1e51cae | quote: 100 environment-hours/month
  - [2] 2026-10-30: a stopped sandbox keeps its files and stops billing | capture: sha256:39900f4e3d49352db2f96f974aa6d8b5dd52a9b1f94ae345f0d24f4bc40d54ff | quote: # Stop archives the sandbox. Files persist, billing pauses.
  - [1] 2026-10-30: a Free plan environment runs for at most 30 minutes | capture: sha256:f55afdd403f14371dcae8d89df86052206c328884451935d6c5662e4e1e51cae | quote: * 30 minute environment runtime
  - [2] 2026-10-30: one file transfer is capped at 4 MiB | capture: sha256:39900f4e3d49352db2f96f974aa6d8b5dd52a9b1f94ae345f0d24f4bc40d54ff | quote: Individual uploads and downloads are limited to 4 MiB.
  - [2] 2026-10-30: sign-up is with GitHub or an email address, then an API key is created in the dashboard | capture: sha256:39900f4e3d49352db2f96f974aa6d8b5dd52a9b1f94ae345f0d24f4bc40d54ff | quote: Continue with GitHub or email at [tryisle.com](https://www.tryisle.com/login), then create an API key in the [dashboard](https://www.tryisle.com/api-keys).
  - [3] 2026-10-30: the REST API takes a Bearer API key on every request | capture: sha256:3d9c225d793c76799bc6e93713ed8c86a53a49327eb672a1800cf9fdecd4d00b | quote: Authentication: `Authorization: Bearer isle_...` on every API request.
  - [4] 2026-11-03: the sign-in page creates an account on first sign-in and shows only GitHub or email sign-in | capture: sha256:fe57279f0104a24f31a020e9a30a39362905a7157e1592e5f1652091fe84c977 | quote: New here? We'll create your account automatically.
  - [4] 2026-11-03: the email route is a sign-in code sent to the address, with no phone or card step on the page | capture: sha256:fe57279f0104a24f31a020e9a30a39362905a7157e1592e5f1652091fe84c977 | quote: Send sign-in code
  - [1] 2026-11-03: the Free plan button on the home page opens the login page with plan=free | capture: sha256:f55afdd403f14371dcae8d89df86052206c328884451935d6c5662e4e1e51cae | quote: [Start free](https://www.tryisle.com/login?plan=free)
  - [1] 2026-11-03: the Free plan is still published at 5 environment-hours a month | capture: sha256:f55afdd403f14371dcae8d89df86052206c328884451935d6c5662e4e1e51cae | quote: 5 environment-hours/month
- sources:
  - [1] https://www.tryisle.com/
  - [2] https://www.tryisle.com/docs
  - [3] https://www.tryisle.com/llms-full.txt
  - [4] https://www.tryisle.com/login
