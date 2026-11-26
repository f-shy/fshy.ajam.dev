# Hume AI

> hume.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hume/ | JSON https://fshy.ajam.dev/api/v1/entity/hume.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hume AI

- `compute/hume-ai` | fails-identity | evidence documented | binding write-gated | category inference API
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T16:38:11.106Z (live) | stale on 2026-12-26
- url https://dev.hume.ai
- free tier: The API is not self-serve: on the Expression Measurement API launch the vendor states 'The Expression Measurement API is now available in limited release' and 'Contact our team to request access, then start with the overview'. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: application-gated
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
  - [6] 2026-11-25: the Expression Measurement API is in limited release and access requires contacting the vendor team | capture: sha256:06098a51021b1135671363c98509667caa993ae7a989f52b614e50b176f9f4cb | quote: The Expression Measurement API is now available in limited release. It measures emotional expression in speech and in faces, from uploaded audio and images or live audio and video streams. Contact our team to request access, then start with the overview
  - [6] 2026-11-25: the access gate is unchanged: the API is in limited release and access is by contacting the team | capture: sha256:06098a51021b1135671363c98509667caa993ae7a989f52b614e50b176f9f4cb | quote: The Expression Measurement API is now available in limited release. It measures emotional expression in speech and in faces, from uploaded audio and images or live audio and video streams. Contact our team to request access, then start with the overview
  - [2] 2026-11-25: the pricing URL now serves a marketing page for an evaluation platform with no prices or free tier | capture: sha256:8f4301ed048be6b4796530bea239e346189ce6e7e6ba212cf02d9abc2eb6ce69 | quote: One evaluation platform for models and agents
- sources:
  - [1] https://dev.hume.ai
  - [2] https://www.hume.ai/pricing
  - [3] https://platform.hume.ai/pricing
  - [4] https://freedom251.com/apps/hume-octave/pricing/
  - [5] https://costbench.com/software/voice-apis/hume-ai/
  - [6] https://dev.hume.ai/expression-measurement/changelog/2026/10/6
