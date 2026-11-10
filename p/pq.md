# pq hosting

> pq.hosting | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pq/ | JSON https://fshy.ajam.dev/api/v1/entity/pq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pq hosting storage vps

- `storage/pq-hosting-storage-vps` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.pq.hosting/storage-vps
- free tier: none reachable: https://www.pq.hosting/storage-vps returned HTTP 404 through the reader. No storage product at that path. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: https://www.pq.hosting/storage-vps returned HTTP 404 through the reader. No storage product at that path.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: https://www.pq.hosting/storage-vps returned HTTP 404 through the reader. No storage product at that path.
- sources:
  - [1] https://www.pq.hosting/storage-vps

## PQ.Hosting

- `compute/pq-hosting` | dead | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://pq.hosting/en
- free tier: No server is sold at this domain. pq.hosting now serves a ranked directory of other hosting providers: the English page title is 'Global Hosting Catalog - Compare VPS, Dedicated Servers & Hosting Providers' and every ranked entry ends in an outbound link of the form https://pq.hosting/go.php?id=<n>. GET /vps resolves to /vps-vds, a 2026 top-20 VPS provider ranking. The legacy sales paths are gone: /promo, /providers and /en/1-euro-vps each returned the site's own 404 template, and a search result still shows /en/1-euro-vps as the 5.77 EUR plan page, which that snippet describes with plan cards (snippet only: the live page is 404, so no plan card was read from the vendor verification). The sitemap has no order, cart, login or account path: it lists the homepage, 6 language homes, /companies, /choose-vps, /choose-dedicated, /contacts, /continents, /help, /dc and 9 pages under /tools (8 network tools plus a russia-block-check). | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable: no capacity is sold at this domain, so there is no egress term to record | metered: no | source: [1]
- identity: anonymous | detail: No account, email or payment is requested on any page read. The 69-provider list, the language homes, the contacts page and the tools all render without a session, and the only outbound action is a go.php redirect to the listed vendor's own site, where whatever identity that vendor wants applies.
- interface: rest
- limits note: Nothing is sold at this domain, so none of the seven constraint kinds decides anything here. The pages publish no quota, port speed or object cap because there is no product to attach one to.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: no API and no client area of its own; the only outbound mechanism is the go.php redirect. Automated use would be scraping a static directory. That is a tooling note, not a verdict.
- composes with: nothing to chain as compute. The reusable asset is discovery: 69 named providers over country, city, datacenter and ranking pages in 6 languages, plus 9 tool pages (dns-ip-lookup, ssl-tls-check, rbl-check, speed-test, ping-traceroute, http-redirect-check, subnet-calculator, my-ip, russia-block-check).
- reliability: no reliability event observed at this domain; it answers 200 on every page read, including its own 404 template, so a 200 here does not mean a product exists.
- notes: The domain is alive and the vendor function is gone. Routes tried, all from the repo root: read / (exit 0), /en (0), /vps (0, final_url https://pq.hosting/vps-vds), /companies (0), /contacts (0), /help (0), /sitemap.xml (0), /sitemap-main.xml (0), /sitemap-providers.xml (0), /providers/the-hosting (0, final_url https://pq.hosting/), and /promo and /providers (exit 1, origin 404). The English page is a full translation of the Russian one, not a thin stub, so both agree. The contacts page lists info@pq.hosting, partners@pq.hosting and t.me/pqhosting, with a form topic rendered in Russian for partnership and sales. This record is 'dead' in the compute sense, meaning no capacity is purchasable at the domain, not that the domain is offline. The strongest reading of the evidence is a rebrand that split the brands, and that is recorded as an inference, not as a measured fact, in the the.hosting finding.
- extras:
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: the page identifies itself as a directory, not a vendor: title 'Global Hosting Catalog - Compare VPS, Dedicated Servers & Hosting Providers', description 'Compare and choose the best VPS, dedicated servers, and hosting providers worldwide. Independent reviews, transparent ratings, and comprehensive comparisons.', author 'PQ.Hosting'
  - [2] 2026-10-22: the old plan page is withdrawn: HTTP 404 with the body 'Error code: 404 / # 404 - Page not found / Check the URL spelling or explore the global VPS/VDS & Dedicated hosting marketplace.' and links 'Back to homepage' and 'Browse providers'
  - [3] 2026-10-22: the homepage ranks other companies and hands traffic out: entry 1 is 'UFO.Hosting' with 'From $6.23 /month' and '[Visit](https://pq.hosting/go.php?id=2)', entry 2 is 'WeaselCloud' with 'From $3.00 /month' and '[Visit](https://pq.hosting/go.php?id=492)'
  - [4] 2026-10-22: the catalog carries 414 provider URLs over 6 languages, which is 69 distinct slugs, and the slug list includes 'the-hosting' itself; https://pq.hosting/providers/the-hosting is listed there but a fetch of it landed on https://pq.hosting/, so the catalog's own former-brand page no longer resolves
  - [5] 2026-10-22: no commerce path exists: the main sitemap lists /, /en, /de, /es, /it, /tr, /map, /companies, /choose-vps, /choose-dedicated, /contacts, /continents, /help, /dc and 8 /tools/ pages, and no /order, /cart, /login, /register, /billing or /account entry
- sources:
  - [1] https://pq.hosting/en
  - [2] https://pq.hosting/en/1-euro-vps
  - [3] https://pq.hosting/
  - [4] https://pq.hosting/sitemap-providers.xml
  - [5] https://pq.hosting/sitemap-main.xml
