# DooDrive

> doodrive.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/doodrive/ | JSON https://fshy.ajam.dev/api/v1/entity/doodrive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DooDrive

- `debrid/doodrive` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file host (free, ad-supported) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://doodrive.com/faq
- price unverified: no premium price page was readable
- free tier: Free for all users, ad-supported; as many files as you want, each under 2 GB; files may be removed after a period of inactivity. | unit: unlimited | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The FAQ says premium accounts may be offered; no premium price page was found (the /pricing URL answered 404).
- per-object cap: Each file you upload must be less than 2 GB in size. If it is greater than that amount, your file will be rejected. | bytes: 2147483648 | source: [1] | note: bytes = 2 x 1024^3.
- retention: Files may also be removed after a period of inactivity. | source: [1] | note: No number of days is printed on the FAQ.
- egress: No download allowance is printed on the FAQ. | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: unverified: the sign-up form was not read; the FAQ calls it a free cloud file storage service and the homepage lists an upgrade link.
- interface: unknown
- limits:
  - per-object-cap (binding): 2 GB per file [1]
  - retention-clamped: files may be removed after a period of inactivity (days not printed) [1]
- binding note: 2 GB per file is the only published number.
- interface detail: Web upload; the footer links Upgrade Account, Speedtest and Report File.
- tooling: Browser only as read.
- composes with: 2 GB files with an unstated inactivity deletion; a hand-off host.
- reliability: The FAQ states ads cover the running cost.
- evidence note: FAQ read on 2026-11-03. Premium price, retention days and identity are unverified.
- evidence:
  - [1] 2026-11-03: the per-file cap is 2 GB | capture: sha256:dee862c0e87ec8ef385939f8c42fcfcb52e6a55e152ea20f2fde42e7bdc7c40f | quote: Each file you upload must be less than 2 GB in size. If it is greater than that amount, your file will be rejected.
  - [1] 2026-11-03: an inactivity deletion exists with no stated period | capture: sha256:dee862c0e87ec8ef385939f8c42fcfcb52e6a55e152ea20f2fde42e7bdc7c40f | quote: Files may also be removed after a period of inactivity.
  - [1] 2026-11-03: the service is free and ad-supported with possible premium accounts | capture: sha256:dee862c0e87ec8ef385939f8c42fcfcb52e6a55e152ea20f2fde42e7bdc7c40f | quote: Yes, Our service is 100% Free for all users. We rely on advertising to cover the running fee. We may offer premium accounts which allows for greater flexibility with uploading/downloading.
- sources:
  - [1] https://doodrive.com/faq
