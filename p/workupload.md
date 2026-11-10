# Workupload

> workupload.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/workupload/ | JSON https://fshy.ajam.dev/api/v1/entity/workupload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Workupload

- `debrid/workupload` | qualifies-with-caveat | evidence reported | binding per-object-cap | category free one-click file host, retrieval target | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:53.664Z (live) | stale on 2026-11-18
- url https://workupload.com/
- price unverified: the terms mention paid offers for registered users, and no price page was found
- free tier: 2 GB per file ('A file can not be larger than 2 gigabyte.'), no account needed ('without registration'), no limit on the number of files, and files are removed after 30 days without a call unless a retention period is set. The FAQ answers 'Yes, absolutely free!'; the terms also refer to paid offers for registered users ('With registration and paid offers, users have more options'). | unit: GB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: 2 GB per file | bytes: 2000000000 | source: [1]
- retention: files expire 30 days after the last download (vendor default), extendable at upload time | days: 30 | source: [1]
- egress: No cap published and no paid path to remove one. Users report 200-350 KB/s in practice. | metered: no | free allowance: none published | price per TB: none | source: [1]
- identity: anonymous | detail: No account is needed to upload or download; a free account only raises storage.
- interface: unknown
- limits:
  - per-object-cap (binding): 2 GB per file [1]
  - per-ip-shaping: users report 200-350 KB/s; no vendor number [2]
- limits note: The FAQ answers 'Yes, absolutely free!' and the About page lists the premium features as free for all; the terms mention paid offers for registered users, but no price page was found.
- binding note: 2 GB per file means 1 TiB of monthly transfer is at least 550 files, and the observed 0.33 MiB/s makes the month 36 days of continuous transfer.
- interface detail: Browser upload and download only; no API.
- tooling: browser; no download-manager integration documented
- composes with: A free host: it composes as the source of a one-off file rather than as part of a retrieval stack. The terms mention paid offers for registered users, but none is priced on the pages read.
- reliability: Downloads of a 2 GB file take about two and a half hours at the observed rate; some users report transfers stalling every 10-20 MB.
- notes: Included because it is a host that will be met and it has no key to buy; the free tier is the whole offer.
- evidence note: The vendor page confirms the free-only shape and the 2 GB cap; the rate is a forum report, not a measurement.
- extras:
  - free_speed_mib_s: 0.3338
  - max_file_free: 2 GB
  - api: no
  - price_ladder_reported: none: the service sells no premium plan
  - volume_tib_month: 1.0
- evidence:
  - [1] 2026-10-23: landing page: upload without an account, no premium tier offered
  - [3] 2026-10-23: 'Workupload has only a free offer'; 2 GB package, 90-day expiry
  - [2] 2026-10-23: user reports 200-350 KB/s
  - [4] 2026-11-03: a file is removed after 30 days without a call unless a retention period is set | capture: sha256:d6dcac4b95c5a50ecdb77e5f24adef43cec8f5ce1627496882b0f282ad6c02fc | quote: If your file is 30 days inactive (no call receive), it will be removed. Unless you specify a retention period, your file will be stored until the time of your choosing.
  - [5] 2026-11-03: the terms refer to paid offers for registered users | capture: sha256:8b44e927d7b807836c5c331746ff01f65b6834edf76440f00f39fbef6d0289ce | quote: With registration and paid offers, users have more options to share and manage digital content.
  - [1] 2026-11-03: the home page states the 2 GB file limit and that no registration is needed | capture: sha256:ccd3ef52bfb39a6f92cb6b6a890aab4a785de4b9a496a17a836b98e25240f12b | quote: Up to 2 GB files | without registration | all filetypes | secure and fast
  - [4] 2026-11-03: the FAQ states the 2 GB file limit | capture: sha256:d6dcac4b95c5a50ecdb77e5f24adef43cec8f5ce1627496882b0f282ad6c02fc | quote: A file can not be larger than 2 gigabyte.
  - [4] 2026-11-03: the FAQ states the service is free | capture: sha256:d6dcac4b95c5a50ecdb77e5f24adef43cec8f5ce1627496882b0f282ad6c02fc | quote: Yes, absolutely free!
  - [4] 2026-11-03: the FAQ states there is no limit on the number of files | capture: sha256:d6dcac4b95c5a50ecdb77e5f24adef43cec8f5ce1627496882b0f282ad6c02fc | quote: There is no limit.
  - [6] 2026-11-03: premium features are offered free | capture: sha256:70619a761f7588e058ae171f044ab9e148f597234c308ae793cd1896c0293400 | quote: workupload offers premium features such as Bulk-Download, One-Time-Links and Multi-Uploads for free, for all.
- sources:
  - [1] https://workupload.com/
  - [2] https://p-v.club/threads/workupload-the-speed-download.49673/
  - [3] https://filetransfer.io/workupload
  - [4] https://workupload.com/faq
  - [5] https://workupload.com/legal/terms
  - [6] https://workupload.com/about
