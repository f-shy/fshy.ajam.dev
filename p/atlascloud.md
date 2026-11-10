# Atlas Cloud open

> atlascloud.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/atlascloud/ | JSON https://fshy.ajam.dev/api/v1/entity/atlascloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Atlas Cloud open

- `compute/atlas-cloud-open` | qualifies-with-caveat | evidence reported | binding write-gated | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T11:01:13.171Z (live) | stale on 2026-11-19
- url https://www.atlascloud.ai/oss-program
- free tier: Reported tiers for maintainers of public, OSI-licensed projects: Starter at USD 50 to 150 per month for 3 months at roughly 100 to 1,000 stars, Growth at USD 150 to 400 per month for 3 months, and Flagship at USD 400 to 1,500 per month renewed monthly. Reported by a third-party perks directory and by a project maintainer's GitHub discussion post. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: Reported requirement is being a primary or core maintainer of a public repository under an OSI-approved licence; no company or institution is named.
- interface: rest, cli
- limits:
  - write-gated (binding): The vendor page could not be read, so the tier amounts, the star thresholds and the renewal terms are unverified; the maintainer status is the identity gate if the offer is real. [1]
- limits note: The vendor page could not be read, so the tier amounts, the star thresholds and the renewal terms are unverified; the maintainer status is the identity gate if the offer is real.
- binding note: the same as limits note
- interface detail: an API used through the OpenAI SDK, per the docs page: "Drop-in replacement for OpenAI SDK. Just change the base URL and API key to get started"
- tooling: OpenAI-compatible API (change the base URL and API key in the OpenAI SDK); the atlas CLI; a hosted MCP server and agent skills.
- composes with: A monthly renewed inference credit is the only recurring shape found in this class, and it composes with an existing public project rather than requiring a new one. Where it breaks: it buys inference on a reseller's catalogue, not GPU time, and the renewal is at the vendor's discretion.
- reliability: no reliability event recorded
- notes: The vendor URL atlascloud.ai/oss-program redirected to the homepage on the read date, so the primary source could not be read and this stays reported, not documented. Two independent third parties agree on the tier structure, which is why it is recorded at all. If the program is live it is a recurring grant for anyone with a public repository; the route to settle it is a direct request to the vendor.
- extras:
  - facets.class: open-source-sponsorship
  - facets.free_tier_kind: recurring-credit
- evidence:
  - [2] 2026-10-22: three tiers at USD 50-150, USD 150-400 and USD 400-1,500+ per month, the star thresholds, and the OSI-licence and core-maintainer requirement, reported
  - [3] 2026-10-22: an Atlas Cloud team post offers '3 months of free credits if you integrate the API ... and add a small README badge', reported
  - [4] 2026-11-04: a first-party CLI exists | capture: sha256:be50c04d0d084b623b9303d1f884ad4b156f9802533f493400530f432bd5e6ae | quote: Atlas Cloud command-line tool for image, video, and LLM generation
  - [5] 2026-11-04: an OpenAI-compatible HTTP API with SDK support | capture: sha256:7f42447b76e0d5dce8c4cd02f86a62862507bb116407d7209f4896972f787bdd | quote: Drop-in replacement for OpenAI SDK. Just change the base URL and API key to get started
  - [5] 2026-11-04: the docs page names an API used through the OpenAI SDK | capture: sha256:7f42447b76e0d5dce8c4cd02f86a62862507bb116407d7209f4896972f787bdd | quote: Drop-in replacement for OpenAI SDK. Just change the base URL and API key to get started
- sources:
  - [1] https://www.atlascloud.ai/oss-program
  - [2] https://iterm.today/en/offer/atlas-cloud-open-source-program/
  - [3] https://github.com/Comfy-Org/ComfyUI/discussions/14827
  - [4] https://www.atlascloud.ai/cli
  - [5] https://www.atlascloud.ai/docs
