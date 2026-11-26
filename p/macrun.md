# MacRun

> macrun.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macrun/ | JSON https://fshy.ajam.dev/api/v1/entity/macrun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MacRun

- `compute/macrun` | paid-only | evidence documented | binding volume-quota | category rented Mac (bare metal) | tier M6 GitHub Actions runner, monthly
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T02:12:34.858Z (live) | stale on 2026-12-26
- url https://macrun.dev/pricing
- free tier: No free tier: the dedicated M6 GitHub Actions runner is $139/mo with unlimited macOS build minutes and no meter, cancel anytime; a by-the-day rental of the same M6 is $15 for up to 6 days. | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The provider list's $0.19 an hour is $139 a month divided by 730 hours. The agent plan on the same M6 is $169 a month. Annual billing is 10 months for 12.
- per-object cap: not applicable: the unit is a dedicated Mac mini with 16 GB memory and 256 GB storage, not an object; no per-artifact cap is published | source: [1]
- retention: the Mac is wiped when the time is up and the user can cancel anytime from the portal; no separate retention period for files left on the machine is stated | source: [1]
- egress: unverified: no egress allowance, data cap or price is stated on the pages read; the machine is in the vendor's own facility in New Jersey, United States | metered: no | source: [1]
- identity: card | detail: the signup form asks for Name, Email and an optional GitHub org or repo URL, and states 'Secure checkout via Stripe. After payment we provision your machine and email you when it's ready.' The pricing page says pay by card and a full refund in the first 3 days on email request.
- interface: ssh, git, browser
- limits:
  - volume-quota (binding): $139 a month for the M6 runner plan with unlimited macOS build minutes; no per-minute meter [1]
- limits note: the M4 runner is $119 a month and the M5 Pro runner $269 a month before a $199 build fee; the day rental is $15 for up to 6 days and the week rental is $59 for up to 4 weeks; prices are grandfathered.
- binding note: the flat monthly price with an unlimited build-minute allowance is the only published ceiling; there is no per-minute or byte quota to bind first.
- interface detail: GitHub Actions ready via a registered self-hosted runner; GitLab, Bitbucket, Buildkite and Jenkins also work; a desktop session opens from a browser tab and SSH is enabled by accepting a Tailscale invite emailed to the user
- tooling: a GitHub Actions runner registered on the dedicated Mac with a config.sh command, Xcode selection and cache paths; the user installs and runs the runner agent on the rented Mac, which is the hosted offer
- composes with: the always-on M6 runs unlimited macOS builds as a self-hosted GitHub Actions runner with pinned Xcode and warm local SSD caches, and the same machine can be leased as an agent Mac; state that must outlive the lease belongs in a separate storage record.
- reliability: the machine is wiped when the lease ends; the vendor offers a full refund within the first 3 days by email and states a 3-day pre-order window, with live uptime on its status page
- notes: No free tier: the M6 GitHub Actions runner is USD 139 a month with unlimited build minutes, and a day rental is USD 15. The provider list's USD 0.19 an hour is USD 139 divided by 730 hours.
- evidence note: prices, unlimited build minutes, hardware, signup fields and payment rail are quoted from first-party pages read on 2026-11-25; the signup fields were read but no rental was made.
- extras:
  - shape.ram_gib: 16
  - shape.disk_gib: 256
  - shape.gpu_class: Apple M6
  - shape.note: dedicated M6 Mac mini in the vendor's facility in New Jersey, United States
  - billing_model: flat monthly with unlimited build minutes; day and week rentals
  - free_tier_kind: none
  - price_arithmetic: USD 139 / 730 hours = USD 0.19 an hour
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: SSH via a Tailscale invite emailed to the user
  - session_cap.restart_required: no
  - session_cap.note: cancel anytime; the box is wiped when the lease ends
