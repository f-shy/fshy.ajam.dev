# Loophole

> loophole.cloud | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/loophole/ | JSON https://fshy.ajam.dev/api/v1/entity/loophole.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Loophole

- `egress/loophole-cloud` | fails-egress | evidence documented | binding none | category tunnel (hosted, HTTP only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T17:26:44.696Z (live) | stale on 2026-12-26
- url https://loophole.cloud/docs/faq
- price USD 0
- free tier: We do not enforce any limitations on concurrent connections, number of requests or bandwidth. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no quota: 'We do not enforce any limitations on concurrent connections, number of requests or bandwidth. Neither in the cli nor in our proxy servers.'; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: an account and an authtoken: 'To access Loophole services described in further sections, you need to sign up for an account. Once you've signed up, you need to configure loophole with the authtoken.' | country: None
- interface: cli
- binding note: No quantity binds because the proxy speaks HTTP only; at 1 TiB the first failure is that there is nothing to forward.
- interface detail: loophole http <port> [host] [flags]; --hostname sets the custom hostname
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
  - [3] 2026-11-25: the command's usage line and its hostname flag | capture: sha256:9f40bd9a45f62596c4ea811c797fa0ea2954e6939e53b7e6823cf0d49fc9fc82 | quote: loophole http <port> [host] [flags]
  - [4] 2026-11-25: an account and an authtoken are required | capture: sha256:581c4c023cc39fe641ba4526847fbf42c99e158ff21fc96503c59c9cd948530e | quote: To access Loophole services described in further sections, you need to sign up for an account. Once you've signed up, you need to configure loophole with the authtoken.
  - [5] 2026-11-25: the login and signup pages answer HTTP 404, so the form could not be read | capture: sha256:e029278752496e0584545ac87ac810d0e98ff33f11219fecfd0fc3f171af9469 | quote: Page Not Found
  - [1] 2026-11-25: no published limit on connections, requests or bandwidth | capture: sha256:f70b047001cc629a5cc043f253b3493a5cb0b8fd3c476381c4f3f3c766bc39f7 | quote: We do not enforce any limitations on concurrent connections, number of requests or bandwidth.
  - [1] 2026-11-25: the proxy carries http/https only | capture: sha256:f70b047001cc629a5cc043f253b3493a5cb0b8fd3c476381c4f3f3c766bc39f7 | quote: Loophole currently supports http/https connections only.
- sources:
  - [1] https://loophole.cloud/docs/faq
  - [2] https://loophole.cloud/
  - [3] https://loophole.cloud/docs/commands/http
  - [4] https://loophole.cloud/docs/guides/auth
  - [5] https://loophole.cloud/login
