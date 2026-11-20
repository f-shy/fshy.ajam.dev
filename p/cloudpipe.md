# CloudPipe

> cloudpipe.app | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudpipe/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudpipe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudPipe

- `debrid/cloudpipe` | fails-quota | evidence documented | binding per-object-cap | category cloud download manager, torrent to Google Drive | tier free
- needs card no, phone unknown, ID no, institution no | verified 2026-10-23T03:15:33.000Z (live) | stale on 2026-11-23
- url https://cloudpipe.app/pricing
- price USD 0
- free tier: 'Free $0/month ... 5 jobs / day ... 3GB max file size ... Standard download speed ... 6hr server storage (no storage cap) ... 1 download at a time'. Home page adds 'No credit card required for free plan'. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The job counter is the only byte-bearing free counter that is also a daily one. The 450 GB in the ladder is 5 jobs x 3 GB x 30 days, which requires every job to be a distinct 3 GB file.
- per-object cap: '3GB max file size' on the free plan, '10GB max file size' on Basic and 'Unlimited file size' on Pro. | bytes: 3000000000 | source: [1] | note: The page says max file, not max job. Whether a multi-file torrent summing above 3 GB is refused, or whether each file inside it is checked, is not stated.
- retention: '6hr server storage (no storage cap)' on free; 'We delete our copy immediately' once the file lands in the destination cloud drive | source: [1]
- egress: not metered by bytes at any tier; 'No Storage Limits - We use your cloud storage. Download as much as your storage can handle without extra fees.' | metered: no | free allowance: 5 jobs/day, 3 GB each | source: [2]
- identity: email | detail: 'No credit card required for free plan'; the destination is a Google Drive account connected by OAuth after signup. A Google account is itself the identity gate, and Google may ask for a phone number at creation.
- interface: rest, cli
- limits:
  - request-rate: 5 jobs a day on the free plan; 20 on Basic; unlimited on Pro [1]
  - per-object-cap (binding): 3 GB max file on free [1]
  - pull-count: 1 download at a time on free [1]
  - retention-clamped: 6 hours of server storage on free [1]
  - request-rate: 5 jobs per day [2]
  - per-object-cap (binding): 3 GB per file on free [2]
  - retention-clamped: 6 hours of server storage [2]
- limits note: The binding constraint on the 450 GB is not CloudPipe at all: it is whether a 15 GB free Google Drive can be emptied 30 times in a month without the OAuth app's read-only-write permission getting in the way.
- binding note: 3 GB per file is 7.2x too small for a 20 GiB object, so the object fails before the daily count is reached.
- interface detail: web dashboard that authorises against the account's Google Drive; no documented public API on the free plan
- tooling: browser dashboard plus a Drive OAuth grant; the Drive side is then reachable by rclone
- composes with: The largest step in the ladder and the only one that stages through a free Google Drive of 15 GB, so the 450 GB is a monthly flow rather than a monthly store.
- reliability: files are on CloudPipe's servers for 6 hours on free and then gone; one download at a time; the Drive permission is read-only for existing files, so deletion must go through Drive, not through CloudPipe.
- notes: Every number in the ladder's CloudPipe row is confirmed. Two caveats the arithmetic hides: '3GB max file' is a file cap that the ladder converts into a per-job cap, and the 450 GB needs the Drive emptied between jobs because free Drive holds 15 GB. If the cap is per file inside a multi-file torrent, 450 GB is an undercount; if it is per job, it stands. The page does not say which. The cheapest paid price in the sector, but the free 3 GB cap and the 6-hour server window mean it cannot host the 20 GiB case even on the paid plan unless the paid cap is larger, which the vendor does not state.
- evidence note: Both the pricing and home pages were read. No job was run, so the Drive churn is arithmetic, not measurement.
- extras:
  - job_to_file_assumption: unstated by the vendor
  - ladder_gb_month: 450
  - drive_free_gb: 15
  - destination: user's own cloud drive
- evidence:
  - [1] 2026-10-23: 'Free $0/month', '5 jobs / day', '3GB max file size', '6hr server storage (no storage cap)', '1 download at a time'
  - [2] 2026-10-23: 'No credit card required for free plan', 'No Storage Limits - We use your cloud storage', 'We delete our copy immediately', and the FAQ sentence 'You connect your Drive after signing up'
  - [2] 2026-10-23: 'Free $0 - 5 jobs/day, 3GB max file, 6hr server storage, 1 download at a time, No credit card required'; paid '$2.99 /mo'; 'We delete our copy immediately'
  - [3] 2026-10-23: a torrent-to-cloud destination page exists, so the target cloud is interchangeable
- sources:
  - [1] https://cloudpipe.app/pricing
  - [2] https://cloudpipe.app/
  - [3] https://cloudpipe.app/features/torrent-to-mega
