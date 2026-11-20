# Proxlane

> proxlane.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxlane/ | JSON https://fshy.ajam.dev/api/v1/entity/proxlane.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Proxlane

- `egress/proxlane` | fails-egress | evidence documented | binding write-gated | category developer tunnel (HTTP, TCP, UDP) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://proxlane.com/
- price CNY 0 free; Plus CNY 390/month
- free tier: Free: Active tunnels 1, Connected devices 3, Protocols HTTP / TCP, Monthly transfer 5 GB, Fixed TCP ports 0, Fixed UDP ports 0, UDP Not included. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 GB monthly transfer on Free, 50 GB on Plus at CNY 390 per month, 200 GB on Pro at CNY 980 per month.; ingress: tcp | metered: yes | free allowance: 5 GB monthly transfer on Free, 50 GB on Plus at CNY 390 per month, 200 GB on Pro at CNY 980 per month. | source: [1]
- identity: email | detail: An account plus a device approval: 'proxlane login' and 'approve this device with proxlane login'. | country: None
- interface: cli, rest
- limits:
  - volume-quota: 5 GB per month on Free [1]
  - write-gated (binding): UDP is 'Not included' on Free and 'Fixed UDP ports' is 0; Plus is required [1]
- binding note: At 1 TiB/month the byte allowance is irrelevant because the free tier carries no UDP at all: the plan is what fails first, and the earliest plan with one fixed UDP port is Plus.
- interface detail: 'The CLI supports Windows and Linux; Launcher is for Windows.', plus automation tokens on the pricing table
- tooling: Proxlane CLI and a Windows Launcher
- composes with: The CLI runs on Linux, so a free VM can host the origin; the UDP port still needs Plus.
- reliability: Free tier is one active tunnel and one device-attached agent; the public UDP port on Plus is a fixed port, one per account.
- notes: Chinese tunneling provider. Free plan includes 5 GB of monthly bandwidth. Dedicated persistent UDP ports require the paid Plus tier.
- evidence note: The free plan's protocol list and the vendor's own Bedrock answer both state the gate, so the verdict is settled; only a paid account would show the port behaviour.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard, and the free tier has no UDP endpoint to put one behind.
  - ingress: tcp
  - volume_tib_month: 0.0045
  - volume_stated: 5 GB monthly transfer on Free, 50 GB on Plus at CNY 390 per month, 200 GB on Pro at CNY 980 per month.
  - bytes_transit: yes
  - transit_note: Proxlane's relay carries the bytes and rewrites the port.
- evidence:
  - [1] 2026-10-23: Free plan rows: 'Protocols HTTP / TCP', 'Fixed UDP ports 0', 'UDP Not included', 'Monthly transfer 5 GB'; Plus lists 'Protocols HTTP / TCP / UDP', 'Fixed UDP ports 1', 'Monthly transfer 50 GB'
  - [2] 2026-10-23: 'UDP forwarding and public port allocation are enabled on Plus and Pro. Free can publish HTTP and TCP within its active-tunnel limit but cannot start a Bedrock UDP profile.'
  - [2] 2026-10-23: 'The public port may not be the same as local port 19132.', so even a paid plan hands out a rewritten port on a shared edge
- sources:
  - [1] https://proxlane.com/
  - [2] https://proxlane.com/guides/minecraft-bedrock-server
