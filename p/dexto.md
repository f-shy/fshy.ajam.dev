# Dexto

> dexto.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dexto/ | JSON https://fshy.ajam.dev/api/v1/entity/dexto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dexto

- `compute/dexto` | qualifies-with-caveat | evidence documented | binding write-gated | category container and VM sandbox
- needs card unknown, phone no, ID no, institution no | verified 2026-11-04T15:51:59.408Z (live) | stale on 2026-12-05
- url https://www.dexto.ai/docs/models/
- free tier: free access to specific zero-priced models through Dexto Cloud, such as Apodex 1.1 Mini at $0.00 per token; the page prices models rather than machines and states no compute credit | unit: tokens | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: email: the login page offers only a GitHub or a Google account, and the signed-in account carries an email address; the CLI signs in through a browser and prints the account email. Whether the sign-up form requires a card is unverified. No phone or identity document is named.
- interface: unknown
- limits:
  - request-rate: the free path is a set of $0.00-per-token models; paid models run from $0.05 to $5.00 an input million tokens [1]
  - write-gated (binding): there is no machine to rent: the product runs a model, so a free model is the whole free tier [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the models page was read on 2026-10-22. It is a model catalogue with per-token prices and several $0.00 rows, and it states no machine rate or credit. The USD 5 the record carried is not on it
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the unit is a token, not a second; there is no session to reap
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the model documentation was read on 2026-10-22 and is a per-model price and capability table: 'Apodex 1.1 Mini (free) openrouter/apodex/apodex-1.1-mini:free 262K $0.00 / $0.00' beside 'Claude Haiku 5.5 $0.10 / $0.50'. It prices models, not machines
  - [2] 2026-11-04: the login page offers only GitHub and Google, so the identity is an email account behind one of them | capture: sha256:dac2585328cf744b9784daa1c2d6239da6342fd224342a9fadb9b540c07ac88a | quote: GitHub Google
  - [3] 2026-11-04: the signed-in account is identified by an email address | capture: sha256:42a784030e7164a7a7278a6bd19d216a78af07eb3ec0c55285e47ed5ab083915 | quote: "account": { "email": " ada@example.com" }
  - [3] 2026-11-04: sign-in is a browser approval of the account, not a separate registration form | capture: sha256:42a784030e7164a7a7278a6bd19d216a78af07eb3ec0c55285e47ed5ab083915 | quote: The CLI opens your browser, you approve, and it saves the sign-in on this machine.
- sources:
  - [1] https://www.dexto.ai/docs/models/
  - [2] https://app.dexto.ai/login
  - [3] https://www.dexto.ai/docs/cli/sign-in/
