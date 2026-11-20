# Turbobitpremium.org

> turbobitpremium.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/turbobitpremium/ | JSON https://fshy.ajam.dev/api/v1/entity/turbobitpremium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Turbobitpremium.org

- `debrid/turbobitpremium-org` | paid-only | evidence documented | binding volume-quota | category Turbobit Turbo-access reseller (brand-name reseller site) | tier 1 / 6 / 12 / 24 months of Turbo access
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:10:00.226Z (live) | stale on 2026-11-23
- url https://turbobitpremium.org/
- price USD 9.95 per month at the 1-month term; USD 3.75/month at the 24-month term | parsed USD 3.75/mo
- free tier: None. Four paid terms only, from $9.95 for one month. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: 'up to 100 GB single file transfer / unregistered users up to 20 MB' | source: [1] | note: The vendor's own sentence; it describes transfer, and no single-object cap is stated as a hard number.
- retention: not stated; the reseller sells access time, not storage | source: [2] | note: unstated
- egress: 'download speed up to 1Gbit/sec' with Turbo access; no byte quota published on the pricing block | metered: no | free allowance: none | source: [1]
- identity: email | detail: Either a turbobit.net account or a guest purchase that emails a Turbo code; the reseller's own checkout could not be read, so an extra gate cannot be excluded.
- interface: unknown
- limits:
  - volume-quota (binding): the reseller sells access terms (1, 6, 12, 24 months), not traffic; any traffic cap is Turbobit's and was not read [1]
- limits note: No concurrent-download or daily-traffic number is published by the reseller.
- binding note: At 1 TiB/month the only thing this shop defines is the access term; the traffic rule lives behind Turbobit's own checkout and is not restated here, so the term - not a rate - is what a client buys and what expires.
- interface detail: A Turbo code or an account upgrade entered at turbobit.net; the reseller itself is a shop page plus a /turbo/ checkout that renders from JavaScript.
- tooling: Browser. The FAQ explains the two delivery modes: code into a guest checkout, or automatic upgrade of a registered turbobit.net account.
- composes with: The cheapest documented USD route to Turbobit premium at the long end ($89.95 for 2 years = $3.75/month), and the price anchor against which the Russian resellers among debrid providers should be judged.
- reliability: The name implies it is Turbobit's own premium site but it is a separate shop; its own news page warns that free 'premium account generators' for Turbobit are a trap, which is at least consistent with it being a paid reseller rather than a generator.
- notes: This is the only page in the sector where a Turbobit price is stated in plain HTML at a stable URL, which is why it carries the price other records refer to. It is not in Turbobit's own reseller filter as far as the pages read could show, so 'reseller' here means 'a shop that sells Turbo codes', not 'an officially listed partner'. Payment methods: unverified.
- evidence note: All four prices are quoted verbatim from the live home page today. The payment methods are not: the /turbo/ checkout answered 200 with a 2.7 KB shell. A checkout read would complete the record.
- evidence:
  - [1] 2026-10-23: 1 MONTH $9.95, 6 MONTHS $34.95, 1 YEAR $59.95, 2 YEARS $89.95, and 'up to 100 GB single file transfer / unregistered users up to 20 MB'
  - [2] 2026-10-23: the two delivery modes (auto-upgrade of a registered account, or a Turbo code entered at the download page) and that a code extends the same account on each purchase
  - [3] 2026-10-23: the reseller's own warning that 'free Turbobit premium account generators' are not a legitimate route
- sources:
  - [1] https://turbobitpremium.org/
  - [2] https://turbobitpremium.org/faq/
  - [3] https://turbobitpremium.org/news/free-turbobit-premium-account-generators/
