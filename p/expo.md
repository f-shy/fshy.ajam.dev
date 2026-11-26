# Expo Simulators

> expo.dev | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/expo/ | JSON https://fshy.ajam.dev/api/v1/entity/expo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Expo

- `compute/expo` | qualifies-with-caveat | evidence documented | binding request-rate | category macOS host
- needs card no, phone no, ID no, institution no | verified 2026-11-24T11:38:13.593Z (live) | stale on 2026-12-25
- url https://expo.dev
- free tier: Expo and the Expo SDK are free and open source (MIT license). Expo services (formerly EAS) have a free tier: 15 Android and 15 iOS builds, 60 min. on CI/CD Workflows, updates to 1K MAUs, 100 GiB of global edge bandwidth and 20 GiB of update storage. | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: Observe data retention is 90 days on every plan; Hosting preview deployments are deleted after 30 days on Free and 90 days on paid plans; Simulator artifacts are retained 30 days. | source: [1]
- egress: EAS Update global edge bandwidth: 100 GiB on Free and Starter, then $0.10 per GiB on Starter; the Hosting table lists no bandwidth row | metered: yes | free allowance: 100 GiB of EAS Update global edge bandwidth on the Free plan | source: [1]
- identity: email | detail: The hosted Expo services are used through an account; the signup page renders 'Create your Expo account' with a sign-in link. 'Get started for free: https://expo.dev/signup' is published on the front page.
- interface: unknown
- limits:
  - request-rate (binding): Free includes up to 15 Android and 15 iOS builds and 60 min. on CI/CD Workflows, with a 45-minute build timeout and 5 concurrencies, up to 1 on macOS [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the page was read on 2026-10-22 and states the licence position and that EAS has a free tier with the three meters named. It does not publish the free tier's minute count, so no figure is given
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a build is a job with its own timeout; the free tier's minute pool is unstated here
  - free_tier_kind: allowance
  - granularity.min_billed_s: 60
  - burst_x: 2.4032
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Expo and the Expo SDK are free and open source (MIT license). EAS has a free tier and usage-based paid plans for build minutes, OTA updates, hosting bandwidth, and priority support.'…
  - [2] 2026-11-03: EAS Update global edge bandwidth is 100 GiB on Free, then $0.10 per GiB on Starter | capture: sha256:57ba013c713b80abef59829dadf62a18b998a0030a57629b779086ade502174e | quote: | Global edge bandwidth | 100 GiB | 100 GiB, then $0.10 per GiB
  - [2] 2026-11-24: the free tier publishes a fixed build allowance | capture: sha256:f9be4a65ff1a2fdae3d8f7e04f69d66750d7026a0f2875d2f731551782aa834a | quote: - 15 Android and 15 iOS builds
  - [2] 2026-11-24: the free allowance mixes build counts, minutes, users and bandwidth, which fits no single unit | capture: sha256:f9be4a65ff1a2fdae3d8f7e04f69d66750d7026a0f2875d2f731551782aa834a | quote: Every plan includes Expo Build, Expo Submit, Expo Update, and CI/CD Workflows. Plans differ in included credit, queue priority, concurrency, included monthly active users (MAUs) for updates, and support.
  - [3] 2026-11-24: the hosted services require an account | capture: sha256:b5dabe55b4d9361e5429478ca86530722ac2e62671630e583108901df9c2115d | quote: # Create your Expo account
  - [2] 2026-11-24: the free tier publishes a build timeout and build counts | capture: sha256:f9be4a65ff1a2fdae3d8f7e04f69d66750d7026a0f2875d2f731551782aa834a | quote: | Build timeout | 45-minute build timeout | 2-hour build timeout | 2-hour build timeout | 2-hour build timeout |
  - [2] 2026-11-24: the pricing page publishes retention windows for the hosted services | capture: sha256:f9be4a65ff1a2fdae3d8f7e04f69d66750d7026a0f2875d2f731551782aa834a | quote: | Logs retention | 7 days | 3 months | 3 months | 3 months |
  - [2] 2026-11-24: the free tier includes 100 GiB of global edge bandwidth | capture: sha256:f9be4a65ff1a2fdae3d8f7e04f69d66750d7026a0f2875d2f731551782aa834a | quote: | Global edge bandwidth | 100 GiB | 100 GiB, then $0.10 per GiB _(100 GiB of global edge bandwidth included. For every additional MAU over 3,000 MAUs, 40 MiB of bandwidth is added to your bandwidth quota. After that, you'll be charged $0.10 per GiB.)_ | 1 TiB, then $0.10 per GiB
- sources:
  - [1] https://expo.dev
  - [2] https://expo.dev/pricing
  - [3] https://expo.dev/signup

## Expo Simulators (EAS)

- `compute/expo-simulators-eas` | paid-only | evidence documented | binding volume-quota | category cloud iOS simulator and Android emulator | tier Starter, with 60 simulator minutes included until 2027
- needs card unknown, phone no, ID no, institution no | verified 2026-11-25T16:38:10.532Z (live) | stale on 2026-12-26
- url https://expo.dev/pricing
- free tier: Starter, Production and Enterprise plans include 60 simulator minutes a month until 2027; the Free plan lists Simulators as coming soon, and sessions start only on paid plans. | unit: minutes | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: Starter is $19/month plus additional usage cost. Usage beyond the included minutes is $0.10 per simulator minute, billed per second.
- per-object cap: not applicable: the unit is a simulator session, not an object; one artifact can be up to about 5 GiB. | source: [2]
- retention: Job logs on the session page are available for 30 days after the session is created; session artifacts such as screenshots and recordings are kept until the session is deleted. | days: 30 | source: [2] | note: Artifact retention on the pricing table is 30 days; the security page says artifacts survive until the user deletes the session.
- egress: Without local egress, all traffic from the simulator exits from Expo infrastructure; with --egress local, device traffic exits from the user's computer and the egress client refuses local, private, link-local and multicast addresses. | metered: no | source: [2]
- identity: email | detail: Sessions require a paid Starter, Production or Enterprise plan. Whether a card is collected at signup is unverified: behind a sign-up.
- interface: rest, graphql, cli, browser, chat
- limits:
  - volume-quota (binding): 60 simulator minutes a month included until 2027 on Starter, Production and Enterprise; then $0.10 per iOS Simulator or Android Emulator minute [1]
  - request-rate: 115 minutes maximum session duration; 5 concurrencies on Starter up to 2 on macOS [1]
- limits note: The session timer starts when the session is ready; the job running the session has a hard limit of the maximum duration plus five minutes. An unnamed session has no idle timeout until --max-idle-time-minutes is set. Sessions wait in the account's job concurrency queue.
- binding note: The 60 included minutes a month, then the $0.10 per-minute meter, bind before the 115-minute per-session cap for a single agent.
- interface detail: Sessions start with the `eas simulator` CLI, the REST API or a browser live view; agents drive the device with agent-device, Argent or Appium commands, including MCP.
- endpoint: https://api.expo.dev/v2/device-run-sessions
- tooling: The EAS CLI and REST API start and stop sessions; Claude Code, Codex, Cursor, agent-device, Argent, Appium and Maestro drive the simulator.
- composes with: A coding agent can install a build into an isolated cloud simulator, drive it, and attach a recording to a pull request without a local Mac.
- reliability: A session that is not stopped runs until its maximum duration or idle limit; the REST API returns controller tokens only while the session is in-progress, and every session is isolated in its own VM.
- notes: Expo Simulators is a hosted simulator/emulator service, not user-run software. The Free plan has no Simulators access (listed as coming soon); paid plans include 60 minutes a month until 2027 and then bill $0.10 a simulator minute. Session artifacts survive until the session is deleted; job logs are kept 30 days.
- evidence note: Price, included minutes, session cap and retention are quoted from Expo's own pricing and documentation pages read on 2026-11-25; the signup gate is from the signup page.
- extras:
  - billing_model: monthly plan with included minutes then per-second usage
  - free_tier_kind: included minutes on a paid plan
  - term: monthly
  - price_arithmetic: $0.10 per minute is $6.00 an hour
  - session_cap.wall_clock_min: 115
  - session_cap.note: no idle timeout unless --max-idle-time-minutes is set
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - network_out.default_egress: Expo infrastructure
  - artifacts: one artifact up to about 5 GiB; artifact download URL needs no login but contains a long random key
- evidence:
  - [1] 2026-11-25: Starter costs $19 a month plus usage | capture: sha256:f9be4a65ff1a2fdae3d8f7e04f69d66750d7026a0f2875d2f731551782aa834a | quote: ### Starter — $19/month plus additional usage cost
  - [1] 2026-11-25: 60 simulator minutes a month are included until 2027 on paid plans and the Free plan lists Simulators as coming soon | capture: sha256:f9be4a65ff1a2fdae3d8f7e04f69d66750d7026a0f2875d2f731551782aa834a | quote: Simulator minutes | Coming soon | Usage-based pricing (60 min/month included until 2027) | Usage-based pricing (60 min/month included until 2027) | Custom (60 min/month included until 2027) _(Custom pricing available. [Contact us](https://expo.dev/contact) for more information.)_
  - [1] 2026-11-25: the iOS Simulator rate is $0.10 a minute | capture: sha256:f9be4a65ff1a2fdae3d8f7e04f69d66750d7026a0f2875d2f731551782aa834a | quote: | iOS Simulator | $0.10 |
  - [1] 2026-11-25: the rate is billed per second and applies to Starter and Production | capture: sha256:f9be4a65ff1a2fdae3d8f7e04f69d66750d7026a0f2875d2f731551782aa834a | quote: Billed per second while a session runs. These rates apply to Starter and Production. Custom pricing available for Enterprise plans. [Contact us](https://expo.dev/contact) for more information.
  - [3] 2026-11-25: Simulators are available on paid plans only | capture: sha256:34790800b8746bdd77e05181991619caf802dbe527472a49c7230928a7c8100b | quote: Expo Simulators is available on the Starter, Production, and Enterprise plans. Check the account of the current project:
  - [3] 2026-11-25: sessions stop at a 115-minute maximum | capture: sha256:34790800b8746bdd77e05181991619caf802dbe527472a49c7230928a7c8100b | quote: Only paid plans can start sessions. Each session has a maximum duration of 115 minutes. When the session reaches it, Expo Simulators stops the session.
  - [2] 2026-11-25: simulator traffic exits Expo infrastructure by default, or the user's computer with local egress | capture: sha256:5cf0ae105920cbb28a40d00ae96696adb9ff0aae73a8734205c6cdf4315af4f7 | quote: - Default egress: without local egress, all traffic from the simulator exits from Expo infrastructure.
  - [2] 2026-11-25: job logs are available for 30 days and artifacts survive until the session is deleted | capture: sha256:5cf0ae105920cbb28a40d00ae96696adb9ff0aae73a8734205c6cdf4315af4f7 | quote: - Job logs on the session page are available for 30 days after the session is created.
  - [4] 2026-11-25:  | capture: sha256:b5dabe55b4d9361e5429478ca86530722ac2e62671630e583108901df9c2115d | quote: Unsubscribe anytime.
  - [5] 2026-11-25: the product is on-demand cloud iOS simulators and Android emulators for agents | capture: sha256:b35a80c4a78c73eeac551561df497b2787c6fa5479fe1098e21fff3b6033654e | quote: Spin up secure cloud iOS simulators and android emulators on demand. Your agents install a build, drive it, and verify their own work, running as many in parallel as you need.
  - [4] 2026-11-25: the Expo signup form labels its email input "Email", so an email address is the identity required to register | capture: sha256:5fc842a8f9e515da9fc2e6950c76173b94f9651dc4eb2421ac85047965eba14c | quote: data-form-field-label="true" for="email"><div class="flex items-center"><span class="text-sm font-medium">Email</span></div></label>
  - [6] 2026-11-25: even the GitHub sign-up route on Expo requires the user's email address, so email is the identity gate | capture: sha256:70fe7dee2ba75cc7a83c795a23290659c5d7d50a5d0e8f2ab6fe9801ddfd2738 | quote: We require permission to view your email address in order to offer GitHub Sign In as an authentication method.
- sources:
  - [1] https://expo.dev/pricing
  - [2] https://docs.expo.dev/eas/simulators/reference/security-and-data.md
  - [3] https://docs.expo.dev/eas/simulators/reference/usage-and-billing/
  - [4] https://expo.dev/signup
  - [5] https://expo.dev/services/simulators
  - [6] https://expo.dev/changelog/sign-in-with-github
