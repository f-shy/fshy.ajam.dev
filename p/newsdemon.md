# NewsDemon

> newsdemon.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/newsdemon/ | JSON https://fshy.ajam.dev/api/v1/entity/newsdemon.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NewsDemon

- `debrid/newsdemon` | paid-only | evidence documented | binding none | category usenet provider (UsenetExpress backbone, retail) | tier Unlimited annual
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:47:09.201Z (live) | stale on 2026-12-26
- url https://www.newsdemon.com/usenet-access
- price USD 5.00 (unlimited, annual at $60/yr)
- free tier: No free tier and no free trial: 'NewsDemon does not offer a free trial. We used to, but payment processing partners discourage trial-to-paid conversion flows, and we decided to keep things simple instead.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: 5,948+ days of binary and text retention on the plans page and the free-trial page; the block page still prints a lower figure. The figure on the main plans page is recorded. | days: 5948 | source: [1]
- egress: Unlimited speed and downloads on the unlimited plans; 50 SSL connections on every plan | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: No trial at all, so a card or another accepted payment is required before the first byte. The vendor does not publish its payment list on the pages read; crypto is reported by the r/usenet deals wiki and was not confirmed here.
- interface: nntp
- limits:
  - request-rate: 50 SSL connections on every plan, including the $3 metered tier [2]
  - volume-quota: 50 GB/month on the metered tier; blocks of 100 GB, 500 GB and 1 TB never expire [3]
  - retention-clamped: 5,854 to 5,948 days depending on the page [3]
- limits note: Three unlimited terms (monthly, quarterly, annual) plus metered 50/100/200 GB and non-expiring blocks. Blocks are listed twice on the same page at two price columns: 100 GB at $15 or $17, 500 GB at $47 or $49, 1000 GB at $87 or $89. A separate page offers a 100 GB block for $5 and a 50 GB metered plan for $3/mo.
- binding note: The annual unlimited plan publishes no byte counter. At 1 TiB/month nothing in the vocabulary binds on that tier; the metered tier would bind at 50 GB by construction.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: The usual shape is a NewsDemon unlimited primary plus an Abavia block as fill: two independent spools, one subscription and one prepaid allowance.
- reliability: UsenetExpress backbone with NewsDemon's own spool on top, three regions (US East, US West, EU), 550 TB/day feed claimed. Post-quantum encryption is advertised on every plan.
- notes: The $3 metered plan is the cheapest paid entry of any provider among debrid providers and carries the same 50 connections as the unlimited plans.
- evidence note: All prices and the explicit refusal of a free trial come from vendor pages read. The two block price columns disagree with each other on the same page and the record keeps the higher.
- extras:
  - backbone: UsenetExpress
  - server_regions: US East; US West; NL
  - block_price_columns_conflict: yes
  - crypto: reported by r/usenet wiki/providerdeals, not vendor-confirmed
- evidence:
  - [1] 2026-10-23: unlimited monthly/quarterly/annual plus 50/100/200 GB metered and 100 GB/500 GB/1 TB blocks; 50 SSL connections; 5,914+ days
  - [2] 2026-10-23: 'NewsDemon does not offer a free trial'; 50 GB metered at $3/mo, 100 GB block at $5, unlimited annual at $60/yr
  - [3] 2026-10-23: blocks 10 GB $4.00, 25 GB $7.00, 50 GB $12.00, 100 GB $17.00, 500 GB $49.00, 1000 GB $89.00, against a second column $2.50/$5.00/$10.00/$15.00/$47.00/$87.00; 5,854++ days; 50 connections
  - [1] 2026-11-25: the plans page now states 5,948+ days of retention | capture: sha256:4f80487cfc7601f6008f34b083243d57180c0d14e37f2008da7c3c674574456b | quote: 5,948+
  - [1] 2026-11-25: 50 SSL connections are listed on the plans page | capture: sha256:4f80487cfc7601f6008f34b083243d57180c0d14e37f2008da7c3c674574456b | quote: 50 SSL Connections
  - [1] 2026-11-25: unlimited speed and downloads on the unlimited plans | capture: sha256:4f80487cfc7601f6008f34b083243d57180c0d14e37f2008da7c3c674574456b | quote: - ✓ Unlimited speed & downloads
  - [2] 2026-11-25: the vendor states there is no free trial | capture: sha256:838a39180cf26f09ca8e7a9592bbd2fbff507b0f1eced2ffa284e8a261f4dc76 | quote: NewsDemon does not offer a free trial. We used to, but payment processing partners discourage trial-to-paid conversion flows, and we decided to keep things simple instead.
  - [2] 2026-11-25: 50 SSL connections on every plan including the metered tier | capture: sha256:838a39180cf26f09ca8e7a9592bbd2fbff507b0f1eced2ffa284e8a261f4dc76 | quote: 50 SSL connections. On every plan, including the $3/month metered plan.
  - [2] 2026-11-25: the unlimited annual plan is USD 5 per month | capture: sha256:838a39180cf26f09ca8e7a9592bbd2fbff507b0f1eced2ffa284e8a261f4dc76 | quote: Unlimited Annual — $5/month
  - [3] 2026-11-25: the block page still states 5,854++ days | capture: sha256:4abce159155cda12ce446c546ef6307f348805b11728ce3c0ddc37cb1d9db794 | quote: - 5854++ Days Retention
  - [4] 2026-11-25: the refund policy names card and PayPal | capture: sha256:9412a47a0b41b5e874f3b951410fab73fc6e8bdeb68ceee9e356a343cb19cf6f | quote: Refunds are typically processed within 1-3 business days. The refund goes back to the original payment method. If you paid by credit card, the refund appears on your statement. If you paid by PayPal, it goes back to your PayPal account.
- sources:
  - [1] https://www.newsdemon.com/usenet-access
  - [2] https://www.newsdemon.com/free-trial
  - [3] https://www.newsdemon.com/block-accounts
  - [4] https://www.newsdemon.com/refund-policy
