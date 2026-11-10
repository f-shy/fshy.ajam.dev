# EasyDebrid

> easydebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/easydebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/easydebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EasyDebrid

- `debrid/easydebrid` | paid-only | evidence reported | binding none | category multi-host debrid | tier paid
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T11:28:55.820Z (live) | stale on 2026-11-18
- url https://easydebrid.com/
- price USD 4.50 per 30 days, no volume figure published | parsed USD 4.5/mo
- free tier: No free tier on the vendor site: 'EasyDebrid is a service optimized to be used with apps.' The landing page offers only 'Get Started' into the dashboard. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not stated on the vendor page read | source: [1]
- retention: not stated on the vendor page read; a debrid caches resolved files for the account rather than storing them | source: [1]
- egress: The vendor page publishes no byte allowance. Plans are sold through a reseller at '1 Month Plan (30 Days) $4.5' and '1 Year Plan (365 Days) $40', each described only as 'Fast - Distributed CDN PoPs across the world'. | metered: no | free allowance: none | source: [2]
- identity: email | detail: Account at easydebrid.com from an email address alone ('If the email exists, you will be logged in. Otherwise, a new account will be created.'), with email verification and no password; paid plans are bought through the reseller paradise-cloud.com, whose payment methods were not read.
- interface: rest
- limits:
  - pull-count: unstated; plans are sold by period only [2]
- limits note: No fair-use figure, no concurrent-stream cap and no per-day byte count appears on either the vendor page or the reseller page. The absence is the finding: a debrid with no published limit is bounded by whatever the operator enforces silently.
- binding note: Nothing in the vocabulary is stated, so nothing can be named as binding from the evidence. The practical bound is the same as any debrid's: cached availability and silent fair-use enforcement, neither of which is published.
- interface detail: REST API at https://easydebrid.com/api/v1 with 'Authorization: Bearer YOUR_API_KEY' (key from the dashboard, or OAuth 2.0 with PKCE where the access token is the key); documented endpoints: user/details, link/lookup, link/generate. Plus a torrent downloader at downloader.hostyour.app.
- tooling: Named as a TorBox/RD alternative in Stremio and debrid-manager comparisons; three independent third-party guides describe it as multi-IP, which is the rare property among debrids. No client code was read here.
- composes with: At $4.50 a month it is the cheapest paid debrid found in tested services, and the annual at $40 is $3.33 a month. If multi-IP holds, it is the one debrid a user can use from two machines at once without a ban.
- reliability: Third-party reviewers report weak customer support and thin link sources, and one review says the operator is Singapore-based, which is why it survived the EU enforcement that cut the French debrids' caches.
- notes: Debrid provider appearing in Stremio addon listings. The vendor website publishes minimal information regarding quotas and supported hosts.
- evidence note: The price comes from the reseller page the vendor's own flow points at; the vendor page itself carries no price. The multi-IP claim is third-party and unverified. Opening the account page or the API docs would raise this.
- extras:
  - plans: 30 days $4.5; 365 days $40
  - annual_effective_monthly: USD 3.33
  - reseller: paradise-cloud.com
  - torrent_downloader: https://downloader.hostyour.app/
  - multi_ip_claim: reported by three third-party guides, unverified
- evidence:
  - [1] 2026-10-23: the vendor describes itself only as 'optimized to be used with apps', claims 'a huge cache of sources', and publishes no price or allowance
  - [2] 2026-10-23: the two plans: '1 Month Plan (30 Days) $4.5' and '1 Year Plan (365 Days) $40', plus 'Distributed CDN PoPs across the world'
  - [3] 2026-11-03: the vendor publishes a REST API with Bearer authentication | capture: sha256:a767f5ce5320fd2076af24228eee8a64d403f9f5109e89e1a18dec3cba8ff116 | quote: The EasyDebrid API allows you to integrate our debrid service into your applications.
  - [3] 2026-11-03: the API base URL | capture: sha256:a767f5ce5320fd2076af24228eee8a64d403f9f5109e89e1a18dec3cba8ff116 | quote: https://easydebrid.com/api/v1
  - [4] 2026-11-03: sign-in and sign-up are one email-only form | capture: sha256:62d96bd1f21e3b1b13bcbf3185ed5c250e357e27d661863bc13b83ca3c5a60d5 | quote: If the email exists, you will be logged in. Otherwise, a new account will be created.
  - [3] 2026-11-03: OAuth flow requires email verification | capture: sha256:a767f5ce5320fd2076af24228eee8a64d403f9f5109e89e1a18dec3cba8ff116 | quote: User completes email verification
  - [2] 2026-11-03: 30-day plan at $4.5 unchanged | capture: sha256:0e2a86738fdaea8278002f7fc4f0749eb84bb0bb1552064d8dc22174b4ca73bd | quote: ## 1 Month Plan (30 Days) $4.5
  - [1] 2026-11-03: vendor landing page unchanged | capture: sha256:846c713e8081fda052dc68ba77bec23e531b2ce138cff2bd29ea59be51c4edcc | quote: EasyDebrid is a service optimized to be used with apps.
  - [2] 2026-11-03: annual plan still listed | capture: sha256:0e2a86738fdaea8278002f7fc4f0749eb84bb0bb1552064d8dc22174b4ca73bd | quote: Save 25% by getting the annual plan
- sources:
  - [1] https://easydebrid.com/
  - [2] https://paradise-cloud.com/products/easydebrid
  - [3] https://easydebrid.com/api
  - [4] https://easydebrid.com/dashboard
