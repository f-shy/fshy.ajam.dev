# Filer.net

> filer.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filer/ | JSON https://fshy.ajam.dev/api/v1/entity/filer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filer.net

- `debrid/filer-net` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category file host (Swiss-operated, premium one-time) | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:38.368Z (live) | stale on 2026-12-26
- url https://filer.net/
- price EUR 9.99 per 30 days, no volume figure published | parsed USD 11.26/mo
- free tier: 'Filer.net is a worldwide cloud service available to all users for free. Registration is required to upload files.' The free plan is named 'FREE Unlimited Basic' with unlimited storage. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: Premium buys speed, parallel downloads and no wait time, not more space.
- per-object cap: not stated on the page read | source: [1]
- retention: not stated on the page read | source: [1]
- egress: Premium is sold on four features only: 'Maximum Speed', 'Parallel Downloads', 'No Wait Time', 'Download Manager'. No byte allowance appears for either tier, so the free tier is throttled and the paid tier is not, but neither is metered. | metered: no | free allowance: unlimited storage on the free plan; no transfer figure published | source: [1]
- identity: email | detail: 'Registration is required to upload files'. The sign-up form requires an email address; the API takes the same email and password as HTTP Basic credentials.
- interface: browser, rest
- limits:
  - per-ip-shaping (binding): free tier is speed-limited and serialised; premium adds 'Maximum Speed' and 'Parallel Downloads' with the amount unstated [1]
  - write-gated: 'Registration is required to upload files' [1]
- limits note: 'Unlimited' storage is the vendor's word; no per-file cap and no retention period is printed on the page read.
- binding note: With storage unlimited and transfer unmetered, the only thing that can fail at 1 TiB a month is the speed cap on the free tier. The premium tier removes it and the page then names no further constraint.
- interface detail: Web upload with a download manager and a documented REST API on filer.net/api with status, folder and download-link endpoints.
- tooling: The vendor publishes a REST API on filer.net/api that most endpoints reach with HTTP Basic credentials; no rclone backend was found. Filer.net is also on the PrimeLeech generator list.
- composes with: Free unlimited storage with registration is the unusual part: it is a place to park files rather than to move them. Premium at €9.99 a month removes the throttle when a pull has to finish tonight.
- reliability: Unlimited free storage with no published retention rule means files can be removed on a policy the user never sees; the page states none.
- notes: Operated by FITSCHIGOGERL SA, Geneva, per the page footer. Web upload uses a download manager; a REST API is documented at filer.net/api.
- evidence note: Prices and the four premium features read on the vendor home page. The per-file cap, retention and the actual free speed are all unread.
- extras:
  - plans: 2 days €4.99; 30 days €9.99; 90 days €19.99; 365 days €49.99
  - annual_effective_monthly: EUR 4.11
  - vouchers: the 90-day and 365-day purchases include a 14-day and a 30-day voucher respectively
- evidence:
  - [1] 2026-10-23: 'No hidden costs!', the 'FREE Unlimited Basic' plan, and the four prices: 4.99 € 2 days, 9.99 € 30 days, 19.99 € 90 days, 49.99 € 365 days
  - [2] 2026-11-25: the published API uses email and password basic authentication | capture: sha256:cd77bcb9358605e625b724502517e72682f593d9ffff5d30dafc090cc4e730e3 | quote: Most endpoints require HTTP Basic Authentication with your Filer.net credentials (email and password).
  - [3] 2026-11-25: the sign-up form requires an email address | capture: sha256:6e89b8e8cf1025fb51739444ea73ebecabe626c342ca7511d8fdcdb4eb59bac9 | quote: Email address is required
  - [1] 2026-11-25: the free tier requires registration to upload | capture: sha256:aa8a8476f4975e3097173e776ba6f2cad91468ab7915e9984b19db2c2e5e8b72 | quote: Filer.net is a worldwide cloud service available to all users for free. Registration is required to upload files.
  - [1] 2026-11-25: the 365-day premium plan is priced at EUR 49.99 | capture: sha256:aa8a8476f4975e3097173e776ba6f2cad91468ab7915e9984b19db2c2e5e8b72 | quote: 49.99 €
  - [1] 2026-11-25: the 365-day plan includes a 30-day voucher | capture: sha256:aa8a8476f4975e3097173e776ba6f2cad91468ab7915e9984b19db2c2e5e8b72 | quote: Includes voucher for 30 days!
  - [3] 2026-11-25: the terms require a registered account to use the service | capture: sha256:6e89b8e8cf1025fb51739444ea73ebecabe626c342ca7511d8fdcdb4eb59bac9 | quote: Use requires registration of a user account.
- sources:
  - [1] https://filer.net/
  - [2] https://filer.net/api
  - [3] https://filer.net/user/register
