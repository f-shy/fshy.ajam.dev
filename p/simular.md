# box by Simular

> simular.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/simular/ | JSON https://fshy.ajam.dev/api/v1/entity/simular.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## box by Simular

- `compute/box-by-simular` | trial-only | evidence documented | binding volume-quota | category sandbox | tier Free / S / M
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:55:06.337Z (live) | stale on 2026-12-26
- url https://box.simular.ai/
- free tier: Free: 5,000 credits to start, valid 90 days, on a box of 4 vCPU / 8 GB; at 200 credits an hour that is 25 hours of awake time. S at $19 a month adds 5,000 credits a month, M at $39 a month adds 10,000. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1]
- per-object cap: not applicable: the unit is one cloud Ubuntu desktop with a persistent shell, not a stored object
- retention: A box asleep 14 consecutive days is deleted with its files and saves, 30 days if the account has paid for box or Sai, and never while it has an S or M plan; any wake resets the count. | days: 14 | source: [2]
- egress: A residential IP add-on costs 1,000 credits per 100 MB on paid plans; no general egress allowance or per-GB rate for ordinary traffic is published. | metered: yes | source: [1]
- identity: email | detail: Sign-in is through a Simular account with Google or GitHub OAuth; the MCP connection opens a browser page where the person approves which boxes it may use and for how long. A personal bearer key from box.simular.ai/access works for clients that cannot sign in. No card is asked for on the free tier.
- interface: rest, browser
- limits:
  - volume-quota (binding): 5,000 free credits once, valid 90 days; 200 credits an hour for a 4 vCPU / 8 GB awake box, so 25 hours free [1]
  - retention-clamped: a box asleep 14 consecutive days is deleted with its files and saves, 30 days if the account has ever paid, never on an S or M plan [2]
  - request-rate: one box per account; extra boxes cost 200 credits an hour each while awake [1]
- limits note: One cloud Linux desktop per account. The box sleeps when idle except on the M plan; a plan's own box is not charged by the hour.
- binding note: The 5,000 credits expire after 90 days and are the first limit reached; at 200 credits an hour they buy 25 awake hours before the $19 or $39 plan or a top-up is needed.
- interface detail: One hosted MCP server at https://mcp.box.simular.ai/mcp (Streamable HTTP, OAuth sign-in), plus a live screen at box.simular.ai/box and a personal key for clients that cannot sign in.
- endpoint: part of interface detail
- tooling: Add the remote MCP URL to Claude, ChatGPT, Gemini, Claude Code, Codex, Cursor, OpenCode or VS Code, or run npx @simular-ai/box@1.2.2 connect on the user's own computer.
- composes with: A 4 vCPU / 8 GB box at 200 credits an hour is $0.20 an hour, or $0.10 an hour at half duty; its persistent desktop keeps browser logins between agent sessions and hands files to other records.
- reliability: System images may be reconfigured, so installed packages can need reinstalling; an idle box is deleted after 14 days of sleep and a box's small model calls are billed separately from its awake time.
- notes: The hosted computer is a persistent Ubuntu desktop that sleeps when idle and wakes on connect; 5,000 credits are $5 and buy 25 awake hours at the published 200 credits an hour. The $19 S and $39 M plans include a box and monthly credits; extra boxes are metered. A separate self-hosted CLI configures the user's own AI apps and does not supply the box, so it is listed after this hosted offer.
- evidence note: Prices, free credits, sleep deletion, the MCP sign-in and the credit rate are quoted from the vendor's own home page, docs and terms read on 2026-11-25.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.note: one hosted Ubuntu desktop per account with Chrome, a shell and 4 vCPU / 8 GB
  - billing_model: credits per second while awake, at 200 credits an hour for the standard box; S and M plans are monthly
  - free_tier_kind: one-time-credit
  - term: 5,000 credits valid 90 days; top-ups valid 12 months
  - price_arithmetic: 1,000 credits = $1, so 200 credits an hour is $0.20 an hour and 5,000 credits is 25 hours or $5
  - derived: 200 credits/hour / 1000 credits per dollar = $0.20 per hour; $0.20 x 0.5 = $0.10 per hour at half duty; 5000 / 200 = 25 hours
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: a residential IP add-on is 1,000 credits per 100 MB; no general egress allowance is stated
  - session_cap.restart_required: no
  - session_cap.note: the box sleeps when idle and wakes on connection; 14 consecutive days asleep deletes it unless the account has paid or holds an S or M plan
