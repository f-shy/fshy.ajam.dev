# Zeldoc

> zeldoc.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zeldoc/ | JSON https://fshy.ajam.dev/api/v1/entity/zeldoc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zeldoc

- `inference/zeldoc` | fails-identity | evidence documented | binding write-gated | category inference gateway (invitation only)
- needs card no, phone no, ID no, institution yes | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://docs.zeldoc.ai/connect-opencode
- free tier: Zeldoc.ai is currently invitation-only. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: institution | detail: an invitation or a key issued directly by the Zeldoc team is required; no public self-serve account
- interface: rest
- limits:
  - write-gated (binding): models available per key are determined by the account; no free allowance stated [1]
- endpoint: https://api.zeldoc.ai/v1
- composes with: The invitation gate is the finding: a reader without an invitation cannot obtain a key.
- reliability: not observed
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Zeldoc.ai access requires an invitation from the team, so there is no self-serve signup | capture: sha256:9c2da106ab062c8123cb15ed6bffd93a5a3dc3fb924c0a864bcd56a18ebd1435 | quote: Zeldoc.ai is currently invitation-only.
- sources:
  - [1] https://docs.zeldoc.ai/connect-opencode
