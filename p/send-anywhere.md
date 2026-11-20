# Send Anywhere

> send-anywhere.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/send-anywhere/ | JSON https://fshy.ajam.dev/api/v1/entity/send-anywhere.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Send Anywhere

- `storage/send-anywhere` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:25.779Z (live) | stale on 2026-12-04
- url https://send-anywhere.com
- free tier: Free: 1:1 real-time transfer up to 50 GB; LINK creation capped at 10 GB. Lite $5.99/mo raises download data to 200 GB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 10 GB | bytes: 10000000000 | source: [1] | note: not stated
- retention: Free stored links expire; after expiry all files are deleted from the server and cannot be retrieved. | source: [1] | note: not stated
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
  - [2] 2026-11-19: files in expired links are deleted from the server and are unrecoverable | capture: sha256:59a70a0687ea096e7c1b347176b462fa1b571f0659848283ba740186c4b2bc80 | quote: all files are deleted from the server once a link expires. After this point, they cannot be retrieved any longer.
  - [1] 2026-11-19: the free plan offers 50 GB real-time transfer and 10 GB link creation | capture: sha256:bf5d665167a485a774ca221519d928fe4e179f3435a930f9c65d7e26cadee4c5 | quote: 1:1 real-time file transfer up to 50GB Link creation up to 10GB
- sources:
  - [1] https://send-anywhere.com/pricing
  - [2] https://support.send-anywhere.com/hc/en-us/articles/360003085053
  - [3] https://support.send-anywhere.com/hc/en-us/articles/16479573128473
