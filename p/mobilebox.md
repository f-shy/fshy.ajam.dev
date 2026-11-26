# Mobilebox

> mobilebox.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mobilebox/ | JSON https://fshy.ajam.dev/api/v1/entity/mobilebox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mobilebox

- `compute/mobilebox` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted Android phone sandbox | tier Cloud Android 14 phone (arm64)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.878Z (live) | stale on 2026-12-26
- url https://mobilebox.dev/pricing
- free tier: new workspaces get free credit, with no amount published; boot time and parked phones are free, and a phone parks itself after 5 idle minutes with installed apps, saved data and logins kept | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: one-time credit, amount unstated
- per-object cap: not applicable: the unit is a cloud phone, not an object | source: [1]
- retention: a parked phone keeps installed apps, saved app data and logins for free; unsaved in-memory state does not survive a resume, and no maximum park duration is published | source: [2]
- egress: a data-center IP is included; a residential IP costs USD 8 per GB and a mobile carrier IP USD 15 per GB of traffic, and a customer's own proxy can be set at no charge | metered: yes | source: [1]
- identity: email | detail: the signup page offers GitHub or Google sign-in, an existing team API key, and email, and says no password is needed; the docs name a configured GitHub/Google provider or a team-issued key, then an agent key created in the dashboard; paid credit is prepaid in USD through Stripe
- interface: rest, unknown
- limits:
  - request-rate: at most 20 actions per observation call; a phone parks itself after 5 idle minutes and after 15 minutes of running unless a longer duration up to 3 hours is requested [2]
  - volume-quota (binding): a one-minute minimum per session and a hold of the longest possible session from the balance when a phone starts; a start fails with insufficient_credits if the balance cannot cover the… [1]
- limits note: prices: USD 0.01 per phone-minute for a cloud Android 14 (arm64) phone or a real Android device, USD 0.02 for a large phone with 4 GB RAM and 16 GB storage, USD 0.03 for iPhone and iPad, and from USD 79 a month for dedicated team phones. Residential and mobile IPs bill per GB; free credit has no cash value.
- binding note: the per-second billing with a one-minute minimum and the balance hold at start bind first: a short task still costs one minute and a start fails when the balance cannot cover the hold. The free credit amount is unstated.
- interface detail: a REST API and a stateless Streamable HTTP MCP server at https://mobilebox.dev/mcp with a bearer API key; 21 MCP tools cover phone lifecycle, app installs, screen observation, actions and recording; the network proxies raise egress price, not a storage interface
- tooling: any MCP client or any code that makes HTTP requests; a team-issued key is used to sign in and an agent key is created in the dashboard; a Python package wraps the same REST API
- composes with: one phone per task for an agent that tests an app it built in a cloud sandbox without KVM: install the APK, read the screen as numbered elements, tap and swipe, then park the phone so the next task can resume it with saved logins. A hosted service, not self-hosted software. The free credit amount is unstated, so the published price of USD 0.01 a phone-minute is the entry cost after it runs out.
- reliability: phones can fail to start with no uptime guarantee and data on a phone can be lost; a failed DELETE can still leave a phone, and the docs advise inspecting the account and retrying creates with an Idempotency-Key.
- notes: A hosted cloud Android 14 (arm64) phone for agents, USD 0.01 per phone-minute (USD 0.60/hour over 60 minutes) billed by the second with a one-minute minimum; the free credit amount for new workspaces is not published. The list's USD 0.60/hour is 60 × USD 0.01, not a separate list price. Free boot time and free parked phones are included, and signup needs a GitHub/Google account or an email, no card for the free credit.
- evidence note: prices, devices, network prices, billing rules and signup options are quoted from the vendor's own pricing page, home page, docs and terms read on 2026-11-25.
- extras:
  - shape.disk_gib: 16
  - shape.note: a cloud Android 14 phone on arm64 in the vendor's servers; iOS simulators are hosted by a provider and cost USD 0.03 a minute
  - billing_model: per-second while a phone is ready, one-minute minimum, prepaid credit with a start hold
  - free_tier_kind: one-time-credit-amount-unstated
  - term: no subscription; credit is prepaid
  - price_arithmetic: USD 0.01/minute × 60 = USD 0.60/hour; a 15-minute default session costs USD 0.15
  - status: available
  - network_out.allow_outbound: yes
  - network_out.ports: REST and MCP; a customer proxy can be set
  - network_out.static_ip: residential or mobile IP is a paid add-on
  - session_cap.wall_clock_min: 1
  - session_cap.idle_reap_s: 300
  - session_cap.restart_required: no
  - session_cap.note: a one-minute minimum, auto-park after 5 idle minutes and after 15 minutes unless a longer duration up to 3 hours is requested
