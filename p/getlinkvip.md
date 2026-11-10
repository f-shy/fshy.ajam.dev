# GetLinkVip

> getlinkvip.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getlinkvip/ | JSON https://fshy.ajam.dev/api/v1/entity/getlinkvip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GetLinkVip

- `debrid/getlinkvip-net` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category multi-host premium link generator (Vietnamese: 14+ hosts, two-connection cap) | tier vip
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://getlinkvip.net/guide.html
- free tier: The guide describes a free tier and a VIP tier only through connection count: 'chỉnh số kết nối tối đa của IDM là 1 (đối với Free) và 2 (đối với Vip)'. No byte allowance and no price is published on the guide page. | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: Price is the missing fact in this record; the homepage advertises 'giá thấp hơn 3-5 lần so với mua từng tài khoản ở mỗi filehost' without a number.
- per-object cap: not stated | source: [1]
- retention: not applicable: a direct link is returned | source: [1]
- egress: Per-host daily bandwidth, deducted on a successful get: 'Đối với những host có giới hạn băng thông trong ngày ... sau get link thành công, băng thông của host đó sẽ bị trừ.' Re-getting a link to resume does not re-deduct. | metered: yes | free allowance: unstated | source: [1]
- identity: card | detail: Not documented on the pages read: the guide and homepage publish no payment page. Every other Vietnamese PLG among debrid providers takes either a card (LinksVIP) or domestic rails only (Getlink.vn), so this is unresolved rather than assumed. | country: Vietnam
- interface: rest
- limits:
  - per-ip-shaping (binding): maximum 2 simultaneous connections per machine on VIP (1 on free) [1]
  - volume-quota: per-host daily bandwidth, amount unpublished [1]
- limits note: 'Vì giới hạn tối đa mỗi máy chỉ được 2 kết nối để download' - the cap is per machine, which is why the guide tells users to queue downloads rather than parallelise.
- binding note: Two connections per machine caps throughput well below what a monthly transfer of 1 TiB needs unless each connection is fast; no byte figure is published to check against.
- interface detail: Web panel; the guide is written for IDM on Windows and assumes a browser get then a manager download.
- tooling: IDM on Windows is the documented client; the guide gives exact IDM settings (Default max conn = 1 free / 2 VIP).
- composes with: A Vietnamese PLG positioned as the cheap alternative to buying each host account. The two-connection cap makes it a poor fit for 1 TiB of monthly transfer unless the per-host daily cap is large, which is not published.
- reliability: A hard two-connection limit per machine with no published quota means the failure mode is a slow download rather than an error; support is a Facebook/Zalo channel.
- notes: Included for the constraint, not the price: it is the only Vietnamese service found that states a connection cap instead of a byte cap, and that changes the failure mode. Trigger condition: a published price and host table appear.
- evidence note: The guide's limit sentences and the homepage's positioning sentence were read. The price and payment rail are the two facts this record does not have; a pricing page or a checkout would supply both.
- extras:
  - hosts: 14+
  - client: IDM on Windows
  - resume: re-get for resume does not re-deduct bandwidth
- evidence:
  - [1] 2026-10-23: 'Vì giới hạn tối đa mỗi máy chỉ được 2 kết nối để download'; 'chỉnh số kết nối tối đa của IDM là 1 (đối với Free) và 2 (đối với Vip)'; 'sau get link thành công, băng thông của host đó sẽ bị trừ'
  - [2] 2026-10-23: 'hơn 14+ filehosts ... với giá thấp hơn 3-5 lần so với mua từng tài khoản ở mỗi filehost' (search-index read of the homepage)
- sources:
  - [1] https://getlinkvip.net/guide.html
  - [2] https://getlinkvip.net/
