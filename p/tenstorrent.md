# Tenstorrent TT Console

> tenstorrent.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tenstorrent/ | JSON https://fshy.ajam.dev/api/v1/entity/tenstorrent.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tenstorrent TT Console

- `compute/tenstorrent-tt-console` | qualifies-with-caveat | evidence documented | binding none | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-24T13:21:06.616Z (live) | stale on 2026-12-25
- url https://docs.tenstorrent.com/tools/index.html
- free tier: The docs state 'No hardware yet? console.tenstorrent.com lets you run LLM inference and image and video generation in the browser, backed by Tenstorrent hardware.' The console catalogue adds 'Cloud hardware access and advanced workflows (deployments, agents) available in staged rollout.' The Cloud Services Agreement says 'Certain Cloud Services and Models may be designated as fee-free or otherwise available without triggering a payment for a limited time or based on usage limits.' No catalogue price or free-tier size is published on the pages read. | unit: TiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-browser-inference
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The agreement states 'Fees are published at console.tenstorrent.com/dashboard/pricing, in the Console, or specified in an Order Form.' That pricing page answers a login wall and publishes no egress allowance or price to an anonymous reader. | metered: no | source: [1]
- identity: email | detail: The Cloud Services Agreement states 'Customer must have an Account to use the Cloud Services'; the signup form itself was not read, so which identifiers the account asks for is unverified.
- interface: browser, rest
- limits note: no rate, session length, token allowance or concurrency figure is published for the free console, so the constraint that fails first cannot be named.
- binding note: the same as limits note
- interface detail: The docs describe an in-browser console; models.dev lists an OpenAI-compatible REST API at https://console.tenstorrent.com/v1.
- tooling: not stated
- composes with: The console is the cheapest way to touch Tensix silicon and it chains with the open-source TT-Metalium and TT-Forge stacks, which compile locally at no cost. It breaks at scale: anything beyond a demo needs a Cloud instance or the Koyeb rental, both billed.
- reliability: unverified: https://console.tenstorrent.com/v1 answered HTTP 404 on 2026-11-24; the browser console was not exercised without an account
- notes: Two open questions, stated rather than filled: whether the console costs nothing at all, and what it caps. The console terms say 'Certain Cloud Services and Models may be designated as fee-free or otherwise available without triggering a payment for a limited time or based on usage limits', which describes a fee-free tier without naming it. A signup attempt is the only route and verification holds no account.
- extras:
  - facets.class: hardware-vendor-programme
  - facets.free_tier_kind: free-browser-inference
  - facets.shape.gpu_class: Tenstorrent Wormhole / Blackhole Tensix
- evidence:
  - [1] 2026-10-22: 'No hardware yet? console.tenstorrent.com lets you run LLM inference and image and video generation in the browser, backed by Tenstorrent hardware', quoted
  - [2] 2026-10-22: 'Cloud hardware access and advanced workflows (deployments, agents) available in staged rollout', quoted
  - [3] 2026-10-22: the console answered with a login wall (200 with a sign-in page from every reader), so the allowance could not be measured
  - [4] 2026-10-22: '1-128 Wormhole Tensix Processors per instance', 'Up to 2TB memory', 'Up to 96 vCPU', no price published
  - [4] 2026-11-03: the vendor names a browser console and remote access; the remote-access protocol is not stated | capture: sha256:6c85213d0c72d10a1dba748a3d6be526f85f4b1362c32a8f3244a476f5de8aa1 | quote: Develop applications and workloads through your browser or via remote access.
  - [1] 2026-11-18: not stated | capture: sha256:ae03a761353b4d8df44483b3f611f2eda3a38306942d9a6b40f3178145501248 | quote: # Tools ## Hardware Monitoring
  - [5] 2026-11-24: the agreement describes fee-free services and models without naming a tier or price | capture: sha256:409002a0cbaca7f600baea27fe422d7884e293d65a8e7417bf784b7d3b747544 | quote: Certain Cloud Services and Models may be designated as fee-free or otherwise available without triggering a payment for a limited time or based on usage limits.
  - [1] 2026-11-24: the docs offer browser inference on Tenstorrent hardware without owning hardware | capture: sha256:ae03a761353b4d8df44483b3f611f2eda3a38306942d9a6b40f3178145501248 | quote: No hardware yet? [console.tenstorrent.com](https://console.tenstorrent.com/) lets you run LLM inference and image and video generation in the browser, backed by Tenstorrent hardware.
  - [2] 2026-11-24: the console catalogue states browser inference and staged cloud hardware access | capture: sha256:1dbb16b2b48b85fca270ce04d3af61722cf027fc06ad5ca540c364db496d596f | quote: Cloud hardware access and advanced workflows (deployments, agents) available in staged rollout.
  - [5] 2026-11-24: using the Cloud Services requires an account | capture: sha256:409002a0cbaca7f600baea27fe422d7884e293d65a8e7417bf784b7d3b747544 | quote: Customer must have an Account to use the Cloud Services and is responsible for the information it provides to create the Account
  - [5] 2026-11-24: fees, if any, are named in the console pricing page or an order form | capture: sha256:409002a0cbaca7f600baea27fe422d7884e293d65a8e7417bf784b7d3b747544 | quote: Fees are published at [console.tenstorrent.com/dashboard/pricing](https://console.tenstorrent.com/dashboard/pricing), in the Console, or specified in an Order Form.
  - [6] 2026-11-24: models.dev names an HTTP API at the console /v1 endpoint | capture: sha256:d98e52f46fe546fc08e22f802e19d6606b23a511df68f5d040f56424db462785 | quote: API https://console.tenstorrent.com/v1
  - [6] 2026-11-24: the console API is consumed as an OpenAI-compatible REST endpoint | capture: sha256:d98e52f46fe546fc08e22f802e19d6606b23a511df68f5d040f56424db462785 | quote: Package @ai-sdk/openai-compatible
  - probe:https://console.tenstorrent.com/v1 2026-11-24: the GET /v1 endpoint answered HTTP 404 on 2026-11-24 | capture: sha256:2187773f006d1519d2a98dfbf3c0902dcb044e16f2caae0728ebc4e51169982d | quote: "status": 404
- sources:
  - [1] https://docs.tenstorrent.com/tools/index.html
  - [2] https://docs.tenstorrent.com/tt-awesome/entry/tt-console/
  - [3] https://console.tenstorrent.com/
  - [4] https://tenstorrent.com/en/hardware/cloud
  - [5] https://console.tenstorrent.com/terms
  - [6] https://models.dev/providers/tenstorrent
