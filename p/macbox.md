# macbox

> macbox.build | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macbox/ | JSON https://fshy.ajam.dev/api/v1/entity/macbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## macbox

- `compute/macbox` | trial-only | evidence documented | binding volume-quota | category hosted Mac build and simulator service for coding agents | tier Prepaid credit with a USD 10 starter grant
- needs card no, phone no, ID no, institution no | verified 2026-11-25T16:38:11.881Z (live) | stale on 2026-12-26
- url https://macbox.build/
- free tier: USD 10 of prepaid credit for a new account, about 200 Mac minutes at USD 0.05 a Mac minute; whole minutes only and a job under a minute is free; no subscription or minimum | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The USD 10 grant is a one-time starter credit, not a recurring monthly allowance. Uploading, waiting in line and starting the Mac are not billed. The credit is prepaid; there is no card charge described at signup.
- per-object cap: not an object-storage offer; no per-file size ceiling is published on the landing or setup pages | source: [1]
- retention: each user gets their own macOS VM and its build cache stays between runs; unused for 14 days and all of it is deleted, or immediately with macbox purge; a device build archive is kept for 24 hours | days: 14 | source: [1]
- egress: the VM can reach the internet but cannot reach other VMs or the provider network; no transfer allowance or per-GB price is published | metered: no | source: [1]
- identity: email | detail: the setup guide says the user signs in with GitHub and a new account gets USD 10 of credit; the sign-in page is a GitHub OAuth prompt asking for a GitHub username or email address and password and requesting read:user and user:email scopes. No card field appears at signup; a cloud agent uses a key added as a secret instead of an interactive login.
- interface: cli, rest
- limits:
  - volume-quota (binding): USD 0.05 per Mac minute, whole minutes only, a job under a minute is free; prepaid credit with no subscription or minimums, USD 10 at signup [1]
  - retention-clamped: a live session ends at macbox stop, on the next build/test/run in the folder, after 10 minutes with nobody watching, or at the 30-minute job limit [2]
  - write-gated: sign-in is GitHub OAuth requesting read:user and user:email; a cloud agent needs a key added as the MACBOX_API_KEY secret [3]
