# OpenHands Remote Sandbox

> openhands.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openhands/ | JSON https://fshy.ajam.dev/api/v1/entity/openhands.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenHands Remote Sandbox / Cloud

- `compute/openhands-runtime` | qualifies-with-caveat | evidence reported | binding write-gated | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:16.615Z (live) | stale on 2026-11-19
- url https://docs.openhands.dev/openhands/usage/sandboxes/remote
- free tier: not stated: https://docs.openhands.dev/openhands/usage/sandboxes/remote prints no free amount, unit or period; the page documents how to point the runtime at a remote sandbox (an API URL and an API key) and names no hosted plan or price | unit: none | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: the cited page prints no allowance and no price; it says remote sandboxes serve managed deployments such as OpenHands Cloud and self-hosted setups
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: no egress allowance or overage price on https://openhands.dev/pricing and https://docs.openhands.dev/openhands/usage/sandboxes/remote | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - write-gated (binding): the record documents a configuration switch, not a hosted service: the remote sandbox is supplied by somebody else [1]
- interface detail: API URL and API key for remote sandboxes; the OpenHands Cloud API with API keys is documented
- tooling: part of the free tier
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the documentation page was read on 2026-10-22 and explains how to point the runtime at a remote sandbox. It names no hosted service and no price, so the record's free-tier claim cannot be settled from its own URL
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the runtime can expose extra service URLs such as VS Code and app ports; the page states no clock
  - free_tier_kind: allowance
  - net.out: yes
  - net.in: yes
  - net.ports: additional service URLs may be exposed
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Run conversations in a remote sandbox environment. A remote sandbox runs the agent server in a remote execution environment instead of on your local machine.' with `export RUNTIME=remote`, quoted; the page names no hosted provider and no price
  - [1] 2026-10-30: the cited page is a configuration guide for a remote sandbox and prints no free allowance, unit or period | capture: sha256:42de761f266aab2cd99994be96699cbfc73edc573a9db49a2f1ab46e780df8cf | quote: Remote sandboxes require additional configuration (API URL + API key).
  - [1] 2026-10-30: the free tier source page was read on the date set | capture: sha256:42de761f266aab2cd99994be96699cbfc73edc573a9db49a2f1ab46e780df8cf | quote: Remote sandboxes require additional configuration (API URL + API key).
  - [1] 2026-10-30: the page describes where remote sandboxes are used and states no allowance | capture: sha256:42de761f266aab2cd99994be96699cbfc73edc573a9db49a2f1ab46e780df8cf | quote: This is typically used by managed deployments (e.g., OpenHands Cloud) and advanced self-hosted setups.
  - [1] 2026-10-30: the cited page states no free amount, so free_tier.unit none still holds | capture: sha256:42de761f266aab2cd99994be96699cbfc73edc573a9db49a2f1ab46e780df8cf | quote: This is typically used by managed deployments (e.g., OpenHands Cloud) and advanced self-hosted setups.
  - [2] 2026-10-30: the vendor pricing page lists every plan as self-hosted and names no hosted free plan | capture: sha256:221538c35dbaefa2bad2e43f4019e6980c7f9a225d5d88d23838583a395ac612 | quote: | Deployment | Local Self-hosted | Self-hosted | Self-hosted |
  - [2] 2026-11-03: the pricing page prints a session cap and no egress allowance or overage price | capture: sha256:221538c35dbaefa2bad2e43f4019e6980c7f9a225d5d88d23838583a395ac612 | quote: The Teams plan is capped at 5,000 sessions per month. Enterprise usage remains uncapped.
  - [1] 2026-11-03: remote sandboxes are reached through an API URL and an API key | capture: sha256:42de761f266aab2cd99994be96699cbfc73edc573a9db49a2f1ab46e780df8cf | quote: Remote sandboxes require additional configuration (API URL + API key).
  - [3] 2026-11-03: OpenHands Cloud offers API keys for programmatic access | capture: sha256:2fc1845c6b6663ddc36b3bc8586b512b0ecda36589fe6085f89dafbcfa0310e7 | quote: [Create API keys to work with OpenHands programmatically]
- sources:
  - [1] https://docs.openhands.dev/openhands/usage/sandboxes/remote
  - [2] https://openhands.dev/pricing
  - [3] https://docs.openhands.dev/openhands/usage/cloud/cloud-ui.md
