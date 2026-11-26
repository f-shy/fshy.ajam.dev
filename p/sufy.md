# SUFY Sandbox

> sufy.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sufy/ | JSON https://fshy.ajam.dev/api/v1/entity/sufy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SUFY Sandbox

- `compute/sufy-sandbox` | paid-only | evidence documented | binding volume-quota | category sandbox | tier Pay as you go
- identity a placeholder: card and phone unknown | verified 2026-11-25T11:55:06.337Z (live) | stale on 2026-12-26
- url https://developer.sufy.com/compute-service/sandbox/overview
- free tier: No free compute hours are stated: each sandbox gets 20 GiB of local storage free of charge, persistent storage has a 10 GiB per account per month free tier, and network traffic is currently not billed separately. | unit: GiB | metered on: stored-bytes | read on: 2026-11-25 | source: [1]
- per-object cap: not applicable: the storage limit is a 20 GiB local disk per sandbox and a 10 GiB monthly persistent-storage allowance, not one object's size
- retention: Persistent storage billed hourly keeps templates and snapshots until deleted; billing continues when the sandbox is not running until the data is deleted. | source: [1]
- egress: Network traffic is currently not billed separately; sandboxes can make HTTP requests and database connections. | metered: no | source: [1]
- identity: email | detail: unverified: an account is required, but no captured Sufy page states what registration asks for; the sign-up page (sufy.com/home) is a login wall and a JavaScript shell that every route failed to read, so email is a placeholder rather than an observed requirement
- interface: rest, cli
- limits:
  - volume-quota (binding): 10 GiB of persistent storage per account per month free, then $0.00002727 per GiB-hour [1]
  - volume-quota (binding): 20 GiB of local storage per sandbox free of charge; memory is configurable from 512 MiB to 8192 MiB in 512 MiB steps and vCPU from 1 to 8 [1]
- limits note: Persistent storage is billed hourly for anything above the 10 GiB per account per month allowance, with partial hours billed as full hours. If the account is in arrears, new sandboxes cannot be created and running sandboxes are released.
- binding note: The 10 GiB monthly persistent-storage allowance is the only stated free quantity; compute is charged from the first second at $0.00000564 per core-second and $0.00000282 per GiB-second.
- interface detail: Fully compatible with the E2B SDK, with a simple SDK interface, management through command-line tools and full file-system operations including upload and download.
- endpoint: https://us-south-1-sandbox.sufyapi.com
- tooling: the official E2B SDK, a command-line tool and REST calls; Python, JavaScript/TypeScript and C++ are listed as supported languages.
- composes with: A two-vCPU, 4 GiB sandbox at $0.020304 per vCPU-hour and $0.010152 per GiB-hour runs about $0.081 an hour, and its unmetered outbound traffic and S3-compatible object storage on the same account can carry results onward.
- reliability: Running sandboxes are released when an account is in arrears and new instances cannot be created; persistent storage keeps billing until its data is deleted.
- notes: A two-vCPU, 4 GiB sandbox is about $0.081 an hour by the published per-second rates, matching the operator list. The free allowance is storage, not compute time: 20 GiB local per sandbox and 10 GiB persistent per account per month. Outbound traffic has no separate charge. Registration is account-gated but the pages read do not state what the sign-up form asks for.
- evidence note: The rates, free allowances and egress term are quoted from the vendor's own sandbox overview read on 2026-11-25; the sign-up gate is not described on the pages read, so identity detail is unverified beyond the need for an account.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 20
  - shape.note: 1 to 8 vCPU, 512 MiB to 8192 MiB memory in 512 MiB steps, 20 GiB local disk per sandbox
  - billing_model: per-second for vCPU and memory, hourly for persistent storage above 10 GiB
  - free_tier_kind: recurring-storage-allowance
  - term: monthly persistent-storage allowance; compute is usage-based
  - price_arithmetic: $0.00000564 per core-second is $0.020304 per vCPU-hour; $0.00000282 per GiB-second is $0.010152 per GiB-hour; 2 vCPU plus 4 GiB is $0.081216 an hour
  - derived: 2 x $0.020304 per vCPU-hour + 4 x $0.010152 per GiB-hour = $0.081216 per hour, about the $0.081 per hour in the operator list
  - network_out.allow_outbound: yes
  - network_out.ports: outbound HTTP and database connections are documented; no inbound port terms are stated
  - session_cap.restart_required: no
  - session_cap.note: pause and resume preserve the file system and process state; billing stops when the sandbox stops
