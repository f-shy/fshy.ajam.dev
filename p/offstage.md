# offstage

> offstage.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/offstage/ | JSON https://fshy.ajam.dev/api/v1/entity/offstage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## offstage

- `compute/offstage` | trial-only | evidence documented | binding volume-quota | category sandbox | tier macOS sandbox on Mac Studio M5 Max ($5 one-time credit)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.813Z (live) | stale on 2026-12-26
- url https://offstage.cloud/
- free tier: $5 in free credit, no credit card needed; the account starts with $5 in free credit and the user adds credit by card in the console when it runs out | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: A one-time sign-up credit, at $1.10/hour about 4.5 hours of macOS sandbox time. No recurring free tier is published on the pricing or sign-up pages read.
- per-object cap: not applicable: the unit is a macOS sandbox on a Mac Studio M5 Max, not an object store | note: No per-file or disk cap is published on the pages read.
- retention: unverified: no workspace-file retention period is stated on the pages read; sandboxes close after a job and the page shows per-team concurrency limits | source: [1]
- egress: not published as a per-GB price: usage is billed at $1.10 an hour by the second with no minimum; no outbound byte allowance or price per GB is stated on the pages read | metered: no | source: [1]
- identity: email | detail: The sign-up page reads 'Sign up with a social provider or your email'; no credit card is needed for the $5 free credit. No phone, ID document or institution is asked for on that page.
- interface: rest, cli
- limits:
  - volume-quota (binding): 4 open sandboxes and 4 running CI jobs per team; additional CI jobs queue [1]
  - request-rate: $1.10 an hour billed by the second with no minimum; $5 one-time free credit at sign-up [1]
- limits note: macOS 27, Xcode 27.2 and Apple silicon on a Mac Studio M5 Max; sandboxes queue for available Macs.
- binding note: The one-time $5 credit runs out after about 4.5 billed hours, before the per-team four-sandbox concurrency cap is reached in ordinary use.
- interface detail: An API key created in the console, pasted into an agent such as Claude Code, Codex or Cursor; the page links a computer-use guide and a quickstart for direct API use. macOS sandboxes run Swift tests, Xcode and the iOS Simulator, and give an agent desktop control.
- endpoint: https://console.offstage.cloud/keys
- tooling: Console API keys, a documented API quickstart and agent integrations for Claude Code, Codex and Cursor; no rclone backend is relevant to a Mac desktop sandbox.
- composes with: The one-time $5 credit buys roughly 4.5 hours of a real Mac for computer-use, Xcode builds and iOS simulator tests; an agent pays for the sandbox from the account credit and queues for an available Mac when all are busy.
- reliability: Sandboxes queue for an available Mac and a team can run at most 4 open sandboxes and 4 CI jobs; additional CI jobs queue. The vendor states no matched build-speed benchmark against other Mac clouds.
- notes: Hosted macOS sandboxes on a Mac Studio M5 Max for computer-use agents and CI: $1.10/hour billed by the second, no minimum, $5 one-time credit with no card. About 4.5 hours of Mac time on the free credit. A comparison table on the page lists GitHub Actions, Scaleway, AWS EC2 Mac and Daytona with 24-hour minimums on the last three.
- evidence note: The $1.10/hour rate, per-second billing with no minimum, $5 no-card credit, per-team limits and the email-or-social sign-up gate are quoted from first-page and sign-up pages read on 2026-11-25.
- extras:
  - shape.gpu_class: Apple silicon (Mac Studio M5 Max)
  - shape.note: a real Mac desktop with macOS 27 and Xcode 27.2; vCPU, RAM and disk are not published
  - billing_model: per-second usage against prepaid credit with a one-minute-free minimum
  - free_tier_kind: one-time credit
  - term: no minimum rental period
  - price_arithmetic: $5 / $1.10 per hour = about 4.5 hours of sandbox time
  - status: hosted and priced
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - session_cap.restart_required: no
  - session_cap.note: sandboxes queue for available Macs; 4 open sandboxes and 4 CI jobs per team
