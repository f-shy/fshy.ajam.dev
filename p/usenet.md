# UsenetAgency

> usenet.agency | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenet/ | JSON https://fshy.ajam.dev/api/v1/entity/usenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UsenetAgency

- `debrid/usenetagency` | qualifies-with-caveat | evidence documented | binding volume-quota | category usenet provider (Abavia reseller, NL) | tier Senior
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:29.000Z (live) | stale on 2026-11-23
- url https://usenet.agency/en/
- price EUR 5.75 (Senior, monthly)
- free tier: A 30 GB, 7-day try-out: 'The try out plan gives you: 500 mbit speed, 4084 days retention, 30 gigabytes free, No auto billing, Absolutely free'. The vendor's payment FAQ repeats it: 'Can I try your service before I pay? Hell yes! You can always try the first 7 days for free.' | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: 4085 days retention on the home page, 4084 days on the try-out page | days: 4084 | source: [1]
- egress: Unlimited speed on Senior; 40 Mbit on Junior and 80 Mbit on Medior | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: An email address, and the trial has three explicit gates: 'You can't register with a disposable e-mail address', 'You can't use a VPN or proxy server to register' and 'You can't have multiple accounts'. The VPN ban means the signup must come from a real residential address.
- interface: nntp
- limits:
  - request-rate: 25 connections on Junior and Medior, 50 on Senior [1]
  - per-ip-shaping: 40 Mbit Junior, 80 Mbit Medior, unlimited Senior [1]
  - volume-quota (binding): 30 GB on the free try-out, then unlimited on paid plans [2]
  - retention-clamped: 4085 days [1]
- limits note: Junior EUR 2.46/mo (40 Mbit, 25 connections), Medior EUR 3.69/mo (80 Mbit, 25 connections), Senior EUR 5.75/mo (unlimited speed, 50 connections). No automatic renewal: 'Your subscription expires when your subscription days have passed.'
- binding note: The free path is a 30 GB one-off, so at 1 TiB/month the allowance is what fails, and it fails after 30 GB. On Senior the vendor publishes no volume ceiling.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: A 30 GB Abavia allowance tests whether an Abavia spool completes the requested content before any money is spent; after that the Junior tier keeps it for EUR 2.46/mo.
- reliability: The try-out page also carries the line 'Payment will show up on your statement as NectoFarm B.V.', which is odd for a product listed at 'Total cost: FREE' and suggests a payment method may still be captured. That was not tested at checkout, so it is flagged rather than resolved. Abavia reseller operated by NectoFarm BV. The 30 GB try-out is the largest card-free allowance found on any provider among debrid providers, and the VPN ban is the price of it.
- notes: The caveat is the identity gate rather than the product: no disposable email, no VPN or proxy at signup, one account. A client behind a VPN cannot claim this trial at all.
- evidence note: The trial terms, the three registration rules, the prices and the retention figure are all from vendor pages read. Whether a card is captured at checkout is the one gap, because the signup form itself was not opened.
- extras:
  - backbone: Abavia
  - trial_rules: no disposable email; no VPN or proxy; no multiple accounts
  - payment_line_conflict: try-out page mentions a statement descriptor
- evidence:
  - [2] 2026-10-23: '30 gigabytes free', 'No auto billing', 'Absolutely free'; 7 days; 500 mbit; 4084 days; 'You can't use a VPN or proxy server to register'; 'Total cost: FREE'
  - [1] 2026-10-23: Junior EUR 2.46/mo 40 Mbit 25 connections; Medior EUR 3.69/mo 80 Mbit 25 connections; Senior EUR 5.75/mo unlimited 50 connections; 4085 days
  - [3] 2026-10-23: 'Can I try your service before I pay? Hell yes!'; 'It is possible to set an automatic payment? We choose not to.'
- sources:
  - [1] https://usenet.agency/en/
  - [2] https://usenet.agency/en/try-for-free/
  - [3] https://usenet.agency/en/support/?category=payments
