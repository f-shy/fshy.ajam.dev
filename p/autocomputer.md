# AutoComputer

> autocomputer.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/autocomputer/ | JSON https://fshy.ajam.dev/api/v1/entity/autocomputer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AutoComputer

- `compute/autocomputer` | paid-only | evidence documented | binding none | category Windows host
- identity a placeholder: card and phone unknown | verified 2026-11-06T15:56:55.348Z (live) | stale on 2026-12-07
- url https://www.autocomputer.ai/
- free tier: no free tier: the last published price list, the Wayback copy of 2025-07-17, offers Business from USD 999 a month and Enterprise custom, and the live site on 2026-11-06 states no price at all | unit: none | metered on: wall-clock | read on: 2026-11-06 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: unverified: the live site offers a demo booking and the archived price list only a sales contact, so no self-service sign-up and no form field were read; the kind is an assumption, not a finding
- interface: unknown
- binding note: no constraint row: the offer is a sales-led business plan from USD 999 a month with no published rate, quota or retention term, so the price binds before any limit does
- interface detail: the live site publishes no API page; the archived API page of 2025-07-17 advertises a beta REST API that you request access to, so no published interface is established
- tooling: no client is published; the archived API page describes a beta REST API you request access to
- composes with: not established
- reliability: no reliability event recorded
- notes: The homepage answers with a one-paragraph statement and is a different site: it states no product tier, no API and no price. The pricing path is behind a Vercel Security Checkpoint, which answers a challenge to a raw fetch and is reported as not-found by two providers. The last published price list is the Wayback copy of 2025-07-17: Business from USD 999 a month with up to 100 instances, Enterprise custom with up to 1000, and no free plan. The price is therefore the archived one and is not current.
- evidence note: documented from the vendor's own pages read on 2026-11-06: the live homepage, which states no price, and the Wayback copy of 2025-07-17 of the pricing page, which states the Business and Enterprise plans and no free tier. identity_cost stays a guess: no sign-up form was read, so its kind is not established and the detail says so.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: unverified: no route returned the page on 2026-10-22.
  - [1] 2026-11-06: the homepage answers 200 and carries no price and no free tier | capture: sha256:11a267e60d304b4a1db218be4109910f6b4ccf8326c3df2a4c21a9c555e2e048 | quote: We build autonomous AI systems to do long-horizon tasks on computers and the internet.
  - [2] 2026-11-06: the archived price list opens the Business plan at USD 999 a month and lists no free plan | capture: sha256:2b739d812715cab807b61c6c33a7b0487a3569336bb68b340d92f59045ffb91f | quote: Use-case specific pricing, starting from
  - [1] 2026-11-06: the vendor page was read on 2026-11-06 | capture: sha256:11a267e60d304b4a1db218be4109910f6b4ccf8326c3df2a4c21a9c555e2e048 | quote: We build autonomous AI systems to do long-horizon tasks on computers and the internet.
  - [2] 2026-11-06: the archived first-party price list states the plan limits and the entry price | capture: sha256:2b739d812715cab807b61c6c33a7b0487a3569336bb68b340d92f59045ffb91f | quote: Up to 100 instances
  - [2] 2026-11-06: the only published ceiling is an instance count in a sales plan, not a rate or a quota that would bind first | capture: sha256:2b739d812715cab807b61c6c33a7b0487a3569336bb68b340d92f59045ffb91f | quote: Up to 100 instances
  - [2] 2026-11-06: the vendor publishes no rate, quota or retention term, only a sales contact | capture: sha256:2b739d812715cab807b61c6c33a7b0487a3569336bb68b340d92f59045ffb91f | quote: Looking for something else? Contact our sales team for a tailored package.
  - [2] 2026-11-06: the archived price list holds two paid plans and no free plan | capture: sha256:2b739d812715cab807b61c6c33a7b0487a3569336bb68b340d92f59045ffb91f | quote: Business
  - [2] 2026-11-06: the archived price list opens the Business plan at USD 999 a month with up to 100 instances and lists no free plan | capture: sha256:2b739d812715cab807b61c6c33a7b0487a3569336bb68b340d92f59045ffb91f | quote: $999/month
  - [2] 2026-11-06: the only route to a plan is a sales contact, with no sign-up form on the page | capture: sha256:2b739d812715cab807b61c6c33a7b0487a3569336bb68b340d92f59045ffb91f | quote: Looking for something else? Contact our sales team for a tailored package.
  - [3] 2026-11-06: the archived API page describes REST endpoints inside a beta programme you request access to | capture: sha256:18819d869b4c64d6dab7e8b54a46e6cfc0ffedb56d84eb0e362c3bf571f068e5 | quote: Automate workflows through RESTful endpoints
  - [3] 2026-11-06: API access is a beta programme, and no client is published | capture: sha256:18819d869b4c64d6dab7e8b54a46e6cfc0ffedb56d84eb0e362c3bf571f068e5 | quote: Get early access to our API that lets you host instances with your software and run pre-built end-to-end automations on them.
  - [2] 2026-11-06: the Business plan starts at USD 999 a month | capture: sha256:2b739d812715cab807b61c6c33a7b0487a3569336bb68b340d92f59045ffb91f | quote: $999/month
  - [2] 2026-11-06: the Enterprise plan carries up to 1000 instances and a custom price | capture: sha256:2b739d812715cab807b61c6c33a7b0487a3569336bb68b340d92f59045ffb91f | quote: Up to 1000 instances
- sources:
  - [1] https://www.autocomputer.ai/
  - [2] https://web.archive.org/web/20250717194128/https://www.autocomputer.ai/pricing
  - [3] https://web.archive.org/web/2026/https://www.autocomputer.ai/api
