# Uploady.io

> uploady.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploady/ | JSON https://fshy.ajam.dev/api/v1/entity/uploady.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Uploady.io

- `debrid/uploady-io` | qualifies | evidence documented | binding volume-quota | category file host (premium one-time) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://uploady.io/premium.html
- price USD 14.99 per 30 days for 50 GB/day | parsed USD 14.99/mo
- free tier: 'Upload files instantly and share secure download links. Free file upload platform with fast speeds, large file support, and no sign-up required.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: No free allowance is printed; the premium block is what names a number.
- per-object cap: not stated on the page read | source: [2]
- retention: not stated on the page read | source: [2]
- egress: Premium: '30-Day Premium 50.00 GB/day'. The four things premium buys are listed as 'Faster download speed', 'No waiting or countdowns', 'High-volume daily traffic', 'Ad-free experience'. | metered: yes | free allowance: none published | source: [2]
- identity: card | detail: Payment methods on the premium page: credit card through Stripe (two variants, 'No Fees' and 'Low Fees'), Byteseller, PayPal through Patreon, and Apple/Google Pay. Free upload needs no account.
- interface: unknown
- limits:
  - volume-quota (binding): 50 GB per day on the 30-day premium [2]
  - per-ip-shaping: free tier has a wait/countdown and an ad layer; premium removes both [2]
- limits note: Only one paid period ($14.99 / 30 days) is offered on the page read; there is no annual plan and no traffic top-up.
- binding note: 50 GB/day is 1.46 TB a month, above the 1 TiB monthly volume. Nothing in the vocabulary fails at this scale on premium; the free tier has no published number to bind against.
- interface detail: Web upload with no signup required for free use; premium is attached to an account. No API published.
- tooling: Browser only as read. The host is on the Leechall generator list, which is the scripted path found.
- composes with: 50 GB/day for $14.99 is the cheapest per-GB-per-day in tested services after Drop Download, and the free tier needs no account at all, which makes it the lowest-identity way to hand a file to somebody.
- reliability: The free tier needs no account, so a link has no owner to appeal to; a removal cannot be contested by the uploader.
- notes: The Stripe 'Low Fees' variant exists because the 'No Fees' variant passes the processor cost on; the checkout totals differ by the fee, not the plan.
- evidence note: Price and daily volume read on the vendor premium page. The free tier's actual ceiling and the per-file cap are unread.
- extras:
  - plans: 30 days $14.99, 50 GB/day
  - payments: Stripe (No Fees / Low Fees), Byteseller, PayPal via Patreon, Apple/Google Pay
  - anonymous_upload: yes
- evidence:
  - [2] 2026-10-23: '30-Day Premium 50.00 GB/day · One-time · No subscription $14.99', the four premium features, and the payment list
  - [1] 2026-10-23: 'no sign-up required' for free upload and the free account offer
- sources:
  - [1] https://uploady.io/
  - [2] https://uploady.io/premium.html
