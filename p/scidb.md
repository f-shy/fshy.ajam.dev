# Science Data

> scidb.cn | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scidb/ | JSON https://fshy.ajam.dev/api/v1/entity/scidb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Science Data Bank (ScienceDB, Chinese Academy of Sciences / CNIC)

- `storage/science-data-bank` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.scidb.cn/en
- free tier: Allowance is 1 TB per dataset and 2,000 files per dataset with no published per-user or per-account cap. The 1 TB limit is a soft threshold requiring administrator coordination for larger submissions. Data packages bundle multiple datasets under one published record. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free public HTTPS download; no egress accounting in any policy page read. | metered: no
- identity: email | detail: email
- interface: s3, rest
- limits:
  - write-gated (binding): Review gate before publication [1]
- limits note: Review gate before publication; upload UI is the practical path (no public write API found for bulk); 2,000-file soft cap per dataset.
- interface detail: rest
- tooling: Web upload plus an Open API and OAI-PMH (listed in the help centre nav). No S3 backend exposed, so bulk automation is upload-by-UI or the Open API.
- composes with: Unlimited datasets x 1 TB each is the stated model; data packages then group them. This is the one Chinese academic repository that needs no +86 phone, no Alipay and no real-name verification - registration accepts username/password, GitHub, ORCID or WeChat, and only the first two are needed.
- reliability: Operated by CNIC with Springer Nature recommended repository status. Single-stream network throughput outside mainland China is unmeasured.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'if a single dataset contains more than 2,000 files or exceeds 1 TB in size, file upload functionality will be restricted... contact the ScienceDB official email'
  - [2] 2026-10-21: registration 'using the username and password you created during registration, or through third-party authentication such as CAS email/CSD account, GitHub account, ORCID and WeChat account'
  - [3] 2026-10-21: comparative table: ScienceDB 'no limit on data volume, users can upload datasets of any size' vs Zenodo 50 GB
- sources:
  - [1] https://www.scidb.cn/en/faq
  - [2] https://www.scidb.cn/en/help
  - [3] http://agbigdata.aiijournal.com/EN/Y2025/V7/I2/193

## ScienceDB (Science Data Bank, CAS / CNIC)

- `storage/sciencedb-re-verified-write-path` | qualifies-with-caveat | evidence reported | binding write-gated | category research-data-repository
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.scidb.cn/en
- free tier: No data-volume limit. A 2025 peer-reviewed comparison of Zenodo and ScienceDB in Journal of Agricultural Big Data states it plainly: for ScienceDB the 数据大小 row reads '没有数据量的限制，用户可以上传任意大小的数据集' (no limit on data volume; users may upload datasets of any size), against Zenodo's 'max 50 GB, can be raised to 200 GB in one step'. Datasets above 2,000 files or above 1 TB are merely flagged 'restricted' pending an email. A negotiable ceiling, not a hard one. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, anonymous for public datasets. DOI resolution works (302 to the dataset page). | metered: no
- identity: email | detail: email
- interface: ftp
- limits:
  - write-gated (binding): reviewed comparison of Zenodo and ScienceDB in Journal of Agricultural Big Data states i [1]
  - write-gated (binding): review' (形式审核) of upload completeness, accessibility and the data-availability stateme [1]
- limits note: Write-gated by 'formal review' (形式审核) of upload completeness, accessibility and the data-availability statement. Light-touch but still a human queue. Every dataset must have a subject category from the PRC GB/T 13745-2009 classification and at least three keywords. Metadata is mandatory and detailed (data generation procedure, temporal/spatial scope, per-file description). Some submission flows route through a CAS email or CSD account, which for the foreign client means using the GitHub/ORCID button rather than the native form.
- interface detail: web + ftp
- tooling: Explicitly two upload paths: '浏览器在线上传和FTP客户端在线上传'. Browser and FTP client. FTP is the one that matters at TB scale and is unusual among research repositories. There is also an Open API and OAI-PMH listed in the help centre. Login accepts a native account or third-party GitHub / ORCID / CAS / WeChat. And the English help page lists GitHub explicitly, which is the route that avoids Chinese identity requirements entirely.
- composes with: Unlimited datasets per account with no per-user aggregate cap, so capacity is datasets × a negotiable per-dataset ceiling. FTP ingest means an unattended rclone or lftp job.
- reliability: Public JSON endpoints differ from Zenodo conventions. Specific API download paths returned HTTP 404 on 2026-10-21 while dataset web pages resolved normally. Following DOI redirects (`/detail?dataSetId=...`) provides the standard path to download assets.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: opened: Table 1 row 数据大小, Zenodo '最多50 GB，可以一次性增加配额至200 GB' vs ScienceDB '没有数据量的限制，用户可以上传任意大小的数据集'; row 数据提交方式 for ScienceDB '浏览器在线上传和FTP客户端在线上传'; row 登录方式 'ScienceDB平台提供的登录界面；第三方账号，如中国科技云、Github、ORCID、Google账号等'. This is an independent 2025 academic comparison, not vendor copy.
  - [2] 2026-10-21: opened: registration via native account or 'third-party authentication such as CAS email/CSD account, GitHub account, ORCID and WeChat account'; four-step flow metadata -> review -> publish.
  - [3] 2026-10-21: PROBED: curl -qsS -o /dev/null -w '%{http_code}' -> 302 with redirect to https://www.scidb.cn/detail?dataSetId=3ac806eb277c4fecb37a55d472b1e82f. DOI routing is live.
  - withheld 2026-10-21: PROBED: that detail page read returns the real record — title, 'Published on 2026-10-21', CSTR/DOI, PACKAGE type, abstract, keywords. A dataset published this week is retrievable, so the platform is active.
  - withheld 2026-10-21: PROBED (negative, recorded honestly): /api/v1/dataset/detail?doi=… -> HTTP 404, 9 bytes; /api/download/<doi> -> 404, 9 bytes; /api/download?dataSetId=…&fileId=1 -> 404, 9 bytes. The guessed API paths do not exist. Trust HTTP 200 only after a hash, and here even the status was wrong.
- sources:
  - [1] http://agbigdata.aiijournal.com/EN/Y2025/V7/I2/193
  - [2] https://www.scidb.cn/en/help
  - [3] https://doi.org/10.57760/sciencedb.0142q
