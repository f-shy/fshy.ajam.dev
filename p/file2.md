# file2.me

> file2.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/file2/ | JSON https://fshy.ajam.dev/api/v1/entity/file2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## file2.me

- `debrid/file2-me` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file transfer service (free tiers, beta paid plan) | tier guest
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://file2.me/pricing
- price KRW 9,900 per month for Pro (5GB files, 20GB vault) after the beta ends; volume not priced per TB | parsed USD 7.47/mo
- free tier: Guest (no account, free): single file 500MB, 5GB per share, 20 files per share, expiry up to 7 days. Free account: single file 2GB, 10GB per share, 50 files, expiry up to 30 days, 2GB vault. | unit: GB | metered on: uploaded-bytes | read on: 2026-11-03 | source: [1] | note: The page is in Korean; figures read from the comparison table.
- per-object cap: 단일 파일: 비회원 500MB, Free 2GB, Pro 5GB, Biz 5GB | bytes: 524288000 | source: [1] | note: bytes = 500 x 1024^2 for the guest tier; 2GB for a free account, 5GB for Pro.
- retention: Maximum expiry: guest 7 days, Free 30 days, Pro 3 months, Biz 1 year. | days: 7 | source: [1] | note: days is the guest tier; a free account reaches 30 days.
- egress: Shares are unlimited in count; no download byte cap is printed. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The guest tier is labelled 비회원 (non-member), one-off use, free; the Free tier is an account whose sign-up fields were not read.
- interface: unknown
- limits:
  - per-object-cap (binding): 500MB guest, 2GB free account, 5GB Pro [1]
  - volume-quota: 5GB per share guest, 10GB per share free account, 50GB per share Pro [1]
  - retention-clamped: 7 days guest, 30 days free account, 3 months Pro [1]
- binding note: 500MB per file for a guest is the first limit a large pull meets; the 2GB cap needs a free account.
- interface detail: Web upload; a CLI example is advertised by a third-party list and was not read.
- tooling: Browser only as read.
- composes with: A guest share is capped at 500MB per file; 2GB needs a free account.
- reliability: The Pro plan is a beta that is free until 2026-12-31; the page says it will cost KRW 9,900 a month after launch.
- evidence note: Pricing page read on 2026-11-03; Korean table cells read as printed.
- extras:
  - plans: Guest free; Free; Pro KRW 9,900/month after beta; Biz price not set
- evidence:
  - [1] 2026-11-03: per-file caps by tier: guest 500MB, Free 2GB, Pro 5GB, Biz 5GB | capture: sha256:a3b9ce8a2baa7127bd7d070f0e9358e6e74a5763530673fa4c2c3d46821abb80 | quote: | 만료 공유 - 단일 파일 | 500MB | 2GB | 5GB | 5GB |
  - [1] 2026-11-03: maximum expiry by tier: 7 days, 30 days, 3 months, 1 year | capture: sha256:a3b9ce8a2baa7127bd7d070f0e9358e6e74a5763530673fa4c2c3d46821abb80 | quote: | 만료 공유 - 최대 만료일 | 7일 | 30일 | 3개월 | 1년 |
  - [1] 2026-11-03: Pro is free until 2026-12-31 and KRW 9,900 a month after launch | capture: sha256:a3b9ce8a2baa7127bd7d070f0e9358e6e74a5763530673fa4c2c3d46821abb80 | quote: 2026년 12월 31일까지 무료정식 출시 후 월 ₩9,900
- sources:
  - [1] https://file2.me/pricing
