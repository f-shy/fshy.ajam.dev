# Esperanto Technologies

> esperanto.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/esperanto/ | JSON https://fshy.ajam.dev/api/v1/entity/esperanto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Esperanto Technologies

- `compute/esperanto-technologies` | dead | evidence documented | binding none | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.esperanto.ai/
- free tier: Ceased operations, while its own homepage still sells the product. The live page states 'Esperanto Technologies has ceased operations. Esperanto Technologies' IP has been acquired by Nekko.ai' at the top, and further down, unchanged, 'The Esperanto AI / HPC Compute Server... Available today for purchase or secure remote cloud access', describing the ET-SoC-1 as a TSMC 7 nm chip with over a thousand RISC-V cores. The company closed in July 2025; the IP sale completed in October 2025 and the RTL is being released as CORE-ET through the OpenHW Group. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous
- interface: unknown
- limits note: nothing binds because no capacity is sold or given: there is no operator of the hardware left to rent it from.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing chains. The only artifact with continuing value is the open-sourced RTL, which runs in a simulator and produces no compute; the SDK and the cloud access that the page still advertises have no operator behind them.
- reliability: no reliability event recorded
- notes: Acquisition by Nekko.ai is documented as an IP purchase and open-source release rather than an active operating cloud business.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: Esperanto ET-SoC-1, RISC-V many-core
- evidence:
  - [1] 2026-10-22: 'Esperanto Technologies has ceased operations. Esperanto Technologies' IP has been acquired by Nekko.ai', quoted from the live homepage, on the same page as 'Available today for purchase or secure remote cloud access'
  - [2] 2026-10-22: EE Times reported on 2025-07-04 that the company was winding down its silicon business, with headcount cut by 90 percent and European subsidiaries closing
  - [3] 2026-10-22: Ainekko acquired the IP in October 2025 after Esperanto closed in July 2025, and is releasing RTL, tools and documentation under Apache License v2
- sources:
  - [1] https://www.esperanto.ai/
  - [2] https://www.eetimes.com/ai-startup-esperanto-winds-down-silicon-business/
  - [3] https://www.jonpeddie.com/news/ainekko-acquires-esperanto-ip/
