# uploader.jp

> uploader.jp | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploader/ | JSON https://fshy.ajam.dev/api/v1/entity/uploader.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## uploader.jp / getuploader.com (アップローダーレンタル)

- `storage/uploader-jp-getuploader-com` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:31.025Z (live) | stale on 2026-12-04
- url https://uploader.jp
- free tier: 10 GB total per account: 100 MB per file, 1,000 MB per uploader, 10 uploaders per account = 10 GB. Free, and the terms state '当サイトが金銭を要求することは一切ありません'. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: 1 GB per uploader, 10 GB per account. No retention limit (persistent hosting, unlike the transfer services), which is the one thing it does better than Gigafile. | source: [1] | note: not stated
- egress: No meter; ad-supported on download pages. | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 100 MB per file [1]
  - per-object-cap (binding): 1,000 MB per upload [1]
- limits note: per-object-cap 100 MB. 1 GB per uploader, 10 GB per account. No retention limit (persistent hosting, unlike the transfer services), which is the one thing it does better than Gigafile.
- interface detail: rest
- tooling: Per-uploader web forms with no API. Community-maintained link lists exist (w.atwiki.jp/vbmaker, uploaders.jp).
- composes with: 10 uploaders x 1 GB inside one account; multiple accounts would be needed to pass 500 GB, and 100 MB per file is the hard wall. This cannot hold bulk data of any kind.
- reliability: Genuinely old and genuinely alive. A sample uploader showed files posted the previous day in Sept 2026, while the official site's own copy still says 2017. Default configuration makes every upload publicly listable and search-indexable.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GB total per account: 100 MB per file, 1,000 MB per uploader, 10 uploaders per account = 10 GB. Free, and the terms state '当サイトが金銭を要求することは一切ありません'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'アップローダーまで 1 アカウント あたり MBまで' (Live counter), '完全無料'
  - [2] 2026-10-21: measured 2026-09-04: '1ファイル100MB', '1アップローダー1,000MB', '1アカウント合計10,000MB', 'アップローダーは1アカウントにつき10個'
  - [1] 2026-11-19: the service still advertises free long-term file storage | capture: sha256:13bfa40dc736f7bceeb3c6b835eec7c0144e25957d797c2cad07d248cee7be93 | quote: すべての機能が無料でご利用頂けます。何千件、何万件でも長期間ファイルを保存、公開できます。
  - [1] 2026-11-19: one account can still rent up to 10 uploaders | capture: sha256:13bfa40dc736f7bceeb3c6b835eec7c0144e25957d797c2cad07d248cee7be93 | quote: ひとつのアカウントで10個までアップローダーをレンタルできます。
- sources:
  - [1] https://uploader.jp/
  - [2] https://giga-watasu.jp/blog/uploader-jp
