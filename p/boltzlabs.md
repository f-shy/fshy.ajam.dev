# BoltzLabs

> boltzlabs.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boltzlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/boltzlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BoltzLabs

- `compute/boltzlabs-sandboxes` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox | tier Free account
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.610Z (live) | stale on 2026-12-26
- url https://boltzlabs.cloud/docs/limits
- free tier: A free account includes $1 of trial usage for Small sandboxes and code execution, from the website, the CLI and the desktop app, and can run one Small sandbox at a time. A Small sandbox is 1 vCPU and 4 GB at $0.0219 an hour, so the credit is about 46 hours of a Small sandbox. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The machine rates are billed by the second out of the same monthly allowance as execution requests, RL machines, eval model use and billed storage; unused allowance does not roll over. The GitHub org profile at https://github.com/boltzlabs names boltzlabs.cloud as the site.
- per-object cap: not stated: the unit is a machine, not a stored object | source: [2]
- retention: Pausing releases compute while retaining files; storage is free for 3 days after pausing, then $0.05 per GB per month. Deleting a sandbox ends the meter and removes its files. | days: 3 | source: [2]
- egress: unverified: no egress price or allowance is published for sandboxes; a public preview URL is available for a port when the sandbox is created with internet access | metered: no | source: [2]
- identity: email | detail: The sign-up form at https://boltzlabs.cloud/login?mode=signup asks for 'name email password at least 8 characters confirm password' and offers 'continue with github'. No card, phone or identity document appears on the form. The sign-in page reads 'Sign in to create sandboxes'.
- interface: cli, rest
- limits:
  - volume-quota (binding): $1 of trial usage, about 46 hours of the Small size at $0.0219 an hour, out of a monthly allowance that does not roll over [1]
  - write-gated: free accounts run one Small sandbox at a time; Medium and Large need an active monthly subscription, with up to 25 concurrent sandboxes [1]
  - retention-clamped: paused sandbox storage is free for 3 days, then $0.05 per GB per month [2]
- limits note: Evals and recordings need an active monthly subscription. Available capacity can limit how many sandboxes a free account starts. The $10 starting price is a monthly subscription, not the price of one sandbox.
- binding note: The $1 trial credit is consumed after about 46 hours of the Small sandbox, before the one-at-a-time concurrency gate or the three-day paused-storage clock becomes the main obstacle.
- interface detail: A boltz CLI, a Python SDK and a JavaScript/TypeScript SDK create, pause, resume, fork and delete sandboxes and expose a public URL for a port; a Judge0-style execution API runs code without a sandbox to manage.
- endpoint: the boltz CLI and the Python/TypeScript SDK APIs
- tooling: curl -fsSL https://boltzlabs.cloud/cli/install.sh | sh installs the boltz binary; boltz auth login, boltz create, boltz exec and boltz connect, or the boltzlabs Python package with BOLTZLABS_API_KEY.
- composes with: A Small sandbox at $0.0219 an hour runs Python commands and a public preview port for an agent; pausing keeps its workspace for $0.05 per GB a month after three days, and the execution API handles one-off code without provisioning a machine.
- reliability: Available capacity can limit how many sandboxes start, and spot-like capacity is not described on the pages read. An active monthly subscription is required for evals and recordings; when paused sandboxes pass three days, storage bills from the allowance.
- notes: The $1 trial allowance is smaller than the operator list's 36 hours: at the published $0.0219 an hour for the Small size, $1 buys about 46 hours, and only one Small sandbox may run at a time. Sign-up asks for an email and password rather than a card. GPU sandboxes are announced as 'on the way' and have no published price.
- evidence note: The free-account allowance, concurrency, machine rates, paused-storage price, API and sign-up form are read from the vendor's limits, sandbox-pricing and login pages on 2026-11-25 and quoted below. Egress is not published and is left unverified.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 4
  - shape.disk_gib: 20
  - shape.gpu_class: GPU sandboxes announced, on the way with no published price
  - billing_model: per-second active compute against a monthly allowance
  - free_tier_kind: trial-credit
  - session_cap.restart_required: no
  - session_cap.note: no session clock published; pausing releases compute and keeps files for 3 days free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: public preview URL for a port when internet is enabled
- evidence:
  - withheld 2026-11-25: the operator's list places BoltzLabs at $0.028 an hour with a 36-hour one-time free tier; a lead, not the basis for the record's values | capture: sha256:4d220f8008ed2a6126e4b7f8bc4639bd9e625605ec428846fde2bdf593cc5c95 | quote: 21. BoltzLabs → $0.028/h · billed per second
  - [1] 2026-11-25: a free account gets $1 of trial usage for Small sandboxes and code execution and can run one Small sandbox at a time | capture: sha256:c9dc0cb3c22390f8adb2f8ed5b8393116b96936a9137dd7ba575db048d33a7ff | quote: Free accounts include $1 in trial usage for Small sandboxes and code execution, from the website, the CLI and the desktop app.
  - [1] 2026-11-25: a paid subscription unlocks Medium and Large with up to 25 concurrent sandboxes, and capacity can limit starts | capture: sha256:c9dc0cb3c22390f8adb2f8ed5b8393116b96936a9137dd7ba575db048d33a7ff | quote: Active monthly subscriptions unlock Small, Medium and Large sandboxes, with up to 25 concurrent sandboxes.
  - [2] 2026-11-25: the Small size is 1 vCPU, 4 GB and 20 GB at $0.0219 an hour, billed by the second out of the monthly allowance | capture: sha256:cea216da0e09408e5b510012d2821d7e5b1e877f7522c1fd1ba036a5d94c52b2 | quote: | Small Shells, scripts, and lightweight services | 1 | 4 GB | 20 GB | $0.0219 | $0.0000061 |
  - [2] 2026-11-25: paused storage is free for 3 days, then $0.05 per GB per month | capture: sha256:cea216da0e09408e5b510012d2821d7e5b1e877f7522c1fd1ba036a5d94c52b2 | quote: Pausing releases compute while retaining files. Storage is free for 3 days, then costs $0.05 per GB per month.
  - [3] 2026-11-25: the sign-up form asks for name, email and password and offers GitHub, with no card field | capture: sha256:b6edcf93e69eaa8407f2ef227e653fc11132c9da3c488295d33b9bbbe0567b71 | quote: name email password at least 8 characters confirm password create account ▸
  - [4] 2026-11-25: the hosted sandbox supports pause, resume, fork, public port URLs and Python and CLI access | capture: sha256:a92d138585430183170fdd396d7bd5a56c827d0f4006223a094f8cb78f38840b | quote: sandbox.pause() # release CPU/RAM, keep files
  - [5] 2026-11-25: the product is a hosted sandbox service with per-second active compute and a CLI installer | capture: sha256:736e0bdb42da35215a1dc0ca313f103d0bb33d0b840f1992dd6f140c6284d03d | quote: Sandboxes for a single tool-call, workspaces that pause and resume across long agent sessions, environments built for RL rollouts, GPU sandboxes on the way
- sources:
  - [1] https://boltzlabs.cloud/docs/limits
  - [2] https://boltzlabs.cloud/docs/pricing/sandboxes
  - [3] https://boltzlabs.cloud/login?mode=signup
  - [4] https://boltzlabs.cloud/docs/sandboxes
  - [5] https://boltzlabs.cloud/
