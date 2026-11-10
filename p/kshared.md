# Kshared

> kshared.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kshared/ | JSON https://fshy.ajam.dev/api/v1/entity/kshared.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kshared

- `debrid/kshared` | qualifies-with-caveat | evidence documented | binding volume-quota | category file host (Korean-market, premium subscription) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://www.kshared.com/premium
- price EUR 17.95 per month for 1 TB stored and 35 GB/day | parsed USD 20.09/TB-mo
- free tier: Account creation is free ('Create Account') and the site offers 'Share any number of files in seconds. View over 200 file types online.'; no free allowance is given in the plan block. | unit: TB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not stated on the page read | source: [1]
- retention: not stated on the page read | source: [1]
- egress: Every plan carries '35GB/Daily Bandwidth'. No per-byte price is stated; the plan price is flat. | metered: yes | free allowance: none published | source: [1]
- identity: card | detail: Free signup, paid plan at checkout. Payment processors were not listed on the page read.
- interface: unknown
- limits:
  - volume-quota (binding): 35 GB per day of download bandwidth [1]
  - volume-quota (binding): 1 TB of storage on the 1-month plan [1]
- limits note: The plan block on the page read showed the 1-month tier; the longer tiers were behind the same 'Select a Plan' step and were not expanded.
- binding note: 35 GB/day against a 34.1 GB/day requirement for 1 TiB a month leaves under 1 GB a day of slack. Storage and transfer are the same figure, so a full month cannot keep a full month's data.
- interface detail: Web drive ('CloudDrive'), web upload, and a share link. No API or FTP path is published on the pages read.
- tooling: Browser only as read. Kshared is on the Leechall generator list, so a leecher is the fallback.
- composes with: The same product as Emload at the same price, so a client picks whichever local-market releases it needs. 35 GB/day puts it in the top-up role, not the bulk role.
- reliability: Referral programme pays 20% of a referred user's purchase, which means the signup flow is built to be shared; treat any third-party 'free premium' offer for the host as an affiliate link.
- notes: Emload and Kshared share the plan name 'CloudFLA', the same €17.95, the same 35 GB/day and the same page structure. Recorded separately because a client meets two domains and needs to know they are one purchase.
- evidence note: Plan price and the daily bandwidth figure read on the vendor premium page. The 3/6/12-month tiers were not expanded, so only the 1-month price is recorded.
- extras:
  - referral_share: 20% of each referred purchase
  - twin_site: emload.com
  - plan_name: CloudFLA
- evidence:
  - [1] 2026-10-23: '1 Month €17.95', '1 TB Storage', '35GB/Daily Bandwidth', 'No captcha codes' in the Kshared plan block
  - [2] 2026-10-23: the identical plan and price on a sibling site, which is why the two records describe one product
- sources:
  - [1] https://www.kshared.com/premium
  - [2] https://www.emload.com/v2/
