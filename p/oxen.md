# Oxen.ai

> oxen.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oxen/ | JSON https://fshy.ajam.dev/api/v1/entity/oxen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Oxen.ai (Oxen Hub — dataset versioning for ML)

- `storage/oxen-ai` | fails-quota | evidence reported | binding per-object-cap | category dataset-hosting
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.oxen.ai
- free tier: Explorer (free forever): 50 GB data storage + 50 GB data transfer, unlimited public repos with unlimited collaborators, 5 private repos (max 3 collaborators). Hacker $30/mo: 100 GB storage / 100 GB transfer. Pro $60/mo: 500 GB / 500 GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: No per-file cap published | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Hard-capped at 50 GB of data transfer per month on the free tier. Transfer allowances are exhausted quickly under continuous data retrieval. | metered: yes
- identity: email | detail: email (self-service signup).
- interface: rest, git, cli
- limits:
  - per-ip-shaping: transfer, unlimited public repos with unlimited collaborators, 5 private repos [1]
  - per-object-cap (binding): No per-file cap published [1]
- limits note: 50 GB storage, 50 GB/month transfer, 5 private repos. No per-file cap published. Public repos are unlimited in COUNT, which is the only multiplier. But the 50 GB is account-level, so repo count does not add bytes.
- interface detail: rest
- tooling: Genuine: `oxen` CLI (oxen add/commit/push/pull, merkle-tree diffing), Python SDK, and a documented REST API. The oxen-server is open source and self-hostable (Oxen positions itself as 'git for data'). This is a real product with a real client, not a wrapper.
- composes with: 50 GB x N free accounts, but the 50 GB/month transfer cap applies per account too, so chaining accounts multiplies egress but not storage usefulness. 10 TiB would need 205 accounts.
- reliability: Mature, funded, stable. Data is content-addressed and versioned, so no silent expiry. The API host api.oxen.ai did not resolve from this network, which suggests the documented API endpoint has moved or is geo-restricted.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Explorer (free forever): 50 GB data storage + 50 GB data transfer, unlimited public repos with unlimited collaborators, 5 private repos (max 3 collaborators). Hacker $30/mo: 100 GB storage / 100 GB transfer. Pro $60/mo: 500 GB / 500 GB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'Free Forever! ... Unlimited public repositories with unlimited collaborators · 5 private repositories · 50gb of data storage · 50gb of data transfer'; Hacker '100gb of data storage / 100gb of data transfer'; Pro '500gb'
  - [2] 2026-10-21: probe: GET -> 404 (146 bytes); GET https://api.oxen.ai/api/repos/ox/COCO-2017 -> DNS resolution failure (Could not resolve host)
- sources:
  - [1] https://oxen.ai/pricing
  - [2] https://hub.oxen.ai/api/repos/ox/COCO-2017
