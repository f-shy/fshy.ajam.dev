# Fireload

> fireload.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fireload/ | JSON https://fshy.ajam.dev/api/v1/entity/fireload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fireload

- `debrid/fireload` | qualifies-with-caveat | evidence documented | binding per-object-cap | category cloud file storage (freemium, WebDAV and S3 on paid plans) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://www.fireload.com/upgrade
- price USD 10 per month for 1 TB (Pro, monthly billing) | parsed USD 10/TB-mo
- free tier: Free, $0/mo, no credit card required: 2 GB upload limit per file, 3-day trash history, active files space. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: No total storage figure is printed for the free plan; Pro lists 1 TB.
- per-object cap: 2 GB upload limit per file | bytes: 2147483648 | source: [1] | note: bytes = 2 x 1024^3; Pro and above list no upload limit.
- retention: unverified: the pricing page prints a 3-day trash history, not a retention period for files | source: [1]
- egress: Unlimited Bandwidth is listed in the plan comparison; no byte cap is printed. | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: The free plan states 'No credit card required' and has a 'Sign up for free' button; the sign-up form fields were not read.
- interface: rest, webdav, s3-compatible
- limits:
  - per-object-cap (binding): 2 GB per file on the free plan; no limit on Pro [1]
  - volume-quota: 1 TB on Pro, 2 TB on Pro +, 10 TB on Business + [1]
- binding note: 2 GB per file on the free plan is the one published free limit.
- interface detail: The plan comparison lists WebDAV Protocol, Restful HTTP API and S3 Compliant Storage; which plans include each was not separated in the text read.
- tooling: WebDAV, REST and S3-compatible access are listed on the comparison; the plan split was not read.
- composes with: Pro at $10 a month lists 1 TB with no upload limit and direct links, a plain paid storage path.
- reliability: Prices change with the Monthly or Annual toggle; the figures read are the monthly ones.
- notes: Plans: Pro $10/mo 1 TB; Pro + $15/mo 2 TB; Business + Unlimited $45/mo 10 TB.
- evidence note: Pricing page read on 2026-11-03. Retention and the sign-up form are unverified.
- extras:
  - plans: Free $0; Pro $10/mo; Pro + $15/mo; Business + Unlimited $45/mo
- evidence:
  - [1] 2026-11-03: the free plan caps a file at 2 GB | capture: sha256:d2b36e8b2d0c5bfb3928e37ac7d209f31cd750bb79893fa41b1b8b75935f1e0e | quote: 2 GB upload limit per file
  - [1] 2026-11-03: the Pro plan lists 1 TB of space | capture: sha256:d2b36e8b2d0c5bfb3928e37ac7d209f31cd750bb79893fa41b1b8b75935f1e0e | quote: 1 TB (1,000 GB) of space
  - [1] 2026-11-03: the free plan needs no card | capture: sha256:d2b36e8b2d0c5bfb3928e37ac7d209f31cd750bb79893fa41b1b8b75935f1e0e | quote: No credit card required
- sources:
  - [1] https://www.fireload.com/upgrade
