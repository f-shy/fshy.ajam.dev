# Sanity

> sanity.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sanity/ | JSON https://fshy.ajam.dev/api/v1/entity/sanity.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sanity

- `storage/sanity` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:20.740Z (live) | stale on 2026-12-10
- url https://www.sanity.io
- free tier: 100 GB assets + 100 GB bandwidth/month per project; no maximum number of projects per account | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: Media Library maximum file size: up to 5 TB.
- retention: source: [1] | note: Existing assets will continue to be served.
- egress: 100 GB/month CDN bandwidth included per project, hard cap on Free (no overage purchase). Assets served from cdn.sanity.io with on-the-fly transforms. | metered: yes | free allowance: 100 GB per month
- identity: institution
- interface: rest, cli
- limits note: Free tier allows 2 datasets and 10,000 documents per project, with 20 user seats. Hard limits enforce 100 GB asset storage and 100 GB monthly bandwidth, blocking asset API access once quota is reached.
- interface detail: rest
- tooling: sanity CLI (`sanity dataset create`, `sanity assets upload`), @sanity/client HTTP API; assets land on cdn.sanity.io with stable public URLs
- composes with: Accounts have no published maximum limit on project count. Each project provides 2 datasets with 100 GB asset storage (200 GB total per project). Additional accounts can be created via standard third-party login providers.
- reliability: Free projects are hard-capped, not throttled: at 100 GB bandwidth the CDN returns errors until the calendar month resets. Asset URLs are public and permanent; no expiry observed.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Assets 100GB', 'Bandwidth (per month) 100GB', 'Additional assets — Not included' on Free
  - [2] 2026-10-21: 'no maximum limit on the number of projects'
  - [3] 2026-10-21: probe: GET -> 200 image/png 990776 bytes; same URL ?w=200&auto=format -> 200 29387 bytes (transforms are free, uncounted as assets)
  - [1] 2026-11-19: the Free tier still includes 100GB monthly bandwidth | capture: sha256:2315349d939bdbd84b3907bc62cdfd07c87df8934e38c44e3c4f28357c715bd5 | quote: | Bandwidth (per month) | 100GB | 100GB | Custom |
  - [1] 2026-11-19: the Free tier still includes 100GB of assets | capture: sha256:2315349d939bdbd84b3907bc62cdfd07c87df8934e38c44e3c4f28357c715bd5 | quote: | Assets | 100GB | 100GB | Custom |
  - [2] 2026-11-19: Sanity's answers page still states no maximum limit on projects per account | capture: sha256:5cb2d765dbdc0bd5900b904120b00389941e4c151b786c40eb93f04de162611b | quote: no maximum limit
  - [4] 2026-11-25: Media Library documents a maximum file size of 5 TB | capture: sha256:53da1da760ae36645656068c7c81030ff328df7e0cc1e294af4c1319218e4941 | quote: - Maximum file size: up to 5 TB
  - [5] 2026-11-25: assets already uploaded keep being served when the asset quota is reached | capture: sha256:92ccd49ed838224f2f60c6939275a0bcf6651d1053deae7d27ba610efca2cc55 | quote: Existing assets will continue to be served.
  - [4] 2026-11-25: the original uploaded file is downloadable from Media Library | capture: sha256:53da1da760ae36645656068c7c81030ff328df7e0cc1e294af4c1319218e4941 | quote: You can download the original file you uploaded and its static renditions from the library.
- sources:
  - [1] https://www.sanity.io/pricing
  - [2] https://www.sanity.io/answers/is-there-a-maximum-number-of-projects-i-have-p1599929930432100
  - [3] https://cdn.sanity.io/images/3do82whm/next/f21df064721ee7867372278bcbd0de4b512de556-1200x630.png
  - [4] https://www.sanity.io/docs/media-library/limits-and-usage
  - [5] https://www.sanity.io/docs/platform-management/plans-and-payments
