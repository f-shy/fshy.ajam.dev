# データ便

> datadeliver.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datadeliver/ | JSON https://fshy.ajam.dev/api/v1/entity/datadeliver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## データ便 / DataDeliver (dd.datadeliver.net)

- `storage/datadeliver` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:32.922Z (live) | stale on 2026-12-04
- url https://datadeliver.net
- free tier: Free tier: 5 GB per transfer (registered, free), 2 GB per transfer (Light, no registration). '1回の転送容量' is 無制限 only on the 330/550-yen business plan. The site's own headline says 無料無制限. The plan table contradicts it. No total storage: '転送容量は1回に転送できる最大容量となり、何度でもご利用いただけます'. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 5 GB | bytes: 5000000000 | source: [1] | note: not stated
- retention: Retention 7 days on the free and light (no-registration) plans, 30 days on the business plan | days: 7 | source: [1] | note: not stated
- egress: No metered egress; free tiers are ad-supported, business tier is ad-free. | metered: yes
- identity: anonymous
- interface: rest, rclone
- limits:
  - retention-clamped: Retention 7 days [1]
  - per-object-cap (binding): per-object-cap 5 GB [1]
- limits note: per-object-cap 5 GB (free) / 2 GB (guest). Retention 3 days guest, 7 days free registered, 30 days business. Free tier gets throttled transfer speed (`△` vs `〇`).
- interface detail: rest
- tooling: Web form; no API, no rclone backend.
- composes with: 5 GB x unlimited sends, but 7-day retention on free means chaining is strictly a re-send loop, not accumulation.
- reliability: Running since 2004, ~3M users/month, run by 株式会社ファルコ. Stable, but the 無料無制限 headline on the marketing page is marketing. The plan table is the truth.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free tier: 5 GB per transfer (registered, free), 2 GB per transfer (Light, no registration). '1回の転送容量' is 無制限 only on the 330/550-yen business plan. The site's own headline says 無料無制限 — the plan table contradicts it. No total storage: '転送容量は1回に転送できる最大容量となり、何度でもご利用いただけます'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: free plan '1回の転送容量 ~~2GB~~ 5GB', 'データ保管期間 ~~3日間~~ 7日間', business plan '無制限' / '30日間'
  - [2] 2026-10-21: 2024-03-04 changelog: '500MB→2GB ライトプラン', '2GB→5GB フリープラン'
  - [3] 2026-10-21: page title claims '無料無制限の大容量ファイル送信'
  - [1] 2026-11-19: the plan table now states 7-day retention on the free and light plans | capture: sha256:645ca2eb026088c44d069ea77b2fbd9e8f387d585b5364dc3d01f89d8c76376a | quote: | データ保管期間 | 30日間 | ~~3日間~~ 7日間 | ~~3日間~~ 7日間 |
  - [1] 2026-11-19: the plan table states 5GB per transfer on the free plan and 2GB without registration | capture: sha256:645ca2eb026088c44d069ea77b2fbd9e8f387d585b5364dc3d01f89d8c76376a | quote: | 1回の転送容量 | 無制限 | ~~2GB~~ 5GB | ~~500MB~~ 2GB |
  - [1] 2026-11-19: the plan table states the free plans cost nothing and the business plan is paid; one account per email address | capture: sha256:645ca2eb026088c44d069ea77b2fbd9e8f387d585b5364dc3d01f89d8c76376a | quote: | 利用料金 | 月額 ￥330／￥550 ※1アカウント=1メールアドレス | ￥0 | ￥0 |
  - [1] 2026-11-19: the plan page says the transfer volume is a per-send maximum and can be used repeatedly | capture: sha256:645ca2eb026088c44d069ea77b2fbd9e8f387d585b5364dc3d01f89d8c76376a | quote: ・転送容量は1回に転送できる最大容量となり、何度でもご利用いただけます。
  - [2] 2026-11-19: the first-party changelog records the free-plan increase to 5GB | capture: sha256:624b8b37897f836258ad9a58fa364aa38c89999b2b2f29cf4ada06a7b45ef906 | quote: ◆2GB→5GB ※フリープラン(無料・要会員登録)
  - [3] 2026-11-19: the first-party upload page restates 2GB light, 5GB free and unlimited business | capture: sha256:625f3b1eec9c55d6579ad846fecb7ae64ab376a7550681367cc78252e121c06b | quote: ※アップロードできるファイルの容量は、ライトプラン:2GB、フリープラン:5GB、ビジネスプラン:容量無制限となります。
- sources:
  - [1] https://dd.datadeliver.net/plan/
  - [2] https://dd.datadeliver.net/info/update-240304/
  - [3] https://datadeliver.net/
