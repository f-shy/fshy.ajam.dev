# briq

> briq.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/briq/ | JSON https://fshy.ajam.dev/api/v1/entity/briq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## briq

- `compute/briq` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox | tier Hobby, medium briq
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.630Z (live) | stale on 2026-12-26
- url https://briq.cloud/docs/cost
- free tier: EUR 10 of credits for every new account on its personal team; the Hobby plan itself is free with no monthly fee | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: Credits are prepaid and usage draws them down as it runs; a sleeping or stopped briq is not billed for compute.
- per-object cap: not applicable: the unit is a microVM with a volume, not an object; the Hobby plan holds 10 GB of disk across the whole team | source: [1] | note: Volumes start at 2 GB unless the spec sets gb; a recipe takes 1 to 5 GB.
- retention: a sleeping or stopped briq keeps its volume until the user destroys it; a disposable screen is not used here; a Hobby briq goes to sleep after its sleep window, an hour by default | source: [1]
- egress: Disk and outbound traffic are not billed today | metered: no | source: [1]
- identity: email | detail: the sign-up page offers Continue with Google or Continue with GitHub, or Name, Email and Password with a minimum of 8 characters; no phone number or ID document is asked at sign-up. The EUR 10 credits are claimed from an account; a card is needed only to run past zero credits or to use the large size
- interface: rest, cli, chat
- limits:
  - volume-quota (binding): Hobby: 5 sandboxes and services at once, 16 GB of memory across live briqs, 10 GB of disk held, pico through medium sizes only [1]
  - per-object-cap: the medium size is shared 2 vCPU and 4 GB of RAM at EUR 0.03 per hour; a briq needs credits for its first hour before it starts [1]
  - write-gated: Hobby pay-as-you-go needs a card on file; with no card the team stops at zero credits [1]
- limits note: Compute concurrency and memory are shared by every API key, CLI and MCP client in the team. A dailySpendCapCents policy limits each agent per day. An EU-based team can run large on Hobby with a card on file.
- binding note: The 5 concurrent briqs and 16 GB shared memory on Hobby bind before the EUR 10 credit, which is drawn down per second.
- interface detail: CLI, REST API and MCP; a briq MCP server at https://api.briq.cloud/mcp
- endpoint: part of interface detail
- tooling: @briq-cloud/cli with briq login and briq run sandbox, a REST API with a BRIQ_API_KEY bearer token, and MCP clients including Claude Code, Cursor, VS Code, Codex and OpenCode
- composes with: a hosted Firecracker microVM that runs a sandbox or an OCI image beside a database, with per-second billing and an idle sleep that stops compute charges
- reliability: a briq goes to sleep after its sleep window and is not billed while asleep; at zero credits running briqs stop and visits do not wake them
- notes: The operator's list quotes USD 0.035 per hour for briq at 2 vCPU and 4 GB and 333 hours free one time; the vendor's cost page quotes EUR 0.03 per hour for the medium size and EUR 10 of account credits. The amounts are in different currencies and the free allowances differ; the vendor's own figures are the ones used here.
- evidence note: the vendor's cost, quickstart and sign-up pages were read on 2026-11-25; the price and free credit come from the cost page and the sign-up gate from the sign-up page
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 2
  - billing_model: per-second while running; sleeping is not billed; prepaid euro credits with optional card
  - session_cap.idle_reap_s: 3600
  - session_cap.restart_required: no
  - session_cap.note: a briq sleeps after its sleep window, an hour by default, and wakes on the next use
  - free_tier_kind: one-time account credit
  - term: per-second
  - source_scope: the medium size is the closest published shape to 2 vCPU / 4 GB
