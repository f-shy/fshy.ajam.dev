# Rainyun

> rainyun.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rainyun/ | JSON https://fshy.ajam.dev/api/v1/entity/rainyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rainyun

- `compute/rainyun` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone yes, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.rainyun.com/
- free tier: A one-yuan one-day trial of each product, quoted 一元试用 and 我们为您提供一元试用体验保障, with a seven-day no-reason refund stated as 7天无理由, on a ladder whose lowest cloud server is advertised at CNY 15 a month and whose lowest shared host is CNY 8 a month. The operator states five years of trading, 30,000 sites hosted and hold its own mainland licences. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: The trial is one day per product and one purchase per account, so it demonstrates the machine rather than running it; the standing constraint is the monthly invoice, and the free part of the offer is the refund window. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id | detail: Mainland host selling in CNY with a stated ISP, IDC and CDN licence and invoicing, which in practice requires real-name registration; the signup page was not read, so the exact document is not established. A 2019 forum post describes email plus phone verification with a CNY 10 balance for the first month.
- interface: unknown
- limits:
  - retention-clamped (binding): The trial is one day per product and one purchase per account, so it demonstrates the machine rather than running it; the standing constraint is the monthly invoice, and the free part of the offer is the refund window. [1]
- limits note: The trial is one day per product and one purchase per account, so it demonstrates the machine rather than running it; the standing constraint is the monthly invoice, and the free part of the offer is the refund window.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The CNY 1 day is enough to benchmark the mainland latency of a HK or JP node before paying for a month, which is the only cheap way to test a route without a card.
- reliability: no reliability event recorded
- notes: The CNY 15/month floor is taken from the storefront mirror because the main site renders prices in script; the figure is quoted as written and not converted. The one-yuan trial limits are three refunds per account and one trial per product, quoted from the vendor forum.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: trial
- evidence:
  - [1] 2026-10-22: page states 一元试用 and 七天无理由退订保证 (seven-day no-reason cancellation), plus 五年运营经验 and 超过30,000个网站在雨云运行, quoted
  - [2] 2026-10-22: a mirror of the storefront lists 虚拟主机 最低 8¥ /月 起 and 云服务器 最低 15¥ /月 起, quoted from the snippet
  - [3] 2026-10-22: the vendor forum states 可7天内无理由退款（每个账号限3次） and 云服务器/游戏云产品可1元试用一天（每款限1次）, quoted
  - [4] 2026-10-22: a 2019 forum post describes the signup route as email plus phone verification with a CNY 10 balance, which is the earliest record and is kept as history rather than as current terms
- sources:
  - [1] https://www.rainyun.com/
  - [2] https://www.rainyun.com.cn/
  - [3] https://forum.rainyun.com/t/topic/12461
  - [4] https://hostloc.com/thread-628983-1-1.html
