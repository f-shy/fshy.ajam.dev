# YesFile

> yesfile.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yesfile/ | JSON https://fshy.ajam.dev/api/v1/entity/yesfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YesFile (예스파일)

- `debrid/yesfile-com` | fails-identity | evidence documented | binding none | category webhard content marketplace (Korean: point top-up plus 30-day pass) | tier 30-day pass
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://www.yesfile.com/html/popup/charge/ecoupon.html
- price KRW 9,900 per 30-day pass (promotional; list KRW 25,000), VAT extra
- free tier: A new-member trial is advertised, not a free allowance: '이벤트 패키지 정액권 - 30일 정액제 + 9,900P + 쿠폰 20장 ... 25,000원 9,900원'. Third-party trackers describe '신규가입 시 3일 무료이용권 지급' and a '3개월 무제한 9900원' promotion. | unit: requests | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: Top-up is in points; the pass is sold as a 30-day window. The 3-day trial and the 3-month offer come from Korean comparison sites, not the vendor.
- per-object cap: no per-file cap published | source: [1]
- retention: not applicable: a catalogue, not client storage; bonus points expire in 30 days per the charge-page note | days: 30 | source: [2]
- egress: Catalogue downloads inside the pass window; points are consumed per file. No byte allowance is published. | metered: no | free allowance: 3-day trial (third-party stated) | source: [1]
- identity: country-phone | detail: Domestic-only rails: the charge page prices 상품권 (Korean gift certificates) alongside card and bank transfer, and Korean webhard practice ties signup and rewards to a Korean handset ('휴대폰 본인 인증 시 1,000P' per a Korean webhard ranking site). No foreign-issuer card path is published. | country: South Korea
- interface: rest
- limits:
  - volume-quota: points are consumed per download; pass covers 30 days of catalogue access [1]
  - write-gated: paid tiers are domestic 정액제 only [3]
- limits note: VAT is added on top of listed prices ('모든 결제 상품은 부가세 10% 별도 금액이며, 상품권 결제의 경우 부가세 10%가 차감 된 포인트가 적립 됩니다'), and gift-certificate payment credits fewer points than cash.
- binding note: No byte meter; the catalogue is the limit. At 1 TiB/month the constraint is that the files are Korean-market content, not capacity.
- interface detail: Web marketplace with its own player and download pages; a mobile site at m.yesfile.com. No API.
- tooling: Browser only in practice; the vendor's own player handles in-page playback. Nothing that a download manager can batch.
- composes with: Sits in the same slot as Filecast: Korean catalogue, Korean rails, no arbitrary URL support. It is not a substitute for a debrid and does not combine with one.
- reliability: Point balances expire, gift-certificate purchases credit less than cash, and the catalogue is Korean-market media whose availability the operator controls; there is no export path.
- notes: Second Korean webhard, included because its promo price (9,900원) matches Filecast's and because the gift-certificate rail is the clearest sign that the payment layer is domestic. Trigger condition: an overseas card rail appears.
- evidence note: The pass price and the VAT sentence were read from yesfile.com on 2026-10-23; the phone-verification detail is third-party and marked as such. Reading the live charge flow needs a Korean session, which debrid does not have.
- extras:
  - rails: gift certificate (상품권), card, bank transfer, points
  - trial: 3 days, third-party stated
- evidence:
  - [1] 2026-10-23: '이벤트 패키지 정액권 30일 정액제 + 9,900P + 쿠폰 20장 ... 25,000원 9,900원'; '30일동안 24시간! PC + 모바일 모두 이용 가능'
  - [4] 2026-10-23: payment note: '모든 결제 상품은 부가세 10% 별도 금액이며, 상품권 결제의 경우 부가세 10%가 차감 된 포인트가 적립 됩니다'
  - [5] 2026-10-23: third-party price list: '월자동 정액제 9,900원 - 30일 무제한 + 3000P 12,000원' and '신규가입 시 3일 무료이용권'
  - [6] 2026-10-23: third-party ranking site: '휴대폰 본인 인증 시 1,000P를 적립' - evidence that a Korean handset is in the signup path
- sources:
  - [1] https://www.yesfile.com/html/popup/charge/ecoupon.html
  - [2] https://www.yesfile.com/
  - [3] https://www.yesfile.com/charge/
  - [4] https://yesfile.com/html/content/charge/pandatv.html
  - [5] https://webhardrank.com/webhard/%EC%98%88%EC%8A%A4%ED%8C%8C%EC%9D%BC/
  - [6] https://dpgtestbed.kr/
