# TransferXL

> transferxl.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transferxl/ | JSON https://fshy.ajam.dev/api/v1/entity/transferxl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TransferXL

- `storage/transferxl` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:29.929Z (live) | stale on 2026-12-04
- url https://www.transferxl.com/
- free tier: Free with account: 5 GB max transfer size, 10 GB daily / 300 GB monthly transfer allowance. Paid plans reach 100–200 GB per transfer. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 5 GB | bytes: 5000000000 | source: [1] | note: not stated
- retention: 1 week retention on the Free plan (Pro 6 weeks, Enterprise 3 months). | source: [1] | note: not stated
- egress: Free but counted against 10 GB/day and 300 GB/month; not unmetered. | metered: no | free allowance: 300 GB per month
- identity: anonymous
- interface: unknown
- limits:
  - per-ip-shaping: 10 GB/day [1]
  - per-object-cap (binding): per-object-cap 5 GB [1]
- limits note: per-object-cap 5 GB free; request-rate/quota 10 GB/day and 300 GB/month; retention not stated on the page (unverified).
- interface detail: web-only
- tooling: none found
- composes with: 5 GB/transfer x unlimited transfers, bounded at 300 GB/month per account. This is a transfer allowance, not storage, so multiplying accounts multiplies throughput not capacity.
- reliability: Free tier is ad-supported and capped at 300 GB/month of movement; no storage product on the free plan.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free with account: 5 GB max transfer size, 10 GB daily / 300 GB monthly transfer allowance. Paid plans reach 100–200 GB per transfer.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'the basic features (File transfers up to 5 GB) will be free forever', 'Free with account - 5 GB max. transfer size - 10 GB daily/300 GB monthly', 'Send files up to 200 GB' (paid)
  - [1] 2026-11-19: the Free plan still states 5 GB per transfer, 10 GB/day and 300 GB/month, and now also 1 week retention | capture: sha256:0c500c54330307bbf885c48b072be2bcf9ffa1a8d0d1aeec06d40850972cb431 | quote: - 5 GB max. transfer size - Up to 10 transfers per day - 10 GB daily/300 GB monthly - 1 week retention - End-to-end encryption
  - [1] 2026-11-19: the Free plan now states a one-week retention period | capture: sha256:0c500c54330307bbf885c48b072be2bcf9ffa1a8d0d1aeec06d40850972cb431 | quote: - 1 week retention
  - [1] 2026-11-19: the basic free features remain free forever with transfers up to 5 GB | capture: sha256:0c500c54330307bbf885c48b072be2bcf9ffa1a8d0d1aeec06d40850972cb431 | quote: TransferXL is and will remain totally free to use. So the basic features (File transfers up to 5 GB) will be free forever!
  - [1] 2026-11-19: the Free plan table states 1 week retention | capture: sha256:0c500c54330307bbf885c48b072be2bcf9ffa1a8d0d1aeec06d40850972cb431 | quote: - 1 week retention
- sources:
  - [1] https://www.transferxl.com/
