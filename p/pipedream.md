# Pipedream

> pipedream.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pipedream/ | JSON https://fshy.ajam.dev/api/v1/entity/pipedream.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pipedream

- `dev-services/pipedream` | qualifies-with-caveat | evidence documented | binding request-rate | category hosted integration platform (Connect API and MCP servers) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:37:46.632Z (live) | stale on 2026-12-03
- url https://pipedream.com/pricing
- free tier: Free, no credit card required: every feature in development, with a daily credit limit and at most 10 external users | unit: credits | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: A credit is 30 seconds of compute; running an action, an MCP tool call, a Connect proxy request and a deployed-trigger emit each use credits, while listing and configuration calls do not. The daily number of free credits is unverified: the documentation names a daily limit without a number, and the figure is behind a sign-up. Unused daily credits do not roll over. Production use with real external users needs the Startup plan. Workflows takes no new sign-ups and shuts down on March 31, 2027; Connect is not affected.
- per-object cap: not stated on the pages read
- retention: Workflows event history: 7 days of events on free tiers; Connect retention not stated on the pages read | source: [2] | note: All Workflows data is deleted by April 30, 2027.
- egress: not applicable: actions call third-party APIs; dedicated static egress IPs are on Business only | metered: no | source: [1]
- identity: email | detail: The sign-up form asks for a work email and a password, or Google or GitHub sign-in; the free plan needs no credit card.
- interface: rest, cli
- limits:
  - request-rate (binding): a daily credit limit on free workspaces; the number is unverified (behind a sign-up) [3]
  - volume-quota: 10 external users in the development environment [4]
