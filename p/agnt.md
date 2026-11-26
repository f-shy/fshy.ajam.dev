# AGNT Sandbox

> agnt.gg | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/agnt/ | JSON https://fshy.ajam.dev/api/v1/entity/agnt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AGNT Sandbox

- `compute/agnt-sandbox` | paid-only | evidence documented | binding write-gated | category isolated VM sandbox for short jobs | tier Pay-as-you-go prepaid execution
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.836Z (live) | stale on 2026-12-26
- url https://sandbox.agnt.gg/
- free tier: no recurring free allowance is published; pay-as-you-go is 6 US cents per compute-minute after a USD 10 minimum prepaid credit, where a compute-minute is one started minute of a Small sandbox (1 vCPU, 1 GB RAM) | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: Prepaid credit persists; optional monthly plans bundle 100, 400 or 1200 compute-minutes that reset on day 1 UTC and do not roll over. Queue and provisioning time are not billed. A job under one minute costs one compute-minute.
- per-object cap: not an object-storage offer; job inputs are up to 8 root filenames combined 8 MB and each artifact export is at most 8 MB | source: [2] | note: The 8 MB figures are per transfer, not a sandbox disk cap.
- retention: exported artifacts remain after the VM is destroyed for 1 day on pay-as-you-go or Starter, 7 days on Pro and 30 days on Business; the VM itself is destroyed at job teardown | days: 1 | source: [2]
- egress: networking is offline only inside the VM, and monthly artifact downloads are 1 GB on PAYG or Starter, 5 GB on Pro and 15 GB on Business | metered: yes | free allowance: 1 GB of artifact downloads a month on PAYG and Starter | source: [2]
- identity: email | detail: the docs say to create the Sandbox account with an email address, and no existing AGNT account or app subscription is required; an agent can sign up headlessly with no email or browser, receiving a secret shown once, and fund the account through a human claim link or x402 in USDC on Base. Prepaid execution needs no card; the docs say there are no automatic card charges.
- interface: rest
- limits:
  - request-rate: one started minute minimum per run, then started-minute rounding; default job 120 seconds, maximum 900 seconds [2]
  - per-object-cap: job inputs up to 8 root filenames combined 8 MB; each artifact transfer at most 8 MB [2]
  - retention-clamped: artifacts retained 1 day on PAYG and Starter, 7 days on Pro, 30 days on Business; monthly downloads 1 GB, 5 GB, 15 GB respectively [2]
  - write-gated (binding): a USD 10 minimum prepaid top-up is required before a PAYG job can run, and every paid job needs a maxChargeMicroUSD spending cap [2]
- limits note: A compute-minute is one started minute of a Small (1 vCPU, 1 GB) sandbox; Medium and Large consume 2 and 4 compute-minutes a minute. Guests have offline networking, no arbitrary images, no snapshots, no public ports and no inherited secrets. Current capacity is serial and queued, not reserved concurrency.
- binding note: A new account cannot run a job at all until prepaid credit is added; the USD 10 minimum top-up is the first gate a user meets, ahead of the per-minute charge.
- interface detail: an HTTP API at https://sandbox.agnt.gg/sandbox/v1 with /jobs, /jobs/quote, /artifacts and /agents endpoints, an OpenAPI document, and JavaScript and Python job helpers; agents can sign up and fund themselves over HTTP
- endpoint: https://agnt.gg
- tooling: an HTTP client and a Bearer sandbox_ key; headless agent signup returns a secret, and funding is by a human claim link or x402 with USDC on Base
- composes with: a bounded Python, Node or shell job runs in an isolated Kata-backed VM and exports selected files through the API, with a spend cap on each run; the offline guest has no inherited credentials, so outside data must be passed in as inputs.
- reliability: Guests run offline with no network access and no inherited credentials. Capacity is serial and queued rather than reserved concurrency; a busy or absent worker rejects new admission. Customer-code failures and timeouts consume runtime; confirmed lost-worker failures on managed jobs are refunded.
- notes: The operator's provider list prices AGNT Sandbox at USD 6.00/h billed per minute; the vendor's published sizes are Small at 6 US cents a minute (USD 3.60/h), Medium 2 vCPU/2 GB at 12 cents a minute (USD 7.20/h) and Large 4 vCPU/4 GB at 24 cents a minute (USD 14.40/h). No free tier is published: the monthly Starter plan costs USD 5 and bundles 100 compute-minutes. The 2 vCPU/4 GB size in the list is not a published size.
- evidence note: the pricing page, llms.txt and docs page were read on 2026-11-25; the quoted lines establish the prepaid model, the per-minute rates, the signup gate and the artifact and network limits. No account, wallet funding or job was created, so the rung is documented rather than measured.
- self hosted: no
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.note: Small is the pay-as-you-go unit; Medium and Large consume 2 and 4 compute-minutes a minute
  - billing_model: prepaid pay-as-you-go by started compute-minute, with optional monthly minute bundles
  - free_tier_kind: none
  - price_arithmetic: 6 US cents per compute-minute for Small = USD 3.60 per hour (derived: 0.06 x 60); Medium 0.12 x 60 = USD 7.20 per hour; Large 0.24 x 60 = USD 14.40 per hour
  - billing_note: the vendor publishes per-minute rates, not an hourly rate; the hourly figures here are arithmetic on the quoted rates
  - session_cap.wall_clock_min: 15
  - session_cap.restart_required: no
  - session_cap.note: default job 120 seconds, maximum 900 seconds; the VM is destroyed after job teardown
  - network_out.allow_outbound: no
  - network_out.allow_inbound_listen: no
  - network_out.ports: no public ports; artifacts are fetched through the authenticated API
