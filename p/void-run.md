# VoidRun

> void-run.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/void-run/ | JSON https://fshy.ajam.dev/api/v1/entity/void-run.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VoidRun, Usage-first (trial credits)

- `compute/voidrun` | trial-only | evidence documented | binding volume-quota | category cloud sandbox | tier Usage-first (trial credits)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.709Z (live) | stale on 2026-12-26
- url https://void-run.com/pricing
- duplicate of `compute/voidrun-sandboxes`
- free tier: No base subscription. Fully usage-based. Launch trial: get started with free credits and run real workloads without adding a card. Up to ₹4,600.00 free credits, then pay only for consumed compute, memory, and storage. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The page fixes an exchange rate of $1 = ₹92.00 (fallback). Metered rates are ₹0.0010304 per compute-second, ₹0.0003312 per GB-second of memory and ₹0.000002208 per GB-second of storage; the storage meter reads 'Beta: ₹0.0000 charge'. Rates are published in Indian rupees.
- per-object cap: not applicable: the billed unit is compute-seconds and GB-seconds, not an object; no per-object cap is published | source: [1]
- retention: not published for sandboxes: the pricing page names persisted disk volume for artifacts and cache but states no retention period | source: [1]
- egress: not published: the pricing page lists compute, memory and storage meters and states no egress allowance or price | metered: no | source: [1]
- identity: email | detail: It says 'No. You can start with free credits and add payment later.' No card, phone or ID is asked for at signup.
- interface: rest, cli
- limits:
  - volume-quota (binding): up to ₹4,600.00 of free credits, then pay per compute-second, GB-second of memory and GB-second of storage [1]
  - volume-quota (binding): ₹89.03 per compute unit per day and ₹2,670.80 per compute unit per month at the published meter [1]
- binding note: The ₹4,600.00 credit is the first limit reached; there is no subscription floor, so usage is capped by the credit before any unpublished concurrency limit.
- interface detail: A dashboard at dash.void-run.com and an API are implied by the usage-first lane; the pricing page does not name an endpoint or a CLI.
- tooling: the dashboard at dash.void-run.com is the stated entry point; no SDK, CLI or API endpoint is published on the pricing page.
- composes with: Hosted, usage-metered sandboxes for developers and AI agents with no base subscription, so short workloads can be paid per consumed compute, memory and storage without a card until credits run out.
- reliability: Storage billing is marked Beta with a ₹0.0000 charge in one line and a nonzero meter in another; charges are metered continuously and the trial credits are one-time.
- notes: Hosted, disposable cloud sandboxes for developers and AI agents, sold entirely usage-based with up to ₹4,600.00 of trial credit and no card needed to start. The credit is a sign-up trial rather than a recurring free tier, so the verdict is trial-only; interface and retention beyond the dashboard are unverified from the public pages.
- evidence note: The credit amount, no-card statement, metered rates and signup fields are quoted from VoidRun's own pricing and signup pages read 2026-11-25; the prices are published in rupees.
- extras:
  - shape.gpu_class: not published
  - shape.gpu_count: 0
  - shape.note: compute units, GB of memory and GB of storage are metered separately; no machine shape is published
  - billing_model: usage-only meters for compute, memory and storage, with trial credits
  - free_tier_kind: signup-credit
  - network_out.ports: not published
  - session_cap.note: not published
- evidence:
  - [1] 2026-11-25: a trial gives free credits usable without a card, with payment added later only for higher limits | capture: sha256:4d48ff10f119a30b41e93956bda67d964e8cbbd5f97738737a5f2dae54e08dd0 | quote: No. You can start with free credits and add payment later.
  - [1] 2026-11-25: the free credit allowance is up to ₹4,600.00, after which usage is billed | capture: sha256:4d48ff10f119a30b41e93956bda67d964e8cbbd5f97738737a5f2dae54e08dd0 | quote: Up to ₹4,600.00 free credits, then pay only for consumed compute, memory, and storage.
  - [1] 2026-11-25: the compute meter is ₹0.0010304 per second | capture: sha256:4d48ff10f119a30b41e93956bda67d964e8cbbd5f97738737a5f2dae54e08dd0 | quote: ₹0.0010304
  - [2] 2026-11-25: signup accepts GitHub or an email address with optional first and last name | capture: sha256:5d3ffedb25d58ea707e7de2558efc9ba1561c7337cdc169362326413f9bd0975 | quote: Continue with GitHub
- sources:
  - [1] https://void-run.com/pricing
  - [2] https://dash.void-run.com/sign-up

## VoidRun, Usage-first (Lane 1)

