# Hume AI

> hume.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hume/ | JSON https://fshy.ajam.dev/api/v1/entity/hume.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hume AI

- `compute/hume-ai` | fails-identity | evidence documented | binding write-gated | category inference API
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://dev.hume.ai
- free tier: The API is no longer self-serve: 'The API is currently in limited release; contact our team to request access', on the Expression Measurement overview. The pricing URL no longer exists as a page: https://www.hume.ai/pricing and https://platform.hume.ai/pricing both land on the marketing home page, which now sells a voice-AI evaluation platform rather than an API. Third-party readings of the pricing page from September 2026 recorded a Free plan at '10,000 characters per month, 5 EVI minutes, 15 requests per minute, 1 concurrent connection' plus USD 20 of new-account credits. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: application-gated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): access is granted by a sales conversation: 'contact our team to request access' means the free allowance that existed in September 2026 cannot be signed up for in October 2026, and a person with an email address has no route in without an approved application. [1]
- limits note: access is granted by a sales conversation: 'contact our team to request access' means the free allowance that existed in September 2026 cannot be signed up for in October 2026, and a person with an email address has no route in without an approved application.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the interesting part of the September free tier was 10,000 characters of Octave TTS plus 5 EVI minutes on one email; with the gate now in place, the only route is to substitute ElevenLabs or Cartesia, both recorded among evaluated providers at 10,000 and 20,000 monthly credits.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The finding is the withdrawal of a self-serve free tier behind an access request, which is why the verdict is fails-identity rather than dead: Hume sells and its evaluation product is live, but the API needs an approved conversation. Data point worth carrying: the site's own benchmark page labels one model view 'Illustrative, not real data', so the leaderboard numbers on the new home page are not measurements.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: application-gated
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'The API is currently in limited release; contact our team to request access', quoted from the Expression Measurement API overview
  - [2] 2026-10-22: requesting the pricing URL returned final_url https://www.hume.ai/ with the title 'Measure and improve real-world voice AI performance'; the page sells an evaluation platform and states no prices or free tier
  - [3] 2026-10-22: the platform pricing URL also returned final_url https://www.hume.ai/, the same marketing home page
  - [4] 2026-10-22: 'Free | billed monthly - 10,000 characters per month - 5 EVI minutes - 15 RPM', read by that site on 2026-09-20, reported and no longer reproducible from the vendor
  - [5] 2026-10-22: 'Free - 10,000 characters of TTS/month (Octave 1 & Octave 2) - 5 minutes of EVI included - 15 requests per minute - 1 concurrent connection', reported, corroborating the September reading
- sources:
  - [1] https://dev.hume.ai
  - [2] https://www.hume.ai/pricing
  - [3] https://platform.hume.ai/pricing
  - [4] https://freedom251.com/apps/hume-octave/pricing/
  - [5] https://costbench.com/software/voice-apis/hume-ai/