- limits note: The production environment is not included on Free. Development mode is for the developer's own accounts. Workflows on free tiers time out at up to 300 seconds and test runtime is limited per day, but Workflows takes no new sign-ups.
- binding note: The daily credit cap binds first; the 10-user development limit matters only when serving others.
- interface detail: Connect SDKs and REST API at api.pipedream.com, MCP servers and the Connect proxy; the development environment is selected with an x-pd-environment header, and connecting an account in development needs a pipedream.com sign-in in the same browser.
- endpoint: https://api.pipedream.com/v1/connect/
- tooling: the Connect SDKs and REST API, an MCP client against Pipedream MCP servers, and the Pipedream CLI
- composes with: Supplies managed OAuth and prebuilt actions for 3,000+ APIs to a script or an agent working on the developer's own accounts, so it pairs with a scheduler or a compute host that runs the caller.
- reliability: Workflows is in maintenance mode with no new sign-ups and shuts down on March 31, 2027, with its data deleted by April 30, 2027; Connect is not affected.
- evidence note: Plan, environment limits, credit rules and the Workflows shutdown are read on first-party pages; the free daily credit number is not published and is behind a sign-up.
- evidence:
  - [1] 2026-10-30: the free plan needs no credit card | capture: sha256:a58cf9dfbd53973868e1618e3599f95b13e0ca91e0bc2d18da1b7dfdedab1ef4 | quote: Free, no credit card required
  - [1] 2026-10-30: the free plan covers every feature in development | capture: sha256:a58cf9dfbd53973868e1618e3599f95b13e0ca91e0bc2d18da1b7dfdedab1ef4 | quote: - Every feature, in development
  - [1] 2026-10-30: the production environment is not on Free | capture: sha256:a58cf9dfbd53973868e1618e3599f95b13e0ca91e0bc2d18da1b7dfdedab1ef4 | quote: | Production environment | Not included | Included | Included |
  - [1] 2026-10-30: MCP servers are on Free | capture: sha256:a58cf9dfbd53973868e1618e3599f95b13e0ca91e0bc2d18da1b7dfdedab1ef4 | quote: | MCP servers | Included | Included | Included |
  - [1] 2026-10-30: development gives free API, SDK and MCP access | capture: sha256:a58cf9dfbd53973868e1618e3599f95b13e0ca91e0bc2d18da1b7dfdedab1ef4 | quote: Development gives you full API, SDK, and MCP access to build and test, free.
  - [1] 2026-10-30: static egress IPs are on Business only | capture: sha256:a58cf9dfbd53973868e1618e3599f95b13e0ca91e0bc2d18da1b7dfdedab1ef4 | quote: | Dedicated static egress IPs | Not included | Not included | Included |
  - [3] 2026-10-30: free workspaces have a daily credit limit; no number is given | capture: sha256:9ff91c706fa71bde9e268496fa459680abd8b14534878d239dbd552825490412 | quote: * Daily credit limit: Free workspaces have a daily limit of free credits that cannot be exceeded
  - [3] 2026-10-30: a credit is 30 seconds of compute | capture: sha256:9ff91c706fa71bde9e268496fa459680abd8b14534878d239dbd552825490412 | quote: API operations that consume credits (1 credit per 30 seconds of compute time):
  - [3] 2026-10-30: Connect is reached through SDKs and APIs | capture: sha256:9ff91c706fa71bde9e268496fa459680abd8b14534878d239dbd552825490412 | quote: Pipedream Connect provides SDKs and APIs to let you easily add 3,000+ integrations to your app or AI agent.
  - [1] 2026-10-30: actions, MCP tool calls, proxy requests and deployed-trigger emits use credits | capture: sha256:a58cf9dfbd53973868e1618e3599f95b13e0ca91e0bc2d18da1b7dfdedab1ef4 | quote: Running an action, calling a tool through MCP, sending a request through the Connect proxy, and emitting an event from a deployed trigger each use 1 credit per 30 seconds of compute.
  - [1] 2026-10-30: listing and configuration calls use no credits | capture: sha256:a58cf9dfbd53973868e1618e3599f95b13e0ca91e0bc2d18da1b7dfdedab1ef4 | quote: Listing apps and accounts, configuring components, and other management calls don't use credits.
  - [1] 2026-10-30: production with real external users needs Startup | capture: sha256:a58cf9dfbd53973868e1618e3599f95b13e0ca91e0bc2d18da1b7dfdedab1ef4 | quote: Serving real external users in production requires Startup.
  - [2] 2026-10-30: Workflows test runtime is limited per day on Free | capture: sha256:859250b9f2c430eeed5f03e62685fd58f5a6c17956193a38fd6596e94632f30a | quote: You do not use credits testing workflows, but workspaces on the Free plan are limited to 750 of test runtime per day.
  - [5] 2026-10-30: unused daily credits do not roll over | capture: sha256:735a42def6939d37f5b1c325a8c82d33b3c7255b41ce1074a53084f85bbc791d | quote: On the Free tier, unused included daily credits under the daily limit are not rolled over to the next day.
  - [4] 2026-10-30: development is limited to 10 external users | capture: sha256:a56578b3b8492504418b54468148cad8417727d99319f622f3a2248eedddb5b5 | quote: * Maximum of 10 external users: The development environment is limited to 10 unique external user IDs.
  - [4] 2026-10-30: connecting an account in development needs a pipedream.com sign-in | capture: sha256:a56578b3b8492504418b54468148cad8417727d99319f622f3a2248eedddb5b5 | quote: * Must be signed in to pipedream.com: When connecting an account in development mode, you must be signed in to pipedream.com in the same browser where you’re connecting your account.
  - [4] 2026-10-30: the Connect REST API is at api.pipedream.com/v1/connect | capture: sha256:a56578b3b8492504418b54468148cad8417727d99319f622f3a2248eedddb5b5 | quote: curl -X POST https://api.pipedream.com/v1/connect/{project_id}/tokens
  - [6] 2026-10-30: Workflows takes no new sign-ups and runs until March 31, 2027 | capture: sha256:25a080440ffea6fde40be7f049502b2a50e5e278173f1ae50da62cee2475c7b1 | quote: Your existing workflows will keep running normally through March 31, 2027, but we're no longer accepting signups or subscriptions, and we won't be shipping new features for Workflows.
  - [6] 2026-10-30: Workflows data is deleted by April 30, 2027 | capture: sha256:25a080440ffea6fde40be7f049502b2a50e5e278173f1ae50da62cee2475c7b1 | quote: All Workflows data will be permanently deleted by April 30, 2027, including the credentials and OAuth tokens for your connected accounts.
  - [6] 2026-10-30: Connect is not affected by the Workflows shutdown | capture: sha256:25a080440ffea6fde40be7f049502b2a50e5e278173f1ae50da62cee2475c7b1 | quote: If you're using our Connect API, MCP Servers, or API Proxy, nothing changes for you.
  - [2] 2026-10-30: Workflows keep 7 days of events on free tiers | capture: sha256:859250b9f2c430eeed5f03e62685fd58f5a6c17956193a38fd6596e94632f30a | quote: | Free tiers | 7 days of events |
  - [2] 2026-10-30: Workflows time out at up to 300 seconds on free tiers | capture: sha256:859250b9f2c430eeed5f03e62685fd58f5a6c17956193a38fd6596e94632f30a | quote: | Free tiers | 300 seconds (5 min) |
  - [7] 2026-10-30: GitHub sign-in is offered, alongside Google and a work email with a password | capture: sha256:c1a00a867438cbb302c19dbe15e8aa9091ff65ea8d4f29a4b3cb2336108e9e82 | quote: Sign up with GitHub
  - [7] 2026-10-30: the sign-up form asks for a work email and a password | capture: sha256:c1a00a867438cbb302c19dbe15e8aa9091ff65ea8d4f29a4b3cb2336108e9e82 | quote: Work email
  - [8] 2026-11-01: Connect integrations are added with the Pipedream CLI | capture: sha256:7bf680012daeb3f45ce4f1ed469af0e8edd81cf4c74d1c1640a222bcd91e8466 | quote: * Building integrations for your app? Follow our [Connect quickstart](https://pipedream.com/docs/connect/quickstart.md) to add integrations using the CLI
  - [9] 2026-11-01: the Pipedream pricing page archived on 2025-06-14 listed the Free plan at up to 300 credits a month and 10 credits a day; the current page names no number | capture: sha256:2f9f35cd693c3e24a3a7b700c55d18cc4ef5f9ca65a99d096eda5955c3f01081 | quote: # Up to 300 credits/mo ... Includes 10 credits/day
  - [10] 2026-11-01: the Pipedream pricing page archived on 2026-01-17 listed the Free plan at up to 100 credits a month | capture: sha256:fdf12b0604c703fe7d67abfc6a9bd523d6f59e8b5bdf49623a47121c5cfe5080 | quote: # Up to 100 credits/mo
  - [11] 2026-11-01: a community thread shown as dated 2024-09-09, mirrored from Slack with the posters unnamed, says the latest free plan includes 10 credits a day for new accounts | capture: sha256:5da0469cf81072ece3c232c3b402088b0880340000e03921668715ae3aac97bf | quote: the latest free plan includes 10 credit per day, this applies for all new accounts.
  - [3] 2026-11-01: free workspaces have a daily credit limit, and the current page gives no number for it | capture: sha256:9ff91c706fa71bde9e268496fa459680abd8b14534878d239dbd552825490412 | quote: * Daily credit limit: Free workspaces have a daily limit of free credits that cannot be exceeded
  - [12] 2026-11-01: anyone can use the hosted Pipedream MCP servers for their own use for free | capture: sha256:bbb592a9b1cfcea3d2e826e0e8cd2ea1bc361d9391a92ef3f7220da138952f2f | quote: * Anyone can use Pipedream’s hosted MCP servers for their own use for free
  - [13] 2026-11-01: the Pipedream MCP server takes SSE and streamable HTTP, chosen dynamically | capture: sha256:ad340b3a1ef8bbd478eb423456111b3806c917d77d611d559ae7bb107df82124 | quote: The Pipedream MCP server supports both SSE and streamable HTTP transport types dynamically, with no configuration required by the developer or MCP client.
  - [13] 2026-11-01: the base URL of the Pipedream MCP server for developers is https://remote.mcp.pipedream.net/v3 | capture: sha256:ad340b3a1ef8bbd478eb423456111b3806c917d77d611d559ae7bb107df82124 | quote: https://remote.mcp.pipedream.net/v3
  - [14] 2026-11-01: the Pipedream MCP server URL for a person's own MCP client is https://mcp.pipedream.net/v2 | capture: sha256:dbd35bb09b3d117af3aed6588646e377bbde3d6c58611152c00540c9ce1d7635 | quote: https://mcp.pipedream.net/v2
  - [14] 2026-11-01: a Pipedream MCP account for a person's own MCP client is separate from a pipedream.com account | capture: sha256:dbd35bb09b3d117af3aed6588646e377bbde3d6c58611152c00540c9ce1d7635 | quote: > Pipedream MCP accounts are currently separate from your [pipedream.com](https://pipedream.com) account.
  - [4] 2026-11-01: the development environment is limited to 10 unique external user IDs | capture: sha256:a56578b3b8492504418b54468148cad8417727d99319f622f3a2248eedddb5b5 | quote: * Maximum of 10 external users: The development environment is limited to 10 unique external user IDs.
  - [7] 2026-11-01: the sign-up form asks for a work email | capture: sha256:c1a00a867438cbb302c19dbe15e8aa9091ff65ea8d4f29a4b3cb2336108e9e82 | quote: Work email
- sources:
  - [1] https://pipedream.com/pricing
  - [2] https://pipedream.com/docs/workflows/limits
  - [3] https://pipedream.com/docs/pricing
  - [4] https://pipedream.com/docs/connect/managed-auth/environments
  - [5] https://pipedream.com/docs/pricing/faq
  - [6] https://pipedream.com/docs/workflows
  - [7] https://pipedream.com/auth/signup
  - [8] https://pipedream.com/docs
  - [9] https://web.archive.org/web/20250614093733/https://pipedream.com/pricing
  - [10] https://web.archive.org/web/20260117135813/https://pipedream.com/pricing
  - [11] https://web.archive.org/web/20241215181325/https://pipedream.com/community/t/did-the-free-tier-credits-recently-decrease-from-100-to-10/11651
  - [12] https://pipedream.com/docs/connect/mcp
  - [13] https://pipedream.com/docs/connect/mcp/developers
  - [14] https://pipedream.com/docs/connect/mcp/users
