# Filecast

> filecast.co.kr | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filecast/ | JSON https://fshy.ajam.dev/api/v1/entity/filecast.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filecast (파일캐스트)

- `debrid/filecast-co-kr` | fails-identity | evidence documented | binding none | category webhard content marketplace (Korean: subscription download of a domestic catalogue) | tier 30-day unlimited
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://filecast.co.kr/www/index.php/charge/flat/
- price KRW 9,900 per 30 days (recurring) or KRW 11,000 one month, plus 10% VAT by the conservative reading | parsed USD 7.47/mo
- free tier: No free download allowance on the charge page; the entry product is a 30-day pass: '30일 무제한 이용권 - 정기결제(자동결제) 50% 20,000원 9,900원 - 1개월 45% 20,000원 11,000원'. A second tier: 25,000원 list at 13,200원 recurring / 14,500원 one month; a third: 30,000원 list at 15,600원 / 17,000원. | unit: requests | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: The unit is a 30-day window of unlimited catalogue downloads, not bytes. Sign-up is marketed as ten seconds ('회원가입은 10초면 충분합니다').
- per-object cap: no per-file cap published; the pass covers '파일캐스트(제휴콘텐츠 제외)의 모든 콘텐츠' | source: [1]
- retention: not applicable: a catalogue, not client storage | source: [1]
- egress: Unlimited downloads inside the 30-day window of the domestic catalogue; the pass excludes partner content ('제휴콘텐츠 제외'). Fair-use clause: '일반적인 이용이 아닌 다른 용도로 사용할 경우 다운로드가 제한될 수 있습니다'. | metered: no | free allowance: none; 30-day pass only | source: [1]
- identity: country-phone | detail: The product is a Korean domestic 정액제: the charge flow is the vendor's own '캐스트 원페이' and the refund clause speaks to a mobile number ('환불로 인한 휴대폰 정보는 ...'), which places a Korean handset in the payment path. No card rail for foreign issuers is documented on the page. | country: South Korea
- interface: rest
- limits:
  - request-rate: unstated; unlimited within the 30-day pass subject to the fair-use clause [1]
  - write-gated: paid tier only exists as a domestic subscription; no per-file sale on this page [1]
- limits note: Two contradictory VAT statements sit on the same page: '결제시 부가세 10%가 포함됩니다' beside the price table and '모든 이용권 금액은 부가세 10% 별도 입니다' in the notes. The conservative reading (VAT extra) is the one recorded.
- binding note: There is no byte meter to hit; a monthly transfer of 1 TiB is limited by what the catalogue holds, not by a quota.
- interface detail: Web plus a Windows download client (the site advertises speed through its own client) and a mobile app. No API.
- tooling: The vendor's own PC client and mobile app; the catalogue is not exposed to rclone or JDownloader.
- composes with: Not a multi-hoster and not chainable into one: it retrieves only Filecast's own catalogue, so it solves Korean-content gaps rather than host gaps. For the stack it is a source of Korean media, never of arbitrary URLs.
- reliability: Subscriptions are Korean-time based ('월정액 상품의 사용기간은 대한민국 표준시간을 기준으로 합니다'), refunds only within 48 hours and only once, and downloads are throttled for non-ordinary use under the fair-use clause.
- notes: Korea's retrieval market is not debrid at all: it is webhard, a domestic catalogue sold by the month. That is why the Korean queries return no premium-link generator. Trigger condition: Filecast publishes an overseas payment path.
- evidence note: Charge page read with prices and clauses. The identity claim rests on the domestic payment flow plus the mobile-number clause; completing a signup from outside Korea would test it, and that test is the thing this record says will fail.
- extras:
  - positioning: webhard / P2P content marketplace
  - client: vendor PC client plus mobile app
  - vat_conflict: two statements on one page
- evidence:
  - [1] 2026-10-23: '30일 무제한 이용권 - 정기결제(자동결제) 50% 20,000원 9,900원', '1개월 45% 20,000원 11,000원', '25,000원 13,200원 / 14,500원', '30,000원 15,600원 / 17,000원', '하루 단돈 330원으로 즐기는 파일캐스트 정액제'
  - [1] 2026-10-23: terms: '결제시 부가세 10%가 포함됩니다' and '모든 이용권 금액은 부가세 10% 별도 입니다'; '월정액 상품의 사용기간은 대한민국 표준시간을 기준으로 합니다'; '결제 후 48시간 이내에 신청하셔야만 환불이 가능합니다'
- sources:
  - [1] https://filecast.co.kr/www/index.php/charge/flat/
