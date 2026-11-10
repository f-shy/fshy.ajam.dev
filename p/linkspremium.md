# Links Premium

> linkspremium.com.br | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linkspremium/ | JSON https://fshy.ajam.dev/api/v1/entity/linkspremium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Links Premium

- `debrid/links-premium` | qualifies-with-caveat | evidence documented | binding volume-quota | category premium link generator / multi-host (Brazil, BRL) | tier Mensal
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://linkspremium.com.br/
- price BRL 39.90 per 30 days flat (USD 7.92 at 5.0383); no TB metering published | parsed USD 7.91/mo
- free tier: GRATIS: Duracao 7 dias, Servidores +45, Gerar links: 300MB. 'Teste GRATIS!' | unit: MB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The 300 MB is the size of a generated link on the trial, not a monthly volume. No card is mentioned for the trial.
- per-object cap: not applicable: the file stays on the third-party host, so the host's own per-file cap applies. The trial caps a generated link at 300 MB. | source: [1] | note: No per-file cap is published for paid plans.
- retention: not applicable: no files are stored. A generated link is time-limited and must be regenerated after it expires; the lifetime is not published. | source: [1]
- egress: Paid plans list 'Gerar links: Ilimitado' (unlimited link generation) and no byte allowance, no per-GB price and no speed cap. The trial is the only plan with a published number (300 MB per link). | metered: no | free allowance: 300 MB per generated link on the 7-day trial | source: [1]
- identity: email | detail: Registration at /sistema/index.php/register creates the trial account. The page does not say whether a card is required to start the trial.
- interface: unknown
- limits:
  - volume-quota (binding): 'Gerar links: Ilimitado' is the only published figure; no monthly byte cap, fair-use threshold or concurrent-download count is stated [1]
- limits note: The upstream input cost is published by a Brazilian host: BRFiles sells generator traffic at 'R$ 180,00 por cada TB de trafego' (brfiles.com/geradores-de-links/). At that cost R$ 39.90 of monthly revenue buys 0.222 TB, so a plan sold as unlimited at this price has an undisclosed ceiling somewhere below 250 GB/month. This is arithmetic on a third party's price list, not a statement by Links Premium.
- binding note: At 1 TiB/month the operator must buy roughly R$ 180 of host traffic against R$ 39.90 of revenue, so the plan cannot be honoured at that volume; the first thing to fail is a volume ceiling the page does not name.
- interface detail: Browser panel at linkspremium.com.br/sistema; registration and generation are web-only. No API is named on the pricing or affiliate page.
- tooling: Browser plus the site's own panel. The output is a direct HTTP link, which JDownloader, aria2 or a browser can take.
- composes with: One plan covers +45 hosts including 1fichier and Mega, the two hosts the archive actually sits on, so it substitutes for two separate host subscriptions at the price of one.
- reliability: A single-operator Brazilian reseller storefront with recurring billing; a 365-day prepaid term depends on the operator staying up. The comparable Brazilian generator Libera Premium closed in 2026 (see liberapremium.json).
- notes: linkspremium.postador.com.br serves the identical page and prices, so the two hostnames are one service. The affiliate page is the site's front page, which is a small signal about how the business acquires users: commission is paid on renewals, and the affiliate does not need a plan.
- evidence note: Prices, durations, trial size and host count were read from the vendor's own pricing page. The binding constraint is inferred from another vendor's published traffic price, which is why it is argued in limits_note rather than asserted as a Links Premium cap.
- extras:
  - fx: BRL to USD at 5.0383, Banco Central do Brasil PTAX dollar sale rate for 2026-10-22; local price kept as stated
  - plans_brl.trial_7d: 0.00
  - plans_brl.mensal_30d: 39.90
  - plans_brl.trimestral_90d: 104.90
  - plans_brl.semestral_180d: 179.90
  - plans_brl.anual_365d: 239.90
  - usd_at_rate.mensal_30d: 7.92
  - usd_at_rate.trimestral_90d: 20.82
  - usd_at_rate.semestral_180d: 35.71
  - usd_at_rate.anual_365d: 47.62
  - host_count_claimed: +45
- evidence:
  - [1] 2026-10-23: the five plans and their prices: GRATIS 7 days 300MB, Mensal R$ 39,90, Trimestral R$ 104,90, Semestral R$ 179,90, Anual R$ 239,90, each with 'Servidores: +45'
  - [1] 2026-10-23: 'Gerar links: Ilimitado' on every paid plan, which is the only statement about volume the page makes
  - [2] 2026-10-23: 'R$ 180,00 por cada TB de trafego' and 'O trafego comprado nunca expira', the input cost used in limits_note
- sources:
  - [1] https://linkspremium.com.br/
  - [2] https://brfiles.com/geradores-de-links/
