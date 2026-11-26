# Metered tsocket

> metered.ca | Storage, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/metered/ | JSON https://fshy.ajam.dev/api/v1/entity/metered.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## metered open relay at the advertised 20 gb

- `storage/metered-open-relay-at-the-advertised-20-gb` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:03.171Z (live) | stale on 2026-12-04
- url https://www.metered.ca/tools/openrelay/
- free tier: none reachable: The 20 GB/month figure on the Open Relay landing page is stale; the billing page sells a 500 MB/month free tier shared ingress+egress. 40x overstatement on the vendor's own site. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: The 20 GB/month figure on the Open Relay landing page is stale; the billing page sells a 500 MB/month free tier shared ingress+egress. 40x overstatement on the vendor's own site.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The 20 GB/month figure on the Open Relay landing page is stale; the billing page sells a 500 MB/month free tier shared ingress+egress. 40x overstatement on the vendor's own site.
  - [2] 2026-10-21: cited as the basis of the rejection: The 20 GB/month figure on the Open Relay landing page is stale; the billing page sells a 500 MB/month free tier shared ingress+egress. 40x overstatement on the vendor's own site.
  - [1] 2026-11-19: the Open Relay landing page still advertises 20 GB of free monthly TURN usage | capture: sha256:6ccf4dee6c1c890cbbd19eb9a1813ab1703fd1c55aa39e9b298e1b86d974cca3 | quote: The TURN Server provides 20 GB of free TURN Usage every month.
  - [1] 2026-11-19: the STUN/TURN pricing page lists a 500 MB monthly free TURN allowance | capture: sha256:401c1fb6e67daea6f3b3a96590f69fdc0bc52a27132fd7601c60e18041c1cd6b | quote: - 500 MB monthly TURN usage(ingress + egress)
- sources:
  - [1] https://www.metered.ca/tools/openrelay/
  - [2] https://www.metered.ca/stun-turn

## Metered tsocket

- `egress/metered-tsocket` | fails-egress | evidence documented | binding write-gated | category tunnel (hosted, HTTP and TCP) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:30.546Z (live) | stale on 2026-12-26
- url https://www.metered.ca/tools/tsocket/
- price USD 0
- free tier: tsocket is completely free. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no bandwidth figure is published; the claim is 'without limitation' on tunnel count and no paid plan exists; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: an auth token from a Metered account: 'authenticate with the auth token' | country: None
- interface: cli
- limits:
  - write-gated (binding): an account is required to create a tunnel [1]
- binding note: Creating any tunnel requires a Metered account, which is the constraint that binds the path.
- interface detail: tsocket with an auth token, multiple concurrent http and tcp tunnels
- tooling: tsocket binary
- composes with: HTTP and TCP ingress.
- reliability: free with no stated cap, which usually means an unpublished tolerance
- notes: Metered provides TURN relay infrastructure with a 500 MB monthly free allowance, designed for WebRTC media routing rather than general TCP/UDP port forwarding.
- evidence note: The vendor also sells a TURN service whose free allowance is 500 MB monthly, but TURN grants allocations to authenticated clients and does not present a public listening port, so it was not pursued as an ingress path.
- extras:
  - wg_path: none
  - wg_detail: HTTP and TCP tunnels: 'Launch secure multiple http and tcp tunnels, without limitation.'
  - ingress: tcp
  - volume_stated: no bandwidth figure is published; the claim is 'without limitation' on tunnel count and no paid plan exists
  - bytes_transit: yes
  - transit_note: the Metered edge carries the TCP stream
- evidence:
  - [1] 2026-10-23: 'tsocket is completely free. Launch secure multiple http and tcp tunnels, without limitation.' and the TCP-only feature list
  - [2] 2026-10-23: 'Free 500MB monthly with unlimited STUN' on the TURN service, which is a relay for WebRTC and not a port forward
  - [1] 2026-11-25: the page states that tsocket is free | capture: sha256:95c4c3bdbc45a8c0a414bf30ca00262539997bba6597c407c6cfeec6c6c515ce | quote: tsocket is completely free.
  - [1] 2026-11-25: creating a tunnel requires an account | capture: sha256:95c4c3bdbc45a8c0a414bf30ca00262539997bba6597c407c6cfeec6c6c515ce | quote: To create tunnels using tsocket you need to have an account. An account is required to prevent spam.
  - [1] 2026-11-25: the offer is http and tcp tunnels | capture: sha256:95c4c3bdbc45a8c0a414bf30ca00262539997bba6597c407c6cfeec6c6c515ce | quote: Launch secure multiple http and tcp tunnels, without limitation.
  - [1] 2026-11-25: the page offers http and tcp tunnels | capture: sha256:95c4c3bdbc45a8c0a414bf30ca00262539997bba6597c407c6cfeec6c6c515ce | quote: Launch secure multiple http and tcp tunnels, without limitation.
- sources:
  - [1] https://www.metered.ca/tools/tsocket/
  - [2] https://www.metered.ca/stun-turn
