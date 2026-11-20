# QVAC

> npmjs.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/npmjs-package/ | JSON https://fshy.ajam.dev/api/v1/entity/npmjs-package.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## QVAC

- `inference/qvac` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category local-first P2P AI runtime provider (self-hosted)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://www.npmjs.com/package/@qvac/ai-sdk-provider
- free tier: QVAC is an open-source local-first peer-to-peer AI runtime; models run on the user's own hardware through qvac serve --openai; no hosted inference is offered and no per-token charge applies, but the reader supplies the hardware | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no account; the runtime is installed and run locally on the user's machine
- interface: rest
- binding note: no hosted quota; the constraint is local hardware
- tooling: the @qvac/ai-sdk-provider package, qvAC CLI and a local qvac serve --openai endpoint
- composes with: pairs with the Vercel AI SDK against a local runtime; the scarce link is the user's own hardware, not a hosted service
- reliability: no reliability event recorded
- notes: self-hosted last resort: a local-first P2P runtime with no hosted inference capacity of its own.
- self hosted: yes
- evidence:
  - [1] 2026-11-18: QVAC is a local-first peer-to-peer runtime running on the user's hardware | capture: sha256:50448042c4c9e3333082954ea93a982e0590e1155ee6937f8f68a59e4937c27f | quote: QVAC is an open-source, cross-platform ecosystem for local-first, peer-to-peer AI — LLMs, embeddings, transcription, translation, speech, OCR, and image generation, all running on the user's own hardware.
- sources:
  - [1] https://www.npmjs.com/package/@qvac/ai-sdk-provider
