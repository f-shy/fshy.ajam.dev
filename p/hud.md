# HUD

> hud.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hud/ | JSON https://fshy.ajam.dev/api/v1/entity/hud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HUD

- `compute/hud` | qualifies-with-caveat | evidence reported | binding write-gated | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T15:51:59.409Z (live) | stale on 2026-11-19
- url https://www.hud.ai/
- free tier: a new team starts with no credits: 'Runs and QA reviews are paid from your team's credit balance, and a new team starts with none.' The cited page https://www.hud.ai/ (read 2026-10-30) states no amount | unit: credits | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: A HUD guide page still states 'Cloud starts at $0.25+/environment hour with $10 in free credits.' and $100 for an academic .edu email; the quickstart says a new team starts with none, so whether a grant is applied at sign-up is unverified: only an account shows the balance.
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: not published | metered: no | source: [2]
- identity: email | detail: email: sign-up is held by Clerk and accepts an email address or a Google account, with no phone number field and a password required; a first and last name are required fields. A credit card is required to run work, because credits are bought with one and a new team starts with none.
- interface: rest, cli
- limits:
  - write-gated (binding): plans are Pay as you go, from credits bought with a card, and Pro at USD 50 a month, which adds USD 50 of credits each paid month; on Pay as you go work starts only while the credit balance is above zero [2]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: REST API at https://api.hud.ai/v2, a CLI and an SDK
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The first read was refused with 429; the page was reached through the firecrawl provider. It carries no price and no free credit, so the USD 10 the record held is not established here.
- evidence note: the home page, the platform quickstart, the billing documentation and a guide page were read on 2026-10-30: the quickstart says a new team starts with no credits, a guide page still advertises USD 10 in free credits, and the billing documentation prices Pay as you go and Pro
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the page states no clock
  - free_tier_kind: one-time-credit
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: 'Start from a community environment, build your own with the SDK, or import existing tasks from Harbor' and 'pip install hud'; the page publishes no plan, price or free tier, and a 429 on the first read was cleared by the firecrawl route
  - [1] 2026-10-30: a new team has no credits; runs are paid from the credit balance | capture: sha256:bfb6b0a5ffeb16d6b3e7fe25d3918ae93e2586fee5583a7e89d67a9c595254c1 | quote: Runs and QA reviews are paid from your team's credit balance, and a new team starts with none.
  - [3] 2026-10-30: usage is drawn from prepaid credits denominated in US dollars | capture: sha256:5738dbeaaeeb39d770283e247e0d039b6a9a1a56c8caa3b5699966a4e4fe2c33 | quote: HUD bills in prepaid credits, in US dollars.
  - [4] 2026-10-30: a HUD guide page advertises USD 10 in free credits for cloud runs | capture: sha256:248442a6ef8d09ee1ef61b7120bdf155052e8003d4a0ad14a14e6ccf40792a93 | quote: Cloud starts at $0.25+/environment hour with $10 in free credits.
  - [4] 2026-10-30: the guide page advertises USD 100 in credits for an academic .edu email | capture: sha256:248442a6ef8d09ee1ef61b7120bdf155052e8003d4a0ad14a14e6ccf40792a93 | quote: Academic accounts receive $100 in free credits with a.edu email.
  - [2] 2026-10-30: creating a first environment needs no card | capture: sha256:df4d6d59ce67df966d77261396e9ac6c44f91e4ba6fdfd9a2159a6aa6e6fa8a2 | quote: Create your first environment in minutes. No credit card required.
  - [3] 2026-10-30: credits are bought with a card | capture: sha256:5738dbeaaeeb39d770283e247e0d039b6a9a1a56c8caa3b5699966a4e4fe2c33 | quote: Add credits buys credits with a card.
  - [3] 2026-10-30: the Pro plan is USD 50 a month and adds USD 50 of credits each paid month | capture: sha256:5738dbeaaeeb39d770283e247e0d039b6a9a1a56c8caa3b5699966a4e4fe2c33 | quote: | Pro | \$50 a month | Each paid month adds \$50 of credits.
  - [5] 2026-11-03: HUD has a REST API | capture: sha256:2b87ebafabd27872b8f9294f40c2c85c4712fbe24f5f394aaa43e8229e355895 | quote: The REST API is the HTTP interface to the HUD platform
  - [5] 2026-11-03: HUD has a CLI and an SDK | capture: sha256:2b87ebafabd27872b8f9294f40c2c85c4712fbe24f5f394aaa43e8229e355895 | quote: The CLI and SDK use this public surface
  - [6] 2026-11-04: the sign-up form identifies a person by an email address or a Google account | capture: sha256:78ad17d16efd29b0df2abbc79d26056c1909c852f0ba8cb1cdb1d735c8160deb | quote: "identification_requirements":[["email_address","oauth_google"],[]]
  - [6] 2026-11-04: the sign-up form has no phone number field | capture: sha256:78ad17d16efd29b0df2abbc79d26056c1909c852f0ba8cb1cdb1d735c8160deb | quote: "phone_number":"off"
  - [1] 2026-11-04: a new team has no credits, so work needs a purchase | capture: sha256:5642b89f87bd19f3cdfdc24607a89d6541cc00a4ba0d90e917a72b7f90d09a5a | quote: Runs and QA reviews are paid from your team's credit balance, and a new team starts with none.
  - [3] 2026-11-04: the credit balance that work is paid from is bought with a card | capture: sha256:2a5606030826f3b45bdbc7ebe1468562ad1c4f9ce89afc72c8475a865b5f6da0 | quote: Add credits buys credits with a card.
- sources:
  - [1] https://docs.hud.ai/platform/quickstart
  - [2] https://www.hud.ai/
  - [3] https://docs.hud.ai/platform/billing
  - [4] https://www.hud.ai/guides/top-5-reinforcement-learning-environments
  - [5] https://docs.hud.ai/platform/rest-api.md
  - [6] https://clerk.hud.ai/v1/environment
