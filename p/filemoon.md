# filemoon

> filemoon.sx | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filemoon/ | JSON https://fshy.ajam.dev/api/v1/entity/filemoon.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## filemoon

- `storage/filemoon` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:30.231Z (live) | stale on 2026-12-04
- url https://filemoon.sx/
- free tier: None reachable: Reachable (200) but the landing page offers only paid-tier marketing ('Storage 2.4 TB', RAID storage, $45/10k views). 2.4 TB is a paid-plan figure, not free, and there is no free anonymous. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Reachable (200) but the landing page offers only paid-tier marketing ('Storage 2.4 TB', RAID storage, $45/10k views) — 2.4 TB is a paid-plan figure, not free, and there is no free anonymous
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Reachable (200) but the landing page offers only paid-tier marketing ('Storage 2.4 TB', RAID storage, $45/10k views) — 2.4 TB is a paid-plan figure, not free, and there is no free anonymous
  - [1] 2026-11-19: the landing page is paid-tier marketing with a 2.4 TB storage figure and no free anonymous tier | capture: sha256:af39d92dffe82500325f9451237435c306238bbf17d5a78e18aa78628b6e9709 | quote: 26 global locations · RAID 1+0 storage · Payouts up to $45 per 10k views
  - [1] 2026-11-19: the sign-up is account-based; the page does not state which identifier registration requires | capture: sha256:af39d92dffe82500325f9451237435c306238bbf17d5a78e18aa78628b6e9709 | quote: [Log in](https://filemoon.sx/login)[Sign up](https://filemoon.sx/register)
- sources:
  - [1] https://filemoon.sx/

## filemoon.sx

- `storage/filemoon-sx` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:37.564Z (live) | stale on 2026-12-04
- url https://filemoon.sx/
- free tier: none reachable: filemoon.sx is a video-hosting and monetization service (the 'Byse' frontend). It accepts browser, remote-URL and FTP uploads across 12 video formats and exposes a REST API for accounts, but it is a video host, not a general file dump. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The first-party site is a video host ('Byse') with browser, remote-URL and FTP upload, 26-location delivery and an account REST API; it has no general-purpose arbitrary-file storage surface.
- notes: filemoon.sx is a video-hosting and monetization service, not a general file dump.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Video-hosting shell, not a general file dump: the page is 1605 bytes of 'Byse Frontend' JS that only activates on /e/ embed paths. No upload API and no file storage surface for arbitrary…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Video-hosting shell, not a general file dump: the page is 1605 bytes of 'Byse Frontend' JS that only activates on /e/ embed paths. No upload API and no file storage surface for arbitrary…
  - [1] 2026-11-19: the first-party page still presents filemoon.sx as a video-hosting service, not a general file dump | capture: sha256:af39d92dffe82500325f9451237435c306238bbf17d5a78e18aa78628b6e9709 | quote: Video hosting, delivery and monetization
  - [1] 2026-11-19: the first-party page describes a video-hosting upload and streaming workflow | capture: sha256:af39d92dffe82500325f9451237435c306238bbf17d5a78e18aa78628b6e9709 | quote: Upload from your browser, a remote link, or FTP. We encode every file, stream it from 26 locations worldwide, and help you earn from ads and referrals.
  - [1] 2026-11-19: the first-party page lists a REST API as a feature of the video-hosting service | capture: sha256:af39d92dffe82500325f9451237435c306238bbf17d5a78e18aa78628b6e9709 | quote: Full REST API
  - [1] 2026-11-19: the first-party page describes the service as video hosting | capture: sha256:af39d92dffe82500325f9451237435c306238bbf17d5a78e18aa78628b6e9709 | quote: Video hosting, delivery and monetization
- sources:
  - [1] https://filemoon.sx/
