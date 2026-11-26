# Gabia VPS hosting

> gabia.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gabia/ | JSON https://fshy.ajam.dev/api/v1/entity/gabia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gabia VPS hosting

- `compute/gabia-vps-hosting` | dead | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.gabia.com/gabia_notice/view.php?seq_no=32081
- free tier: The product still has a published ladder of 2 vCPU with 512 MB and 12.5 GB SSD and 300 GB monthly traffic at KRW 10,000 a month, 1 GB at 20,000, 2 GB at 35,000 and 4 GB at 55,000, with no minimum term and no cancellation penalty. New applications were restricted from 2024-05-02 14:00, and the vendor named g클라우드 가상서버 and 1분 설치 서버 as the replacements. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - write-gated (binding): The door is closed rather than measured: the vendor restricted new applications for this product in 2024 and points buyers to two other products, so the constraint that fails first is that no new account can be opened at all. [1]
- limits note: The door is closed rather than measured: the vendor restricted new applications for this product in 2024 and points buyers to two other products, so the constraint that fails first is that no new account can be opened at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing chains, and the record exists so that a reader who finds the KRW 10,000 ladder on Gabia's manual does not spend time looking for the order button.
- reliability: no reliability event recorded
- notes: Classified as dead on the vendor's own restriction notice. The notice is dated 2024 and no reopening was found; a reopening announcement would supersede this record, and the two replacement products are separate findings. This is the same pattern as XServer VPS in Japan: the cheap classic product is withdrawn and the replacement is a metered cloud that costs more.
- extras:
  - facets.class: regional-withdrawn
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 0.5
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the vendor's notice states that new applications for VPS 호스팅 are restricted from 2024-05-02 14:00, that existing services are unaffected, and that the replacement products are g클라우드 가상서버 and 1분 설치 서버
  - [2] 2026-10-22: the product manual still publishes the ladder: VPS 512MB at 10,000 원 a month with 2 vCore, 512 MB, SSD 12.5 GB and 300 GB of traffic, VPS 1G at 20,000 원, VPS 2G at 35,000 원 and VPS 4G at 55,000 원, with no compulsory period and no cancellation penalty
- sources:
  - [1] https://www.gabia.com/gabia_notice/view.php?seq_no=32081
  - [2] https://customer.gabia.com/manual/hosting/9862/16522
