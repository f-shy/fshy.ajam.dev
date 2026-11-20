# pgrok/pgrok

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-pgrok/ | JSON https://fshy.ajam.dev/api/v1/entity/github-pgrok.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pgrok/pgrok

- `egress/pgrok-pgrok` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:04.144Z (live) | stale on 2026-12-20
- url https://github.com/pgrok/pgrok
- price USD 0
- free tier: A multi-tenant HTTP reverse tunnel solution through SSH remote port forwarding. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. HTTP reverse tunnel over SSH remote forwarding.
- interface detail: not established
- tooling: The user installs and runs the pgrok server and client binaries on infrastructure the user supplies.
- reliability: the same as interface detail
- notes: HTTP reverse tunnel over SSH remote forwarding. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: First-party project README read; it describes self-hosted multi-tenant software that the user runs on their own infrastructure with SSO, and offers no hosted endpoint or byte allowance. The first-party source supersedes the aggregator list sentence.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: A multi-tenant HTTP reverse tunnel solution through SSH remote port forwarding.
  - [2] 2026-11-19: the first-party README states pgrok is self-hosted software with no hosted endpoint or published byte allowance | capture: sha256:8eeb521148053adc5271d747e0c7328ae61f4953931298f7fca2c39fba925843 | quote: pgrok is a self-hosted, multi-tenant networking platform for exposing HTTP services and raw TCP connections through SSH reverse tunnels.
  - [2] 2026-11-19: the first-party README says the server runs on user-supplied infrastructure | capture: sha256:8eeb521148053adc5271d747e0c7328ae61f4953931298f7fca2c39fba925843 | quote: Run it on your own infrastructure with your own domain and OIDC-compatible SSO provider.
  - [2] 2026-11-19: the first-party README is the basis for the egress finding | capture: sha256:8eeb521148053adc5271d747e0c7328ae61f4953931298f7fca2c39fba925843 | quote: pgrok is a self-hosted, multi-tenant networking platform for exposing HTTP services and raw TCP connections through SSH reverse tunnels.
  - [2] 2026-11-19: the first-party README describes self-hosted software with no hosted endpoint | capture: sha256:8eeb521148053adc5271d747e0c7328ae61f4953931298f7fca2c39fba925843 | quote: pgrok is a self-hosted, multi-tenant networking platform for exposing HTTP services and raw TCP connections through SSH reverse tunnels.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/pgrok/pgrok