- `compute/voidrun-sandboxes` | trial-only | evidence documented | binding volume-quota | category disposable cloud sandbox | tier Usage-first (Lane 1)
- needs card no, phone no, ID no, institution no | verified 2026-11-26T02:53:32.774Z (live) | stale on 2026-12-27
- url https://void-run.com/pricing
- free tier: Up to ₹4,600.00 free credits, then pay only for consumed compute, memory, and storage. The FAQ states no card is needed to start: 'No. You can start with free credits and add payment later.' | unit: credits | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: A one-time credit allowance of up to INR 4,600.00, not a recurring monthly grant. The exchange rate stated on the page is '$1 = ₹92.00 (fallback)'. No expiry for the credits is stated on the pricing page.
- per-object cap: not applicable: the unit is a sandbox, not an object | source: [1]
- retention: Files persist as long as the sandbox exists. When you delete a sandbox, all files are permanently removed. A sandbox that stays snapshotted past the retention window is deleted; the documented default is 7 days snapshotted (604800 s). | days: 7 | source: [2] | note: Idle sandboxes are snapshotted after 60 seconds; auto-delete after being snapshotted defaults to 7 days. These are hosted-VoidRun defaults.
- egress: No egress price or included traffic volume is published. Outbound internet access can be restricted at the MicroVM level with allowlists and blocklists, or disabled entirely, and each published sandbox port gets a stable public HTTPS URL served by the VoidRun gateway. | metered: no | source: [3]
- identity: email | detail: The sign-up page offers 'Continue with GitHub' or an email address field with first and last name optional; it asks for no phone number and no card. The quickstart requires a VoidRun API key from the dashboard to use the API, SDKs or CLI.
- interface: rest, cli, ssh
- limits:
  - retention-clamped: auto-delete after snapshotted defaults to 7 days (604800 s), after which the sandbox and its snapshot are removed [2]
  - volume-quota (binding): up to ₹4,600.00 in free credits, then usage-metered compute at ₹0.0010304/second, memory at ₹0.0003312/GB second and storage at ₹0.000002208/GB second (beta: ₹0.000000/GB second) [1]
- limits note: Unlimited workspaces and team members are stated for Lane 1. Compute unit equivalence: ₹89.03/day or ₹2,670.80/month; memory GB equivalence: ₹28.62/day or ₹858.47/month; storage GB equivalence: ₹0.190771/day or ₹5.72/month. No free credit expiry is stated on the pricing page.
- binding note: The INR 4,600.00 credit allowance is a one-time amount that is spent before any published meter begins charging, while the 7-day snapshot deletion only applies after a sandbox goes idle.
- interface detail: Create a sandbox using API or CLI; the SDKs & API page documents REST routes with X-API-Key authentication and a WebSocket PTY; SSH and VNC access are documented for sandboxes.
- endpoint: https://platform.void-run.com/api/sandboxes
- tooling: npm install @voidrun/sdk, pip install voidrun, npm install -g @voidrun/cli, or curl against the REST API with an X-API-Key header; an SSH client reaches sandboxes directly.
- composes with: A sandbox runs untrusted code and writes results out through the file download API before teardown, with external object storage used when data must outlive the 7-day snapshot retention window.
- reliability: Snapshotted sandboxes are auto-deleted after 7 days by default and an open PTY connection does not count as activity; deletion is permanent and destroys files and snapshots.
- notes: Free credits are a one-time INR 4,600.00 allowance, not a monthly grant. The meters are per-second for CPU, per GB-second for memory and per GB-second for storage, with the storage meter marked beta at INR 0.000000. An enterprise lane is priced by annual contract and is a separate offer. Self-hosted deployments are documented but the offer priced here is the hosted platform.
- evidence note: The credit amount, per-second meters and the no-card statement are quoted from the vendor's pricing page; the sign-up fields from the vendor's sign-up page; and the retention default from the vendor's lifecycle documentation, all read on 2026-11-24. The egress price is unverified because no page states one.
- extras:
  - billing_model: one-time free credits then per-second usage billing
  - free_tier_kind: one-time-credit
  - shape.note: the pricing page meters compute units, GB-seconds of memory and GB-seconds of disk; the example workload quoted is 4 compute units, 8 GB memory and 120 GB disk
  - price_note: compute INR 0.0010304/second, memory INR 0.0003312/GB second, storage INR 0.000002208/GB second; page states $1 = ₹92.00 (fallback)
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: public HTTPS URL per published port
  - network_out.egress_price: unverified: no price or included volume published
  - session_cap.idle_reap_s: 60
  - session_cap.note: idle sandboxes are snapshotted after 60 seconds by default; running sandboxes have no maximum execution time
