# Baixar Premium

> baixarpremium.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/baixarpremium/ | JSON https://fshy.ajam.dev/api/v1/entity/baixarpremium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Baixar Premium

- `debrid/baixarpremium` | qualifies-with-caveat | evidence documented | binding volume-quota | category Brazilian reseller of premium host accounts (combo bundles, BRL) | tier MegaCombo / SuperCombo / ComboSupremo
- needs card unknown, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://baixarpremium.net/comprar/
- price BRL 39.99 per 31 days for 23 hosts (USD 7.94 at 5.0383); BRL 58.99 for 31 hosts; BRL 99.99 for 35 hosts
- free tier: No free tier. The store sells paid account bundles only; the site separately advertises a link generator with a free trial at baixarpremium.net/gerador-de-links-premium/. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the seller publishes no object cap. Each bundled account carries the host's own per-file cap. | source: [1]
- retention: not applicable: accounts are sold for a fixed number of days; no storage is sold by the reseller. | source: [1]
- egress: No egress number is published by the reseller. The buyer gets premium access at each named host and is bound by that host's own transfer allowance. The bundles are priced per period, not per byte. | metered: no | source: [1]
- identity: email | detail: A store account is needed to order; delivery is by email or panel after payment. The payment methods offered were not read, so whether a card is mandatory is unverified.
- interface: unknown
- limits:
  - volume-quota (binding): not published by the reseller; the bundled host account's own allowance applies (for example BRFiles premium is 'Baixe ate 2 TB por mes') [1]
- limits note: The page sells host coverage by count (23, 31 or 35 hosts) and never by volume. The only volume figure in the bundle ecosystem is the host's: BRFiles states 2 TB/month on its own premium page.
- binding note: At 1 TiB/month the first thing to fail is the per-host transfer allowance of whichever host the files sit on, because the reseller adds no traffic of its own.
- interface detail: A WooCommerce-style storefront; delivery of the account or voucher is arranged after payment. No API and no endpoint are named on the page.
- tooling: The delivered credentials are used at each host's own site or its download manager integration. The reseller ships nothing executable.
- composes with: A single R$ 39.99 bundle covers 23 hosts including 1fichier, Mega, MediaFire and BRFiles for 31 days, which is the cheapest way to hold all four at once without a multi-host; but each account is separate, so a script still has to know which host a link belongs to.
- reliability: The buyer receives an account somebody else registered, so the original owner can change the password or the host can bind the session to one IP; the reseller's own warranty is the only recourse and its terms are not on this page.
- notes: The commercial model is a bundle of separately registered host accounts, resold. That is a different object from a multi-host: coverage is high but each host has its own login, its own quota and its own simultaneous-session rule. The seller has run since at least the date its generator page claims ('ha mais de 10 anos'), which is longer than most services among debrid providers.
- evidence note: Every price and host list here was read from the vendor's purchase page. Whether the bundled accounts are exclusive to the buyer or shared between buyers is not stated anywhere on the page, which is why the verdict keeps a caveat rather than a qualification.
- extras:
  - fx: BRL to USD at 5.0383, Banco Central do Brasil PTAX dollar sale rate for 2026-10-22; local prices kept as stated
  - bundles.MegaCombo.hosts: 23
  - bundles.MegaCombo.31d_brl: 39.99
  - bundles.SuperCombo.hosts: 31
  - bundles.SuperCombo.31d_brl: 58.99
  - bundles.ComboSupremo.hosts: 35
  - bundles.ComboSupremo.31d_brl: 99.99
  - usd_31d.MegaCombo: 7.94
  - usd_31d.SuperCombo: 11.71
  - usd_31d.ComboSupremo: 19.85
- evidence:
  - [1] 2026-10-23: MegaCombo prices: 9 days R$ 26.99, 31 days R$ 39.99, 61 days R$ 72.99, 95 days R$ 102.99, 185 days R$ 176.99, 365 days R$ 269.99
  - [1] 2026-10-23: the three bundle host lists, including MegaCombo's '1Fichier, 4Shared, Brfiles, ClicknUpload ... MediaFire, Mega ... Zippyshare' and SuperCombo's extension to 31 hosts
  - [1] 2026-10-23: SuperCombo 31 days R$ 58.99 and ComboSupremo 31 days R$ 99.99, the two larger tiers
  - [2] 2026-10-23: 'ha mais de 10 anos, compre com quem realmente tem um sistema de qualidade' and 'O servico sera fornecido com gerador ou conta, depende do servidor comprado' - the seller also runs its own generator, the same shape as the reseller network
  - [3] 2026-10-23: 'Baixe ate 2 TB por mes' on BRFiles premium, the host allowance that binds a MegaCombo containing BRFiles
- sources:
  - [1] https://baixarpremium.net/comprar/
  - [2] https://baixarpremium.net/gerador-de-links-premium/
  - [3] https://brfiles.com/planos/
