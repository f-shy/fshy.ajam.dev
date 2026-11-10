# ClawCloud

> claw.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/claw/ | JSON https://fshy.ajam.dev/api/v1/entity/claw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ClawCloud

- `compute/clawcloud` | dead | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-24T03:25:00.000Z (live) | stale on 2026-11-24
- url https://claw.cloud/
- free tier: Withdrawn. The operator published a shutdown notice quoted in the forums: 2026年6月1日 stops new registrations, new purchases, renewals and upgrades; 2026-06-01 to 2026-06-30 is a migration and refund window; 2026年6月30日 24:00 the service is formally shut down, every affected instance is force-stopped and 数据将被永久销毁 (the data is permanently destroyed). On 2026-10-22 the domain returns HTTP 503. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: Moot: the product cannot be bought. The earlier signup route was not recorded on 2026-10-24.
- interface: unknown
- limits note: The binding fact is the closure date. The refund was pro-rata by remaining billing period, by ticket, and only to the original payment rail; a machine transferred between accounts with no payment record was refused.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing composes: a machine that no longer exists cannot host anything, and the notice gives 30 days to move, which is the practical planning number for any small host among evaluated providers.
- reliability: no reliability event recorded
- notes: ClawCloud is documented as a Chinese-market host that discontinued service with a published 30-day schedule.
- extras:
  - facets.class: enforcement
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: HTTP/1.1 503 Service Unavailable returned for the site root, one-line body No server is available to handle this request
  - [2] 2026-10-22: the shutdown notice is reposted with its dates: 2026-06-01 stop new purchases and renewals, 2026-06-30 24:00 服务正式关停, and 数据将被永久销毁, quoted from the thread body in the search snippet
  - [3] 2026-10-22: a second copy of the same notice states 2026年6月30日 起，正式关停 VPS 及相关托管业务, quoted
  - [4] 2026-10-22: a customer posts the vendor's refund reply, which confirms 云服务 being discontinued effective June 30, 2026 and pro-rata refunds by ticket date
  - [5] 2026-10-24: HTTP 530 on 2026-10-24: the free container product's own host does not answer, which is consistent with the published 2026-06-30 shutdown
- sources:
  - [1] https://claw.cloud/
  - [2] https://www.nodeseek.com/post-756028-1
  - [3] https://www.nodeseek.com/post-755905-1
  - [4] https://www.nodeseek.com/post-794064-1
  - [5] https://run.claw.cloud/
