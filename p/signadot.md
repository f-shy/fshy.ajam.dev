# Signadot

> signadot.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/signadot/ | JSON https://fshy.ajam.dev/api/v1/entity/signadot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Signadot

- `compute/signadot` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:18.387Z (live) | stale on 2026-12-05
- url https://www.signadot.com/
- free tier: ephemeral environments that share self-hosted cluster, so hundreds fit on one; the changed code joins an existing environment rather than standing up a copy | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://www.signadot.com/pricing and https://www.signadot.com/ state no egress allowance or overage price; billing is by sandboxes, test invocations and concurrent devboxes | metered: no | source: [1]
- identity: email
- interface: cli, rest
- limits:
  - request-rate: hundreds of ephemeral environments share one cluster; the page states no numeric cap [1]
  - write-gated (binding): the product is a control plane over self-hosted cluster, so there is no hosted compute [1]
- interface detail: Signadot CLI and API (the dashboard and API are hosted by the vendor; the operator runs in the user's Kubernetes cluster), plus an MCP server shipped with the CLI
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and describes the shared-cluster model precisely. The free tier's existence is a claim about a plan, and the page says a free Starter plan exists but does not price it here
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an environment is created on the first push and deleted when the pull request closes
  - free_tier_kind: allowance
  - ps.price: a user's own cluster storage
  - ps.durability: a user's own cluster
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.max_retention: the pull request's life
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'A Signadot ephemeral environment starts in seconds and costs a fraction of a full copy, yet behaves like an entire environment, with real services, data and queues. Hundreds share one cluster.' and 'Through the CLI or the MCP server, the changed code joins an ephemeral environment in your cluster', quoted
  - [2] 2026-11-03: the pricing page meters sandboxes, devboxes and test invocations and lists no egress allowance or overage line | capture: sha256:74ac027c589548333371b579384eb79ef10138b6783437d6c9257ae8c2279c05 | quote: Pricing is a la carte, so you can buy more sandboxes, concurrent devboxes and Test Invocations.
  - [1] 2026-11-03: a CLI and an API exist | capture: sha256:fda769404ed2768dd95f3e520ab4973c08d898903068f25a4cf3e66e2593b551 | quote: called a Sandbox in the Signadot CLI and API
  - [1] 2026-11-03: an MCP server exists | capture: sha256:fda769404ed2768dd95f3e520ab4973c08d898903068f25a4cf3e66e2593b551 | quote: The [Signadot MCP server](https://www.signadot.com/docs/integrations/mcp) connects coding agents to your Kubernetes clusters through the Model Context Protocol.
- sources:
  - [1] https://www.signadot.com/
  - [2] https://www.signadot.com/pricing
