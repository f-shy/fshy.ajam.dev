# Acast

> acast.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/acast/ | JSON https://fshy.ajam.dev/api/v1/entity/acast.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Acast — Starter (free) plan

- `storage/acast-starter-plan` | fails-quota | evidence documented | binding volume-quota | category media
- identity a placeholder: card and phone unknown | verified 2026-11-04T00:31:28.056Z (live) | stale on 2026-12-05
- url https://www.acast.com
- free tier: 1 show, 5 episodes on Free. 'unlimited episodes when you make your show available in Acast's advertising marketplace'. So free capacity is 5 episodes unless you opt into ad monetisation, in which case episodes are unlimited but storage is still bounded by the 150 MB file cap. | unit: objects | metered on: object-count | read on: 2026-10-21 | source: [1]
- per-object cap: 150 MB per episode file: Acast sets the internal limit to 150MB, in line with Apple's 150MB cellular download limit; MP3 and M4A only | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free distribution to all major platforms; no egress charge. Acast monetises via ads, not storage. | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): 5 episodes per show on Starter (free); unlimited episodes only when the show is available in Acast's advertising marketplace [1]
  - per-object-cap: 150 MB per episode file, MP3 or M4A only, re-encoded at 128kbps [2]
- limits note: 150 MB hard per-episode cap. 'Acast sets the internal limit to 150MB also', and going over produces an 'episode unavailable' error on listener devices because Apple caps cellular downloads at 150 MB. MP3 or M4A only (no WAV/FLAC).
- binding note: 5 episodes per show on the free Starter plan; lifting the episode count needs the advertising marketplace or a paid plan
- interface detail: wrapper-only
- tooling: Dashboard only; no public upload API.
- composes with: 5 episodes x 150 MB = 750 MB per free account in the honest reading; N accounts. Not interesting at scale.
- reliability: Re-encodes to 128 kbps: 'Acast will encode your uploaded files at 128kbps, which will not impair the perceived quality for your listeners.' Two independent caps (150 MB, 5 episodes) plus a 128k transcode make this the weakest of the majors.
- notes: Starter: Free, 1 show, 5 episodes ('Get unlimited episodes when you make your show available in Acast's advertising marketplace'). Paid: Essential $14.99 / Month with unlimited episodes (the page's Monthly or Yearly toggle state is not visible in the captured text).
- evidence note: The 2026-11-03 evidence rows read https://www.acast.com/en/pricing (episode count on Starter, unlimited only through the advertising marketplace, Essential price) and https://learn.acast.com/en/articles/ (which-audio-file-format-should-i-use-for-my-podcast) (150MB internal limit, re-encode of uploads). Every field that decides the verdict cites those captures; the identity requirement was not read.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 show, 5 episodes on Free — 'unlimited episodes when you make your show available in Acast's advertising marketplace'. So free capacity is 5 episodes unless you opt into ad monetisation, in which case episodes are unlimited but storage is still bounded by the 150 MB file cap.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Starter: 'Free', '1 Show', '5 Episodes', 'Get unlimited episodes when you make your show available in Acast's advertising marketplace'
  - [2] 2026-10-21: 'Acast will encode your uploaded files at 128kbps'; 'Acast sets the internal limit to 150MB also'; 'MP3 and M4A files are the only audio filetypes that are supported'
  - [1] 2026-11-03: the Starter plan includes 5 episodes, so the free allowance is counted in episodes | capture: sha256:ab74721c19c036332db0e5bc178d855abf1ae4cf6f6f71c16c46f08239e641a4 | quote: 5 Episodes
  - [1] 2026-11-03: episodes beyond 5 depend on the advertising marketplace, so the meter is the episode count | capture: sha256:ab74721c19c036332db0e5bc178d855abf1ae4cf6f6f71c16c46f08239e641a4 | quote: Get unlimited episodes when you make your show available in Acast's advertising marketplace.
  - [2] 2026-11-03: Acast enforces a 150MB internal limit per file | capture: sha256:d758bf96652fecb2b36217fd54238bc87c56a94ea2d327cd725f68f306b6bfb6 | quote: Acast sets the internal limit to 150MB also.
  - [1] 2026-11-03: Starter is limited to 5 episodes | capture: sha256:ab74721c19c036332db0e5bc178d855abf1ae4cf6f6f71c16c46f08239e641a4 | quote: 5 Episodes
  - [1] 2026-11-03: Essential, the cheapest paid plan, is listed at $14.99 per month with unlimited episodes | capture: sha256:ab74721c19c036332db0e5bc178d855abf1ae4cf6f6f71c16c46f08239e641a4 | quote: $14.99
  - [2] 2026-11-03: uploads are re-encoded at 128kbps | capture: sha256:d758bf96652fecb2b36217fd54238bc87c56a94ea2d327cd725f68f306b6bfb6 | quote: Acast will encode your uploaded files at 128kbps, which will not impair the perceived quality for your listeners.
  - [1] 2026-11-03: the Starter plan is free with 5 episodes and unlimited episodes only through the advertising marketplace | capture: sha256:ab74721c19c036332db0e5bc178d855abf1ae4cf6f6f71c16c46f08239e641a4 | quote: Get unlimited episodes when you make your show available in Acast's advertising marketplace.
  - [2] 2026-11-04: Acast enforces a 150MB internal limit per file | capture: sha256:d758bf96652fecb2b36217fd54238bc87c56a94ea2d327cd725f68f306b6bfb6 | quote: Acast sets the internal limit to 150MB also.
- sources:
  - [1] https://www.acast.com/en/pricing
  - [2] https://learn.acast.com/en/articles/3505536-which-audio-file-format-should-i-use-for-my-podcast
