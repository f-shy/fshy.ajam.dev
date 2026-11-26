# HUMAIN

> humain.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/humain/ | JSON https://fshy.ajam.dev/api/v1/entity/humain.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HUMAIN

- `inference/humain` | fails-identity | evidence documented | binding write-gated | category inference API
- needs card no, phone no, ID no, institution yes | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://www.humain.com/en/node.html
- free tier: No self-serve free tier; HUMAIN Node is 'available in limited preview. Access is granted by request' and usage is 'pay as you go with prepaid credits'. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: institution | detail: access granted by request form; identity and organization details required by the preview
- interface: rest
- limits:
  - write-gated (binding): limited preview, access by request form [1]
- endpoint: https://api.node.humainaic.com/v1
- tooling: OpenAI-compatible client pointed at the Node base URL
- composes with: no self-serve route; access requires an approved request and prepaid credits
- notes: No self-serve free route: access is by request and paid with prepaid credits. The models.dev api host (api.node.humainaic.com) differs from the documented base (api.node.humain.com/v1).
- evidence:
  - [1] 2026-11-18: Node is a limited preview with access by request and pay-as-you-go credits | capture: sha256:48c8d87a02db2fa6e426b350259896d4e6e564027aaa0e8569e3073ada71907b | quote: HUMAIN Node is available in limited preview. Access is granted by request
- sources:
  - [1] https://www.humain.com/en/node.html
