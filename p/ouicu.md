# ouicu

> ouicu.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ouicu/ | JSON https://fshy.ajam.dev/api/v1/entity/ouicu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ouicu

- `egress/ouicu` | fails-quota | evidence inferred | binding volume-quota | category tunnel (hosted, HTTP and WebSocket only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://ouicu.com/docs/plans
- price USD 0
- free tier: The Free plan costs nothing and needs no card: 1 live share at a time with a random name, shares of up to 2 hours, 1 uploaded site kept 7 days, and 1 GB of data a month. | unit: GB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: 1 GB of data a month; ingress: http-only | metered: yes | free allowance: 1 GB of data a month | source: [2]
- identity: email | detail: an Account page exists and ouicu whoami is documented, and the free plan is stated to need no card; the signup mechanism itself was not observed, so email is inferred from the absence of any phone or card requirement | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 GB of data a month [2]
- binding note: 1 GB a month is short of 1 TiB by about three orders of magnitude, so the volume quota fails first; the 2-hour session cap is the second failure and has no vocabulary kind
- interface detail: run ouicu share 3000 beside your app
- tooling: the ouicu CLI, plus an MCP server and SDK under MIT; the CLI and the service are closed
- composes with: nothing to chain: HTTP-only and 1 GB a month, so it cannot carry UDP and cannot reach the volume bar
- reliability: the page states a live share stops while the laptop sleeps or is off and returns at the same address on reconnect; no ban or throttle is documented
- notes: Registry comparison tool for tunneling services. Individual free sessions are subject to a 2-hour duration cap.
- evidence note: the quota and the session length are documented on the vendor's own plans page; registration is inferred from an Account page and a whoami command, without an observed signup, so the record sits one rung below documented
- extras:
  - wg_path: none
  - wg_detail: its own comparison table states the protocol as HTTP and WebSockets, web pages only; no WireGuard endpoint or raw TCP/UDP path is offered
  - ingress: http-only
  - volume_tib_month: 0.00091
  - volume_stated: 1 GB of data a month
  - bytes_transit: yes
  - transit_note: ouicu's own relay carries the bytes
- evidence:
  - [1] 2026-10-23: free plan needs no card, 1 live share at a time, 2-hour shares, 1 GB of data a month
  - [2] 2026-10-23: per-plan table: 2-hour share limit on Free, no limit on Hobby and Pro, and an Account page
  - [3] 2026-10-23: its own table lists protocols as HTTP and WebSockets, web pages only
- sources:
  - [1] https://ouicu.com/
  - [2] https://ouicu.com/docs/plans
  - [3] https://ouicu.com/compare
