# MultiDebrid

> multidebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/multidebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/multidebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MultiDebrid

- `debrid/multidebrid` | qualifies-with-caveat | evidence documented | binding none | category premium link generator / multi-host (global, PT-BR and ES storefronts) | tier Premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://multidebrid.com/pt-br/premium
- free tier: No free allowance is published. The plan page contrasts a 'plano gratuito' (waiting and a quota) with Premium: 'Velocidade maxima Gere e baixe sem espera do plano gratuito' and 'Uso pessoal ilimitado Sem cota inicial quando o Premium esta ativo'. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: The free plan is named but never quantified on the page.
- per-object cap: not applicable: files stay on the third-party host, whose own per-file cap applies. No per-file cap is published. | source: [1]
- retention: not applicable: no storage. Link history is kept in the member panel; how long a generated link stays valid is not stated. | source: [1]
- egress: 'Uso pessoal ilimitado - Sem cota inicial quando o Premium esta ativo' (unlimited personal use, no initial quota once Premium is active). No per-GB price appears anywhere on the plan page. | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Account creation with email, confirmed in the payment flow ('You must confirm your account by email before subscribing' is AllDebrid's wording, not MultiDebrid's; MultiDebrid's page only offers 'criar uma conta' and a voucher field). The exact fields were not read because the plan grid never rendered.
- interface: rest
- limits:
  - volume-quota: 'Uso pessoal ilimitado' with no published byte cap, fair-use threshold or concurrent-link count [1]
  - request-rate: free tier has waiting and a 'starter quota'; numbers unpublished [2]
- limits note: The only quantitative promise is the word 'ilimitado'. The site runs a 50%-discount banner, a voucher system and five resellers, which is a business that needs volume; nothing on the page says what volume it will serve.
- binding note: Nothing in the vocabulary is documented as failing at 1 TiB/month. The plausible failure is an unpublished fair-use ceiling, which would make it volume-quota; that is a guess with no page behind it, so the record stays at none.
- interface detail: The plan page lists 'Acesso a API - Use o MultiDebrid nos seus proprios apps e ferramentas' as a Premium feature. The endpoint is not published on the page; a member must obtain it.
- tooling: The vendor's own API, plus the web panel and link history. Output is an HTTP direct link.
- composes with: 52-host coverage behind one API key is the shape a batch archiver needs: a script posts a list of host URLs and gets direct links back, instead of holding logins at each host.
- reliability: Prices are rendered client-side and no read returned them, so the service is recorded but not priced. A reseller-voucher model means the buyer's recourse on a bad voucher is the reseller, not MultiDebrid.
- notes: MultiDebrid is the clearest case among debrid providers of a global service wearing LatAm clothes: /pt-br/ and /es/ storefronts, Portuguese and Spanish blog posts, and a reseller list that is entirely English-language. A Brazilian or Argentine buyer pays in EUR or USD through a foreign processor; the localization is marketing, not a local payment rail. A 2026-era entrant with a Turkish-first interface (the /tr pages render plan names and reseller copy) and an affiliate-style reseller network shared with other small providers. Documented as a name to re-check with a logged-in session rather than as a priced option. Its 52-host count matches BestDebrid's exactly, which may mean a common supplier; that is unverified.
- evidence note: Host count, API access, reseller list and the unlimited claim were read from the vendor's own plan page in Portuguese and English today. The price is unverified: the plan grid is JavaScript-rendered and returned no numbers. Opening the checkout would move the price to documented.
- extras:
  - hosts_claimed: 52
  - resellers: 5
  - storefronts: pt-BR; es; en
  - price_status: unverified: plan grid client-rendered, no number returned by three reads
  - hosts: 52
  - plans: 6
  - languages: tr, en
- evidence:
  - [1] 2026-10-23: Premium features as listed: 'Velocidade maxima', 'Uso pessoal ilimitado', 'Acesso a API', 'Historico de links', plus a voucher field
  - [1] 2026-10-23: the five authorized resellers and their payment methods: filesharingkey, Plusinstant, Premiumkeystore.com, Takenkey, UTop.us; none is Brazilian or Spanish-language except UTop.us, which lists 'Ingles, Alemao, Espanhol'
  - [3] 2026-10-23: the host count in the vendor's own title, 'Gerador de Links Premium para 52 Hosts Compativeis', and the host list beginning Rapidgator, Nitroflare, Turbobit, DDownload
  - [4] 2026-10-23: a Spanish storefront exists with the same '52 filehosts' claim, so this is a global service localized into both Iberian languages, not a Latin American operator
  - [5] 2026-10-23: 'Supported hosts 52', 'Configured hosts 52', 'Premium plans 6', 'API access Available', 'Checks (24h) 65', 'Successful checks 80%', 'Last successful check 2026-10-23 01:38 UTC'
  - [2] 2026-10-23: 'Generate and download without free-tier waiting', 'No starter quota once Premium is active', 'API access', and the table of five authorised resellers
- sources:
  - [1] https://multidebrid.com/pt-br/premium
  - [2] https://multidebrid.com/premium
  - [3] https://multidebrid.com/pt-br/
  - [4] https://multidebrid.com/es/
  - [5] https://multidebrid.com/
