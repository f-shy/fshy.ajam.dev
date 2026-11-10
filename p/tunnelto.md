# tunnelto

> tunnelto.dev | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnelto/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnelto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunnelto

- `egress/tunnelto` | trial-only | evidence documented | binding none | category tunnel (hosted)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T10:32:57.642Z (live) | stale on 2026-12-04
- url https://www.tunnelto.dev/
- free tier: Free, no card needed: a 10-minute free trial on a random <name>.tunn.dev subdomain with HTTPS and WebSockets; Pro/Teams USD 4 per user per month: no time limit, up to 20 custom subdomains, up to 5 active tunnels per user | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a stream
- retention: the generated subdomain is per session | source: [1]
- egress: no byte cap or transfer allowance is stated for any plan; the pricing section says: Higher volume? Contact us | metered: no | source: [1]
- identity: email | detail: an account for reserved subdomains; generated names need none
- interface: cli
- limits:
  - volume-quota: no byte cap or transfer allowance is published for any plan; the pricing section lists time (10-minute free trial) and tunnel count (up to 5 active tunnels per user on Pro/Teams) and refers higher volume to the vendor [1]
- binding note: No byte cap is published, so no byte volume binds. What ends a free tunnel is the 10-minute trial window, a time limit that the limits vocabulary has no kind for.
- interface detail: tunnelto --port 8000
- tooling: part of interface detail
- composes with: composes with an origin and no domain, and with nothing that needs a published quota.
- reliability: no byte cap is published and limits are set per plan on the pricing section; the terms reserve the right to bill overages, cancel a plan or revoke access when plan limits are not maintained
- notes: Open-source reverse tunnel tool written in Rust. Free service provides random public subdomains without published bandwidth caps.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the tunnel relays the origin's bytes
  - ingress: http-only
- evidence:
  - [1] 2026-10-22: the free install line and the USD 4/month pricing block
  - probe:https://www.tunnelto.dev/pricing 2026-10-22: the standalone /pricing path returns 404; the pricing block lives on the landing page under an anchor
  - [1] 2026-10-23: 'your local port gets a secure https://<subdomain>.tunnelto.dev address'
  - [1] 2026-11-03: the Free plan on the pricing section is a 10-minute free trial on a random <name>.tunn.dev subdomain; Pro/Teams is USD 4 per user per month with no time limit, up to 20 custom subdomains and up to 5 active tunnels per user | capture: sha256:c06712830b4b12dea89a48c310e8475c77963add3d396763fb7089e0dfe966d5 | quote: 10-minute free trial
  - [1] 2026-11-03: volume above the listed plans is handled by contacting the vendor and no byte figure is given | capture: sha256:c06712830b4b12dea89a48c310e8475c77963add3d396763fb7089e0dfe966d5 | quote: Higher volume? [Contact us](mailto:support@tunnelto.dev).
  - [1] 2026-11-03: no byte figure is published and higher volume is referred to the vendor | capture: sha256:c06712830b4b12dea89a48c310e8475c77963add3d396763fb7089e0dfe966d5 | quote: Higher volume? [Contact us](mailto:support@tunnelto.dev).
  - [2] 2026-11-03: the terms tie enforcement to plan limits and state no byte figure | capture: sha256:ddd5ca87e5c798e95af2264aff5004f01e3b87135dede4a1cf5f0267cb33b2dd | quote: tunnelto.dev reserves the right to bill overages, cancel your plan, or revoke access if limits are not maintained.
- sources:
  - [1] https://www.tunnelto.dev/
  - [2] https://tunnelto.dev/legal/terms
