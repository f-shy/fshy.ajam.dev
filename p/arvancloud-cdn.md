# arvancloud free cdn

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arvancloud-cdn/ | JSON https://fshy.ajam.dev/api/v1/entity/arvancloud-cdn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## arvancloud free cdn (iran)

- `storage/arvancloud-free-cdn` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:55.372Z (live) | stale on 2026-12-04
- url https://lowendtalk.com/discussion/181171/another-free-cdn-provider
- free tier: Unlimited Traffic on the free CDN (Basic Plan / Free), subject to a fair-use policy. Arvancloud's own catalogue also lists object storage and traffic free. The former monthly traffic figure is no longer stated on the first-party free-tier page. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the cited report states no per-object size cap | source: [1] | note: not applicable
- retention: stated-absent: the cited report states no retention period for stored bytes | source: [1]
- egress: Free 100GB of traffic per month, with an unlimited number of requests, per the cited report. | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the cited report describes a CDN service with page rules and firewall rules and states no storage client interface
- tooling: not documented
- composes with: stated-absent: the cited report states no way to chain the CDN into a byte store; it describes traffic and page/firewall rules
- reliability: Free CDN tier is 100 GB/month of traffic, per a LowEndTalk report and their own catalogue entries. A third of Gcore's free slice and with far worse latency outside the region. Also a genuin.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free CDN tier is 100 GB/month of traffic, per a LowEndTalk report and their own catalogue entries — a third of Gcore's free slice and with far worse latency outside the region. Also a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free CDN tier is 100 GB/month of traffic, per a LowEndTalk report and their own catalogue entries — a third of Gcore's free slice and with far worse latency outside the region. Also a…
  - [2] 2026-10-21: cited as the basis of the rejection: Free CDN tier is 100 GB/month of traffic, per a LowEndTalk report and their own catalogue entries — a third of Gcore's free slice and with far worse latency outside the region. Also a genuin
  - [3] 2026-10-21: cited as the basis of the rejection: Free CDN tier is 100 GB/month of traffic, per a LowEndTalk report and their own catalogue entries — a third of Gcore's free slice and with far worse latency outside the region. Also a genuin
  - [4] 2026-11-19: the first-party free-tier page states unlimited traffic for the free CDN | capture: sha256:67e889db0a3c12b4be4d206c5e4baccb917beeecd1579880e4c60bbfb5385f76 | quote: Content Delivery NetworkUnlimited Traffic
  - [1] 2026-11-19: the report describes a CDN plan with DDoS protection and names no storage API | capture: sha256:6bd62ea35e0076f1ceb2ffd558002dcc583394d8ecb80fecc06fb65dfc27d148 | quote: Protection against DDoS attacks
  - [1] 2026-11-19: the report states a monthly traffic figure and no retention term | capture: sha256:6bd62ea35e0076f1ceb2ffd558002dcc583394d8ecb80fecc06fb65dfc27d148 | quote: Free 100GB of traffic per monthUnlimited number of requests
  - [1] 2026-11-19: the report describes CDN page rules and states no byte-store chaining | capture: sha256:6bd62ea35e0076f1ceb2ffd558002dcc583394d8ecb80fecc06fb65dfc27d148 | quote: 5 page rule
- sources:
  - [1] https://lowendtalk.com/discussion/181171/another-free-cdn-provider
  - [2] https://www.arvancloud.ir/en/products/cdn
  - [3] https://www.arvancloud.com/
  - [4] https://www.arvancloud.ir/en/pricing/free
