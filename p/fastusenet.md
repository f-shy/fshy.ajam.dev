# Fastusenet

> fastusenet.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fastusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/fastusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fastusenet

- `debrid/fastusenet` | trial-only | evidence documented | binding volume-quota | category usenet provider (Omicron reseller) | tier Unlimited
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:47:09.199Z (live) | stale on 2026-12-26
- url https://www.fastusenet.org/signup/freetrial.php
- price USD 6.95 (unlimited, monthly)
- free tier: A free trial of 14 days or 15 GB, whichever comes first, on all three plans, then the plan price applies. The trial signup runs through a three-step flow whose third step is 'Payment Information'. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: 6,676+ days of binary retention, stated on the vendor home page. The retention guide says 6,668+ days; the more conservative of the two first-party figures is recorded. | days: 6668 | source: [1]
- egress: Unlimited after the trial on the top plan; 35 GB and 15 GB on the two cheaper plans | metered: yes | free allowance: 15 GB during the trial on every plan | source: [1]
- identity: card | detail: The signup flow lists four steps: 'Choose Your Plan', 'Confirm Account', 'Payment Information', 'Create Login'. The payment step asks for an email address, first name, last name and a credit/debit card or PayPal, so a payment method is captured before the trial starts.
- interface: nntp
- limits:
  - request-rate: 50 SSL connections [1]
  - volume-quota (binding): 15 GB during the 14-day trial; 6 GB, 15 GB, 35 GB or unlimited after it [1]
- limits note: Trial then a 6 GB tier is published at $2.95/mo alongside the existing unlimited, 35 GB and 15 GB plans. The trial carries 15 GB whichever plan is chosen.
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
  - [1] 2026-11-25: the free trial is 14 days or 15 GB, whichever comes first | capture: sha256:9d3b1a8089678b1f3110e02b0a3eb2e5dd5ddf1b54decb1fd65ef04709d53cf1 | quote: Our unrestricted free trial gives you 14 days to test our service or 15GB of downloads, whichever comes first.
  - [1] 2026-11-25: 50 SSL connections on the trial | capture: sha256:9d3b1a8089678b1f3110e02b0a3eb2e5dd5ddf1b54decb1fd65ef04709d53cf1 | quote: - 50 SSL Connections
  - [2] 2026-11-25: the vendor now publishes 6,676+ days of retention on its home page | capture: sha256:075efabd9e24be1f82f47e068a974d30d1f3bcb4dc8c83a87c761e3f8ddc11ae | quote: 6,676+ Days Retention
  - [3] 2026-11-25: the retention guide states 6,668+ days of storage | capture: sha256:0614c359c1df1f43fcb4ee593e5fc37413546857681d6cdf3f1ee377ad7c9564 | quote: 6,668+ days
  - [2] 2026-11-25: a 6 GB plan is now listed alongside unlimited, 35 GB and 15 GB | capture: sha256:075efabd9e24be1f82f47e068a974d30d1f3bcb4dc8c83a87c761e3f8ddc11ae | quote: - 6 GB
  - [2] 2026-11-25: the 6 GB plan is priced at USD 2.95 per month | capture: sha256:075efabd9e24be1f82f47e068a974d30d1f3bcb4dc8c83a87c761e3f8ddc11ae | quote: $2.95/mo
  - [4] 2026-11-25: the signup flow includes a Payment Information step before the login step | capture: sha256:46c4bfd46ff90bf65fd81c8cd2fe15fb35bce7e245eb1f5764fdfaea3d23bcd5 | quote: Payment Information
  - [4] 2026-11-25: the signup step offers credit or debit card as a payment method | capture: sha256:46c4bfd46ff90bf65fd81c8cd2fe15fb35bce7e245eb1f5764fdfaea3d23bcd5 | quote: Credit / Debit CardVisa
- sources:
  - [1] https://www.fastusenet.org/signup/freetrial.php
  - [2] https://www.fastusenet.org/
  - [3] https://www.fastusenet.org/usenet-retention.html
  - [4] https://members.fastusenet.org/register?plan=unlimited&trial=1
