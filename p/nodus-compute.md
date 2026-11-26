# Nodus Compute

> nodus-compute.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nodus-compute/ | JSON https://fshy.ajam.dev/api/v1/entity/nodus-compute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nodus Compute

- `compute/nodus-compute` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T15:40:40.205Z (live) | stale on 2026-12-26
- url https://www.nodus-compute.ai/pricing/
- free tier: no free tier: six CPU and memory sizes from $0.0075 to $0.1054, each with an included disk, and a GPU table the page loads on demand | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: Finished Jobs are kept for 30 days so their logs and outputs can be read, then deleted. Research capacity is on-demand and interruptible; local scratch is erased when a node is released or reclaimed. | days: 30 | source: [1]
- egress: not published | metered: no | source: [1]
- identity: card | detail: The install guide states 'Verify your email and card in the console before creating an organization. Card verification does not collect a payment or turn on auto-recharge.' Sign-in accepts a browser session, GitHub, Google or a device code; email verification is required for new accounts.
- interface: cli, rest
- limits:
  - request-rate (binding): $0.0075 for 1 vCPU and 1 GiB up to $0.1054 for 4 vCPU and 16 GiB [1]
  - per-object-cap: included disk ranges from 25 GB at the smallest size to 160 GB at 4 vCPU and 8 GiB [1]
- interface detail: CLI (`nodus`), Python SDK and an API-key-authenticated HTTP API; browser sign-in with GitHub, Google or a device code.
- tooling: the user installs and runs the `nodus` CLI (pip `nodus-compute`, Homebrew or a standalone binary) or uses the Python SDK
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes the six CPU shapes with supply-side rates and included disk. There is no free tier, so the record's USD 30 credit is not established and the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 1
  - shape.disk: 25
  - shape.note: the smallest of six CPU/RAM sizes; the GPU table is loaded by script and was not read
  - session_cap.restart_required: no
  - session_cap.note: supply-side pricing; the page states no clock
  - free_tier_kind: none
  - ps.gib: 25
  - ps.price: included disk per size
  - ps.durability: included disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '| 1 vCPU | 1 GiB | 25 GB | $0.0075 |' through '| 4 vCPU | 16 GiB | 64 GiB | $0.1054 |' with the note 'These six CPU/RAM sizes have nominal Modal equivalents', quoted
  - [2] 2026-11-24: organization creation requires a verified email and a card | capture: sha256:1162b7408fad00e684e502e6507bbeafadac1f8c642e1bf639bb1c75963fc2cc | quote: Verify your email and card in the console before creating an organization. Card verification does not collect a payment or turn on auto-recharge.
  - [2] 2026-11-24: email and card verification, with no payment collected by verification, is the sign-up gate | capture: sha256:1162b7408fad00e684e502e6507bbeafadac1f8c642e1bf639bb1c75963fc2cc | quote: Verify your email and card in the console before creating an organization. Card verification does not collect a payment or turn on auto-recharge.
  - [2] 2026-11-24: the service provides an installable CLI | capture: sha256:1162b7408fad00e684e502e6507bbeafadac1f8c642e1bf639bb1c75963fc2cc | quote: The `nodus` CLI is one self-contained binary for macOS, Linux and Windows on x86-64 and ARM64. Pick one way to install it.
  - [2] 2026-11-24: the service uses browser sign-in and API keys through a CLI | capture: sha256:1162b7408fad00e684e502e6507bbeafadac1f8c642e1bf639bb1c75963fc2cc | quote: Your browser opens to confirm the sign-in. If you belong to several orgs, pick the ones this machine should use: the CLI stores one API key per org in the OS keychain
  - [2] 2026-11-24: the CLI is installed by the user as a Python package | capture: sha256:1162b7408fad00e684e502e6507bbeafadac1f8c642e1bf639bb1c75963fc2cc | quote: pip install nodus-compute
  - [3] 2026-11-24: artifacts are retrievable for 30 days after termination | capture: sha256:49e8bfb257fb26f5009d83f104a63722815b9aa67bb5e86572575710d9cc9524 | quote: After termination you have 30 days to retrieve artifacts and checkpoints, after which we may delete them.
  - [3] 2026-11-24: the artifact retrieval window is 30 days | capture: sha256:49e8bfb257fb26f5009d83f104a63722815b9aa67bb5e86572575710d9cc9524 | quote: After termination you have 30 days to retrieve artifacts and checkpoints, after which we may delete them.
  - [1] 2026-11-24: the pricing page still lists six CPU/RAM sizes with no free tier and no per-object cap | capture: sha256:4ee0d69b4ccd88ada1ddb52002b8fe1a567a730d34ebccb32288548832a6d34b | quote: These six CPU/RAM sizes have nominal Modal equivalents.
  - [1] 2026-11-25: the page was read on 2026-11-25 and still states this value | capture: sha256:4ee0d69b4ccd88ada1ddb52002b8fe1a567a730d34ebccb32288548832a6d34b | quote: | 4 vCPU | 16 GiB | 64 GiB | $0.1054 | | |
- sources:
  - [1] https://www.nodus-compute.ai/pricing/
  - [2] https://nodus-compute.ai/docs/getting-started/authentication/
  - [3] https://www.nodus-compute.ai/terms/
