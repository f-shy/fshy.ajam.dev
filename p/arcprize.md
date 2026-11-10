# ARC Prize Foundation

> arcprize.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arcprize/ | JSON https://fshy.ajam.dev/api/v1/entity/arcprize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ARC Prize Foundation

- `compute/arc-prize-foundation` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:48.985Z (live) | stale on 2026-12-05
- url https://arcprize.org/competitions/2026
- free tier: '$2M in prizes. 3 tracks. Open source progress toward AGI.' The ARC-AGI-3 track is '$850K Total' with a '$700K' grand prize, a '$75K (guaranteed)' top-score award split 40/15/10/5/5 thousand, and two '$75K (guaranteed)' milestone rounds at June 30 and September 30, 2026. The Paper Prize pays '$75K (guaranteed)' to the highest-scoring paper and '$50K / $20K / $5K' for first to third. Entry is a Kaggle competition, and payment is conditional, quoted: 'All leading participants are expected to open source their solutions to be eligible for a prize.' | unit: seconds | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: prize
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published: the page read states no egress allowance and no overage price; https://arcprize.org/competitions/2026 read 2026-11-03; internet access is not available during Kaggle evaluation | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): an open-source release of the whole solution is a condition of payment and the modal outcome is zero: entry is free and open, but the money is decided on a leaderboard whose top places are contested by funded labs, while the $700K grand prize is written as a forward offer ('Awarded to the first eligible agent that scores 100%') rather than as an accumulated balance. [1]
- limits note: an open-source release of the whole solution is a condition of payment and the modal outcome is zero: entry is free and open, but the money is decided on a leaderboard whose top places are contested by funded labs, while the $700K grand prize is written as a forward offer ('Awarded to the first eligible agent that scores 100%') rather than as an accumulated balance.
- binding note: the same as limits note
- interface detail: unverified: the page documents no REST API, CLI or SSH access; there is a Kaggle competition for each track
- tooling: not stated
- composes with: The competition supplies the compute: entry is a Kaggle notebook, and earlier readings already holds Kaggle's weekly 30 hour GPU quota and free TPU in compute/kaggle-notebooks, so the prize can be contested with no card. A guaranteed milestone award then buys GPU at spot rates. What breaks the chain is the open-source condition: the solution must be public to be paid, so the same work cannot be sold twice.
- reliability: no reliability event recorded
- notes: The distinction that matters here is that the entry cost is zero and the tool is a browser notebook, so the downside is time only. The milestone structure supports the second for a solo entrant: two guaranteed rounds of USD 75,000 across three places each, decided on a leaderboard rather than on a grant application. The page states the grand prize as a forward-looking offer ('the first eligible agent'), not as a fact about past results, and this record adds no claim about whether it has been won.
- extras:
  - facets.class: prize
  - facets.free_tier_kind: prize
- evidence:
  - [1] 2026-10-22: '$2M in prizes. 3 tracks.'; key dates 'March 25, 2026 - Competition starts', 'June 30, 2026 - ARC-AGI-3 Milestone #1', 'November 2, 2026 - Submissions due'; 'All leading participants are expected to open source their solutions to be eligible for a prize'; page 200
  - [2] 2026-10-22: '$850K Total'; 'Grand Prize (100%) - $700K Awarded to the first eligible agent that scores 100%'; 'Top Score Award - $75K (guaranteed)'; 'Milestone Prizes - $75K (guaranteed)'; 'No internet access during evaluation'; 'Hardware and compute limits will be announced with the competition launch' (read through the search index for arcprize.org, not the origin page)
  - [3] 2026-10-22: 'Top Paper - $75K (guaranteed)'; '1st Prize: $50K', '2nd Prize: $20K', '3rd Prize: $5K' (read through the search index for arcprize.org)
  - [4] 2026-10-22: 'TOTAL PRIZES AVAILABLE: $75,000 First Prize: $50,000 Second Prize: $20,000 Third Prize: $5,000'; 'Client may choose to award up to $375,000 for papers that score above 4.5/5 on the paper rubric' (read through the search index for kaggle.com)
  - [1] 2026-11-03: evaluation runs without internet; the page states no egress allowance or price | capture: sha256:1bc1195e84a4c3180d019482264956a7989864e19fe78132ec30ca6375d0a4d2 | quote: Internet access is not available during Kaggle evaluation (no API-based systems like GPT/Claude/etc.)
- sources:
  - [1] https://arcprize.org/competitions/2026
  - [2] https://arcprize.org/competitions/2026/arc-agi-3
  - [3] https://arcprize.org/competitions/2026/paper
  - [4] https://www.kaggle.com/competitions/arc-prize-2026-paper-track/rules
