# unsandbox

> unsandbox.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unsandbox/ | JSON https://fshy.ajam.dev/api/v1/entity/unsandbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## unsandbox

- `compute/unsandbox` | qualifies-with-caveat | evidence documented | binding request-rate | category container sandbox / remote code execution API | tier Development
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T13:21:07.386Z (live) | stale on 2026-12-25
- url https://unsandbox.com/pricing
- price parsed USD 7/mo
- free tier: Free $0 forever: 1 concurrent container, 1 request per 42 seconds, zerotrust execute only, 15 minute TTL max, no sessions or services, community support | unit: mixed | metered on: request-count | read on: 2026-10-24 | source: [1] | note: the free tier is a concurrency and rate allowance, not a byte or an hour allowance
- per-object cap: 10 files per execution, 10 MB total per execution and 5 MB per single file; maximum container resources 8 vCPU and 16 GB RAM
- retention: unknown: sessions and services survive freeze/unfreeze and services auto-unfreeze on an inbound HTTP request, but no page read states how long a frozen service or a snapshot is kept before deletion | source: [2]
- egress: No rate or allowance is published. The docs describe two network modes: zerotrust with complete network isolation and no internet access, and semitrusted with internet access via an egress proxy; services use automatic HTTPS at *.on.unsandbox.com and custom domains by CNAME. | metered: no | source: [1]
- identity: card | detail: The pricing page's flow is 'Select tier → Choose duration → Pick payment → Get API key instantly', so a payment is part of obtaining a key. The docs say to sign up at unsandbox.com/console for API credentials and the console offers email-based OTP protection; the free tier's card requirement is not published.
- interface: rest, cli
- limits:
  - request-rate (binding): 7 requests a minute and 1 concurrent execution on Development; 91 a minute and 4 concurrent on Production at USD 91 a month [1]
  - retention-clamped: 15 minute TTL max on the free tier; paid plans get 'Custom TTL', and the maximum permitted TTL is not published [1]
- limits note: Freeze/unfreeze is the lifecycle: a frozen service unfreezes on an HTTP request, which is what turns a 15-minute-TTL container into a service. The requests-per-minute cap, not the container size, is what a webhook or agent workload hits first.
- binding note: At 7 requests a minute a single agent loop or a modest webhook receiver saturates the plan long before the 1 vCPU or the 2 GB is used, and the next step up is USD 91 a month.
- interface detail: REST API with HMAC-SHA256-signed public/secret keys, a downloadable CLI and 42+ language SDKs, persistent sessions over tmux/screen, and long-running services with automatic TLS.
- tooling: The vendor's own Python client and raw REST. Sessions are reached with a shell over tmux or screen, so existing SSH-style workflows do not transfer: this is an API-first product, not a machine you log into.
- composes with: USD 7 a month buys a 1 vCPU / 2 GB container that can run as a long-lived HTTPS service with a custom domain, freezing between requests. That makes it a candidate for a small always-on endpoint or a scheduled job runner, not for a daily-driver shell and not for a VPN node.
- reliability: Frozen services auto-unfreeze on an HTTP request; snapshots and images are published as preserving data across freezes and container deletion. Interrupt-free process continuity is not promised.
- notes: The plan ladder is USD 0 / 7 / 91 / 203, so the USD 7 tier is the only affordable one and its 7 requests a minute is the whole offer. Region and hosting provider are not published. The maximum custom TTL on a paid plan is the single fact that decides whether USD 7 buys an always-on service or an occasionally-running one; it was not recoverable from the pricing or docs pages, and support would have to answer it.
- evidence note: Plan prices, resources and rate caps come from the vendor's pricing page read; the lifecycle and freeze behaviour come from the docs page read. What is missing and would change the record: the maximum custom TTL (which decides whether this is an always-on box at all), the egress terms, and the payment/identity gate.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 2
  - billing_model: monthly
  - term: monthly plan
  - m10h_usd: 7.0
  - m24h_usd: 7.0
  - price_arithmetic: USD 7.00 a month flat for 1 vCPU and 2 GB, so the 10-hour and 24/7 figures are both USD 7.00. Included disk is not published.
  - free_tier_kind: capped-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: HTTP/HTTPS ingress through the service proxy and custom domains; arbitrary TCP/UDP listeners are not documented
  - session_cap.wall_clock_min: 15
  - session_cap.restart_required: no
  - session_cap.note: 15 minute TTL maximum on Free; paid plans take a custom TTL with no published maximum
  - aggregator_note: sandboxprices.com lists unsandbox at the end of its 160-product picker with no modelled price, so the site contributes discovery only for this provider.