- evidence:
  - [1] 2026-11-25: the dedicated M6 GitHub Actions runner is USD 139 a month with unlimited macOS build minutes | capture: sha256:da74f0b09d5e81ff883497d4f8aa15409c0566111c59965007efaa38d4c4f2d8 | quote: $139/mo
  - [1] 2026-11-25: the runner plan has unlimited macOS build minutes and no meter | capture: sha256:da74f0b09d5e81ff883497d4f8aa15409c0566111c59965007efaa38d4c4f2d8 | quote: Unlimited macOS build minutes, no meter
  - [1] 2026-11-25: the same M6 can be rented for USD 15 a day or USD 59 a week without a subscription | capture: sha256:da74f0b09d5e81ff883497d4f8aa15409c0566111c59965007efaa38d4c4f2d8 | quote: Rent the M6 by the day for $15, up to 6 days, or by the week for $59, up to 4 weeks.
  - [1] 2026-11-25: the M6 runner has 16 GB memory and 256 GB storage | capture: sha256:da74f0b09d5e81ff883497d4f8aa15409c0566111c59965007efaa38d4c4f2d8 | quote: | M6 | 16 GB · 256 GB | CI builds and cloud-model agents | Available now | $139/mo | $169/mo | none |
  - [2] 2026-11-25: signup asks for a name and email, with an optional GitHub org or repo URL, and payment is by Stripe | capture: sha256:1e9cd02a414e4d7fbdcd87d26e5947268d9b9741588f07f29b28cb67203a8f24 | quote: Secure checkout via Stripe. After payment we provision your machine and email you when it's ready.
  - [3] 2026-11-24: a day pass is USD 15 for 24 hours and a week is USD 59, paid once | capture: sha256:632e58921c8dd68fa41bdb64e3eaab5a6cb5c894001deebb0fff3a5a70049644 | quote: A MacRun pass is $15 for 24 hours or $59 for a week, paid once.
  - [4] 2026-11-24: the signup asks for a name, an email and an optional GitHub org or repo URL | capture: sha256:cceac82cb01792440ccb2d12020f8951f5acafade49efc43b63b679c08a4ec28 | quote: Name Email GitHub org or repo URL · optional
  - [4] 2026-11-24: checkout is a one-time Stripe payment with no subscription | capture: sha256:cceac82cb01792440ccb2d12020f8951f5acafade49efc43b63b679c08a4ec28 | quote: Secure checkout via Stripe. One payment. No subscription, and nothing renews.
  - [5] 2026-11-24: no free trial is offered | capture: sha256:44c7d3f775b8fb189bb004c73e190ee2c2bd474651030b1cb0dd3449922c3bc2 | quote: You want a free trial. We do not offer one.
  - [3] 2026-11-24: SSH is available only over a private Tailscale network with no public port | capture: sha256:632e58921c8dd68fa41bdb64e3eaab5a6cb5c894001deebb0fff3a5a70049644 | quote: At MacRun, every Mac sits on a private Tailscale network. There is no public SSH port.
  - [6] 2026-11-24: SSH and screen sharing are the connection methods | capture: sha256:82e283abe88537566796e021bbaf4593cc36a8dbe2aabc40b8442a079670f591 | quote: SSH and screen sharing over a private Tailscale network.
  - [7] 2026-11-24: build minutes on the CI runner plan are unlimited with no meter | capture: sha256:75f1ab387146930b558fb531e177ff2899ed77b1ac8de329668d230dbc0f9533 | quote: Unlimited macOS build minutes, no meter
  - [8] 2026-11-24: egress is monitored in aggregate at the hub for abuse signatures | capture: sha256:48f0c88895f4894fb40ea8bf937661e3195386f589812b8b003e8988190e9f87 | quote: We monitor aggregate network egress at the hub for abuse signatures such as bulk SMTP, mass-messaging patterns, anonymizing traffic, and scanning. Every unit reaches the internet through the same address.
  - [9] 2026-11-24: data is wiped at the end of the lease | capture: sha256:daaf7b124c5107f1c098a822c8c0cf073a2fc7f83d5f88f40bed4db5de2344b7 | quote: When your lease ends, whether by cancellation, non-payment, or termination, the unit is wiped automatically and permanently.
- sources:
  - [1] https://macrun.dev/pricing
  - [2] https://macrun.dev/signup
  - [3] https://macrun.dev/cloud-mac
  - [4] https://macrun.dev/signup?term=day&n=1
  - [5] https://macrun.dev/rent-a-mac-mini
  - [6] https://macrun.dev/rent-a-mac-for-a-day
  - [7] https://macrun.dev/
  - [8] https://macrun.dev/legal/aup
  - [9] https://macrun.dev/legal/terms
