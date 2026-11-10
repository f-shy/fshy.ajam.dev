# FileLu

> filelu.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filelu/ | JSON https://fshy.ajam.dev/api/v1/entity/filelu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileLu

- `storage/filelu` | fails-egress | evidence reported | binding per-object-cap | category cloud drive + S3 object storage
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://filelu.com/
- price $81/TB one-time at the 8 TB lifetime tier ($649) — amortised over 5 years that is $1.35/TB/mo; $56/TB one-time at 4 TB ($449)
- free tier: 1 GB free. Free accounts can upload 10 GB per file but only hold 1 GB total. Paid: S3-compatible 'FileLu S5', 1 PB scale. Lifetime promo: 1 TB $149, 2 TB $249, 4 TB $449, 8 TB $649. 1 TB monthly transfer per 1 TB of purchased storage. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 GB per file | bytes: 10000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No request or retrieval fees. '$0 request or retrieval fees' is stated on the homepage and repeated as 'No request fees' / 'Always free' for S5. Transfer quota is tied 1:1 to storage purchased (buy 1 TB, get 1 TB/month). | metered: yes | free allowance: 1 TB per month
- identity: email | detail: email
- interface: s3, rest, webdav, ftps, ftp, rsync, rclone, cli
- limits:
  - per-object-cap (binding): 10 GB per file [1]
  - per-object-cap (binding): 10 GB/file [1]
- limits note: per-object: 10 GB/file on free, no limit on premium. Transfer is 1:1 with storage purchased, which is the binding constraint at archive-restore time.
- interface detail: s3
- tooling: Very wide: S3 (S5), WebDAV, FTP/FTPS, Rsync, rclone, REST API. rclone has a native Tier-1 backend (read-only in the table, ModTime R). Explicitly named as compatible with AWS CLI, rclone, Restic, Kopia, Proxmox, Duplicacy, Duplicati, S3 Browser, FileBrowserGO, Synology Hyper Backup, s3cmd, Cyberduck, Mountain Duck.
- composes with: Purchased 8 TB lifetime plan at $649 supports Rsync and S3, serving as a backup target for tools like Duplicati, Kopia, and restic. Transfer is bound by a 1:1 transfer to storage capacity ratio.
- reliability: 146,000 users; lifetime promos move between $149 and $350 list, so the lifetime price is a channel promotion rather than a stable list price. Read-only rclone classification means rclone cannot write; S3/Rsync/WebDAV must carry writes.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 GB free. Free accounts can upload 10 GB per file but only hold 1 GB total. Paid: S3-compatible 'FileLu S5', 1 PB scale. Lifetime promo: 1 TB $149, 2 TB $249, 4 TB $449, 8 TB $649. 1 TB monthly transfer per 1 TB of purchased storage.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $81/TB one-time at the 8 TB lifetime tier ($649) — amortised over 5 years that is $1.35/TB/mo; $56/TB one-time at 4 TB ($449)
- evidence:
  - [1] 2026-10-21: '1 GB free to get started', '1 PB scalable storage', '$0 request or retrieval fees', 'FileLu WebDAV cloud drive access', 'FileLu S3 compatible object storage', 'FileLu Rsync server backup storage'
  - [2] 2026-10-21: 'Free users: 10GB per file. Premium users: no limit'; 'Your transfer quota is based on the storage you purchase. For example, if you purchase 1 TB of storage, you receive a 1 TB monthly transfer quota'
  - [3] 2026-10-21: S3-compatible; 'works with AWS CLI, Rclone, Restic, Kopia, Proxmox, Duplicacy, Duplicati, S3 Browser, FileBrowserGO, Synology Hyper Backup'
  - [4] 2026-10-21: '+20GB' earn-free-storage tasks (the only free path above 1 GB, still far short of 500 GB)
  - [5] 2026-10-21: lifetime: 1 TB $149, 2 TB $249, 4 TB $449, 8 TB $649
  - [6] 2026-10-21: native backend, Tier 1, ModTime R (read-oriented)
  - [7] 2026-10-21: PROBE PROPFIND — HTTP/1.1 401, 13 bytes, WWW-Authenticate: Basic realm="FileLu", X-FileLu-Origin: US-WebDAV-Proxy, Server-Timing cfCacheStatus DYNAMIC (live, CF-fronted)
  - [8] 2026-10-21: PROBE — DNS NXDOMAIN; the S5 endpoint hostname is not published on the pages read, so the S3 endpoint could not be confirmed
- sources:
  - [1] https://filelu.com/pricing/
  - [2] https://filelu.com/pages/faq/
  - [3] https://filelu.com/pages/s5-object-storage/
  - [4] https://filelu.com/pages/earn-free-storage/
  - [5] https://grabltd.com/products/filelu
  - [6] https://rclone.org/filelu/
  - [7] https://webdav.filelu.com/
  - [8] https://s5.filelu.com/
