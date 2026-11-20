# kuhehe.github.io AList site index

> kuhehe.github.io | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kuhehe-github-io/ | JSON https://fshy.ajam.dev/api/v1/entity/kuhehe-github-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## kuhehe.github.io AList site index (the 2024 cohort source)

- `netdisk-pan/kuhehe-alist-index` | qualifies-with-caveat | evidence measured | binding retention-clamped | category index-list
- needs card no, phone no, ID no, institution no | verified 2026-10-30T17:26:52.225Z (live) | stale on 2026-11-21
- url https://kuhehe.github.io/20240120224502/
- free tier: not stated: https://kuhehe.github.io/20240120224502/ is a static HTML post listing AList sites and prints no allowance, quota or price | unit: none | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: not applicable; it is a list, not a service | source: [1]
- retention: the page is still served; the repository was last committed 2025-06-17 and the newest section is dated 23 March, so it stopped tracking new hosts well before that | source: [2]
- egress: no egress; it is HTML | metered: no | source: [1]
- identity: anonymous | detail: an open HTML page
- interface: rest
- limits:
  - retention-clamped (binding): the page is edited in place rather than republished, so its permalink date is not its content date [2]
- binding note: The bias that matters is not the page dying but the page changing: hosts were added to a permalink after its date, so a survival rate computed from the URL's date overstates survival.
- tooling: plain HTML with one bare https:// host per line, so an extraction is a regex and not a parser
- composes with: the only dated cohort available, and therefore the only way this topic can state a half-life at all
- reliability: The permalink 20240120224502 reads as a publish date and is not one: the file at that path was committed 36 times, the first surviving revision is 2024-02-29 and the last is 2025-06-17.
- notes: The commit history says otherwise: 36 commits touch this path, the earliest the API returned is 2024-02-29 and the last is 2025-06-17, and the page carries a section headed 3月23日新发现的alist资源站. The 144-host cohort as probed therefore mixes hosts first listed in 2024-01 with hosts added as late as mid-2025.
- extras:
  - access_mode: index
  - commits_touching_path: 36
  - earliest_revision: 2024-02-29T14:59:37Z
  - latest_revision: 2025-06-17T14:45:50Z
  - cohort_size: 144
  - cohort_size_at_first_revision: 126
- evidence:
  - [1] 2026-10-22: the page is served, the title is '分享一些基于Alist搭建的资源站合集', the author is 酷小呵, the meta published date is 2024-01-20T14:45:02Z, and the body begins '不定时更新中' with a section headed '3月23日新发现的alist资源站'
  - [2] 2026-10-22: 36 commits touch this path; the oldest returned is 2024-02-29T14:59:37Z and the newest is 2025-06-17T14:45:50Z, so the permalink is not a frozen snapshot
  - probe:https://api.github.com/repos/kuhehe/kuhehe.github.io/contents/20240120224502/index.html?ref=5f5947f0 2026-10-22: the 2024-02-29 revision contains 126 instance hostnames after noise removal, of which 11 still list mounts, giving 8.7% survival over 2.65 years
  - probe:https://kuhehe.github.io/20240120224502/ 2026-10-30: the page answered 200 to a request with no session and is a post collecting AList-built resource sites; it carries no quota, unit or price | capture: sha256:c3799c94d4c63a6e75ec341132c5101a9613226e4c3401921075569542d8a01f | quote: 分享一些基于Alist搭建的资源站合集
- sources:
  - [1] https://kuhehe.github.io/20240120224502/
  - [2] https://api.github.com/repos/kuhehe/kuhehe.github.io/commits?path=20240120224502/index.html&per_page=100
