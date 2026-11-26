# Zapier

> zapier.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zapier/ | JSON https://fshy.ajam.dev/api/v1/entity/zapier.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zapier

- `dev-services/zapier` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted no-code workflow automation | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:37:46.631Z (live) | stale on 2026-12-03
- url https://zapier.com/pricing
- free tier: Free: 100 tasks/mo; unlimited Zap workflows, Tables and Forms; two-step Zap workflows; 15 min polling | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: A task is a successful Zap step; each programmatic call through Zapier MCP also uses tasks. Multi-step Zaps, webhooks, filters and paths are on Pro. Code steps get 1 second of included runtime per step on Free. The allowance resets monthly. New accounts get a 14-day Professional trial with no credit card.
- per-object cap: not stated on the pages read
- retention: Zap history: a maximum of 60 days of Zap run data guaranteed, up to 10,000 runs displayed; Zap content and run metadata 7 days in logs and 29-69 days in the account | source: [2]
- egress: not applicable: actions call third-party apps; no traffic allowance is published | metered: no | source: [1]
- identity: email | detail: The sign-up form asks for a work email, first name, last name and a password of at least 14 characters, or Google sign-in; the Professional trial needs no credit card. Whether an address at a public mail domain is accepted is unverified.
- interface: cli
- limits:
  - volume-quota (binding): 100 tasks per month [1]
  - request-rate: polling every 15 minutes [1]
  - retention-clamped: at most 60 days of Zap run data, up to 10,000 runs [2]
  - volume-quota (binding): 2 tasks per successful Zapier MCP tool call, from the plan's task allowance; a failed call uses none [3]
  - volume-quota (binding): 1 task per Zapier SDK action, fetch call or inbox-lease trigger outside Zapier, billed from December 1, 2026 [4]
