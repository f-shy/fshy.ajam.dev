# Phonebox

> phonebox.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/phonebox/ | JSON https://fshy.ajam.dev/api/v1/entity/phonebox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Phonebox

- `compute/phonebox` | trial-only | evidence documented | binding volume-quota | category cloud Android phone | tier Starter, with 7-day free trial
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T02:12:34.925Z (live) | stale on 2026-12-26
- url https://phonebox.dev/docs/billing/pricing
- free tier: New accounts get a free 7-day trial with $5 of phone time, then $20/month; a card is required and nothing is charged for 7 days. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The $5 trial credit buys phone time at $0.06 per phone-minute. Starter is $20/month with $20 of phone time; Pro is $99/month with $99.
- per-object cap: not applicable: the unit is a cloud Android phone, not an object; an APK upload is capped at 524,288,000 bytes (500 MiB). | source: [2]
- retention: A parked phone keeps its apps, files and signed-in accounts; a saved phone unused for 30 days is deleted after a warning email a week before. Activity records are kept for 30 days. | days: 30 | source: [2]
- egress: not published: the pricing and limits pages read state no separate egress allowance or price for device traffic | metered: no | source: [3]
- identity: card | detail: Sign up with Google or an email address; the free week is new accounts only, one per person, and a card is required though nothing is charged for 7 days.
- interface: rest, cli, chat, browser
- limits:
  - volume-quota (binding): $5 of trial phone time over 7 days, then $20 of phone time a month on Starter [1]
  - request-rate: 600 requests a minute for each API key; 60 lifecycle requests a minute for each project [2]
- limits note: Sessions default to 15 minutes and run at most 3 hours; the phone auto-parks after about 5 idle minutes; 5 phones run at once on Starter; monthly spending limit $100 by default.
- binding note: Phone time is prepaid credit: the $5 trial week, then $20 a month, runs out before the per-minute request limit on a single agent's workload.
- interface detail: REST API at https://phonebox.dev/v1 with an API key as a bearer token; CLI and TypeScript SDK in the same npm package; hosted MCP server at https://phonebox.dev/mcp.
- endpoint: part of interface detail
- tooling: An agent uses the REST API, the `phonebox` CLI, the TypeScript SDK or the hosted MCP server; no local emulator is needed.
- composes with: A coding agent can install an APK it just built on a cloud phone and walk the screens it changed, with a browser live view for a human handoff.
- reliability: A phone left idle keeps billing until it auto-parks at about 5 minutes; a refused create made no phone; when fleet capacity is exhausted a create or start fails with 503 capacity_unavailable.
- notes: The $5 trial week is time-boxed and needs a card; the recurring Starter plan is $20/month for $20 of phone time at $0.06 a phone-minute. No phone number, SMS or calling is included.
- evidence note: Price, credit, session limits and card gate are quoted from first-party pricing, plans, limits and signup pages read on 2026-11-25.
- extras:
  - billing_model: per-second prepaid phone minutes on a monthly plan
  - free_tier_kind: one-time trial
  - term: 7-day trial, then monthly
  - price_arithmetic: $0.06 per phone-minute is $3.60 an hour
  - session_cap.wall_clock_min: 180
  - session_cap.idle_reap_s: 300
  - session_cap.default_max_duration_s: 900
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - network_out.static_ip: dedicated IPs only on Enterprise
  - requests_per_minute: 600
