# bangumi.tv AList/OpenList index

> bangumi.tv | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bangumi/ | JSON https://fshy.ajam.dev/api/v1/entity/bangumi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bangumi.tv AList/OpenList index (the live community list)

- `netdisk-pan/bangumi-alist-index` | qualifies-with-caveat | evidence measured | binding retention-clamped | category index-list
- needs card no, phone no, ID no, institution no | verified 2026-10-30T17:26:52.225Z (live) | stale on 2026-11-21
- url https://bangumi.tv/m/topic/group/472627
- free tier: not stated: https://bangumi.tv/m/topic/group/472627 is a public forum post listing AList/OpenList sites, with WebDAV guest logins for many of them, and prints no allowance, quota or price | unit: none | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: not applicable; it is a list | source: [1]
- retention: maintained; the post read on 2026-10-22 is the current revision and a maintainer prunes dead entries | source: [1]
- egress: no egress; it is a page | metered: no | source: [1]
- identity: anonymous | detail: an open forum page
- interface: rest
- limits:
  - retention-clamped (binding): a maintainer prunes dead entries, so a survivor count from this list measures the maintainer's diligence and not the population's survival [1]
- binding note: The list is current by construction, so it is the right discovery input and the wrong decay measurement; the constraint is on what the list can prove.
- tooling: A flat forum thread at /m/topic/... accessible without authentication. HTTP GET returns the full post content directly.
- composes with: the highest-yield discovery input measured, and the one whose curation hides churn rather than showing it
- reliability: 20 of the 28 real hostnames on the page answered with a mount list, which is selection and not longevity: a pruned list cannot show you what died.
- notes: The one live index worth automating against. It also carries the WebDAV credential next to each site, which is how the WebDAV read path was testable without an account. Of 31 hostname-shaped strings extracted from it, 3 are not instances (ssl, www, www.kdocs.cn), leaving 28, of which 26 answered HTTP and 20 listed mounts.
- extras:
  - access_mode: index
  - listed_hosts: 28
  - answered_http: 26
  - listed_mounts: 20
  - carries_webdav_credentials: yes
- evidence:
  - [1] 2026-10-22: the post lists public AList/OpenList sites with a WebDAV credential beside most of them, and its own preamble states that AList was sold and recommends OpenList instead
  - probe:https://bangumi.tv/m/topic/group/472627 2026-10-22: 31 hostname-shaped strings were extracted, of which 3 are not instances (ssl, www, www.kdocs.cn), leaving 28; 26 answered HTTP and 20 returned a non-empty mount list
  - probe:https://bangumi.tv/m/topic/group/472627 2026-10-30: the page answered 200 to a request with no session and is a forum post titled as a summary of public AList/OpenList sites; it carries no quota, unit or price | capture: sha256:d25a0db1b35385cfa0951078d1a1f1f0694124ad92f0c9c68a737777bd499450 | quote: 公开 AList/OpenList 在线网盘资源站点汇总
- sources:
  - [1] https://bangumi.tv/m/topic/group/472627
