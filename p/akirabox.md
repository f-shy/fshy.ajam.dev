# AkiraBox

> akirabox.to | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/akirabox/ | JSON https://fshy.ajam.dev/api/v1/entity/akirabox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AkiraBox

- `storage/akirabox` | fails-egress | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://akirabox.to
- free tier: unlimited storage advertised; 5 GB/file anonymous, 20 GB/file with a free account | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB/file | bytes: 5000000000 | source: [1] | note: not stated
- retention: 5 GB/file anonymous (7 days after last download), 20 GB/file free account (30 days after last download) | days: 7 | source: [1] | note: not stated
- egress: unmetered, but free downloads carry an explicit human-verification step | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 5 GB/file [1]
  - per-object-cap (binding): 20 GB/file [1]
- limits note: 5 GB/file anonymous (7 days after last download), 20 GB/file free account (30 days after last download). Premium removes the human check and the size limit; premium is granted only to partner sites with 200k+ visits/month, not sold.
- interface detail: rest
- tooling: documented REST API; GET /api/files?url={fileUrl} for status. Upload-via-API docs are Premium-only ('Docs for the upload steps are Premium only').
- composes with: free accounts are free and email-only; 20 GB/file x N accounts. Storage advertised as unlimited per account.
- reliability: Its own FAQ says premium 'removes the ads and the "verify you are human" check on downloads'. I.e. free downloads require human verification by design. That alone disqualifies it for automated fetch. It also ships a download manager because 'browser downloads stall on big files'.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: unlimited storage advertised; 5 GB/file anonymous, 20 GB/file with a free account
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: POST https://akirabox.com/upload -> 404 'Server action not found.' (Next.js server action, needs browser-issued action id). Upload path NOT scriptable from curl.
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 'Docs for the upload steps are Premium only'
  - withheld 2026-10-21: probe: POST /upload -> 404 'Server action not found.'
- sources:
  - [1] https://akirabox.to/
  - [2] https://akirabox.to/developers
