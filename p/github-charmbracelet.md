# Crush

> github.com | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-charmbracelet/ | JSON https://fshy.ajam.dev/api/v1/entity/github-charmbracelet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Crush

- `coding-subs/crush` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category BYOK coding agent
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:28:03.757Z (live) | stale on 2026-12-05
- url https://github.com/charmbracelet/crush
- free tier: the agent is free to use under FSL-1.1-MIT with keys for many providers; its first-party provider Charm Hyper has no free plan ('We've retired the monthly free Hypercredit allowance') and starts at Shred Diet, USD 10 a month for 180 Hypercredits a week | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: the agent imposes no quota; with Hyper as the endpoint, the weekly and five-hour Hypercredit windows bind
- per-object cap: not applicable: a coding agent meters nothing itself
- retention: not applicable
- egress: not applicable: the chosen endpoint serves the inference | metered: no
- identity: anonymous | detail: no account for the agent, which installs from package managers; Hyper sign-up is 'Sign up with Google, GitHub, or email', and a Shred plan or prepaid credit is billed through Stripe
- interface: cli
- limits note: the agent carries no vendor-imposed usage cap, since the vendor serves no inference through it unless Hyper is chosen; Hyper's weekly and five-hour Hypercredit limits then bind
- binding note: the agent has no quota of its own; the endpoint's quota decides capacity
- interface detail: a terminal UI. Headless: `crush run "prompt"` runs non-interactively, `--continue` (`-C`) and `--session` (`-s`) resume a session, `crush session list --json` lists sessions, and `--yolo` skips every permission prompt
- tooling: the user installs and runs the crush binary (Homebrew, npm, winget, scoop, apt, yum or go install) on a rented or free machine; providers come from the Catwalk model list or a custom OpenAI- or Anthropic-compatible entry, and the HYPER_API_KEY variable selects Hyper
- composes with: Charm Hyper is the first-party endpoint at hyper.charm.land/v1 with OpenAI and Anthropic protocols: Shred Diet USD 10 a month buys 180 Hypercredits a week (about USD 9.00 of inference at 5 cents a credit), 100 per five hours and 2 concurrent requests; Shred Classic is USD 20 for 250; prepaid credits start at USD 5. Any key in inference/ works instead
- reliability: no reliability event recorded; Shred subscriptions on Hyper are not zero-data-retention, while Business plans and prepaid credits are
- notes: Not a subscription by itself: the agent is free and source-available, and its first-party plan Charm Hyper is a separate hosted offer with no free tier and a USD 10 entry plan, under USD 20. Hyper models on the probe include prism, kimi-k3, glm-5.3, glm-5.3-flash, deepseek-v4.1-flash, qwen3.8-max, minimax-m3 and gpt-oss-120b.
- evidence note: licence, headless command, provider support and the Hyper plan table are quoted from first-party pages read on 2026-10-30, and the Hyper model list from a probe of its unauthenticated models endpoint. Hyper's per-model token price inside a Hypercredit was not converted to tokens per week.
- self hosted: yes
- evidence:
  - [1] 2026-10-30: the agent takes keys for many third-party providers | capture: sha256:3de1bde6575792c269eb25f13b7b14885848d65f43fc13b3738fa25b05a5ab83 | quote: You can also use Crush with many other providers such as Anthopic, OpenAI, Gemini, OpenRouter and so on.
  - [1] 2026-10-30: Charm Hyper is the first-party, subscription-based provider for the agent | capture: sha256:3de1bde6575792c269eb25f13b7b14885848d65f43fc13b3738fa25b05a5ab83 | quote: is the official Crush provider. It’s subscription-based and optimized for Crush.
  - [1] 2026-10-30: a flag removes every permission prompt for unattended runs | capture: sha256:3de1bde6575792c269eb25f13b7b14885848d65f43fc13b3738fa25b05a5ab83 | quote: You can also skip all permission prompts completely by running Crush with the `--yolo` flag.
  - [2] 2026-10-30: the agent is licensed under FSL-1.1-MIT | capture: sha256:c9e8c1c4b5371e1046df69760c6b1187dffccffba81bb35bf9b7ba04dbe6fd8f | quote: Functional Source License, Version 1.1, MIT Future License
  - [3] 2026-10-30: `crush run` is the non-interactive mode, and v0.50.0 added session continuation to it | capture: sha256:e9c4ea548d37043f899e091b798ba0062d3926d8924a15fc64dcaaa812e647cb | quote: Did you know that you can Crush in a non-interactive manner? It's easy as `crush run`.
  - [4] 2026-10-30: Shred Diet is USD 10 a month for 180 Hypercredits a week, 100 per five hours and 2 concurrent requests | capture: sha256:c744c3a69dece055a87c6f3fac13322665d925c5e413cf215fd688984f6e75ab | quote: | Shred Diet | $10 / month | 180 | ≈ $9.00 | 100 | 2 |
  - [4] 2026-10-30: Shred Classic is USD 20 a month for 250 Hypercredits a week | capture: sha256:c744c3a69dece055a87c6f3fac13322665d925c5e413cf215fd688984f6e75ab | quote: | Shred Classic | $20 / month | 250 | ≈ $12.50 | 150 | 3 |
  - [4] 2026-10-30: Hyper plans and credits are paid through Stripe | capture: sha256:c744c3a69dece055a87c6f3fac13322665d925c5e413cf215fd688984f6e75ab | quote: Billing is powered by Stripe
  - [5] 2026-10-30: Hyper has no free plan | capture: sha256:c183ba6d8152850e3d310fb8ecd5c0d3533a0608ca36080e97da81d646b9a30c | quote: We've retired the monthly free Hypercredit allowance.
  - [5] 2026-10-30: Shred plans are not zero-data-retention | capture: sha256:c183ba6d8152850e3d310fb8ecd5c0d3533a0608ca36080e97da81d646b9a30c | quote: Shred subscriptions don't include ZDR.
  - [6] 2026-10-30: the Hypercredit allowance resets weekly, and one Hypercredit is 5 cents | capture: sha256:046e23487292f1ac2d6085feb1613ed1045a62afb61067555355071c19e49b91 | quote: Hypercredits refresh every week at Sunday 00:00 UTC.
  - [7] 2026-10-30: Hyper sign-up needs a Google or GitHub login or an email address | capture: sha256:595e192a9b02a4847b0cd0f0e30ff550b00a16a838d844cf303c6091c43afcd0 | quote: Sign up with Google, GitHub, or email.
  - [8] 2026-10-30: the agent signs in to Hyper during its first run or reads HYPER_API_KEY | capture: sha256:45dda5a91fda2a374309ce8fc84767797fab3872850cbbf3ef4bd5da33dc472c | quote: Crush has first-class support for Hyper.
  - probe:https://hyper.charm.land/v1/models 2026-10-30: the unauthenticated Hyper models endpoint answered 200 with 23 model ids, among them kimi-k3, glm-5.3, deepseek-v4.1-flash, qwen3.8-max and gpt-oss-120b | capture: sha256:cc4d593d1ed20425a984d7e86b3921068e50df20013a85cc25040b9c4a353d61 | quote: "id": "kimi-k3"
  - [5] 2026-11-04: Hyper still has no free plan; the free route is the agent with other keys | capture: sha256:c183ba6d8152850e3d310fb8ecd5c0d3533a0608ca36080e97da81d646b9a30c | quote: We've retired the monthly free Hypercredit allowance.
- sources:
  - [1] https://github.com/charmbracelet/crush
  - [2] https://github.com/charmbracelet/crush/blob/main/LICENSE.md
  - [3] https://github.com/charmbracelet/crush/releases/tag/v0.50.0
  - [4] https://hyper.charm.land/docs/plans-billing.md
  - [5] https://hyper.charm.land/faq
  - [6] https://hyper.charm.land/
  - [7] https://hyper.charm.land/docs/
  - [8] https://hyper.charm.land/docs/coding-agents/crush.html
