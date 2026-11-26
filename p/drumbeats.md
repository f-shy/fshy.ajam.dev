# Drumbeats

> drumbeats.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/drumbeats/ | JSON https://fshy.ajam.dev/api/v1/entity/drumbeats.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Drumbeats

- `dev-services/drumbeats-io` | qualifies-with-caveat | evidence documented | binding volume-quota | category cron job, heartbeat and uptime monitoring with incidents and status pages (hosted) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://drumbeats.io/pricing
- free tier: Free plan, $0 forever with no credit card: 200K beats a month, 50 monitors, 3 projects, a 1-minute minimum interval, a ping retention of 250, a maximum payload of 100 KB, unlimited team seats and 8 alert channels; the REST API and the MCP server are part of every plan, Free included | unit: requests | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The unit is the beat, a measure of activity: the pricing page converts 200K beats into 23 cron jobs running every 5 minutes or 5 uptime monitors checked every minute, and bills activity instead of monitor count. The vocabulary has no beats term, so requests is the nearest. Advanced status pages, 30-second checks and overage start on Pro.
- per-object cap: 100 KB maximum payload per ping on Free, against 1 MB on Pro | source: [1]
- retention: a ping retention of 250 on Free, against 1,000 on Pro, printed without a unit | source: [1]
- egress: not applicable: an inbound ping receiver and outbound uptime checker; monitors, incidents and channels are read through the REST API | metered: no | source: [2]
- identity: email | detail: The sign-up page states no credit card is required and asks for an email address and a password of at least 8 characters, then emails a one-time verification code; Google and other sign-in options appear under Or continue with.
- interface: rest
- limits:
  - volume-quota (binding): 200K beats per month, 50 monitors and 3 projects on Free [1]
  - request-rate: 1-minute minimum interval on Free, 30 seconds on Pro [1]
  - per-object-cap: 100 KB maximum payload on Free [1]
  - retention-clamped: ping retention of 250 on Free [1]
- limits note: A Free project gets a public page for every monitor; advanced status pages are not part of Free.
- binding note: The 200K monthly beats are reached before the 50-monitor cap by checks that run every minute, so activity binds before monitor count.
- interface detail: A Ping API at api.drumbeats.io/v1/ping/MONITOR-ID takes plain HTTP requests with no key, the monitor ID being the credential; a REST API for monitors, incidents, projects, notification channels and groups takes an X-API-Key header; an MCP server connects Claude, Cursor, VS Code and other MCP clients.
- endpoint: https://api.drumbeats.io/v1/ping/
- tooling: curl or any HTTP client against the Ping API and the REST API, integration guides for common stacks, an MCP server and the web app
- composes with: Dead man's switch for the scheduled jobs of free hosts with one curl at the end of a job, plus 1-minute uptime checks and a public page for every monitor.
- reliability: what happens past 200K beats on Free is unverified: the pricing page states only that overage starts on Pro
- notes: Pro is USD 20 a month with 1M beats included, unlimited monitors, a 1 MB maximum payload and a 30-second minimum interval.
- evidence note: Plan limits, the API surface and the sign-up form are quoted from first-party pages. No account was opened, so the behaviour past the monthly beats is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the plan is free for 50 monitors with no credit card | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: Free for 50 monitors, no credit card.
  - [1] 2026-11-01: the Free plan costs $0 forever | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: Free $0forever Side projects, and the first production job you care about.
  - [1] 2026-11-01: Free has 200K beats a month, 50 monitors, 3 projects, a 1-minute minimum interval, a ping retention of 250, a 100 KB payload, unlimited seats and 8 alert channels | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: Beats / month 200K Monitors 50 Projects 3 Min interval 1 min Ping retention 250 Max payload 100 KB Team seats Unlimited Alert channels 8
  - [1] 2026-11-01: 200K beats cover 23 cron jobs every 5 minutes and 5 uptime monitors checked every minute | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: 200K beats covers 23 cron jobs running every 5 min 5 uptime monitors checked every minute
  - [1] 2026-11-01: advanced status pages, 30-second checks and overage start on Pro | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: Advanced status pages, 30-second checks, and overage start on Pro.
  - [1] 2026-11-01: the REST API and MCP server are part of every plan including Free | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: REST API and MCP serverCreate, ingest and resolve programmatically — or point an agent at it
  - [1] 2026-11-01: a Free account has no trial window and no reduced version of the listed features | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: A Free account gets all 6 in full: no trial window, no reduced version.
  - [1] 2026-11-01: a Free project still gets a public page for every monitor | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: Not part of Free. A Free project still gets a public page for every monitor.
  - [1] 2026-11-01: Pro costs $20 a month with 1M beats included and unlimited monitors | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: $20/ month 1M beats included · unlimited monitors
  - [1] 2026-11-01: Pro has a ping retention of 1,000, a 1 MB maximum payload and a 30-second minimum interval | capture: sha256:98508cb0c60fc41ce7f5c2c20649f456367b77c69bb1fdf9c6c2238ecc4f59d4 | quote: Ping retention 1,000 Advanced pages 1 Subscribers / page 100 Max payload 1 MB Min interval 30s
  - [2] 2026-11-01: a ping is one curl to api.drumbeats.io with no SDK, agent or API key | capture: sha256:6e02360018af2e4dfca6525009071a46b0381d9a5f62a5d0908263f1a2591049 | quote: That is the whole integration. No SDK, no agent, no API key on the ping path.
  - [2] 2026-11-01: the REST API covers monitors, incidents, projects, channels and groups and takes an X-API-Key header | capture: sha256:6e02360018af2e4dfca6525009071a46b0381d9a5f62a5d0908263f1a2591049 | quote: REST API | Monitors, incidents, projects, notification channels and groups | `X-API-Key` header
  - [2] 2026-11-01: an MCP server connects Claude, Cursor, VS Code and other MCP clients | capture: sha256:6e02360018af2e4dfca6525009071a46b0381d9a5f62a5d0908263f1a2591049 | quote: exposes the Drumbeats MCP server to Claude, Cursor, VS Code, and any other MCP client.
  - [3] 2026-11-01: the sign-up page states no credit card is required | capture: sha256:b3cbdd3f66d4920839be68d30149e796ddfbfe65373947a8d667bd9256e8f751 | quote: Create your account and put your first endpoint on watch in under a minute. No credit card required.
  - [3] 2026-11-01: the sign-up form asks for an email, a password and a confirmation, and emails a one-time verification code | capture: sha256:b3cbdd3f66d4920839be68d30149e796ddfbfe65373947a8d667bd9256e8f751 | quote: Email Password Must contain: 8+ chars, uppercase, lowercase, number, special char Confirm Password
  - [3] 2026-11-01: the sign-up sends a one-time verification email | capture: sha256:b3cbdd3f66d4920839be68d30149e796ddfbfe65373947a8d667bd9256e8f751
- sources:
  - [1] https://drumbeats.io/pricing
  - [2] https://drumbeats.io/docs
  - [3] https://drumbeats.io/register
