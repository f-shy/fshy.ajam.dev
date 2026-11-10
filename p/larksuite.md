# Lark

> larksuite.com | Storage, Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/larksuite/ | JSON https://fshy.ajam.dev/api/v1/entity/larksuite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lark (Feishu) Starter - free plan

- `storage/lark-starter-free-plan` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.larksuite.com
- free tier: 100 GB total storage per organization on Starter (Free); 250 MB single-file limit for Docs uploads on Starter | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 250 MB per file | bytes: 250000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Downloads served from Lark CDN (ByteDance edge) at no metered charge; download via OpenAPI media download returns a signed URL, no per-GB line item anywhere in the plan table | metered: yes
- identity: email
- interface: rest, rclone, cli
- limits:
  - per-object-cap (binding): 250 MB per file [1]
- limits note: 250 MB per file for Docs on Starter (vs 50 GB on Pro); upload_all hard-caps at 20 MB by design, must use multipart; 5 QPS on upload_all; 4 MB fixed chunk size on multipart; upload transaction ID valid 1 day for resume
- interface detail: rest
- tooling: Official OpenAPI v3 drive endpoints (upload_all for <=20MB, multipart upload of 4MB chunks above that) + first-party CLI larksuite/cli (17,762 stars, pushed 2026-10-21) with `lark-cli drive +upload`; no rclone backend
- composes with: 100 GB x N free organizations. Starter is self-serve per organization and the quota is per-org, not per-user, so N disposable orgs = N x 100 GB. Paid Basic (5 TB) shows the ceiling is only billing, not architecture.
- reliability: Rate limits are explicit (5 QPS on single upload) and multipart is resumable, but Starter orgs that lapse back from a paid plan are force-collapsed to Starter member and storage caps - data above 100 GB becomes unwritable, not deleted.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: table row: 'Total storage space | 100 GB | 5 TB | 15 TB | 15 TB + 30 GB x purchased seats'; 'Single file upload limit for Docs | 250 MB'
  - [2] 2026-10-21: 'please do not use this interface to upload files larger than 20MB... use the multipart upload interface', supports 5QPS
  - [3] 2026-10-21: 
- sources:
  - [1] https://www.larksuite.com/hc/en-US/articles/497171699982-overview-of-lark-plans
  - [2] https://open.larksuite.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/upload_all
  - [3] https://open.larksuite.com/open-apis/auth/v3/tenant_access_token/internal

## Lark / 飞书 Drive via multi-tenant app credentials (the FeiSync pattern)

- `netdisk-pan/lark-drive-via-multi-tenant-app-credentials` | qualifies-with-caveat | evidence reported | binding per-object-cap | category platform storage reached through app credentials
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://open.larksuite.com/app
- free tier: 100 GB per Lark tenant. '任意扩容，只要添加 App ID 和 App Secret 就可以免费获得100G空间，单文件250M，简单说就是容量上限取决于你的号数量' | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 250 MB per file | bytes: 250000000 | source: [1]
- retention: While the tenant persists. No retention clock published | source: [2]
- egress: Unmetered in practice; there is no egress line item on the free tier | metered: no | source: [1]
- identity: email | detail: a distinct email address or phone number per tenant. Lark has historically required an overseas IP to register outside the mainland, which is a feature here
- interface: rest
- limits:
  - per-object-cap (binding): 250 MB per file [1]
  - request-rate: apps inside one tenant share that tenant's 100 GB, so a second app is not a second quota [1]
- tooling: FeiSync v1.0.0 by fish2018, Tauri and Rust with a Vue front end, presented on linux.do on 2025-12-28: multi-tenant routing, one-way or two-way cron sync, resumable transfer and an open HTTP API. The underlying API is the Lark Drive open platform v1 at /drive/v1/files
- composes with: This is the Google service-account pattern reimplemented for Lark: create N free tenants, register a custom app in each, and FeiSync load-balances writes across them for 100 GB times N in one flat namespace. 250 MB per file is the binding number, not the bytes
- reliability: Two constraints bite: 250 MB per file caps the cold-archive case hard, and app-permission changes break the wrapper. Tenant creation needs a distinct identity each time
- notes: The most directly applicable of the app-credential patterns, because tenancy is free and self-service. The 250 MB file cap is what makes it a shard target rather than a store, and that is a job for a chunker rather than a blocker.
- extras:
  - access_mode: registration-gated
  - wrapper: FeiSync v1.0.0 (fish2018)
  - quota_per_tenant_bytes_derived: 107374182400
  - per_file_cap_bytes_derived: 250000000
  - overseas_ip_required: yes
  - aliases: Lark / 飞书 Drive via multi-tenant app credentials (FeiSync pattern)
- evidence:
  - [1] 2026-10-21: '免费无限扩容，每个账号免费扩容100G，单文件250M' and '不能是同一个企业的不同应用，会共享100G'
  - [3] 2026-10-21: 'larksuite所谓飞书海外版，必须要海外IP才能注册'; '海外ip，会成功'
  - [4] 2026-10-21: 'Lark 免费用户就有自定域名邮箱、100 GB 存储'
- sources:
  - [1] https://linux.do/t/topic/1371150
  - [2] https://open.larksuite.com/app
  - [3] https://linux.do/t/topic/360439
  - [4] https://linux.do/t/topic/588707
