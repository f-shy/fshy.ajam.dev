# Getlinkfshare

> getlinkfshare.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getlinkfshare/ | JSON https://fshy.ajam.dev/api/v1/entity/getlinkfshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Getlinkfshare

- `debrid/getlinkfshare-com` | qualifies-with-caveat | evidence documented | binding none | category single-host premium link generator (Vietnamese: Fshare only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://getlinkfshare.com/
- price VND 0
- free tier: 'Get link VIP Fshare, tải nhanh link Fshare tốc độ cao miễn phí không giới hạn' - free and unlimited in the vendor's words, with the caveat printed directly beneath: 'Hiện tại Get link Fshare đang bảo trì, tỉ lệ thành công ngẫu nhiên' (under maintenance, success rate random). | unit: unlimited | metered on: unstated | read on: 2026-10-23 | source: [1] | note: No account, no price, no quota: the only stated condition is a random success rate.
- per-object cap: not stated | source: [1]
- retention: not applicable: a direct link is returned | source: [1]
- egress: No published allowance. The mechanism is URL rewriting: 'Thay thế www.fshare.vn thành getlinkfshare.com', so the free path inherits whatever Fshare's own free-account shaping does. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No signup, no payment, no email: the URL rewrite needs nothing. This is the one Vietnamese Fshare path that a foreigner can use without any identity at all.
- interface: rest
- limits:
  - request-rate: unstated; the vendor states a random success rate rather than a limit [1]
- limits note: No numeric cap exists to record. The failure mode is a refused get, not a quota error.
- binding note: Nothing measurable binds because nothing is quantified; the constraint is the vendor's own admission that success is random.
- interface detail: Host-substitution: replace the fshare.vn domain with getlinkfshare.com and keep the /file/<id> path.
- tooling: Any browser; the rewritten URL is a plain HTTP link.
- composes with: The cheapest possible entry to Fshare and the least reliable: no account, no fee, no quota, and a vendor-admitted random success rate. Useful as a fallback in a queue that already has a paid path.
- reliability: Vendor states the service is under maintenance with a random success rate; an unquantified success rate is the whole reliability story, and there is no support channel to ask.
- notes: Included because the sector needs a zero-identity baseline against which the paid shops can be judged: free, anonymous, and explicitly unreliable. Trigger condition: the rewrite stops working twice in a row on a real link.
- evidence note: One page read on 2026-10-23; the maintenance sentence is the vendor's own. Measuring the success rate would need a batch of Fshare links, which on 2026-10-23 did not have.
- extras:
  - mechanism: domain substitution, path preserved
  - maintenance_notice: vendor-stated
- evidence:
  - [1] 2026-10-23: 'Get link VIP Fshare, tải nhanh link Fshare tốc độ cao miễn phí không giới hạn'; 'Hiện tại Get link Fshare đang bảo trì, tỉ lệ thành công ngẫu nhiên'; domain-substitution instructions
  - [2] 2026-10-23: third-party description of the same rewrite workflow, and that the page accepted only 'https://www.fshare.vn/file/xxx' shaped links
- sources:
  - [1] https://getlinkfshare.com/
  - [2] https://trainghiemso.vn/chia-se-2-trang-web-get-link-fshare-moi-nhat-2019/
