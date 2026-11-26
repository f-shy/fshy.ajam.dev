# NoMac

> nomac.app | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nomac/ | JSON https://fshy.ajam.dev/api/v1/entity/nomac.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NoMac

- `compute/nomac` | paid-only | evidence documented | binding volume-quota | category on-demand cloud Mac for agents | tier Pay as you go, prepaid credit
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.836Z (live) | stale on 2026-12-26
- url https://nomac.app/
- free tier: no free tier; USD 0.90 an hour billed per minute with a one-minute minimum, paid from prepaid credit sold in USD 10 packs that never expires; there is no subscription | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The landing page gives a five-minute TestFlight session as 7.5 cents. Larger top-ups lower the rate to USD 0.60 an hour, and a 7-day money-back guarantee applies to the first purchase. A job under a minute is billed as one minute.
- per-object cap: not an object-storage offer; 20 GB of encrypted persistent drive is kept per Mac between sessions | source: [1] | note: The 20 GB figure is the persistent drive, not a per-file limit.
- retention: the Mac and every file outside ~/drive are deleted when the session stops; the encrypted 20 GB drive at ~/drive persists between sessions | source: [2]
- egress: not published as a transfer allowance or per-GB price; upload and download links go through *.r2.cloudflarestorage.com and the Mac has internet access | metered: no | source: [2]
- identity: email | detail: the sign-in page says that signing in creates the account and offers Apple sign-in; the setup guide says to sign in at nomac.app and add credit of USD 10 to USD 1000, with agents able to open a payment link. Credit is prepaid through a payment link, not charged automatically; no phone or ID document is requested on the sign-in page.
- interface: ssh, rest, browser, cli
- limits:
  - volume-quota (binding): USD 0.90 an hour billed per minute, one-minute minimum, prepaid in USD 10 packs; no automatic overage [2]
  - retention-clamped: a session stops after 10 idle minutes or 2 hours by default, and every session has a spending cap [1]
  - write-gated: signing in creates the account; prepaid credit must be added before a Mac can start [3]
- limits note: A Mac takes about 30 seconds to become ready. Queue and setup time are free; ready time includes time between commands. A disconnect does not stop billing. App Store submission requires an Apple Developer account, supplied by the user.
- binding note: The per-minute prepaid credit meter and the one-minute minimum are what a short job hits first; the idle and two-hour caps stop longer sessions.
- interface detail: MCP over streamable HTTP at mcp.nomac.app/mcp, an @nomac/cli command-line tool, a REST API, SSH into the running Mac, and a browser desktop to watch or take over the session
- endpoint: https://nomac.app/api/v1
- tooling: Node 20 or later and OpenSSH for the CLI; an MCP client such as Claude Code, Codex, Cursor, VS Code or ChatGPT; the hosted MCP needs only a sign-in
- composes with: an agent opens a disposable Mac over MCP, builds an iOS app with the preinstalled Xcode 27, uploads to TestFlight and stops the machine, with the persistent drive carrying build caches for later runs.
- reliability: Every session uses a fresh Mac that is deleted on stop; a disconnect does not stop billing, so the session must be stopped explicitly or it reaps after 10 idle minutes or 2 hours. Larger top-ups lower the hourly rate and credit never expires.
- notes: The operator's provider list quotes USD 0.90/h billed per minute, matching the landing page. No free allowance is published: a job under a minute is billed as one minute and credit is prepaid. Larger top-ups bring the rate to USD 0.60 an hour on the vendor page. nomac.app/pricing answered HTTP 404 on 2026-11-25; the price is quoted from the landing page and install guide.
- evidence note: the landing page, install guide, CLI reference and sign-in page were read on 2026-11-25; the quoted lines establish the price, billing minimum, reaping rules, storage, access paths and signup gate. No account, credit purchase or Mac session was created, so the rung is documented rather than measured.
- extras:
  - shape.disk_gib: 20
  - shape.note: real Apple silicon macOS; vCPU and RAM are not published, the persistent drive is 20 GB
  - billing_model: prepaid pay-as-you-go per minute
  - free_tier_kind: none
  - price_arithmetic: USD 0.90 an hour billed per minute; USD 10 of credit is 11.1 hours as stated on the install guide
  - session_cap.wall_clock_min: 120
  - session_cap.idle_reap_s: 600
  - session_cap.restart_required: no
  - session_cap.note: default 2-hour cap and 10-minute idle reap, both configurable in the CLI
  - network_out.allow_outbound: yes
  - network_out.ports: SSH into the Mac; MCP over streamable HTTP
