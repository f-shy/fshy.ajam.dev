# AI Grant

> aigrant.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aigrant/ | JSON https://fshy.ajam.dev/api/v1/entity/aigrant.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AI Grant

- `compute/ai-grant` | dead | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://aigrant.org/
- free tier: The page still advertises '$5,000 - $50,000 in grants for open source projects, no strings attached' and 'Grants can come in the form of compute or cash', with the compute link pointing to andromeda.ai. The programme is described as funding builders of specific open-source artifacts. The listed awards are three in the 'Latest grants' block: abetlen for llama-cpp-python, philpax for the GGUF file format, and TySam for hlb-CIFAR10. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the served HTML contains no application route: the only outbound links are to aigrant.com, andromeda.ai, nfdg.com and the winners' own profiles, and there is no form, no mailto and no apply anchor; probed by extracting every href from the 200 response | metered: yes | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): there is no application route at all: the page carries no apply link, no form and no contact address, and the 'latest grants' list has not changed in at least 17 months, so the programme reads as dormant rather than closed. [1]
- limits note: there is no application route at all: the page carries no apply link, no form and no contact address, and the 'latest grants' list has not changed in at least 17 months, so the programme reads as dormant rather than closed.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing composes while the route is absent. If it reopened, the corporate-compute option via andromeda.ai would be the only award in the class payable as GPU time to a named vendor rather than as cash.
- reliability: no reliability event recorded
- notes: A REFUTATION of the best-known name in this class, and the reason it matters is that AI Grant is the programme a search for 'no strings attached grant for open source AI' surfaces first. Three separate facts make the verdict safe: no application route exists in the served HTML, the page is byte-identical to its May 2025 capture, and the three latest awards are 2023-era projects. This is not a product that was discontinued with a formal announcement; it is a page that stopped moving, which is the quietest way for a programme to end. What would reverse the verdict: an apply link appearing, or a new entry in the latest-grants list.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: '$5,000 - $50,000 in grants for open source projects, no strings attached'; 'Grants can come in the form of compute or cash'; the three latest grants named; read live; page 200
  - [1] 2026-10-22: the served HTML contains no application route: the only outbound links are to aigrant.com, andromeda.ai, nfdg.com and the winners' own profiles, and there is no form, no mailto and no apply anchor; probed by extracting every href from the 200 response
  - [2] 2026-10-22: the sibling accelerator is a different and live product: '$250,000 on an uncapped SAFE for your AI-native product startup', '$350,000 in Azure credits', 'Applications for Batch 4 are closed', quoted; this establishes that the same brand still operates, so the open-source grant lane is dormant by choice rather than because the organisation ended
- sources:
  - [1] https://aigrant.org/
  - [2] https://aigrant.com/
