# Revyl

> revyl.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/revyl/ | JSON https://fshy.ajam.dev/api/v1/entity/revyl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Revyl

- `compute/revyl` | qualifies-with-caveat | evidence documented | binding write-gated | category macOS host
- needs card no, phone no, ID no, institution no | verified 2026-11-24T13:21:02.388Z (live) | stale on 2026-12-25
- url https://www.revyl.com
- free tier: Free plan at USD 0 with up to 1,200 device minutes a month, 2 devices at once, and unlimited developers and agents; iOS, Android and web are included, while macOS requires adding a card | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: no egress allowance or per-GB price is stated; run state and Atlas maps are included on every plan and shared slots are isolated and wiped between sessions | metered: no | source: [1]
- identity: email | detail: A valid email and age 13 or older are required for an account; a card is needed only to move to Pro and unlock macOS computers. No phone or ID document is stated.
- interface: cli, rest, browser
- limits:
  - request-rate: runs execute against real iOS devices; the page states no quota [1]
  - write-gated (binding): the free path is a signup; the paid ladder is not rendered on this page [1]
- interface detail: CLI and API access on every plan, with a dashboard and Atlas for inspecting runs; a coding agent drives runs from the terminal
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and offers a free signup with device runs, but the plan table is not in the extracted body. The product is device time rather than a general machine
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: a cloud iOS device
  - shape.note: an iPhone 15 on iOS 17.4 in the page's example
  - session_cap.restart_required: no
  - session_cap.note: a run is a scripted flow against a device, not a machine held open
  - free_tier_kind: allowance
  - ps.price: run state is committed to Atlas and replayable
  - ps.durability: recorded run and device state
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the run record
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Give your coding agent an iPhone.' with '`revyl run checkout-flow --device ios`' and a recorded run showing device, streaming and state committed, plus 'Start free', quoted; no plan or price is rendered
  - [1] 2026-11-18: not stated | capture: sha256:85204d72784d4c99c0680fede3782aa9f31e247967cfc8cd6d940ff76e46ad66 | quote: # One record of how your software behaves
  - [2] 2026-11-24: the Free plan includes up to 1,200 device minutes every month | capture: sha256:39e125a6359b93ee97f343dfe94c7bf825487b3e674aff2525c2f1e0c03bbdc0 | quote: Free device minutes every month | Up to 1,200
  - [2] 2026-11-24: the free allowance is metered in device minutes | capture: sha256:39e125a6359b93ee97f343dfe94c7bf825487b3e674aff2525c2f1e0c03bbdc0 | quote: Free device minutes every month | Up to 1,200
  - [2] 2026-11-24: device usage is billed by elapsed minutes | capture: sha256:39e125a6359b93ee97f343dfe94c7bf825487b3e674aff2525c2f1e0c03bbdc0 | quote: Every platform, billed by the minute
  - [3] 2026-11-24: shared devices are isolated and erased between sessions; no egress price is published | capture: sha256:a6ac5db44932eed99887d80d6a28e277f84d7fdf91d5e338ea4934596a7a94cd | quote: Between user sessions, Revyl wipes important directories in the assigned user space, destroys the simulator, and recreates a fresh erased simulator before the next session.
  - [2] 2026-11-24: every plan includes CLI and API access, and the service is driven from a dashboard | capture: sha256:39e125a6359b93ee97f343dfe94c7bf825487b3e674aff2525c2f1e0c03bbdc0 | quote: CLI & API access | Included | Included | Included
  - [2] 2026-11-24: CLI and API access are included on the Free plan | capture: sha256:39e125a6359b93ee97f343dfe94c7bf825487b3e674aff2525c2f1e0c03bbdc0 | quote: CLI & API access | Included | Included | Included
  - [4] 2026-11-24: sign-up requires a valid email and age 13 or older | capture: sha256:00458abf82cf8b08ed00895720edb6930029ac3989e0571fd90b298de829b263 | quote: To use the Services, You must first set up an Account by providing a valid email. You must be a human with an age 13 or older.
  - [4] 2026-11-24: the account gate is a valid email and minimum age 13 | capture: sha256:00458abf82cf8b08ed00895720edb6930029ac3989e0571fd90b298de829b263 | quote: To use the Services, You must first set up an Account by providing a valid email. You must be a human with an age 13 or older.
  - [2] 2026-11-24: the Free plan is USD 0 and the Pro rate is USD 0.075 per device minute on iOS and Android | capture: sha256:39e125a6359b93ee97f343dfe94c7bf825487b3e674aff2525c2f1e0c03bbdc0 | quote: Free $0 | Pro $0.075 per device minute on iOS and Android | Enterprise Custom
  - [1] 2026-11-24: the product is a screen-level annotation and test-automation service driven from a dashboard | capture: sha256:e398a35b87834bcffbb993e3bfb6b5cb58a3e24fe8a753cc631547f683bd168a | quote: Talk on the screenComment on the exact screen and @mention the teammate who needs to see it.
- sources:
  - [1] https://www.revyl.com
  - [2] https://www.revyl.com/pricing
  - [3] https://www.revyl.com/security/shared-simulator-capacity/
  - [4] https://www.revyl.com/terms
