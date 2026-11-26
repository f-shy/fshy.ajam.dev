# bangumi.tv AList/OpenList index

> bangumi.tv | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bangumi/ | JSON https://fshy.ajam.dev/api/v1/entity/bangumi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bangumi.tv AList/OpenList index (the live community list)

- `netdisk-pan/bangumi-alist-index` | qualifies-with-caveat | evidence measured | binding retention-clamped | category index-list
- needs card no, phone no, ID no, institution no | verified 2026-11-25T13:26:29.022Z (live) | stale on 2026-12-17
- url https://bangumi.tv/m/topic/group/472627
- free tier: unverified: the post prints no allowance, quota or price | unit: none | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: not applicable; it is a list | source: [1]
- retention: maintained; the post read on 2026-10-22 is the current revision and a maintainer prunes dead entries | source: [1]
- egress: no egress; it is a page | metered: no | source: [1]
- identity: anonymous | detail: an open forum page
- interface: rest
- limits:
  - retention-clamped (binding): a maintainer prunes dead entries, so a survivor count from this list measures the maintainer's diligence and not the population's survival [1]
- binding note: The list is current by construction, so it is the right discovery input and the wrong decay measurement; the constraint is on what the list can prove.
- tooling: A flat forum thread at /m/topic/... accessible without authentication. HTTP GET returns the full post content directly.
- composes with: unverified: no first-party capture measures discovery yield or churn hiding
- reliability: 20 of the 28 real hostnames on the page answered with a mount list, which is selection and not longevity: a pruned list cannot show you what died.
- notes: unverified: the host, HTTP-answering and mount counts are in no first-party capture
- extras:
  - access_mode: index
  - listed_hosts: unverified: no first-party capture states a host count
  - answered_http: unverified: no first-party capture states an HTTP-answering host count
  - listed_mounts: unverified: no first-party capture states a mount-listing host count
  - carries_webdav_credentials: yes
- evidence:
  - [1] 2026-10-22: the post lists public AList/OpenList sites with a WebDAV credential beside most of them, and its own preamble states that AList was sold and recommends OpenList instead
  - probe:https://bangumi.tv/m/topic/group/472627 2026-10-22: 31 hostname-shaped strings were extracted, of which 3 are not instances (ssl, www, www.kdocs.cn), leaving 28; 26 answered HTTP and 20 returned a non-empty mount list
  - probe:https://bangumi.tv/m/topic/group/472627 2026-10-30: the page answered 200 to a request with no session and is a forum post titled as a summary of public AList/OpenList sites; it carries no quota, unit or price | capture: sha256:d25a0db1b35385cfa0951078d1a1f1f0694124ad92f0c9c68a737777bd499450 | quote: 公开 AList/OpenList 在线网盘资源站点汇总
  - probe:https://bangumi.tv/m/topic/group/472627 2026-11-25: the forum page answered HTTP 200 when re-read | capture: sha256:ac73f724c09d8262673e29548786be190a0c2a46a2b5610ea95e776db0271917 | quote: "status": 200
  - probe:https://bangumi.tv/m/topic/group/472627 2026-11-25: the forum page answered HTTP 200; no host count is stated | capture: sha256:ac73f724c09d8262673e29548786be190a0c2a46a2b5610ea95e776db0271917 | quote: "status": 200
  - probe:https://bangumi.tv/m/topic/group/472627 2026-11-25: the forum page answered HTTP 200; no HTTP-answering count is stated | capture: sha256:ac73f724c09d8262673e29548786be190a0c2a46a2b5610ea95e776db0271917 | quote: "status": 200
  - probe:https://bangumi.tv/m/topic/group/472627 2026-11-25: the forum page answered HTTP 200; no mount count is stated | capture: sha256:ac73f724c09d8262673e29548786be190a0c2a46a2b5610ea95e776db0271917 | quote: "status": 200
  - [1] 2026-11-25: the post's preamble states the AList sale and the OpenList recommendation | capture: sha256:80e7fa5813fab0d5da17707daf1c4c6ab078c7666ad7c4eec77e859adf7f4494 | quote: 另外 AList 原项目已被转卖给流氓公司，若考虑部署推荐改用类似 [OpenList](https://github.com/OpenListTeam/OpenList) 等由社区维护的分支
  - probe:https://bangumi.tv/m/topic/group/472627 2026-11-25: the forum page is still served | capture: sha256:ac73f724c09d8262673e29548786be190a0c2a46a2b5610ea95e776db0271917 | quote: "status": 200
- sources:
  - [1] https://bangumi.tv/m/topic/group/472627
