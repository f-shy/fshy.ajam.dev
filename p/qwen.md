# Qwen Code

> qwen.ai | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qwen/ | JSON https://fshy.ajam.dev/api/v1/entity/qwen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qwen Code

- `coding-subs/qwen-code` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category BYOK coding agent
- needs card no, phone no, ID no, institution no | verified 2026-10-30T17:28:48.227Z (live) | stale on 2026-11-30
- url https://qwen.ai/qwencode
- free tier: open-source agent for the terminal; bring an OpenAI, Anthropic or Gemini compatible key; the free Qwen OAuth route was discontinued on 2026-04-15 | unit: none | metered on: none | read on: 2026-10-29 | source: [1] | note: the agent costs nothing; the key it is given is the bill
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: anonymous | detail: none to install or run the CLI; the npm package and the standalone install script download with no credential, and each endpoint key carries that endpoint's own registration cost; the qwen.ai account was needed only for the Qwen OAuth route, closed on 2026-04-15
- interface: cli
- limits note: no quota binds the agent itself; the provider of the chosen endpoint serves and meters the usage, among them the vendor's QwenCloud (a Token Plan with a monthly Credit quota, or a pay-as-you-go Standard API Key) and Alibaba ModelStudio (a Coding Plan with a weekly quota); the free Qwen OAuth route closed on 2026-04-15
- binding note: no vendor quota binds: the agent is free software and the endpoint it is given sets every limit, since the free Qwen OAuth route closed
- interface detail: a terminal agent; multi-protocol, so any OpenAI, Anthropic or Gemini compatible base URL works
- tooling: the user installs and runs the qwen CLI (npm package @qwen-code/qwen-code, which needs Node.js 22 or later, or the vendor's standalone install script) on any machine, rented or free ones included, and gives it an endpoint key
- composes with: the agent pairs with a key of a built-in provider (DeepSeek, Grok, MiniMax, Z.AI, Kimi, Idealab, ModelScope, OpenRouter, Requesty) or with any OpenAI, Anthropic or Gemini compatible endpoint, so a free endpoint recorded under inference makes the whole stack free; the key-free Qwen OAuth route closed on 2026-04-15
- reliability: the vendor cut the free Qwen OAuth quota from 1,000 to 100 requests per day and closed the route on 2026-04-15; cached OAuth tokens may work briefly and new requests are rejected
- notes: The free Qwen OAuth quota was discontinued on 2026-04-15. The /auth options are now QwenCloud, Alibaba ModelStudio, third-party providers and a custom provider, so the agent's cost is the endpoint it is pointed at. The qwen.ai landing page still offers Qwen OAuth sign-in; the auth documentation, last updated on October 22, 2026, says the route is closed.
- evidence note: the vendor's auth documentation states the end of the free OAuth tier and the current /auth routes; the anonymous install path was measured with unauthenticated GETs of the npm tarball and the install script; capacity belongs to the endpoint chosen and is not measured here
- self hosted: yes
- evidence:
  - [2] 2026-10-22: Qwen Code is an open-source terminal agent that supports OpenAI, Anthropic and Gemini compatible APIs or Qwen OAuth sign-in
  - [1] 2026-10-29: the free Qwen OAuth tier was discontinued on 2026-04-15 and new requests are rejected | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: The Qwen OAuth free tier was discontinued on 2026-04-15. Existing cached tokens may continue working briefly, but new requests will be rejected.
  - [1] 2026-10-29: the current /auth options are QwenCloud, Alibaba ModelStudio, Third-party Providers and Custom Provider | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: choose one of the current options (QwenCloud, Alibaba ModelStudio, Third-party Providers, or Custom Provider) instead
  - [1] 2026-10-30: the /auth dialog connects nine built-in third-party providers by API key | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: Third-party Providers**: choose a built-in provider and connect with an API key (DeepSeek, Grok, MiniMax, Z.AI, Kimi, Idealab, ModelScope, OpenRouter, Requesty).
  - probe:registry.npmjs.org/@qwen-code/qwen-code/-/qwen-code-0.26.4.tgz 2026-10-30: an unauthenticated GET of the agent's npm tarball answers 200 and streams the package: no account is needed to install it | capture: sha256:76dae1e3295c8478f8a192258a290ed7641e79fcde4562d715caaef75e4b064b | quote: "status": 200
  - [1] 2026-10-30: the qwen.ai account requirement belongs to the discontinued Qwen OAuth section of the auth page | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: Requirements**: a `qwen.ai` account + internet access (at least for the first login).
  - [3] 2026-10-30: the agent installs from npm as @qwen-code/qwen-code and needs Node.js 22 or later | capture: sha256:d351b8a55481da82b38f27ff4da2dc1852402e3bef5255e1c215a2cfb9e1755d | quote: NPM** (requires [Node.js 22+](https://nodejs.org/)):
  - [4] 2026-10-30: the vendor's repository announced the closure of the free Qwen OAuth entry point on 2026-04-15 | capture: sha256:bdc214bc0e00441559aa45fa733060f6bcfbfd6522eacd2a1bd8dc7c41b2e308 | quote: Phase out free tier: Completely close the Qwen OAuth free entry point on 2026-04-15
  - [1] 2026-10-30: Qwen OAuth is no longer offered in the /auth dialog and its free tier ended on 2026-04-15 | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: Qwen OAuth** is no longer a selectable dialog entry — its free tier was discontinued on 2026-04-15
  - [1] 2026-10-30: the agent accepts any OpenAI, Anthropic or Gemini compatible endpoint, so the endpoint sets the limits | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: Custom Provider**: manually connect a local server, proxy, or unsupported provider — supports OpenAI, Anthropic, Gemini, and other compatible endpoints.
  - [1] 2026-10-30: the free Qwen OAuth tier ended on 2026-04-15; cached tokens may work briefly and new requests are rejected | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: The Qwen OAuth free tier was discontinued on 2026-04-15. Existing cached tokens may continue working briefly, but new requests will be rejected.
  - [2] 2026-10-30: the qwen.ai landing page still offers Qwen OAuth sign-in although the auth documentation says the route is closed | capture: sha256:cd72ceb86270f4882cfbd15e17e02198a7bf77b788065d8fb3848a79ec3452d4 | quote: Use OpenAI / Anthropic / Gemini-compatible APIs, or sign in with Qwen OAuth.
  - [4] 2026-10-30: before the closure the vendor cut the free OAuth quota from 1,000 to 100 requests per day | capture: sha256:bdc214bc0e00441559aa45fa733060f6bcfbfd6522eacd2a1bd8dc7c41b2e308 | quote: Reduce daily free quota: Change from 1,000 requests/day to 100 requests/day effective immediately
  - [5] 2026-10-30: the vendor's troubleshooting page also states Qwen OAuth is unavailable from 2026-04-15 | capture: sha256:c4cafa144f91021659faa69b3482c2ab849e18fae53c95742717c3ed2855674d | quote: Qwen OAuth is no longer available as of April 15, 2026.
  - probe:qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh 2026-10-30: an unauthenticated GET of the vendor's standalone install script answers 200 with the full script | capture: sha256:8ee265cb52e8d51045940a9a847d568b470374b4a9743675c4aeb37b7fdb2da2 | quote: "status": 200
  - [1] 2026-10-30: QwenCloud, the vendor's recommended /auth entry, serves key usage on a Token Plan with a monthly Credit quota or a pay-as-you-go Standard API Key | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: QwenCloud: official recommended setup. Opens a sub-menu with Token Plan (subscription with a monthly Credit quota · dedicated endpoint, Personal and Team editions) or Standard API Key (pay-as-you-go).
  - [1] 2026-10-30: Alibaba ModelStudio serves key usage on a Coding Plan with a weekly quota, a usage-billed Token Plan or a Standard API Key | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: Alibaba ModelStudio: opens a sub-menu with Coding Plan (for individual developers · weekly quota included), Token Plan (for teams and companies · usage-based billing with a dedicated endpoint), or Standard API Key (connect with an existing ModelStudio API key).
  - [1] 2026-10-30: the agent connects to any OpenAI, Anthropic or Gemini compatible endpoint, unchanged | capture: sha256:9b4d0604fdd4cda085eeebcdf4cb2cf717014c36d0781dbce1e326227abe144e | quote: Custom Provider**: manually connect a local server, proxy, or unsupported provider — supports OpenAI, Anthropic, Gemini, and other compatible endpoints.
- sources:
  - [1] https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/
  - [2] https://qwen.ai/qwencode
  - [3] https://github.com/QwenLM/qwen-code
  - [4] https://github.com/QwenLM/qwen-code/issues/3203
  - [5] https://qwenlm.github.io/qwen-code-docs/en/users/support/troubleshooting/
