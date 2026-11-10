# MiraclePlus Compute

> miracleplus.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/miracleplus/ | JSON https://fshy.ajam.dev/api/v1/entity/miracleplus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MiraclePlus Compute

- `compute/miracleplus-compute` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.miracleplus.com/compute/
- free tier: Live English page, verbatim: 'MiraclePlus Compute is open to universities, research institutes, enterprises, startups, and independent researchers globally. Your physical location or business registration does not affect eligibility. While our infrastructure is based in Haidian, Beijing, we fully support remote access for international teams, and have supported 60+ teams worldwide.' Quota line, verbatim: 'Up to 1 million RMB in compute Quota (equivalent to 8x H800 cards for 15 months).' Mechanism, verbatim: 'Credits will be allocated based on a comprehensive assessment of each project. Once accepted, credits are issued on a dedicated platform for immediate use.' Chinese counterpart, verbatim: 'Qiji compute is open to universities, research institutes, large enterprises, startups and independent individual researchers. Wherever you are, and whether or not the business is in China, you may apply if you meet the conditions. The compute is deployed in Haidian, Beijing, but international teams are supported for remote use.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an account on the application site, reachable by any one of three credentials: the sign-in page 'offers phone, email and WeChat as three separate routes', so a phone number, an email address or a WeChat account each reach the form. The page states 'Your physical location or business registration does not affect eligibility', so no Chinese entity or national ID is named. The real gate is the application review, not the credential. No card, hold, debit or prepaid term is stated.
- interface: rest
- limits:
  - write-gated (binding): Selection is a startup-accelerator screen at roughly a 2 percent acceptance rate, so the binding constraint is the panel and not the passport: no Chinese entity or national ID is named anywhere on the page, but an applicant must pass a founder-style review to receive anything at all. [1]
- limits note: Selection is a startup-accelerator screen at roughly a 2 percent acceptance rate, so the binding constraint is the panel and not the passport: no Chinese entity or national ID is named anywhere on the page, but an applicant must pass a founder-style review to receive anything at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing chains usefully here. One award of CNY 1,000,000 in platform credits replaces a stack of spot instances and notebook quotas outright. The break is that the credits spend only on the provider's own dedicated platform at the provider's own rate card, so the award converts to GPU-hours at their price and not at a market price.
- reliability: no reliability event recorded
- notes: SETTLED: the two batch-1 readings did not actually conflict. The Chinese page and the English page both name individual freelancers and independent researchers globally, and both deny that physical location or business registration affects eligibility. No Chinese entity, national ID or in-country presence is required by the page. The compute page's three buttons carry data-apply-url https://apply.miracleplus.com/?p=gpu, which redirects to sign-in and then to the Qiji accelerator application. The binding document is the district government's own scheme guideline, which lists six criteria for the individual. Open: the median award is unpublished; the page states only a maximum, and nothing establishes how far a typical award falls below it.
- extras:
  - facets.class: research-credit
  - facets.free_tier_kind: grant-credit
  - facets.shape.gpu_class: H800
  - facets.shape.gpu_count: 8
- evidence:
  - [1] 2026-10-22: live English page quotes the 1 million RMB quota, the independent-researcher eligibility sentence, the location and business-registration sentence, the credits-issued-on-a-dedicated-platform line, and the 60+ international teams figure. Probe: status 200, 10042 bytes, sha256 e54d12ff64d7.
  - [2] 2026-10-22: the Chinese page carries the same eligibility sentence verbatim and names the two backers: the Haidian District Elastic Compute Laboratory and a Xuhui District SME AI compute platform. Probe: status 200, 11144 bytes, sha256 d7b66a42a75c.
  - [2] 2026-10-22: the duration line reads 'within the year, the applicant schedules use freely', which does not state 15 months; the 15-month figure appears only inside the quota equivalence, so the term and the ceiling are two different statements on one page.
  - [3] 2026-10-22: the same content is served under /en/compute/, so the English wording is a maintained mirror and not a stale page.
  - [4] 2026-10-22: status 200, redirects to /users/sign_in with the p=gpu parameter preserved; the sign-in page offers phone, email and WeChat as three separate routes.
  - [2] 2026-10-22: the three compute buttons carry data-apply-url with p=gpu, and the page states the process is identical to the startup camp.
  - [5] 2026-10-22: the two-round screen quoted above, plus two direct answers: 'can independent founders apply? yes, we frequently accept independent founders' and 'do we need to incorporate before applying? no'.
  - [6] 2026-10-22: the form bundle carries founder equity and round-size fields, confirming the compute intake reuses the accelerator questionnaire. This URL is the site-wide Featured Content header link and not the compute apply link.
  - [2] 2026-10-22: quota line and eligibility paragraph, quoted in Chinese on the page and translated here: up to RMB 1,000,000 of compute, about 8 H800 for 15 months; open to universities, institutes, large enterprises, startups and independent individual researchers; anywhere in the world, whether or not the business is in China; deployed in Haidian, Beijing, reachable remotely by international teams; no KPI and no return requirement; no equity. Page 200, 2,964 words
  - [2] 2026-10-22: 
  - [7] 2026-10-22: the English-language version of the same page, Wayback capture 2026-06-11, quotes: 'Open to universities, research institutes, tech companies, startups, and independent developers'; 'Your physical location or business registration does not affect eligibility'; 'we fully support remote access for international teams, and have supported 60+ teams worldwide'; 'Up to 1 million RMB in compute Quota (equivalent to 8x H800 cards for 15 months)'; 'Purely academic or scientific projects with no plans for commercialization are fully eligible for support'
  - [1] 2026-10-22: probe status 200, 10042 bytes, sha256 e54d12ff64d7; the string 4132 Applications Received is present in the served HTML.
  - [7] 2026-06-11: the same capture carries 4132 Applications Received, unchanged four months earlier.
  - [2] 2026-10-22: the Chinese page carries the same 4132 in the same markup position, so both language versions share the frozen figure.
- sources:
  - [1] https://www.miracleplus.com/compute/
  - [2] https://www.miracleplus.com/cn/compute/
  - [3] https://www.miracleplus.com/en/compute/
  - [4] https://apply.miracleplus.com/?p=gpu&c=ib&r=PRteam&utm_source=ob
  - [5] https://www.miracleplus.com/cn/faq/
  - [6] https://apply.miracleplus.com/high_quality_content?p=ba&c=ib&r=PRteam&utm_source=ob
  - [7] https://web.archive.org/web/20260611105714/https://www.miraclepl.us/compute/?provider=wayback
