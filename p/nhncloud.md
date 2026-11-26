# NHN Cloud

> nhncloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nhncloud/ | JSON https://fshy.ajam.dev/api/v1/entity/nhncloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NHN Cloud

- `compute/nhn-cloud` | fails-identity | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone yes, ID no, institution no | verified 2026-11-25T05:18:13.620Z (live) | stale on 2026-12-26
- url https://docs.nhncloud.com/ko/nhncloud/ko/user-guide/
- free tier: New members receive a KRW 200,000 signup credit after registering a payment method, usable toward NHN Cloud service payments; Compute Instance is among the services the credit can be used on. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-shot-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | detail: a mobile phone that can receive an SMS code, plus a payment method: the user guide states an individual member needs a mobile phone capable of SMS confirmation and that members are split at signup into Korean and Japanese members, with credits granted only to members in some countries after a payment method is registered; payment is PAYCO credit card or credit card for a Korean personal member and credit card only for a Japanese one, and the credit is one per phone number and one per business number. No hold is stated, debit or prepaid acceptance is not stated, and whether the SMS number must match the signup country is not stated | country: KR or JP
- interface: unknown
- limits:
  - volume-quota (binding): Signup requires an SMS-verifiable mobile number and splits members into Korea and Japan entities only, and the credit is issued only to members in some countries after a payment method is registered. [1]
- limits note: Signup requires an SMS-verifiable mobile number and splits members into Korea and Japan entities only, and the credit is issued only to members in some countries after a payment method is registered.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: KRW 200,000 with GPU instances excluded lands on CPU instances only, which is the one class documented records already holds at USD 13.20 a month for 1 vCPU / 1 GB from the same provider.
- reliability: no reliability event recorded
- notes: The Korean cloud signup credits cluster at KRW 100,000 to KRW 300,000 and all sit behind a business registration or a domestically verifiable phone. The GPU exclusion is the detail that matters, because the headline figure would otherwise read as GPU credit.
- extras:
  - facets.class: regional-credit
  - facets.free_tier_kind: one-shot-credit
- evidence:
  - [1] 2026-10-22: the user guide states, in Korean, that an individual member needs a mobile phone capable of SMS confirmation, that members are split by the country chosen at signup into Korean members and Japanese members, that credits are granted only to members in some countries after registering a payment method, and that excluded services are Notification, GPU Instance, the marketplace and separately quoted services
  - [2] 2026-10-22: 
  - [1] 2026-10-22: the user guide lists the payment methods by signup country, in Korean: Korea personal is PAYCO credit card or credit card, Japan is credit card only
  - [2] 2026-11-25: new members get a KRW 200,000 credit after registering a payment method, usable toward NHN Cloud charges | capture: sha256:2f3a7d6990caf3d7250177718e030a5254c57b68dac77bbc3f118c04a3e0f19e | quote: NHN Cloud 서비스 이용 요금을 결제할 수 있는 20만 원 상당의 크레딧입니다. 신규 회원 가입 후 결제 수단을 등록하여 ‘가입 축하 크레딧’을 받을 수 있습니다.
  - [2] 2026-11-25: the KRW 200,000 signup credit after registering a payment method is still stated | capture: sha256:2f3a7d6990caf3d7250177718e030a5254c57b68dac77bbc3f118c04a3e0f19e | quote: NHN Cloud 서비스 이용 요금을 결제할 수 있는 20만 원 상당의 크레딧입니다. 신규 회원 가입 후 결제 수단을 등록하여 ‘가입 축하 크레딧’을 받을 수 있습니다.
- sources:
  - [1] https://docs.nhncloud.com/ko/nhncloud/ko/user-guide/
  - [2] https://m.blog.naver.com/nhncloud_official/222982284804