- evidence:
  - [1] 2026-10-24: quoted: 'Development $7 /month - 1 concurrent, 7 RPM, 1 vCPU, 2GB RAM, 1 concurrent execution, 7 requests/minute, Sessions + Services, Custom TTL'
  - [1] 2026-10-24: free tier: 'Free $0 forever - 1 concurrent container, 1 request per 42 seconds, Zerotrust execute only, 15 minute TTL max, No sessions or services'
  - [2] 2026-10-24: service model: 'Create long-running services with automatic HTTPS at *.on.unsandbox.com. TLS certificates are provisioned automatically via Let's Encrypt. Custom domains supported via CNAME' and 'Freeze (auto-unfreezes on HTTP request)'
  - [2] 2026-10-24: caps: 'Maximum resources (8 vCPUs, 16GB RAM)', 'Maximum files: 10 per execution', 'Maximum total size: 10MB (encoded)'
  - [2] 2026-11-04: the vendor ships a command-line client | capture: sha256:e799d5396d5271283a78e4909cfe51cdfdcf9bc94beff557b3f29c11ead79937 | quote: wget https://unsandbox.com/cli/inception/un.py
  - [1] 2026-11-18:  | capture: sha256:433d52663aa3ea3795a80d5ab4a7e1644ab58f9a80fcba4e4e2f10acf606cd57 | quote: ✓ 15 minute TTL max
  - [1] 2026-11-24: the free tier still carries a 15-minute TTL maximum | capture: sha256:38e05ee71c26a6067fe36643b3bc2894efd72bb38c9b56862af80fdf451446bc | quote: ✓ 15 minute TTL max
  - [1] 2026-11-24: a payment step is part of the API-key flow | capture: sha256:38e05ee71c26a6067fe36643b3bc2894efd72bb38c9b56862af80fdf451446bc | quote: Select tier → Choose duration → Pick payment → Get API key instantly →
  - [2] 2026-11-24: network egress exists through a proxy, with no rate published | capture: sha256:1b15831f77edf6d101a22fce8228785ac35324751c69e6e9ed52c951826c8511 | quote: # Semi-Trusted Internet access via egress proxy.
  - [2] 2026-11-24: the API uses signed keys and is reachable from the CLI and SDKs | capture: sha256:1b15831f77edf6d101a22fce8228785ac35324751c69e6e9ed52c951826c8511 | quote: All API requests require HMAC-SHA256 signature authentication for security.
  - [2] 2026-11-24: a frozen service wakes on an inbound request | capture: sha256:1b15831f77edf6d101a22fce8228785ac35324751c69e6e9ed52c951826c8511 | quote: # Freeze (auto-unfreezes on HTTP request)
  - [1] 2026-11-24: the Development tier price is unchanged at USD 7 a month | capture: sha256:38e05ee71c26a6067fe36643b3bc2894efd72bb38c9b56862af80fdf451446bc | quote: ### Development $7 /month
  - [3] 2026-11-24: captured while checking sign-in routes; not used for an unsandbox value | capture: sha256:07d892d5ea287fe71f5e0adc55b094734fd3f5882a9550e28590b211500aa90d | quote: Use one of the sign-in methods below to continue.
- sources:
  - [1] https://unsandbox.com/pricing
  - [2] https://unsandbox.com/docs
  - [3] https://console.unikraft.cloud/auth/signin
