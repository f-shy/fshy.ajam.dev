# Coder

> coder.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coder/ | JSON https://fshy.ajam.dev/api/v1/entity/coder.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Coder

- `compute/coder` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:14.690Z (live) | stale on 2026-12-05
- url https://coder.com/pricing
- free tier: free Community plan, installed from open source: unlimited self-hosted workspaces and up to 5 active Coder Agents, with no period: "Provision unlimited self-hosted workspaces on the infrastructure you already own." | unit: unlimited | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page comparison table lists no egress or bandwidth item; traffic is that of the machines the user rents or runs | metered: no | source: [1]
- identity: email
- interface: cli, rest, ssh
- limits:
  - request-rate: up to 5 active Coder Agents on Community, unlimited on AI Premium [1]
  - write-gated (binding): the free product is self-hosted open source: the user supplies the machines, so there is no hosted capacity to rent. [1]
- interface detail: web UI, the coder CLI (including coder ssh) and a REST API of the server the user installs and runs
- tooling: the user installs and runs the open-source Coder Community server on a rented or free machine, and it provisions the workspaces on rented or free machines as well
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and compares a free open-source Community column against two paid ones. The free product is software for the user's own hardware, not hosted compute.
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: workspaces are a user's own; the page states no clock and Community has no agent cap on workspaces
  - free_tier_kind: allowance
  - ps.price: a user's own storage
  - ps.durability: a user's own infrastructure
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: as long as the host exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Provision unlimited self-hosted workspaces on the infrastructure you already own' and the plan table's 'Community (install open source)' column with 'Up to 5 Active Coder Agents' and 'Unlimited workspaces', quoted
  - [1] 2026-10-30: the free Community plan provisions unlimited self-hosted workspaces, with no period stated | capture: sha256:be2ca22eb89eff7552c3e01f163ee439ae3f31af4cb0961beefdda2590f50a41 | quote: Provision unlimited self-hosted workspaces on the infrastructure you already own.
  - [1] 2026-10-30: Community allows up to 5 active Coder Agents | capture: sha256:be2ca22eb89eff7552c3e01f163ee439ae3f31af4cb0961beefdda2590f50a41 | quote: | Active Coder Agents | Up to 5 | Up to 5 | Unlimited |
  - [1] 2026-11-03: the platform is operated through a web UI, a CLI and a REST API | capture: sha256:8d08d3273dafce4bbf9ca8950f8972fa73698d182052aa585558fdee80dda88e | quote: | Web UI, CLI, REST API |
  - [2] 2026-11-03: the CLI has an ssh command that opens a shell in a workspace | capture: sha256:fc6d8ec0cd288cb3c6145e542419aa0db837acadb1502a38b876791e1acdf31f | quote: | [`ssh`](https://coder.com/docs/reference/cli/ssh/) | Start a shell into a workspace or run a command |
- sources:
  - [1] https://coder.com/pricing
  - [2] https://coder.com/docs/reference/cli
