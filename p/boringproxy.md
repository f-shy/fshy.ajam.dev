# boringproxy

> boringproxy.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boringproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/boringproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## boringproxy

- `egress/boringproxy` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category overlay network or advanced tunnel tool | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:11:01.399Z (live) | stale on 2026-12-04
- url https://boringproxy.io/
- price USD 0
- free tier: Designed to be very easy to use. No config files. Clients can be remote-controlled through a simple WebUI and/or REST API on the server. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: unverified: no hosted allowance is published; the hosted site redirects to a parked domain on 2026-11-19; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: email | detail: an account on the hosted service, terms not read | country: None
- interface: cli
- binding note: No allowance is published, so the byte wall is unknown; the transport column is what the list states. Reverse proxy with a WebUI; HTTP.
- interface detail: not established
- tooling: The user builds and runs the boringproxy server and client; no hosted endpoint is published.
- composes with: Needs an account before any capacity is visible.
- reliability: Hosted site redirects to a parked domain and answers HTTP 403 under a challenge on 2026-11-19; first-party repo describes a self-hosted server.
- notes: Reverse proxy with a WebUI; HTTP. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Hosted site unreachable: boringproxy.io redirects to a parked domain and answers HTTP 403 under a challenge on 2026-11-19; the first-party GitHub README describes building and running the server from source.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No allowance is published in the list entry.
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Designed to be very easy to use. No config files. Clients can be remote-controlled through a simple WebUI and/or REST API on the server.
  - probe:https://boringproxy.io/ 2026-11-19: the hosted site redirects to a parked domain | capture: sha256:a82f36af502c2a16c332121c349f18005590385e97f8a0fca31ce53bd622f084 | quote: "final_url": "https://rlcinvest.hk.com/"
  - [3] 2026-11-19: the first-party README describes software the user builds and runs | capture: sha256:23f0e35b97d07b6c84b1864854b145ab7581aa63d565ce02908615ec63eb0832 | quote: The information in this README is just for building from source.
  - [3] 2026-11-19: the software is built and run by the user | capture: sha256:23f0e35b97d07b6c84b1864854b145ab7581aa63d565ce02908615ec63eb0832 | quote: The information in this README is just for building from source.
  - probe:https://boringproxy.io/ 2026-11-19: the hosted site answered HTTP 403 on 2026-11-19 | capture: sha256:a82f36af502c2a16c332121c349f18005590385e97f8a0fca31ce53bd622f084 | quote: "status": 403
  - [3] 2026-11-19: the first-party README describes self-hosted software with no hosted endpoint | capture: sha256:23f0e35b97d07b6c84b1864854b145ab7581aa63d565ce02908615ec63eb0832 | quote: The information in this README is just for building from source.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://boringproxy.io/
  - [3] https://github.com/boringproxy/boringproxy
