# DICE

> dice-eosc.eu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dice-eosc/ | JSON https://fshy.ajam.dev/api/v1/entity/dice-eosc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DICE / EUDAT cost-free storage call (the EU's funded-storage instrument)

- `storage/dice-eudat-cost-free-storage-call` | fails-identity | evidence inferred | binding none | category eu-research-infrastructure
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.dice-eosc.eu/call-service-requests
- free tier: Not published as a number. DICE is a funding instrument, not a product. It buys you 'personal drive storage' up to long-term preservation, priced by negotiation with whoever provides it. The EC put over EUR 6 million into Virtual Access to make it free for new users. What that buys in TB is determined per request. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free at the point of use. Paid by the EC grant, not the user. | metered: no
- identity: institution | detail: institution
- interface: rest
- limits note: Two gates, both fatal or near-fatal: (1) eligibility is territorial. 'Any individual, or research entity located within the EU Member States or Associated Countries is eligible'; (2) the funding window was 'until June 2023' and the news item was last updated Nov 2023, i.e. the free window as documented has already closed and its continuation is 'under appropriately agreed conditions of use'. Undocumented. So this is a lead for a European client and not a live offer for anyone else.
- interface detail: rest
- tooling: Whatever the chosen provider offers; services are ordered through the EOSC Portal (marketplace.eosc-portal.eu) by selecting a service and submitting an order flagged as a DICE request. No uniform API.
- composes with: Basic requests ('personal workspace') are granted same-day on registration alone; Standard (2–10 working days) and Customised (negotiated) tiers scale into archives. The multiplier is service requests, each of which is separately approved.
- reliability: The page still advertises the call but dates itself to a funding period that ended in 2023. Treat as a lead to re-check with the EUDAT helpdesk, not as an available quota.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Not published as a number — DICE is a funding instrument, not a product. It buys you 'personal drive storage' up to long-term preservation, priced by negotiation with whoever provides it. The EC put over EUR 6 million into Virtual Access to make it free for new users. What that buys in TB is determined per request.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: opened: 'Any individual, or research entity located within the EU Member States or Associated Countries is eligible to access the DICE services free of charge'; 'over six million Euros … to offer free data storage facilities … until June 2023'; 'Basic service requests are satisfied immediately after request … it needs just an account registration — for example, an individual user requesting a personal workspace'; 'Created on: Mar 2, 2021 Last updated: Nov 2, 2023'.
  - [2] 2026-10-21: 504 on the first attempt; the EUDAT copy of the same call was readable, so the content is confirmed but the canonical URL is flaky.
- sources:
  - [1] https://www.eudat.eu/news/submit-your-request-for-cost-free-dice-data-storage-for-new-users-in-the-eu-research-community
  - [2] https://www.dice-eosc.eu/call-service-requests
