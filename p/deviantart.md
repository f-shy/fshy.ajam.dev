# DeviantArt Sta.sh

> deviantart.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deviantart/ | JSON https://fshy.ajam.dev/api/v1/entity/deviantart.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DeviantArt Sta.sh

- `storage/deviantart-sta-sh` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:34.057Z (live) | stale on 2026-12-04
- url https://deviantart.com
- free tier: 2 GB Sta.sh storage free, up to 100 GB with Core | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free direct CDN links on wixmp.com; no egress metering | metered: no
- identity: institution
- interface: rest
- limits note: 2 GB total free (hard cap, not per-file); non-image files 200 MB (1 GB Core); video submissions Core-only; Sta.sh items are private until published
- interface detail: rest
- tooling: DeviantArt published API (OAuth2, /api/v1/.. stash endpoints); mostly stale since the 2020 ownership change. Wrapper risk is high.
- composes with: 2 GB x unlimited free accounts. 500 GB = 250 accounts. Repeatable but tedious; the 200 MB per-file cap is the more useful dimension for mixed data.
- reliability: 2 GB is a real, enforced bucket cap and the API is legacy; no bulk path worth building
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 2 GB Sta.sh storage free, up to 100 GB with Core
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'All deviants receive 2GB of Sta.sh storage space ... Core Members receive up to 100GB'
  - [2] 2026-10-21: 'Non-Images: 200MB (1GB for Core Members)'
  - [1] 2026-11-19: free Sta.sh storage is 2GB, up to 100GB with Core | capture: sha256:b766369b5450ac8e6f8357553e254aa2f61cf9f38506cded3f7a3402a63582d5 | quote: All deviants receive 2GB of Sta.sh storage space to freely use, and Core Members receive up to 100GB of storage space, depending on their Core plan.
  - [2] 2026-11-19: non-image files are capped at 200MB, 1GB for Core | capture: sha256:83eec299163f1c65d9ec146f4059a7e133021c1b4894987de03bfeb4ef19dfb8 | quote: - Non-Images: 200MB (1GB for [Core Members](https://www.deviantart.com/core-membership/))
- sources:
  - [1] https://www.deviantartsupport.com/kb/en/article/what-is-stash-3391708
  - [2] https://www.deviantartsupport.com/kb/en/article/what-file-types-can-i-submit-to-deviantart