- evidence:
  - [1] 2026-11-25: one credit is $0.001 and a 4 vCPU / 8 GB box costs 200 credits an hour while awake | capture: sha256:30ab6c907b4e48440310a9a5593e7ca5c6daac225ba33a977ccc853a0e9cd78d | quote: 1,000 credits = $1
  - [1] 2026-11-25: an extra box costs 200 credits an hour at 4 vCPU / 8 GB while awake | capture: sha256:30ab6c907b4e48440310a9a5593e7ca5c6daac225ba33a977ccc853a0e9cd78d | quote: 200 credits an hour (4 vCPU / 8 GB), only while it's awake.
  - [1] 2026-11-25: the free tier gives 5,000 credits to start, valid 90 days, on a 4 vCPU / 8 GB box | capture: sha256:30ab6c907b4e48440310a9a5593e7ca5c6daac225ba33a977ccc853a0e9cd78d | quote: 5,000 credits to start
  - [1] 2026-11-25: the free credits are valid 90 days and the box is 4 vCPU / 8 GB | capture: sha256:30ab6c907b4e48440310a9a5593e7ca5c6daac225ba33a977ccc853a0e9cd78d | quote: Valid 90 days
  - [1] 2026-11-25: a residential IP add-on costs 1,000 credits per 100 MB | capture: sha256:30ab6c907b4e48440310a9a5593e7ca5c6daac225ba33a977ccc853a0e9cd78d | quote: 1,000 credits per 100 MB.
  - [2] 2026-11-25: an idle box is deleted after 14 days of sleep, 30 days if the account has paid, and never on an S or M plan | capture: sha256:c20d34c44919e5520c7a2f9f5d02de3cd5d0af87b6b390fe87fa5725f7174e3e | quote: A box asleep 14 days in a row is deleted with its files and saves (30 days if the account has ever paid for box or Sai; never while it has an S or M plan); any wake resets the count.
  - [2] 2026-11-25: the first MCP connection signs in with a Simular account over OAuth and approves box access in a browser | capture: sha256:2591404e858cd03ed74813fe1a672a842337fde6c604f93136a173095457c323 | quote: You sign in with your Simular account the first time your AI connects (MCP authorization, OAuth 2.0): your app opens a browser page where you approve which boxes it may use and for how long.
  - [2] 2026-11-25: a bearer key is available for clients that cannot sign in | capture: sha256:2591404e858cd03ed74813fe1a672a842337fde6c604f93136a173095457c323 | quote: For an app that can't sign in and can only send a fixed header, create a personal key at https://box.simular.ai/access
  - [3] 2026-11-25: the hosted service is a cloud computer with remote desktop, shell and MCP connections, and system images may be reconfigured | capture: sha256:fa20134de198b0caad89e2dc781d8857689dda4192c21f3010df7ba6212c587f | quote: Box System Updates. Simular may update, replace, or reconfigure a Box’s system image, operating system, software, or other components
  - [1] 2026-11-24: box free tier is 5,000 credits once, valid 90 days, on a 4 vCPU / 8 GB box; credits are $1 per 1,000, box time is 200 credits an hour and residential IP on paid plans is 10,000 credits a GB | capture: sha256:1fae5aeaa4da8ac4ce614917366cb7696b1ab2b4519448dc4ec5569f43da7ad7 | quote: 1,000 credits = $1. box credits pay for box time by size, per second while the box is awake (4 vCPU / 8 GB: 200 credits an hour), residential IP on paid plans (10,000 credits a GB) and box's own model calls. Free: 5,000 credits once, valid 90 days, on the Free box (4 vCPU / 8 GB).
  - [1] 2026-11-24: a box asleep 14 days in a row is deleted with its files and saves; any wake resets the count | capture: sha256:1fae5aeaa4da8ac4ce614917366cb7696b1ab2b4519448dc4ec5569f43da7ad7 | quote: A box asleep 14 days in a row is deleted with its files and saves (30 days if the account has ever paid for box or Sai; never while it has an S or M plan); any wake resets the count.
  - [4] 2026-11-24: there is no agent self-registration; credentials come from a person with a Simular account | capture: sha256:8b64eea54697af739e2e4442333ccca3515fd2b22e7e138b3a2670a9c0744b71 | quote: box has no agent self-registration. There is no anonymous, email or identity-assertion (ID-JAG) registration. Every credential comes from a person with a Simular account, in one of two ways.
  - [2] 2026-11-24: one remote MCP server at https://mcp.box.simular.ai/mcp with OAuth sign-in or a personal key | capture: sha256:2591404e858cd03ed74813fe1a672a842337fde6c604f93136a173095457c323 | quote: box is one MCP server, named `box`: ```text https://mcp.box.simular.ai/mcp ```
  - [5] 2026-11-24: the remote is Streamable HTTP and the optional Authorization header carries a personal key for clients that cannot use OAuth | capture: sha256:ce443c1a7d4533000e302daa409bee056f72f53a29856093a1b297351f01db21 | quote: "type": "streamable-http", "url": "https://mcp.box.simular.ai/mcp",
  - [6] 2026-11-24: sign-in offers Google, Apple and GitHub accounts and says new accounts start on the free plan | capture: sha256:2c48d36858e75d291cf2cdbbd7e67f5a6b808d205b32641a3b6c783c5e89497b | quote: const Vj="Sign in to box",qc=["Google",Af&&"Apple",tu&&"GitHub"].filter(e=>!!e),Bj=`Use your ${qc.length>1?`${qc.slice(0,-1).join(", ")} or ${qc.at(-1)}`:qc[0]} account. New accounts start on the free plan.`;
- sources:
  - [1] https://box.simular.ai/
  - [2] https://box.simular.ai/docs/mcp.md
  - [3] https://box.simular.ai/terms
  - [4] https://box.simular.ai/auth.md
  - [5] https://box.simular.ai/.well-known/mcp/server-card.json
  - [6] https://box.simular.ai/sign-in
