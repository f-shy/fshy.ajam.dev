# io.net Intelligence

> io.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/io/ | JSON https://fshy.ajam.dev/api/v1/entity/io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## io.net Intelligence

- `compute/io-net-intelligence` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API | tier Standard (free daily allowance of the IO Intelligence inference API)
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T10:14:37.872Z (live) | stale on 2026-12-04
- url https://io.net/docs/guides/payment/io-intelligence-payments
- free tier: A free daily inference allowance exists and is documented, but its size is not published. Quoted: 'Standard (default): Explore and learn with free, light daily access. Pay-as-you-go (PAYG) pricing is applied for usage beyond the daily limit.' Quoted: 'The IO Intelligence API offers different free daily limits per account, depending on the AI model.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: account creation by Google, Apple ID, GitHub or an email one-time password, and the free daily allowance needs no payment details: a guide states 'The io.intelligence API includes free daily limits per model, so you can start without entering payment details'. Adding credit takes a card or Solana, and the 5% top-up fee applies 'only to credit top-ups made with a credit or debit card', so debit is accepted. Prepaid acceptance and any authorisation amount are not stated
- interface: rest
- limits:
  - request-rate (binding): The Standard plan's free daily allowance is not sized on the pages read. It is a credit pool shared across models, each model consuming credits at its own rate, and chat and API calls draw on the same daily limit. The per-model limit table that the API guide points to is not on the API reference page read. [1]
- limits note: The Standard plan's free daily allowance is not sized on the pages read. It is a credit pool shared across models, each model consuming credits at its own rate, and chat and API calls draw on the same daily limit. The per-model limit table that the API guide points to is not on the API reference page read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the only free lane io.net actually operates, and it is inference not GPU rental. It composes with a coding agent that needs a daily token allowance rather than a machine.
- reliability: no reliability event recorded
- notes: io.net needs two records, not one, and conflating them is the error a roundup makes. IO Cloud is a paid GPU marketplace with a USD 10 minimum. io.net Intelligence is a separate product with a genuinely free daily token allowance.
- extras:
  - facets.class: decentralized-inference
  - facets.free_tier_kind: recurring-allowance
- evidence:
  - [1] 2026-10-22: quoted: the Standard plan is the default and gives 'free, light daily access'; paid plans are Professional at USD 15 per month and Developer at USD 150 per month; daily limit covers both chat and API
  - [2] 2026-10-22: quoted: 'The IO Intelligence API offers different free daily limits per account, depending on the AI model. See the table in our API Reference for model-specific limits'
  - [3] 2026-10-22: quoted: 'Tokens reset automatically every day. The usage display (e.g., 1.4K/1M) shows how many tokens you've used out of the total available', which shows a 1M-token daily figure as the worked example
  - [4] 2026-10-22: quoted: 'The io.intelligence API includes free daily limits per model, so you can start without entering payment details'
  - [5] 2026-10-22: quoted: minimum purchase USD 10; purchased credits expire 12 months after purchase; promotional credits exist but with terms stated only when issued
  - [6] 2026-10-22: account creation by Google, Apple ID, GitHub or email one-time password; payments are card or Solana only, with no free tier mentioned anywhere in the account or payment path
  - [7] 2026-10-22: quoted: 'A 5% fee applies only to credit top-ups made with a credit or debit card'
  - [1] 2026-11-03: the Standard plan is the default and gives free, light daily access, with pay-as-you-go beyond the daily limit | capture: sha256:f696e8eeba015d07c4d497bacdad81cf34644c588a7428ef78dd56c713552e0f | quote: * Standard (default): Explore and learn with free, light daily access. Pay-as-you-go (PAYG) pricing is applied for usage beyond the daily limit.
  - [1] 2026-11-03: the allowance is a credit pool shared across models, each model consuming at its own rate | capture: sha256:f696e8eeba015d07c4d497bacdad81cf34644c588a7428ef78dd56c713552e0f | quote: Credits can be spent on any model, with each consuming credits at a different rate depending on the complexity.
  - [4] 2026-11-03: the free daily limits need no payment details | capture: sha256:063fd111aed7b0cd52530df2b6ff0825c6d97ec0ab96bafb70f78a0cb0c4aa27 | quote: The io.intelligence API includes free daily limits for certain models, so you can start without entering payment details.
  - [6] 2026-11-03: account creation by social login or an email one-time password | capture: sha256:349fc76437790db58d16217eefa3d64915627f98c6bf884930785db3a76acbec | quote: To create an account, go to [cloud.io.net](https://cloud.io.net/cloud/home) using Google, Apple ID, GitHub, or simply with a one-time password by clicking the "Login with Email" button.
- sources:
  - [1] https://io.net/docs/guides/payment/io-intelligence-payments
  - [2] https://io.net/docs/guides/intelligence/io-intelligence-apis
  - [3] https://support.io.net/en/support/solutions/articles/156000296695-io-intelligence-exploring-ai-models
  - [4] https://io.net/p/how-to-deploy-llama-3-on-io-net-step-by-step-guide
  - [5] https://io.net/docs/guides/payment/io-credits
  - [6] https://io.net/docs/guides/clouds/start-using-io-cloud
  - [7] https://io.net/docs/guides/payment/io-cloud-payments
