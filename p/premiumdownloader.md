# Premium Downloader

> premiumdownloader.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/premiumdownloader/ | JSON https://fshy.ajam.dev/api/v1/entity/premiumdownloader.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Premium Downloader

- `debrid/premiumdownloader-net` | paid-only | evidence documented | binding volume-quota | category pay-per-file premium download service (no subscription, no account) | tier pay-per-file
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-23
- url https://premiumdownloader.net/
- free tier: None. 'No subscriptions - you pay per file, only for what you actually grab.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not stated: the price is computed per file from its size ('we check the file and price in real time') | source: [1]
- retention: not stated; the link is shown on-page and emailed | source: [1]
- egress: Each download is priced individually; balance top-ups carry a bonus (+10% from $10, +15% from $20, +20% from $50) and paying from balance is fee-free. | metered: yes | price per TB: not published as a rate; priced per file | source: [1]
- identity: anonymous | detail: 'no signup' and 'no accounts to create'; the download link is emailed, so an email address is optional rather than required, and payment is by crypto or PayPal.
- interface: unknown
- limits:
  - volume-quota (binding): pay per byte, priced per file; no free allowance [1]
- limits note: 'Works with 155+ hosts'; no monthly cap, no concurrency figure, no per-host limits published.
- binding note: Money is the counter: every byte is bought, so at 1 TiB a month the constraint is the invoice rather than a rate or a shaping rule. The site publishes no per-GB rate, so the invoice cannot be predicted without submitting a file.
- interface detail: Web form only; payment by Crypto (Cryptomus: USDT, BTC, ETH) or PayPal. No API is documented.
- tooling: Browser only; no download-manager integration named.
- composes with: It is the only service here that turns a single file into a known cash price before download, which makes it the fallback when a subscription's host list fails and one file must still arrive.
- reliability: Pay-per-file removes subscription risk but leaves balance risk: a top-up bonus encourages prepaying into a wallet held by an operator with no status page.
- notes: The absence of a published per-GB rate is the finding: the same service sells files at a price it computes at submission time, so a client cannot budget a terabyte month without sampling. Useful as a one-file fallback, not as a base.
- evidence note: The pay-per-file model, the host count, the top-up bonuses and the payment rails are vendor-stated and read. The actual price of any file was not measured because that requires submitting a link and a payment.
- evidence:
  - [1] 2026-10-23: 'No subscriptions - you pay per file', 'Works with 155+ hosts', the top-up bonuses (+10/+15/+20%), Cryptomus and PayPal rails, 'no signup'
- sources:
  - [1] https://premiumdownloader.net/