- limits note: Free Zaps are two-step (one trigger, one action). Code steps get 1 second of included runtime per step on Free. Copilot has a daily message limit on Free.
- binding note: 100 tasks a month runs out first for any Zap that fires more than a few times a day.
- interface detail: Zapier MCP takes the Model Context Protocol over Streamable HTTP only at one endpoint, with OAuth from the MCP client or a connection token; the TypeScript SDK and its CLI give programmatic access to 9,000+ app integrations. The interface vocabulary has no MCP or SDK term, so the list holds cli, which names the SDK CLI only.
- endpoint: https://mcp.zapier.com/api/v1/connect
- tooling: an MCP client against Zapier MCP; the Zapier TypeScript SDK and its CLI
- composes with: Moves data between hosted app accounts on a 15-minute poll within 100 tasks a month, so it fits low-volume glue between SaaS accounts, not a scheduler or a compute host.
- reliability: With pay-per-task billing off, usage stops at the task limit until the next cycle; the feature table lists pay-per-task billing for paid plans only.
- evidence note: Plan limits, retention and sign-up fields are read on first-party pages; a Zap run and an MCP call are not measured.
- evidence:
  - [1] 2026-10-30: the free plan has 100 tasks a month, two-step Zaps and basic MCP access | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: | Free | Trying automation solo | 100 tasks/mo; unlimited Zap workflows/Tables/Forms; two-step Zap workflows; Copilot (daily limit); basic access to AI products (Agents, Chatbots, MCP) |
  - [1] 2026-10-30: the free plan includes 100 tasks a month | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: + Free includes 100 tasks/month.
  - [1] 2026-10-30: the free plan polls every 15 minutes | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: | Polling time | How often Zapier checks for new data to start your Zap. | 15 min | 2 min | 1 min | 1 min |
  - [1] 2026-10-30: Zap steps and MCP calls both use tasks | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: 2. Usage — each successful step in a Zap workflow and each programmatic call (e.g. Zapier MCP) consumes tasks from that allowance.
  - [1] 2026-10-30: the task allowance resets monthly | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: + Self-serve (Free, Pro, Team): task allowance resets monthly, even on an annual subscription.
  - [1] 2026-10-30: multi-step Zaps, webhooks, filters and paths are Pro features | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: | Professional (Pro) | Individuals needing the full platform | Multi-step Zap workflows; unlimited premium apps; webhooks; AI by Zapier + AI fields; filters & paths; email + live chat support (live chat on 2,000+ task tiers) |
  - [1] 2026-10-30: Code steps get 1 second of included runtime per step on Free | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: | 1 second included runtime per step |
  - [1] 2026-10-30: Zapier MCP is on every plan, Free included | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: | [Zapier MCP](http://zapier.com/mcp) | Developers can give their AI tools access to thousands of apps instantly with Zapier MCP—no complex API integrations required. | ✓ | ✓ | ✓ | ✓ |
  - [1] 2026-10-30: new accounts get a 14-day Professional trial with no credit card | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: + Free trial: new accounts get a 14-day free trial of Professional (no credit card required).
  - [1] 2026-10-30: with pay-per-task off, usage stops at the task limit until the next cycle; the feature table marks pay-per-task billing as not included on Free | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: PPT disabled: usage stops once you reach your task limit, until the next cycle.
  - [5] 2026-10-30: the sign-up form asks for a work email | capture: sha256:30e7362e1a7b1cfed2deda57783bed5484fcd7956976271f639c9459b7f1a4a9 | quote: Work email *
  - [5] 2026-10-30: the sign-up password must be at least 14 characters | capture: sha256:30e7362e1a7b1cfed2deda57783bed5484fcd7956976271f639c9459b7f1a4a9 | quote: - Not met: Must be at least 14 characters
  - [5] 2026-10-30: Google sign-in is offered as an alternative | capture: sha256:ed06360aae7635803ba661ea004972c59121e2bcc0d3574c8f9fec99bd3ff74d | quote: [Sign up with Google](https://zapier.com/google-sso/start?scopes=basic&next=%2Fapp%2Fonboarding)
  - [5] 2026-10-30: the sign-up form asks for first and last name | capture: sha256:ed06360aae7635803ba661ea004972c59121e2bcc0d3574c8f9fec99bd3ff74d | quote: Last name *
  - [2] 2026-10-30: Zap history keeps at most 60 days of run data and shows up to 10,000 runs | capture: sha256:7862935493b4fd26e0a3453878d5a1d3a29ecb131ebb759c5f9198541dd3d3dc | quote: Zapier can only guarantee a maximum of 60 days of Zap run data in your Zap history and will display up to 10,000 runs.
  - [6] 2026-10-30: Zap content and run metadata are kept 7 days in logs and 29-69 days in the account | capture: sha256:dcb28a2247fb1d5d39dc8657c09986274a2e975e7cb050199f6d5602b9cae673 | quote: 7 days in logs. 29-69 days in your Zapier account.
  - [7] 2026-11-01: MCP clients connect to Zapier MCP at https://mcp.zapier.com/api/v1/connect | capture: sha256:ad698800cd0fb601c43d69a1aecb1ed87106e494e8e3236618225c0ca9c5fe26 | quote: | Authorization header (preferred) | `Authorization: Bearer YOUR_CONNECTION_TOKEN` sent to `https://mcp.zapier.com/api/v1/connect` |
  - [3] 2026-11-01: a successful Zapier MCP tool call uses 2 tasks at a fixed rate and a failed call uses 0 | capture: sha256:446f4dce3b10e350e42d7d80333980f7de3fe8b81bd84115759ecb95ec65ed15 | quote: | Tasks per successful tool call | 2 (fixed rate) | ... | Tasks per failed tool call | 0 |
  - [4] 2026-11-01: SDK actions, fetch calls and inbox-lease triggers outside Zapier use 1 task each once billing starts on December 1, 2026 | capture: sha256:f51db836988fd22b9716e686d0ecb2a9764b289d397aa6b76d786876d6bf40d4 | quote: Billing for Next Gen Zaps and the Zapier SDK starts at 12 pm ET (17:00 UTC) on December 1, 2026. ... | Outside Zapier, such as on your own servers, in scripts, or in cron jobs | SDK actions, fetch calls, and inbox-lease triggers | 1 task each |
  - [8] 2026-11-02: the vendor lists a TypeScript SDK and a CLI for programmatic access to its 9,000+ app integrations | capture: sha256:93c711d4f96403f37481e88fb392ab70b00b48595811f3081deb93968c29a0a3 | quote: The TypeScript SDK and CLI for coding agents and developers who need programmatic access to Zapier's 9,000+ app integrations.
  - [8] 2026-11-02: Zapier MCP has one endpoint, takes Streamable HTTP only and authenticates by OAuth in the MCP client or by a connection token | capture: sha256:93c711d4f96403f37481e88fb392ab70b00b48595811f3081deb93968c29a0a3 | quote: - [How Zapier MCP connections work](https://docs.zapier.com/mcp/overview/how-connections-work.md): One endpoint, Streamable HTTP only, and the two auth paths: OAuth inside the MCP client, or a connection token.
  - [7] 2026-11-01: Zapier MCP supports only the Streamable HTTP transport | capture: sha256:ad698800cd0fb601c43d69a1aecb1ed87106e494e8e3236618225c0ca9c5fe26 | quote: Zapier MCP supports the Model Context Protocol over Streamable HTTP only.
  - [9] 2026-11-01: the Zapier SDK needs a Zapier account, and a free-tier account works | capture: sha256:892746fa98acab3b0a8643488ea7c05f5851d52bed6af69371f32e3575069bbc | quote: * A [Zapier account](https://zapier.com/sign-up) (free tier works). Or create one using the CLI in Step 3
  - [10] 2026-11-01: the Zapier SDK is free in open beta until billing starts on December 1, 2026 | capture: sha256:1becf1a31328aa639d1a0e765a6764c0418b36c0379b3d7cddc61c6295159d7b | quote: In open beta, free until billing starts on December 1, 2026.
  - [11] 2026-11-01: a new Zapier account needs no payment method for its trial and does not auto-upgrade when the trial ends | capture: sha256:734e0080223a7db888b6b9002b48c3df89394d50e973ddda52b2944782f71db0 | quote: No payment method is required, and your account will not auto-upgrade when the trial ends.
  - [12] 2026-11-01: a Zapier Staff reply dated 2024-12-11 says any accessible email address, not already linked to a Zapier account, can be used to create a test account | capture: sha256:c59b3656199d2681289412bc783bbaefba5312783a7f788618ad175f3eff90de | quote: Yes, you can use any accessible email address to create a test account, as long as it's not already linked to an existing Zapier account.
  - [13] 2026-11-01: a third-party review dated 2023-05-01 reports signing up for Zapier with a Gmail account, without saying whether through the work-email field or Google sign-in; the current form is not tested | capture: sha256:9872b2959d2c17db7a66cb701d831fce7b53b23470bdd75b859238da83ae729c | quote: I was able to sign up with a Gmail account.
  - [14] 2026-11-01: a third-party review dated 2023-11-23 reports signing up for Zapier with a personal email address on the email form; the current form is not tested | capture: sha256:0647a744d2409594264da04ec1cafd7edaa8cc951792203b7d50b468ddf0bbc5 | quote: But I tried to sign up with a personal one, and it works.
  - [1] 2026-11-01: the free plan has 100 tasks a month, two-step Zaps and basic access to MCP | capture: sha256:c09f8efc28c528317ac9af318736b9974440b0bc54a00c8900b814871d80ebc0 | quote: | Free | Trying automation solo | 100 tasks/mo; unlimited Zap workflows/Tables/Forms; two-step Zap workflows; Copilot (daily limit); basic access to AI products (Agents, Chatbots, MCP) |
  - [5] 2026-11-01: the sign-up form asks for a work email | capture: sha256:3fd0501e358f4aba21ed16ca00c6fc2af54c76557e6945d5eba2549a5bf5fa22 | quote: Work email
- sources:
  - [1] https://zapier.com/pricing
  - [2] https://help.zapier.com/hc/en-us/articles/8496291148685-View-and-manage-your-Zap-history
  - [3] https://docs.zapier.com/mcp/overview/usage
  - [4] https://help.zapier.com/hc/en-us/articles/49965546559117-How-Next-Gen-Zaps-and-the-Zapier-SDK-are-billed
  - [5] https://zapier.com/sign-up
  - [6] https://zapier.com/legal/data-retention-deletion
  - [7] https://docs.zapier.com/mcp/overview/how-connections-work
  - [8] https://docs.zapier.com/llms.txt
  - [9] https://docs.zapier.com/sdk/quickstart
  - [10] https://docs.zapier.com/sdk
  - [11] https://help.zapier.com/hc/en-us/articles/8496197192461-Get-started-with-your-free-Zapier-trial
  - [12] https://community.zapier.com/general-discussion-13/how-can-i-create-a-test-account-46000
  - [13] https://ozenguner.com/2023/05/01/product-on-trial-1-zapier/
  - [14] https://lascabritas.substack.com/p/decoding-zapiers-activation-flow
