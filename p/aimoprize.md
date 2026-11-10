# AIMO Prize

> aimoprize.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aimoprize/ | JSON https://fshy.ajam.dev/api/v1/entity/aimoprize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AIMO Prize

- `compute/aimo-prize` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:48.984Z (live) | stale on 2026-12-05
- url https://www.aimoprize.com/updates/2025-11-19-third-progress-prize-launched
- free tier: USD 10,000,000 fund, quoted: 'XTX Markets has launched a new $10mn challenge fund'; grand prize, quoted: 'The grand prize of $5mn will be awarded to the first publicly-shared AI model to enter an AIMO approved competition and perform at a standard equivalent to a gold medal in the IMO', plus 'a series of progress prizes ... totalling up to $5mn'. AIMO3 pot, quoted: 'Third $2.2 million AIMO progress prize'. Compute supplied, quoted: 'Contestants will have access to H100 GPUs to run their models, offering roughly double the compute power of AIMO2'; and for a subset, quoted: 'Up to 128 H100 GPUs are available to fine-tune models before submission through our partnership with the Fields Model Initiative ... For select participants (see Kaggle for criteria)'. Tinker credits are also offered, quoted: 'Tinker credits are available via our partnership with Thinking Machines'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: prize
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published: the page read states no egress allowance and no overage price; https://www.aimoprize.com/updates/2025-11-19-third-progress-prize-launched read 2026-11-03 | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): a Kaggle account and a successful subclass submission are the entry fee, and the compute pool is contest-scoped: H100 sessions exist only for notebooks attached to this competition, run with internet disabled, under a 5 hour GPU notebook limit, so the grant cannot be redirected to another workload. [1]
- limits note: a Kaggle account and a successful subclass submission are the entry fee, and the compute pool is contest-scoped: H100 sessions exist only for notebooks attached to this competition, run with internet disabled, under a 5 hour GPU notebook limit, so the grant cannot be redirected to another workload.
- binding note: the same as limits note
- interface detail: unverified: the announcement documents no REST API, CLI or SSH access; the compute is reached through Kaggle notebooks attached to the competition
- tooling: not stated
- composes with: The only programme among evaluated providers that hands a solo entrant a datacentre: a Kaggler who wins an extra prize received three nodes of eight H200s for a month, which is 24 H200s for roughly 730 hours, or about 17,520 H200-hours per team, over 168 H200s across seven teams. It composes with Kaggle because the pool, the notebook and the leaderboard are one account, and with earlier Kaggle record because that free weekly GPU quota is the practice rig for the same competition.
- reliability: no reliability event recorded
- notes: Future program phases depend on upcoming official announcements.
- extras:
  - facets.class: prize
  - facets.free_tier_kind: prize
  - facets.shape.gpu_class: H100
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: 'Third $2.2 million AIMO progress prize'; 'Contestants will have access to H100 GPUs to run their models, offering roughly double the compute power of AIMO2'; 'Up to 128 H100 GPUs are available to fine-tune models before submission through our partnership with the Fields Model Initiative'; 'Tinker credits are available via our partnership with Thinking Machines'; 'Whether you are a researcher at a major lab, a student with a passion for math and AI development, or an independent developer, we encourage you to enter AIMO3'; page 200
  - [2] 2026-10-22: 'we've added powerful new H100 machines to the AIMO hardware pool'; 'H100 are only available for notebooks attached to this competition, use of H100s for any other activity could result in moderation action'; 'all H100 sessions must have internet disabled'; 'CPU Notebook <= 9 hours run-time', 'GPU Notebook <= 5 hours run-time'
  - [3] 2026-10-22: 'each team in the AIMO Proof Pilot has been given access to three GPU nodes (8x H200s each) by the Japanese National Institute of Informatics. This totals 168 H200 GPUs across the evaluation'; winners named as individuals: 'Exalted Joseph, varianceofx, SKobayak, TAMU-TACO' and 'yemao ye'; page 200
  - [4] 2026-10-22: 'a $10mn challenge fund'; 'The grand prize of $5mn'; 'a series of progress prizes ... totalling up to $5mn'; 'The first AIMO progress prize opened to participants in April 2024, the second in October 2024, and the third in November 2025'; page 200
  - [1] 2026-11-03: the announcement describes the compute supplied and names no API, CLI or SSH access and no egress term | capture: sha256:01876c0ff6542cc2b5b47f097f633731985119cdd7dfc92be4aabfcbce17a472 | quote: Contestants will have access to H100 GPUs to run their models, offering roughly double the compute power of AIMO2.
- sources:
  - [1] https://www.aimoprize.com/updates/2025-11-19-third-progress-prize-launched
  - [2] https://www.kaggle.com/competitions/ai-mathematical-olympiad-progress-prize-3
  - [3] https://aimoprize.com/updates/2026-06-24-aimo-3-winners-announced
  - [4] https://www.aimoprize.com/
