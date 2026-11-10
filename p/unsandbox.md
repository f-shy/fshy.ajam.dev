# unsandbox

> unsandbox.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unsandbox/ | JSON https://fshy.ajam.dev/api/v1/entity/unsandbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## unsandbox

- `compute/unsandbox` | qualifies-with-caveat | evidence documented | binding request-rate | category container sandbox / remote code execution API | tier Development
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:20:51.332Z (live) | stale on 2026-12-05
- url https://unsandbox.com/pricing
- price parsed USD 7/mo
- free tier: Free $0 forever: 1 concurrent container, 1 request per 42 seconds, zerotrust execute only, 15 minute TTL max, no sessions or services, community support | unit: mixed | metered on: request-count | read on: 2026-10-24 | source: [1] | note: the free tier is a concurrency and rate allowance, not a byte or an hour allowance
- per-object cap: 10 files per execution, 10 MB total per execution and 5 MB per single file; maximum container resources 8 vCPU and 16 GB RAM
- retention: unknown: sessions and services survive freeze/unfreeze and services auto-unfreeze on an inbound HTTP request, but no page read states how long a frozen service or a snapshot is kept before deletion | source: [2]
- egress: Not published. Neither the pricing page nor the docs page read states a traffic allowance, a per-GB rate, or an egress quota; the plan card sells concurrency, request rate and container size only. Services are served with automatic HTTPS on *.on.unsandbox.com and custom domains by CNAME. | metered: no | source: [1]
- identity: card | detail: The paid path is 'Purchase API Key' from the pricing page, so the USD 7 tier is bought, not registered for. The USD 0 free tier also requires an account. Whether a debit or prepaid card is accepted, whether any authorisation is held, and whether the free tier can be entered without a card are not stated on the pages read.
- interface: rest, cli
- limits:
  - request-rate (binding): 7 requests a minute and 1 concurrent execution on Development; 91 a minute and 4 concurrent on Production at USD 91 a month [1]
  - retention-clamped: 15 minute TTL max on the free tier; paid plans get 'Custom TTL', and the maximum permitted TTL is not published [1]
- limits note: Freeze/unfreeze is the lifecycle: a frozen service unfreezes on an HTTP request, which is what turns a 15-minute-TTL container into a service. The requests-per-minute cap, not the container size, is what a webhook or agent workload hits first.
- binding note: At 7 requests a minute a single agent loop or a modest webhook receiver saturates the plan long before the 1 vCPU or the 2 GB is used, and the next step up is USD 91 a month.
- interface detail: REST API with public/secret API keys, a Python client (un.py), 42+ language runtimes, persistent sessions over tmux/screen, and long-running services with automatic TLS.
- tooling: The vendor's own Python client and raw REST. Sessions are reached with a shell over tmux or screen, so existing SSH-style workflows do not transfer: this is an API-first product, not a machine you log into.
- composes with: USD 7 a month buys a 1 vCPU / 2 GB container that can run as a long-lived HTTPS service with a custom domain, freezing between requests. That makes it a candidate for a small always-on endpoint or a scheduled job runner, not for a daily-driver shell and not for a VPN node.
- reliability: Nothing observed. A container that is frozen between requests loses in-flight process state on the unfreeze unless the service is designed for it; the docs present freeze as resource saving and do not promise process continuity.
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
  - session_cap.restart_required: no
  - session_cap.note: 15 minute TTL max on free; 'Custom TTL' on paid, maximum unpublished
  - aggregator_note: sandboxprices.com lists unsandbox at the end of its 160-product picker with no modelled price, so the site contributes discovery only for this provider.
- evidence:
  - [1] 2026-10-24: quoted: 'Development $7 /month - 1 concurrent, 7 RPM, 1 vCPU, 2GB RAM, 1 concurrent execution, 7 requests/minute, Sessions + Services, Custom TTL'
  - [1] 2026-10-24: free tier: 'Free $0 forever - 1 concurrent container, 1 request per 42 seconds, Zerotrust execute only, 15 minute TTL max, No sessions or services'
  - [2] 2026-10-24: service model: 'Create long-running services with automatic HTTPS at *.on.unsandbox.com. TLS certificates are provisioned automatically via Let's Encrypt. Custom domains supported via CNAME' and 'Freeze (auto-unfreezes on HTTP request)'
  - [2] 2026-10-24: caps: 'Maximum resources (8 vCPUs, 16GB RAM)', 'Maximum files: 10 per execution', 'Maximum total size: 10MB (encoded)'
  - [2] 2026-11-04: the vendor ships a command-line client | capture: sha256:e799d5396d5271283a78e4909cfe51cdfdcf9bc94beff557b3f29c11ead79937 | quote: wget https://unsandbox.com/cli/inception/un.py
- sources:
  - [1] https://unsandbox.com/pricing
  - [2] https://unsandbox.com/docs