- evidence:
  - [1] 2026-11-25: the service sells on-demand cloud macOS for agents at USD 0.90 an hour billed per minute with no subscription | capture: sha256:0d4ef39c1920967106e46d16f87cf5e21dba4cad27886f4c18321c10bc5b8039 | quote: $0.90 an hour, billed per minute. Pay as you go, no subscription. Your credit never expires.
  - [1] 2026-11-25: each Mac gets a 20 GB encrypted drive kept between sessions | capture: sha256:0d4ef39c1920967106e46d16f87cf5e21dba4cad27886f4c18321c10bc5b8039 | quote: An encrypted drive for every Mac, kept between sessions.
  - [1] 2026-11-25: sessions stop after 10 idle minutes or 2 hours by default with a per-session spending cap | capture: sha256:0d4ef39c1920967106e46d16f87cf5e21dba4cad27886f4c18321c10bc5b8039 | quote: It stops on its own after 10 idle minutes or 2 hours by default, and every session has a spending cap.
  - [1] 2026-11-25: App Store submission needs an Apple Developer account supplied by the user | capture: sha256:0d4ef39c1920967106e46d16f87cf5e21dba4cad27886f4c18321c10bc5b8039 | quote: Yes. Your agent signs your app, uploads it to TestFlight and submits it for review. You need an Apple Developer account.
  - [2] 2026-11-25: the setup asks for a sign-in and prepaid credit of USD 10 to USD 1000 at USD 0.90 an hour with no subscription or Apple setup needed | capture: sha256:25ffdb34ccbd6c17c33c7b4e2cfde848d0456a4eb40118197038c59f6f597f21 | quote: Sign in at https://nomac.app/dash and add credit: $10 to $1,000, at $0.90 an hour, billed per minute ($10 = 11.1 hours). Credit never expires. No subscription, no Apple setup required.
  - [2] 2026-11-25: a one-minute minimum applies and there is no automatic overage | capture: sha256:25ffdb34ccbd6c17c33c7b4e2cfde848d0456a4eb40118197038c59f6f597f21 | quote: One-minute minimum, then billed per minute. No automatic overage.
  - [2] 2026-11-25: the Mac is reached over MCP, the CLI, the API or SSH, and uploaded files travel through Cloudflare R2 | capture: sha256:25ffdb34ccbd6c17c33c7b4e2cfde848d0456a4eb40118197038c59f6f597f21 | quote: An agent in a sandbox that limits the network needs nomac.app and *.nomac.app allowed, and *.r2.cloudflarestorage.com for upload and download links, whose files travel there.
  - [4] 2026-11-25: SSH access and a default two-hour session with a USD 5 spending cap are offered | capture: sha256:8d1160e060705e60af403cfd79cdfeaef149e6c4a0e19814ffb18275c9224f63 | quote: nomac start Starts a Mac, or reconnects to this folder's. It runs 2 hours by default (`--max-duration` sets longer, with no longest), stops after 10 idle minutes (`--idle-timeout`) and spends $5 at most (`--max-cost`).
  - [3] 2026-11-25: signing in creates the account and Apple sign-in is available | capture: sha256:ff383ee1f25732a12439b915f41fcf3a2194f71b487c51ac11acdbfd3413090e | quote: New to NoMac? Signing in creates your account. Signed up with Apple? Continue with Apple.
  - [5] 2026-11-24: the published rate is USD 0.90 an hour or 1.5 cents a minute, billed per minute from prepaid credit with no subscription | capture: sha256:a88c4a2ccfa59ecb8ec2a5b045d0fd4858a1f5b880004870c1973b2abe426981 | quote: $0.90 an hour for a Mac or a phone (1.5¢ a minute), billed per minute from prepaid credit. No subscription, no minimum term.
  - [5] 2026-11-24: billing covers ready time only, with a one-minute minimum | capture: sha256:a88c4a2ccfa59ecb8ec2a5b045d0fd4858a1f5b880004870c1973b2abe426981 | quote: Ready time only. Billing runs while the machine is ready, in whole minutes, one minute at least. Waiting for one and setting it up are free.
  - [5] 2026-11-24: credit is sold in USD 10 packs of 11.1 hours and never expires | capture: sha256:a88c4a2ccfa59ecb8ec2a5b045d0fd4858a1f5b880004870c1973b2abe426981 | quote: $10 packs of 11.1 hours, 1 to 100 at a time. Credit never expires, and nothing renews.
  - [5] 2026-11-24: each Mac has a USD 5 default spend cap | capture: sha256:a88c4a2ccfa59ecb8ec2a5b045d0fd4858a1f5b880004870c1973b2abe426981 | quote: Every Mac also has a spend cap, $5 unless your agent sets another, so a forgotten Mac never empties the account. See [Limits](https://nomac.app/docs/limits).
  - [5] 2026-11-24: the price has been USD 0.90 an hour since 1 November 2026 | capture: sha256:a88c4a2ccfa59ecb8ec2a5b045d0fd4858a1f5b880004870c1973b2abe426981 | quote: The price is $0.90 an hour since November 1, 2026. Credit bought before then keeps the hours it bought: we added the difference to each account as promotional credit.
  - [6] 2026-11-24: default session length 2 hours, idle stop after 10 minutes, and 1 Mac at once by default | capture: sha256:30a4869d538bce706ed00655f1ab8bf160a6730ef0db5dd333effcaeed70855d | quote: Session length 2 hours by default, with no longest; `extend_mac` or `nomac extend` adds time. A phone runs up to 8 hours. Idle stop After 10 minutes without a command, SSH connection or desktop viewer, up to 60. Spend cap $5 per Mac by default, enough for 5 hours 33 minutes, set at each start.
  - [6] 2026-11-24: a 20 GB drive at ~/drive is kept between sessions, with 10 included per account | capture: sha256:30a4869d538bce706ed00655f1ab8bf160a6730ef0db5dd333effcaeed70855d | quote: One per Mac at `~/drive`, 20 GB each, kept between sessions; 10 included per account, and a drive you name past them costs 1¢ per GB of changed data at each save. Deleted after 30 days without a session.
  - [6] 2026-11-24: an upload or download link is 2 GiB and a command outputs at most 8 MiB plus a tail | capture: sha256:30a4869d538bce706ed00655f1ab8bf160a6730ef0db5dd333effcaeed70855d | quote: Upload or download link 2 GiB. A download link works for an hour by default, a day at most.
  - [1] 2026-11-24: the Mac has root access, Xcode 27 and iOS Simulator, and is driven over MCP, CLI, API or SSH | capture: sha256:0d4ef39c1920967106e46d16f87cf5e21dba4cad27886f4c18321c10bc5b8039 | quote: On-demand cloud macOS for AI agents. Short-lived, disposable sessions, billed by the minute.
  - [7] 2026-11-24: credit is prepaid with no subscription, billed by the minute with a one-minute minimum, and there are no overage charges | capture: sha256:a6cb5f7e5116a103a20d5668eaa6aaa1485048d481aa5fd25be1b3bb7b5baa76 | quote: NoMac is paid for with prepaid credit. Polar sells credit as our merchant of record and handles payment, tax and invoices. There is no subscription and nothing renews. Credit does not expire.
  - [7] 2026-11-24: stopping deletes files outside the drive and the drive is deleted after 30 days without a session | capture: sha256:a6cb5f7e5116a103a20d5668eaa6aaa1485048d481aa5fd25be1b3bb7b5baa76 | quote: A drive keeps your files between sessions. A drive is deleted after 30 days without a session, when you reset it, or when your platform deletes its user's data.
  - [8] 2026-11-24: signing in creates an account and offers Apple sign-in; no other identity field is stated on that page | capture: sha256:ff383ee1f25732a12439b915f41fcf3a2194f71b487c51ac11acdbfd3413090e | quote: New to NoMac? Signing in creates your account. Signed up with Apple? Continue with Apple.
  - [2] 2026-11-24: the human buys credit at the dashboard and an agent is told never to enter payment details | capture: sha256:25ffdb34ccbd6c17c33c7b4e2cfde848d0456a4eb40118197038c59f6f597f21 | quote: Sign in at https://nomac.app/dash and add credit: $10 to $1,000, at $0.90 an hour, billed per minute ($10 = 11.1 hours). Credit never expires. No subscription, no Apple setup required. Agents can buy for you: nomac credits buy --packs 1 opens a payment link.
- sources:
  - [1] https://nomac.app/
  - [2] https://nomac.app/install
  - [3] https://nomac.app/sign-in?next=/dash
  - [4] https://nomac.app/docs/cli
  - [5] https://nomac.app/docs/pricing
  - [6] https://nomac.app/docs/limits
  - [7] https://nomac.app/terms
  - [8] https://nomac.app/sign-in