- evidence:
  - [1] 2026-11-25: the service sells prepaid short jobs in isolated Linux VMs with a USD 10 minimum credit and a 6-cent per compute-minute rate | capture: sha256:fc9c14115ed457edd765e3cb5c5fa74801533dc02a894f778dc67425e51ac7b0 | quote: Start with $10 prepaid credit. No subscription required: 6¢ per compute-minute.
  - [1] 2026-11-25: a compute-minute is one minute of a Small 1 vCPU/1 GB sandbox and the PAYG rates for the three sizes | capture: sha256:fc9c14115ed457edd765e3cb5c5fa74801533dc02a894f778dc67425e51ac7b0 | quote: A compute-minute is one minute of a Small sandbox (1 vCPU, 1 GB RAM). Pay as you go: Small 6¢/min, Medium 12¢/min, Large 24¢/min. Every run rounds up to a whole minute, and a default job runs 2 minutes.
  - [1] 2026-11-25: the monthly plans bundle 100, 400 or 1200 compute-minutes and cap artifacts at 250 MB for 1 day, 1 GB for 7 days or 3 GB for 30 days | capture: sha256:fc9c14115ed457edd765e3cb5c5fa74801533dc02a894f778dc67425e51ac7b0 | quote: | Starter | $5 | 100 | 50 default jobs | 4¢/min | 15 minutes | 250 MB · 1 day |
  - [3] 2026-11-25: the Sandbox account is created with an email address and is separate from an AGNT subscription | capture: sha256:a10e9901fa7e080a33700fc1a8c894318ae6dc3e80451dc2d7241f97ceaa3676 | quote: Create your Sandbox account with your email address, or sign in if you already have one. No existing AGNT account or app subscription is required. Headless agents can register and fund themselves over HTTP.
  - [3] 2026-11-25: an agent can sign up with no email or browser using a secret shown once | capture: sha256:a10e9901fa7e080a33700fc1a8c894318ae6dc3e80451dc2d7241f97ceaa3676 | quote: No email, no browser. The secret is your identity. Store it securely; it is shown only once.
  - [3] 2026-11-25: prepaid balances fund execution and there are no automatic card charges | capture: sha256:a10e9901fa7e080a33700fc1a8c894318ae6dc3e80451dc2d7241f97ceaa3676 | quote: Prepaid balances fund pay-as-you-go execution without a subscription. Optional monthly plans include compute-minutes and a lower rate beyond them. There are no automatic card charges.
  - [2] 2026-11-25: the artifact retention windows and monthly download allowances for each plan | capture: sha256:a83582912ba35e9389b1392890da1f211c8dcbd2ce872b44a1e4cd7296dd4583 | quote: PAYG/Starter artifacts250MB/1day; Pro1GB/7days; Business3GB/30days. Monthly downloads1/5/15GB respectively. Retained output survives VM destruction until expiry.
  - [2] 2026-11-25: the VM is offline only and has no arbitrary images, snapshots, public ports or inherited secrets | capture: sha256:a83582912ba35e9389b1392890da1f211c8dcbd2ce872b44a1e4cd7296dd4583 | quote: Python3, Node and shell installed. Offline networking only. No secrets inherited, no arbitrary images, no snapshots, no public ports.
  - [2] 2026-11-25: the default job is 120 seconds with a 900-second maximum for new jobs | capture: sha256:a83582912ba35e9389b1392890da1f211c8dcbd2ce872b44a1e4cd7296dd4583 | quote: Default 120 seconds. New jobs/sessions maximum 900 seconds. Explicit sessions remain for advanced use; DELETE /sandboxes/{id} is required for early cleanup.
  - [2] 2026-11-25: the job input and output transfer ceilings are 8 MB per transfer with at most 8 files | capture: sha256:a83582912ba35e9389b1392890da1f211c8dcbd2ce872b44a1e4cd7296dd4583 | quote: Job inputs up to 8 root filenames, combined 8MB, base64 encoded. Job outputs up to 8 relative paths. Each transfer <=8MB.
  - [2] 2026-11-25: capacity is serial and queued rather than reserved concurrency | capture: sha256:a83582912ba35e9389b1392890da1f211c8dcbd2ce872b44a1e4cd7296dd4583 | quote: Current capacity is serial and queued, not guaranteed parallel execution. Inspect /capabilities.
  - [4] 2026-11-24: the hosted Sandbox service runs code in a machine of its own and is bundled into paid plans | capture: sha256:fbcde912c2b79c05ef53c9b3abc1ca3cba3c23d5bb0a685d4b97baf3d8039337 | quote: Sandbox runs the code in a machine of its own.
  - [4] 2026-11-24: AGNT Pro includes 100 compute-minutes of Sandbox per month, Team 600 | capture: sha256:fbcde912c2b79c05ef53c9b3abc1ca3cba3c23d5bb0a685d4b97baf3d8039337 | quote: | Sandbox minutes | — | 100 | 300 | 600 |
  - [4] 2026-11-24: a compute-minute is one minute of Small, with size multipliers and rounding | capture: sha256:fbcde912c2b79c05ef53c9b3abc1ca3cba3c23d5bb0a685d4b97baf3d8039337 | quote: A compute-minute is one minute of Small.
  - [4] 2026-11-24: sandboxes are capped at 15 minutes and destroyed when the job ends | capture: sha256:fbcde912c2b79c05ef53c9b3abc1ca3cba3c23d5bb0a685d4b97baf3d8039337 | quote: Medium counts 2×, Large 4×, rounded up per run. Sandboxes live at most 15 minutes and are destroyed when the job ends.
  - [5] 2026-11-24: the free Community Core tier runs locally and excludes the hosted Sandbox service; paid plans start at $29/mo | capture: sha256:1f4dde98e4581336b76088cc690197a9317a94971456844ede875bc0a2914ee8 | quote: | Price | Community Core: free and small businesses, unlimited local runs. AGNT Pro $29/mo, Pro + Always-On $49/mo and AGNT Team $99/mo with 3 seats, each including a hosted instance plus Models, Search, Scrape, Sandbox, Mail and Webhooks. Enterprise: custom. [See pricing](https://agnt.gg/pricing) |
  - [5] 2026-11-24: the runtime is a local desktop app or Docker with a cloud instance option | capture: sha256:1f4dde98e4581336b76088cc690197a9317a94971456844ede875bc0a2914ee8 | quote: Runs on | Windows, macOS and Linux desktop apps and Docker. Reachable from the web and the AGNT Chat mobile app, paired by QR code, locally or through a remote server.
  - [6] 2026-11-24: API request and daily email caps of the hosted Pro and Team plans | capture: sha256:9251d1f183405569e47ba033237b5a8e48661ae060218d841359a236915e9ad1 | quote: | API requests per hour | — | 10,000 | 100,000 | Unlimited |
  - [6] 2026-11-24: the hosted Pro instance is active 8 hours a day | capture: sha256:9251d1f183405569e47ba033237b5a8e48661ae060218d841359a236915e9ad1 | quote: | Active time per dayTime your instance spends awake and working — not time you spend at the screen. | — | 8 hours | Unlimited | Unlimited |
  - [7] 2026-11-24: sign-in is by a 6-digit email code and the local app needs no account | capture: sha256:d44fb1af2e447af4470a8bf9ca2d795d31a6d3fe052d1d605da98bcef6e7ad96 | quote: AGNT itself runs locally and needs no account. You only sign in to sync your license, marketplace publishing, and referral credit.
- sources:
  - [1] https://sandbox.agnt.gg/
  - [2] https://sandbox.agnt.gg/llms.txt
  - [3] https://sandbox.agnt.gg/docs
  - [4] https://agnt.gg/services
  - [5] https://agnt.gg/
  - [6] https://agnt.gg/pricing
  - [7] https://agnt.gg/login
