# SunnyNgrok

> ngrok.cc | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ngrok/ | JSON https://fshy.ajam.dev/api/v1/entity/ngrok.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SunnyNgrok (ngrok.cc)

- `egress/sunny-ngrok` | fails-quota | evidence documented | binding volume-quota | category tcp+udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.ngrok.cc/
- price USD 0
- free tier: Trial edition, CNY 0 / permanent: 1 tunnel, random domain / port, 2 Mbps bandwidth rate, 1 GB of traffic per month. [translated] | unit: GB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 GB per month on the trial edition.; ingress: udp | metered: yes | free allowance: 1 GB per month on the trial edition. | source: [1]
- identity: email | detail: Registration asks for an email address, a password of at least eight characters and a verification code; an invite code is optional. No phone field appears. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 GB per month [1]
  - per-ip-shaping: 2 Mbps on the trial edition [1]
  - write-gated: fixed TCP ports are a paid feature [1]
- binding note: 1 GB per month is 0.0009 TiB, three orders; 2 Mbps would cap a month at about 648 GB anyway.
- interface detail: Windows, macOS, Linux, Android and ARM clients; a dashboard reports traffic and request counts.
- tooling: vendor client on Windows/macOS/Linux/Android/ARM plus wg-quick on the local box
- composes with: 1 GB monthly bandwidth supports WireGuard handshakes and keepalives at 2 Mbps, but restricts bulk transfer.
- reliability: The free tier gets a random subdomain and port; the vendor markets a separate paid tier for a fixed port and unlimited traffic.
- notes: Email-only registration and UDP ingress, so it is testable; the byte quota is what rules it out. Fixed TCP ports are listed only on the CNY 15/month tier.
- evidence note: Plan table and registration form read first-party. Whether the free random port survives a client restart is not stated and would need a probe.
- extras:
  - wg_path: inside-udp
  - wg_detail: The site states support for TCP and UDP, with UDP named for game hosting, so a WG datagram can ride a UDP tunnel. No WG config is issued, and the free tier assigns a random port.
  - ingress: udp
  - volume_tib_month: 0.00091
  - volume_stated: 1 GB per month on the trial edition.
  - bytes_transit: yes
  - transit_note: Vendor nodes on a CN2 line carry the tunnel.
- evidence:
  - [1] 2026-10-23: trial edition is 1 tunnel, random domain/port, 2 Mbps, 1 GB per month; UDP is listed as supported
  - [2] 2026-10-23: registration is email, password and verification code
- sources:
  - [1] https://www.ngrok.cc/
  - [2] https://www.ngrok.cc/register
