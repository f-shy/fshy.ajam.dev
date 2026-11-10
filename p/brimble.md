# Brimble Sandboxes

> brimble.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/brimble/ | JSON https://fshy.ajam.dev/api/v1/entity/brimble.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Brimble Sandboxes

- `compute/brimble` | qualifies-with-caveat | evidence documented | binding write-gated | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-09T13:25:35.685Z (live) | stale on 2026-12-10
- url https://brimble.io/pricing
- free tier: a Free plan at $0/mo for hobby projects; the page publishes no CPU-hour, sandbox or bandwidth allowance for it, and the sandbox quotas it does list belong to the $3 Hacker plan | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: App bandwidth is a plan quota (the Hacker plan lists 250 Gb); the Free plan's bandwidth allowance is not published on the pricing page; Object Storage egress has no bandwidth fees | metered: yes | free allowance: unverified: the Free plan's bandwidth allowance is not published; the Hacker plan lists 250 Gb | source: [1]
- identity: email | detail: an email address, a first name and a username at sign-up, 'Email address First name Last nameoptional Username Referral codeoptional', behind a Cloudflare security check, with GitHub, Google, GitLab or Bitbucket sign-in as the alternative. The free plan needs no card: 'Paid plans need a payment method and an active subscription. Free does not.' The form asks for no phone number.
- interface: unknown
- limits:
  - write-gated (binding): a Free plan exists at $0 but the page publishes no compute allowance for it; the numbers it lists are Hacker's, so the free ceiling is unstated [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and lists a $0 Free plan above the $3 Hacker tier. The record's paid-only verdict was wrong about the plan's existence, and the free plan's own limits are genuinely not on this page, which the free tier field says rather than inventing a number
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.wall_clock_min: 120
  - session_cap.restart_required: no
  - session_cap.note: the Free plan's sandbox bullet states a 120 minute maximum runtime with up to 2 vCPU and 4 GB, so the wall clock is 120 minutes; no idle reap interval is published
  - free_tier_kind: allowance
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free · For hobby projects and learning · $0/mo' with 'Hacker $3/mo' and 'Developer $11/mo'; the sandbox allowances on the page ('3 Sandboxes at a time (up to 2 vCPU / 4 GB, 120 min max runtime)', '5 Sandbox CPU hours + 10 GB-hours included') sit under Hacker, not under Free
  - [1] 2026-11-03: the Hacker plan lists 250 Gb of bandwidth | capture: sha256:c24ed1c652a3252c0b2f1df3bda09daebdd2096eca4d76449801d03e1359669a | quote: - 250 Gb Bandwidth
  - [1] 2026-11-03: object storage egress carries no bandwidth fees | capture: sha256:c24ed1c652a3252c0b2f1df3bda09daebdd2096eca4d76449801d03e1359669a | quote: no bandwidth fees
  - [2] 2026-11-04: the sign-up form collects an email address, a first name and a username | capture: sha256:cea12c5d131a7016e454820b12ff49bf14b29b800246b6801ffce7d5b0b7be46 | quote: Email address First name Last nameoptional Username Referral codeoptional
  - [3] 2026-11-04: the free plan carries no payment method while paid plans do | capture: sha256:0f295cf96261b77266976b666667a7db9f84feeaec896f9e269fd1fe6c6fb781 | quote: Paid plans need a payment method and an active subscription. Free does not.
  - [1] 2026-11-04: the free start is advertised on the pricing page with no card named | capture: sha256:aaa98dd4253b392395bc244941aec40a869d383dceb6031eaf95de9cdec586e0 | quote: Start for free, and upgrade when you're ready.
  - [1] 2026-11-09: the Free plan states a 120 minute maximum runtime for its sandboxes | capture: sha256:1fab0f763be9650c1d9abc339581780366c9d50203003b08abad199ac6761dd1 | quote: - 3 Sandboxes at a time (up to 2 vCPU / 4 GB, 120 min max runtime)
  - [1] 2026-11-09: the 120 minute cap sits on the Free plan bullet, not on Hacker only | capture: sha256:1fab0f763be9650c1d9abc339581780366c9d50203003b08abad199ac6761dd1 | quote: - 3 Sandboxes at a time (up to 2 vCPU / 4 GB, 120 min max runtime)
  - [1] 2026-11-09: the Free plan states the 120 minute maximum runtime | capture: sha256:1fab0f763be9650c1d9abc339581780366c9d50203003b08abad199ac6761dd1 | quote: - 3 Sandboxes at a time (up to 2 vCPU / 4 GB, 120 min max runtime)
- sources:
  - [1] https://brimble.io/pricing
  - [2] https://app.brimble.io/signup
  - [3] https://paper.brimble.io/billing/plans
