# Goose

> goose-docs.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/goose-docs/ | JSON https://fshy.ajam.dev/api/v1/entity/goose-docs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Goose

- `compute/goose` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:53:22.456Z (live) | stale on 2026-12-05
- url https://goose-docs.ai/
- free tier: not stated: https://goose-docs.ai/ prints no allowance, quota or price; goose is open-source software that "runs on your machine" and sends model calls to a provider the user configures | unit: none | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: free-product
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous
- interface: rest, cli
- limits note: the vendor serves no inference, so nothing binds on its side; the cost is the endpoint key and the machine it runs on.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the user installs and runs the goose desktop app (macOS, Linux, Windows) or the goose CLI on a rented or free machine, and configures a model provider with an API key or an existing subscription
- composes with: the CLI and the API mean the agent can run on a free remote machine while the model comes from a separate free inference lane, which is the composition this class exists for.
- reliability: no reliability event recorded
- notes: Not a subscription: goose is a free open-source general-purpose agent whose project sells no plan, price or hosted inference; models come from a hosted provider the user configures (15 or more providers, or an existing Claude, ChatGPT or Gemini subscription), and the agent itself runs on a machine the user supplies. A candidate for coding-subs beside the other bring-your-own-key agents; no coding-subs record holds it. The docs moved from block.github.io/goose to goose-docs.ai. The desktop app and the CLI both run on a machine the user supplies. The project now lives under an aaif-goose GitHub organisation, not under block.
- self hosted: yes
- extras:
  - facets.class: free-standing-agent
  - facets.free_tier_kind: free-product
- evidence:
  - [1] 2026-10-22: "Your native open source AI agent. Desktop app, CLI, and API" with 55k+ GitHub stars and "Works with 15+ providers", quoted
  - [2] 2026-10-22: the install page offers a desktop download for macOS, Linux and Windows plus a CLI, quoted
  - [1] 2026-10-30: goose is software that runs on the user's machine; the page states no allowance, quota or price | capture: sha256:430bb2c0c4a20efad84cd3a28d7240cd84aec98596e6f8343b8a140018f8af96 | quote: goose is a general-purpose AI agent that runs on your machine.
  - [1] 2026-10-30: goose ships as a desktop app, a CLI and an embeddable API | capture: sha256:430bb2c0c4a20efad84cd3a28d7240cd84aec98596e6f8343b8a140018f8af96 | quote: A native desktop app for macOS, Linux, and Windows. A full CLI for terminal workflows. An API to embed it anywhere.
  - [1] 2026-11-03: goose takes models from 15 or more providers or from an existing subscription | capture: sha256:9ae27f0e61c2c274e58ddffd6cc29376d1f1237684b2f069c8748b4cdd529ea2 | quote: Works with 15+ providers — Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, and more. Use API keys or your existing Claude, ChatGPT, or Gemini subscriptions via ACP.
  - [1] 2026-11-03: goose is agent software that runs on the user's machine | capture: sha256:9ae27f0e61c2c274e58ddffd6cc29376d1f1237684b2f069c8748b4cdd529ea2 | quote: goose is a general-purpose AI agent that runs on your machine. Not just for code
  - [1] 2026-11-04: goose is software that runs on the user's machine; the page states no allowance, quota or price | capture: sha256:897250836b7d75e15b7e16a2ea57308a4926891d40f9cf0476037a1cc8f3db19 | quote: goose is a general-purpose AI agent that runs on your machine.
- sources:
  - [1] https://goose-docs.ai/
  - [2] https://goose-docs.ai/docs/getting-started/installation/
