# Rollin Host Drive empresarial

> rollinhost.com.br | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rollinhost/ | JSON https://fshy.ajam.dev/api/v1/entity/rollinhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rollin Host Drive empresarial / Backup & Storage (Brazil) — flat per-TB, no request or traffic charge, Pix/boleto

- `storage/rollin-host-drive-empresarial-backup-storage-flat-per-tb` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category storage-vps-managed-nas
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.rollinhost.com.br/backup-na-nuvem
- price $7.56/TB/mo at 10 TB ($75.63/mo); $7.96/TB/mo at 5 TB ($39.80/mo); $15.91/TB/mo at 1 TB ($15.91/mo). At 20 TB: $7.56/TB/mo if the 10 TB plan can be bought twice ($151.26/mo). BRL at 0.199082 USD/BRL. Egress $0. | parsed USD 7.56/TB-mo
- free tier: Topázio 1 TB R$79.90/mo; Esmeralda 5 TB R$199.90/mo; Diamante 10 TB R$379.90/mo. Monthly cycle, no lock-in («sem fidelidade»), Brazilian NF-e invoice, ceiling 10 TB then sales contact. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: FREE, stated twice and unambiguously: «Preço fixo por capacidade. Sem cobrança por upload, download ou requisição» (fixed price per capacity. No charge for upload, download or request) and repeated per plan as «Sem cobrança de tráfego». The FAQ confirms it is not S3-compatible: «não é object storage S3-compatible». | metered: no
- identity: card | detail: card
- interface: webdav, sftp, rsync, smb, rclone
- limits:
  - per-ip-shaping (binding): 1 TiB/day [1]
- limits note: Datacenter is located in Brazil, resulting in international latency for outside traffic. Interfaces do not include S3 compatibility or presigned URLs. Product is designed for backup and archive rather than high-concurrency distribution.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: webdav + sftp + samba
- tooling: SFTP, Samba/CIFS, WebDAV; explicitly documented as working with BorgBackup, Restic, rsync, rclone and Duplicati. Mounts as a network drive on Windows and macOS. Automatic read-only snapshots for ransomware rollback.
- composes with: Three fixed capacities; 20 TB would need sales contact (they say «Precisa de mais de 10 TB? Fale com a gente»). Two 10 TB plans = 20 TB at the same rate if they will sell it.
- reliability: Small Brazilian host; the product is explicitly positioned as backup storage («Não é uma suíte de documentos colaborativos: é o arquivo central da empresa»). No independent benchmark exists. Payment friction is low for a Brazilian buyer (Pix, boleto, card in 12×) and moderate for a foreign one (card only, BRL FX).
- notes: the same as the free tier
- extras:
  - price_verbatim: $7.56/TB/mo at 10 TB ($75.63/mo); $7.96/TB/mo at 5 TB ($39.80/mo); $15.91/TB/mo at 1 TB ($15.91/mo). At 20 TB: $7.56/TB/mo if the 10 TB plan can be bought twice ($151.26/mo). BRL at 0.199082 USD/BRL. Egress $0.
- evidence:
  - [1] 2026-10-21: «Topázio 1 TB R$ 79,90/mês … Esmeralda 5 TB R$ 199,90/mês … Diamante 10 TB R$ 379,90/mês», each with «Sem cobrança de tráfego»
  - withheld 2026-10-21: same page — «Preço fixo por capacidade — sem cobrança por upload, download ou requisição»; «Faturamento em real (Pix, boleto, cartão), NF-e brasileira»
  - [2] 2026-10-21: «1 TB (R$ 79,90/mês) a 10 TB (R$ 379,90/mês), com preço fixo pela capacidade e sem cobrança por upload, download ou requisição … acessada como unidade de rede (WebDAV ou Samba), por SFTP ou por ferramentas como rclone»
- sources:
  - [1] https://www.rollinhost.com.br/backup-na-nuvem
  - [2] https://www.rollinhost.com.br/drive-empresarial
