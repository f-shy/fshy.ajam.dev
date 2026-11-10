# Send Anywhere

> send-anywhere.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/send-anywhere/ | JSON https://fshy.ajam.dev/api/v1/entity/send-anywhere.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Send Anywhere

- `storage/send-anywhere` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://send-anywhere.com
- free tier: Free: 1:1 real-time transfer up to 50 GB; LINK creation capped at 10 GB. Lite $5.99/mo raises download data to 200 GB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 10 GB | bytes: 10000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: download-data metered on the recipient side (that is what the paid 'Download data' allowance buys). | metered: yes
- identity: institution
- interface: unknown
- limits:
  - per-object-cap (binding): per-object-cap: 10 GB [1]
- limits note: Per-object-cap: 10 GB stored link / 50 GB real-time. Retention: expires, and expired links are unrecoverable. pull-count: 'download data' is a metered allowance. This is the actual binding constraint on free, and exhausting it blocks further downloads from your own links.
- interface detail: none
- tooling: The Open API Service was RETIRED — support article 'End of support for Open API Service (26.3.31)'. No SDK path remains.
- composes with: The 50 GB figure is real-time device-to-device, not stored. Stored links are 10 GB and die on expiry with no recovery ('all files are deleted from the server once a link expires').
- reliability: Dead API and metered read path.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free: 1:1 real-time transfer up to 50 GB; LINK creation capped at 10 GB. Lite $5.99/mo raises download data to 200 GB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free: '1:1 real-time file transfer up to 50GB', 'Link creation up to 10GB'
  - [2] 2026-10-21: 'all files are deleted from the server once a link expires. After this point, they cannot be retrieved'
  - [3] 2026-10-21: policy change moving free users to a link-download allowance
- sources:
  - [1] https://send-anywhere.com/pricing
  - [2] https://support.send-anywhere.com/hc/en-us/articles/360003085053
  - [3] https://support.send-anywhere.com/hc/en-us/articles/16479573128473
