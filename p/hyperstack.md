# Hyperstack

> hyperstack.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hyperstack/ | JSON https://fshy.ajam.dev/api/v1/entity/hyperstack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hyperstack

- `compute/hyperstack` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:28.018Z (live) | stale on 2026-12-04
- url https://www.hyperstack.cloud/gpu-pricing
- free tier: no free tier: GPU and CPU capacity billed per minute. On-demand rates per hour as listed: NVIDIA H100 SXM $3.20, NVIDIA H100 NVLink $2.60, NVIDIA H100 $2.50, NVIDIA A100 SXM 80 GB $1.60, NVIDIA A100 NVLink 80 GB $1.40, NVIDIA A100 80 GB $1.35. Spot VM rates: NVIDIA H100 PCIe $2.00, NVIDIA A100 $1.08. Reservation rates start at $2.72 for an H100 SXM and $0.95 for an A100. The page lists an NVIDIA L40 at $1.00 but no L40S, RTX 4090 or L4, and states no minimum bill. Storage is about $0.10 a TB an hour; egress and ingress traffic are listed as free | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: the page's Other Services table lists egress and ingress traffic together as free | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): GPU and CPU capacity billed per minute, with per-hour rates on the page [1]
  - per-object-cap: storage is $0.000096774 a GB-hour, about $0.10 a TB-hour [1]
  - retention-clamped: attached volumes and Cloud-SSD storage bill separately from the GPU [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the GPU pricing page was read on 2026-10-22 and states per-minute billing with hourly rates. There is no free tier, so the verdict moves to paid-only and the storage rate is recorded because it is the number a large-volume reader needs
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: billed per minute; the page states no reap
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - burst_x: 1.0
  - ps.price: $0.000096774 a GB-hour, about $0.10 a TB-hour
  - ps.durability: attached volume or Cloud-SSD
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the volume exists
  - net.out: yes
  - net.in: yes
  - net.allowance: egress and ingress traffic are listed together as free
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'billed per minute' with 'Pricing Per Hour', '$0.000096774 per GB per hour (approximately $0.10 per TB per hour)' of storage and '0.00672043 per hour' on a GPU row, quoted
  - [1] 2026-11-03: the on-demand table lists the NVIDIA H100 SXM at $3.20 per hour; the table lists no L40S, RTX 4090 or L4 | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: NVIDIA H100 SXM 80 24 240 $3.20
  - [1] 2026-11-03: the pricing page was read on this date | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: NVIDIA H100 SXM 80 24 240 $3.20
  - [1] 2026-11-03: egress and ingress traffic are listed as free | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: Egress/Ingress traffic Free
  - [1] 2026-11-03: one row lists egress and ingress traffic as free, not two meters | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: Egress/Ingress traffic Free
  - [1] 2026-11-03: billing granularity is one minute; no minimum bill is stated | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: transparent and competitive pricing structure, billed per minute.
  - [1] 2026-11-03: the A100 80 GB on-demand rate is $1.35 per hour | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: NVIDIA A100 80 28 120 $1.35
  - [1] 2026-11-03: the A100 SXM 80 GB on-demand rate is $1.60 per hour | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: NVIDIA A100 SXM 80 24 120 $1.60
  - [1] 2026-11-03: the on-demand row named NVIDIA H100 is $2.50 per hour | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: NVIDIA H100 80 28 180 $2.50
  - [1] 2026-11-03: the Spot VM table lists the H100 PCIe at $2.00 per hour | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: NVIDIA H100 PCIe $2.00
  - [1] 2026-11-03: the Spot VM table lists the A100 at $1.08 per hour | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: NVIDIA A100 $1.08
  - [1] 2026-11-03: the page lists an L40, not an L40S, at $1.00 per hour on demand | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: NVIDIA L40 48 28 120 $1.00
  - [1] 2026-11-03: the pricing page lists the on-demand H100 SXM rate | capture: sha256:7717dfaa55436d5c162115dc710b5b04a934b3e6aa7117eb3cea12fca9352f6f | quote: NVIDIA H100 SXM 80 24 240 $3.20
- sources:
  - [1] https://www.hyperstack.cloud/gpu-pricing
