# Hoppy Network

> hoppy.network | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hoppy/ | JSON https://fshy.ajam.dev/api/v1/entity/hoppy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hoppy Network

- `egress/hoppy` | paid-only | evidence documented | binding volume-quota | category public IPv4 over WireGuard | tier standard
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://hoppy.network/pricing/
- price USD 8 per month | parsed USD 8/mo
- free tier: STANDARD $8/mo: '1 IPv4 Address', '/56 IPv6 Network', '1 TB Monthly data', '100/100 Mbps'. No free plan is listed. | unit: TB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: 'We calculate the limit using the sum of bytes transferred in and bytes transferred out, as reported by the WireGuard tunnel.' 1 TB per month on STANDARD, 3 TB on PLUS.; ingress: tcp+udp | metered: yes | free allowance: 'We calculate the limit using the sum of bytes transferred in and bytes transferred out, as reported by the WireGuard tunnel.' 1 TB per month on STANDARD, 3 TB on PLUS. | source: [2]
- identity: card | detail: a Hoppy account plus a paid plan; the pricing page lists card checkout through Stripe Portal and no free tier | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 TB per month on STANDARD, counted as bytes in plus bytes out [2]
  - per-ip-shaping: 100/100 Mbps on STANDARD; after the quota is exceeded the interface is 'rate-limited to anywhere between 64 kbps and 256 kbps' [1]
  - volume-quota (binding): 1 TB per month on Standard, counted in and out [1]
- binding note: The 100 Mbps rate is 32.4 TB/day, so the quota binds long before the rate.
- interface detail: 'download the configuration file. Import the configuration file into your client and activate the interface.'
- tooling: any WireGuard client (wg-quick, the official apps), the Hoppy dashboard
- composes with: replaces the VPS in the Pangolin/Wiredoor/Wireport chain with a rented address, so it removes the server to patch and keeps the port-opening job
- reliability: exceeding the quota does not cut the tunnel, it shapes it to 64-256 kbps, which keeps SSH and SMTP alive and makes bulk transfer impractical
- notes: The only provider where a standard .conf plus a real public IPv4 plus no port blocking was all stated first-party. It fails the free test, not the technical one: at USD 8/mo for 1 TB it is the cheapest documented route to a public address that carries UDP. metered_on is recorded as unstated because the vocabulary has no token for a bidirectional sum; the vendor sentence is in volume_stated. Yggdrasil traffic on the private relay is not counted toward the cap.
- evidence note: A transfer through a provisioned interface would raise this to measured and would confirm that inbound ports really are open.
- extras:
  - wg_path: native-conf
  - wg_detail: 'Create a New Interface, making sure to select Generate Client Keypair. Click Modify on the provisioned interface, then download the configuration file. Import the configuration file into your client.' The vendor then states: 'Your device is now using the Hoppy Public IP address for all incoming and outgoing traffic!'
  - ingress: tcp+udp
  - volume_tib_month: 0.909
  - volume_stated: 'We calculate the limit using the sum of bytes transferred in and bytes transferred out, as reported by the WireGuard tunnel.' 1 TB per month on STANDARD, 3 TB on PLUS.
  - bytes_transit: yes
  - transit_note: Hoppy terminates the WireGuard tunnel on its own address, so every byte crosses its network
- evidence:
  - [2] 2026-10-23: STANDARD $8/mo with 1 TB monthly data and 100/100 Mbps; PLUS $16/mo with 3 TB; no free plan on the page
  - [3] 2026-10-23: a downloadable WireGuard configuration file and 'Your device is now using the Hoppy Public IP address for all incoming and outgoing traffic!'
  - [1] 2026-10-23: 'Do you block ports on the tunnels? Nope'; over-limit shaping to 64-256 kbps; the limit counts bytes in plus bytes out
- sources:
  - [1] https://hoppy.network/docs/frequently-asked-questions/
  - [2] https://hoppy.network/pricing/
  - [3] https://hoppy.network/docs/wireguard-config/quickstart.html
