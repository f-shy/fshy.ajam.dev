# FEX.NET

> fex.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fex/ | JSON https://fshy.ajam.dev/api/v1/entity/fex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FEX.NET

- `storage/fex-net` | qualifies-with-caveat | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:14.808Z (live) | stale on 2026-11-25
- url https://fex.net
- free tier: You can share up to 50 GB worth of files without registration. | unit: GB | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: unverified: the home page states a 10 GB maximum file size only inside the 7-day trial block, not for anonymous shares | source: [1] | note: not stated
- retention: Storage capacity 50 gb for 7 days | days: 7 | source: [1] | note: not stated
- egress: No egress meter documented on the free transfer path; paid plans sell storage volume. | metered: no
- identity: anonymous
- interface: unknown
- limits note: 50 GB total per unregistered share. Paid storage ladder: 16 GB, 64 GB, 128 GB, 512 GB, 1 TB, 2 TB, 3 TB, 6 TB, 9 TB. Retention for anonymous shares not stated numerically on the read pages.
- interface detail: wrapper-only
- tooling: Web plus desktop/mobile clients; no documented API on the pages read.
- composes with: 50 GB per anonymous share x unlimited shares, but retention is time-boxed, so it chains as transit only.
- reliability: Russian-market host; the 50 GB is a per-share envelope rather than a quota, so it cannot accumulate. Pricing page renders as a bare ladder without terms.
- notes: the same as the free tier
- evidence note: the cited page was read on 2026-11-09
- evidence:
  - [1] 2026-10-21: 'You can share up to 50 GB worth of files without registration'
  - [2] 2026-10-21: storage ladder '16 GB / 64 GB / 128 GB / 512 GB / 1 TB / 2 TB / 3 TB / 6 TB / 9 TB'
  - [1] 2026-11-09: files up to a 50 GB share can be sent without registration | capture: sha256:a7ada2aaa00867de438e0333d24676dba668a3fdd6caf61ce2f3a46705cf0a2e | quote: You can share up to 50 GB worth of files without registration.
  - [1] 2026-11-09: the trial block gives 50 GB for 7 days with a 10 GB maximum file size | capture: sha256:a7ada2aaa00867de438e0333d24676dba668a3fdd6caf61ce2f3a46705cf0a2e | quote: - Free storage 7 days - Storage capacity 50 gb for 7 days - Maximum file size: 10 GB
- sources:
  - [1] https://fex.net/
  - [2] https://fex.net/pricing
