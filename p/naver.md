# Naver MYBOX

> naver.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/naver/ | JSON https://fshy.ajam.dev/api/v1/entity/naver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Naver MYBOX (네이버 마이박스)

- `netdisk-pan/naver-mybox` | fails-quota | evidence reported | binding per-object-cap | category consumer-pan
- needs card no, phone no, ID yes, institution no | verified 2026-11-04T00:21:08.720Z (inherited) | stale on 2026-11-19
- url https://mybox.naver.com
- free tier: 30 GB free: '국내 최대 무료 용량 30GB'. MYBOX+ adds 50 GB, 150 GB, 300 GB, 2 TB, 5 TB, 10 TB or 20 TB on top of the base | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GB per file on the free 30 GB plan; maxFileBytes is returned per account and depends on the plan | bytes: 4000000000 | source: [2]
- retention: Dormant after two years without a login, and stored files are deleted | days: 730 | source: [2]
- egress: No egress fee documented. The binding limit is the API's 50,000 downloads a day, flat across all plan tiers from 30 GB to 20 TB; the page states the plan tiers share one limit only until 2026-12-31 and limits may differ by plan after that date | metered: yes | free allowance: 50,000 downloads a day | source: [3]
- identity: national-id | detail: a Naver account that passes Korean real-name verification, which is the wall the forum reports agree on | country: kr
- interface: rest
- limits:
  - per-object-cap (binding): 4 GB per file on the free plan [2]
  - request-rate: 50,000 API downloads a day, 30 searches a minute and 240 deletes a minute [3]
  - retention-clamped: two years without a login makes the account dormant and deletes the files [2]
- binding note: Storage is limited to 30 GB total with a 4 GB per-file cap, and stored content is deleted after 730 days of account dormancy. The 4 GB per-file ceiling remains an immutable boundary across multiple accounts.
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
  - [6] 2026-11-03: the MYBOX introduction page still states 30 GB as the free capacity | capture: sha256:44dc5a1ab75037437ce698e68f6414613c3b2e3cd8d27bff508fdec6551a0d3b | quote: 국내 최대 무료 용량 30GB로 시작하세요.
  - [3] 2026-11-03: the identical per-plan API limits are stated as temporary until 2026-12-31, after which they may change by plan | capture: sha256:c39418cbc9e7e91f505b3cd1cc875f2cba66362e327177d2341e4dae3b63df39 | quote: 26.12.31까지 한시적으로 모든 요금제 한도가 동일하게 적용됩니다.
  - [3] 2026-11-03: downloads are limited to 50,000 per day on every plan from 30 GB to 20 TB | capture: sha256:c39418cbc9e7e91f505b3cd1cc875f2cba66362e327177d2341e4dae3b63df39 | quote: | 다운로드 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 | 50,000회/일 |
- sources:
  - [1] https://help.naver.com/service/5594/contents/329?lang=ko
  - [2] https://bokgoon.com/free-cloud-storage-services/
  - [3] https://developers.mybox.naver.com/getting-started
  - [4] https://developers.mybox.naver.com/docs/dms_storage
  - [5] https://webhardrank.kr/legal-file-sharing-webhard-alternatives/
  - [6] https://mybox.naver.com
