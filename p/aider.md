# Aider

> aider.chat | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aider/ | JSON https://fshy.ajam.dev/api/v1/entity/aider.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aider

- `coding-subs/aider` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category BYOK coding agent
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:28:03.757Z (live) | stale on 2026-12-05
- url https://aider.chat/
- free tier: free and open source under the Apache License 2.0; the agent works with any model behind the user's own key, and its docs name free API providers: 'OpenRouter offers free access to many models, with limitations on daily usage' | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: the agent costs nothing and imposes no quota; the endpoint it calls is the bill and the binding limit
- per-object cap: not applicable: a coding agent meters nothing itself
- retention: not applicable
- egress: not applicable: the chosen endpoint serves the inference | metered: no
- identity: anonymous | detail: no account is needed to run the agent, which installs from PyPI with 'python -m pip install aider-install'; each endpoint it calls carries its own identity cost
- interface: cli
- limits note: no vendor-imposed usage cap: the vendor serves no inference, so the quota of the chosen endpoint binds
- binding note: the agent has no quota of its own; the endpoint's quota decides capacity
- interface detail: a terminal program. Headless: `aider --message` (`-m`) or `--message-file` runs one instruction, applies the edits and exits; `--yes` answers every confirmation; a Python API (`Coder.create`) exists but is documented as unsupported
- tooling: the user installs and runs the aider CLI (pip `aider-install`, uv, pipx or the install script) on a rented or free machine, and points it at an endpoint with `--model` and `--api-key`; OpenAI-compatible endpoints, OpenRouter and GitHub Copilot's api.githubcopilot.com are documented
- composes with: pairs with any endpoint in inference/ and with a GitHub Copilot subscription, whose calls through aider are billed to that subscription; the agent is free and the tokens are not
- reliability: the latest PyPI release is 0.86.2, uploaded 2026-02-12; the release notes list further unreleased changes on the main branch
- notes: Not a subscription: a free agent with no vendor-served inference. It answers the question only as the USD 0 harness for a free or cheap endpoint chosen from inference/.
- evidence note: licence, install path, headless flags and the free-provider guidance are quoted from the project's own pages read on 2026-10-30. Capacity belongs to the endpoint chosen, so nothing about quota can be measured on the agent.
- self hosted: yes
- evidence:
  - [2] 2026-10-30: the agent installs from PyPI with no account | capture: sha256:41b2cec5ccf40d12ddd593e4a6c140ad5912033157001e6b6fb571cd6b60c3b4 | quote: python -m pip install aider-install
  - [1] 2026-10-30: the docs name free API providers the agent works with, OpenRouter with daily limits among them | capture: sha256:5cd7dcb080554bcba8b7e3df1eda965983d7bb2966d8caf21421b61a8915fd15 | quote: OpenRouter offers free access to many models
  - [3] 2026-10-30: `aider --message` runs non-interactively and exits | capture: sha256:d6cf1eec737eec8954c4c62b904df6e06fa9aa84b27e93f53a3a81e13f8295da | quote: It will do that one thing, apply the edits to the files and then exit.
  - [3] 2026-10-30: the Python API is unsupported; the CLI flag is the stable headless route | capture: sha256:d6cf1eec737eec8954c4c62b904df6e06fa9aa84b27e93f53a3a81e13f8295da | quote: The python scripting API is not officially supported or documented, and could change in future releases without providing backwards compatibility.
  - [4] 2026-10-30: the agent is licensed under the Apache License 2.0 | capture: sha256:6c5691d020bcfb35d27cf0ddaaf7b6497da79183ce897bc61405870927c25d89 | quote: Version 2.0, January 2004
  - [5] 2026-10-30: a Copilot subscription can serve as the endpoint | capture: sha256:2580c7499cc6ee413f31157b71603d65da7832bca143e77b4eb010045c6e5eb7 | quote: Calls made through aider are billed through your Copilot subscription
  - [6] 2026-10-30: the latest release on PyPI is 0.86.2, whose files were uploaded on 2026-02-12 | capture: sha256:58eacf57856e303ade64fdec05746bfe4a0e19142fc0007b2ddaff37cc24dcce | quote: "version":"0.86.2"
  - [7] 2026-10-30: the main branch carries unreleased changes after 0.86.2, so development continues | capture: sha256:32f0318a17f1c4461689c750d728dca6a8625f2db049f9c978444fdc388ee6f4 | quote: Added support for GPT‑5.3/5.4 model variants across OpenAI, Azure, and OpenRouter, plus GPT‑4.1‑nano.
  - [1] 2026-11-04: the docs still name OpenRouter free models as a free endpoint | capture: sha256:5cd7dcb080554bcba8b7e3df1eda965983d7bb2966d8caf21421b61a8915fd15 | quote: OpenRouter offers free access to many models
- sources:
  - [1] https://aider.chat/docs/llms.html
  - [2] https://aider.chat/
  - [3] https://aider.chat/docs/scripting.html
  - [4] https://github.com/Aider-AI/aider/blob/main/LICENSE.txt
  - [5] https://aider.chat/docs/llms/github.html
  - [6] https://pypi.org/pypi/aider-chat/json
  - [7] https://aider.chat/HISTORY.html
