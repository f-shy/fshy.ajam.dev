# Fastusenet

> fastusenet.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fastusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/fastusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fastusenet

- `debrid/fastusenet` | trial-only | evidence documented | binding volume-quota | category usenet provider (Omicron reseller) | tier Unlimited
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:52:29.000Z (live) | stale on 2026-11-23
- url https://www.fastusenet.org/signup/freetrial.php
- price USD 6.95 (unlimited, monthly)
- free tier: A free trial of 14 days or 15 GB, whichever comes first, on all three plans, then the plan price applies. The trial signup runs through a three-step flow whose third step is 'Payment Information'. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: Not stated by the vendor on any page read. The trial and plans pages carry no day count; the Omicron spool this reseller serves through us.sslusenet.com is sold elsewhere as 6,642+ days, which is inferred rather than measured here. | source: [1]
- egress: Unlimited after the trial on the top plan; 35 GB and 15 GB on the two cheaper plans | metered: yes | free allowance: 15 GB during the trial on every plan | source: [1]
- identity: card | detail: 'Payment Information' is step 3 of the trial signup, before 'Create Login' is step 4, so a payment method is captured before the trial starts. The card is what makes this trial-only.
- interface: nntp
- limits:
  - request-rate: 50 SSL connections [1]
  - volume-quota (binding): 15 GB during the 14-day trial; 15 GB, 35 GB or unlimited after it [1]
- limits note: Trial then $6.95/mo unlimited, $5.95/mo for 35 GB, $3.95/mo for 15 GB. The trial carries 15 GB whichever plan is chosen, so the most a free trial yields here is 15 GB once.
- binding note: The trial is hard-capped at 15 GB and the two cheap plans are hard-capped at 15 GB and 35 GB per month. At 1 TiB/month the counter is the first thing that fails, on every tier.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: Once the trial converts this is a second Omicron feed and adds nothing to a Newshosting or Eweka subscription; its stack value is the 14-day test window.
- reliability: Omicron reseller on the sslusenet.com hosts, the same pair Newsgroup Ninja uses. The 14-day window is longer than the 3 to 7 days most competitors allow.
- notes: Documented as the clearest example of the pattern: a trial advertised as free, gated at a payment step that no vendor page describes as optional.
- evidence note: Trial terms, prices and step order are on the vendor's signup pages read. The card requirement is read from the step name, not from submitting the form.
- extras:
  - backbone: Omicron, via us.sslusenet.com / nl.sslusenet.com
  - trial_gate: step 3 of 4 is Payment Information
- evidence:
  - [1] 2026-10-23: '14 days to test our service or 15GB of downloads, whichever comes first'; 50 SSL connections; then $6.95/$5.95/$3.95 per month
  - [1] 2026-10-23: the meta description adds 'Choose the plan your account converts to after the trial'
- sources:
  - [1] https://www.fastusenet.org/signup/freetrial.php
