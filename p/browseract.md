# BrowserAct

> browseract.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/browseract/ | JSON https://fshy.ajam.dev/api/v1/entity/browseract.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BrowserAct

- `compute/browseract` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-06T17:48:23.919Z (live) | stale on 2026-12-07
- url https://www.browseract.com/pricing
- free tier: 200 free credits on signup, 2 free agent builds and 5 free local browsers; paid tiers are $16 a month for 10,000 credits and $70 for 50,000 | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://www.browseract.com/pricing states credits and no egress allowance or overage price | metered: no | source: [1]
- identity: email | detail: email: the sign-up form's identity field is an email address, with a password, its confirmation and an emailed code ('<input autoComplete="email" placeholder="Email" id="formRegister_email"'; 'id="formRegister_code"'), beside Google and Github single sign-on; the form carries no phone field and no card field, so a card and a phone are not required at sign-up. Country: not published at https://www.browseract.com/pricing.
- interface: rest, cli
- limits:
  - request-rate (binding): 200 credits on signup, one time; 10,000 a month on the $16 tier [1]
  - request-rate (binding): 2 agent builds and 5 local browsers are the other two free caps [1]
- interface detail: BrowserAct API for Bot runs and results; a Local CLI that runs on the user's own machine; the web console builds Bots
- tooling: Local CLI (runs on the user's own machine with no runtime fee); MCP servers on paid plans
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the free grant and the two paid tiers. The free half is a one-time 200-credit grant, which contradicts the record's USD 0.32 figure as a description of it
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the free caps are counts of credits, builds and browsers; the page states no session clock
  - free_tier_kind: one-time-credit
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '200 Free Credits on Signup', '2 Free Agent Builds', '5 Free Local Browsers', against '$16.00/month 10,000 Monthly Credits' and '$70.00/month 50,000 Monthly Credits', quoted
  - [2] 2026-11-03: results are available through the BrowserAct API | capture: sha256:b9f07d819f2294469513c75f40153db4af2bf08765591e1233feb24a50a07cbd | quote: access through the BrowserAct API
  - [1] 2026-11-03: credits meter browser and proxy services; no egress allowance or overage price is stated | capture: sha256:4b7831759501415a384df8a0b49e4bb805fe75771b6ae62fb4ccf2cc3a812fdb | quote: Credits are used only when you add optional BrowserAct browser or proxy services.
  - [1] 2026-11-03: the pricing page names a Local CLI that runs on the user's own machine | capture: sha256:4b7831759501415a384df8a0b49e4bb805fe75771b6ae62fb4ccf2cc3a812fdb | quote: Local CLI runs on your own machine with no BrowserAct runtime fee.
  - [3] 2026-11-04: the registration form's first field is an email address | capture: sha256:3fc0d1606fc9130d55b7c3aa599c7abf2e9074f489f02cc7adce6f77d2bbb072 | quote: <input autoComplete="email" placeholder="Email" id="formRegister_email"
  - [3] 2026-11-04: an emailed six-digit code verifies the address | capture: sha256:3fc0d1606fc9130d55b7c3aa599c7abf2e9074f489f02cc7adce6f77d2bbb072 | quote: <button type="button" ><span>Send Code</span></button>
  - [3] 2026-11-06: the sign-up form's first field is an email address | capture: sha256:72b5f932b143bf7535519f0f133ef15fe30f86ca34af45eccb403bc7666099ff | quote: <input autoComplete="email" placeholder="Email" id="formRegister_email"
  - [3] 2026-11-06: an emailed code is the only other identity step in the sign-up form | capture: sha256:72b5f932b143bf7535519f0f133ef15fe30f86ca34af45eccb403bc7666099ff | quote: id="formRegister_code"
- sources:
  - [1] https://www.browseract.com/pricing
  - [2] https://docs.browseract.com/
  - [3] https://www.browseract.com/reception
