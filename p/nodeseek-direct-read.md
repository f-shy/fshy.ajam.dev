# nodeseek direct read

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nodeseek-direct-read/ | JSON https://fshy.ajam.dev/api/v1/entity/nodeseek-direct-read.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nodeseek direct read (nodeseek.com)

- `storage/nodeseek-direct-read` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:54.246Z (live) | stale on 2026-12-04
- url https://www.nodeseek.com/post-382621-1
- free tier: None reachable: Cloudflare/geo wall plus a hard IPv6 block: every fetch redirects to warning.nodeseek.com/ipv6-is-disabled and returns a 29-word apology page with HTTP 200. The exact 'status-code theatre'. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Unpinned reads redirect to warning.nodeseek.com/ipv6-is-disabled (a 29-word notice at HTTP 200), but pinning the read provider firecrawl reaches the real forum post.
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Cloudflare/geo wall plus a hard IPv6 block: every fetch redirects to warning.nodeseek.com/ipv6-is-disabled and returns a 29-word apology page with HTTP 200 — the exact 'status-code theatre'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cloudflare/geo wall plus a hard IPv6 block: every fetch redirects to warning.nodeseek.com/ipv6-is-disabled and returns a 29-word apology page with HTTP 200 — the exact 'status-code theatre'
  - [2] 2026-10-21: cited as the basis of the rejection: Cloudflare/geo wall plus a hard IPv6 block: every fetch redirects to warning.nodeseek.com/ipv6-is-disabled and returns a 29-word apology page with HTTP 200 — the exact 'status-code theatre'
  - [1] 2026-11-19: a pinned first-party read returns the real forum post, so the IPv6 notice is not a hard block on the content | capture: sha256:f7f3920280f02fdee4513228ab85bdcbeeb34bc7f18eefb4e5ebc40f74e9549e | quote: # [有没有性价比高的T级大盘鸡推荐](https://www.nodeseek.com/post-382621-1)
  - [1] 2026-11-19: the default read still answers the IPv6 notice page rather than the forum post | capture: sha256:fff92e661d0dbbbc36fe46d8ee51b27d2c082eaca77eae695b104c5f8605e774 | quote: The forum has closed IPv6 access, please refresh the local DNS cache.
  - [1] 2026-11-19: the pinned provider read reached the actual forum thread | capture: sha256:f7f3920280f02fdee4513228ab85bdcbeeb34bc7f18eefb4e5ebc40f74e9549e | quote: # [有没有性价比高的T级大盘鸡推荐](https://www.nodeseek.com/post-382621-1)
- sources:
  - [1] https://www.nodeseek.com/post-382621-1
  - [2] https://warning.nodeseek.com/ipv6-is-disabled
