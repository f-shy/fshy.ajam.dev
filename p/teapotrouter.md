# Teapot Router

> teapotrouter.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/teapotrouter/ | JSON https://fshy.ajam.dev/api/v1/entity/teapotrouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Teapot Router

- `inference/teapot-router` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://teapotrouter.com/en/docs/billing
- free tier: No self-serve standing free tier is published: a small amount of test credit can be added by the platform administrator on request, and otherwise the user pays online at the displayed minimum. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: verify email and set a password to open a workspace; test credit needs an administrator
- interface: rest
- limits:
  - volume-quota (binding): administrator-granted test credit, otherwise online top-up at a displayed minimum [1]
- endpoint: https://api.teapotrouter.com/v1
- composes with: the administrator-granted test credit is the only free route
- reliability: test credit is discretionary and not a self-serve route
- evidence:
  - [1] 2026-11-18: free test credit is granted administratively rather than offered self-serve | capture: sha256:488761f7e26515354e9fce280b59a213997fc3d8e85a04f596e316db9eb1881d | quote: ask the platform administrator to add a small amount of test credit to your account
- sources:
  - [1] https://teapotrouter.com/en/docs/billing
