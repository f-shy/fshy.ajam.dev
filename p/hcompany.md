# H Company

> hcompany.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hcompany/ | JSON https://fshy.ajam.dev/api/v1/entity/hcompany.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## H Company / Surfer / H Agents API

- `compute/h-company` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-06T17:48:23.921Z (live) | stale on 2026-12-07
- url https://www.hcompany.ai/pricing
- free tier: a Free tier at $0 a month with up to 3 concurrent agents and rate limits | unit: objects | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the page read states no egress allowance and no overage price per TB | metered: no | source: [1]
- identity: email | detail: email: an account is mandatory ('Access to the Service requires mandatory creation of a User Account via:') and is created with 'A valid email address associated with a display name; or', or with Google single sign-on ('Single sign-on authentication via Google account compliant with OAuth 2.0 standards.'), and 'These identifiers constitute the sole personal elements collected, strictly necessary for authentication, session management, and functional notifications.' A card is not required at sign-up: the sign-up form at https://platform.hcompany.ai/auth/signup asks for an email address, a password and its confirmation, with no card field. A phone is not required: the terms name the email address or the Google account as the sole personal elements. Country: not published at https://hcompany.ai/terms-of-use.
- interface: rest, cli
- limits:
  - request-rate (binding): up to 3 concurrent agents on Free [1]
  - write-gated: session plans for the Agents API and per-token rates for the Models API sit above the free tier [1]
- interface detail: Agents API and Models API (transport not stated on the page); HoloDesktop CLI runs the agent on-device with inference through the Models API
- tooling: Agents API, Models API; HoloDesktop CLI on-device
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The bound is concurrency.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: bounded by 3 concurrent agents and a rate limit; the page states no session clock
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start free and scale as you build' with a 'Free · $0 per month' tier carrying 'Up to 3 concurrent agents' and rate limits, quoted
  - [1] 2026-11-03: the plans state session counts and top-up rates and no egress allowance or overage price per TB | capture: sha256:6c831efca5dfb48444b8b468170149a15c50aec4fc9e7ce33574dfad4d915ec5 | quote: Top-ups at model cost + 20%
  - [1] 2026-11-03: an Agents API and a Models API are sold; a HoloDesktop CLI exists | capture: sha256:6c831efca5dfb48444b8b468170149a15c50aec4fc9e7ce33574dfad4d915ec5 | quote: Session plans for the Agents API, per-token rates for the Models API, and free ways to try HoloTab, HoloDesktop CLI, and open weights on Hugging Face.
  - [2] 2026-11-04: the sign-up form is an email address and a password with terms acceptance | capture: sha256:56a251d6790b61283b9b1a11c96ecd926f0d9f73d1f78118fe020bee1eaad4ad
  - [3] 2026-11-04: an account is mandatory to reach the service | capture: sha256:95d002d3e54ee91f77c861d33a6b5ec62032effce049afa194f7c4a89928b74d | quote: Access to the Service requires mandatory creation of a User Account via:
  - [3] 2026-11-06: an account is created with a valid email address or a Google account | capture: sha256:95d002d3e54ee91f77c861d33a6b5ec62032effce049afa194f7c4a89928b74d | quote: A valid email address associated with a display name; or
  - [3] 2026-11-06: the email address or Google account is the only personal element collected | capture: sha256:95d002d3e54ee91f77c861d33a6b5ec62032effce049afa194f7c4a89928b74d | quote: These identifiers constitute the sole personal elements collected, strictly necessary for authentication, session management, and functional notifications.
  - [2] 2026-11-06: the sign-up form asks for an email address, a password and its confirmation, with no phone or card field | capture: sha256:0aa2dfba5bc4bd8a8754cd2b7d8ec2940109bdffdc6a78c1ada6b295ace2e576 | quote: Confirm password
- sources:
  - [1] https://www.hcompany.ai/pricing
  - [2] https://platform.hcompany.ai/auth/signup
  - [3] https://hcompany.ai/terms-of-use
