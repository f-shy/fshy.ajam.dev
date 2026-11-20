# InstaBox

> instabox.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/instabox/ | JSON https://fshy.ajam.dev/api/v1/entity/instabox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InstaBox

- `compute/instabox` | qualifies-with-caveat | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:43:14.343Z (live) | stale on 2026-12-05
- url https://instabox.sh/changelog
- free tier: 'Free gives you one 4 vCPU / 8 GiB machine to run every month at no cost', quoted, with 5 snapshots, the standard agent-browser template, auto-pause after 30 idle minutes, and the 2 vCPU / 4 GiB or 4 vCPU / 8 GiB sizes allowed. Pro is USD 20 a month and Team USD 500, each including usage equal to its fee. Accounts created before 2026-10-20 keep five free machines until 2026-12-01 | unit: hours | metered on: wall-clock | read on: 2026-10-20 | source: [1] | note: perpetual-monthly
- per-object cap: not applicable | source: [1]
- retention: The five-machine grant is a legacy state with a printed end date of 2026-12-01, so the 20 vCPU / 40 GiB figure that circulated in October 2026 expires in six weeks and the steady state is 4 vCPU / 8 GiB. | source: [1]
- egress: Free plan: 100 GiB of egress a month, then USD 0.02 per GiB; ingress is free. Separately, a machine's upload is capped at about 50 Mbit/s per VM. | metered: yes | free allowance: 100 GiB a month on the Free plan (Pro 1 TiB, Builder 5 TiB, Team 50 TiB) | price per TB: USD 0.02 per GiB beyond the allowance (USD 20.48 per TiB) | source: [1]
- identity: email
- interface: rest, cli, ssh
- limits:
  - retention-clamped (binding): auto-pause after 30 idle minutes on the free plan [1]
  - volume-quota: one machine on the free plan, 4 vCPU / 8 GiB, the only size [1]
  - retention-clamped (binding): accounts created before 2026-10-20 keep five free machines only until 2026-12-01 [1]
- limits note: The five-machine grant is a legacy state with a printed end date of 2026-12-01, so the 20 vCPU / 40 GiB figure that circulated in October 2026 expires in six weeks and the steady state is 4 vCPU / 8 GiB.
- binding note: auto-pause after 30 idle minutes binds first: a free machine stops on any job that goes quiet for half an hour, and the five-machine legacy grant that circulated in the Chinese forums ends on 2026-12-01
- interface detail: HTTP API with an API key, the instabox CLI, SSH through a gateway (certificate or SSH token), a TypeScript SDK (@insforge/instabox-sdk), an MCP server and a web dashboard
- tooling: the instabox CLI and the TypeScript SDK @insforge/instabox-sdk (npm), authenticated with an API key (INSTABOX_API_KEY)
- composes with: One 4 vCPU / 8 GiB machine with persistent files and snapshots is a place to hold a working set between sessions, which a notebook that resets does not give.
- reliability: no reliability event recorded
- notes: Instabox provides isolated container environments.
- extras:
  - facets.class: enforcement
  - facets.free_tier_kind: perpetual-monthly
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 8
- evidence:
  - [1] 2026-10-20: quoted: 'Free gives you one 4 vCPU / 8 GiB machine to run every month at no cost'; 'Accounts created before October 20 keep five free machines until December 1'; Free sizes are 2 vCPU / 4 GiB and 4 / 8
  - [2] 2026-10-22: the vendor's own free-tier explanation: 'we pause it after 30 minutes of inactivity' and 'Is there a usage limit on the free machine? No. Use it as much as you want'
  - [3] 2026-10-01: the circulating five-machine figure, translated: 'up to 5 machines free, each 4 vCPU and 8GB', during an invite-only beta [date precision: month precision]
  - [4] 2026-10-01: a user who received an invite after 48 hours found the 8 GiB plan could not be created and took the 4 GiB plan instead, and reports the running limit as 30 minutes [date precision: month precision]
  - [5] 2026-10-22: quoted: Free is USD 0 with 1 machine, 4 vCPU / 8 GiB, 5 snapshots
  - [6] 2026-10-22: quoted: a real virtual machine with its own kernel and root, Docker and Docker Compose run inside, persistent storage, any port gets an HTTPS URL, pause and resume
  - [7] 2026-10-20: reported, translated: 4 vCPU / 8 GB RAM, a full Linux environment with root, Docker support, one machine per account, paused after 30 minutes idle with session state kept, and an invite code from a waitlist of up to about 48 hours
  - [8] 2026-11-04: the free plan includes 100 GiB of egress a month, then USD 0.02 per GiB | capture: sha256:91f8ebecd50c8f6b346eb21045aabde8bb78bf5becb7e1d38325d9475a33a88b | quote: | Egress | Free: 100 GiB, Pro: 1 TiB, Builder: 5 TiB, Team: 50 TiB a month, then $0.02 per GiB |
  - [9] 2026-11-04: the TypeScript SDK, HTTP, the CLI and SSH are access interfaces; the dashboard is the console | capture: sha256:7da86e2bc7a933d45c9014163d76a782464776afd4f35080ba238b7b5ce85686 | quote: Code uses an API key (`ibk_...`): the TypeScript SDK, plain HTTP, the CLI and SSH all accept one.
  - [8] 2026-11-04: per-VM upload cap, separate from the monthly egress allowance | capture: sha256:91f8ebecd50c8f6b346eb21045aabde8bb78bf5becb7e1d38325d9475a33a88b | quote: What a machine sends is capped at about 50 Mbit/s (~6 MB/s), with little or no burst
  - [8] 2026-11-04: the free plan has a single machine size | capture: sha256:91f8ebecd50c8f6b346eb21045aabde8bb78bf5becb7e1d38325d9475a33a88b | quote: | Machine size | 4 vCPU / 8 GiB by default, the only size on the free plan.
  - [9] 2026-11-04: SDK, CLI, HTTP and SSH are documented clients | capture: sha256:7da86e2bc7a933d45c9014163d76a782464776afd4f35080ba238b7b5ce85686 | quote: Code uses an API key (`ibk_...`): the TypeScript SDK, plain HTTP, the CLI and SSH all accept one.
- sources:
  - [1] https://instabox.sh/changelog
  - [2] https://instabox.sh/blog/instabox-pricing
  - [3] https://www.uupc.cn/instabox-free-beta-five-cloud-vms/
  - [4] https://aijp.jizhiku.net/archives/21208
  - [5] https://instabox.sh/pricing
  - [6] https://instabox.sh/
  - [7] https://www.nodeseek.com/post-997124-1
  - [8] https://instabox.sh/docs/limits.md
  - [9] https://instabox.sh/docs/keys-sdk.md
