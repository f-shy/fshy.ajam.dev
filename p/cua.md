# Cua

> cua.ai | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cua/ | JSON https://fshy.ajam.dev/api/v1/entity/cua.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cua

- `compute/cua` | self-hosted, last resort | verdict dead | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://cua.ai/pricing
- free tier: no hosted sandbox rate is published: the pricing page states the offer now connects computer-use agents to your own compute | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: the earlier hosted Fleet rate is withdrawn
- per-object cap: not applicable
- retention: not applicable: no hosted machine is sold | days: 0
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: no hosted signup exists to price
- interface: unknown
- limits:
  - retention-clamped (binding): the hosted Fleet rate is no longer published [1]
- limits note: the page offers no managed rate to compare, so there is nothing to price
- binding note: the hosted Fleet rate is withdrawn; the offer ends at the product, not at a quota
- interface detail: an agent framework that targets published compute.
- tooling: a Python framework for computer-use agents
- composes with: none as a host: it runs on a machine already in place
- reliability: no reliability event recorded
- notes: Dead as a compute provider and alive as a framework. A reader who wants a hosted sandbox should not look here, and a reader who already has a machine should.
- self hosted: yes
- extras:
  - billing_model: flat-pool
  - free_tier_kind: none
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: the page states the current offer connects computer-use agents to your own compute and no hosted rate is published
- sources:
  - [1] https://cua.ai/pricing

## Cua (Cua Spaces)

- `compute/cua-windows` | self-hosted, last resort | verdict dead | evidence documented | binding request-rate | category Windows host
- needs card no, phone no, ID no, institution no | verified 2026-10-26T11:33:32.317Z (live) | stale on 2026-11-26
- url https://cua.ai/pricing
- free tier: no rented Windows machine; the free tier is 2 live sessions and 20 remote hours a month, where a remote hour is time spent using a computer the customer already owns through Cua's relay. Cua states 'You bring the computers; Cua doesn't rent them.' | unit: hours | metered on: wall-clock | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable: no machine is provided
- retention: not applicable: no machine or disk is provided
- egress: not applicable: no machine is provided; traffic crosses the customer's own computer and Cua's relay | metered: no | source: [1]
- identity: email | detail: an account is required to use the relay; no card and no phone were read
- interface: unknown
- limits:
  - request-rate (binding): 20 remote hours a month and 2 live sessions on Free, 200 hours and 5 sessions for USD 25 a seat [1]
- limits note: a remote hour is counted once for each hour with at least one live session through the relay, per calendar month UTC; it is relay time, not machine time
- binding note: the 20-hour relay allowance is the only meter, and it measures time on hardware the customer owns rather than a rented host.
- interface detail: a relayed desktop session to a computer the customer already owns; no machine is rented
- tooling: Cua's client and relay; the customer supplies the computer
- composes with: not a compute source; it shares a computer already in place, and the analysis assumes no local hardware, so the free tier is worth nothing as compute
- reliability: no reliability event observed; the service relays to the customer's own computer and provides no machine of its own
- notes: Corrected on 2026-10-26. The record had read 'using your computers from somewhere else' as a rented Windows Server host. The live page says the opposite: Cua relays to a computer the customer already owns and rents no machine. The 20 remote hours are relay hours, not a Windows host, so the record's qualifies-with-caveat verdict is withdrawn. The analysis assumes no local hardware, so the free tier is worth zero as compute.
- evidence note: the live pricing page was read on 2026-10-26 and states that Cua does not rent machines. Earlier evaluation read 'using your computers from somewhere else' as a rented Windows host; the page's own words refute that reading.
- self hosted: yes
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the meter is an hour with at least one live session through the relay, on a computer the customer owns
  - free_tier_kind: none
  - net.out: yes
  - net.in: yes
  - net.ports: sessions are relayed to the customer's own computer
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Up to 2 live sessions and 20 remote hours a month' on the free tier against 'Up to 5 live sessions and 200 remote hours a month' at '$25 per seat a month', and 'Remote hours: time spent using your computers from somewhere else. Using a computer from itself is free.', quoted
  - [1] 2026-10-26: quoted: 'Cua Spaces turns the Macs, Linux boxes and cloud VMs your team already has into shared desktops. ... You bring the computers; Cua doesn't rent them.'
- sources:
  - [1] https://cua.ai/pricing
