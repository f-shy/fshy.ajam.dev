# Prismic

> prismic.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/prismic/ | JSON https://fshy.ajam.dev/api/v1/entity/prismic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Prismic

- `storage/prismic` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:16.879Z (live) | stale on 2026-12-10
- url https://prismic.io
- free tier: Unlimited assets + unlimited documents on Free; 100 GB CDN bandwidth/month (no overage) | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: The maximum image size is 10MB; other file types, including videos, can be up to 100MB. | source: [1] | note: The media documentation states the 10MB image ceiling and 100MB ceiling for other files.
- retention: source: [1] | note: Deleting an asset removes it from the media library but leaves it accessible at its direct URL; pages using the asset continue.
- egress: 100 GB/month built-in CDN bandwidth, hard cap on Free ('100 GB (no overages)'). Served via images.prismic.io with imgix-style transform params. | metered: yes | free allowance: 100 GB per month
- identity: email
- interface: rest, graphql, cli
- limits note: Per-asset size cap not published on the pricing page (needs verification in the repo settings); 100 GB/month bandwidth hard stop; Free has 1 repository per... verify. Documents unlimited.
- interface detail: rest
- tooling: Prismic REST API + GraphQL, `@prismicio/client`, slice-machine CLI; assets public at images.prismic.io/<repo>/<id>.<ext>?w=&auto=format,compress
- composes with: The Free plan is $0/month per repository.
- reliability: Hard bandwidth stop at 100 GB with no paid overage on Free; assets remain stored and resume serving next month.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Free ... 100 GB of built-in CDN bandwidth a month | Unlimited documents | Unlimited assets'; table 'CDN bandwidth/month | 100 GB (no overages)'
  - [2] 2026-10-21: probe: GET ,compress&w=400 -> 200, 18202 bytes (public, transformable, no auth)
  - [1] 2026-11-11: the pricing page gives the Free CDN allowance in GB a month | capture: sha256:4fe7740a02630d6c1279de41cc9ac040df116db8a22a1ec80a73569bf731c172 | quote: 100 GB of built-in CDN bandwidth a month
  - [3] 2026-11-25: the media documentation states the 10MB image and 100MB other-file ceilings | capture: sha256:302e22b6181863d96ac2f962548cb6cd974a1ca049da8dd1c38adde5a1fb7132 | quote: The maximum image size is 10MB; other file types, including videos, can be up to 100MB.
  - [3] 2026-11-25: deleted assets remain reachable at their direct URL | capture: sha256:302e22b6181863d96ac2f962548cb6cd974a1ca049da8dd1c38adde5a1fb7132 | quote: Deleting an asset removes it from the media library but leaves it accessible at its direct URL. Pages that use the asset will continue using the asset.
  - [1] 2026-11-25: the Free plan lists 100 GB of built-in CDN bandwidth per month | capture: sha256:deecda043957e74c12e86f2b6d7552e9e9dd4c32a39429bcf37c0644a6d2d5f1 | quote: 100 GB of built-in CDN bandwidth a month
  - [1] 2026-11-25: the pricing page states the Free plan price is per repository | capture: sha256:deecda043957e74c12e86f2b6d7552e9e9dd4c32a39429bcf37c0644a6d2d5f1 | quote: $0/month Per repository
- sources:
  - [1] https://prismic.io/pricing
  - [2] https://images.prismic.io/prismic-main/airYaqlQnVZVEOJV_woman-prompting-ai-landing-page-builder.png?auto=format
  - [3] https://prismic.io/docs/media
