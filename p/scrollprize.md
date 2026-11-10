# Vesuvius Challenge

> scrollprize.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scrollprize/ | JSON https://fshy.ajam.dev/api/v1/entity/scrollprize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vesuvius Challenge

- `compute/vesuvius-challenge` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://scrollprize.org/prizes
- free tier: 'Open prize pool $2,140,000'. Grand prize, quoted: '$800,000 to the first team or individual to fully unroll and make readable a scroll from the set below. We also have prizes for second place ($100,000), third place ($50,000), and fourth place ($50,000) - $1,000,000 in total.' The door, quoted: 'Prizes will be awarded to any team or individual that fully digitally unrolls and makes readable ... one of the eligible CT scans', 'Anyone can help', and the only registration term: 'To qualify, you must have registered on the Vesuvius Challenge Discord at the time of the submission.' Computing is the entrant's, quoted: 'Unlimited time, compute, and manual effort may be spent creating generic ML datasets to train ML models.' Deadline, quoted: 'June 25th, 2027 (11:59pm Pacific)'. | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: prize
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): the constraint is the science: the prize needs a fully automated unrolling pipeline judged reproducible by a technical team and legible by papyrologists, and the rules permit unlimited compute, which means the entrant funds the GPU time. [1]
- limits note: the constraint is the science: the prize needs a fully automated unrolling pipeline judged reproducible by a technical team and legible by papyrologists, and the rules permit unlimited compute, which means the entrant funds the GPU time.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Cash with no spending restriction, so it buys compute at any rate: USD 100,000 at Lambda's documented on-demand rate of USD 3.99 per H100 GPU-hour (compute/lambda) is about 25,000 H100-hours. The monthly progress prizes are the part that composes with a zero budget, because they pay before the grand prize is won and are sized for a weekend of work.
- reliability: no reliability event recorded
- notes: The only programme documented that pays monthly, names individuals explicitly, and requires nothing but a Discord account. It awards no compute, so the record names the compute cost as a binding constraint instead of hiding it: 'Unlimited time, compute' is the provider saying the entrant pays. What would raise the verdict is a published compute partnership; none appeared on either page read. The open question is the size and cadence of the monthly prizes, which the front page asserts ('prizes every month') and the prizes page does not itemise in the portion read.
- extras:
  - facets.class: prize
  - facets.free_tier_kind: prize
- evidence:
  - [1] 2026-10-22: 'Open prize pool$2,140,000'; 'Grand Prize deadline June 25th, 2027'; '$800,000 to the first team or individual'; 'second place ($100,000)', 'third place ($50,000)', 'fourth place ($50,000)'; 'To qualify, you must have registered on the Vesuvius Challenge Discord at the time of the submission'; 'Unlimited time, compute, and manual effort may be spent'; page 200
  - [2] 2026-10-22: 'Over $1,958,500 awarded'; 'we run a $2M competition, with prizes every month'; 'Win the $1,000,000 Grand Prize'; 'Win the $500,000 First Letters Prizes'; page 200
- sources:
  - [1] https://scrollprize.org/prizes
  - [2] https://scrollprize.org/
