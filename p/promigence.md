# Promigence

> promigence.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/promigence/ | JSON https://fshy.ajam.dev/api/v1/entity/promigence.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Promigence

- `compute/promigence` | qualifies-with-caveat | evidence documented | binding volume-quota | category agent sandbox | tier Free plan (USD 100 credit)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.751Z (live) | stale on 2026-12-26
- url https://www.promigence.ai/llms-full.txt
- free tier: USD 100 of free credit for 30 days, claimed in the browser with no card, then per-second list pricing; 20 sandboxes at once and sessions up to an hour on the Free plan. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: Credit is a USD amount spent against compute meters; the trial is time-boxed to 30 days. A separate free, one-time validity report of 1,000 episodes is offered with no card.
- per-object cap: not applicable: the unit is a sandbox, not an object | note: No per-object cap is published.
- retention: A paused sandbox is kept for 30 days; waking it starts the 30 days again. | source: [2]
- egress: Included; registries and git hosts are not metered separately. The trial caps data out at 20 GB a month. | metered: yes | free allowance: included, with a 20 GB monthly data-out cap on the trial | source: [2]
- identity: email | detail: Sign-up is invite-only: request access and Promigence emails an invite code with the credit; the console sign-up asks for that invite code. The credit is claimed in the browser with no card. The exact fields of the account form are unverified: the page shows only the invite-code step.
- interface: cli, rest, chat
- limits:
  - volume-quota (binding): USD 100 of free credit usable within 30 days; 20 concurrent sandboxes and sessions up to an hour on Free [1]
  - volume-quota (binding): 20 GB data out per month on the trial [2]