- evidence:
  - [1] 2026-11-24: the usage-first lane includes up to INR 4,600.00 in free credits before metered usage | capture: sha256:4d48ff10f119a30b41e93956bda67d964e8cbbd5f97738737a5f2dae54e08dd0 | quote: Up to ₹4,600.00 free credits, then pay only for consumed compute, memory, and storage.
  - [1] 2026-11-24: no card is needed to start; payment is added only when higher limits are needed | capture: sha256:4d48ff10f119a30b41e93956bda67d964e8cbbd5f97738737a5f2dae54e08dd0 | quote: No. You can start with free credits and add payment later.
  - [1] 2026-11-24: compute is metered at INR 0.0010304 per second and memory at INR 0.0003312 per GB second | capture: sha256:4d48ff10f119a30b41e93956bda67d964e8cbbd5f97738737a5f2dae54e08dd0 | quote: Compute meter ₹0.0010304 /second
  - [1] 2026-11-24: storage is metered at INR 0.000002208 per GB second, with a beta charge of INR 0.000000 per GB second | capture: sha256:4d48ff10f119a30b41e93956bda67d964e8cbbd5f97738737a5f2dae54e08dd0 | quote: ₹0.000002208/GB second
  - [4] 2026-11-24: the sign-up form asks for an email address, with GitHub SSO as the alternative and no card or phone field | capture: sha256:5d3ffedb25d58ea707e7de2558efc9ba1561c7337cdc169362326413f9bd0975 | quote: Email address
  - [2] 2026-11-24: auto-delete after snapshotted defaults to 7 days for hosted VoidRun | capture: sha256:44d848f44722322ba99720c50cd1358d7225d99963aed8bcfa1729be1e8a02f0 | quote: Auto-delete after snapshotted | 7 days (604800 s) | `AUTO_LIFECYCLE_DELETE_AFTER_SNAPSHOTTED_SEC` |
  - [5] 2026-11-24: files are lost permanently when a sandbox is deleted | capture: sha256:46bef30122f66f048d8ac43484a050611f1d948d53d61b88a91769a79d8dd7bb | quote: When you delete a sandbox, all files are permanently removed.
  - [5] 2026-11-24: files can be read back out over the REST file download endpoint | capture: sha256:46bef30122f66f048d8ac43484a050611f1d948d53d61b88a91769a79d8dd7bb | quote: curl -X GET "https://api.void-run.com/api/sandboxes/<sandbox-id>/fs/download?path=/app/output.json"
  - [6] 2026-11-24: sandboxes are created through an API or a CLI | capture: sha256:b4ad070f7f4d08e0e6cf7ac2f5b399e7a542ee27cd4f99cb9ee8abd8639bd39c | quote: Create a sandbox using API or CLI
  - [7] 2026-11-24: each published port gets a public HTTPS URL through the gateway | capture: sha256:a0fffce029cc3df86e2171619f362b6a854dd5577d94d329d877ad13bfeb97c5 | quote: Every sandbox port you publish gets a stable public HTTPS URL served by the VoidRun gateway.
  - [3] 2026-11-24: outbound access can be restricted at the MicroVM level | capture: sha256:3234b5f7d45f64d2e7092583cb04593877d913aedda9bcbe8597b6434b05169a | quote: VoidRun provides granular network control at the MicroVM level, allowing you to restrict outbound connections
  - [8] 2026-11-24: REST endpoints authenticate with an X-API-Key header | capture: sha256:4a1e60ec1beae66b8136c554be831e813896d4f42373e66bedaf10501fedc00a | quote: Authenticated endpoints expect your API key on every request:
  - [9] 2026-11-24: using the API needs an API key obtained from the dashboard | capture: sha256:f5f7a1a523f7bf8c1045ff70d26ef887aa5d36244a671857b09eb6fcb6f6d0c1 | quote: A VoidRun API key (get one from the [VoidRun Dashboard](https://dash.void-run.com))
  - [1] 2026-11-25: the free allocation is a one-time credit, so the offer is a trial rather than a recurring free allowance | capture: sha256:4d48ff10f119a30b41e93956bda67d964e8cbbd5f97738737a5f2dae54e08dd0 | quote: Up to ₹4,600.00 free credits, then pay only for consumed compute, memory, and storage.
  - [1] 2026-11-25: the pricing page was read again on 2026-11-25; the free allocation is a one-time credit | capture: sha256:4d48ff10f119a30b41e93956bda67d964e8cbbd5f97738737a5f2dae54e08dd0 | quote: Up to ₹4,600.00 free credits, then pay only for consumed compute, memory, and storage.
- sources:
  - [1] https://void-run.com/pricing
  - [2] https://void-run.com/docs/core-concepts/lifecycle.md
  - [3] https://void-run.com/docs/networking/internet-access.md
  - [4] https://dash.void-run.com/sign-up
  - [5] https://void-run.com/docs/core-concepts/file-system.md
  - [6] https://void-run.com/
  - [7] https://void-run.com/docs/networking/public-urls.md
  - [8] https://void-run.com/docs/sdks/overview.md
  - [9] https://void-run.com/docs/getting-started/quickstart.md
