# BoxCompute

> boxcompute.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boxcompute/ | JSON https://fshy.ajam.dev/api/v1/entity/boxcompute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BoxCompute

- `compute/boxcompute` | trial-only | evidence documented | binding volume-quota | category sandbox | tier Free one-time $5 compute credit (Small and Large VMs)
- identity a placeholder: card and phone unknown | verified 2026-11-25T02:12:34.813Z (live) | stale on 2026-12-26
- url https://boxcompute.ai/pricing/
- free tier: $5 compute credit, valid for 14 days, added when you sign up, one per person, cannot pay the Starter subscription fee; no credit card required, with the BoxCompute agent's daily AI allowance and two VMs and two chats at once | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: A one-time credit, not a recurring allowance: 'Credit is added when you sign up. It doesn't renew.' At about $0.05/hour for a Small VM the credit is roughly 100 Small-VM hours, and at about $0.15/hour for a Large VM roughly 33 Large-VM hours, while the VM runs.
- per-object cap: files kept in Assets stay after a VM is deleted, up to 5 GiB each; no storage limit on any plan | bytes: 5368709120 | source: [1] | note: The cap is per file in Assets, not a total account cap.
- retention: a VM keeps its workspace files when it stops; a VM stops after 30 minutes idle and its files stay; files saved to Assets stay after a VM is deleted, with no storage limit on any plan | source: [1]
- egress: not published as a per-GB price: a VM's running time is billed by the second, including idle time; web apps get preview links and database clients need TCP access that depends on the deployment. No outbound byte allowance or price per GB is stated on the pricing page. | metered: no | source: [1]
- identity: email | detail: unverified: the sign-up link goes to https://app.boxcompute.ai/signup, which answered with a login wall on 2026-11-25; the page shell contains no identity fields. The pricing page states 'No credit card required' for the free credit. Whether registration asks for an email, a social login or a card is unverified;
- interface: rest, cli, chat
- limits:
  - volume-quota (binding): $5 compute credit valid 14 days, one per person; two concurrent VMs and two chats on free, three with pay-as-you-go credit [1]
  - retention-clamped: a VM stops after 30 minutes idle and keeps its files; running time bills per second with a one-minute minimum, stopped VMs cost nothing [1]
  - per-object-cap: up to 5 GiB per file in Assets [1]
- limits note: VM sizes: Small 0.5 vCPU/1 GiB RAM about $0.05/hour; Large 1.5 vCPU/3 GiB RAM about $0.15/hour; XL 4 vCPU/8 GiB and XXL 4-8 vCPU/16 GiB about $0.40 or $0.80/hour on Starter. Hosted in Cyberjaya, Malaysia; VM sandboxes are in beta.
- binding note: The $5 credit is one-time and expires after 14 days, so it runs out first; the 30-minute idle stop keeps an unattended VM from draining it.
- interface detail: MCP server at https://mcp.boxcompute.ai/mcp for Claude, Claude Code, Codex and Cursor; an HTTP API and SDKs; a CLI with a coding-agent skill; and a browser chat agent with live preview links. VMs are full Ubuntu/Linux machines with their own kernel.
- endpoint: part of interface detail
- tooling: MCP client, HTTP API, SDKs and CLI; the browser chat agent runs the VM in the cloud, so the user needs only a browser. No rclone backend exists for its Assets store; that is a tooling note, not a verdict.
- composes with: A one-time $5 credit buys a few tens of hours of Small or Large Linux VMs for agent work; the agent connects through MCP using the user's own model key, so the BoxCompute credit pays only VM time, and files that must outlive a VM go to Assets before deletion.
- reliability: A VM stops after 30 minutes idle and keeps its files; VM sandboxes are in beta, and a free credit is valid 14 days and does not renew.
- notes: Hosted Linux VM sandboxes in Malaysia. A one-time $5 credit, no card required, valid 14 days, buys roughly 100 Small-VM hours at $0.05/hour or 33 Large-VM hours at $0.15/hour while the VM runs. Starter at $16.99/month includes $40 of monthly compute credit, about 800 Small or 270 Large VM hours. No recurring free tier is published.
- evidence note: Prices, VM sizes, credit terms, idle stop, file cap and sign-up no-card statement are quoted from the first-party boxcompute.ai pricing page read on 2026-11-25; the sign-up form itself is behind a login wall and its identity gate is unverified.
- extras:
  - shape.vcpu: 0.5
  - shape.ram_gib: 1
  - shape.note: Small 0.5 vCPU/1 GiB about $0.05/hour, Large 1.5 vCPU/3 GiB about $0.15/hour, XL 4 vCPU/8 GiB about $0.40/hour, XXL 4-8 vCPU/16 GiB about $0.80/hour
  - billing_model: one-time credit or monthly plan, VM time billed per second with a one-minute minimum
  - free_tier_kind: one-time credit
  - term: 14-day validity on the free credit
  - price_arithmetic: $5 / $0.05 per hour = about 100 Small-VM hours; $5 / $0.15 per hour = about 33 Large-VM hours
  - status: hosted, VM sandboxes in beta
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: web apps get preview links; database clients need TCP access depending on deployment
  - session_cap.idle_reap_s: 1800
  - session_cap.restart_required: no
  - session_cap.note: a VM stops after 30 minutes idle and keeps its files; two concurrent VMs on free, three on pay-as-you-go
