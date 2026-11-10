# 八八ファイル便

> 88file.jp | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/88file/ | JSON https://fshy.ajam.dev/api/v1/entity/88file.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 八八ファイル便 / 88file.jp

- `storage/88file-jp` | qualifies-with-caveat | evidence inferred | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://88file.jp
- free tier: Claims '容量無制限のファイル転送を無料にて提供します' (unlimited-capacity file transfer, free) and 'データ送信量の制限はありません'. No send-volume limit, free, ad-free, domestic Japanese servers. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No metered egress claimed; ad-free at the free tier. | metered: yes
- identity: anonymous
- interface: rest
- limits note: Unverified. The landing page states unlimited, but /datafiles/new, /plan, /faq and /about all return 503 '現在システムメンテナンス中'. Do not treat the unlimited claim as usable until the upload path answers.
- interface detail: rest
- tooling: Web form only. No API.
- composes with: Nominally unlimited capacity, but unverified. Upload and pricing endpoints returned HTTP 503 on 2026-10-21.
- reliability: This is the classic Japanese small-host failure mode: the marketing page stays up and the actual service is down. Every functional URL 503'd while the root page served fine, which is exactly the 'never trust HTTP 200' trap in reverse. Here the 200 was the brochure and the 503 was the service.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '容量無制限のファイル転送を無料にて提供します', 'データ送信量の制限はありません'
  - withheld 2026-10-21: probe: GET /datafiles/new -> 503, /plan -> 503, /faq -> 503, /about -> 503, body title '八八ファイル便 - 現在システムメンテナンス中'
- sources:
  - [1] https://88file.jp/