- evidence:
  - [1] 2026-11-25: the medium briq is shared 2 vCPU and 4 GB at EUR 0.03 per hour, billed per second | capture: sha256:ee3e9323e28c1b495154bb66585920698050c7c26dd836f28c6b9873cef7caf2 | quote: | `medium` | shared 2 | 4 GB | €0.03 |
  - [1] 2026-11-25: every new account gets EUR 10 of prepaid credits on its personal team | capture: sha256:ee3e9323e28c1b495154bb66585920698050c7c26dd836f28c6b9873cef7caf2 | quote: Every new account gets €10 of credits on its personal team. Credits are prepaid; usage draws them down as it runs.
  - [1] 2026-11-25: the Hobby plan is free with 5 concurrent sandboxes, 16 GB shared memory, 10 GB disk and pico through medium sizes | capture: sha256:ee3e9323e28c1b495154bb66585920698050c7c26dd836f28c6b9873cef7caf2 | quote: | Price | Free | €20 / month | €100 / month |
  - [1] 2026-11-25: disk and outbound traffic are not billed, and a sleeping or stopped briq is not billed for compute | capture: sha256:ee3e9323e28c1b495154bb66585920698050c7c26dd836f28c6b9873cef7caf2 | quote: A sleeping or stopped briq is not billed for compute, and its volume is kept until you destroy it. Disk and outbound traffic are not billed today.
  - [2] 2026-11-25: briq is reached over CLI, REST API and an MCP server at https://api.briq.cloud/mcp | capture: sha256:6704385b216decac85f6487925d4e19a54985fcad03eabd52b3c616bd73cc95c | quote: Create an account from the [dashboard](https://briq.cloud/sign-up), then open API keys and create a key.
  - [3] 2026-11-25: sign-up offers Google, GitHub or email with name, email and password, and no phone or ID field | capture: sha256:f89a7871d41a6672bf047730d55f5bf1f31e953ccff3387a6f6958f0fd86ea6e | quote: Continue with GoogleContinue with GitHub or with email Name Email Password
  - withheld 2026-11-25: the operator's list prices briq at USD 0.035 per hour billed per second and 333 hours free one time, a reported rate about a third party and not a reading of the vendor's own page | capture: sha256:4d220f8008ed2a6126e4b7f8bc4639bd9e625605ec428846fde2bdf593cc5c95 | quote: 26. briq → $0.035/h · billed per second
  - [1] 2026-11-24: a new account gets €10 of credits and disk and outbound traffic are not billed today | capture: sha256:ee3e9323e28c1b495154bb66585920698050c7c26dd836f28c6b9873cef7caf2 | quote: Every new account gets €10 of credits on its personal team. Credits are prepaid; usage draws
  - [1] 2026-11-24: briq bills per second with published hourly rates and does not bill disk or outbound traffic | capture: sha256:ee3e9323e28c1b495154bb66585920698050c7c26dd836f28c6b9873cef7caf2 | quote: Disk and outbound traffic are not billed today.
  - [1] 2026-11-24: the small size is shared 1 vCPU and 2 GB at €0.016 an hour | capture: sha256:ee3e9323e28c1b495154bb66585920698050c7c26dd836f28c6b9873cef7caf2 | quote: | `small` | shared 1 | 2 GB | €0.016 |
  - [1] 2026-11-24: the Hobby plan is free with five concurrent sandboxes, 16 GB live memory, 10 GB disk and no always-on briqs | capture: sha256:ee3e9323e28c1b495154bb66585920698050c7c26dd836f28c6b9873cef7caf2 | quote: | Price | Free | €20 / month | €100 / month | | Included | No monthly fee | €20 of usage included every month | €100 of usage included every month | | Sandboxes & services at once | 5 | 50 | 200 | | Memory across live briqs | 16 GB | 80 GB | 256 GB |
  - [4] 2026-11-24: egress is open except outbound SMTP ports 25, 465 and 587 | capture: sha256:71f435aa81d7ff04b3af936b306f06d395708e354aafc32f0993bb2f52732d57 | quote: * Egress is open, except outbound mail (SMTP ports 25, 465, 587), which the
  - [3] 2026-11-24: sign-up accepts Google, GitHub, or a name, email and password, and the personal team starts with €10 of credits | capture: sha256:f89a7871d41a6672bf047730d55f5bf1f31e953ccff3387a6f6958f0fd86ea6e | quote: Your personal team starts with €10 of credits. Continue with GoogleContinue with GitHub or with email Name Email Password
  - [5] 2026-11-24: a briq sleeps after its window unused, keeps its disk and is not billed while asleep | capture: sha256:ae9648a0d44d099c47a2a14934f00afbf174c0e8740f3be602f376fefdb832cf | quote: Every briq has one setting that decides when it stops on its own: `sleep`. After that long without
- sources:
  - [1] https://briq.cloud/docs/cost
  - [2] https://briq.cloud/docs/getting-started
  - [3] https://briq.cloud/sign-up
  - [4] https://briq.cloud/docs/security
  - [5] https://briq.cloud/docs/concepts/lifecycle-and-sleep
