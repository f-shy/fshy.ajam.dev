# SpaceByte Cloud

> spacebyte.in | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/spacebyte/ | JSON https://fshy.ajam.dev/api/v1/entity/spacebyte.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SpaceByte Cloud (India) — ₹150/TB/mo claimed

- `storage/spacebyte-cloud-150-tb-mo-claimed-the-lowest-credible-lo` | fails-quota | evidence inferred | binding none | category consumer-cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (live) | stale on 2026-11-21
- url https://spacebyte.in/cloud-storage-pricing
- price $1.58/TB/mo at 1 TB ($18.95/TB/yr) as advertised, $1.19/TB/mo on the ₹1,650/yr annual. At 5 TB and 20 TB: NO PUBLISHED PLAN — the ladder stops at 1 TB and «Enterprise pooled storage» is quote-only, so the 5 TB and 20 TB figures do not exist and the number cannot be used for the sizing. | parsed USD 1.19/TB-mo
- free tier: Starter 50 GB ₹20/mo; Freelancer 100 GB ₹35/mo; 500 GB ₹100/mo; Studio Pro 1 TB ₹150/mo (or ₹1,650/yr); 25 GB free forever. Enterprise pooled storage on request. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Claimed free. The business page is titled «Eliminate Egress Fees» and argues against providers «that charge hidden egress fees», and the pricing JSON-LD implies flat-rate. But no numbered egress allowance, no fair-use clause and no overage rate is published anywhere on the site. So the claim cannot be falsified from outside. | metered: yes
- identity: email | detail: email
- interface: s3, rest, webdav, rclone, cli
- limits note: Zero programmatic API access. Client-side zero-knowledge encryption ensures that stored data is encrypted prior to transmission. Marketing comparison pages advertise promotional pricing while direct pricing endpoints returned incomplete placeholder pages on 2026-10-21.
- interface detail: rest
- tooling: None documented. No public API, no WebDAV, no S3 endpoint, no rclone backend, no CLI. The product page describes «Zero-Knowledge Personal Vault», AES-256-GCM client-side encryption, mobile sync and a web UI. This is the disqualifying gap.
- composes with: Per-account consumer plans; no documented route that uses several accounts and no API to automate one.
- reliability: unverified: https://spacebyte.in/cloud-storage-pricing, / and /pricing answered HTTP 503 with a maintenance notice on 2026-11-03; routes tried: four reader pins, a direct fetch, the archive (none for the pricing page) and a probe.
- notes: the same as the free tier
- evidence note: no plan page could be read on 2026-11-03: https://spacebyte.in/cloud-storage-pricing, the site root and /pricing answered HTTP 503 with a maintenance notice (probe:spacebyte.in); the plan prices date from 2026-10-21 and no page states them now
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Starter 50 GB ₹20/mo; Freelancer 100 GB ₹35/mo; 500 GB ₹100/mo; Studio Pro 1 TB ₹150/mo (or ₹1,650/yr); 25 GB free forever. Enterprise pooled storage on request.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $1.58/TB/mo at 1 TB ($18.95/TB/yr) as advertised, $1.19/TB/mo on the ₹1,650/yr annual. At 5 TB and 20 TB: NO PUBLISHED PLAN — the ladder stops at 1 TB and «Enterprise pooled storage» is quote-only, so the 5 TB and 20 TB figures do not exist and the number cannot be used for the sizing.
- evidence:
  - [1] 2026-10-21: «1TB of high-speed cloud storage on SpaceByte costs just ₹150/month with zero foreign exchange credit card markups»; «25 GB Permanent Free Storage»; «Pay in Indian Rupees using PhonePe, Google Pay, Paytm, BHIM UPI, and RuPay from ₹20/month»
  - [2] 2026-10-21: «SpaceByte’s transparent, tiered approach … Starter: 50GB for ₹20/month. Freelancer: 100GB for ₹35/month. Studio Pro: 1TB for ₹150/month»; page title «Eliminate Egress Fees, Ensure Compliance, and Scale Infinitely»
  - [3] 2026-10-21: 
  - [4] 2026-10-21: probe: curl -> HTTP 403 in 0.44 s; no S3/WebDAV/REST endpoint exists to probe
  - probe:spacebyte.in 2026-11-03: the pricing page URL answered HTTP 503 on 2026-11-03; the captured body of the site root, /pricing and the guide page is a maintenance notice | capture: sha256:60ffa1b8bc7be3dcbf5d4921d327521439a45bf7b92c790226e307cc9310b733 | quote: "status": 503
  - probe:spacebyte.in 2026-11-03: the pricing page answered HTTP 503 | capture: sha256:60ffa1b8bc7be3dcbf5d4921d327521439a45bf7b92c790226e307cc9310b733 | quote: "status": 503
- sources:
  - [1] https://spacebyte.in/cloud-storage-pricing
  - [2] https://spacebyte.in/pages/spacebyte-business-cloud-storage-2026-guide
  - [3] https://spacebyte.in/pricing
  - [4] https://spacebyte.in/
