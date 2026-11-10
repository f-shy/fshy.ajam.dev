# AnyFlip

> anyflip.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anyflip/ | JSON https://fshy.ajam.dev/api/v1/entity/anyflip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AnyFlip (flipbook PDF host)

- `storage/anyflip` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://anyflip.com
- free tier: FREE plan: 100 GB storage, unlimited number of publications, 5 uploads/day, 150 MB max PDF. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 GB cap | bytes: 100000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress metering documented; free plan caps "Daily Opens" at 30,000/day and readers can download the PDF; flipbooks are served from online.anyflip.com with a per-page HTML reader. Free tier embeds an AnyFlip watermark in the embed. | metered: no
- identity: email
- interface: unknown
- limits:
  - request-rate: 5 uploads/day [1]
  - per-object-cap (binding): 100 GB cap [1]
- limits note: 150 MB per PDF; 5 uploads/day free (60/day Pro); 30,000 daily opens; 100 GB cap; watermark on free embeds; download of the source PDF is plan-gated in practice.
- interface detail: wrapper-only
- tooling: No public API; upload is the web form at anyflip.com/quick-upload/ (POST without a session 302s to /login.php). Flipbook pages are static per-page HTML at online.anyflip.com/<a>/<b>/files/basic-html/pageN.html so a downloader can be written, but there is no upload client.
- composes with: Multiple free accounts provide 100 GB each. Upload rate is the primary constraint: 5 uploads per day at 150 MB yields 750 MB per day per account.
- reliability: Originals are re-served as derived page images, and the free download path returns 403 without a session; content is publicly listed, so anything put here is discoverable.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: table: 'Storage | 100G' (free column), 'Uploads / Day | 5', 'Daily Opens | 30 000'
  - [2] 2026-10-21: 'The max PDF file size is 150 MB'; 'There is no limit on the publications you may have'
  - [3] 2026-10-21: probe: POST -F file=@t.pdf -> 302 Location: /login.php (no anonymous upload)
  - [4] 2026-10-21: probe: GET -> 200 HTML reader page; GET https://online.anyflip.com/xrbo/eygi/download.pdf -> 403
- sources:
  - [1] https://anyflip.com/pricing/
  - [2] https://anyflip.com/faq/
  - [3] https://anyflip.com/quick-upload/
  - [4] https://online.anyflip.com/xrbo/eygi/files/basic-html/page2.html
