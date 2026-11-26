# GetAStatic

> getastatic.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getastatic/ | JSON https://fshy.ajam.dev/api/v1/entity/getastatic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GetAStatic

- `egress/getastatic` | paid-only | evidence documented | binding volume-quota | category static IPv4 with open ports (paid)
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T15:23:42.069Z (live) | stale on 2026-12-26
- url https://getastatic.com/pricing
- free tier: none; USD 4/month for 1 TB and 50 Mbps on a dedicated US IPv4 (Plus plan) | unit: TB | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a port and an address
- retention: not applicable | source: [1]
- egress: 1 TB monthly bandwidth and 50 Mbps on the USD 4 Plus plan | metered: yes | free allowance: 1 TB/month on the USD 4 Plus plan | source: [1]
- identity: card | detail: a card or crypto at signup
- interface: cli
- limits:
  - volume-quota (binding): 1 TB monthly bandwidth on Plus (2 TB on Pro, 5 TB on Ultra, unlimited on the $15/mo Unlimited plan) [1]
  - per-ip-shaping: 50 Mbps on Plus (100 Mbps Pro, 1 Gbps Ultra) [1]
- limits note: The allowance is the volume-quota row; the rate is the per-ip-shaping row.
- binding note: The monthly bandwidth allowance (1 TB on the Plus plan) is what runs out first; the 50 Mbps rate caps throughput at about 16 TB a month, above it.
- interface detail: a forwarded port on a dedicated IPv4
- tooling: any WireGuard client, or AmneziaWG for networks that block WireGuard
- composes with: the paid answer to a static address with open ports, which no free provider offers; it composes with an origin and stops at its quota.
- reliability: the only route found to a real static IPv4 with open ports
- notes: 2026-10-23: this is a WireGuard VPN with open ports, not an SSH tunnel. 'Every plan is a WireGuard VPN with your own dedicated static public IPv4 in the US'; 'Connect your device with WireGuard and open the TCP or UDP ports you need from the dashboard'. The plan table is the fact the record is missing: Plus USD 2/mo gives 5 ports, 100 GB and 20 Mbps; Pro USD 4/mo gives unlimited ports, 1 TB and 100 Mbps; Ultra USD 10/mo gives 5 TB. So the record's 100 GB is the entry tier, not the ceiling, and UDP is available on every tier.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the port forwards to the origin and the bytes cross GetAStatic's network
- evidence:
  - [2] 2026-10-23: 'Connect your device with WireGuard and open the TCP or UDP ports you need from the dashboard'
  - [1] 2026-11-25: the entry plan Plus costs $4/mo with 5 open ports, 50 Mbps and 1 TB bandwidth | capture: sha256:a3d5e6fa32333a19c68807fc6ed2fe1fcf97819e398d7aeed0987431fb5b36f3 | quote: | Plus | $4/mo | $36/yr | 1 | 5 | 50 Mbps | 1 TB |
  - [1] 2026-11-25: the service is a WireGuard VPN, not an SSH tunnel | capture: sha256:a3d5e6fa32333a19c68807fc6ed2fe1fcf97819e398d7aeed0987431fb5b36f3 | quote: Every plan is a WireGuard VPN with your own dedicated static public IPv4 in the US, not shared with other users.
  - [1] 2026-11-25: WireGuard and AmneziaWG are a user protocols on every plan | capture: sha256:a3d5e6fa32333a19c68807fc6ed2fe1fcf97819e398d7aeed0987431fb5b36f3 | quote: AmneziaWG on every plan, for networks that block WireGuard.
  - [1] 2026-11-25: payment is by card or cryptocurrency | capture: sha256:a3d5e6fa32333a19c68807fc6ed2fe1fcf97819e398d7aeed0987431fb5b36f3 | quote: Pay by card through Stripe, or with cryptocurrency: Monero, Litecoin, Bitcoin Cash, Tether, Polygon, Toncoin, Bitcoin, Ethereum.
- sources:
  - [1] https://getastatic.com/pricing
  - [2] https://getastatic.com/wireguard-port-forwarding-without-vps
