# GPU Outlet

> gpuoutlet.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gpuoutlet/ | JSON https://fshy.ajam.dev/api/v1/entity/gpuoutlet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GPU Outlet

- `compute/gpu-outlet` | fails-identity | evidence documented | binding write-gated | category GPU cloud | tier reserved capacity marketplace
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T07:36:21.683Z (live) | stale on 2026-12-04
- url https://gpuoutlet.ai/
- free tier: no free tier and no rented machine: a marketplace for reserved GPU capacity between companies. Indicative clearing prices on its home page: H100 80 GB $1.85 an hour, A100 80 GB $0.95, RTX 4090 $0.42 (windows dated Aug to Sep 2026); the price index lists an 8x H100 SXM node in Helsinki at $2.30 per GPU-hour. The pages list no L40S or L4. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: the unit is reserved GPU capacity, not an object | source: [2]
- retention: not applicable: the marketplace gives no access to machines | source: [2]
- egress: not applicable: the seller delivers the capacity under its own contract with the buyer | metered: no | source: [2]
- identity: institution | detail: 'Every participant is a company, not a person.' Sign-up takes a first name, last name and work email with a 6-digit email code (or Google or GitHub); Buyers pay the marketplace nothing and sellers pay a 2% success fee.
- interface: rest
- limits:
  - write-gated (binding): reserved capacity only, sold by introduction; there is no on-demand or hourly self-service rental, and every participant is a company [1]
- limits note: buying is sales-assisted: a listing becomes a request and the team brokers the deal; some listings are indicative with no published rate
- binding note: the gate is the company account and the brokered introduction, not a quota
- interface detail: a web dashboard (Radar board and requests) and a partner REST API at api.gpuoutlet.ai for requests, opportunities and introductions; neither gives access to a machine.
- tooling: a dashboard with a Radar board of listings by GPU model, region and availability window, plus a partner API; after a seller accepts a request, the two companies contract and pay each other directly.
- composes with: not a route to a machine: the marketplace introduces a buyer company to a seller that holds reserved nodes, and the capacity is reserved for a term, not rented by the hour.
- reliability: unverified: no status page or incident history was read; the home page rows for H100, A100 and RTX 4090 carry windows from Aug to Sep 2026, so they are indicative and may be out of date
- notes: reserved multi-node capacity from other operators, brokered by introduction; the 2% success fee is paid by the seller.
- evidence note: the marketplace model and company requirement are read on the vendor's own docs; the prices are indicative rows from its home page
- evidence:
  - [1] 2026-11-03: an indicative H100 80 GB row at $1.85 an hour, US East, Sep 2026 window | capture: sha256:2fcddd1edcce921c93f7c2919db8543262e59a87468cbc9561f6383a30e72d71 | quote: ### H100 80GB 80 GB US EastSep 2026 $1.85/hr
  - [1] 2026-11-03: an indicative A100 80 GB row at $0.95 an hour, US Central, Sep 2026 window | capture: sha256:2fcddd1edcce921c93f7c2919db8543262e59a87468cbc9561f6383a30e72d71 | quote: ### A100 80GB 80 GB US CentralSep 2026 $0.95/hr
  - [1] 2026-11-03: an indicative RTX 4090 row at $0.42 an hour, US West, Aug 2026 window | capture: sha256:2fcddd1edcce921c93f7c2919db8543262e59a87468cbc9561f6383a30e72d71 | quote: ### RTX 4090 24 GB US WestAug 2026 $0.42/hr
  - [1] 2026-11-03: the home-page prices are indicative clearing prices for reserved windows | capture: sha256:2fcddd1edcce921c93f7c2919db8543262e59a87468cbc9561f6383a30e72d71 | quote: Reserved windows for the next season's inventory. Indicative clearing prices update in real time on Radar.
  - [2] 2026-11-03: the marketplace does not rent hardware or give machine access | capture: sha256:9e498ea3506ee74fe0534476c2f79f54a50ae74703f942aa6f227cd923806731 | quote: It does not rent hardware or run workloads.
  - [2] 2026-11-03: every participant is a company | capture: sha256:9e498ea3506ee74fe0534476c2f79f54a50ae74703f942aa6f227cd923806731 | quote: Every participant is a company, not a person.
  - [2] 2026-11-03: buyers pay the marketplace nothing | capture: sha256:9e498ea3506ee74fe0534476c2f79f54a50ae74703f942aa6f227cd923806731 | quote: Buyers pay GPU Outlet nothing.
  - [2] 2026-11-03: the 2% success fee is paid by the seller | capture: sha256:9e498ea3506ee74fe0534476c2f79f54a50ae74703f942aa6f227cd923806731 | quote: Sellers pay a success fee of 2% of every amount they actually receive from an introduced buyer.
  - [3] 2026-11-03: a partner API for requests, opportunities, introductions and the Radar board | capture: sha256:d9a3b78bd54c1cda085f9d726e71dd688df6a1f7c8e059db4714819c9fbdf95e | quote: Programmatic access to requests, opportunities, introductions and the Radar board.
  - [4] 2026-11-03: sign-up asks for a first name, last name and work email with an emailed code | capture: sha256:6e0104a3178edae8a2c9aaa1a2f8529aaab1702cc032557151787ac93a0817b0 | quote: Sign up with your first name, last name and work email, then press Send verification code.
  - [4] 2026-11-03:  | capture: sha256:6e0104a3178edae8a2c9aaa1a2f8529aaab1702cc032557151787ac93a0817b0
  - [3] 2026-11-03: the price index lists reserved capacity only, no on-demand or hourly self-service rental | capture: sha256:d9a3b78bd54c1cda085f9d726e71dd688df6a1f7c8e059db4714819c9fbdf95e | quote: Reserved capacity only; there is no on-demand or hourly self-service rental.
  - [3] 2026-11-03: the price index lists an 8x H100 SXM reserved node in Helsinki at $2.30 per GPU-hour | capture: sha256:d9a3b78bd54c1cda085f9d726e71dd688df6a1f7c8e059db4714819c9fbdf95e | quote: | [H100 SXM](https://computeprices.com/providers/gpuoutlet/gpus/h100) | $2.30/hrReservedHelsinki | 80GB | 8× | 2048 GB | 11/2/2026 | [Rent](https://gpuoutlet.ai/app/radar) |
- sources:
  - [1] https://gpuoutlet.ai/
  - [2] https://docs.gpuoutlet.ai/introduction
  - [3] https://computeprices.com/providers/gpuoutlet
  - [4] https://docs.gpuoutlet.ai/quickstart.md
