# MacStadium

> macstadium.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macstadium/ | JSON https://fshy.ajam.dev/api/v1/entity/macstadium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MacStadium

- `compute/macstadium` | paid-only | evidence documented | binding write-gated | category macOS host
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:03:50.407Z (live) | stale on 2026-12-26
- url https://www.macstadium.com/pricing
- free tier: M2.S Mac mini M2 8 Core 8 GB 256 GB SSD $109 | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: unlimited bandwidth on a dedicated IPv4 address is included at a flat 1 GB internet link with no published overage price | metered: no | source: [1]
- identity: email | detail: a free MacStadium portal account is required to see inventory and get a quote before buying; the portal page is behind a login wall. The identity fields requested at signup are unverified
- interface: unknown
- limits:
  - request-rate: individual hosted Macs from USD 109 a month up to USD 449 a month; enterprise Mac Cloud Compute is quote-only [1]
  - per-ip-shaping: 1 GB internet link with 'Unlimited bandwidth', a claim about a missing limit rather than a number [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Flexible monthly or annual pricing options. Unlimited bandwidth is included with flat-rate billing. A free MacStadium portal account is needed to see the inventory and get an instant price quote before buying. The FAQ asks whether free trials exist but gives no answer on this page.
- evidence note: the pricing page was read on 2026-10-22 and describes fixed monthly or annual billing with no free tier. The record's free-tier claim is contradicted
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon
  - shape.gpu_count: 1
  - shape.note: standard configurations, width not stated on this page
  - session_cap.restart_required: no
  - session_cap.note: a dedicated or hosted Mac on a monthly term; no session clock
  - free_tier_kind: none
  - granularity.min_billed_s: 2592000
  - ps.price: included in the monthly term
  - ps.durability: dedicated storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - net.allowance: unlimited bandwidth
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Unlimited bandwidth' and 'predictable, fixed monthly or annual billing' with 'Sign-up online', and a FAQ entry 'Do you offer free trials on individual hosted Macs?', quoted
  - [1] 2026-11-25: the pricing table states the entry hosted Mac configuration and monthly price | capture: sha256:4230d3bb3b826593f06683e2d496f2d120e47138258203259d421ffac7c8b3b4 | quote: M2.S Mac mini M2 8 Core 8 GB 256 GB SSD $109
  - [1] 2026-11-25: the page describes the portal account used to see prices before buying | capture: sha256:4230d3bb3b826593f06683e2d496f2d120e47138258203259d421ffac7c8b3b4 | quote: Create a free MacStadium portal account to see our full inventory and get an instant price quote with our pricing calculator before you buy.
  - [1] 2026-11-24: the pricing page lists individual hosted Macs with a monthly price and no free tier | capture: sha256:4230d3bb3b826593f06683e2d496f2d120e47138258203259d421ffac7c8b3b4 | quote: M2.S Mac mini | M2 8 Core | 8 GB | 256 GB SSD | $109
  - [1] 2026-11-24: the billing model is fixed monthly or annual, and individual model prices are listed | capture: sha256:4230d3bb3b826593f06683e2d496f2d120e47138258203259d421ffac7c8b3b4 | quote: Reduce expenses vs. a DIY solution and get predictable, fixed monthly or annual billing.
  - [1] 2026-11-24: an online sign-up is required before a purchase | capture: sha256:4230d3bb3b826593f06683e2d496f2d120e47138258203259d421ffac7c8b3b4 | quote: Sign-up online
  - [1] 2026-11-24: a free portal account is the gate to see prices and buy | capture: sha256:4230d3bb3b826593f06683e2d496f2d120e47138258203259d421ffac7c8b3b4 | quote: Create a free MacStadium portal account to see our full inventory and get an instant price quote with our pricing calculator before you buy.
  - [1] 2026-11-24: bandwidth is included without a per-GB charge | capture: sha256:4230d3bb3b826593f06683e2d496f2d120e47138258203259d421ffac7c8b3b4 | quote: Fast 1GB internet is included. Use as much as you need without affecting your flat rate billing.
  - [1] 2026-11-24: the pricing page still shows the included-bandwidth term | capture: sha256:4230d3bb3b826593f06683e2d496f2d120e47138258203259d421ffac7c8b3b4 | quote: Unlimited bandwidth
- sources:
  - [1] https://www.macstadium.com/pricing
