# Kubi

> trykubi.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trykubi/ | JSON https://fshy.ajam.dev/api/v1/entity/trykubi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kubi

- `compute/kubi` | paid-only | evidence documented | binding volume-quota | category cloud desktop sandbox | tier Persistent screen / disposable screen
- needs card no, phone no, ID no, institution no | verified 2026-11-25T16:38:11.396Z (live) | stale on 2026-12-26
- url https://trykubi.com/pricing
- free tier: no free tier: a persistent screen is USD 20 a month at the founding price, USD 25 list, and a disposable screen is USD 0.035 an hour from prepaid credit starting at USD 10; USD 5 of credit for disposable screens is given when a card is added | unit: none | metered on: none | read on: 2026-11-25 | source: [1] | note: The USD 5 card credit is a one-time card-gated amount, not a standing free tier.
- per-object cap: not applicable: the unit is a VM with a disk, not an object; each screen has a 50 GB disk | source: [1] | note: Snapshots are 3 per screen, up to 50 GB of changes.
- retention: a persistent screen runs until stopped or deleted and keeps its disk when stopped; a stopped disposable screen is deleted after 7 days unless started again; each call and its screenshot are kept for 30 days | source: [1]
- egress: all screen traffic leaves through the user's own proxy; if it fails the screen goes offline instead of using the Kubi network; no egress price or allowance is published on the pages read | metered: no | source: [2]
- identity: email | detail: the hosted sign-up page offers Google, GitHub, passkey or email magic-link sign-in; the vendor states there is no waitlist and no approval at sign-up. A card is required for the USD 5 disposable-screen credit and for a persistent subscription through Stripe; no phone number or ID document is stated
- interface: rest, chat, browser
- limits:
  - volume-quota (binding): a disposable screen bills USD 0.035 an hour by the minute from prepaid credit, USD 0.003 an hour stopped, with a USD 10 minimum top-up [1]
  - volume-quota (binding): a persistent screen is USD 20 a month running or stopped at the founding price, USD 25 list, with one subscription per organization and a screen cap per organization [1]
  - per-object-cap: each screen has 4 vCPU, 8 GB of memory and a 50 GB disk; 5 templates per organization and 3 snapshots per screen [1]
- limits note: Private beta with early access sign-up and no waitlist or approval; no Windows, macOS or GPU; AI models are not included.
- binding note: The USD 20 monthly subscription price, or the USD 10 prepaid credit minimum for a disposable screen, is what a reader must pay before any sandbox time is available.
- interface detail: An API, a TypeScript SDK and a hosted MCP server; screen control by pixels or accessibility tree, root and Tailscale SSH, and a live dashboard view
- endpoint: https://api.trykubi.com/v1/
- tooling: a hosted MCP server for Claude Code, Codex and Cursor, a TypeScript SDK and a plain HTTP and JSON API; bring your own model
- composes with: a hosted Linux cloud desktop for computer-use agents, with the browser logins and open apps kept between sessions; it runs on a private VM with its own proxy
- reliability: a persistent screen has no idle timeout and keeps its disk when stopped; a failed proxy leaves the screen with no internet; all traffic is recorded for 30 days
- notes: This is a hosted cloud desktop that a computer-use agent drives, not a general code sandbox: the vendor states explicitly that a screen is not a sandbox and is priced to stay on. The operator's list USD 0.035 per hour matches the vendor's disposable-screen rate.
- evidence note: the vendor's home and pricing pages were read on 2026-11-25; the sign-in methods are from the hosted console's own sign-in JavaScript, and the free-tier statement from the pricing FAQ
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.disk_gib: 50
  - billing_model: monthly subscription for a persistent screen, or by-the-minute prepaid credit for a disposable screen
  - session_cap.restart_required: no
  - session_cap.note: a persistent screen has no idle timeout; a stopped disposable screen is deleted after 7 days
  - free_tier_kind: card-gated one-time credit
  - term: monthly or prepaid credit
  - source_scope: the disposable-screen rate is the one that matches the operator's hourly list price
