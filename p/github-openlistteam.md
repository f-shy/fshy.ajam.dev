# 中国电信魔盘 mopan

> github.com | Storage, Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-openlistteam/ | JSON https://fshy.ajam.dev/api/v1/entity/github-openlistteam.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 中国电信魔盘 mopan (mopan)

- `storage/mopan` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/OpenListTeam/OpenList/blob/main/drivers/mopan/meta.go
- free tier: None reachable: Has a dedicated OpenList driver (`mopan`, reverse-engineered, with an explicit provider warning 'This network disk may store your password in clear text'), so it is technically mountable. B. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Has a dedicated OpenList driver (`mopan`, reverse-engineered, with an explicit provider warning 'This network disk may store your password in clear text'), so it is technically mountable…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Has a dedicated OpenList driver (`mopan`, reverse-engineered, with an explicit provider warning 'This network disk may store your password in clear text'), so it is technically mountable…
  - [2] 2026-10-21: cited as the basis of the rejection: Has a dedicated OpenList driver (`mopan`, reverse-engineered, with an explicit provider warning 'This network disk may store your password in clear text'), so it is technically mountable — b
- sources:
  - [1] https://github.com/OpenListTeam/OpenList/blob/main/drivers/mopan/meta.go
  - [2] https://eyun.baidu.com/content/169088/

## OpenList (OpenListTeam/OpenList)

- `netdisk-pan/openlist` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category bridge
- needs card no, phone no, ID no, institution no | verified 2026-11-02T09:58:36.718Z (live) | stale on 2026-11-24
- url https://github.com/OpenListTeam/OpenList
- free tier: free software, no allowance stated: https://github.com/OpenListTeam/OpenList is AGPL-3.0 software the user runs; it states there are no paid plans and prints no quota, unit or price | unit: none | metered on: none | read on: 2026-11-02 | source: [1]
- per-object cap: no cap of its own; the cap is the mounted upstream's | source: [1]
- retention: as long as the operator keeps the process and the upstream alive | source: [1]
- egress: unmetered by the software; the egress is whatever the upstream provider and any CDN in front charge | metered: no | source: [1]
- identity: anonymous | detail: the operator installs it; a reader needs no account on the bridge itself
- interface: rest, webdav, s3, ftp, sftp
- limits:
  - write-gated (binding): the write gate is CanWriteContent (bit 3) OR a per-path meta override, evaluated in server/middlewares/fsup.go [2]
- binding note: The bridge itself is not the constraint; what it can do is entirely set by which upstream it mounts and whether that upstream grants a write.
- tooling: a single Go binary; REST under /api/*, WebDAV at /dav, an S3-compatible gateway, FTP and SFTP; the rclone alist backend works against it
- composes with: the bridge layer of the whole topic: mount a pooled tenant or a pan account, serve it over REST and WebDAV, put a CDN in front
- reliability: A community fork of AList, created in June 2025 after the AList project was sold and its ownership, docs and community were rewritten. The fork is the maintained one; AList v3 builds still run on many public instances and still work.
- notes: The one piece of this topic that can be owned outright. The source is explicit that fs/list's write field is CanWrite, a per-user exclusion-list negation, while the upload gate is CanWriteContent(bit 3) OR a per-path meta; that distinction is why a host can report write:true and refuse every PUT, and why the one writable instance in the population reports write_content_bypass:true and permission 256 with no bit 3.
- self hosted: yes
- extras:
  - access_mode: self-hosted-bridge
  - language: Go
  - license: AGPL-3.0
  - stars: 25183
  - last_push: 2026-10-21T17:00:56Z
  - aliases: AList / OpenList — the most-used multi-storage aggregator (50.3k / 25.2k stars); alist / OpenList — the layer that works around a missing provider client; AList / OpenList; AList / OpenList — the most-used multi-storage aggregator
  - aggregator_note: This record is the single home for both spellings of the aggregator, so the name the completeness audit called unindexed resolves here.
- evidence:
  - [1] 2026-10-22: the repository describes itself as 'A new AList Fork to Anti Trust Crisis', 25,183 stars, last push 2026-10-21
  - [3] 2026-10-22: the write gate is: if !user.CanWriteContent() && !common.CanWriteContentBypassUserPerms(parentMeta, parentPath) then deny, then a second check common.CanWrite(user, parentMeta, parentPath)
  - [4] 2026-10-22: the fs/list response carries Write: common.CanWrite(user, meta, reqPath) and WriteContentBypass: common.CanWriteContentBypassUserPerms(meta, reqPath); these are two different predicates and only the second mirrors the upload gate
  - [5] 2026-10-22: the permission bitmask is documented in the struct comment: bit 3 is mkdir and upload, bit 8 is WebDAV read, bit 9 is WebDAV write
  - [6] 2026-10-22: the AList project was reported sold in June 2025 and OpenList was created as a replacement that removes the original developer's private API links
  - [1] 2026-10-30: OpenList has no paid plan and no metered allowance; the software is free to run | capture: sha256:a3a61e1281c815782fe05a2c8c2d57687f09990055360a1c0db3fbfe9c780446 | quote: There are currently no paid plans or commercial deployments, and the use of existing features does not involve any costs.
  - [3] 2026-11-02: the upload middleware answers 403 permission denied unless the user holds the write-content permission or a per-path meta override applies, so a write gate stands in front of every upload | capture: sha256:40be4bd2faba0f824529c234a82168630b454053b53c810779a797144f1dff3f | quote: if !user.CanWriteContent() && !common.CanWriteContentBypassUserPerms(parentMeta, parentPath) { common.ErrorResp(c, errs.PermissionDenied, 403)
  - [1] 2026-11-02: the README states no paid plans and no cost for existing features; its text prints no quota, unit or price | capture: sha256:a3a61e1281c815782fe05a2c8c2d57687f09990055360a1c0db3fbfe9c780446 | quote: There are currently no paid plans or commercial deployments, and the use of existing features does not involve any costs.
  - [5] 2026-11-02: bit 3 of the user permission bitmask is the right to mkdir and upload, the permission that the upload gate tests first | capture: sha256:5bc44ed0d99484342dce21ffc09ef83e501fd0fb054a5780f7e5d98ef688c69b | quote: // 3: can mkdir and upload
- sources:
  - [1] https://github.com/OpenListTeam/OpenList
  - [2] https://github.com/OpenListTeam/OpenList/blob/main/server/middlewares/fsup.go
  - [3] https://raw.githubusercontent.com/OpenListTeam/OpenList/main/server/middlewares/fsup.go
  - [4] https://raw.githubusercontent.com/OpenListTeam/OpenList/main/server/handles/fsread.go
  - [5] https://raw.githubusercontent.com/OpenListTeam/OpenList/main/internal/model/user.go
  - [6] https://finance.sina.com.cn/tech/digi/2025-06-16/doc-infahqye9515437.shtml
