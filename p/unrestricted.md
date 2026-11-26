# Unrestricted

> unrestricted.sh | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unrestricted/ | JSON https://fshy.ajam.dev/api/v1/entity/unrestricted.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Unrestricted

- `inference/unrestricted` | trial-only | evidence documented | binding volume-quota | category inference gateway (abliterated models)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://unrestricted.sh/pricing
- free tier: New accounts start with $0.50 of credit for the chat, which expires if it is not used within 72 hours. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an account; API keys work with the welcome credit and no top-up
- interface: rest
- limits:
  - volume-quota (binding): USD 0.50 welcome credit expiring after 72 hours; 3 requests at once; a USD 0.01 wake fee when a model was idle [1]
- endpoint: https://api.unrestricted.sh/v1
- composes with: The credit expires, so this is a trial rather than a standing free tier.
- reliability: a wake fee of USD 0.01 is charged when a sleeping GPU is woken
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Unrestricted grants USD 0.50 of welcome credit that expires after 72 hours | capture: sha256:be58c99cd238d6dafe39ac79e7536394d751232f28179eea398de4bf42216914 | quote: New accounts start with $0.50 of credit for the chat, which expires if it is not used within 72 hours.
- sources:
  - [1] https://unrestricted.sh/pricing
