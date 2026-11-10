# Qwen Code OAuth free tier

> qwenlm.github.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qwenlm-github-io/ | JSON https://fshy.ajam.dev/api/v1/entity/qwenlm-github-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qwen Code OAuth free tier

- `inference/qwen-code-oauth` | dead | evidence documented | binding request-rate | category coding agent CLI, OAuth login
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:19.143Z (live) | stale on 2026-11-28
- url https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/
- free tier: discontinued on 2026-04-15: Qwen OAuth is no longer a selectable /auth entry and new requests are rejected | unit: none | metered on: none | read on: 2026-10-28 | source: [1] | note: the replacement routes on the same page are the Alibaba Cloud Coding Plan, which is a fixed monthly fee, or a third-party key
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a qwen.ai account; unverified: the page does not say what creating one requires
- interface: cli
- limits:
  - request-rate (binding): no free quota is served: the Qwen OAuth free tier was discontinued on 2026-04-15 [1]
- binding note: nothing is served on the OAuth route
- interface detail: qwen CLI; the OAuth browser login cannot be completed in non-interactive or headless environments
- tooling: qwen CLI (Qwen Code), /auth to choose a provider
- composes with: nothing chains on the OAuth route; the same page lists Third-party Providers and Custom Provider entries for the agent, and the agent is recorded at coding-subs/qwen-code
- reliability: existing cached tokens may continue working briefly but new requests are rejected
- notes: The coding-subs/qwen-code record covers the agent and its bring-your-own-key routes, which are unaffected; only the OAuth free route is closed here.
- evidence note: the vendor's authentication page states the end date and the rejection; no request was made because the route is closed
- evidence:
  - [1] 2026-10-28: the free Qwen OAuth tier was discontinued on 2026-04-15 and new requests are rejected | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: The Qwen OAuth free tier was discontinued on 2026-04-15. Existing cached tokens may continue working briefly, but new requests will be rejected.
  - [1] 2026-10-28: Qwen OAuth is no longer a selectable dialog entry in the CLI | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: Qwen OAuth** is no longer a selectable dialog entry — its free tier was discontinued on 2026-04-15
  - [1] 2026-10-28: the OAuth route required a qwen.ai account and internet access for the first login | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: Requirements: a `qwen.ai` account + internet access (at least for the first login).
  - [1] 2026-10-28: the OAuth browser login cannot be completed headless | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: In non-interactive or headless environments (e.g., CI, SSH, containers), you typically cannot complete the OAuth browser login flow.
  - [1] 2026-10-28: the current /auth options are QwenCloud, Alibaba ModelStudio, Third-party Providers and Custom Provider | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: choose one of the current options (QwenCloud, Alibaba ModelStudio, Third-party Providers, or Custom Provider) instead.
  - [1] 2026-10-28: the replacement Coding Plan is a fixed monthly fee | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: Subscribe to the Coding Plan with a fixed monthly fee, then configure Qwen Code to use the dedicated endpoint and your subscription API key.
- sources:
  - [1] https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/