- evidence:
  - [1] 2026-11-25: the macOS sandbox is $1.10 an hour billed by the second with no minimum | capture: sha256:2508a87cf7ddf25f94712fc05bbfbcd4dbe1e42cdf550e186b9550a22d84e8af | quote: $1.10 an hour.
  - [1] 2026-11-25: billing is per second with no minimum, and sandboxes queue for Macs with 4 CI jobs per team | capture: sha256:2508a87cf7ddf25f94712fc05bbfbcd4dbe1e42cdf550e186b9550a22d84e8af | quote: Billed by the second. No minimum.
  - [1] 2026-11-25: the account starts with $5 in free credit and needs no credit card | capture: sha256:2508a87cf7ddf25f94712fc05bbfbcd4dbe1e42cdf550e186b9550a22d84e8af | quote: $5 in free credit. No credit card needed.
  - [1] 2026-11-25: the sandbox runs on a Mac Studio M5 Max with macOS 27, Xcode 27.2 and Apple silicon | capture: sha256:2508a87cf7ddf25f94712fc05bbfbcd4dbe1e42cdf550e186b9550a22d84e8af | quote: Running on Mac Studio M5 Max
  - [1] 2026-11-25: access uses an API key pasted into an agent such as Claude Code, Codex or Cursor | capture: sha256:2508a87cf7ddf25f94712fc05bbfbcd4dbe1e42cdf550e186b9550a22d84e8af | quote: Works with Claude Code, Codex and Cursor. Your agent will ask for the key.
  - [2] 2026-11-25: sign-up asks for a social provider or an email, and repeats the $5 no-card credit | capture: sha256:44faa992750b7eddac34b226ea169b8da726b1d6baf3da53442476833db5ce29 | quote: Sign up with a social provider or your email.
  - [1] 2026-11-24: the sandbox runs on a Mac Studio M5 Max at $1.10 an hour billed by the second with no minimum | capture: sha256:2508a87cf7ddf25f94712fc05bbfbcd4dbe1e42cdf550e186b9550a22d84e8af | quote: $1.10 an hour.
  - [1] 2026-11-24: billing is per second with no minimum and at most 4 CI jobs run per team with the rest queued | capture: sha256:2508a87cf7ddf25f94712fc05bbfbcd4dbe1e42cdf550e186b9550a22d84e8af | quote: Billed by the second. No minimum. Sandboxes queue for available Macs. Up to 4 CI jobs run per team; additional jobs queue.
  - [2] 2026-11-24: the sign-up page shows $5 free credit with no card needed and social or email sign-in | capture: sha256:44faa992750b7eddac34b226ea169b8da726b1d6baf3da53442476833db5ce29 | quote: Sign up with a social provider or your email. or Already have an account? Sign in. We'll send occasional product updates; unsubscribe anytime. $0.0183 a minute ($1.10 an hour), billed per second$5.00 of free credit, no card needed
  - [3] 2026-11-24: a new personal account gets $5 in free credit with no credit card needed, and the team task and queue limits | capture: sha256:9d4b3a54c04f0cd8f93832581d0c6ac5b5b2cb1b7306dedfa89a375cca576e7c | quote: New personal accounts get \$5 in free credit. No credit card is needed to use it. When it runs out, add credit by card in the console under Billing, or turn on auto-reload.
  - [3] 2026-11-24: there is no fixed team limit on open sandboxes and up to 4 tasks or CI jobs run per team with 16 queued | capture: sha256:9d4b3a54c04f0cd8f93832581d0c6ac5b5b2cb1b7306dedfa89a375cca576e7c | quote: There is no fixed team limit on open sandboxes. Sandboxes queue for available Macs and reserve credit for their requested lifetime. Up to 4 tasks or CI jobs run per team; 16 more can queue.
  - [4] 2026-11-24: request rate, sandbox lifetime, idle timeout, file caps and concurrency limits | capture: sha256:c151c96afc7ec4543673d48ef77cf72ec4f48402236060776ce093eb86ef39c1 | quote: | Requests per team | 120 a minute, whatever key or session |
  - [4] 2026-11-24: a sandbox lives 15 minutes by default, never more than 24 hours from creation, and closes after 10 idle minutes by default | capture: sha256:c151c96afc7ec4543673d48ef77cf72ec4f48402236060776ce093eb86ef39c1 | quote: | Sandbox lifetime (`timeoutMs`) | 15 min by default. Never more than 24 h from creation, even with [Set the timeout](https://offstage.cloud/docs/api/sandboxes.md#set-the-timeout) |
  - [5] 2026-11-24: signup takes email and a password of at least 10 characters and emails a verification link before the team can create sandboxes or keys | capture: sha256:94deeda65178f79022a8f74996ff3138f0f3420eae0f4380551c1db28c0393e7 | quote: `POST /v1/auth/signup` `{email, password, name?}` | `201 {user, team}`, and sets the session cookie. The password needs at least 10 characters. It emails a link that verifies the address: until the owner opens it, `team.verified` is false and creating a sandbox, task or key answers 403 `email-unverified`
  - [5] 2026-11-24: artifacts and recordings are kept 7 days and a 24-hour sandbox reserves $26.40, beyond the $5 signup credit | capture: sha256:94deeda65178f79022a8f74996ff3138f0f3420eae0f4380551c1db28c0393e7 | quote: | A 24-hour sandbox | $26.40, more than the free credit |
  - [6] 2026-11-24: the public price sheet gives per-hour, per-minute and per-second rates and a $5 free credit | capture: sha256:ff43f237fff4e880171d7f68e1d63d535b9f13c2e94921ea7a83b6efab8f9af9 | quote: "usdPerHour": 1.1,
  - [7] 2026-11-24: the user installs the hosted SDK and drives sandboxes over the API | capture: sha256:a3de3ef77cad113fe37030507231dd9a7851547b2a16dad4580bdc14d7a059be | quote: `Sandbox.create({ session?, timeoutMs?, idleTimeoutMs? })` | Makes a sandbox. `session` is `"headless"` (the default) or `"gui"`. It lives 15 minutes by default and never more than 24 hours; it closes after 10 idle minutes by default
- sources:
  - [1] https://offstage.cloud/
  - [2] https://console.offstage.cloud/sign-up
  - [3] https://offstage.cloud/docs/pricing.md
  - [4] https://offstage.cloud/docs/api/limits.md
  - [5] https://api.offstage.cloud/llms.txt
  - [6] https://offstage.cloud/docs/api/pricing.md
  - [7] https://offstage.cloud/docs/sandboxes.md
