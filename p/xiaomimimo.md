# Xiaomi MiMo API Open Platform

> xiaomimimo.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xiaomimimo/ | JSON https://fshy.ajam.dev/api/v1/entity/xiaomimimo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Xiaomi MiMo API Open Platform

- `inference/xiaomi-mimo-api` | trial-only | evidence documented | binding volume-quota | category inference API, one-time free credit
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T11:30:43.059Z (live) | stale on 2026-12-04
- url https://platform.xiaomimimo.com/
- free tier: One-time free credits for all new and existing users, collected on the console Balance page, announced with the start of billing. No vendor page read states the amount of this credit. The promotions FAQ states that bonus credit from new user registration or Refer & Earn is currently valid for 40 days; the expiry of the January 2026 one-time credit itself is not stated. Calls deduct the complimentary free quota first and then the recharged balance, and an account with insufficient balance cannot use the API | unit: mixed | metered on: unstated | read on: 2026-10-28 | source: [1] | note: one-time-credit
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: overseas users register a Xiaomi account by email or by Google or Facebook sign-in; mainland users by mobile number or third-party sign-in. Real-name authentication applies to mainland users before recharging or buying a package, and overseas users recharge without it
- interface: rest
- limits:
  - volume-quota (binding): unverified: no vendor page read states the amount of the one-time free credit or the expiry of the January 2026 grant (one news site reports a figure received by one user); after the credit is used the account needs a recharged balance [1]
- binding note: the one-time credit is the only free allowance and its size is unpublished on the page read
- tooling: part of the free tier
- composes with: mainland and overseas accounts have separate base URLs and keys, so usage and credit do not aggregate across regions
- reliability: an automatic keyword-based protection mechanism can block an account as abnormal usage until the vendor reviews it on request
- notes: overseas first-recharge bonus: USD 0.72 once per account on a first top-up of any amount, valid 40 days; it needs a payment so it is not a card-free credit
- evidence note: the billing notice is dated January 23, 2026; whether the credit is still granted is unverified
- evidence:
  - [1] 2026-10-28: free credits are offered to all new and existing users | capture: sha256:9392eb0712c5b3455e09d728879f6d28fe01811197058b4c2500964a8304b276 | quote: To thank you for your support, we have prepared exclusive free credits for all new and existing users.
  - [1] 2026-10-28: only mainland users need real-name authentication before recharging | capture: sha256:9392eb0712c5b3455e09d728879f6d28fe01811197058b4c2500964a8304b276 | quote: Other users can recharge directly without real-name authentication.
  - [1] 2026-10-28: overseas mimo-v2-flash list price in USD per million tokens | capture: sha256:9392eb0712c5b3455e09d728879f6d28fe01811197058b4c2500964a8304b276 | quote: Overseas: Input $0.1 / 1M tokens, Input (Cache Hit) $0.01 / 1M tokens, Output $0.3 / 1M tokens
  - [2] 2026-10-28: the FAQ lists a separate registration method for overseas users | capture: sha256:960d475c24eb3523f528bc71d293fba23867a91fd97a88e0fc9056a651ee8550 | quote: Registration Methods for Overseas Users
  - [2] 2026-10-28: mainland and overseas accounts use separate base URLs and keys | capture: sha256:960d475c24eb3523f528bc71d293fba23867a91fd97a88e0fc9056a651ee8550 | quote: Return different Base URLs + Keys based on the region where the account is located, which are not interoperable.
  - [2] 2026-10-28: accounts can be blocked by an automatic protection mechanism | capture: sha256:960d475c24eb3523f528bc71d293fba23867a91fd97a88e0fc9056a651ee8550 | quote: It may be because the system captured certain keywords during detection, triggering the automatic protection mechanism.
  - [3] 2026-11-03: bonus credit from new user registration or Refer & Earn is currently valid for 40 days | capture: sha256:b319d04aee7715f584de56d12ec585532eb2d508e5443a0afb86ede888614faf | quote: Bonus credit is currently valid for 40 days and expires after that.
  - [1] 2026-11-03: the vendor notice offers free credits to all new and existing users and states no amount | capture: sha256:9392eb0712c5b3455e09d728879f6d28fe01811197058b4c2500964a8304b276 | quote: To thank you for your support, we have prepared exclusive free credits for all new and existing users.
  - [4] 2026-11-03: overseas first-recharge bonus is USD 0.72 and needs a first top-up | capture: sha256:29005f456884c666ce06d96f2bedbe5b5a26f279e52ed4f2b99c4a26b784359c | quote: Overseas users who make their first recharge of any amount on the Xiaomi MiMo Open Platform will receive an additional $0.72 bonus, which will be credited to their account in real time.
  - [5] 2026-11-03: a news site reports a user received 20 yuan of the free balance; not stated by the vendor | capture: sha256:0af7bd06ac21e6162ff3790250eafd595b8f40c95ea6b82354ef9b7b00da7835 | quote: 有IT之家小伙伴已经领取到了 20 元赠送余额
- sources:
  - [1] https://mimo.mi.com/docs/en-US/news/previous-news/billing
  - [2] https://mimo.mi.com/docs/quick-start/faq/account
  - [3] https://mimo.mi.com/docs/en-US/quick-start/faq/promotions
  - [4] https://mimo.mi.com/docs/en-US/quick-start/promotions/Welcome%20Bonus
  - [5] https://www.ithome.com/0/914/844.htm
