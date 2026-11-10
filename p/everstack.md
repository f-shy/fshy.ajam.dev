# Everstack

> everstack.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/everstack/ | JSON https://fshy.ajam.dev/api/v1/entity/everstack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Everstack

- `compute/everstack` | trial-only | evidence documented | binding volume-quota | category container and VM sandbox
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T06:40:20.286Z (live) | stale on 2026-12-05
- url https://everstack.ai/pricing
- free tier: Sandbox compute bills per second at USD 0.0333 per hour for Nano (0.5 vCPU, 0.5 GiB), USD 0.0666 for Small (1 vCPU, 1 GiB), USD 0.1332 for Medium (2 vCPU, 2 GiB), USD 0.2664 for Large (4 vCPU, 4 GiB) and USD 0.5328 for XL (8 vCPU, 8 GiB). 'Every new organization receives a one-time $5 sandbox compute credit with no payment method required.' The platform plan is USD 20 a month for Build with 3 seats, USD 100 a month for Scale with 10 seats. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published for sandboxes: https://everstack.ai/pricing bills sandbox compute per second and lists no sandbox egress allowance or price; hosted-site delivery is USD 0.10 per GB of response bytes delivered to visitors | metered: no | source: [1]
- identity: email | detail: No payment method required: the pricing page states "Every new organization receives a one-time $5 sandbox compute credit with no payment method required", so there is no card and no hold; the credit is granted per organisation. The record does not state what signup asks for. An email address, a phone number or a company name. Nor whether debit or prepaid cards are accepted later, which does not arise while no payment method is taken.
- interface: rest, cli, ssh
- limits:
  - volume-quota (binding): Memory is 1 GiB per vCPU on every size, so a workload that needs 4 GiB of RAM has to buy a 4 vCPU box at USD 0.2664 per hour; the USD 5 credit is one per organization and does not renew. [1]
- limits note: Memory is 1 GiB per vCPU on every size, so a workload that needs 4 GiB of RAM has to buy a 4 vCPU box at USD 0.2664 per hour; the USD 5 credit is one per organization and does not renew.
- binding note: the same as limits note
- interface detail: REST API (OpenAI-compatible gateway and platform APIs), official Go, Python and TypeScript SDKs, a CLI, and sandbox SSH through SSH key and SSH token endpoints, documented at docs.everstack.ai
- tooling: the official Everstack Go, Python and TypeScript (Node.js) SDKs and the Everstack CLI
- composes with: The sandbox sizes line up with the whole platform: the same account supplies an AI gateway over 200 models, a vector memory store and the sandbox, so an agent can be built without a second vendor, and the sandbox is the only part billed by the second.
- reliability: no reliability event recorded
- notes: Rate per vCPU-hour works out to USD 0.0666 flat, which is a quarter above ix's USD 0.0288 and double Bunny's USD 0.02, and the RAM ratio is the reason: 1 GiB per vCPU is tight for a build that compiles anything. The USD 5 credit at USD 0.0666 per hour is 75 hours of Small. Whether sandbox compute requires the USD 20 Build plan is not stated on the pricing page; the credit is offered to a new organization with no payment method, which implies at least a trial path without one. Isolation technology not read. Documentation exposes an llms.txt and an OpenAPI index, so the API surface is testable without a browser.
- extras:
  - facets.class: platform-with-sandbox
  - facets.free_tier_kind: one-time-credit
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
- evidence:
  - [1] 2026-10-22: sandbox compute per second: Nano USD 0.0333 per hour at 0.5 vCPU and 0.5 GiB, Small USD 0.0666 at 1/1, Medium USD 0.1332 at 2/2, Large USD 0.2664 at 4/4, XL USD 0.5328 at 8/8
  - [1] 2026-10-22: 'Every new organization receives a one-time $5 sandbox compute credit with no payment method required'
  - [1] 2026-10-22: Build USD 20 per month with 3 seats, Scale USD 100 per month with 10 seats, hosted browser sessions USD 0.05 per browser hour with a 1 minute minimum
  - [2] 2026-10-22: the sandbox backend is selectable between docker and kubernetes, with defaults of max_cpu 4.0 and max_memory_mb 4096
  - [1] 2026-11-03: only hosted-site delivery has a transfer price; no sandbox egress allowance or price is published | capture: sha256:736b19635ef8063aa58241677d690118f074a9065937b3df53b60eaf250988fc | quote: | Site data transfer | $0.10 per GB | Response bytes delivered to visitors |
  - [3] 2026-11-03: the REST API has sandbox SSH token endpoints | capture: sha256:81318e1ce7aee651c7294d384fc4a8d7993230ee9abae975a958d86ab624912f | quote: - [POST Create Sandbox SSHToken](https://docs.everstack.ai/api-reference/agents/create-sandbox-sshtoken)
  - [3] 2026-11-04: REST API reference | capture: sha256:81318e1ce7aee651c7294d384fc4a8d7993230ee9abae975a958d86ab624912f | quote: - [API Reference](https://docs.everstack.ai/api-reference): Everstack REST API reference — OpenAI-compatible gateway and platform APIs.
  - [3] 2026-11-04: official Python SDK | capture: sha256:81318e1ce7aee651c7294d384fc4a8d7993230ee9abae975a958d86ab624912f | quote: - [Python](https://docs.everstack.ai/sdks/python): Official Everstack Python SDK with sync and async clients.
  - [3] 2026-11-04: official Go SDK | capture: sha256:81318e1ce7aee651c7294d384fc4a8d7993230ee9abae975a958d86ab624912f | quote: - [Go](https://docs.everstack.ai/sdks/go): Official Everstack Go SDK with streaming support and typed responses.
  - [3] 2026-11-04: official TypeScript SDK | capture: sha256:81318e1ce7aee651c7294d384fc4a8d7993230ee9abae975a958d86ab624912f | quote: - [TypeScript / Node.js](https://docs.everstack.ai/sdks/typescript): Official Everstack Node.js SDK for gateway and platform APIs.
  - [3] 2026-11-04: a CLI exists | capture: sha256:81318e1ce7aee651c7294d384fc4a8d7993230ee9abae975a958d86ab624912f | quote: - [Get Started](https://docs.everstack.ai/getting-started/installation): Sign up for Everstack Cloud and install the CLI.
- sources:
  - [1] https://everstack.ai/pricing
  - [2] https://docs.everstack.ai/getting-started/configuration/
  - [3] https://docs.everstack.ai/llms.txt
