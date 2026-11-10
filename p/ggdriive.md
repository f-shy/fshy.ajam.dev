# ggdriive.com

> ggdriive.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ggdriive/ | JSON https://fshy.ajam.dev/api/v1/entity/ggdriive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ggdriive.com

- `storage/ggdriive-com` | fails-quota | evidence inferred | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://ggdriive.com/
- free tier: 20 GB free; 'ILIMITADO PRO' marketed as unlimited (paid) | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: | Unverified and unaudited. An anonymous WebDAV 'unlimited' host is the exact profile of the lifetime-deal failures below. | source: [1] | note: not stated
- egress: Claims 'Almacenamiento, ancho de banda, subidas y descargas sin límites' (unlimited bandwidth, uploads and downloads) on the paid unlimited tier. | metered: no
- identity: anonymous
- interface: webdav, rclone
- limits note: Free tier is only 20 GB. Unlimited is a PAID plan. Spanish-language site; no published infrastructure or company details.
- interface detail: webdav
- tooling: WebDAV only (rclone's generic webdav backend). Surfaced on the rclone forum (2026-04-21) as 'unlimited storage, I already have many tb'; forum reply warns rclone cannot checksum-verify over WebDAV.
- composes with: Unknown/undocumented. No account-multiplication story verified; would need a signup to test.
- reliability: Unverified and unaudited anonymous WebDAV storage service claiming unlimited capacity without enterprise service level agreements.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 20 GB free; 'ILIMITADO PRO' marketed as unlimited (paid)
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Almacenamiento ILIMITADO REAL... Conecta con rclone'
  - [1] 2026-10-21: 'Free: 20 GB de almacenamiento'; 'ILIMITADO PRO: Almacenamiento ILIMITADO REAL' (paid tier, no price shown)
  - [3] 2026-10-21: user claims unlimited storage over WebDAV; replies note no checksums and 'not suitable for backups'
  - [4] 2026-10-21: probe: GET -> 530; https://dav.ggdriive.com/ -> 530; site root -> 200 (no discoverable DAV host)
- sources:
  - [1] https://ggdriive.com/pricing
  - [2] https://ggdriive.com/
  - [3] https://forum.rclone.org/t/unlimited-storage/53709
  - [4] https://webdav.ggdriive.com/