- evidence:
  - [3] 2026-11-25: the price is $0.06 per phone-minute, $3.60 an hour, billed per second | capture: sha256:3e380249d9ddf3bc039ad697091dd2689e735117b3aa320f9593e9b3e22bf34f | quote: Phonebox has one price for every phone: $0.06 per phone-minute, which is $0.001 a second or $3.60 an hour. Credit comes with a [plan](https://phonebox.dev/docs/billing/plans). There is no seat fee.
  - [3] 2026-11-25: a phone is billed per second with a 60-second minimum per session | capture: sha256:3e380249d9ddf3bc039ad697091dd2689e735117b3aa320f9593e9b3e22bf34f | quote: A phone is billed while it is `creating`, `starting` or `ready`, per second, with a minimum of 60 seconds for each session.
  - [1] 2026-11-25: the free week is 7 days with $5 of trial credit and requires a card | capture: sha256:95d32769bcd1005cd830c4af315e1fa230a8805b0cb49489fd99cc3e66819adc | quote: New accounts only, one per person. Start it in the console or from the link `phonebox setup` gives your agent. A card is required, and nothing is charged for 7 days.
  - [1] 2026-11-25: the trial credit is $5 and the Starter plan is $20 a month | capture: sha256:95d32769bcd1005cd830c4af315e1fa230a8805b0cb49489fd99cc3e66819adc | quote: - It comes with $5 of trial credit and Starter's limits. Running out never charges you; start Starter early to keep going, or choose Pro. Either ends the week and charges that plan at once, and any trial credit left carries over.
  - [4] 2026-11-25: signup needs a Google account or an email address | capture: sha256:0635ec58af610fbbf6ea3b5c449ba9c951fb0e9f63920dc2018b55eeb4d31a83 | quote: Sign up with Google or your email. Start with a free week.
  - [5] 2026-11-25: the API is REST at https://phonebox.dev/v1 with an API key bearer token | capture: sha256:90e68388d9269d668b5077728e069fb05a2b52503f5e9bfe54d96800308bda7c | quote: The API lives at `https://phonebox.dev/v1` and takes an API key as a bearer token.
  - [2] 2026-11-25: session maximum duration is 3 hours with a 15-minute default | capture: sha256:9a2e98450e50bd1771795921a06b5d154dbae3b53faf5ff2550152ed7f66bef9 | quote: `max_duration` | 60 to 10800 seconds, 900 by default
  - [6] 2026-11-25: the offer is a cloud Android device, not a phone number or SMS inbox | capture: sha256:2f45d260446b2e12a3504e204cd84d02802b2d7717607346c11fde52679f587e | quote: Phonebox doesn't give your agent a phone number, an SMS inbox or calling. It gives it the device itself: the screen, the installed apps, touch input and the keyboard.
  - [3] 2026-11-24: the single price is USD 0.06 per phone-minute, which is USD 0.001 a second or USD 3.60 an hour | capture: sha256:3e380249d9ddf3bc039ad697091dd2689e735117b3aa320f9593e9b3e22bf34f | quote: Phonebox has one price for every phone: $0.06 per phone-minute, which is $0.001 a second or $3.60 an hour.
  - [3] 2026-11-24: a parked phone costs nothing and keeps apps and signed-in accounts | capture: sha256:3e380249d9ddf3bc039ad697091dd2689e735117b3aa320f9593e9b3e22bf34f | quote: A parked phone costs nothing, and it keeps its apps, files and signed-in accounts.
  - [3] 2026-11-24: the free week gives USD 5 of phone time for 7 days and requires a card | capture: sha256:3e380249d9ddf3bc039ad697091dd2689e735117b3aa320f9593e9b3e22bf34f | quote: New accounts start with a free 7-day trial and $5 of phone time, card required; see [Plans](https://phonebox.dev/docs/billing/plans).
  - [2] 2026-11-24: 600 requests a minute per API key with a 429 and Retry-After | capture: sha256:9a2e98450e50bd1771795921a06b5d154dbae3b53faf5ff2550152ed7f66bef9 | quote: | Requests | 600 a minute for each API key | `429 rate_limited` with `Retry-After` |
  - [2] 2026-11-24: the APK upload cap is 524,288,000 bytes and other uploads and downloads are capped at 4 MB | capture: sha256:9a2e98450e50bd1771795921a06b5d154dbae3b53faf5ff2550152ed7f66bef9 | quote: | File uploads and downloads | 4 MB, which is 4,000,000 bytes | `413 payload_too_large` |
  - [2] 2026-11-24: the APK size cap is 524,288,000 bytes (500 MiB) within 2 minutes | capture: sha256:9a2e98450e50bd1771795921a06b5d154dbae3b53faf5ff2550152ed7f66bef9 | quote: | An APK [upload](https://phonebox.dev/docs/api-reference/uploads) | 524,288,000 bytes (500 MiB), sent within 2 minutes | The upload ends as `too_large` |
  - [2] 2026-11-24: the default monthly spending limit is USD 100 and can be set to USD 0 to stop new spending | capture: sha256:9a2e98450e50bd1771795921a06b5d154dbae3b53faf5ff2550152ed7f66bef9 | quote: | Monthly spending | $100, which you change in Settings. $0 pauses new spending. | `402 spend_limit_reached` |
  - [1] 2026-11-24: the free week is one per person, requires a card and charges nothing for 7 days | capture: sha256:95d32769bcd1005cd830c4af315e1fa230a8805b0cb49489fd99cc3e66819adc | quote: - New accounts only, one per person. Start it in the console or from the link `phonebox setup` gives your agent. A card is required, and nothing is charged for 7 days.
  - [1] 2026-11-24: a saved phone unused for 30 days is deleted with a warning a week before | capture: sha256:95d32769bcd1005cd830c4af315e1fa230a8805b0cb49489fd99cc3e66819adc | quote: - A saved phone unused for 30 days is deleted, after a warning email a week before. The [terms](https://phonebox.dev/docs/terms) have the details.
  - [4] 2026-11-24: sign-up offers Google or email and starts a free week | capture: sha256:0635ec58af610fbbf6ea3b5c449ba9c951fb0e9f63920dc2018b55eeb4d31a83 | quote: Sign up with Google or your email. Start with a free week.
  - [5] 2026-11-24: the service gives an agent a cloud Android device with screen, apps, touch and keyboard and not a phone number | capture: sha256:426885a0dd915a0e34bb94d6980d6d80d37f2285ba4865626e21d608875ba0e7 | quote: Phonebox gives an agent the device itself, with its screen, apps, touch and keyboard, and not a phone number.
- sources:
  - [1] https://phonebox.dev/docs/billing/plans
  - [2] https://phonebox.dev/docs/billing/limits
  - [3] https://phonebox.dev/docs/billing/pricing
  - [4] https://phonebox.dev/sign-up
  - [5] https://phonebox.dev/docs
  - [6] https://phonebox.dev/
