# CloudCruise

> cloudcruise.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudcruise/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudcruise.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudCruise

- `compute/cloudcruise` | trial-only | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-06T17:48:23.920Z (live) | stale on 2026-12-07
- url https://cloudcruise.com/pricing
- free tier: 2 automation hours of workflow runtime, then $3 an hour; the hour includes the VM, the proxies and the AI usage | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the page read states no egress allowance and no overage price per TB | metered: no | source: [1]
- identity: email | detail: email: the sign-in page offers an email address and a password ('EmailPassword') with a Sign Up tab, beside Google and SSO ('Sign in with Google'; 'Sign in with SSO'). A card is not required for the free allowance: the terms state 'Some Services are free; others require payment (“Paid Services”).' and charge a payment method only when Paid Services are bought ('You authorize us (via our payment processor – currently Stripe) to charge your chosen payment method.'). A phone is not required: the sign-in form at https://app.cloudcruise.com/login carries an email address and a password and no phone field. Country: not published at https://cloudcruise.com/terms.
- interface: rest
- limits:
  - request-rate (binding): 2 free automation hours, then $3 an hour of runtime [1]
  - per-object-cap: an automation hour is 60 minutes of workflow runtime with the VM, proxies and AI usage bundled [1]
- interface detail: HTTP API at api.cloudcruise.com with TypeScript and Python SDKs
- tooling: HTTP API with TypeScript and Python SDKs
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states a 2-hour free allowance before $3 an hour. Two hours is a trial in practice and the record says so rather than calling it a tier
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.wall_clock_min: 120
  - session_cap.restart_required: no
  - session_cap.note: the free allowance is 2 hours in total; the page states no per-run cap
  - free_tier_kind: trial
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '2 automation hours, then $3/hour' and '1 automation hour = 60 minutes of workflow runtime. VM infrastructure, proxies, and AI usage are all included.' quoted
  - [1] 2026-11-03: the usage fee covers VM, proxies and AI; no egress allowance or overage price is stated | capture: sha256:005872c9f2f4731173ababd49ac4a750620a114046fcf418efaeaa5e1b064ab6 | quote: 1 automation hour = 60 minutes of workflow runtime. VM infrastructure, proxies, and AI usage are all included.
  - [2] 2026-11-03: the browser agent is run over an API | capture: sha256:436250191a280027c3441be7daf74ac81ed4ad12bc9a755865f9884539b5afe7 | quote: you can trigger the browser agent over our API.
  - [3] 2026-11-04: the account is an email address and a password | capture: sha256:ab7687685d35816ccaa2a64c9b9776dfc34c57c1ba40a896fa4321321ec76d94 | quote: EmailPassword
  - [4] 2026-11-04: registration collects the account information the form asks for | capture: sha256:5f995277d341eb8806c2417320bcf282c6d56f1fe15ca58893bb3b6a91390d5a | quote: When registering, you agree to provide accurate, current, and complete information, keep your credentials secure, and notify us of any unauthorized use.
  - [3] 2026-11-06: the sign-in form is an email address and a password | capture: sha256:6d67f898f4e24c7ad75b691fb96177bf800f05db3fccfec868c47332e40865ca | quote: EmailPassword
  - [3] 2026-11-06: SSO and Google sign-in sit beside the email and password form | capture: sha256:6d67f898f4e24c7ad75b691fb96177bf800f05db3fccfec868c47332e40865ca | quote: Sign in with SSO
  - [4] 2026-11-06: the free services are distinguished from the paid ones | capture: sha256:5f995277d341eb8806c2417320bcf282c6d56f1fe15ca58893bb3b6a91390d5a | quote: Some Services are free; others require payment (“Paid Services”).
  - [4] 2026-11-06: a payment method is charged only when Paid Services are bought | capture: sha256:5f995277d341eb8806c2417320bcf282c6d56f1fe15ca58893bb3b6a91390d5a | quote: You authorize us (via our payment processor – currently Stripe) to charge your chosen payment method.
- sources:
  - [1] https://cloudcruise.com/pricing
  - [2] https://docs.cloudcruise.com/
  - [3] https://app.cloudcruise.com/login
  - [4] https://cloudcruise.com/terms
