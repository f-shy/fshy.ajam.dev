# bytescale

> bytescale.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bytescale/ | JSON https://fshy.ajam.dev/api/v1/entity/bytescale.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bytescale

- `storage/bytescale` | fails-egress | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:25.571Z (live) | stale on 2026-12-04
- url https://www.bytescale.com/pricing
- free tier: None reachable: No free tier at all any more. Cheapest plan is $7/mo Basic with 10 GB storage and 10 GB download bandwidth; over-quota returns HTTP 400. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Download bandwidth is capped per month on every self-serve plan: 10GB on Basic ($7/month), 50GB on Plus ($35/month), 300GB on Advanced ($195/month). At 100% of the quota the API and CDN return HTTP 400. Higher limits are by upgrade or by contacting the vendor. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the verdict rests on the vendor pricing page and the vendor support article, both read on 2026-11-03: the 10GB, 50GB and 300GB monthly download quotas, the $7, $35 and $195 monthly prices and the HTTP 400 at 100% of quota are quoted from the pricing page, and the egress basis and the route to higher limits from the support article; storage per plan and the absence of a free plan are not quoted there
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: No free tier at all any more — cheapest plan is $7/mo Basic with 10 GB storage and 10 GB download bandwidth; over-quota returns HTTP 400
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No free tier at all any more — cheapest plan is $7/mo Basic with 10 GB storage and 10 GB download bandwidth; over-quota returns HTTP 400
  - [2] 2026-10-21: cited as the basis of the rejection: No free tier at all any more — cheapest plan is $7/mo Basic with 10 GB storage and 10 GB download bandwidth; over-quota returns HTTP 400
  - [1] 2026-11-03: the top self-serve plan (Advanced) includes 300GB of download traffic per month | capture: sha256:560bfad33ba2fe4822767bc582de6b0723151ad928c2b37b7fb952553000591c | quote: 300GB Download Bandwidth Total download traffic per month across all your files.
  - [1] 2026-11-03: Basic includes 10GB of download traffic per month | capture: sha256:560bfad33ba2fe4822767bc582de6b0723151ad928c2b37b7fb952553000591c | quote: 10GB Download Bandwidth Total download traffic per month across all your files.
  - [1] 2026-11-03: Plus includes 50GB of download traffic per month | capture: sha256:560bfad33ba2fe4822767bc582de6b0723151ad928c2b37b7fb952553000591c | quote: 50GB Download Bandwidth Total download traffic per month across all your files.
  - [1] 2026-11-03: Basic costs $7 per month | capture: sha256:560bfad33ba2fe4822767bc582de6b0723151ad928c2b37b7fb952553000591c | quote: Basic $7/month For individual developers building apps with light usage.
  - [1] 2026-11-03: Plus costs $35 per month | capture: sha256:560bfad33ba2fe4822767bc582de6b0723151ad928c2b37b7fb952553000591c | quote: Plus $35/month For teams building production apps with moderate usage.
  - [1] 2026-11-03: Advanced costs $195 per month | capture: sha256:560bfad33ba2fe4822767bc582de6b0723151ad928c2b37b7fb952553000591c | quote: Advanced $195/month For teams building production apps with high usage.
  - [1] 2026-11-03: at 100% of the quotas the API and CDN answer HTTP 400 | capture: sha256:560bfad33ba2fe4822767bc582de6b0723151ad928c2b37b7fb952553000591c | quote: If this happens, the Bytescale API and Bytescale CDN will return 400 HTTP status codes, accompanied by descriptive JSON error responses.
  - [2] 2026-11-03: the bandwidth limit counts all egress to the Internet | capture: sha256:29b3a108b6dacba56e1c5e29e8bcb2b1963f9e8fc4094e235644afa99d7afa79 | quote: Total monthly egress data transfer from Bytescale to the Internet.
  - [2] 2026-11-03: higher limits are by upgrade or by contacting the vendor | capture: sha256:29b3a108b6dacba56e1c5e29e8bcb2b1963f9e8fc4094e235644afa99d7afa79 | quote: If you require higher limits, please upgrade your plan or contact our team to discuss custom limits.
- sources:
  - [1] https://www.bytescale.com/pricing
  - [2] https://support.bytescale.com/article/10-what-happens-if-i-exceed-the-limits
