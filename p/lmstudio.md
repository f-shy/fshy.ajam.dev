# LMStudio

> lmstudio.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lmstudio/ | JSON https://fshy.ajam.dev/api/v1/entity/lmstudio.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LMStudio

- `inference/lmstudio` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category local inference app (self-hosted)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://lmstudio.ai
- free tier: the app downloads and runs local models on the user's own hardware; the local endpoint serves them free of per-token charges; LM Studio also lists 9 cloud models on its catalog but those are separate paid offers | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no account is needed for local models; the app is downloaded and runs on the user's machine
- interface: rest
- binding note: local inference has no hosted quota; the constraint is the user's machine
- endpoint: http://127.0.0.1:1234/v1
- tooling: the LM Studio desktop app (Bionic agent) and a local OpenAI-compatible endpoint at 127.0.0.1:1234/v1
- composes with: pairs with an agent through the local endpoint only; the scarce link is the hardware the reader supplies
- reliability: no reliability event recorded
- notes: record for the LMStudio offer; verdict qualifies-with-caveat, confidence documented
- self hosted: yes
- evidence:
  - [1] 2026-11-18: the app is local and natively runs open models | capture: sha256:20aad08c91f54b2a7fea6cd5af8193e1ef08f1b9405efaffa5034efb653a8511 | quote: Natively local. Built for creativity, work, and code.
- sources:
  - [1] https://lmstudio.ai
