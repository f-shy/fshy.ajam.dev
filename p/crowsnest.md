# hostens storage vps

> crowsnest.network | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crowsnest/ | JSON https://fshy.ajam.dev/api/v1/entity/crowsnest.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hostens storage vps

- `storage/hostens-storage-vps` | paid-only | evidence reported | binding request-rate | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:03:55.915Z (live) | stale on 2026-11-18
- url https://crowsnest.network/plan/hostens/storage-vps-large/
- price USD 21.00 per TB-month at Storage VPS Large (1 TB, USD 21.00 per month) | parsed USD 21/TB-mo
- free tier: none free; paid only: Storage VPS Large, 1 TB of storage at $21.00/mo (the 1 month term) | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: 8TB per month of bandwidth is listed for Storage VPS Large; overage handling is not specified | metered: no
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): disk I/O capped at 50 MB/s and 200 IOPS on storage servers since 4 May 2026 [2]
- binding note: disk I/O is capped at 50 MB/s and 200 IOPS on storage servers; at 50 MB/s a full 1 TB read takes about 5.6 hours, and the plan is 1 TB for USD 21.00 per month
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: since 4 May 2026 storage servers are capped at 50 MB/s and 200 IOPS; the 75 MB/s and 300 IOPS cap applies to KVM servers and containers, not storage servers
- notes: OpenVZ containers on 12x4TB RAID, priced at $21/mo for 1 TB = $21/TB. And since May 2026 all VPS are capped at 75 MB/s I/O and 300 IOPS. The I/O cap alone disqualifies it for a hot working.
- evidence note: the 2026-11-03 evidence rows read the third-party plan listing https://crowsnest.network/plan/hostens/storage-vps-large/ (price and bandwidth) and the vendor help article on help.hostens.com help article (the disk I/O cap); the price rests on a third-party page, and the vendor plan page https://www.hostens.com/vps-hosting/ was not captured
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: OpenVZ containers on 12x4TB RAID, priced at $21/mo for 1 TB = $21/TB — and since May 2026 all VPS are capped at 75 MB/s I/O and 300 IOPS. The I/O cap alone disqualifies it for a hot working
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: OpenVZ containers on 12x4TB RAID, priced at $21/mo for 1 TB = $21/TB — and since May 2026 all VPS are capped at 75 MB/s I/O and 300 IOPS. The I/O cap alone disqualifies it for a hot working
  - [2] 2026-10-21: cited as the basis of the rejection: OpenVZ containers on 12x4TB RAID, priced at $21/mo for 1 TB = $21/TB — and since May 2026 all VPS are capped at 75 MB/s I/O and 300 IOPS. The I/O cap alone disqualifies it for a hot working
  - [3] 2026-10-21: cited as the basis of the rejection: OpenVZ containers on 12x4TB RAID, priced at $21/mo for 1 TB = $21/TB — and since May 2026 all VPS are capped at 75 MB/s I/O and 300 IOPS. The I/O cap alone disqualifies it for a hot working
  - [1] 2026-11-03: Storage VPS Large costs USD 21.00 per month at the 1 month term, intro and renewal alike | capture: sha256:ff5c61c6e5519ee695ae8a1dcf6281b10a3f1ccbe38b81a195537221b57eeccb | quote: | 1 month | $21.00/mo | $21.00/mo | — | — |
  - [1] 2026-11-03: Storage VPS Large lists 8TB per month of bandwidth; the page lists overage handling as not specified | capture: sha256:ff5c61c6e5519ee695ae8a1dcf6281b10a3f1ccbe38b81a195537221b57eeccb | quote: Bandwidth8TB/mo
  - [2] 2026-11-03: storage servers carry a 50 MB/s and 200 IOPS disk limit | capture: sha256:372ff2189f0c8024b145f0fe7dc58cccc652f0335c6e6384669de6fab3d61671 | quote: For storage servers, the I/O speed limit is 50 MB/s, and the limit for operations per second (IOPS) is 200.
- sources:
  - [1] https://crowsnest.network/plan/hostens/storage-vps-large/
  - [2] https://help.hostens.com/en/articles/312057-
  - [3] https://www.hostens.com/vps-hosting/
