# osdn

> osdn.net | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/osdn/ | JSON https://fshy.ajam.dev/api/v1/entity/osdn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## osdn (osdn.net / osdn.jp)

- `storage/osdn` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:05.886Z (live) | stale on 2026-12-04
- url https://osdn.net/
- free tier: none reachable: Service is inactive. Domain osdn.net no longer resolves with DNS NXDOMAIN. Domain osdn.jp resolves to a consumer affiliate content site. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: `osdn.net` no longer resolves (DNS NXDOMAIN from two separate attempts); `osdn.jp` resolves but is now a Japanese consumer-affiliate content farm…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: `osdn.net` no longer resolves (DNS NXDOMAIN from two separate attempts); `osdn.jp` resolves but is now a Japanese consumer-affiliate content farm 'ネットマ
  - [2] 2026-10-21: `osdn.net` no longer resolves (DNS NXDOMAIN from two separate attempts); `osdn.jp` resolves but is now a Japanese consumer-affiliate content farm 'ネットマ
  - [2] 2026-11-19: osdn.jp now serves Japanese consumer affiliate content, not the code forge | capture: sha256:f336d989c28c24f3af8819eacce927133c63b840c70d47e63e89e85eda5d5082 | quote: 置くだけで使用できるWiFiホームルーターおすすめ8選！メリットとデメリットや適切な契約先の選び方
  - probe:osdn.net 2026-11-19: a DNS-over-HTTPS answer on 2026-11-19 reports no reachable authority for osdn.net, so the host does not resolve | capture: sha256:e0d6790cb00656bf70b1a0d7463bf470e0570c22c6835519f567fe81736f764d | quote: EDE(22): No Reachable Authority at delegation osdn.net.
- sources:
  - [1] https://osdn.net/
  - [2] https://osdn.jp/

## osdn (osdn.net)

- `storage/osdn-2` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:05.886Z (inherited) | stale on 2026-12-04
- url https://web.archive.org/web/202506/osdn.net/docs/FileRelease_Guide
- free tier: None reachable: The SourceForge-Japan equivalent. Would have been the obvious sibling candidate. Is gone. DNS does not resolve (probe: Could not resolve host: osdn.net), read/fetch both 530, and the last. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The SourceForge-Japan equivalent — would have been the obvious sibling candidate — is gone. DNS does not resolve (probe: Could not resolve host: osdn.net), read/fetch both 530, and the last
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: The SourceForge-Japan equivalent — would have been the obvious sibling candidate — is gone. DNS does not resolve (probe: Could not resolve host: osdn.net), read/fetch both 530, and the last
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The SourceForge-Japan equivalent — would have been the obvious sibling candidate — is gone. DNS does not resolve (probe: Could not resolve host: osdn.net), read/fetch both 530, and the last
  - probe:https://osdn.net/ 2026-11-19: a probe on 2026-11-19 could not reach osdn.net (transport error, no status) | capture: sha256:56efe5a9f4ae4047b9f5df33412c96fec7c3d11de0d060187163f7f6d2603242 | quote: "status": null
- sources:
  - [1] https://web.archive.org/web/202506/osdn.net/docs/FileRelease_Guide
