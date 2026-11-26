# Atomic Chat

> atomic.chat | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/atomic/ | JSON https://fshy.ajam.dev/api/v1/entity/atomic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Atomic Chat

- `inference/atomic-chat` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category local desktop inference app (self-hosted)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://atomic.chat
- free tier: the app is free and local: unlimited messages, no rate limits, no subscription, no cloud, 0 bytes of data leave the device; it runs on the user's own hardware | unit: unlimited | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no account is needed; the app is downloaded and runs locally
- interface: rest
- limits note: no rate limits, no caps, no subscription; runs fully offline on the device
- binding note: no hosted quota binds; the constraint is hardware the reader supplies
- endpoint: http://127.0.0.1:1337/v1
- tooling: a local desktop app (macOS, Windows, Linux, iOS, Android) exposing a 127.0.0.1 OpenAI-compatible endpoint
- composes with: pairs with an agent through the local endpoint only; the scarce link is the user's own hardware, not a hosted service
- reliability: fully offline; no vendor-side suspension or throttling applies to the local app
- notes: record for the Atomic Chat offer; verdict qualifies-with-caveat, confidence documented
- self hosted: yes
- evidence:
  - [1] 2026-11-18: unlimited local messages, no rate limits, no subscription, no cloud | capture: sha256:08df26411edc09a479211e60b65d59f71b2781a3f621c8a4964f9af32c450320 | quote: messages, no rate limits, no caps
- sources:
  - [1] https://atomic.chat
