# LycheeIP

> lycheeip.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lycheeip/ | JSON https://fshy.ajam.dev/api/v1/entity/lycheeip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LycheeIP

- `ip-proxy/lycheeip-residential` | trial-only | evidence reported | binding per-ip-shaping | category per-GB dynamic residential and per-IP monthly static residential proxy (Chinese market) | tier Dynamic per GB and static per IP per month
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T07:35:32.366Z (live) | stale on 2026-11-18
- url https://www.lycheeip.com/
- free tier: The menu offers "动态住宅代理送500MB体验" (dynamic residential proxy, 500 MB trial). Prices for the dynamic (per GB), static residential (per IP per month, unlimited traffic) and static datacenter products are not in the page text the reader returned: unverified: the pricing path returned the site 404 page. | unit: MB | metered on: unstated | read on: 2026-11-03 | source: [1] | note: A read of the pricing path returned the site 404 page with its menu; no price was captured.
- per-object cap: not applicable: an address or a traffic pack, not an object | source: [1]
- retention: not applicable: addresses and traffic, not stored bytes. unverified: the term of a static IP. | source: [1] | note: days is null because no bytes are stored.
- egress: Dynamic: billed by traffic ("按流量计费"). Static: billed per IP per month with unlimited traffic ("按IP包月计费（不限流量）"). | metered: yes | free allowance: 500 MB dynamic residential trial | source: [1]
- identity: email | detail: No card or ID document is asked on that page.
- interface: cli, rest
- limits:
  - per-ip-shaping (binding): static IPs are exclusive during the term ("使用期限内保证独享") with unlimited traffic [1]
  - volume-quota: dynamic residential is metered per GB; the pack sizes and prices are unverified [1]
- binding note: The prices were not read, so the number that binds is unverified; the stated shape is one exclusive address per unit for the static product.
- interface detail: http/https/socks5, stated on the page, and an API for automated purchase and management ("API对接，支持自动化采购管理"), plus a documentation centre.
- tooling: Any client that speaks SOCKS5 or an HTTP proxy, reached from a Worker through a relay that dials SOCKS5. The vendor also sells cloud phones, which are a separate product.
- composes with: The upstream sees a pooled dynamic address or an exclusive static address. The static product is labelled "真实住宅ISP代理 100%真人住宅属性" (real residential ISP proxy); no delivered address was seen, so the class is unverified.
- reliability: No measurement was made. A forum thread calls a static line of this vendor a pseudo-residential address; that is a third-party report and was not verified.
- notes: Named on the Chinese-language forum source in a thread offering a static line of this vendor for resale. The forum is the lead; the evidence is the vendor page. The pricing route needs a rendered read.
- evidence note: The product labels and the registration route are first-party reads from 2026-11-03; no price was captured, so the record stays at reported until the pricing page is read.
- extras:
  - rung: 5
  - rung_note: The static product is a registration-class claim; nothing was looked up.
  - pool_claim: 85 million dynamic IPs, 190+ countries
- evidence:
  - [2] 2026-11-03: The site menu offers the dynamic residential product with a 500 MB trial. | capture: sha256:b5ebba9ab224552ba4ec1f5d977e3df5f1be827a1397fd4d10bf046bff41dfca | quote: 动态住宅代理送500MB体验
  - [2] 2026-11-03: The site menu lists the static product as billed per IP per month with unlimited traffic. | capture: sha256:b5ebba9ab224552ba4ec1f5d977e3df5f1be827a1397fd4d10bf046bff41dfca | quote: 按IP包月计费（不限流量）
  - [1] 2026-11-03: The dynamic pool is claimed at 85 million IPs. | capture: sha256:277c55aadd81d9b382656bc0e3d08aae3609d0d90d6fd0f2ac132ad07241ed7e | quote: 稳定安全的8500万全球IP池
  - [3] 2026-11-03: Registration is offered by phone or by email. | capture: sha256:fa8c3f7dd899ab9613b69bdd9a6575307d0c80e0e9ab3930aca8b54926043365 | quote: 手机注册 邮箱注册
- sources:
  - [1] https://www.lycheeip.com/
  - [2] https://www.lycheeip.com/pricing
  - [3] https://www.lycheeip.com/register
