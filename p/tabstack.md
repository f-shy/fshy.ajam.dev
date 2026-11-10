# Tabstack

> tabstack.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tabstack/ | JSON https://fshy.ajam.dev/api/v1/entity/tabstack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tabstack

- `compute/tabstack` | qualifies-with-caveat | evidence reported | binding write-gated | category browser host
- needs card no, phone unknown, ID no, institution no | verified 2026-11-06T17:42:10.985Z (live) | stale on 2026-11-21
- url https://tabstack.ai/
- free tier: free tier published without a credit amount | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: an account created with an email address: the console sign-up form carries one visible field, 'type="email" name="user_signup[email_address]"'. No credit card is required: 'No. Every new account includes the 10,000 credits without one.' The phone requirement is not published on https://console.tabstack.ai/signup. Country: not published on https://console.tabstack.ai/signup.
- interface: rest, cli
- limits:
  - write-gated (binding): access is an API key with a CLI; no plan or price appears on the extracted page [1]
- interface detail: HTTP API with an OpenAPI 3.0.3 spec, TypeScript and Python SDKs and a CLI authenticated with an API key; no MCP is named on the site
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and describes a managed web API with a CLI and an API key. It publishes no plan or price in the extracted body, so the record's free-tier claim cannot be settled from it
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: one call returns a finished output; there is no session
  - free_tier_kind: allowance
  - net.out: yes
  - net.in: no
  - net.ports: an HTTP API
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'The managed web API for models that don't come with the web. One call returns finished output: a cited answer from live sources, clean Markdown or JSON matching a schema you define' with a CLI authenticated by an API key, quoted; no plan and no price in the extracted body
  - [1] 2026-11-04: the site publishes an OpenAPI 3.0.3 wire contract for its HTTP API | capture: sha256:7748631d85ca3cb04a170d7d3932ec356737876961ed13107b8c69aecf122421 | quote: - [Tabstack API OpenAPI spec (JSON)](https://tabstack.ai/openapi.json): The wire contract, OpenAPI 3.0.3
  - [1] 2026-11-04: the site lists a CLI | capture: sha256:7748631d85ca3cb04a170d7d3932ec356737876961ed13107b8c69aecf122421 | quote: - [Tabstack CLI](https://github.com/Mozilla-Ocho/tabstack-cli): tabstack-cli, authenticated with TABSTACK_API_KEY
  - [1] 2026-11-04: the site lists a TypeScript SDK | capture: sha256:7748631d85ca3cb04a170d7d3932ec356737876961ed13107b8c69aecf122421 | quote: - [Tabstack TypeScript SDK](https://www.npmjs.com/package/@tabstack/sdk): npm install @tabstack/sdk
  - [2] 2026-11-04: the sign-up form takes an email address | capture: sha256:8521234a76743a64bc2b1b028f74ef86708fb00900510cf2d834127cecdeacc9 | quote: type="email" name="user_signup[email_address]"
  - [3] 2026-11-06: a new account needs no card for its free credits | capture: sha256:0907f094e1a89e602d8d9ab24df75a4c05cc80be630ceb2c9239e10bcd482c9a | quote: No. Every new account includes the 10,000 credits without one.
  - [2] 2026-11-06: the sign-up form takes an email address and carries no card or phone field | capture: sha256:30e821cc7c5139e1ba0506f3a7cda201faa59cd4a6f1a7bb90bd6a7a6fd020cd | quote: type="email" name="user_signup[email_address]"
- sources:
  - [1] https://tabstack.ai/
  - [2] https://console.tabstack.ai/signup
  - [3] https://tabstack.ai/pricing
