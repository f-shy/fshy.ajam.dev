# データ便

> datadeliver.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datadeliver/ | JSON https://fshy.ajam.dev/api/v1/entity/datadeliver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## データ便 / DataDeliver (dd.datadeliver.net)

- `storage/datadeliver` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://datadeliver.net
- free tier: Free tier: 5 GB per transfer (registered, free), 2 GB per transfer (Light, no registration). '1回の転送容量' is 無制限 only on the 330/550-yen business plan. The site's own headline says 無料無制限. The plan table contradicts it. No total storage: '転送容量は1回に転送できる最大容量となり、何度でもご利用いただけます'. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 5 GB | bytes: 5000000000 | source: [1] | note: not stated
- retention: Retention 3 days guest, 7 days free registered, 30 days business | days: 3 | source: [1] | note: not stated
- egress: No metered egress; free tiers are ad-supported, business tier is ad-free. | metered: yes
- identity: anonymous
- interface: rest, rclone
- limits:
  - retention-clamped: Retention 3 days [1]
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
- sources:
  - [1] https://dd.datadeliver.net/plan/
  - [2] https://dd.datadeliver.net/info/update-240304/
  - [3] https://datadeliver.net/
