# AIcrowd

> aicrowd.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aicrowd/ | JSON https://fshy.ajam.dev/api/v1/entity/aicrowd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AIcrowd

- `compute/aicrowd` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone unknown, ID no, institution no | verified 2026-11-06T17:42:10.985Z (live) | stale on 2026-12-07
- url https://discourse.aicrowd.com/t/how-to-claim-compute-credits/17582
- free tier: Sponsored compute credits for competition entrants, quoted: 'Each eligible team may initially receive USD 100 in credits from one sponsor of their choice: NVIDIA, AWS or OpenAI.' Eligibility, quoted: 'Teams that submit results exceeding the baseline performance in a track are eligible to apply for credits, on a first come, first served basis.' Allocation, quoted: 'Credits are limited and will be allocated first come, first served among eligible teams.' The application form closed, quoted: 'Please fill the form by 31st Decemeber, 2025'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an AIcrowd account: 'Such information includes your email and username (display name), which are required for creating an Account'. The sign-up form asks for a full name, a username, an email address and a password, and no payment detail. The account is also the delivery address for the credits: 'If approved, your credit code and redemption instructions will be sent to the AIcrowd linked email you provided in the form.' The phone requirement is not published on https://www.aicrowd.com/participants/sign_up.
- interface: unknown
- limits:
  - write-gated (binding): the gate is a qualifying leaderboard submission before the credit round closes: a team must first beat a published baseline, then wait 7 to 14 days for manual verification, and credits are first come first served, so the pool can close before a slow entrant applies. [1]
- limits note: the gate is a qualifying leaderboard submission before the credit round closes: a team must first beat a published baseline, then wait 7 to 14 days for manual verification, and credits are first come first served, so the pool can close before a slow entrant applies.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The USD 100 is redeemable at NVIDIA, AWS or OpenAI, so it buys a different shape depending on the sponsor: at Lambda's documented on-demand rate of USD 3.99 per H100 SXM GPU-hour (compute/lambda) USD 100 is about 25 H100-hours, while the same credit at OpenAI buys tokens instead of a machine.
- reliability: no reliability event recorded
- notes: The smallest credit among evaluated providers and the most repeatable: AIcrowd runs several credit-backed challenges a year with the same claim-form pattern. Three explanations for the size were considered: a fixed marketing budget per team, anti-farming through the baseline requirement, and platform economics. The page states the second explicitly and is silent on the other two. What would change the verdict is the additional round, quoted: 'If credits remain in the middle of the competition, we will open an additional round for extra credit applications', which did not appear on the page read.
- extras:
  - facets.class: hackathon-credit
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'Each eligible team may initially receive USD 100 in credits from one sponsor of their choice: NVIDIA, AWS or OpenAI.'; 'Teams that submit results exceeding the baseline performance in a track are eligible to apply for credits, on a first come, first served basis'; 'We will verify your score and submission link against the official AIcrowd leaderboard'; 'KRAFTON and its subsidiaries are not eligible for prize money or credits'; page 200
  - [2] 2026-10-22: the challenge page links 'Claim compute credits to improve your solution' and names two tracks with a separate 'sponsored credit pool'; the cash prize structure is separate from the credits; page 200
  - [3] 2026-11-04: an AIcrowd account requires an email address and a username | capture: sha256:14f11959c1bac19f004ce0ad06cecd2b8b34bcf8b916ccbfdeb64038cf4535e4 | quote: Such information includes your email and username (display name), which are required for creating an Account
  - [4] 2026-11-06: the sign-up form takes an email address, a username and a password and no payment detail | capture: sha256:283be41852956ce3d03fc6776fc19374d5b5bea150279bf8c8ffe17479aec47c | quote: type="text" name="participant[user_email]"
- sources:
  - [1] https://discourse.aicrowd.com/t/how-to-claim-compute-credits/17582
  - [2] https://www.aicrowd.com/challenges/orak-game-agent-challenge-2025
  - [3] https://design.aicrowd.com/pages/privacy-policy
  - [4] https://www.aicrowd.com/participants/sign_up
