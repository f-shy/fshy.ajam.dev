# 21tunnel

> 21tunnel.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/21tunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/21tunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 21tunnel

- `egress/21tunnel` | dead | evidence measured | binding per-ip-shaping | category udp port forward plus relay WireGuard (hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-12-23
- url https://21tunnel.com/pricing/
- price USD 0
- free tier: Everything, $0 forever: Unlimited concurrent tunnels, Unlimited bandwidth and requests, Private VPN over WireGuard, No card, no trial, no expiry | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unlimited bandwidth and requests, with 'Bandwidth is fair-use guidance, not a meter - we don't throttle or bill per-GB.'; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'mytunnel login' opens a browser and saves a 90-day token; signup is at login.21tunnel.com, which does not resolve (see notes) | country: None
- interface: cli, rest
- limits:
  - per-ip-shaping (binding): fair-use guidance only, no meter and no number [1]
- binding note: As published, nothing binds: unlimited bandwidth, 60-second per-source idle window that matches WireGuard keepalive. That is the published figure. The service is not reachable, which is a stronger failure than any constraint.
- interface detail: mytunnel udp 51820 --public-port 31099, mytunnel wg up, and a REST API at login.21tunnel.com/api
- tooling: mytunnel CLI, systemd unit, REST API
- composes with: Provides a WireGuard endpoint with a reserved UDP port, composable with an external virtual machine.
- reliability: the documented relay and dashboard hostnames do not exist in DNS as of 2026-10-23; the marketing site is a static Cloudflare page
- notes: The best-designed free WireGuard ingress and the only provider that ships the .conf, the reserved UDP port and a WireGuard recipe together. It is not running. The wildcard caveat that applies to playit (a bare subdomain legitimately NXDOMAIN while a wildcard serves) does not apply here because login.21tunnel.com is a named host, not a wildcard member.
- evidence note: Service status is measured: agent.21tunnel.com and login.21tunnel.com both returned DNS status 3 (NXDOMAIN) for A and AAAA from Cloudflare DNS-over-HTTPS on 2026-10-23, while 21tunnel.com resolved on the same zone.
- extras:
  - wg_path: registration-api
  - wg_detail: the vendor documents the full path: '21tunnel reserves a public UDP endpoint and relays datagrams to it', clients get a .conf with 'Endpoint = agent.21tunnel.com:31099', and 'mytunnel udp 51820 --public-port 31099' is the exact relay command; 'Free on all plans.' https://21tunnel.com/docs/private-vpn/
  - ingress: udp
  - volume_stated: Unlimited bandwidth and requests, with 'Bandwidth is fair-use guidance, not a meter - we don't throttle or bill per-GB.'
  - bytes_transit: yes
  - transit_note: the relay would carry the datagrams; as of this reading there is no relay to carry them
- evidence:
  - [1] 2026-10-23: 'It's free. All of it.' - unlimited tunnels, unlimited bandwidth and requests, Private VPN over WireGuard, no card, no trial, no expiry
  - [2] 2026-10-23: reserved public UDP port, generated wg0.conf with Endpoint agent.21tunnel.com:31099, 'Free on all plans'
  - [3] 2026-10-23: 'WireGuard endpoint behind NAT' with 'mytunnel udp 51820 --public-port 31820' and a 60-second idle window'
  - probe:https://cloudflare-dns.com/dns-query?name=agent.21tunnel.com&type=A 2026-10-23: DNS status 3, NXDOMAIN, no answer record; the same query for 21tunnel.com returns status 0 with 172.67.170.252 and 104.21.87.222
  - probe:https://cloudflare-dns.com/dns-query?name=login.21tunnel.com&type=A 2026-10-23: DNS status 3, NXDOMAIN, for A and AAAA; a direct HTTPS request to login.21tunnel.com from this host returns no status code and no remote IP
  - [4] 2026-10-23: 'We're newer, and we're up-front about it - MVP-stage', which is consistent with docs published ahead of deployment
- sources:
  - [1] https://21tunnel.com/pricing/
  - [2] https://21tunnel.com/docs/private-vpn/
  - [3] https://21tunnel.com/docs/tunnels/
  - [4] https://21tunnel.com/vs/ngrok/