- evidence:
  - [1] 2026-11-25: a persistent screen is USD 20 a month at the founding price, USD 25 list, and a disposable screen is USD 0.035 an hour by the minute from prepaid credit, USD 0.003 an hour stopped | capture: sha256:0fceb7774aa8dfa28714938c1fa3b25e8ec3c756a52b3c78646ca4001019f354 | quote: Disposable $0.035an hour while running Charged by the minute from prepaid credit. $0.003 an hour stopped.
  - [1] 2026-11-25: each screen has 4 vCPU, 8 GB of memory and a 50 GB disk, and the API, TypeScript SDK and hosted MCP server are included | capture: sha256:0fceb7774aa8dfa28714938c1fa3b25e8ec3c756a52b3c78646ca4001019f354 | quote: 4 vCPU, 8 GB of memory, 50 GB disk, its own virtual machine
  - [1] 2026-11-25: there is no free tier and disposable screens run on prepaid credit from USD 10 | capture: sha256:0fceb7774aa8dfa28714938c1fa3b25e8ec3c756a52b3c78646ca4001019f354 | quote: No. Disposable screens run on prepaid credit from $10, about 285 hours of a running disposable screen.
  - [2] 2026-11-25: the vendor gives USD 5 of credit for disposable screens when a card is added, and states there is no waitlist or approval at sign-up | capture: sha256:9061d76cf38b1c06e4b8eba357612751b4db62c621112932b096bf73cc685ac1 | quote: $5 of credit for disposable screens when you add a card, about 140 hours.
  - [2] 2026-11-25: all screen traffic leaves through the user's own proxy and a failed proxy leaves the screen offline | capture: sha256:9061d76cf38b1c06e4b8eba357612751b4db62c621112932b096bf73cc685ac1 | quote: All of a screen's traffic leaves through your own proxy, not just the browser. If it fails, the screen goes offline instead of using Kubi's network.
  - [3] 2026-11-25: an agent reaches a screen through an MCP connection, a TypeScript SDK quickstart or a plain HTTP and JSON API | capture: sha256:d43cdb53c4877d76acde32ca9cd4bc839116204d5eed43ea45666205adad7563 | quote: | Any language | [API reference](https://docs.trykubi.com/api) | Plain HTTP and JSON, `curl` works |
  - withheld 2026-11-25: the operator's list prices Kubi at USD 0.035 per hour billed per minute, a reported rate about a third party and not a reading of the vendor's own page | capture: sha256:4d220f8008ed2a6126e4b7f8bc4639bd9e625605ec428846fde2bdf593cc5c95 | quote: 27. Kubi → $0.035/h · billed per minute
  - [1] 2026-11-24: a persistent screen is $20 a month at the founding price | capture: sha256:0fceb7774aa8dfa28714938c1fa3b25e8ec3c756a52b3c78646ca4001019f354 | quote: $20a screen a month
  - [1] 2026-11-24: a disposable screen is $0.035 an hour while running | capture: sha256:0fceb7774aa8dfa28714938c1fa3b25e8ec3c756a52b3c78646ca4001019f354 | quote: $0.035an hour while running
  - [1] 2026-11-24: there is no free tier and disposable credit starts at $10 for about 285 running hours | capture: sha256:0fceb7774aa8dfa28714938c1fa3b25e8ec3c756a52b3c78646ca4001019f354 | quote: No. Disposable screens run on prepaid credit from $10, about 285 hours of a running disposable screen.
  - [1] 2026-11-24: each screen has 4 vCPU, 8 GB of memory and a 50 GB disk in its own VM | capture: sha256:0fceb7774aa8dfa28714938c1fa3b25e8ec3c756a52b3c78646ca4001019f354 | quote: 4 vCPU, 8 GB of memory, 50 GB disk, its own virtual machine
  - [2] 2026-11-24: $5 of credit for disposable screens is granted when a card is added, about 140 hours | capture: sha256:9061d76cf38b1c06e4b8eba357612751b4db62c621112932b096bf73cc685ac1 | quote: $5 of credit for disposable screens when you add a card, about 140 hours.
  - [4] 2026-11-24: sign-in uses an emailed link, GitHub, Google or a passkey, and anyone can sign up at once | capture: sha256:2fda537d68f0a149a9c323b3bd581e174bdc97457fe96489eb35df5760457bab | quote: 3.3 You sign in with a link sent to your email, with GitHub or Google, or with a passkey.
  - [4] 2026-11-24: exports and switching, including their data transfer, are free | capture: sha256:2fda537d68f0a149a9c323b3bd581e174bdc97457fe96489eb35df5760457bab | quote: 12.5 Exports and switching are free, including their data transfer, and there are no early termination fees.
  - [5] 2026-11-24: file upload or download is capped at 64 MiB | capture: sha256:7e167c5a64590e1b79ba44a5b27b83bc3b78b83ec6b3444e3ce68d8cae4cd63c | quote: File upload or download | 64 MiB
  - [5] 2026-11-24: requests are limited to 60 a minute per key for each screen, at least 300 | capture: sha256:7e167c5a64590e1b79ba44a5b27b83bc3b78b83ec6b3444e3ce68d8cae4cd63c | quote: Requests per key | 60 a minute for each screen in your organization, at least 300
  - [6] 2026-11-24: a screen makes no inbound connections and ports carry HTTP and WebSocket only | capture: sha256:d9ca4f1ea8ca08812e6be585c9e6930b363a6dffcf6ae25aa89b442ce6ba6dd4 | quote: A screen makes no connections inbound: nothing on the internet can reach it directly.
  - [4] 2026-11-25: the first-party terms name an emailed sign-in link as one sign-in route, so email is a stated sign-up identity | capture: sha256:2fda537d68f0a149a9c323b3bd581e174bdc97457fe96489eb35df5760457bab | quote: 3.3 You sign in with a link sent to your email, with GitHub or Google, or with a passkey.
- sources:
  - [1] https://trykubi.com/pricing
  - [2] https://trykubi.com/
  - [3] https://docs.trykubi.com/
  - [4] https://trykubi.com/legal/terms
  - [5] https://docs.trykubi.com/reference/limits
  - [6] https://docs.trykubi.com/guides/ports
