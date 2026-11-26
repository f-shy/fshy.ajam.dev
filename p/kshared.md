# Kshared

> kshared.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kshared/ | JSON https://fshy.ajam.dev/api/v1/entity/kshared.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kshared

- `debrid/kshared` | qualifies-with-caveat | evidence documented | binding volume-quota | category file host (Korean-market, premium subscription) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:46:38.368Z (live) | stale on 2026-12-26
- url https://www.kshared.com/premium
- price EUR 17.95 per month for 1 TB stored and 35 GB/day | parsed USD 20.22/TB-mo
- free tier: Account creation is free ('Create Account') and the site offers 'Share any number of files in seconds. View over 200 file types online.'; no free allowance is given in the plan block. | unit: TB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: 'No file size limits' is stated for all Kshared plans on the premium page; no numeric cap is published. | source: [1]
- retention: not stated on the page read | source: [1]
- egress: Every plan carries '35GB/Daily Bandwidth'. No per-byte price is stated; the plan price is flat. | metered: yes | free allowance: none published | source: [1]
- identity: card | detail: Free signup through a Create Account page; paid plan at checkout. The payment link is provided by chat or an authorized reseller Telegram account; the checkout names PayPal and asks for VPN or proxy to be disabled.
- interface: browser
- limits:
  - volume-quota (binding): 35 GB per day of download bandwidth [1]
  - volume-quota (binding): 1 TB of storage on the 1-month plan [1]
- limits note: All four tiers are visible on the premium page. The payment link is obtained through chat or an authorized reseller on Telegram.
- binding note: 35 GB/day against a 34.1 GB/day requirement for 1 TiB a month leaves under 1 GB a day of slack. Storage and transfer are the same figure, so a full month cannot keep a full month's data.
- interface detail: Web drive ('CloudDrive'), web upload, and a share link. No API or FTP path is published on the pages read.
- tooling: Browser only as read. Kshared is on the Leechall generator list, so a leecher is the fallback.
- composes with: The same product as Emload at the same price, so a client picks whichever local-market releases it needs. 35 GB/day puts it in the top-up role, not the bulk role.
- reliability: Referral programme pays 20% of a referred user's purchase, which means the signup flow is built to be shared; treat any third-party 'free premium' offer for the host as an affiliate link.
- notes: Emload and Kshared share the plan name 'CloudFLA', the same €17.95, the same 35 GB/day and the same page structure. Recorded separately because a client meets two domains and needs to know they are one purchase. No programmatic path found: Web drive ('CloudDrive'), web upload, and a share link. No API or FTP path is published on the pages read.
- evidence note: Plan price and the daily bandwidth figure read on the vendor premium page. The 3/6/12-month tiers were not expanded, so only the 1-month price is recorded.
- extras:
  - referral_share: 20% of each referred purchase
  - twin_site: emload.com
  - plan_name: CloudFLA
- evidence:
  - [1] 2026-10-23: '1 Month €17.95', '1 TB Storage', '35GB/Daily Bandwidth', 'No captcha codes' in the Kshared plan block
  - [2] 2026-10-23: the identical plan and price on a sibling site, which is why the two records describe one product
  - [1] 2026-11-25: the plan page states no per-file size limit | capture: sha256:76f4b2419cf6286337358c67940bf7d02f3acbcec81ee5594c5e8890a39cd0c2 | quote: No file size limits
  - [1] 2026-11-25: the payment link is supplied through chat or an authorized reseller Telegram account | capture: sha256:76f4b2419cf6286337358c67940bf7d02f3acbcec81ee5594c5e8890a39cd0c2 | quote: To get the payment link. kindly contact our chat or our authorized reseller through their Telegram account.
  - [1] 2026-11-25: every plan carries 35GB of daily download bandwidth | capture: sha256:76f4b2419cf6286337358c67940bf7d02f3acbcec81ee5594c5e8890a39cd0c2 | quote: ## 35GB/Daily Bandwidth
  - [1] 2026-11-25: the 1-month plan is priced at EUR 17.95 | capture: sha256:76f4b2419cf6286337358c67940bf7d02f3acbcec81ee5594c5e8890a39cd0c2 | quote: ## €17.95
  - [1] 2026-11-25: the checkout names PayPal and asks that VPN or proxy be disabled | capture: sha256:76f4b2419cf6286337358c67940bf7d02f3acbcec81ee5594c5e8890a39cd0c2 | quote: Kindly disable vpn/proxy before continue otherwise the PayPal method will not work.
  - [3] 2026-11-25: the referral programme pays 20 percent of a referred purchase | capture: sha256:c9be128949dfd02b0568338630d3863eb6c041e016850ce5f662eda8062f3ee0 | quote: ## Earn 20% of the revenue from each purchase made by a user you have referred to Kshared.
  - [4] 2026-11-25: the sign-up page offers a Create Account action | capture: sha256:da77ee915e2e261ba263bc618f00755fd47077545837460626adae5245c6268b | quote: [Create Account](https://www.kshared.com/account/signup)
  - [5] 2026-11-25: a third-party leecher still lists kshared as a supported host | capture: sha256:d8bf63f755d814642dc9a8e0b3c6a5e73d73009145cafcb9b09340ebcd64cf2f | quote: kshared.com premium link generator
- sources:
  - [1] https://www.kshared.com/premium
  - [2] https://www.emload.com/v2/
  - [3] https://www.kshared.com/
  - [4] https://www.kshared.com/account/signup
  - [5] https://leechall.com/
