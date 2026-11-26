# machine0

> machine0.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/machine0/ | JSON https://fshy.ajam.dev/api/v1/entity/machine0.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## machine0

- `compute/machine0` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:17:40.889Z (live) | stale on 2026-12-26
- url https://machine0.io/
- free tier: no free tier: pay-as-you-go billed per minute, CPU VMs from $0.013/hr, the smallest `small` VM being 1 vCPU, 1 GB RAM and 25 GB disk at $0.013/hr (~$9/month); suspend freezes a VM's state, stops billing and resumes later | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: A suspended VM keeps its disk image and bills USD 0.078 per GB-month while suspended; unused credits are refundable; no deletion clock is published. | source: [1]
- egress: Each VM has a dedicated public IP and HTTPS at <vm>.mac0.io; no egress volume allowance or price is published. | metered: no | source: [1]
- identity: email | detail: Authentication is browser OAuth with a session token; funds are added through Stripe with a USD 5 minimum; the OAuth provider's identity fields are not published.
- interface: cli, ssh
- limits:
  - request-rate (binding): $0.013 an hour for the smallest VM, up to $0.208 for xxl at 8 vCPU and 16 GB [1]
  - retention-clamped: a VM stays on unless stopped or suspended; suspend freezes state and stops compute billing while image storage bills USD 0.078 per GB-month [1]
  - per-object-cap: GPUs run from $0.836 an hour up to eight H200s on one VM [1]
- limits note: A VM stays on unless stopped or suspended; suspend freezes state and stops compute billing while image storage bills USD 0.078 per GB-month.
- interface detail: CLI and SSH: every operation is a CLI command with --json; machine0 ssh my-vm; HTTPS at <vm>.mac0.io.
- tooling: machine0 CLI installed by https://machine0.io/install.sh; remote MCP server; NixOS or Ubuntu images.
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the VM ladder, per-minute billing and the suspend behaviour. There is no free tier, so the verdict moves to paid-only, and suspend-stops-billing is the keeper cost
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: first-party: very operation is a CLI command with --json . A remote MCP server lets agents drive everything programmaticall
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 1
  - shape.disk: 25
  - shape.note: small at $0.013 an hour; GPUs including H100, H200, L40S, MI300X and RTX Ada are optional per VM
  - session_cap.restart_required: no
  - session_cap.note: VMs remain on unless stopped or suspended: the default is no reap, and suspend is a user action
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.gib: 25
  - ps.price: included in the VM size
  - ps.durability: VM disk, frozen on suspend
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.ports: dedicated resources with static IPs
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'VMs remain on unless stopped or suspended.' and 'Start, Suspend, Snapshot & Resume: Freeze a VM's state, stop billing, restore later. Create golden images from any VM and spin up clones.' with the ladder: 'small 1 vCPU 1 GB 25 GB $0.013/hr ~$9/month' to 'xxl 8 vCPU 16 GB 320 GB $0.208/hr', quoted
  - [1] 2026-11-25: the pricing table states the smallest paid VM's shape and per-hour price | capture: sha256:fa017346ccce8ac1ac196a8561174ff306ab2a91f75022dbd2e5e5f6a3c920e5 | quote: | `small` | 1 vCPU | 1 GB | 25 GB | $0.013 | $9 |
  - [1] 2026-11-24: the entry CPU and GPU hourly prices | capture: sha256:fa017346ccce8ac1ac196a8561174ff306ab2a91f75022dbd2e5e5f6a3c920e5 | quote: CPU VMs from $0.013/hr. GPU VMs from $0.836/hr, up to 8x H200.
  - [1] 2026-11-24: the platform is driven by a CLI with JSON output and a remote MCP server | capture: sha256:fa017346ccce8ac1ac196a8561174ff306ab2a91f75022dbd2e5e5f6a3c920e5 | quote: Every operation is a CLI command with `--json`. A remote MCP server lets agents drive everything programmatically.
  - [2] 2026-11-24: the quickstart uses SSH to reach a VM | capture: sha256:7e81adea6fb02b25fa674eec339d995e5762412690a5ea9f2ed1d41cd949bc23 | quote: machine0 ssh my-vm
  - [1] 2026-11-24: suspension stops compute billing, image storage has a per-GB-month rate and the minimum top-up is USD 5 | capture: sha256:fa017346ccce8ac1ac196a8561174ff306ab2a91f75022dbd2e5e5f6a3c920e5 | quote: Suspend VMs to stop billing. You pay only for image storage ($0.078/GB/month) while suspended. Minimum top-up $5. Unused credits are refundable.
  - [1] 2026-11-24: each VM has a public IP and an HTTPS endpoint | capture: sha256:fa017346ccce8ac1ac196a8561174ff306ab2a91f75022dbd2e5e5f6a3c920e5 | quote: Every VM gets a public IP and HTTPS at `<vm>.mac0.io`. No NAT, no tunnels.
  - [3] 2026-11-24: authentication uses a browser OAuth login | capture: sha256:8523b8d4d3580e8d798b493678db8a8c53ff2b811684dde86ad67cd8ea5cc998 | quote: Log in via browser OAuth. Session token stored at `~/.machine0/auth-token`.
- sources:
  - [1] https://machine0.io/
  - [2] https://docs.machine0.io/introduction/quickstart
  - [3] https://docs.machine0.io/cli/account.md
