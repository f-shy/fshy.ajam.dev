# Autarcho

> autarcho.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/autarcho/ | JSON https://fshy.ajam.dev/api/v1/entity/autarcho.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Autarcho

- `inference/autarcho` | paid-only | evidence documented | binding volume-quota | category inference marketplace
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://autarcho.com/use/
- free tier: No standing free tier. Credit is bought with USDC on Solana; card payments are not supported in this release. Trial keys are issued directly during the preview. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no signup; a key is generated locally and only its hash is stored; the stored balance is lost with the key
- interface: rest
- limits:
  - volume-quota (binding): credit bought with USDC on Solana; trial keys issued directly during the preview [1]
- endpoint: https://api.autarcho.com/v1
- tooling: an OpenAI-compatible base URL with a locally generated ak_ key; text only with streaming, tool calls and JSON mode
- composes with: the USDC-on-Solana top-up and the invite-only trial key are the scarce links
- reliability: no operator online for a model means it is not offered; a request priced above max_price_per_token_micro_usdc is refused before any charge
- notes: no public standing free inference allowance; the only free route is a trial key issued directly during the preview, and the general service requires a USDC-funded balance
- evidence:
  - [1] 2026-11-18: there is no signup; a key is generated on the device and only its hash is stored; topping up needs USDC on Solana | capture: sha256:907280a5924592af202ca4e7e4b3d2fcaf46905e16b9ba46b78f4ffeb058bc71 | quote: No. There is no signup. A key is made on your device and only a hash of it is stored, so nobody can show it to you again.
- sources:
  - [1] https://autarcho.com/use/
