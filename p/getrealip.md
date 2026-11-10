# Get Real IP

> getrealip.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getrealip/ | JSON https://fshy.ajam.dev/api/v1/entity/getrealip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Get Real IP

- `egress/get-real-ip` | trial-only | evidence documented | binding none | category dedicated IPv4 over WireGuard | tier tunnel
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://getrealip.net/pricing/
- price USD 8 per month for one IPv4 and an IPv6 range, unlimited data; 7 days free | parsed USD 8/mo
- free tier: "Try free for 7 days - no charge until your trial ends", on a "Tunnel $8/mo" plan that "Includes 1 static IP" and "First 7 days free". | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: "Unlimited data" appears in the list of what is included with every tunnel. No fair-use figure accompanies it.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: The trial starts at account.getrealip.net with a signup form and "no charge until your trial ends", which implies a card is taken at signup; the form itself was not read. | country: None
- interface: cli
- limits:
  - volume-quota: unlimited data, no fair-use figure stated [1]
- binding note: Nothing in the published terms fails at 1 TiB/month: data is unlimited, every port and protocol is open, and the plan is one address at USD 8. The unstated fair-use policy behind "unlimited" is the only risk, and it is not documented.
- interface detail: Config file, QR code and a dashboard for IP and reverse DNS management.
- tooling: wg-quick; config plus QR code for phones
- composes with: Incoming-only mode leaves the local outbound path untouched, so it composes with a free-tier VM that already has outbound.
- reliability: No throttle or ban policy published; the absence of a fair-use clause is undocumented rather than guaranteed.
- notes: Provides dedicated IPv4 addresses with unmetered bandwidth at USD 8 monthly, with no port blocking.
- evidence note: Price, the unlimited-data claim, the config file and the port policy are first-party.
- extras:
  - wg_path: native-conf
  - wg_detail: "WireGuard config + QR code" is a listed feature of the USD 8 plan, and "Full tunnel or incoming only" is offered: "use your static IP for all traffic, or just receive inbound while keeping your normal internet for outbound (requires OS routing policy support)".
  - ingress: tcp+udp
  - volume_stated: "Unlimited data" appears in the list of what is included with every tunnel. No fair-use figure accompanies it.
  - bytes_transit: yes
  - transit_note: The vendor routes the address to the tunnel from its own network in six regions.
- evidence:
  - [1] 2026-10-23: USD 8/mo for 1 static IPv4 and an IPv6 range, unlimited data, any protocol and any port, WireGuard config with QR code, 7 days free; additional IP USD 4/mo
  - [2] 2026-10-23: "Any protocol, any port - not just HTTP"; "Full tunnel or incoming only"; USD 8 first IP, USD 4 additional; 7-day free trial
- sources:
  - [1] https://getrealip.net/pricing/
  - [2] https://getrealip.net/
