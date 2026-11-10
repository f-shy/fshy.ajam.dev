# GetAStatic

> getastatic.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getastatic/ | JSON https://fshy.ajam.dev/api/v1/entity/getastatic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GetAStatic

- `egress/getastatic` | paid-only | evidence documented | binding volume-quota | category static IPv4 with open ports (paid)
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://getastatic.com/pricing
- free tier: none; USD 2/month for 100 GB and 20 Mbit/s on a dedicated US IPv4 | unit: GB | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a port and an address
- retention: not applicable | source: [1]
- egress: 100 GB included and 20 Mbit/s on the USD 2 tier | metered: yes | free allowance: 100 GB/month on the USD 2 tier | source: [1]
- identity: card | detail: a card or crypto at signup
- interface: ssh
- limits:
  - per-ip-shaping: 20 Mbit/s [1]
- limits note: the allowance is a byte volume over a period, which none of the six kinds names; the number is in egress.free_allowance and binding names per-ip-shaping as the nearest kind
- binding note: the monthly byte allowance in egress.free_allowance is what runs out, and no kind in the six-value vocabulary names a byte volume over a period counted per account. per-ip-shaping is the closest, because it is the only kind that bounds a volume, and its subject here is the account rather than the caller's address
- interface detail: a forwarded port on a dedicated IPv4
- tooling: OpenSSH
- composes with: the paid answer to a static address with open ports, which no free provider offers; it composes with an origin and stops at its quota.
- reliability: the only route found to a real static IPv4 with open ports
- notes: 2026-10-23: this is a WireGuard VPN with open ports, not an SSH tunnel. 'Every plan is a WireGuard VPN with your own dedicated static public IPv4 in the US'; 'Connect your device with WireGuard and open the TCP or UDP ports you need from the dashboard'. The plan table is the fact the record is missing: Plus USD 2/mo gives 5 ports, 100 GB and 20 Mbps; Pro USD 4/mo gives unlimited ports, 1 TB and 100 Mbps; Ultra USD 10/mo gives 5 TB. So the record's 100 GB is the entry tier, not the ceiling, and UDP is available on every tier.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the port forwards to the origin and the bytes cross GetAStatic's network
- evidence:
  - [1] 2026-10-22: USD 2/month for a dedicated US IPv4 with 100 GB and 20 Mbit/s
  - [1] 2026-10-23: 'Every plan is a WireGuard VPN with your own dedicated static public IPv4 in the US, not shared with other users'; Plus $2/mo 5 ports 100 GB, Pro $4/mo unlimited ports 1 TB, Ultra $10/mo 5 TB
  - [2] 2026-10-23: 'Connect your device with WireGuard and open the TCP or UDP ports you need from the dashboard'
- sources:
  - [1] https://getastatic.com/pricing
  - [2] https://getastatic.com/wireguard-port-forwarding-without-vps
