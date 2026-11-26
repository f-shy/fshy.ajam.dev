# Uploady.io

> uploady.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploady/ | JSON https://fshy.ajam.dev/api/v1/entity/uploady.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Uploady.io

- `debrid/uploady-io` | qualifies | evidence documented | binding volume-quota | category file host (premium one-time) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:46:40.369Z (live) | stale on 2026-12-26
- url https://uploady.io/premium.html
- price USD 14.99 per 30 days for 50 GB/day | parsed USD 14.99/mo
- free tier: 'Upload files instantly and share secure download links. Free file upload platform with fast speeds, large file support, and no sign-up required.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: No free allowance is printed; the premium block is what names a number.
- per-object cap: Anon 5120 Mb, Premium 15360 Mb, Registered 10240 Mb per file | bytes: 5368709120 | source: [2]
- retention: Anon files 3 days, Premium 60 days, Registered 30 days after last download | days: 3 | source: [2]
- egress: Premium: '30-Day Premium 50.00 GB/day'. The four things premium buys are listed as 'Faster download speed', 'No waiting or countdowns', 'High-volume daily traffic', 'Ad-free experience'. | metered: yes | free allowance: none published | source: [2]
- identity: card | detail: Payment methods on the premium page: credit card through Stripe (two variants, 'No Fees' and 'Low Fees'), Byteseller, PayPal through Patreon, and Apple/Google Pay. Free upload needs no account.
- interface: browser
- limits:
  - volume-quota (binding): 50 GB per day on the 30-day premium [2]
  - per-ip-shaping: free tier has a wait/countdown and an ad layer; premium removes both [2]
- limits note: Only one paid period ($14.99 / 30 days) is offered on the page read; there is no annual plan and no traffic top-up.
- binding note: 50 GB/day is 1.46 TB a month, above the 1 TiB monthly volume. Nothing in the vocabulary fails at this scale on premium; the free tier has no published number to bind against.
- interface detail: Web upload with no signup required for free use; premium is attached to an account. No API published.
- tooling: Browser only as read. The host is on the Leechall generator list, which is the scripted path found.
- composes with: 50 GB/day for $14.99 is the cheapest per-GB-per-day in tested services after Drop Download, and the free tier needs no account at all, which makes it the lowest-identity way to hand a file to somebody.
- reliability: The free tier needs no account, so a link has no owner to appeal to; a removal cannot be contested by the uploader.
- notes: The Stripe 'Low Fees' variant exists because the 'No Fees' variant passes the processor cost on; the checkout totals differ by the fee, not the plan. No programmatic path found: Web upload with no signup required for free use; premium is attached to an account. No API published.
- evidence note: Price and daily volume read on the vendor premium page. The free tier's actual ceiling and the per-file cap are unread.
- extras:
  - plans: 30 days $14.99 50 GB/day; 30-day Pro $27.99 100 GB/day; 90 days $35.99 75 GB/day; 90-day Pro $69.99 150 GB/day; 180 days $59.99 100 GB/day; 180-day Pro $99.99 200 GB/day; 365 days $89.99 150 GB/day; 365-day Pro $149.99 300 GB/day
  - payments: Stripe (No Fees / Low Fees), Byteseller, PayPal via Patreon, Apple/Google Pay
  - anonymous_upload: yes
- evidence:
  - [2] 2026-10-23: '30-Day Premium 50.00 GB/day · One-time · No subscription $14.99', the four premium features, and the payment list
  - [1] 2026-10-23: 'no sign-up required' for free upload and the free account offer
  - [2] 2026-11-25: the 30-day premium is USD 14.99 for 50 GB per day | capture: sha256:32be6a32f82503abfae8f9946deb5e8ce7e6bf863dc798c80ee0a6e26563be91 | quote: 30-Day Premium 50.00 GB/day · One-time · No subscription $14.99
  - [2] 2026-11-25: premium buys speed, no waiting, daily traffic and no ads | capture: sha256:32be6a32f82503abfae8f9946deb5e8ce7e6bf863dc798c80ee0a6e26563be91 | quote: * Faster download speed * No waiting or countdowns * High-volume daily traffic * Ad-free experience
  - [2] 2026-11-25: per-file caps by account: Anon 5120 Mb, Premium 15360 Mb, Registered 10240 Mb | capture: sha256:32be6a32f82503abfae8f9946deb5e8ce7e6bf863dc798c80ee0a6e26563be91 | quote: | Max upload file size 5120 Mb 15360 Mb 10240 Mb
  - [2] 2026-11-25: file retention by account: Anon 3 days, Premium 60 days, Registered 30 days | capture: sha256:32be6a32f82503abfae8f9946deb5e8ce7e6bf863dc798c80ee0a6e26563be91 | quote: 3 days 60 days 30 days
  - [1] 2026-11-25: upload needs no account | capture: sha256:5c6318b62ebd4b46a7d7fc124b88aea18695daaae23248e29f3cf753a493f25c | quote: No. You can upload and share files instantly without signing up. Just drag, drop, and share.
  - [1] 2026-11-25: registered free files expire after 30 days of no downloads | capture: sha256:5c6318b62ebd4b46a7d7fc124b88aea18695daaae23248e29f3cf753a493f25c | quote: Files expire after 30 days of no downloads
  - [3] 2026-11-25: registration asks for no card | capture: sha256:77bad6e26e4b128de8d7ac81de4aee97936ee60ddebc98af520a645ca01082db | quote: Free forever. No credit card required.
  - [2] 2026-11-25: the Anon per-file cap is 5120 Mb | capture: sha256:32be6a32f82503abfae8f9946deb5e8ce7e6bf863dc798c80ee0a6e26563be91 | quote: 5120 Mb
  - [2] 2026-11-25: retention by account: Anon 3 days, Premium 60 days, Registered 30 days | capture: sha256:32be6a32f82503abfae8f9946deb5e8ce7e6bf863dc798c80ee0a6e26563be91 | quote: 3 days 60 days 30 days
  - [2] 2026-11-25: anonymous files are kept 3 days | capture: sha256:32be6a32f82503abfae8f9946deb5e8ce7e6bf863dc798c80ee0a6e26563be91 | quote: 3 days
- sources:
  - [1] https://uploady.io/
  - [2] https://uploady.io/premium.html
  - [3] https://uploady.io/register.html
