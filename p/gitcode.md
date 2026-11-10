# GitCode

> gitcode.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitcode/ | JSON https://fshy.ajam.dev/api/v1/entity/gitcode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GitCode (gitcode.com, CSDN) — Git/LFS/container quota

- `storage/gitcode-git-lfs-container-quota` | fails-quota | evidence reported | binding none | category registry
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gitcode.com
- free tier: No number published. GitCode documents that it meters four resources per user. Git Repository Storage (all branches + all history, excluding LFS), Container Usage (core-hours), Git LFS Storage (all LFS-tracked files, all versions), and Project Count. With alerts at 80% and 95% of 'the quota'. The quota values themselves are only visible in the logged-in console. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Presumably free for public repos (standard for code hosts) but not stated. LFS reads go through the GitCode CDN. | metered: no
- identity: email | detail: email + likely +86 phone (CSDN account).
- interface: rest, oci, git
- limits note: 10 MB web upload, ~100 MB single-file push limit (community-documented, not in official docs), LFS for anything larger. Quota numbers unpublished and enforced with 80%/95% warnings. Usage resets monthly (statistics are calendar-month based).
- interface detail: git
- tooling: git + git-lfs; a documented REST API (docs.gitcode.com/en/docs/repos); container registry. GitCode also mirrors ModelScope/HF repos, which is how most people touch it.
- composes with: Per-user quota, so N accounts. But the practical ceiling is the per-file limit, not the account total: community docs put the web uploader at 10 MB per file and the default push limit at 100 MB, with LFS as the only path above that.
- reliability: Quota is enforced by silent rejection at the 95% mark with only an email warning; because the numbers are hidden until you hit them, this is a poor host for a planned multi-TB load.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No number published. GitCode documents that it meters four resources per user — Git Repository Storage (all branches + all history, excluding LFS), Container Usage (core-hours), Git LFS Storage (all LFS-tracked files, all versions), and Project Count — with alerts at 80% and 95% of 'the quota'. The quota values themselves are only visible in the logged-in console.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: the four metered resource types and 'When resource usage reaches 80% of the quota, the system will send a reminder ... When it reaches 95%, a warning notification'
  - [2] 2026-10-21: third-party: '网页端上传文件时，单个文件最大不得超过 10MB ... GitCode 默认限制单文件大小上限 100MB'
- sources:
  - [1] https://docs.gitcode.com/en/docs/help/home/user_center/data_management/usage_and_storage
  - [2] https://blog.csdn.net/2401_83096323/article/details/160687305
