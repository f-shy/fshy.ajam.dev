# Inference Cooperative

> inference.coop | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inference-2/ | JSON https://fshy.ajam.dev/api/v1/entity/inference-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Inference Cooperative

- `inference/inference-coop` | paid-only | evidence documented | binding volume-quota | category member-governed inference cooperative, paid membership
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://inference.coop
- free tier: no free tier: membership dues are a sliding scale starting at USD 5 per month; every member gets a USD 15 monthly credit for chat and API regardless of what they pay; credits never expire and carry over | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: membership requires joining the cooperative and paying sliding-scale dues starting at USD 5 per month; the signup fields are not stated on the apex page
- interface: rest
- limits:
  - volume-quota (binding): USD 15 monthly chat and API allowance for every member; extra credit packs can be bought and never expire [1]
- binding note: the allowance requires a paid membership, so dues bind first
- endpoint: https://gateway.inference.coop/v1
- tooling: an OpenAI-compatible gateway key available to members, plus a web chat
- composes with: pairs with an OpenAI-compatible agent through a paid membership; the USD 15 monthly credit binds first
- reliability: no reliability event recorded
- notes: the 'fair price' framing is a paid membership, not a free tier; a fixed USD 15 allowance is granted to all members.
- evidence:
  - [1] 2026-11-18: sliding-scale dues from USD 5 per month, every member gets USD 15 monthly credit | capture: sha256:e98f4dc2ac3dd34865e6fe6a47342666fe793655a397d149f54e12f811ea3a41 | quote: Dues are a sliding scale starting at $5 a month — you choose the amount that fits your circumstances. Every member gets the same allowance: a $15 monthly credit for chat and API, whatever they pay.
- sources:
  - [1] https://inference.coop
