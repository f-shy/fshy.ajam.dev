# Drime

> drime.cloud | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/drime/ | JSON https://fshy.ajam.dev/api/v1/entity/drime.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Drime (Advanced / 10 TB lifetime)

- `storage/drime` | qualifies-with-caveat | evidence documented | binding write-gated | category EU collaborative cloud, lifetime one-time
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:26.263Z (live) | stale on 2026-12-26
- url https://drime.cloud/pricing
- price USD 47.699/TB one-time at 10 TB (USD 476.99)
- free tier: 10TB Lifetime $476.99$1,299.00(63% off) | unit: TB | metered on: unstated | read on: 2026-11-09 | source: [1] | note: Start free with 20 GB. Upgrade when you need more space, more members or more power. Cancel anytime.
- per-object cap: Maximum file size: Unlimited | source: [1] | note: Unlimited
- retention: Restore deleted files 30 days | source: [1] | note: 30 days file history; 90 days file history; 120 days file history
- egress: Unlimited Bandwidth Included | metered: yes
- identity: email | detail: email
- interface: rest, rclone
- limits:
  - write-gated (binding): Review. Shortest track record of any vendor here. [1]
- limits note: Unlimited File Size: Upload large files; no file is ever too big!
- interface detail: Native rclone Tier 1 backend (rclone/rclone backend/drime, integration_tests: Passing, data_integrity: High), plus REST API + webhooks and a documented developer portal
- tooling: rclone native, first-class; API token auth
- composes with: Mount, sync and script Drime storage with rclone
- reliability: Founded 2024 per third-party review. Shortest track record of any vendor here. No data-loss event yet, simply because there is not enough history. Redemption deadline: code must be redeemed within 30 days of purchase.
- notes: Prices go up soon. Get up to 39% off Advanced Lifetime now: 6 TB for $169 or 10 TB for $299, paid once.
- evidence note: the StackSocial page states the current 10 TB lifetime price
- extras:
  - price_verbatim: $3.00/TB at 6 TB subscription (EUR 15.99 = $17.96); one-time $36.00/TB lifetime at 10 TB ($359.97), which amortises to $1.50/TB/mo over 2 years and $0.50/TB/mo over 6 years
- evidence:
  - [2] 2026-10-21: 'Essentials ... EUR 5.50 EUR 4.40 per month, billed annually ... 2 TB of storage'; 'Advanced EUR 19.99 EUR 15.99 per month ... 6 TB'
  - [1] 2026-10-21: 'Deal Price $359.97 ... 10TB'
  - [3] 2026-10-21: 'Advanced - 10TB Lifetime ... $249 ... $360'
  - [4] 2026-10-21: backend: drime, tier: Tier 1, integration_tests: Passing
  - [5] 2026-10-21: native backend docs
  - [1] 2026-11-09: the StackSocial page lists the 10 TB lifetime plan at $476.99 against a $1,299.00 list price, 63% off | capture: sha256:4aeb33f45d16e64fa780e15cb381b436c0b79a480a063079c27e512793e72d74 | quote: [10TB Lifetime $476.99$1,299.00(63% off)]
  - [2] 2026-11-09: the pricing page states the free tier starts at 20 GB and paid plans upgrade it | capture: sha256:30fd1f25069504bbd3d304024d580ce29ad31bf4b23a7445e38741210b44ab69 | quote: Start free with 20 GB. Upgrade when you need more space, more members or more power. Cancel anytime.
  - [1] 2026-11-09: the StackSocial page lists the file size as unlimited | capture: sha256:bbc6a5f822312b8b9cef6e6e4f075c0130527261966c6ee50f03d70ac5337ba7 | quote: Unlimited File Size: Upload large files; no file is ever too big!
  - [3] 2026-11-09: the partner landing states a 6 TB lifetime price of $169 and a 10 TB lifetime price of $299, paid once | capture: sha256:81052b85171773dafe7388eda6917be159ebce17d32dd0d5f4f826c4fea5b8a5 | quote: Prices go up soon. Get up to 39% off Advanced Lifetime now: 6 TB for $169 or 10 TB for $299, paid once.
  - [2] 2026-11-25: the plan comparison lists a 30 day deleted-file restore window | capture: sha256:93bb749cc20e3f3d378c188edcd74bf92d6d956bf4c48881e5249953002feede | quote: Restore deleted files 30 days 30 days 30 days 30 days 30 days
  - [2] 2026-11-25: the plan list states 30, 90 and 120 day file history windows | capture: sha256:93bb749cc20e3f3d378c188edcd74bf92d6d956bf4c48881e5249953002feede | quote: **✓ 30 days file history...✓ 90 days file history...✓ **120 days file history
  - [2] 2026-11-25: the plan comparison lists maximum file size as Unlimited | capture: sha256:93bb749cc20e3f3d378c188edcd74bf92d6d956bf4c48881e5249953002feede | quote: Maximum file size Unlimited Unlimited Unlimited Unlimited Unlimited
  - [2] 2026-11-25: maximum file size is Unlimited in the plan comparison | capture: sha256:93bb749cc20e3f3d378c188edcd74bf92d6d956bf4c48881e5249953002feede | quote: Maximum file size Unlimited Unlimited Unlimited Unlimited Unlimited
  - [2] 2026-11-25: the plan comparison lists Unlimited Bandwidth as included | capture: sha256:93bb749cc20e3f3d378c188edcd74bf92d6d956bf4c48881e5249953002feede | quote: Unlimited Bandwidth Included Included Included Included Included
  - [6] 2026-11-25: the developer page describes rclone scripting of Drime storage | capture: sha256:8135c5aaaaf3dbb6f120f54c83a8473ed9bbb32f7fba11c82953c5b6ea782343 | quote: Advanced users can mount, sync and script their Drime storage with rclone, using the official Drime backend at rclone.org/drime.
  - [6] 2026-11-25: the developer page names a REST API and rclone compatibility | capture: sha256:8135c5aaaaf3dbb6f120f54c83a8473ed9bbb32f7fba11c82953c5b6ea782343 | quote: A REST API, an embeddable signing widget, webhooks for Sign events and rclone compatibility.
- sources:
  - [1] https://www.stacksocial.com/sales/drime-secure-cloud-storage-lifetime-subscription-advanced-plan-10tb
  - [2] https://drime.cloud/pricing
  - [3] https://drime.cloud/kenmoo
  - [4] https://github.com/rclone/rclone/blob/b5a81dab/docs/data/backends/drime.yaml
  - [5] https://rclone.org/drime/
  - [6] https://drime.cloud/developer
