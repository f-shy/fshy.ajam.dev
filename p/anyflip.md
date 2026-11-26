# AnyFlip

> anyflip.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anyflip/ | JSON https://fshy.ajam.dev/api/v1/entity/anyflip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AnyFlip (flipbook PDF host)

- `storage/anyflip` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T13:25:54.291Z (live) | stale on 2026-12-10
- url https://anyflip.com
- free tier: FREE plan: 100 GB storage, unlimited number of publications, 5 uploads/day, 150 MB max PDF. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 150 MB maximum PDF file size | bytes: 150000000 | source: [2] | note: The FAQ states a 150 MB maximum PDF file size; the total storage quota is a separate pricing figure.
- retention: AnyFlip Cloud hosts publications forever, and the account may be used forever. | source: [2] | note: The FAQ states that publications are hosted forever and the account may be used forever.
- egress: No egress metering documented; free plan caps "Daily Opens" at 30,000/day and readers can download the PDF; flipbooks are served from online.anyflip.com with a per-page HTML reader. Free tier embeds an AnyFlip watermark in the embed. | metered: no
- identity: email
- interface: browser
- limits:
  - request-rate: 5 uploads/day [1]
  - per-object-cap (binding): 150 MB maximum PDF size [2]
- limits note: 150 MB per PDF; 5 uploads/day free (60/day Pro); 30,000 daily opens; 100 GB cap; watermark on free embeds; download of the source PDF is plan-gated in practice.
- interface detail: Website Quick Upload after login; the installed desktop software is documented separately.
- tooling: No public API; upload is the web form at anyflip.com/quick-upload/ (POST without a session 302s to /login.php). Flipbook pages are static per-page HTML at online.anyflip.com/<a>/<b>/files/basic-html/pageN.html so a downloader can be written, but there is no upload client.
- composes with: Multiple free accounts provide 100 GB each. Upload rate is the primary constraint: 5 uploads per day at 150 MB yields 750 MB per day per account.
- reliability: Originals are re-served as derived page images, and the free download path returns 403 without a session; content is publicly listed, so anything put here is discoverable.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: table: 'Storage | 100G' (free column), 'Uploads / Day | 5', 'Daily Opens | 30 000'
  - [2] 2026-10-21: 'The max PDF file size is 150 MB'; 'There is no limit on the publications you may have'
  - [3] 2026-10-21: probe: POST -F file=@t.pdf -> 302 Location: /login.php (no anonymous upload)
  - [4] 2026-10-21: probe: GET -> 200 HTML reader page; GET https://online.anyflip.com/xrbo/eygi/download.pdf -> 403
  - [1] 2026-11-19: the free plan allows 5 uploads per day | capture: sha256:fe291709dca964fb101db7807cd6bc74e875c21f8ef600697859bb54a6332b72 | quote: | Uploads / Day | 5 | 60 | 100 | Unlimited |
  - [5] 2026-11-25: the online upload flow starts on the AnyFlip website navigation menu | capture: sha256:1c219a8f8250fed66f3eac0768233cbb8f4ed51cb46ead296bc445f3a8c28e35 | quote: Visit AnyFlip website (<a href="//anyflip.com/" target="_blank"><b>http://anyflip.com/</b></a>) and on the navigation menu, click "login" (or "Upload").
  - [6] 2026-11-25: the website upload flow uses Quick Upload after login | capture: sha256:7551c59f804e0f3a5789887e4599a439b15df232a6931d60a3788ac05f51d84e | quote: You can click the Quick Upload button on the Navigation Bar as you log in.
  - [2] 2026-11-25: the FAQ states permanent hosting for publications | capture: sha256:80c5749a6adc1e27f871be413c48d6ba1e9f38a09af6b5c30f725c21c9daeac5 | quote: The AnyFlip Cloud will host your publications forever, You may use this account FOREVER!.
  - [2] 2026-11-25: the per-file PDF cap is 150 MB | capture: sha256:80c5749a6adc1e27f871be413c48d6ba1e9f38a09af6b5c30f725c21c9daeac5 | quote: The max PDF file size is 150 MB.
  - [1] 2026-11-25: the free plan includes 100G of storage | capture: sha256:fe291709dca964fb101db7807cd6bc74e875c21f8ef600697859bb54a6332b72 | quote: | Storage | 100G | 500G | Unlimited | Unlimited |
  - [2] 2026-11-25: the FAQ states no publication-count cap | capture: sha256:80c5749a6adc1e27f871be413c48d6ba1e9f38a09af6b5c30f725c21c9daeac5 | quote: There is no limit on the publications you may have.
- sources:
  - [1] https://anyflip.com/pricing/
  - [2] https://anyflip.com/faq/
  - [3] https://anyflip.com/quick-upload/
  - [4] https://online.anyflip.com/xrbo/eygi/files/basic-html/page2.html
  - [5] https://anyflip.com/manual/online-conversion-sign-in.html
  - [6] https://anyflip.com/manual/online-conversion-upload-pdf.html
