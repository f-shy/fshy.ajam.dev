# VikingFile

> vikingfile.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vikingfile/ | JSON https://fshy.ajam.dev/api/v1/entity/vikingfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VikingFile

- `storage/vikingfile` | qualifies-with-caveat | evidence documented | binding retention-clamped | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:03:57.987Z (live) | stale on 2026-12-04
- url https://vikingfile.com
- price 10 EUR per TB stored per month on the Option for webmaster (traffic unlimited); Premium is 10 EUR per month. | parsed USD 11.2/TB-mo
- free tier: The page states unlimited storage, anonymous use and no speed limit on the free Regular plan, which shows full advertisement and a captcha. The unlimited claim is not measured. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Free Regular plan: files deleted 15 days after last download. Premium: files never deleted if shared. | days: 15 | source: [1] | note: not stated
- egress: Free Regular plan: downloads go through a landing page with a captcha and full advertisement; no speed limit is claimed and no GB meter is published. | metered: no
- identity: anonymous | detail: The page states that no email is required to upload.
- interface: unknown
- limits:
  - retention-clamped (binding): free Regular plan: files deleted 15 days after last download [1]
- limits note: Unpublished per-file and retention terms; only the marketing claims are visible without a session.
- binding note: free files are deleted 15 days after last download, so stored data does not persist without downloads or a paid plan; the unlimited storage claim is not measured
- interface detail: wrapper-only
- tooling: No documented API; the endpoints found in the page source (/api/complete, /api/get, /api/upload-url) reject naive curl with an HTML error page, so a browser/session is required.
- composes with: Anonymous, no-mail, no-size-limit uploads. The same shape as Buzzheavier/ZeroFS. Retention policy is unpublished, which is the risk.
- reliability: Landing page contains no published terms or documentation. Upload endpoints return error pages to programmatic requests. Storage quota claims remain unverified.
- notes: The page states unlimited storage, anonymous use and no speed limit; the free Regular plan deletes files 15 days after last download.
- evidence note: page read on 2026-11-03: vikingfile.com (landing page: Unlimited storage, Anonymous, No speed limit, No mail required; REGULAR is Free with Full advertisement, Landing page for download, Captcha, Files deleted 15 days after last download; PREMIUM is 10 € / month with Files never deleted if shared). Upload endpoints were not probed on 2026-11-03 and the unlimited-storage claim is not measured.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Tagline: 'Share large files anonymously. Unlimited storage. No mail required. No speed limit. No size limit.' No numeric quota page found.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: meta description 'Unlimited storage. No mail required. No speed limit. No size limit.'
  - [2] 2026-10-21: probe: POST -F file=@vk2.txt -> 200 text/html 'File not found' (no JSON API)
  - [1] 2026-11-03: the page states unlimited storage, anonymous use and no speed limit | capture: sha256:3571d383f5b34363e99b8b6e75041836a9c17e468b7b2cb5d6ff9b5790a6d7e6 | quote: No speed limit Unlimited storage Anonymous
  - [1] 2026-11-03: the free Regular plan shows advertisements and a captcha and deletes files 15 days after last download | capture: sha256:3571d383f5b34363e99b8b6e75041836a9c17e468b7b2cb5d6ff9b5790a6d7e6 | quote: ### REGULAR --- Free Full advertisement Landing page for download Captcha Files deleted 15 days after last download
  - [1] 2026-11-03: the page states unlimited filesize and no mail required | capture: sha256:3571d383f5b34363e99b8b6e75041836a9c17e468b7b2cb5d6ff9b5790a6d7e6 | quote: Unlimited filesize No mail required
  - [1] 2026-11-03: the Option for webmaster is 10 EUR per TB stored per month with unlimited traffic | capture: sha256:3571d383f5b34363e99b8b6e75041836a9c17e468b7b2cb5d6ff9b5790a6d7e6 | quote: ### OPTION FOR WEBMASTER --- 10 € / TB stored / month Traffic unlimited
  - [1] 2026-11-03: Premium is 10 EUR per month and never deletes shared files | capture: sha256:3571d383f5b34363e99b8b6e75041836a9c17e468b7b2cb5d6ff9b5790a6d7e6 | quote: ### PREMIUM --- 10 € / month No advertisement Direct download No captcha Files never deleted if shared
  - [1] 2026-11-03: the free Regular plan deletes files 15 days after last download | capture: sha256:3571d383f5b34363e99b8b6e75041836a9c17e468b7b2cb5d6ff9b5790a6d7e6 | quote: Files deleted 15 days after last download
- sources:
  - [1] https://vikingfile.com/
  - [2] https://vikingfile.com/api/complete