- limits note: Native iOS Xcode projects, workspaces, Swift packages, CocoaPods and XcodeGen are supported on the iOS simulator; React Native, Flutter, signing and TestFlight are not supported by the service itself. The VM has no inbound access to other VMs or the provider network.
- binding note: The prepaid credit at USD 0.05 a minute is what depletes first for repeated builds; the 30-minute job and 10-minute unwatched-session caps bound each run.
- interface detail: a macbox CLI and an MCP server that exposes build, test, run, screenshot and simulator interaction tools to Claude Code, Codex, Cursor and other agents; setup uses the guide at api.macbox.build/guide
- endpoint: https://api.macbox.build
- tooling: one CLI installed with curl or a package manager, plus an API key obtained at signup; agents call macbox commands or the MCP tools, and the Xcode-facing tools run MobileBuildMCP on the hosted Mac
- composes with: an agent runs macbox build and macbox test from a Linux or cloud sandbox, gets a live simulator link for run and ui interactions, and receives a signed-off-device archive to sign and upload elsewhere.
- reliability: The macOS VM is isolated: it reaches the internet but not other VMs or the provider network. It is deleted after 14 days unused, or immediately with macbox purge. A live session ends after 10 minutes without a viewer or at the 30-minute job limit. Signing and TestFlight are not performed by the service.
- notes: The operator's provider list quotes USD 3.00/h billed per minute, which matches the vendor's USD 0.05 per Mac minute (derived: 0.05 x 60 = USD 3.00 per hour). The vendor grants USD 10 of one-time credit, about 200 Mac minutes; no recurring free tier is published. macbox.build/pricing answered HTTP 404 on 2026-11-25; the price is quoted from the landing page.
- evidence note: the landing page, setup guide and public sign-in form were read on 2026-11-25; the quoted lines establish the price, starter credit, signup gate and retention rules. The rung stays documented because no live build was measured.
- extras:
  - shape.note: a dedicated macOS VM with the current Xcode and iOS simulator; CPU, RAM and disk sizes are not published
  - billing_model: prepaid per whole Mac minute with a one-time starter credit
  - free_tier_kind: one-time-credit
  - price_arithmetic: USD 0.05 per Mac minute = USD 3.00 per hour (derived: 0.05 x 60); USD 10 of starter credit is about 200 Mac minutes
  - session_cap.wall_clock_min: 30
  - session_cap.idle_reap_s: 600
  - session_cap.restart_required: no
  - session_cap.note: 30-minute job limit and a 10-minute unwatched-session end; signing and TestFlight are not supported by the service
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: no access to other VMs or the provider network; a live simulator link is given to the user
- evidence:
  - [1] 2026-11-25: the service sells hosted Mac time at USD 0.05 a Mac minute with a job under a minute free and no subscription or minimums | capture: sha256:1b9307d5f7edf1453d7e2fd9d3524b59ce944032a1255f167185914a17d0e578 | quote: $0.05 per Mac minute - You pay only while a build, tests, or a live session runs. - Whole minutes only. A job under a minute is free. - Uploading, waiting in line, and starting the Mac are free. - Prepaid credit. No subscription, no minimums.
  - [1] 2026-11-25: a new account starts with USD 10 of credit, about 200 Mac minutes | capture: sha256:1b9307d5f7edf1453d7e2fd9d3524b59ce944032a1255f167185914a17d0e578 | quote: Start with $10 of credit, about 200 Mac minutes.
  - [1] 2026-11-25: each user gets an isolated macOS VM with internet access that cannot reach other VMs or the provider network | capture: sha256:1b9307d5f7edf1453d7e2fd9d3524b59ce944032a1255f167185914a17d0e578 | quote: Each user gets their own macOS VM. It can reach the internet but not other VMs or our network.
  - [1] 2026-11-25: the VM and build cache are deleted after 14 days unused or immediately on purge | capture: sha256:1b9307d5f7edf1453d7e2fd9d3524b59ce944032a1255f167185914a17d0e578 | quote: After 14 days unused it is deleted, or right away with macbox purge.
  - [2] 2026-11-25: signup is with a GitHub account and a new account receives USD 10 of credit | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: They open it, check the code matches, and sign in with GitHub; a new user gets an account with $10 of credit on the way.
  - [2] 2026-11-25: a live session ends on stop, a new build, 10 minutes without a viewer or the 30-minute job limit | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: A session ends with `macbox stop`, a new build, test, or run in the same folder, 10 minutes with nobody using or watching it, or the 30-minute job limit.
  - [2] 2026-11-25: a cloud agent uses a key added as the MACBOX_API_KEY secret instead of an interactive login | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: Ask the user to get a key at https://api.macbox.build/signup?key=1, add it as the `MACBOX_API_KEY` secret in the agent's environment settings
  - [2] 2026-11-25: a device build archive is kept on the hosted Mac for 24 hours | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: macbox keeps the zip for 24 hours.
  - [3] 2026-11-25: signup redirects to a GitHub sign-in asking for a username or email address and password and requesting read:user and user:email | capture: sha256:213deac092df53b4c75b684c178aaa7c74f8335f6e66782acad2b4d539f393b0 | quote: Sign in to <strong>GitHub</strong> <br> to continue to <strong>Macbox</strong>
  - [3] 2026-11-25: the GitHub OAuth callback requests read:user and user:email scopes | capture: sha256:213deac092df53b4c75b684c178aaa7c74f8335f6e66782acad2b4d539f393b0 | quote: scope=read%3Auser+user%3Aemail
  - [3] 2026-11-25: the sign-in form asks for a GitHub username or email address and password | capture: sha256:213deac092df53b4c75b684c178aaa7c74f8335f6e66782acad2b4d539f393b0 | quote: Username or email address
  - [1] 2026-11-24: the price is USD 0.05 per Mac minute with whole-minute billing and a USD 10 starting credit | capture: sha256:1b9307d5f7edf1453d7e2fd9d3524b59ce944032a1255f167185914a17d0e578 | quote: $0.05 per Mac minute - You pay only while a build, tests, or a live session runs. - Whole minutes only. A job under a minute is free. - Uploading, waiting in line, and starting the Mac are free. - Prepaid credit. No subscription, no minimums. Start with $10 of credit, about 200 Mac minutes.
  - [2] 2026-11-24: a whole minute is charged for the part used and only running jobs are billed | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: $0.05 per Mac minute. Each job pays for the whole minutes it ran; the part of a minute left over is free, so a job under a minute costs nothing.
  - [2] 2026-11-24: the VM is reachable over the internet but not from other VMs or the operator network | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: Only you use that VM. It can reach the internet (to fetch packages), but not other VMs or our network.
  - [2] 2026-11-24: code and cache are deleted after 14 days unused | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: If you don't run anything for 14 days, we delete all of it. `macbox purge --yes` deletes it now.
  - [2] 2026-11-24: a live session ends after 10 minutes unwatched or at 30 minutes of runtime | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: A session ends with `macbox stop`, a new build, test, or run in the same folder, 10 minutes with nobody using or watching it, or the 30-minute job limit.
  - [2] 2026-11-24: two folders can run at once on the one Mac and a third waits | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: macbox runs two of your folders at the same time, on your one Mac. Each folder keeps its own code and build cache, and each running folder gets its own simulator. A third folder waits until one finishes
  - [2] 2026-11-24: sign-in is with GitHub and the starting credit arrives on a new account | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: They open it, check the code matches, and sign in with GitHub; a new user gets an account with $10 of credit on the way.
  - [3] 2026-11-24: the signup page is a GitHub OAuth login asking for a username or email and user:email scope | capture: sha256:f74b9b9757626502b964c4f1953bb05272cb8c1d472fc87ab0084088054ffb40 | quote: scope%3Dread%253Auser%2Buser%253Aemail
  - [1] 2026-11-24: the offer is a real cloud Mac reached by one CLI from any machine | capture: sha256:1b9307d5f7edf1453d7e2fd9d3524b59ce944032a1255f167185914a17d0e578 | quote: From anywhere Your own Mac, a Linux box, or a cloud agent like Claude Code on the web, Codex, or Cursor. Nothing to install but one CLI.
  - [2] 2026-11-24: only native iOS projects and the latest Xcode work today; signing and TestFlight are not supported | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: Not yet: signing on the Mac, uploading to TestFlight for you, React Native, Flutter, private packages that need SSH keys.
  - [3] 2026-11-25: the Macbox signup URL redirects to a GitHub sign-in form whose login field accepts a GitHub username or email address | capture: sha256:d6d3e2d7477cdc62932369fa7a8f2fce7031c323496f4022855ca5126487c05a | quote: Username or email address
  - [2] 2026-11-25: the setup guide makes GitHub sign-in the route to a new account | capture: sha256:5c8958611e6c8a8514232ee5907ae3d82567eb0790075f6295240d45adc4f85b | quote: They open it, check the code matches, and sign in with GitHub; a new user gets an account with $10 of credit on the way.
- sources:
  - [1] https://macbox.build/
  - [2] https://api.macbox.build/guide/
  - [3] https://api.macbox.build/signup?key=1
