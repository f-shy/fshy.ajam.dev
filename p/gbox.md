# GBOX

> gbox.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gbox/ | JSON https://fshy.ajam.dev/api/v1/entity/gbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GBOX

- `compute/gbox` | qualifies-with-caveat | evidence documented | binding volume-quota | category desktop and Android environment sandbox | tier Usage-based (Linux / Android boxes)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.732Z (live) | stale on 2026-12-26
- url https://docs.gbox.ai/pricing
- free tier: Sign up and get USD 100 in credits instantly, spent at the published per-second rates; no recurring free allowance is stated. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The signup credit is one-time. No card is stated as required to create an account.
- per-object cap: The unit is a box, not an object. Linux boxes include 10 GiB of storage free; the Android emulator is offered in Medium (4 cores, 8 GB RAM) and Large (8 cores, 16 GB RAM), and a physical device is 8 cores, 8 GB RAM and 128 GB storage. | source: [1]
- retention: Not stated on the pricing page; the SDK exposes create and destroy of boxes and the terms page states a hosted environment is provided with no published retention period. | source: [2]
- egress: No egress allowance or per-GB price is stated on the pricing page; the Android physical device rate includes its network in the per-second charge, and no base traffic price is published. | metered: no | source: [1]
- identity: email | detail: The API key page says to go to GBOX AI, log in to an account and create the key in the dashboard. No phone, ID document or card is stated as required for signup.
- interface: rest, cli
- limits:
  - volume-quota (binding): USD 100 in signup credits, one-time; Linux box vCPU USD 0.054/hour and memory USD 0.0144/GiB/hour, billed per second [1]
  - volume-quota (binding): Android emulator has a 30-second minimum charge; a physical device has a 10-minute minimum charge [1]
- limits note: A credit balance is consumed at the per-second rates; no concurrent box count or session length is published on the pricing page.
- binding note: The USD 100 signup credit runs out before any published rate or concurrency cap, since no concurrency or session count limit is stated.
- interface detail: A GBOX API key from the dashboard is passed as a Bearer token to the REST API; an SDK and a CLI/MCP connector create and drive Android, browser and Linux boxes.
- tooling: The GBOX SDK (npx/npm), a CLI and an MCP server drive boxes; an API key from the GBOX dashboard is required.
- composes with: Android, browser and Linux boxes share one GBOX account and its USD 100 signup credits, so an agent can move between mobile, browser and desktop tasks on one balance.
- reliability: Physical devices are beta and may have limited availability.
- notes: GBOX sells hosted Linux, browser and Android environments for agents, with a USD 100 signup credit. The Linux box is priced at USD 0.054 per vCPU-hour plus USD 0.0144 per GiB-hour with 10 GiB storage free; a 2 vCPU/4 GiB box is USD 0.1656 per hour at list rates. The Android Medium emulator is USD 0.0003/second with a 30-second minimum. Registration uses a GitHub account, which supplies the email address; no card is stated for signup. The on-premise deployment mentioned on the benchmark site is a separate option; this record prices the hosted GBOX service.
- evidence note: Prices and the signup credit are quoted from the vendor's pricing page read on 2026-11-25.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 10
  - billing_model: per-second usage against a signup credit
  - free_tier_kind: one-time-credit
  - status: hosted, available
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - session_cap.restart_required: no
  - session_cap.note: 30-second minimum for an Android emulator and 10-minute minimum for a physical device; no Linux session minimum published
- evidence:
  - [1] 2026-11-25: the Linux box vCPU price and per-second billing | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: | vCPU | $0.054 | Billed per second, shown hourly |
  - [1] 2026-11-25: the Linux box memory price | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: | Memory | $0.0144 / GiB | Billed per second, shown hourly |
  - [1] 2026-11-25: 10 GiB of Linux box storage is included free | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: | Storage | 10 GiB | Free to use |
  - [1] 2026-11-25: a USD 100 signup credit is granted instantly | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: [Sign up](https://gbox.ai/) today and get 100$ in credits instantly.
  - [3] 2026-11-25: registration uses a GitHub account | capture: sha256:be16893a307db3cdd4c5f7adb3856e26ed851070ef24f7a98dbfff68de57c94d | quote: When you register for an account, we will ask you to sign up using github account.
  - [4] 2026-11-25: an account login precedes API key creation | capture: sha256:e23f40d134855c15bdd1b4838386a8c6af4d30915e0687dbd0ee2086877ad2a4 | quote: Login to your account
  - [1] 2026-11-25: the Android emulator Medium price, shape and 30-second minimum | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: Android Emulator Minimum 30-second charge | 4 Core, 8GB RAM • Under 30s: $0.009 flat • Over 30s: $0.0003/sec
  - [1] 2026-11-24: Linux box vCPU costs USD 0.054 per hour and is billed per second | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: | vCPU | $0.054 | Billed per second, shown hourly |
  - [1] 2026-11-24: Linux box memory costs USD 0.0144 per GiB-hour and is billed per second | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: | Memory | $0.0144 / GiB | Billed per second, shown hourly |
  - [1] 2026-11-24: the Linux box includes 10 GiB of storage free to use | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: | Storage | 10 GiB | Free to use |
  - [1] 2026-11-24: signup grants USD 100 in credits, a one-time rather than recurring allowance | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: today and get 100$ in credits instantly.
  - [1] 2026-11-24: Android emulator and physical device rates carry minimum charges | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: | Android Emulator Minimum 30-second charge | 4 Core, 8GB RAM • Under 30s: $0.009 flat • Over 30s: $0.0003/sec | 8 Core, 16GB RAM • Under 30s: $0.015 flat • Over 30s: $0.0005/sec |
  - [1] 2026-11-24: physical-device time has a 10-minute minimum charge and is not available on the medium size | capture: sha256:44ddaae54101dbe393a2de9afb4bce474d0221e72533dc00e1e6c7363b401639 | quote: | Physical Device Minimum 10-minute charge | Not Available | 8 Core, 8GB RAM, 128GB Storage • Under 30s: $0.024 flat • Over 30s: $0.0008/sec |
  - [3] 2026-11-24: registration is through a GitHub account and receives the name, email address and profile photo; a card is only described as an optional payment method | capture: sha256:b6b688527329fcdd0e8e573205cd95a399e2132d22802c24a50b4f38eefb4b4d | quote: Registration and Profile Information. When you register for an account, we will ask you to sign up using github account. We will also receive information from github such as your name, email address, and profile photo. Payment Information. When you add a credit card or payment method to your account a third-party service provider that handles payments on our behalf will receive and process your payment card information.
  - [4] 2026-11-24: an account login and an API key are needed before any box can be created | capture: sha256:e23f40d134855c15bdd1b4838386a8c6af4d30915e0687dbd0ee2086877ad2a4 | quote: 1. Go to [GBOX AI](https://gbox.ai) 2. Login to your account 3. Click on "API Keys" 4. Create / Copy the API key
  - [5] 2026-11-24: the SDK and API cover mobile, browser, desktop and sandbox environments over one interface | capture: sha256:423371ac15cd4af1fb28d00951e8a8a6dd2e5298193f2538071ecf6d5c798bf1 | quote: GBOX supports four types of environments: Mobile, Browser, Desktop and Sandbox.
- sources:
  - [1] https://docs.gbox.ai/pricing
  - [2] https://gbox.ai/home/terms
  - [3] https://gbox.ai/home/privacy
  - [4] https://docs.gbox.ai/api-key
  - [5] https://docs.gbox.ai/
