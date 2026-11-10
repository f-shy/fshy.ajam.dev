# UptimeRobot

> uptimerobot.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uptimerobot/ | JSON https://fshy.ajam.dev/api/v1/entity/uptimerobot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UptimeRobot

- `dev-services/uptimerobot` | qualifies-with-caveat | evidence documented | binding request-rate | category uptime monitoring and status pages | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-02T00:37:34.248Z (live) | stale on 2026-12-03
- url https://uptimerobot.com/pricing/
- free tier: Free, USD 0/month: 50 monitors at a 5-minute monitoring interval, HTTP, port and ping monitors, basic status pages, only 5 integrations and no login seats; no credit card required | unit: objects | metered on: object-count | read on: 2026-10-30 | source: [1] | note: The unit counted is the monitor. The pricing page's feature list for Free also names keyword, API, UDP, DNS and location-specific monitoring, while its own answer on Free against Solo says Solo adds API, multi-location, slow-response, UDP and DNS monitoring; only HTTP, port and ping monitors, 5-minute intervals and basic status pages are taken as the free set. Monthly e-mail reports are sent for the first 3 months only.
- per-object cap: not applicable: a monitor checks a target; nothing is stored per object
- retention: 3 months of monitor logs on the free plan, against 12 months on Solo and 24 months on Team and Scale | source: [1]
- egress: not applicable: an outbound checker; monitor data is read back through the API at 10 requests per minute on the free plan | metered: no | source: [2]
- identity: email | detail: The sign-up page offers Google, GitHub or an e-mail address, and the pricing page states no credit card is required for Free; the mobile-app page states that registration needs just an e-mail address. A no-registration flow creates a free monitor from an e-mail address confirmed with one click. A phone number is not asked for at registration: it is registered afterwards as an SMS and voice-call alert contact, which needs purchased credits.
- interface: rest
- limits:
  - volume-quota: 50 monitors [1]
  - request-rate (binding): 5-minute monitoring interval [1]
  - request-rate (binding): 10 API requests per minute on the free plan [2]
  - retention-clamped: 3 months of monitor logs [1]
