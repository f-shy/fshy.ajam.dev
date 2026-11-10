# Prismic

> prismic.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/prismic/ | JSON https://fshy.ajam.dev/api/v1/entity/prismic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Prismic

- `storage/prismic` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://prismic.io
- free tier: Unlimited assets + unlimited documents on Free; 100 GB CDN bandwidth/month (no overage) | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 100 GB/month built-in CDN bandwidth, hard cap on Free ('100 GB (no overages)'). Served via images.prismic.io with imgix-style transform params. | metered: yes | free allowance: 100 GB per month
- identity: email
- interface: rest, graphql, cli
- limits note: Per-asset size cap not published on the pricing page (needs verification in the repo settings); 100 GB/month bandwidth hard stop; Free has 1 repository per... verify. Documents unlimited.
- interface detail: rest
- tooling: Prismic REST API + GraphQL, `@prismicio/client`, slice-machine CLI; assets public at images.prismic.io/<repo>/<id>.<ext>?w=&auto=format,compress
- composes with: Unlimited assets per repository, bandwidth-capped. Repositories are the unit; creating additional repos is free and each carries its own 100 GB/mo meter. That is a genuine N x 100 GB bandwidth multiplier, with storage effectively unbounded in each.
- reliability: Hard bandwidth stop at 100 GB with no paid overage on Free; assets remain stored and resume serving next month.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Free ... 100 GB of built-in CDN bandwidth a month | Unlimited documents | Unlimited assets'; table 'CDN bandwidth/month | 100 GB (no overages)'
  - [2] 2026-10-21: probe: GET ,compress&w=400 -> 200, 18202 bytes (public, transformable, no auth)
- sources:
  - [1] https://prismic.io/pricing
  - [2] https://images.prismic.io/prismic-main/airYaqlQnVZVEOJV_woman-prompting-ai-landing-page-builder.png?auto=format
