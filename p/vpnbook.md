# VPNBook

> vpnbook.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpnbook/ | JSON https://fshy.ajam.dev/api/v1/entity/vpnbook.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPNBook

- `egress/vpnbook` | fails-egress | evidence documented | binding write-gated | category vpn port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:43:49.813Z (live) | stale on 2026-12-26
- url https://www.vpnbook.com/freevpn/wireguard-vpn
- price USD 0, ad and donation funded
- free tier: Free WireGuard VPN servers in the US, UK, Canada, Germany and France. Generate a WireGuard config file or QR code in seconds, no signup. Configs last 7 days. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The page states no traffic allowance in either direction; it advertises no signup and no account, and is funded by ads and donations.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account at all: no signup, config generated on the page. | country: None
- interface: cli
- limits:
  - retention-clamped: configs expire after 7 days: Configurations auto-expire after 7 days for security. [1]
  - write-gated (binding): no port forwarding: nothing on the page offers an inbound port, and the servers are shared by an unknown number of users [1]
- binding note: Volume is not metered and no identity is demanded, so the failure is the missing inbound path: there is no port to reach a service on.
- interface detail: Web form generating a .conf or QR code.
- tooling: wg-quick or the official WireGuard app importing the generated .conf.
- composes with: A free client-side tunnel that composes with nothing inbound; useful for outbound fetches only.
- reliability: Shared servers with unknown load, 7-day config expiry, and no stated abuse tolerance; UDP only, so networks that block UDP cannot use it.
- notes: Free commercial VPN provider providing WireGuard and OpenVPN client configurations. Operates as an outbound VPN exit gateway; inbound port forwarding is not supported.
- evidence note: The free config and its 7-day expiry are the vendor's own statements read. The 1 TiB/month question is unanswerable from the page, so volume is left null rather than assumed unlimited.
- extras:
  - wg_path: native-conf
  - wg_detail: A genuine free WireGuard configuration with no account: Select a server, choose a port, and generate a unique WireGuard configuration. Each config expires after 7 days. Transport is UDP only.
  - ingress: none
  - volume_stated: The page states no traffic allowance in either direction; it advertises no signup and no account, and is funded by ads and donations.
  - bytes_transit: yes
  - transit_note: Traffic crosses VPNBook's donated servers.
- evidence:
  - [1] 2026-10-23: Free WireGuard configs with no signup in five countries, UDP only, auto-expiry after 7 days, and no port forwarding offered.
  - [1] 2026-11-25: configs expire after 7 days | capture: sha256:4768481443d0e093d44e331d8dca69a091dac63a6dbb5a203be1ad6920346e71 | quote: Each configuration is valid for 7 days. After expiration, you will need to generate a new one.
  - [1] 2026-11-25: free with no account or signup | capture: sha256:4768481443d0e093d44e331d8dca69a091dac63a6dbb5a203be1ad6920346e71 | quote: Yes. The servers, config files and QR codes are free, with no account or signup.
  - [1] 2026-11-25: the service is an outbound exit; no inbound port is described | capture: sha256:4768481443d0e093d44e331d8dca69a091dac63a6dbb5a203be1ad6920346e71 | quote: Your traffic is encrypted between your device and our server. From there it travels to websites as normal, so keep using HTTPS sites for anything sensitive.
- sources:
  - [1] https://www.vpnbook.com/freevpn/wireguard-vpn
