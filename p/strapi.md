# Strapi Cloud

> strapi.io | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/strapi/ | JSON https://fshy.ajam.dev/api/v1/entity/strapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Strapi Cloud (Storage)

- `storage/strapi-cloud` | trial-only | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:22.268Z (live) | stale on 2026-12-10
- url https://strapi.io
- free tier: 50 GB asset storage + 50 GB asset bandwidth on Starter. But Starter is $35/month, NOT free. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: Non-image uploads are capped at 200 MB on all Strapi Cloud plans. The cap is enforced at the infrastructure level and cannot be overridden via the `strapi::body` middleware configuration.
- retention: source: [1] | note: | Backup retention (in month) | - | 1 month | 1 month |
- egress: $35 ... 50 GB asset storage ... 50 GB asset bandwidth | metered: yes | free allowance: 50 GB per month
- identity: institution
- interface: s3-compatible, rest, graphql, cli
- limits note: Paid-only. 50 GB storage / 50 GB bandwidth at $35/mo; unlimited DB entries.
- interface detail: Strapi turns your model into REST and GraphQL APIs instantly, fully typed.
- tooling: Strapi REST + GraphQL, upload plugin → any S3-compatible provider, `strapi` CLI; self-host is MIT-licensed
- composes with: No free tier on Cloud at all. The cheapest plan is $35/project/month. The free path is self-hosting Strapi on free compute (Oracle/AWS free tier) pointed at another storage backend, which is orchestration, not a free storage tier.
- reliability: N/A. Commercial hosting, stable.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 50 GB asset storage + 50 GB asset bandwidth on Starter — but Starter is $35/month, NOT free
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Starter $35 per project / month ... 100k API requests | 50 GB asset storage | 50 GB asset bandwidth' (no $0 tier listed)
  - [1] 2026-11-19: Starter is USD 35 per project per month with 50 GB asset storage and 50 GB asset bandwidth; no free Cloud tier is listed | capture: sha256:5f6ae8e323e70f2a348305abd9ef4a69e0e34144595bfc3f444482dc2818fb20 | quote: $35 per project / month [Sign up](https://cloud.strapi.io/?plan=essential) 100k API requests 50 GB asset storage 50 GB asset bandwidth
  - [2] 2026-11-25: the Strapi Cloud docs state the 200 MB non-image upload cap and its infrastructure enforcement | capture: sha256:9aec303d51eed2d2af706ddc973c9f62bc20169a89e76b9ee247d4e17140deac | quote: Non-image uploads are capped at 200 MB on all Strapi Cloud plans. The cap is enforced at the infrastructure level and cannot be overridden via the `strapi::body` middleware configuration.
  - [1] 2026-11-25: the pricing comparison gives backup retention as none on Starter and one month on Pro and Business | capture: sha256:5f6ae8e323e70f2a348305abd9ef4a69e0e34144595bfc3f444482dc2818fb20 | quote: | Backup retention (in month) | - | 1 month | 1 month |
  - [3] 2026-11-25: the homepage states REST and GraphQL API generation | capture: sha256:41bd65dbc30ec859bcf4be83dd41e93b4618d2f4a9275669fcd032b9cf9043f7 | quote: Strapi turns your model into REST and GraphQL APIs instantly, fully typed.
  - [1] 2026-11-25: the Starter card pairs the $35 monthly price with 50 GB asset storage and 50 GB asset bandwidth | capture: sha256:5f6ae8e323e70f2a348305abd9ef4a69e0e34144595bfc3f444482dc2818fb20 | quote: $35 ... 50 GB asset storage ... 50 GB asset bandwidth
  - [2] 2026-11-25: the docs state the 200 MB non-image cap | capture: sha256:9aec303d51eed2d2af706ddc973c9f62bc20169a89e76b9ee247d4e17140deac | quote: Non-image uploads are capped at 200 MB on all Strapi Cloud plans. The cap is enforced at the infrastructure level and cannot be overridden via the `strapi::body` middleware configuration.
  - [1] 2026-11-25: the pricing table states backup retention by plan | capture: sha256:5f6ae8e323e70f2a348305abd9ef4a69e0e34144595bfc3f444482dc2818fb20 | quote: | Backup retention (in month) | - | 1 month | 1 month |
  - [3] 2026-11-25: the homepage states REST and GraphQL APIs | capture: sha256:41bd65dbc30ec859bcf4be83dd41e93b4618d2f4a9275669fcd032b9cf9043f7 | quote: Strapi turns your model into REST and GraphQL APIs instantly, fully typed.
  - [1] 2026-11-25: the Starter card states the 50 GB monthly asset bandwidth | capture: sha256:5f6ae8e323e70f2a348305abd9ef4a69e0e34144595bfc3f444482dc2818fb20 | quote: $35 ... 50 GB asset storage ... 50 GB asset bandwidth
  - [4] 2026-11-25: the billing docs state that asset bandwidth overages are charged | capture: sha256:f59cccfa7037ae990adfecd26bf54ab916cbd84abd2c69ddf288e8d4291374c7 | quote: If you exceed the limits of your plan for API Requests, Asset Bandwidth, or Asset Storage, you will be charged for the corresponding overages.
- sources:
  - [1] https://strapi.io/pricing-cloud
  - [2] https://docs.strapi.io/cloud/advanced/upload-size-limits
  - [3] https://strapi.io
  - [4] https://docs.strapi.io/cloud/getting-started/usage-billing

## Strapi Cloud (Compute)

- `compute/strapi-cloud` | dead | evidence documented | binding retention-clamped | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-03T01:29:51.742Z (live) | stale on 2026-12-04
- url https://strapi.io/blog/we-re-removing-the-free-plan-from-strapi-cloud
- free tier: removed plan: the Free plan included 10 GB storage and 10 GB bandwidth per month (launch post), with no credit card; the plan is no longer available as of July 1st and existing free projects were deleted on September 1, 2026 | unit: none | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: Both dates are in the past at this read, so a free project either moved to a paid plan or was deleted on 2026-09-01, and no free lane remains. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - retention-clamped (binding): Both dates are in the past at this read, so a free project either moved to a paid plan or was deleted on 2026-09-01, and no free lane remains. [1]
- limits note: Both dates are in the past at this read, so a free project either moved to a paid plan or was deleted on 2026-09-01, and no free lane remains.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing chains, and the deletion date means any state placed here before September 2026 is gone.
- reliability: no reliability event recorded
- notes: storage/strapi-cloud also records Strapi Cloud as trial-only; Starter is a paid plan and not free. Before the removal, the Free plan included 10 GB storage and 10 GB bandwidth per month; the larger asset storage figure on the pricing page belongs to the paid Starter plan.
- extras:
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: quoted: 'As of July 1st, the Free plan is no longer be available'; free projects must upgrade or be deleted by 2026-09-01
  - [2] 2026-10-22: re-read 2026-10-22: the page no longer carries the claim it was cited for. This is the check that confirms the shutdown recorded here, not the notice itself
  - [1] 2026-10-30: the Strapi Cloud Free plan was removed as of 2026-07-01; the post names no amount for it | capture: sha256:bcc4b879a73fac884cf0a232fc81cb67e94c0130051d4b1edf784c32fbd7216b | quote: As of July 1st, the Free plan is no longer be available.
  - [1] 2026-10-30: the only terms the post gives for the removed Free plan are no card and no time limit, with no quota | capture: sha256:bcc4b879a73fac884cf0a232fc81cb67e94c0130051d4b1edf784c32fbd7216b | quote: No credit card, no time limit.
  - [2] 2026-10-30: the cloud pricing page lists Starter at USD 35 per project a month as its entry plan and lists no free plan | capture: sha256:d18b3dd20fb2df38f3eaac2e9051fc40e10c4ab7a799e111fa10e8be98f3c230 | quote: Starter $35 per project / month
  - [3] 2026-11-03: the removed Free plan included 10 GB storage and 10 GB bandwidth a month, not 50 GB | capture: sha256:ea9b6acc3116fd12fcfe38539f98e7423152af5d9cdf4ff6d43592d1ea20b1bb | quote: 10 GB storage and 10 GB bandwidth per month
  - [3] 2026-11-03: the Free plan needed no credit card | capture: sha256:ea9b6acc3116fd12fcfe38539f98e7423152af5d9cdf4ff6d43592d1ea20b1bb | quote: no credit card required
  - [4] 2026-11-03: a second first-party announcement gives the same 10 GB storage and 10 GB bandwidth for the Free plan | capture: sha256:94579066f1d1749aba2f1678c6b85d8b9c4dbecc6e38ec5290786ba83c282e08 | quote: 10 GB storage and 10 GB bandwidth
  - [2] 2026-11-03: the 50 GB figure belongs to the paid Starter plan's asset storage, not the removed Free plan | capture: sha256:5f6ae8e323e70f2a348305abd9ef4a69e0e34144595bfc3f444482dc2818fb20 | quote: | Asset storage (in GB) - per environmentAdditional asset storage: +$0.60 per GB | 50 | 250 | 1,000 |
- sources:
  - [1] https://strapi.io/blog/we-re-removing-the-free-plan-from-strapi-cloud
  - [2] https://strapi.io/pricing-cloud
  - [3] https://strapi.io/blog/introducing-the-free-plan-for-strapi-cloud
  - [4] https://dev.to/strapi/strapiconf-2025-announcements-3j03
