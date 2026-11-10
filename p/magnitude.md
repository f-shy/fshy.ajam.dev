# Magnitude

> magnitude.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/magnitude/ | JSON https://fshy.ajam.dev/api/v1/entity/magnitude.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Magnitude

- `compute/magnitude` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category browser host
- needs card no, phone unknown, ID no, institution no | verified 2026-11-06T17:42:10.984Z (live) | stale on 2026-12-07
- url https://magnitude.dev/
- free tier: the open-source engine is a free download that runs on the user's own hardware | unit: none | metered on: wall-clock | read on: 2026-10-29 | source: [1] | note: read from the vendor site
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the page read states no egress allowance and no overage price per TB | metered: no | source: [1]
- identity: anonymous | detail: none: the download page serves the desktop app and the CLI directly and the install script runs without a key. The site states 'no token costs, nothing leaves your machine', and no card is asked for on the download path. The phone requirement is not published on https://magnitude.dev/download. Country: not published on https://magnitude.dev/download.
- interface: rest
- limits:
  - write-gated (binding): the product is an inference engine the user runs; there is no hosted capacity to rent, and no plan to price. [1]
- interface detail: Desktop app with a local OpenAI-compatible API, plus one-click connectors for coding agents; the user installs and runs it
- tooling: the user installs and runs the desktop app; OpenAI-compatible API
- composes with: not established
- reliability: no reliability event recorded
- notes: Self-hosted: Magnitude is an open-source inference engine the user downloads and runs on their own hardware.
- evidence note: the site was read on 2026-10-22 and states the Apache 2.0 licence and that it runs on the user's own hardware. There is no hosted compute, so the free tier is the software rather than capacity.
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: any Apple Silicon, NVIDIA or AMD GPU
  - shape.gpu_count: 1
  - shape.note: no fixed minimum: a user's own hardware sets the shape
  - session_cap.restart_required: no
  - session_cap.note: runs on a user's own GPU or CPU; the session is the process and quantized KV is freed when an agent stops
  - network_out.out: no
  - network_out.in: no
  - network_out.ports: none
  - network_out.static_ip: no
  - network_out.ipv6: no
  - network_out.allowance: 'nothing leaves your machine'
  - free_tier_kind: none
  - ps.price: a user's own storage
  - ps.durability: the client's machine
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.max_retention: as long as a user keeps it
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free, private, open source: no token costs, nothing leaves your machine, Apache 2.0' and 'Any Apple Silicon, NVIDIA, or AMD GPU, or nothing but a CPU. There is no fixed minimum.' quoted
  - [1] 2026-10-29: Magnitude is an open-source inference engine the client downloads and runs on its own hardware | capture: sha256:153c033f83b1cf124d5ba11bc2c36f89167e8e51e752a45075321c2b05806fc6 | quote: Magnitude is an open source inference engine that tunes its kernels on your hardware to find the fastest way to run each model.
  - [1] 2026-10-29: Magnitude is an open-source inference engine the user downloads and runs on their own hardware | capture: sha256:153c033f83b1cf124d5ba11bc2c36f89167e8e51e752a45075321c2b05806fc6 | quote: Magnitude is an open source inference engine that tunes its kernels on your hardware to find the fastest way to run each model.
  - [1] 2026-11-03: software the user installs and runs; no egress is metered or priced | capture: sha256:153c033f83b1cf124d5ba11bc2c36f89167e8e51e752a45075321c2b05806fc6 | quote: Free, private, open source: no token costs, nothing leaves your machine, Apache 2.0
  - [1] 2026-11-03: a local OpenAI-compatible API is exposed | capture: sha256:153c033f83b1cf124d5ba11bc2c36f89167e8e51e752a45075321c2b05806fc6 | quote: Anything else works through the OpenAI-compatible API.
  - [2] 2026-11-04: the installers are served to anyone, with no account or key on the download page | capture: sha256:94490efd5a82752d76af7cb308110a794de9a5945f46f4a42d44c740e67120e2 | quote: Either way you get the desktop app and the CLI.
  - [2] 2026-11-06: the desktop app and the CLI are served from the download page with no account | capture: sha256:94490efd5a82752d76af7cb308110a794de9a5945f46f4a42d44c740e67120e2 | quote: Either way you get the desktop app and the CLI.
- sources:
  - [1] https://magnitude.dev/
  - [2] https://magnitude.dev/download
