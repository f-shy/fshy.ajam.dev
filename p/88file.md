# 八八ファイル便

> 88file.jp | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/88file/ | JSON https://fshy.ajam.dev/api/v1/entity/88file.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 八八ファイル便 / 88file.jp

- `storage/88file-jp` | qualifies-with-caveat | evidence inferred | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-25T03:33:10.196Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://88file.jp
- free tier: 容量無制限のファイル転送を無料にて提供します。 | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: unverified: the landing page publishes no per-object size cap and the upload page served a maintenance notice on 2026-11-25, so no upload form could be read.
- retention: データ保存３日間 | days: 3 | source: [1] | note: The free Basic plan states "データ保存３日間" (three-day data retention).
- egress: No metered egress claimed; ad-free at the free tier. | metered: no
- identity: anonymous | detail: unverified: the upload page served its maintenance notice on 2026-11-09, so no signup form was seen
- interface: rest
- limits note: Unverified. The landing page states unlimited, but /datafiles/new, /plan, /faq and /about all return 503 '現在システムメンテナンス中'. Do not treat the unlimited claim as usable until the upload path answers.
- interface detail: rest
- tooling: Web form only. No API.
- composes with: Nominally unlimited capacity, but unverified. Upload and pricing endpoints returned HTTP 503 on 2026-10-21.
- reliability: This is the classic Japanese small-host failure mode: the marketing page stays up and the actual service is down. Every functional URL 503'd while the root page served fine, which is exactly the 'never trust HTTP 200' trap in reverse. Here the 200 was the brochure and the 503 was the service.
- notes: Claims '容量無制限のファイル転送を無料にて提供します' (unlimited-capacity file transfer, free) and 'データ送信量の制限はありません'. No send-volume limit, free, ad-free, domestic Japanese servers.
- evidence:
  - [1] 2026-10-21: '容量無制限のファイル転送を無料にて提供します', 'データ送信量の制限はありません'
  - withheld 2026-10-21: probe: GET /datafiles/new -> 503, /plan -> 503, /faq -> 503, /about -> 503, body title '八八ファイル便 - 現在システムメンテナンス中'
  - [1] 2026-11-09: the landing page states unlimited-capacity file transfer is provided free | capture: sha256:56d63a4dc65656e70a36f64d9d4d82a7392e4b9945ff1b2c18d7ea3efc8bac62 | quote: 「八八ファイル便」とは、完全国内運用で安心安全、無料の大容量ファイル転送サービスです。容量無制限のファイル転送を無料にて提供します。
  - [1] 2026-11-09: the free Basic plan lists three-day data retention | capture: sha256:56d63a4dc65656e70a36f64d9d4d82a7392e4b9945ff1b2c18d7ea3efc8bac62 | quote: データ保存３日間
  - [1] 2026-11-09: the landing page states there is no send-volume limit | capture: sha256:56d63a4dc65656e70a36f64d9d4d82a7392e4b9945ff1b2c18d7ea3efc8bac62 | quote: 「八八ファイル便」にデータ送信量の制限はありません。送りたい分のデータを個人商用問わず制限なく送信いただけます。
  - [2] 2026-11-09: the upload page is a maintenance notice, so no signup or upload form could be read | capture: sha256:d912db465f4572038b81bfa9af319b65f1ec914bbf0c581c6416a9bed11a2368 | quote: 現在システムメンテナンス中
  - [2] 2026-11-25: the upload page is a maintenance notice, so no per-object cap is observable | capture: sha256:d912db465f4572038b81bfa9af319b65f1ec914bbf0c581c6416a9bed11a2368 | quote: 現在システムメンテナンス中
  - [1] 2026-11-25: the free Basic plan keeps data for three days | capture: sha256:56d63a4dc65656e70a36f64d9d4d82a7392e4b9945ff1b2c18d7ea3efc8bac62 | quote: データ保存３日間
  - [1] 2026-11-25: the first-party pricing table still states three-day data retention | capture: sha256:56d63a4dc65656e70a36f64d9d4d82a7392e4b9945ff1b2c18d7ea3efc8bac62 | quote: データ保存３日間
  - [2] 2026-11-25: the upload page remains a maintenance notice, so no per-object cap can be read | capture: sha256:d912db465f4572038b81bfa9af319b65f1ec914bbf0c581c6416a9bed11a2368 | quote: 現在システムメンテナンス中
- sources:
  - [1] https://88file.jp/
  - [2] https://88file.jp/datafiles/new
