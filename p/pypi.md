# PyPI

> pypi.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pypi/ | JSON https://fshy.ajam.dev/api/v1/entity/pypi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PyPI (Python Package Index)

- `storage/pypi` | qualifies | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pypi.org
- free tier: 100 MB per file, 10 GB per project. Both are defaults, both are raisable by filing a GitHub issue. Unlimited number of projects. Verified in warehouse source: MAX_FILESIZE = 100 * ONE_MIB, MAX_PROJECT_SIZE = 10 * ONE_GIB, UPLOAD_LIMIT_CAP = 1 GiB. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: | Deletion is permanent and irreversible ('cannot be undone without administrative intervention') | source: [1] | note: not stated
- egress: Free and unmetered. files.pythonhosted.org probe: Server: cloudflare, Cache-Control: 'max-age=365000000, immutable, public', Access-Control-Allow-Origin: *, no auth. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 100 MB per file [1]
  - per-object-cap (binding): 100 MB/file [1]
- limits note: 100 MB/file, 10 GB/project (both raisable; 40 GB grants are routine for large projects). 20 project creations/hour/user, 10/day/organization, 40/hour/IP (warehouse config.py defaults). Files cannot be uploaded to a release older than 14 days (MAXIMUM_AGE_FOR_NEW_UPLOADS). Deleting a file frees quota; yanking does NOT.
- interface detail: rest
- tooling: Legacy upload API POST /legacy/ (twine), JSON API GET /pypi/<name>/json for metadata, direct file GET from files.pythonhosted.org. Orgs/teams exist. Named wrapper class: pypi/* tools, twine, and warehouse itself. No rclone backend.
- composes with: UNBOUNDED via projects: unlimited projects x 10 GB each (raisable to 40 GB. Uv and ruff were both granted 40 GB). 10 TiB = 1,024 projects at default 10 GB. Project creation is rate limited to 20/hour and 40/hour per IP, which is the binding constraint, not bytes.
- reliability: Deletion is permanent and irreversible ('cannot be undone without administrative intervention'). Releases are append-only in practice but files can be deleted to free project quota, so unlike npm this is not immutable-by-design. Treat it as stable-but-deletable. Quota enforcement is a hard 400 at upload, so budget against the 10 GB project figure.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'The current default limits are 100.0 MB for individual files and 10.0 GB for the entire project'; 'we can sometimes increase your limit'
  - [2] 2026-10-21: MAX_FILESIZE = 100 * ONE_MIB; MAX_PROJECT_SIZE = 10 * ONE_GIB; UPLOAD_LIMIT_CAP = ONE_GIB; MAXIMUM_AGE_FOR_NEW_UPLOADS = 14 days
  - [3] 2026-10-21: PROJECT_CREATE_USER_RATELIMIT_STRING default '20 per hour'; PROJECT_CREATE_IP '40 per hour'; PROJECT_CREATE_ORGANIZATION '10 per day'
  - [4] 2026-10-21: 'Project Limit Request: uv - 40 GB' (grant path is real and used)
  - [5] 2026-10-21: probe: GET -> 200, info.version 1.17.0, 2 urls (JSON API works anonymously)
  - [6] 2026-10-21: probe: GET -> 200, Content-Length: 34041, Cache-Control: 'max-age=365000000, immutable, public', Server: cloudflare
- sources:
  - [1] https://docs.pypi.org/project-management/storage-limits/
  - [2] https://github.com/pypa/warehouse/blob/main/warehouse/constants.py
  - [3] https://github.com/pypa/warehouse/blob/main/warehouse/config.py
  - [4] https://github.com/pypi/support/issues/4260
  - [5] https://pypi.org/pypi/six/json
  - [6] https://files.pythonhosted.org/packages/71/39/.../six-1.16.0.tar.gz
