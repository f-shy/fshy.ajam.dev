# OpenAGI

> agiopen.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/agiopen/ | JSON https://fshy.ajam.dev/api/v1/entity/agiopen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenAGI / Lux

- `compute/openagi` | qualifies-with-caveat | evidence unverified | category computer-use model API
- needs card unknown, phone yes, ID no, institution no | verified 2026-11-07T00:31:33.900Z (live) | stale on 2026-11-22
- url https://developer.agiopen.org/docs/pricing
- free tier: the console states free credits to get started with no amount published; the console prices input tokens at USD 0.10 and output tokens at USD 0.90 per 1M | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1] | note: not published
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1] | note: durability of the sandbox disk on stop and on delete is not published
- egress: not published | metered: no | source: [1]
- identity: email | detail: email: an account is required for certain features ('you may be required to create a Lux Account') and holds 'a username; a password; an email address or phone number and your preferred language', so an email address or a phone number is the gate. Phone: not required: the account accepts 'an email address or phone number'. Country: not published: the terms state no country requirement at registration.
- interface: rest
- interface detail: OpenAI-compatible /v1/chat/completions endpoint at api.agiopen.org, documented in the console's OpenAPI bundle
- tooling: not published
- composes with: not established; the console prices input and output tokens (USD 0.10 per 1M input, USD 0.90 per 1M output) and names no route into another offer
- reliability: no reliability event recorded
- notes: The pricing document is a 404 with no body, which is the one case where a 404 is not evidence of a withdrawal: AGI Open's docs live under a path that may have moved, and no replacement path was found. Do not call the provider dead on this alone.
- evidence note: The rung stays unverified because the free tier is what the verdict rests on and it is not established
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: unverified: developer.agiopen.org/docs/pricing returns 404 with an empty body on 2026-10-22 and the firecrawl route, so the pricing document no longer exists at that address and no other route recovers it
  - [2] 2026-10-28: the product is a hosted model that emits UI actions, not a compute or browser host | capture: sha256:99b0bc46b652781a294134d6c7860311b604b790bf21fca11e25364673349a87 | quote: Lux is an AI model that operates computers like a human.
  - [1] 2026-10-28: the pricing document path answers 404 on 2026-10-28 | capture: sha256:2f80d9c8b281fd7d8c7f336a9c5fb2c403478983560fb3b81db191afba8d1e11 | quote: "upstream_status":404
  - [1] 2026-10-28: the pricing document path still answers 404 on 2026-10-28 | capture: sha256:2f80d9c8b281fd7d8c7f336a9c5fb2c403478983560fb3b81db191afba8d1e11 | quote: "upstream_status":404
  - [2] 2026-10-28: the developer console documents Lux from OpenAGI, unchanged | capture: sha256:99b0bc46b652781a294134d6c7860311b604b790bf21fca11e25364673349a87 | quote: Lux is an AI model that operates computers like a human.
  - [3] 2026-11-04: an account is created with a username, a password and an email address or phone number | capture: sha256:08270e76e96f964230b1ee771517be6fb01a51650b8e16a4d6780bddfefe8a08 | quote: a username; a password; an email address or phone number and your preferred language
  - [4] 2026-11-04: the terms make an account a condition of using the service | capture: sha256:6daedeff92886bbe7075ab5879500ef3aa5621eaa1ad970726b89d8363994237 | quote: you may be required to create a Lux Account
  - [4] 2026-11-04: no institution or enterprise route exists, so the gate is an individual account | capture: sha256:6daedeff92886bbe7075ab5879500ef3aa5621eaa1ad970726b89d8363994237 | quote: At present, Lux provides only individual developer accounts and does not offer enterprise accounts
  - probe:https://developer.agiopen.org/docs/pricing 2026-11-04: no pricing document exists at the vendor's pricing path, so no free-credit amount can be read there | capture: sha256:56e73929ca660cb7267199e137c8756887a643209f52aedba3a57cb7c5522419 | quote: "status": 404
  - [3] 2026-11-04: the account gate is an email address or a phone number, and the email kind holds | capture: sha256:08270e76e96f964230b1ee771517be6fb01a51650b8e16a4d6780bddfefe8a08 | quote: a username; a password; an email address or phone number and your preferred language
  - [3] 2026-11-06: an account holds an email address or a phone number, and a card is required only to buy paid Services | capture: sha256:08270e76e96f964230b1ee771517be6fb01a51650b8e16a4d6780bddfefe8a08 | quote: a username; a password; an email address or phone number and your preferred language
  - [5] 2026-11-07: the console offers free credits to get started and states no amount | capture: sha256:c1cc99c37b50f7ea6abdea7bff496dad7ff8ab967209a571aba4dcdb314dc006 | quote: Your API key provides access to Lux foundation models and includes free credits to get started.
  - [5] 2026-11-07: the API is an OpenAI-compatible REST endpoint | capture: sha256:c1cc99c37b50f7ea6abdea7bff496dad7ff8ab967209a571aba4dcdb314dc006 | quote: description:"Using the OpenAI-compatible chat completions endpoint for computer use"
  - [5] 2026-11-07: the production server is api.agiopen.org | capture: sha256:c1cc99c37b50f7ea6abdea7bff496dad7ff8ab967209a571aba4dcdb314dc006 | quote: url:"https://api.agiopen.org",description:"Production server"
  - [5] 2026-11-07: the console prices tokens, not machines | capture: sha256:c1cc99c37b50f7ea6abdea7bff496dad7ff8ab967209a571aba4dcdb314dc006 | quote: e.strong,{children:"Input tokens"})}),n.jsx(e.td,{children:"$0.10 / 1M tokens"})]}),n.jsxs(e.tr,{children:[n.jsx(e.td,{children:n.jsx(e.strong,{children:"Output tokens"})}),n.jsx(e.td,{children:"$0.90 / 1M tokens"})
  - [5] 2026-11-07: the offer is a computer-use model API | capture: sha256:c1cc99c37b50f7ea6abdea7bff496dad7ff8ab967209a571aba4dcdb314dc006 | quote: operates computers like a human. It views the screen, understands natural language goals, and outputs actions (clicks, typing, scrolling) to complete tasks across any application.
- sources:
  - [1] https://developer.agiopen.org/docs/pricing
  - [2] https://developer.agiopen.org/
  - [3] https://agiopen.org/privacy
  - [4] https://agiopen.org/terms
  - [5] https://developer.agiopen.org/assets/index-BVU6vPQ6.js
