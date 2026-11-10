# Hexupload

> hexload.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hexload/ | JSON https://fshy.ajam.dev/api/v1/entity/hexload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hexupload

- `debrid/hexupload` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (freemium, XFileSharing script) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:05:34.563Z (live) | stale on 2026-12-04
- url https://hexload.com/faq.html
- price USD 0.80 per TB-month on the 12-month Premium plan (10 TB storage); USD 15.99 per month on the 30-day plan. | parsed USD 0.8/TB-mo
- free tier: Core service free; Member storage is unlimited hot storage, files deleted 30 days after no activity; 2048 Mb per file; 35 GB per day of traffic. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: Guest traffic is 15 GB per day; Guest uploads are listed as 100 GB a day.
- per-object cap: 2048 Mb per file for Guest and Member; 20480 Mb for Premium only | bytes: 2147483648 | source: [1] | note: The plans table prints the unit as Mb and splits the cap by plan; Premium is 20480 Mb.
- retention: Forever. For premium users. Files are stored indefinitely. For free users, active files will be stored for 30 days, meaning there must be at least one download every 30 days. | days: 30 | source: [1]
- egress: Download and stream traffic is capped per day: 15 GB for Guest, 35 GB per day for Member (registered free), 100 GB per day for Premium. | metered: yes | free allowance: 35 GB per day (registered free); 15 GB per day (non-registered) | source: [1]
- identity: email | detail: The register page asks for username, email, password, a repeated password and an hCaptcha; no phone or card field is on the form. Whether a Guest can upload without registering is unverified: the upload form was not exercised.
- interface: ftp, rest
- limits:
  - per-object-cap: 2048 Mb per file (Guest and Member); 20480 Mb per file for Premium [1]
  - retention-clamped (binding): free files deleted without a download in 30 days [1]
  - volume-quota: 35 GB per day for Member, 15 GB per day for Guest [1]
- binding note: The 30-day inactivity deletion is the only number printed for the free tier.
- interface detail: Upload via browser, FTP, remote URL, API and a Zoom uploader, as listed on the FAQ.
- tooling: FTP, remote URL and API upload per the FAQ; the API page was not read.
- composes with: 20 GB per file and FTP/API upload make it scriptable, but free files need a download every 30 days to stay.
- reliability: Premium plans (10 TB, 100 GB per day) are listed at USD 15.99 per month, USD 8 per month on the 12-month term.
- evidence note: FAQ, plans comparison, register and premium pages read on 2026-11-03. Whether Guest upload needs no account is unverified.
- evidence:
  - [1] 2026-11-03: free retention is 30 days of inactivity | capture: sha256:5190553b9fa2e70e8c234be316c313947e19d3ac7e5b32b49bfe675fce89de3b | quote: Forever. For premium users. Files are stored indefinitely. For free users, active files will be stored for 30 days, meaning there must be at least one download every 30 days.
  - [1] 2026-11-03: the per-file cap is 20 GB | capture: sha256:5190553b9fa2e70e8c234be316c313947e19d3ac7e5b32b49bfe675fce89de3b | quote: - Upload upto 20 GB per file
  - [2] 2026-11-03: download traffic per day by plan: Guest 15 GB, Member 35 GB, Premium 100 GB | capture: sha256:c2f5f65b485195a73aeecb5ee2d322af485f4598594475f7d2f57c8fe90a10f5 | quote: | Traffic | 15 GB per day | 35 GB per day | 100 GB per day |
  - [2] 2026-11-03: the 20 GB per-file cap is Premium only; Guest and Member are 2048 Mb | capture: sha256:c2f5f65b485195a73aeecb5ee2d322af485f4598594475f7d2f57c8fe90a10f5 | quote: | Max upload file size | 2048 Mb | 2048 Mb | 20480 Mb |
  - [2] 2026-11-03: Member storage is unlimited hot storage, Guest upload 100 GB a day, Premium 10 TB | capture: sha256:c2f5f65b485195a73aeecb5ee2d322af485f4598594475f7d2f57c8fe90a10f5 | quote: | Storage space | Upload 100 GB a day | Unlimited hot storage | 10 TB |
  - [3] 2026-11-03: the sign-up form asks for username, email, password and a captcha | capture: sha256:3cfc1b4085a6bf462a190f2622e5cd6f80175d13498113b705a8136e3bec437d | quote: [Username]() [Email]() [Password]() [Retype Password]()
  - [4] 2026-11-03: the 12-month premium plan costs $96 | capture: sha256:3bec5c12c94be14e8ae654d5f75439e895e5521d1d3608cebbfa54360db5684e | quote: Billed $96 every 12 months
  - [2] 2026-11-03: Guest and Member files are deleted 30 days after no activity | capture: sha256:c2f5f65b485195a73aeecb5ee2d322af485f4598594475f7d2f57c8fe90a10f5 | quote: | When are your files deleted? | 30 days after no activity | 30 days after no activity | Never |
- sources:
  - [1] https://hexload.com/faq.html
  - [2] https://hexload.com/Plans_Comparison.html
  - [3] https://hexload.com/register.html
  - [4] https://hexload.com/premium.html