- limits note: A run is quoted before it starts and a hard spend cap pauses a sandbox that reaches it; paused time is not billed.
- binding note: The USD 100 credit with a 30-day expiry is the first allowance to run out; the 20 GB data-out cap is a separate, less likely binding limit.
- interface detail: CLI with a JSON mode, REST API, TypeScript and Python SDKs, and an MCP server; sandboxes are reached through exec, file commands and a shell.
- tooling: The user installs the promigence CLI or an SDK; the hosted service supplies and bills the sandboxes.
- composes with: A verified snapshot can be forked into many sandboxes under a spend cap, so eval, CI and coding-agent runs share one environment.
- reliability: A sandbox that fails on the vendor side before hand-over is not billed; environment failures are reported apart from task failures. Health checks cannot be starved by workload.
- notes: List $0.17 per hour for the 2 vCPU/4 GiB small tier; the trial is USD 100 of credit for 30 days with no card. Registration needs an emailed invite code, and the account form behind it was not seen.
- evidence note: Prices, free credit, egress and retention are quoted from the vendor's own reference and FAQ read on 2026-11-25; the account form behind the invite code was not seen.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.note: small tier 2 vCPU and 4 GiB; disk size not stated
  - billing_model: per-second metered with a prepaid credit trial and hard spend caps
  - free_tier_kind: time-boxed credit
  - term: 30-day trial credit
  - price_arithmetic: 2 vCPU × $0.0504 + 4 GiB × $0.0162 = $0.1656 per hour metered; $0.17 list
  - status: live; invite-only sign-up
  - network_out.allow_outbound: yes
  - network_out.per_session_bytes: 20 GB data out per month on the trial
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: one-hour session cap on the free plan; paused sandboxes kept 30 days
- evidence:
  - [2] 2026-11-25: the metered compute rates | capture: sha256:f57fc8211a6db760d39a0d348f8edef2b0b5c81de33d0cefc6ff138ed85a35a0 | quote: Metered per second at $0.0504 per vCPU-hour plus $0.0162 per GiB-hour, the market's
  - [2] 2026-11-25: the small-tier list and metered price | capture: sha256:f57fc8211a6db760d39a0d348f8edef2b0b5c81de33d0cefc6ff138ed85a35a0 | quote: | Small | 2 vCPU · 4 GiB | $0.17 per hour | $0.000046 per second ($0.1656 per hour) | A SWE-bench-class episode: clone, patch, run the failing test. Ten minutes costs about $0.03. |
  - [2] 2026-11-25: egress is included with a 20 GB monthly trial cap | capture: sha256:f57fc8211a6db760d39a0d348f8edef2b0b5c81de33d0cefc6ff138ed85a35a0 | quote: - Egress: Included. Registries and git hosts are not metered separately. The trial caps data out at 20 GB a month.
  - [2] 2026-11-25: paused-sandbox retention | capture: sha256:f57fc8211a6db760d39a0d348f8edef2b0b5c81de33d0cefc6ff138ed85a35a0 | quote: A paused sandbox is kept for 30 days, and waking it starts the 30 days again.
  - [1] 2026-11-25: the free credit, concurrency, session cap and no-card claim | capture: sha256:6b9750a8309ca069cda486c177df6abc10689159ccfbfacebd4316a1499bcbef | quote: Yes: $100 of free credit for 30 days, with 20 concurrent sandboxes and sessions up to an hour. Request access at www.promigence.ai and Promigence emails an invite code with the credit. It is claimed in the browser (console Billing, or `promigence credits claim`) with no card.
  - [3] 2026-11-25: the invite gate at sign-up | capture: sha256:8e0b48f23e9fb70d25add9ac044dd6824ef92e814d45e3d115c3aa5b1f99d6af | quote: Promigence is invite-only for now.
  - [4] 2026-11-24: the published list rate is USD 0.0504 per vCPU-hour plus USD 0.0162 per GiB-hour, billed per second | capture: sha256:30d7e96325fa5a045a1ccea812acbee10ab7140833828e75d1d9861cb684205b | quote: Metered per second at $0.0504 per vCPU-hour plus $0.0162 per GiB-hour, the market's standard list rate.
  - [4] 2026-11-24: the published per-second rates of the Small, Medium and Large sizes | capture: sha256:30d7e96325fa5a045a1ccea812acbee10ab7140833828e75d1d9861cb684205b | quote: Small | 2 vCPU · 4 GiB | $0.17 per hour | $0.000046 per second ($0.1656 per hour)
  - [4] 2026-11-24: the Free tier includes USD 100 of credit, 20 sandboxes at once and sessions of an hour, with a hard spend cap | capture: sha256:30d7e96325fa5a045a1ccea812acbee10ab7140833828e75d1d9861cb684205b | quote: 20 sandboxes at once, sessions up to an hour
  - [4] 2026-11-24: the trial caps data out at 20 GB a month while registries and git hosts are not metered separately | capture: sha256:30d7e96325fa5a045a1ccea812acbee10ab7140833828e75d1d9861cb684205b | quote: Egress: Included. Registries and git hosts are not metered separately. The trial caps data out at 20 GB a month.
  - [5] 2026-11-24: a new account runs 20 sandboxes at once for at most an hour on sizes up to 8 vCPU with 20 GB a month of data out | capture: sha256:37ca5d295aa6b36c7295778e3ccc92a04f4d89bffc83f31c002f2be82be02e9d | quote: A new account runs 20 sandboxes at once, each for up to an hour (15 minutes unless --timeout asks for more), on sizes up to large (8 vCPU), with 20 GB of data out a month.
  - [5] 2026-11-24: a paused sandbox is kept 30 days and deleted with its files at the end of that period | capture: sha256:37ca5d295aa6b36c7295778e3ccc92a04f4d89bffc83f31c002f2be82be02e9d | quote: It is kept for 30 days, and resuming it starts the 30 days again.
  - [6] 2026-11-24: sign-up takes an invite code that the vendor emails with free credit | capture: sha256:923e2cfb65fe530ae1a379af4e560b20287c40e37b8522435b78e404115f9fe5 | quote: No account yet? Sign-up takes an invite code.
  - [6] 2026-11-24: the CLI and SDK are installed by the user and the MCP server offers read-only tools and a spend cap | capture: sha256:923e2cfb65fe530ae1a379af4e560b20287c40e37b8522435b78e404115f9fe5 | quote: npm i -g promigence # the CLI, with the TypeScript SDK in the same package (needs Node.js)
  - [6] 2026-11-24: sandboxes are billed by the second while they run and paused time is not billed | capture: sha256:923e2cfb65fe530ae1a379af4e560b20287c40e37b8522435b78e404115f9fe5 | quote: A sandbox gives you your own computer to work in: run commands, install packages, edit files, start servers, and throw
  - [7] 2026-11-24: the invite code with USD 100 of free credit is claimed in a browser with no card | capture: sha256:f7f51687718675633bb380ef5d8cbcd41bda2612ec59c0117d830ed759c65998 | quote: "answer": "Request access at www.promigence.ai: Promigence emails an invite code with $100 of free credit. With the code, sign up at console.promigence.ai/signup, or with `promigence signup` from the CLI. The credit is claimed in the browser (console Billing, or `promigence credits claim`) with no card."
  - [7] 2026-11-24: sandbox SSH supports scp, sftp and port forwarding | capture: sha256:f7f51687718675633bb380ef5d8cbcd41bda2612ec59c0117d830ed759c65998 | quote: "summary": "Logs you in to a sandbox over SSH, with the key and access set up for you; `scp`, `sftp` and port forwarding with `-L` work too.
  - [8] 2026-11-24: the free credit covers a first run and there is no card to add; sign-up takes an invite code emailed by the vendor | capture: sha256:ca8aba214b8b1e8cfe10812de713f2c0d27c7787b4cc7073152ed358deab165c | quote: Sign-up takes an invite code: [request access](https://www.promigence.ai/?ref=docs#request-access), and we email you one with $100 of free credit.
- sources:
  - [1] https://www.promigence.ai/faq
  - [2] https://www.promigence.ai/llms-full.txt
  - [3] https://console.promigence.ai/signup
  - [4] https://www.promigence.ai/pricing
  - [5] https://www.promigence.ai/docs/limits
  - [6] https://www.promigence.ai/
  - [7] https://www.promigence.ai/facts.json
  - [8] https://www.promigence.ai/docs/quickstart
