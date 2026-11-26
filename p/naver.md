# Naver MYBOX

> naver.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/naver/ | JSON https://fshy.ajam.dev/api/v1/entity/naver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Naver MYBOX (네이버 마이박스)

- `netdisk-pan/naver-mybox` | fails-quota | evidence reported | binding per-object-cap | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T14:05:44.509Z (inherited) | stale on 2026-12-10
- url https://mybox.naver.com
- free tier: 국내 최대 무료 용량 30GB로 시작하세요. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: unverified: a third party reports 4 GB per file on the free plan but now states the figure is not confirmed against official guidance; maxFileBytes is returned per account and depends on the plan | source: [2]
- retention: unverified: a third party previously reported dormancy after two years without a login, but now states no MYBOX-specific dormancy deletion rule was found in official documents and that the general Naver account policy appears to apply | source: [2]
- egress: No egress fee documented. The binding limit is the API's 50,000 downloads a day, flat across all plan tiers from 30 GB to 20 TB; the page states the plan tiers share one limit only until 2026-12-31 and limits may differ by plan after that date | metered: yes | free allowance: 50,000 downloads a day | source: [3]
- identity: any-phone | detail: If you are using a mobile phone, you can verify your identity when signing up even if the mobile phone is not subscribed under your name, but you cannot sign up by any means other than your mobile phone. | country: kr
- interface: rest
- limits:
  - per-object-cap (binding): unverified: a third party reports 4 GB per file on the free plan but now states the figure is not confirmed against official guidance [2]
  - request-rate: 50,000 API downloads a day, 30 searches a minute and 240 deletes a minute [3]
  - retention-clamped: unverified: a third party previously reported dormancy after two years without a login, but now states no MYBOX-specific dormancy deletion rule was found in official documents [2]
- binding note: Storage is limited to 30 GB total on the first-party page. The 4 GB per-file cap and the dormancy deletion rule are unverified: the third party that supplied them now says official guidance does not confirm either.
- tooling: an official MYBOX Open API with personal access tokens against https://open-api.mybox.naver.com/v1, bearer mbx_pat_ tokens with a 30, 60, 90 or 180-day lifetime and at most five per account. No rclone backend
- composes with: 30 GB times N Naver IDs, where each needs a real-name-verifiable Naver account.
- reliability: An explicit excess-use clause: bulk calls or excess use get access restricted without notice, and dormant accounts and their tokens fail. The market consolidated and MYBOX is the only Korean free personal drive left
- notes: The cleanest documented API in the Asian drive set and the smallest quota.
- extras:
  - access_mode: registration-gated
  - api_tokens: 5 per account, 30 to 180-day lifetime
  - dormancy_days: 730
  - aliases: Naver MYBOX (네이버 마이박스)
- evidence:
  - [1] 2026-10-21: '국내 최대 무료 용량 30GB를 제공'
  - [3] 2026-10-21: the API daily limits table gives '50,000회/일' for downloads across 30 GB to 20 TB, and '단시간 대량 호출, 어뷰징 등이 감지될 경우 ... 서비스 이용이 제한될 수 있습니다'
  - [4] 2026-10-21: GET /v1/drive/storage with a bearer PAT returns quotaBytes, usedBytes and maxFileBytes
  - [2] 2026-10-21: MYBOX 30 GB, '파일 1개당 4GB(무료 30GB 기준)', '2년 이상 미로그인 시 휴면 전환, 저장 파일 삭제'
  - [5] 2026-10-21: '네이버 MYBOX 30GB 무료' as the largest domestic free tier
  - probe:https://open-api.mybox.naver.com/v1/drive/storage 2026-10-21: 401 with {"code":"PLAT-401","message":"UNAUTHORIZED"}, so the API is live
  - [6] 2026-11-25: the free plan still starts at 30 GB | capture: sha256:44dc5a1ab75037437ce698e68f6414613c3b2e3cd8d27bff508fdec6551a0d3b | quote: 국내 최대 무료 용량 30GB로 시작하세요.
  - [3] 2026-11-25: the 50,000-downloads-per-day allowance is still flat across all eight tiers | capture: sha256:c39418cbc9e7e91f505b3cd1cc875f2cba66362e327177d2341e4dae3b63df39 | quote: | 다운로드 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 |
  - [3] 2026-11-25: the shared limit across tiers is still stated as temporary until 2026-12-31 | capture: sha256:c39418cbc9e7e91f505b3cd1cc875f2cba66362e327177d2341e4dae3b63df39 | quote: 26.12.31까지 한시적으로 모든 요금제 한도가 동일하게 적용됩니다.
  - [2] 2026-11-25: the third party that sourced the 4 GB figure now marks it as unconfirmed against official guidance | capture: sha256:b770398adc17cd863fdffe6d7154b7006b13e0c85fb5be2e60f36d5c0bedbef8 | quote: | 1 | 네이버 MYBOX | 30GB | 무료 요금제 4GB라는 자료가 있으나 공식 안내 기준 확인 필요 | MYBOX 전용 휴면 삭제 규정은 공식 문서에서 확인하지 못함. 네이버 계정 정책을 따르는 것으로 보임 | 있음 (Windows, macOS) | 예 |
  - [7] 2026-11-25: the introduction page states 30GB as the starting free capacity | capture: sha256:44dc5a1ab75037437ce698e68f6414613c3b2e3cd8d27bff508fdec6551a0d3b | quote: 국내 최대 무료 용량 30GB로 시작하세요.
  - [8] 2026-11-25: signup requires a mobile phone and allows a phone not in the user's name, with no national ID named | capture: sha256:40ed96631f4829a52d75ca42fa404500a337545ecccf809b3f8d0b4c9c85ac1f | quote: If you are using a mobile phone, you can verify your identity when signing up even if the mobile phone is not subscribed under your name, but you cannot sign up by any means other than your mobile phone.
- sources:
  - [1] https://help.naver.com/service/5594/contents/329?lang=ko
  - [2] https://bokgoon.com/free-cloud-storage-services/
  - [3] https://developers.mybox.naver.com/getting-started
  - [4] https://developers.mybox.naver.com/docs/dms_storage
  - [5] https://webhardrank.kr/legal-file-sharing-webhard-alternatives/
  - [6] https://mybox.naver.com/
  - [7] https://mybox.naver.com
  - [8] https://help.naver.com/service/5594/contents/20782?osType=PC&lang=ko
