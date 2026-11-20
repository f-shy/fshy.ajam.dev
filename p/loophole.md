# Loophole

> loophole.cloud | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/loophole/ | JSON https://fshy.ajam.dev/api/v1/entity/loophole.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Loophole

- `egress/loophole-cloud` | fails-egress | evidence documented | binding none | category tunnel (hosted, HTTP only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://loophole.cloud/docs/faq
- price USD 0
- free tier: We do not enforce any limitations on concurrent connections, number of requests or bandwidth. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no quota: 'We do not enforce any limitations on concurrent connections, number of requests or bandwidth. Neither in the cli nor in our proxy servers.'; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: a sign-up account and an authtoken: 'you need to sign up for an account' | country: None
- interface: cli
- binding note: No quantity binds because the proxy speaks HTTP only; at 1 TiB the first failure is that there is nothing to forward.
- interface detail: loophole http 3000 -s name
- tooling: loophole CLI
- composes with: HTTP ingress only
- reliability: one small operator; no published uptime
- notes: A generous free service disqualified by protocol alone, which is the classic case the memo's tooling rule warns against confusing with a capacity judgement.
- evidence note: The vendor states the protocol limit twice, in the FAQ and in a repository discussion. Nothing would raise it.
- extras:
  - wg_path: none
  - wg_detail: 'Loophole currently supports http/https connections only.' There is no TCP path and no UDP path.
  - ingress: http-only
  - volume_stated: no quota: 'We do not enforce any limitations on concurrent connections, number of requests or bandwidth. Neither in the cli nor in our proxy servers.'
  - bytes_transit: yes
  - transit_note: the Loophole proxy carries the HTTPS traffic
- evidence:
  - [1] 2026-10-23: 'Loophole currently supports http/https connections only', and the no-limits statement
  - [2] 2026-10-23: 'Instantly create a public HTTPS url for a website running locally'
- sources:
  - [1] https://loophole.cloud/docs/faq
  - [2] https://loophole.cloud/
