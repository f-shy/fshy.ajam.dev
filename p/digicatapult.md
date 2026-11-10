# Digital Catapult

> digicatapult.org.uk | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/digicatapult/ | JSON https://fshy.ajam.dev/api/v1/entity/digicatapult.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Digital Catapult

- `compute/digital-catapult` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.digicatapult.org.uk/programmes/programme/bridgeai/high-growth-ai-accelerator-faqs/
- free tier: A 14-week accelerator whose participants get compute from named technology partners: 'up to $25k for two years in AWS credits and one year of AWS business support (up to $10,000)'; 'up to $2,000 USD in Google Cloud credits, valid for two years (Start Tier) or $100,000 USD in Google Cloud credits for one year, with 20% off for the second year (Scale Tier)'; 'EUR 10k in OVHcloud credits for startups and EUR 100k in OVHcloud credits for scaleups'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: partner-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Applicants must be 'a UK based registered company, or prove they are a company that has an establishment in the UK', must 'undertake all activity in the UK', and must be 'eligible to receive GBP 18,000 in State Assistance', so the GBP 18,000 de minimis ceiling also caps how much state-supported credit can be taken in the same period. [1]
- limits note: Applicants must be 'a UK based registered company, or prove they are a company that has an establishment in the UK', must 'undertake all activity in the UK', and must be 'eligible to receive GBP 18,000 in State Assistance', so the GBP 18,000 de minimis ceiling also caps how much state-supported credit can be taken in the same period.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The interesting number is the Google Cloud Scale Tier at USD 100,000 for a year, which is four times the AWS offer in the same programme and is the largest single cloud credit found on any UK accelerator page on 2026-10-22; it composes with the free Google Cloud tier because the credit is applied to a billing account that already carries the always-free SKUs.
- reliability: no reliability event recorded
- notes: The credit figures are the accelerator's own statement of what its technology partners offer, not figures read from AWS, Google or OVH pages, so they are the accelerator's report of a third party's terms and are also qualified by 'Subject to availability and third-party terms'. The 14-week programme length against a one-year credit validity is the useful mismatch: the cohort ends long before the credits do. Who receives the Scale Tier is unresolved: either (a) the Scale Tier is automatic for all participants, plausible but not stated, or (b) it is a tier of Google's own startup programme that the accelerator merely refers to, which the FAQ wording 'Start Tier / Scale Tier' suggests because those are Google's tier names. Only the sibling Applied AI Growth Sprints document has been read.
- extras:
  - facets.class: accelerator-credit
  - facets.free_tier_kind: partner-credit
  - facets.shape.gpu_class: provider-dependent (AWS, Google Cloud, OVHcloud)
- evidence:
  - [1] 2026-10-22: 'up to $25k for two years in AWS credits and one year of AWS business support (up to $10,000)'; '$100,000 USD in Google Cloud credits for one year, with 20% off for the second year (Scale Tier)'; 'EUR 100k in OVHcloud credits for scaleups', quoted
  - [1] 2026-10-22: 'Applicants must be a UK based registered company, or prove they are a company that has an establishment in the UK, and undertake all activity in the UK', quoted
  - [1] 2026-10-22: 'Applicants must be able to receive £18,000 in State Assistance'; 'The High Growth AI Accelerator for Innovate UK BridgeAI is a 14-week accelerator delivered by Digital Catapult', quoted
  - [1] 2026-10-22: credits are 'Subject to availability and third-party terms', quoted
  - [2] 2026-10-22: 'Applicants must be eligible to receive £25,933 in State Assistance'; 'Applicants must be a UK-registered Startup organisation that has fewer than 250 employees and a turnover of less than EUR50 million', quoted from the Applied AI Growth Sprints terms
- sources:
  - [1] https://www.digicatapult.org.uk/programmes/programme/bridgeai/high-growth-ai-accelerator-faqs/
  - [2] https://www.digicatapult.org.uk/wp-content/uploads/2026/07/Applied-AI-Growth-Sprints-Terms-and-Conditions.pdf