- evidence:
  - [1] 2026-11-25: the sandbox is pay-as-you-go, billed per second, and billing stops when the sandbox stops | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: The Sandbox Service uses a pay-as-you-go model with per-second billing. Billing stops as soon as the sandbox stops running.
  - [1] 2026-11-25: a vCPU costs $0.00000564 per core-second and is configurable from 1 to 8 cores | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: | vCPU | $0.00000564/core/second | Billed linearly based on the actual number of allocated vCPU cores, ranging from 1 to 8 cores. |
  - [1] 2026-11-25: memory costs $0.00000282 per GiB-second, in 512 MiB steps from 512 MiB to 8192 MiB | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: | Memory | $0.00000282/GiB/second | Memory must be configured in multiples of 512 MiB, ranging from 512 MiB to 8192 MiB. |
  - [1] 2026-11-25: one vCPU is $0.020304 an hour and $0.487296 a day | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: | 1 vCPU | $0.020304 | $0.487296 |
  - [1] 2026-11-25: one GiB of memory is $0.010152 an hour and $0.243648 a day | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: | 1 GiB Memory | $0.010152 | $0.243648 |
  - [1] 2026-11-25: each sandbox is allocated 20 GiB of local storage free of charge | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: Each sandbox is automatically allocated 20 GiB of local storage space, which is free of charge.
  - [1] 2026-11-25: persistent storage has a 10 GiB per account per month free tier | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: | Free Tier | 10 GiB per account per month |
  - [1] 2026-11-25: excess persistent storage is $0.00002727 per GiB-hour | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: | Excess Usage | $0.00002727/GiB/hour |
  - [1] 2026-11-25: network traffic is not billed separately | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: Network traffic is currently not billed separately.
  - [1] 2026-11-25: running sandboxes are released when the account is in arrears | capture: sha256:15661c8595c75739a635e6ed8c5c64a116550526447c3bbca4977a544d6a5d36 | quote: If your account is in arrears, you will not be able to create new sandbox instances, and running sandboxes will be released.
  - [2] 2026-11-25: the quick start requires creating an account before using services | capture: sha256:94c0eb3224e2fecc2c16aafe9cb605cb3c4aebb660735d554ee3d4326c38f0be | quote: 1. Create an account
  - [3] 2026-11-24: the sandbox service bills per second and stops billing when the sandbox stops | capture: sha256:6aa598f2b0d15e08d90f2e27bc503466d25333033e9cb74b73d42a8ef94cd588 | quote: The Sandbox Service uses a pay-as-you-go model with per-second billing. Billing stops as soon as the sandbox stops running.
  - [3] 2026-11-24: vCPU is USD 0.00000564 per core-second for 1 to 8 cores | capture: sha256:6aa598f2b0d15e08d90f2e27bc503466d25333033e9cb74b73d42a8ef94cd588 | quote: | vCPU | $0.00000564/core/second | Billed linearly based on the actual number of allocated vCPU cores, ranging from 1 to 8 cores. |
  - [3] 2026-11-24: memory is USD 0.00000282 per GiB-second in multiples of 512 MiB up to 8192 MiB | capture: sha256:6aa598f2b0d15e08d90f2e27bc503466d25333033e9cb74b73d42a8ef94cd588 | quote: | Memory | $0.00000282/GiB/second | Memory must be configured in multiples of 512 MiB, ranging from 512 MiB to 8192 MiB. |
  - [3] 2026-11-24: 20 GiB of local storage is free and persistent storage has a 10 GiB per account per month allowance above which USD 0.00002727 per GiB-hour is charged | capture: sha256:6aa598f2b0d15e08d90f2e27bc503466d25333033e9cb74b73d42a8ef94cd588 | quote: Each sandbox is automatically allocated 20 GiB of local storage space, which is free of charge.
  - [3] 2026-11-24: network traffic is not billed separately | capture: sha256:6aa598f2b0d15e08d90f2e27bc503466d25333033e9cb74b73d42a8ef94cd588 | quote: Network traffic is currently not billed separately.
  - [4] 2026-11-24: a sandbox runs 5 minutes by default and has a 1-hour default maximum runtime | capture: sha256:4d55af2ac97da571e0da284beafdd791c05fb8e6341fe1f0aa9f53efc93d460f | quote: Default behavior: A sandbox runs for 5 minutes by default, but custom timeout settings are supported.
  - [5] 2026-11-24: the sandbox service is E2B SDK compatible with an API key and regional endpoint | capture: sha256:a35d0ff96f588e439d8e03b8fa9b7babe56e3f21fb04b3a39c379203b22580bc | quote: Note: The Sufy sandbox service is fully compatible with the E2B API, so you can use the E2B SDK directly. When using the Sufy service, configure both the `E2B_API_KEY` and `E2B_API_URL` environment variables.
  - [5] 2026-11-24: sandbox access requires an account created at the signup page | capture: sha256:a35d0ff96f588e439d8e03b8fa9b7babe56e3f21fb04b3a39c379203b22580bc | quote: If you don't already have a Sufy account, create one at the [Sufy signup page](https://sufy.com/signup).
  - [6] 2026-11-24: the signup form asks for Email, Account name, Password and a Verification code | capture: sha256:cd7490763a8a4886dced5ec8902b116155397ec4eecb32629b9c44d7cc08fb87 | quote: # Sign up for SUFY Email Account name Password Verification code
  - [7] 2026-11-24: users automatically subscribe to the FREE PLAN on first sign in and a card is added later as a payment method based on usage | capture: sha256:76cb4e84ab662b2dae0e4924cb20cbef214bbe6b8807260b9afd8221c290529c | quote: Users automatically subscribe to “FREE PLAN” the first time they sign in, and “FREE PLAN” will not charge you anything.
- sources:
  - [1] https://developer.sufy.com/compute-service/sandbox/overview
  - [2] https://developer.sufy.com/basic-concepts
  - [3] https://developer.sufy.com/compute-service/sandbox/overview.md
  - [4] https://developer.sufy.com/compute-service/sandbox/lifecycle.md
  - [5] https://developer.sufy.com/compute-service/sandbox/quickstart.md
  - [6] https://sufy.com/user/signup?redirect=https%3A%2F%2Fsufy.com%2F
  - [7] https://sufy.com/agreements/cloud-service-agreement
