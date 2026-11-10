# Katfile

> katfile.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/katfile/ | JSON https://fshy.ajam.dev/api/v1/entity/katfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Katfile

- `storage/katfile` | fails-quota | evidence reported | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://katfile.com
- free tier: No free storage quota published; premium advertises 'Download files up to 200 GB' and bandwidth blocks up to 18 TB. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free downloads are the usual XFileSharing throttled path; premium sells bandwidth blocks, so egress is the product. | metered: no
- identity: card
- interface: unknown
- limits note: Premium: 'Download files up to 200 GB', 90-day plan = 18 TB total bandwidth, $64.99. Free: no published storage or per-file number.
- interface detail: wrapper-only
- tooling: Standard XFileSharing API surface (op=... query paths); JDownloader-supported.
- composes with: Nothing free to multiply. The headline number (200 GB) is a download ceiling on a paid plan, not a per-file upload cap.
- reliability: The site canonicalises katfile.com to katfile.co between requests, so links must tolerate the redirect. VPN connections are explicitly unsupported for download, which breaks IP-rotation strategies.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: No free storage quota published; premium advertises 'Download files up to 200 GB' and bandwidth blocks up to 18 TB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Download files up to 200 GB', '90 Days ... 18 TB total bandwidth'
  - [2] 2026-10-21: 'How much storage do free accounts get?' is not answered; only generic hosting text
  - [2] 2026-10-21: 'Be aware that VPN connections for download is not supported'
- sources:
  - [1] https://katfile.co/?op=payments
  - [2] https://katfile.co/faq.html
