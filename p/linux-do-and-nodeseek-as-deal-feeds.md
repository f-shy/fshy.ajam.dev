# linux.do and nodeseek as deal feeds

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linux-do-and-nodeseek-as-deal-feeds/ | JSON https://fshy.ajam.dev/api/v1/entity/linux-do-and-nodeseek-as-deal-feeds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## linux.do and nodeseek as deal feeds

- `storage/linux-do-and-nodeseek-as-deal-feeds` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:14.723Z (live) | stale on 2026-12-04
- url https://linux.do/search.json?q=空间
- free tier: none reachable: BOTH ARE WRITE/READ-GATED FOR THIS PURPOSE. linux.do returns a Cloudflare challenge to direct search.json, and behind it demands login for search (firecrawl resolved it to /login… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Not applicable: a discussion forum that carries threads about storage offers; it stores no user bytes and states no egress allowance or price. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: reported: only https://linux.do/ was captured and quoted on 2026-11-03 (a discussion forum topic list that holds no user bytes); the search gate is not covered by a 2026-11-03 capture
- extras:
  - dead_end.failure_class: read-gated
  - dead_end.why: BOTH ARE WRITE/READ-GATED FOR THIS PURPOSE. linux.do returns a Cloudflare challenge to direct search.json, and behind it demands login for search (firecrawl resolved it to /login…
  - dead_end.retry_when: if the read path opens anonymously
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: BOTH ARE WRITE/READ-GATED FOR THIS PURPOSE. linux.do returns a Cloudflare challenge to direct search.json, and behind it demands login for search firecrawl resolved it to /login; individual
  - [2] 2026-10-21: cited as the basis of the rejection: BOTH ARE WRITE/READ-GATED FOR THIS PURPOSE. linux.do returns a Cloudflare challenge to direct search.json, and behind it demands login for search firecrawl resolved it to /login; individual
  - [3] 2026-10-21: cited as the basis of the rejection: BOTH ARE WRITE/READ-GATED FOR THIS PURPOSE. linux.do returns a Cloudflare challenge to direct search.json, and behind it demands login for search firecrawl resolved it to /login; individual
  - [4] 2026-11-03: the page is a discussion forum topic list, not a storage service | capture: sha256:294584a013e8a2887fd333df9dbe34dc2ffd0bebf2d77cc3d0f2710a012df138 | quote: All latest topics
  - [4] 2026-11-03: the vendor page was read and quoted on 2026-11-03: the page is a discussion forum topic list, not a storage service | capture: sha256:294584a013e8a2887fd333df9dbe34dc2ffd0bebf2d77cc3d0f2710a012df138 | quote: All latest topics
  - [4] 2026-11-19: the linux.do homepage is a discussion-forum topic list, not a storage service | capture: sha256:6f617b086b92739d598fbe09d392d0b45575d4618b8024337403be7358edffc6 | quote: # All latest topics
  - [2] 2026-11-19: nodeseek answers with a forum access notice and holds no storage offer | capture: sha256:fff92e661d0dbbbc36fe46d8ee51b27d2c082eaca77eae695b104c5f8605e774 | quote: The forum has closed IPv6 access, please refresh the local DNS cache.
  - [5] 2026-11-19: linux.do search.json is walled by a Cloudflare challenge (HTTP 403) on 2026-11-19 | capture: sha256:c6131434c8a035d86860c52871d719f1b3c11c8624d0d57ffeb8962fef9591c1 | quote: cf-mitigated: challenge
- sources:
  - [1] https://linux.do/search.json?q=空间
  - [2] https://www.nodeseek.com/
  - [3] https://linux.do/t/topic/1753000
  - [4] https://linux.do/
  - [5] https://linux.do/search.json?q=%E7%A9%BA%E9%97%B4
