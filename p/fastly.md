# Fastly

> fastly.com | Compute, Storage, Egress and tunnels; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fastly/ | JSON https://fshy.ajam.dev/api/v1/entity/fastly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fastly Compute

- `compute/fastly-compute` | qualifies-with-caveat | evidence documented | binding request-rate | category cloud VM
- needs card yes, phone yes, ID no, institution no | verified 2026-11-04T06:40:20.287Z (live) | stale on 2026-12-05
- url https://www.fastly.com/pricing
- free tier: "10 Million Compute requests free" a month and "100 Million Compute vCPU milliseconds free" a month, with overage at USD 0.50 per million requests and USD 0.05 per million vCPU milliseconds. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The pricing page lists CDN bandwidth per region with the first 100 GB per month free and a per-GB price above it; whether bytes served by Compute meter under that table is unverified: the table is headed 'Bandwidth (per month)' and is not labelled for Compute | metered: no | source: [1]
- identity: card | detail: a card is required: the vendor's own announcement states the free developer accounts "require a valid credit card to help prevent abuse on the platform". The record does not state whether the card is charged or authorised for any amount, whether a hold is placed and for how long, whether a debit or prepaid card is accepted, or whether an email or phone is also required at signup
- interface: rest
- limits:
  - request-rate (binding): The free tier is metered in vCPU milliseconds, so 100 million vCPU-ms a month is about 27.8 vCPU-hours, and a Compute program cannot stay resident at all because the model is one request at a time. [1]
- limits note: The free tier is metered in vCPU milliseconds, so 100 million vCPU-ms a month is about 27.8 vCPU-hours, and a Compute program cannot stay resident at all because the model is one request at a time.
- binding note: the same as limits note
- interface detail: REST API at api.fastly.com and the fastly CLI, documented at fastly.com/documentation/reference
- tooling: the fastly CLI, which builds and deploys Compute packages through the Fastly API
- composes with: 10 million requests a month at the edge with no idle cost, useful as a front for an IPv6-only origin or as a webhook receiver that triggers a paid-for-nothing job elsewhere.
- reliability: no reliability event recorded
- notes: The card requirement converts this from an anonymous free tier into a payment relationship, which is why identity_cost is card. Compute is WebAssembly, so a process that needs a shell, a kernel or a long-lived socket does not fit. 27.8 vCPU-hours a month is the number to compare against Deno's 10 and Cloudflare's CPU-time model.
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: perpetual-allowance
- evidence:
  - [1] 2026-10-22: Compute section: 0 to 10 million Compute requests free, 0 to 100 million Compute vCPU milliseconds free, quoted
  - [2] 2026-10-22: "We provide a monthly free tier of services for many Network Services and Compute products", charged only above the limits, quoted
  - [3] 2026-10-22: vendor update on the same page: the free tier is more generous now but "require a valid credit card to help prevent abuse on the platform"
  - [4] 2026-11-03: a REST API covers the platform | capture: sha256:4366426bc622b4d175319d7e604411edb1c75465df43c353b2bc40266901ce34 | quote: The Fastly API is a RESTful API that provides access to all the features available through the Fastly web interface.
  - [1] 2026-11-03: the pricing page lists 100 GB per month of free CDN bandwidth in every region | capture: sha256:c441e9f9991b007daed6871f364939e7fadcaf1fe5c5351706e2c56dca433493 | quote: | 0 - 100 GB | Free | Free | Free | Free | Free | Free | Free | Free | Free | Free |
  - [4] 2026-11-04: REST API | capture: sha256:4366426bc622b4d175319d7e604411edb1c75465df43c353b2bc40266901ce34 | quote: The Fastly API is a RESTful API that provides access to all the features available through the Fastly web interface.
  - [5] 2026-11-04: fastly is the CLI | capture: sha256:1e614f049cf31c29ef61f93ae9fbf112afab08f37527a214a08101033168161a | quote: `fastly` is an [open-source](https://github.com/fastly/cli) command line tool for interacting with the [Fastly API](https://www.fastly.com/documentation/reference/api).
- sources:
  - [1] https://www.fastly.com/pricing
  - [2] https://www.fastly.com/documentation/guides/account-info/billing/account-types/
  - [3] https://www.fastly.com/blog/its-free-instant-and-yours-fastlys-free-developer-accounts-are-here
  - [4] https://www.fastly.com/documentation/reference/api/
  - [5] https://www.fastly.com/documentation/reference/cli/

## Fastly Fast Forward (OSS CDN)

- `storage/fastly-fast-forward` | qualifies-with-caveat | evidence reported | binding write-gated | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.fastly.com/fast-forward
- free tier: No byte quota - free CDN/edge services for eligible OSS projects and the nonprofits that support them. Scope set per applicant after review. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: This is the egress: Fastly absorbs bandwidth for accepted projects. Origin still has to exist and be paid for elsewhere. | metered: no
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): review [1]
  - write-gated (binding): application [1]
