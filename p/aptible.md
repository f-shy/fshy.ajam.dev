# Aptible

> aptible.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aptible/ | JSON https://fshy.ajam.dev/api/v1/entity/aptible.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aptible

- `compute/aptible` | paid-only | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-25T05:18:26.643Z (live) | stale on 2026-12-26
- url https://www.aptible.com
- free tier: Aptible replaces complex, unpredictable AWS pricing with clear, usage-based pricing. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no free tier published; both calls to action lead to a signup that prices the account [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and offers no free tier or trial, only signup links that lead to a billing account. The pricing path is /pricing, which this record does not cite
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a managed deployment into the vendor's own AWS environment; the page states no clock
  - free_tier_kind: none
  - ps.price: scalable volumes, priced with the account
  - ps.durability: managed volume
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the account is active
  - net.out: yes
  - net.in: yes
  - net.ports: HTTPS endpoints
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Deploy in minutes' with 'automated backups, scalable volumes, security, monitoring', 'Aptible enforces encryption, audit logging, quotas, and availability for all LLM usage', and 'Start Deploying' at app.aptible.com/signup, quoted
  - [1] 2026-11-25: the site states that Aptible pricing is usage-based, with no free plan published | capture: sha256:8b8d2141c3971e942c52cfb63cf40cdb16b5742e8197937f8005ec9dc245345d | quote: Aptible replaces complex, unpredictable AWS pricing with clear, usage-based pricing.
- sources:
  - [1] https://www.aptible.com