- binding note: The 5-minute interval sets the detection delay of every monitor and the API answers 10 requests a minute; both bind before 50 monitors are used.
- interface detail: REST API v3 at https://api.uptimerobot.com/v3 with a main or monitor-specific API key, the legacy API still documented, and a remote streamable-HTTP MCP server at https://mcp.uptimerobot.com/mcp that takes OAuth or an API key as a Bearer token and shares the REST API's request quota, with tool calls limited to 10 per minute on the free plan. The v3 host answered 401 to /v3/monitors without a key. A separate no-registration endpoint creates one free 5-minute HTTPS monitor from an e-mail address after a proof-of-work challenge and the owner's one-click confirmation.
- endpoint: part of interface detail
- tooling: any HTTP client with an API key, the MCP server for agent clients, and the Zapier integration
- composes with: Keeps up to 50 endpoints of free hosting under a 5-minute external check, which also keeps an idle-sleeping free web service awake.
- reliability: no throttle, ban or data loss is stated on the pages read beyond the 3-month log retention
- notes: 50 monitors at a 5-minute interval, against 10 monitors at a 3-minute interval on Better Stack's free plan: more targets, slower detection.
- evidence note: Every limit is quoted from a first-party page, and the API host answered 401 without a key. No account was opened; an authenticated API call from a free account would move it to measured.
- evidence:
  - [1] 2026-10-30: the free plan needs no credit card | capture: sha256:fcc841eea58561926c1d658cefd5b50406418c5d6a7bd5b0067f628a0c2aeb13 | quote: Good for personal and commercial projects. No credit card required!
  - [1] 2026-10-30: the free plan checks every 5 minutes | capture: sha256:fcc841eea58561926c1d658cefd5b50406418c5d6a7bd5b0067f628a0c2aeb13 | quote: 5 min. monitoring interval
  - [1] 2026-10-30: the free plan has HTTP, port and ping monitors | capture: sha256:fcc841eea58561926c1d658cefd5b50406418c5d6a7bd5b0067f628a0c2aeb13 | quote: HTTP, port & ping monitor
  - [1] 2026-10-30: Free has 5-minute intervals and basic status pages | capture: sha256:fcc841eea58561926c1d658cefd5b50406418c5d6a7bd5b0067f628a0c2aeb13 | quote: Free includes 5-minute intervals and basic status pages.
  - [1] 2026-10-30: the free plan allows only 5 integrations | capture: sha256:fcc841eea58561926c1d658cefd5b50406418c5d6a7bd5b0067f628a0c2aeb13 | quote: Only 5 integrations
  - [1] 2026-10-30: the free plan has no login seats | capture: sha256:fcc841eea58561926c1d658cefd5b50406418c5d6a7bd5b0067f628a0c2aeb13 | quote: No login seats available
  - [1] 2026-10-30: monitor logs are kept 3 months on Free, 12 on Solo and 24 on Team and Scale | capture: sha256:fcc841eea58561926c1d658cefd5b50406418c5d6a7bd5b0067f628a0c2aeb13 | quote: | Data retentionWe save your logs even for response times. | 3 months | 12 months | 24 months | 24 months |
  - [2] 2026-10-30: the free plan has 50 monitors with no credit card | capture: sha256:f4766e30b8f8b7cc71d7200c579dc76a749c04a801941bf586597b1f7f1211cd | quote: 50 monitors free forever (no credit card required)
  - [2] 2026-10-30: the API allows 10 requests per minute on the free plan | capture: sha256:f4766e30b8f8b7cc71d7200c579dc76a749c04a801941bf586597b1f7f1211cd | quote: Rate Limits: Free plan = 10 req/min. Paid plans = monitor limit * 2 req/min (max 5000 req/min).
  - [2] 2026-10-30: the v3 REST API base URL | capture: sha256:f4766e30b8f8b7cc71d7200c579dc76a749c04a801941bf586597b1f7f1211cd | quote: Base URL: `https://api.uptimerobot.com/v3`
  - [2] 2026-10-30: an MCP server is offered | capture: sha256:f4766e30b8f8b7cc71d7200c579dc76a749c04a801941bf586597b1f7f1211cd | quote: Server URL: https://mcp.uptimerobot.com/mcp
  - [2] 2026-10-30: a free 5-minute HTTPS monitor can be made with only an e-mail address and no registration | capture: sha256:f4766e30b8f8b7cc71d7200c579dc76a749c04a801941bf586597b1f7f1211cd | quote: Create a forever free 5-minute interval HTTPS monitor for a user with only the email where the notifications shall go, no registration or API key.
  - [3] 2026-10-30: the sign-up page offers Google, GitHub or e-mail | capture: sha256:79286d8ad32469b0e295163fc5f1898b0719c7135c9061c5771be4a4dfc6c625 | quote: Google Github Use email
  - probe:https://api.uptimerobot.com/v3/monitors 2026-10-31: the v3 API host answers 401 without a key | capture: sha256:c9a30101de2be644402910011f70d1239b58b991527beb79f4c6c01f233dd5ed | quote: "status": 401
  - [4] 2026-11-01: registration needs just an e-mail address, on the free plan as on the others | capture: sha256:d4f12d33982c52ddaa8b48c9d99c4ea49654919130d699daf9e3332a2e1f38e4 | quote: All plans can use the app. Register with just your email address and set up 50 uptime monitors that check every five minutes.
  - [5] 2026-11-01: MCP tool calls are limited to 10 per minute on the free plan | capture: sha256:fa1f73198dfed8a7ff447722b377aeebc337eebda8a20f5ae0e0add151184c82 | quote: Tool calls are rate-limited too (10 per minute on the free plan).
  - [6] 2026-11-01: a phone number is registered as an SMS and voice-call alert contact, which needs credits | capture: sha256:eb862e69fb207196f3bba58c7b0c85652afdfd587d626d7eeb9548a2d12fe687 | quote: SMS & Voice Call: Users can also register one phone number for SMS and voice call alerts. These features require available credits to activate contact and use.
  - [7] 2026-11-01: SMS and voice calls on the Free plan need purchased credits | capture: sha256:1cbe3d0728ae690c5acf40675965baea0431be57bf608efc3d4ebb53f7b6c571 | quote: SMS and voice calls are features accessible across all available plans, including the Free plan. However, these features require the purchase of additional credits.
  - [8] 2026-11-01: a free account is created from a site URL and an e-mail address with one click of confirmation | capture: sha256:6cf89beafbfa6f70fbc6f8f296d7c375c4e81fa2ce7671087e157033b8636317 | quote: The agent submits your site’s URL and your email, you confirm with one click, and a live monitor plus a free account are created.
  - [9] 2026-11-01: the MCP server is at https://mcp.uptimerobot.com/mcp | capture: sha256:1976dc6e1ef6bdafad56a02b3b5673d4d42ca1bc89cdf28a007e90a82383bb2d | quote: "url": "https://mcp.uptimerobot.com/mcp"
  - [9] 2026-11-01: the MCP server authenticates through OAuth | capture: sha256:1976dc6e1ef6bdafad56a02b3b5673d4d42ca1bc89cdf28a007e90a82383bb2d | quote: Your client will handle authentication automatically via OAuth.
  - [9] 2026-11-01: an API key is the alternative to OAuth for the MCP server | capture: sha256:1976dc6e1ef6bdafad56a02b3b5673d4d42ca1bc89cdf28a007e90a82383bb2d | quote: If your client does not support OAuth, use your UptimeRobot API key instead.
  - [9] 2026-11-01: MCP tool calls share the REST API's request quota | capture: sha256:1976dc6e1ef6bdafad56a02b3b5673d4d42ca1bc89cdf28a007e90a82383bb2d | quote: MCP tool calls count against the same API rate limit as direct UptimeRobot API requests — they share one request quota.
  - [10] 2026-11-01: the MCP server uses the streamable HTTP transport | capture: sha256:da4067829c83650115ad2d2a66261d3cc97821f8a420f7b7d142f6f093c195e4 | quote: Transport: HTTP (streamable), connected directly — nothing runs locally.
  - [9] 2026-11-01: UptimeRobot's MCP server is a remote HTTP server | capture: sha256:1976dc6e1ef6bdafad56a02b3b5673d4d42ca1bc89cdf28a007e90a82383bb2d | quote: The UptimeRobot MCP server runs as a remote HTTP server.
- sources:
  - [1] https://uptimerobot.com/pricing/
  - [2] https://uptimerobot.com/llms.txt
  - [3] https://dashboard.uptimerobot.com/sign-up
  - [4] https://uptimerobot.com/mobile-app/
  - [5] https://github.com/uptimerobot/ai/blob/main/README.md
  - [6] https://help.uptimerobot.com/en/articles/11360953-uptimerobot-personal-notification-channels-setup-guide
  - [7] https://help.uptimerobot.com/en/articles/11361302-uptimerobot-sms-voice-call-credits-how-they-work
  - [8] https://uptimerobot.com/ai-agent-monitoring/
  - [9] https://help.uptimerobot.com/en/articles/12928342-uptimerobot-mcp-integration-guide
  - [10] https://github.com/uptimerobot/ai/blob/main/AGENTS.md