- limits note: Google Form application; acceptance discretionary and reviewed by a human. Must be open-licensed, community-centred, 'built on trust'. No published SLA. Not a storage product at all.
- interface detail: rest
- tooling: Fastly CDN/VCL, custom VCL or Compute@Edge; standard HTTP origin pull.
- composes with: Use as the free front door over any of the qualifying origins (Hugging Face, Internet Archive, a university bucket). Turns a metered origin into an unmetered public read path.
- reliability: Established programme (relaunched 2022) with real OSS members (PyPI historically). Risk is acceptance, not durability. Adds a third-party dependency in the read path.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'we extend free services to eligible open source projects and nonprofits that support them'; application is an embedded Google Form
  - [2] 2026-10-21: 'Fast Forward will offer free services to open source projects and the nonprofits that support them'
- sources:
  - [1] https://www.fastly.com/fast-forward
  - [2] https://www.fastly.com/press/press-releases/fastly-launches-fast-forward-initiative-to-support-open-source-and-internet

## Fastly

- `egress/fastly-free` | fails-quota | evidence documented | binding volume-quota | category CDN
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://www.fastly.com/pricing
- free tier: 100 GB bandwidth and 100,000 requests per month | unit: GB | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: billed by volume
- retention: not applicable | source: [1]
- egress: 100 GB/month per region, then USD 0.12 to 0.28/GB by region | metered: yes | free allowance: 100 GB/month per region | source: [1]
- identity: email | detail: a Fastly account
- interface: rest
- limits:
  - request-rate: 100,000 requests/month on the free band [1]
- limits note: the allowance is a byte volume over a period, which none of the six kinds names; the number is in egress.free_allowance and binding names per-ip-shaping as the nearest kind
- binding note: the monthly byte allowance in egress.free_allowance is what runs out, and no kind in the six-value vocabulary names a byte volume over a period counted per account. per-ip-shaping is the closest, because it is the only kind that bounds a volume, and its subject here is the account rather than the caller's address
- interface detail: a Fastly service domain
- tooling: fastly CLI
- composes with: composes with an origin and a domain, and the 100 GB is spent per region so a multi-region service spends it several ways.
- reliability: the free band is metered per region
- notes: 100 GB a month is about 3.3 GB a day.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the CDN serves the origin's bytes from its edge
- evidence:
  - [1] 2026-10-22: '100 GB free' and '100,000 free' requests, with the per-region band table
- sources:
  - [1] https://www.fastly.com/pricing

## Fastly free account + Fast Forward OSS programme

- `storage/fastly-free-account-fast-forward-oss-programme` | fails-quota | evidence reported | binding write-gated | category cdn
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.fastly.com/fast-forward
- price Free tier 100 GB/mo; $120/TB EU/NA, $190/TB Asia, $280/TB Africa/India/KR. Not competitive as paid egress.
- free tier: Free account: 100 GB bandwidth/month free across all regions, 1M CDN requests/month, 5 domains, 100K purge requests. Above 100 GB: $0.12/GB EU/NA, $0.19/GB Asia/Australia, $0.28/GB Africa/India/South Korea. Fast Forward (OSS/nonprofit programme) has no published byte quota. 'we extend free services to eligible open source projects and nonprofits that support them', scope agreed after human review of a Google Form application. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 100 GB/mo free, then metered per region. Fast Forward absorbs bandwidth for accepted projects but is the only path to meaningful volume. | metered: yes | free allowance: 100 GB per month
- identity: email | detail: email
- interface: rest
- limits:
  - write-gated (binding): review of a Google Form application [1]
- limits note: per-object-cap: none. The binding limit is the 100 GB/month counter (and 1M requests). Fast Forward: discretionary human acceptance, no published SLA, and the previous '$50/month of free traffic' credit model was retired for new accounts created after 2025-10-28.
- interface detail: rest
- tooling: VCL / Compute@Edge; standard HTTP origin pull. Free accounts are self-serve at fastly.com/signup.
- reliability: Bandwidth is metered per region with no pooling, so a geographically mixed audience burns the 100 GB fastest. Fast Forward is real (PyPI, Rust Foundation, PSF, Kubernetes, Mastodon, 100+ projects) and worth applying to if any dataset ships as a public OSS artefact.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: Free account: 100 GB bandwidth/month free across all regions, 1M CDN requests/month, 5 domains, 100K purge requests. Above 100 GB: $0.12/GB EU/NA, $0.19/GB Asia/Australia, $0.28/GB Africa/India/South Korea. Fast Forward (OSS/nonprofit programme) has no published byte quota — 'we extend free services to eligible open source projects and nonprofits that support them', scope agreed after human review of a Google Form application.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: Free tier 100 GB/mo; $120/TB EU/NA, $190/TB Asia, $280/TB Africa/India/KR. Not competitive as paid egress.
- evidence:
  - [1] 2026-10-21: 'Bandwidth | 100 GB free | Billed per GB per Region per month'; per-region table 0-100 GB Free, 100 GB-10 TB $0.28 Africa / $0.19 Asia / $0.12 Europe / $0.12 North America
  - [2] 2026-10-21: 'we extend free services to eligible open source projects and nonprofits that support them'; application is an embedded Google Form; criteria 'Open … Community-centered … Built on trust'
  - [3] 2026-10-21: 'monthly free tier of services for many Network Services and Compute products, subject to certain limitations'; OSS programme contact [address removed]
- sources:
  - [1] https://www.fastly.com/pricing
  - [2] https://www.fastly.com/fast-forward
  - [3] https://www.fastly.com/documentation/guides/account-info/billing/account-types