- evidence:
  - [1] 2026-11-25: the free plan is a one-time $5 compute credit valid 14 days with no credit card required | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: $5 compute credit, valid for 14 days
  - [1] 2026-11-25: no card is required for the free plan | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: No credit card required
  - [1] 2026-11-25: the free credit is one-time and does not renew | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: Credit is added when you sign up. It doesn’t renew.
  - [1] 2026-11-25: the Small and Large VMs are about $0.05 and $0.15 an hour, billed per second | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: About $0.05 / hour
  - [1] 2026-11-25: a VM stops after 30 minutes idle and keeps its files; stopped VMs cost nothing | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: Your agent’s VM stops after 30 minutes idle and keeps its files, so a forgotten VM doesn’t drain credit.
  - [1] 2026-11-25: Assets keeps files after VM deletion, with up to 5 GiB per file | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: Assets keeps them after a VM is deleted, with no storage limit on any plan and files up to 5 GiB each.
  - [1] 2026-11-25: access is through an MCP server, HTTP API, SDKs and a CLI, with a browser agent | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: Add https://mcp.boxcompute.ai/mcp to Claude, Claude Code, Codex, Cursor or another MCP client and sign in, or use an API key.
  - [1] 2026-11-25: the VMs run in Cyberjaya, Malaysia | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: In Southeast Asia. Our first region, Cyberjaya in Malaysia, is online now
  - [1] 2026-11-24: the free plan gives $5 compute credit valid 14 days with no credit card required and runs two VMs at once | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: - $5 compute credit, valid for 14 days - The BoxCompute agent, with a daily AI allowance - Connect your own agent over MCP - Run two VMs and two chats at once - No credit card required
  - [1] 2026-11-24: VMs bill by the second with a one-minute minimum, about $0.05 an hour for Small and $0.15 for Large, and stopped VMs cost nothing | capture: sha256:b82bf312653dd9b1f1e0fa3a8896f0da0add090881e8ad0f2a51c0dfa2aea65a | quote: A running VM uses credit by the second, including idle time, until it stops: about $0.05 an hour for Small and $0.15 for Large, with a one-minute minimum. Stopped VMs cost nothing.
  - [2] 2026-11-24: VMs have outbound public internet unless turned off, no direct inbound connection, one port at a time via preview links, and outbound SMTP port 25 blocked | capture: sha256:698e91e35082e473d6ea7715e0d8a67dc59e5241ec341e94249a2a0edbe1520e | quote: - Public internet only. New VMs have outbound internet unless you turn it off, and it reaches the public internet only: private, carrier-grade NAT and link-local addresses are blocked, so a VM cannot reach our internal network or other customers' VMs. Nothing on the internet connects to a VM directly; a preview link opens one port at a time.
  - [3] 2026-11-24: sign up, confirm your email and create an API key; the $5 credit needs no card | capture: sha256:e356788f0bbc6f27491cbbd024b882fb9d36cf29358f0f9624b602df40420755 | quote: Eligible new customers receive $5 in free compute credit, valid for 14 days. No card required.
  - [4] 2026-11-24: the sign-up screen asks for an email and uses a Turnstile verification check, with no card or phone field at that step | capture: sha256:5de80a56ee06ac94ee8e9fa351ad514f1f142dc4c41cd890dd70c209feb4b6da | quote: htmlFor:`signup-email`,children:`Email`
  - [5] 2026-11-24: one free account per person and free accounts have limits on daily AI allowance and how many chats and VMs run at once | capture: sha256:24f6c81b587166c3bab124792a8626de7faf0752ce17d0e3704e734fa4858a07 | quote: - One free account per person. Don’t create extra accounts to get more free credit or to get around limits.
- sources:
  - [1] https://boxcompute.ai/pricing/
  - [2] https://boxcompute.ai/security/
  - [3] https://boxcompute.ai/docs/quickstart/
  - [4] https://app.boxcompute.ai/assets/signup-hJ_xj5kr.js
  - [5] https://boxcompute.ai/terms/
