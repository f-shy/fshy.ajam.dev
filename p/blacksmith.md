# Blacksmith

> blacksmith.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blacksmith/ | JSON https://fshy.ajam.dev/api/v1/entity/blacksmith.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blacksmith (GitHub Actions runners)

- `compute/blacksmith` | qualifies-with-caveat | evidence documented | binding write-gated | category CI runner (hosted, GitHub Actions-compatible)
- identity a placeholder: card and phone unknown | verified 2026-10-30T10:47:30.677Z (live) | stale on 2026-11-30
- url https://www.blacksmith.sh/pricing
- free tier: 3,000 free minutes a month on every plan the page lists. Beyond the free minutes the page states only that it is 33% cheaper than GitHub per-minute pricing; it prints no per-minute price. | unit: minutes | metered on: wall-clock | read on: 2026-10-30 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: unverified: the pricing page states no signup requirement. Connecting a repository needs a GitHub account, and no signup was performed, so whether a card is required is not established
- interface: unknown
- limits:
  - request-rate: 3,000 free minutes a month [1]
  - request-rate: 33% cheaper than GitHub per-minute pricing; the page prints no per-minute price [1]
  - per-object-cap: Docker layer caching and sticky disks add USD 0.50 a GB-month; a static IP adds USD 100 an IP a month [1]
- limits note: the page publishes no per-minute price table for each runner size; the only price statement is the 33% discount against GitHub, and the macOS M4 rate quoted in a comparison report is not on the page read here
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: the page states no job wall clock, no concurrency cap and no queue limit; the only reliability claim is that the hardware runs 2x faster than GitHub runner, which no page here measures
- notes: The plan grid shows 3,000 free minutes a month on every plan, a 33% discount against GitHub per-minute pricing and three paid add-ons. The startup and OSS programmes are application-gated and grant a discount rather than a free tier. The macOS M4 rate quoted in a comparison report is not on the page read here and stays unverified.
- evidence note: The free allowance, the discount claim and the add-on prices are read from the vendor own pricing page; the per-size rate table is rendered by script and is not in the page text. Raise by running one job on a free account and reading the invoice line.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no clock stated on the rendered page
  - free_tier_kind: recurring-credit
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the pricing page was read on 2026-10-22 and returns customer testimonials only: 'The amount we pay an engineer per minute is far higher than any CI minute'. It states no plan, price or free allowance
  - [1] 2026-10-30: the free allowance is 3,000 minutes a month | capture: sha256:7fa1f56cd550b9066cb1d96c0a9a9b4c346a34b9ac0c17791a9010c9336e86bc | quote: 3,000 free min/mo.
  - [1] 2026-10-30: Docker layer caching and sticky disks cost USD 0.50 a GB-month | capture: sha256:7fa1f56cd550b9066cb1d96c0a9a9b4c346a34b9ac0c17791a9010c9336e86bc | quote: Docker layer caching (+$0.50/GB/mo.)
  - [1] 2026-10-30: the discount is 33% below GitHub per-minute pricing | capture: sha256:7fa1f56cd550b9066cb1d96c0a9a9b4c346a34b9ac0c17791a9010c9336e86bc | quote: We are 33% cheaper than GitHub per-minute pricing
  - [1] 2026-10-30: no signup requirement is stated on the pricing page | capture: sha256:7fa1f56cd550b9066cb1d96c0a9a9b4c346a34b9ac0c17791a9010c9336e86bc | quote: Try for free
  - [1] 2026-10-30: the hardware is claimed to run 2x faster than GitHub's runners | capture: sha256:7fa1f56cd550b9066cb1d96c0a9a9b4c346a34b9ac0c17791a9010c9336e86bc | quote: We are 2x faster than GitHub's runners.
  - [1] 2026-10-30: a startup discount is application-gated | capture: sha256:7fa1f56cd550b9066cb1d96c0a9a9b4c346a34b9ac0c17791a9010c9336e86bc | quote: Under 100 employees
- sources:
  - [1] https://www.blacksmith.sh/pricing
