# Render Network

> rendernetwork.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rendernetwork/ | JSON https://fshy.ajam.dev/api/v1/entity/rendernetwork.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Render Network

- `compute/render-network` | trial-only | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://try.rendernetwork.com/getstarted
- free tier: The credit offer is withdrawn. Page quoted: 'Get EUR 50 in free credits, enough for 300 frames or 30 seconds of animation' and then 'The offer has concluded, please stay updated at rendernetwork.com'. Access now requires a licence: quoted from the artist guide, 'To get started on the Creator portal, you must have an active OctaneRender License or Subscription'. | unit: seconds | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: three tiers priced per 400 OctaneBench-hours: EUR 0.60 economy, EUR 1.20, EUR 2.40; bandwidth 0.09 credits per GB of scene assets | metered: yes | source: [2]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): The free credits are gone and the remaining free path needs a free Octane Prime licence plus a Blender or Octane workflow, so the binding constraint is the software gate rather than a quota. [1]
- limits note: The free credits are gone and the remaining free path needs a free Octane Prime licence plus a Blender or Octane workflow, so the binding constraint is the software gate rather than a quota.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Only useful for rendering, and only through a 3D content pipeline. A free Prime licence plus a Blender scene is a chain that costs nothing, but Prime explicitly disables network rendering and caps at 1 GPU, so the free licence does not by itself unlock the network.
- reliability: no reliability event recorded
- notes: Two things are true and easy to confuse. The EUR 50 and EUR 250 credits are closed. The 'free access for all Blender users' claim traces to RNP-014, a 2024 governance proposal, whose own announcement says free access 'would be added to the Render Foundation roadmap if approved'. The network now requires an active Octane licence. The Prime free tier does not include network rendering, so it does not hand over the network. Also note: render.com is a different company (a PaaS) and its 750 free instance-hours belong to another topic, not to this one.
- extras:
  - facets.class: decentralized-render-marketplace
  - facets.shape.gpu_class: OctaneBench tiers from EUR 0.60 to EUR 2.40 per 400 OBh
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: the page offers EUR 50 in free credits and states in the same block 'The offer has concluded, please stay updated at rendernetwork.com'; a raw fetch confirms both strings
  - [3] 2026-10-22: the same page template offers EUR 250 in free credits, also closed, so per-campaign amounts varied between EUR 50 and EUR 250
  - [4] 2026-10-22: quoted: 'you must have an active OctaneRender License or Subscription', with a free Octane Prime licence named as the no-cost route
  - [5] 2026-10-22: the Octane Prime free tier is real but limited: quoted 'A maximum of 1 GPU is available for rendering' and 'Network rendering is not available'
  - [2] 2026-10-22: three tiers priced per 400 OctaneBench-hours: EUR 0.60 economy, EUR 1.20, EUR 2.40; bandwidth 0.09 credits per GB of scene assets
- sources:
  - [1] https://try.rendernetwork.com/getstarted
  - [2] https://rendernetwork.com/pricing
  - [3] https://try.rendernetwork.com/basel
  - [4] https://know.rendernetwork.com/getting-started/how-to-get-started
  - [5] https://home.otoy.com/render/octane-render/demo/
