# USENEXT

> usenext.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenext/ | JSON https://fshy.ajam.dev/api/v1/entity/usenext.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## USENEXT

- `debrid/usenext` | trial-only | evidence documented | binding volume-quota | category Usenet provider (Aviteo GmbH, Germany) - trial offer | tier 14-day trial
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://www.usenext.com/en-US/anmelden/default
- free tier: "You can try out Usenet risk-free for 14 days with free data volume." The trial page prices the Rookie+ package at "0 € During the trial with free download volume" and "30 GB Monthly highspeed data volume", then "7.95 € per month" after the trial. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The trial page prints no separate byte figure for the trial; 30 GB is the Rookie+ package volume the trial runs on. Whether the trial carries exactly that volume is inferred from the page layout, not from a second sentence.
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention, so 30 GB is about 40,000 article fetches. | source: [1]
- retention: "More than 18 years retention of data (6,600+ days)" in the package feature list on the home page. | days: 6600 | source: [2]
- egress: No separate traffic price is published; the trial is metered by downloaded volume and the plan list prices volume per month after it. The provider does not state an overage rate for the trial. | metered: yes | free allowance: 30 GB during a 14-day trial | source: [1]
- identity: card | detail: The provider §1.1b lists "Entering payment information and billing address" as a registration step. §6.1c says the payment provider may "reserve or deduct and reimburse a small amount of money (less than $5.00 US) from the credit card or PayPal account or iDeal account" to verify the customer. A payment instrument is captured before the trial starts.
- interface: unknown
- limits:
  - volume-quota (binding): 30 GB during the 14-day trial; 30 GB/month on Rookie+ afterwards [1]
  - write-gated: registration requires "Entering payment information and billing address" [3]
- binding note: At 1 TiB per month target the 30 GB trial counter is exhausted in roughly 1% of a month, so the byte counter binds long before speed or retention. No speed figure is published for the trial.
- interface detail: NNTP over SSL. The vendor publishes no API. The schema has no nntp token, so the array says unknown; the protocol is not in doubt.
- tooling: any NNTP client (SABnzbd, NZBGet, nzbget CLI); the package bundles a VPN, not a downloader
- composes with: A one-off 30 GB that must be spent inside 14 days on the largest remaining object, then cancelled before the monthly plan starts; it does not compose into a repeating month.
- reliability: The trial converts to a paid monthly plan at 7.95 € unless cancelled inside the 14 days; §6.4c stores the registration IP and §6.1d allows immediate blocking where payment data is judged false.
- notes: A second address does not defeat this, because the gate is the payment instrument plus the stored registration IP rather than the network address. Abandonment: if the trial stops being priced at 0 € for a full 14 days, the record becomes paid-only.
- evidence note: Trial length, volume and the payment gate are each quoted from a vendor page read. A signup completed to the payment step would raise the volume attribution from inferred to measured; it was not executed.
- extras:
  - repeatable: no
  - repeat_basis: documented
  - repeat_quote: The customer may take advantage of the free trial period only once unless the Provider expressly grants the customer an additional free trial period.
- evidence:
  - [2] 2026-10-23: "Get your 14 day trial with extra security" and "You can try out Usenet risk-free for 14 days with free data volume. During this time, you can cancel at any moment without any hassle."
  - [1] 2026-10-23: "USENEXT Rookie+ 30 GB", "0 € During the trial with free download volume", "7.95 € per month" after it, and FAQ "You will only be charged after the trial phase has elapsed, using the payment method you have specified."
  - [3] 2026-10-23: §4.2a "The customer may take advantage of the free trial period only once unless the Provider expressly grants the customer an additional free trial period"; §1.1b payment information at registration; §6.1c the sub-$5 card hold; §6.4c the stored registration IP
- sources:
  - [1] https://www.usenext.com/en-US/anmelden/default
  - [2] https://www.usenext.com/en-US
  - [3] https://www.usenext.com/en-US/agb