- evidence:
  - [1] 2026-11-25: a cloud Android phone costs USD 0.01 a minute, billed by the second while it runs | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: Mobilebox cloud Android phones for AI agents cost $0.01 a minute, billed by the second while a phone runs.
  - [1] 2026-11-25: the device table lists the cloud Android 14 arm64 phone at USD 0.01 per phone-minute | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: | Cloud Android 14 phone (arm64) | $0.01 per phone-minute |
  - [1] 2026-11-25: new workspaces get free credit, boot time and parked phones are free | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: - Free credit for new workspaces
  - [1] 2026-11-25: signup accepts GitHub or email | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: Sign up with GitHub or email
  - [3] 2026-11-25: sign-in uses a configured GitHub/Google provider or a team-issued key, and the agent key is created in the dashboard | capture: sha256:c1858be3c0383ad272bd9386f0362eeeba4cef4c84faddf9a330ed2787aa84a8 | quote: Sign in at [/login](/login) using a configured GitHub/Google provider or an existing team-issued key, then create an agent key in [/dashboard](/dashboard). Issued agent keys cannot sign into the browser or manage other keys.
  - [4] 2026-11-25: new workspaces get free credit, and paid credit is prepaid in USD through Stripe with a one-minute minimum | capture: sha256:d40e9f4635a4dc31a2cf9349a04a86b6e11c2fd8cb5a08bde6608076e9707c90 | quote: New workspaces get free credit. Running phones cost the price on the [pricing page](https://mobilebox.dev/pricing?via=md), billed per second from the moment a phone is ready, with a one-minute minimum per session.
  - [4] 2026-11-25: paid credit is prepaid through Stripe and not refundable once used | capture: sha256:d40e9f4635a4dc31a2cf9349a04a86b6e11c2fd8cb5a08bde6608076e9707c90 | quote: Paid credit is prepaid, billed in US dollars through Stripe and kept on your workspace; it is not refundable once used.
  - [1] 2026-11-25: billing is per second with a one-minute minimum and no seats or subscriptions | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: - Each second a phone is ready - One-minute minimum per session
  - [2] 2026-11-25: Android is USD 0.01 a minute in a hosted phone reached over API or MCP | capture: sha256:055c570418dda8d9b4cc6315d9f688e3407166eee27d6ef0c040c6d5bc24ce9c | quote: Mobilebox gives AI agents cloud Android phones and iPhones: Android is $0.01 a minute and was ready for a first screenshot in 1.35 s in our 22 November 2026 benchmark.
  - [1] 2026-11-25: a residential IP costs USD 8 per GB and a mobile carrier IP USD 15 per GB | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: | Residential IPCity targeting, sticky per phone | $8 per GB |
  - [2] 2026-11-25: an observation numbers the screen and allows up to 20 actions per call | capture: sha256:055c570418dda8d9b4cc6315d9f688e3407166eee27d6ef0c040c6d5bc24ce9c | quote: Each observation numbers what is on screen. Tap, type and swipe by ref, up to 20 actions per call.
  - [1] 2026-11-24: a cloud Android 14 arm64 phone costs $0.01 per phone-minute | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: Cloud Android 14 phone (arm64) | $0.01 per phone-minute
  - [1] 2026-11-24: a running phone is billed each second with a one-minute minimum | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: Each second a phone is ready
  - [1] 2026-11-24: there is a one-minute minimum per session | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: One-minute minimum per session
  - [1] 2026-11-24: boot time is free | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: Boot time, until the phone is ready
  - [1] 2026-11-24: parked phones keep their apps, data and logins and are free | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: Parked phones, with apps, data and logins kept
  - [1] 2026-11-24: new workspaces receive free credit | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: Free credit for new workspaces
  - [1] 2026-11-24: a city-targeted residential IP costs $8 per GB of traffic | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: Residential IPCity targeting, sticky per phone | $8 per GB
  - [1] 2026-11-24: a phone parks after 5 idle minutes and after 15 minutes unless a longer duration is set | capture: sha256:cf3c566c2dcdc598d757a1ecd95e4ce8d77ab76ab5da9a53348f135730da1f16 | quote: A phone parks itself after 5 idle minutes, and after 15 minutes of running unless you ask for up to 3 hours.
  - [5] 2026-11-24: the sign-up page asks the user to pick a sign-in method | capture: sha256:02a5f7ce9e66434793624c8756398e1c917da779ea3fe8b390e78895188e30d7 | quote: Pick how you sign in.
  - [2] 2026-11-24: sign-up is with GitHub and new workspaces get free credit | capture: sha256:68d38eb74f6769aac02b812e022249a510fc969a2e6fa8a4468a20febd73a91f | quote: Sign up with GitHub; new workspaces get free credit.
  - [4] 2026-11-24: an account is required and the user must be 18 or act for a business | capture: sha256:d40e9f4635a4dc31a2cf9349a04a86b6e11c2fd8cb5a08bde6608076e9707c90 | quote: You need an account and must be at least 18 or act for a business.
  - [4] 2026-11-24: the vendor gives no uptime guarantee and warns of data loss on a phone | capture: sha256:d40e9f4635a4dc31a2cf9349a04a86b6e11c2fd8cb5a08bde6608076e9707c90 | quote: Data on a phone can be lost; keep your own copies of anything that matters.
- sources:
  - [1] https://mobilebox.dev/pricing
  - [2] https://mobilebox.dev/
  - [3] https://mobilebox.dev/docs
  - [4] https://mobilebox.dev/terms
  - [5] https://mobilebox.dev/signup
