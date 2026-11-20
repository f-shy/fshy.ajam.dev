# Tweaknews

> tweaknews.eu | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tweaknews/ | JSON https://fshy.ajam.dev/api/v1/entity/tweaknews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tweaknews

- `debrid/tweaknews` | paid-only | evidence documented | binding none | category usenet provider (Omicron/Base IP backbone, EU retail) | tier Ultimate + VPN
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:52:29.000Z (live) | stale on 2026-11-23
- url https://www.tweaknews.eu/en/usenet-plans
- price EUR 5.83 (Fast, 12-month term, 50 Mbit)
- free tier: No free tier and no trial stated in prose. The plans page carries a checkout option id 'Ultimate-VPN-12Mo-FreeTrial-50GB', which suggests a 50 GB trial exists on the 12-month Ultimate plan, but no sentence on the page describes it. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: 6,000 Days article retention, in the plan table | days: 6000 | source: [1]
- egress: Unlimited downloads on every plan; speed is capped by tier rather than by volume | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: Email plus a paid plan. No card-free path is described; the only trial signal is a checkout option id with no prose.
- interface: nntp
- limits:
  - request-rate: 30 connections on Fast, 40 on Lightning, 60 on Ultimate + VPN [1]
  - per-ip-shaping: 50 Mbit on Fast, 100 Mbit on Lightning, unlimited on Ultimate + VPN [1]
  - retention-clamped: 6,000 days of article retention [1]
- limits note: Annual prices from the plan table: Fast EUR 69.95 (EUR 5.83/mo), Lightning EUR 89.95 (EUR 7.50/mo), Ultimate + VPN EUR 108.78 (EUR 9.07/mo). Monthly prices seen in the same page markup are EUR 7.95, 9.95 and 12.95; the table shows the 12-month term by default.
- binding note: Ultimate + VPN is unlimited speed and unlimited volume with 60 connections; no fair-use number is published, so nothing in the vocabulary binds at 1 TiB/month.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: A low-speed primary for a client whose line is under 50 Mbit on the Fast tier; it stacks with an Abavia block for completion and duplicates the Omicron spool if paired with Newshosting.
- reliability: Base IP BV infrastructure (AS34305), the Dutch arm of the Omicron group. A cached virtual version of the Eweka spool rather than a fourth independent archive.
- notes: The 50 Mbit cap on Fast is the reason the cheapest plan is not the cheapest plan here: at 12.5 MB/s 1 TiB of monthly transfer needs about 24 hours of wall clock, and a single connection cannot use more than that.
- evidence note: Plan prices, speeds, connections and retention come from the vendor's own plan table markup read. The trial is left unclaimed because no prose supports it.
- extras:
  - backbone: Omicron / Base IP BV, AS34305
  - trial_signal: Ultimate-VPN-12Mo-FreeTrial-50GB in page DOM only
  - monthly_prices_in_markup: EUR 7.95 / 9.95 / 12.95
- evidence:
  - [1] 2026-10-23: Fast 50 Mbit 30 connections EUR 69.95/yr; Lightning 100 Mbit 40 connections EUR 89.95/yr; Ultimate + VPN unlimited 60 connections EUR 108.78/yr; 6,000 days
  - [1] 2026-10-23: Page markup carries span[data-id=Ultimate-VPN-12Mo-FreeTrial-50GB], pre-selected by script
- sources:
  - [1] https://www.tweaknews.eu/en/usenet-plans
