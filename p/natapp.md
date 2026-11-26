# NATAPP

> natapp.cn | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/natapp/ | JSON https://fshy.ajam.dev/api/v1/entity/natapp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NATAPP

- `egress/natapp` | fails-quota | evidence documented | binding volume-quota | category udp port forward | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T19:55:31.196Z (live) | stale on 2026-12-26
- url https://natapp.cn/
- price USD 0
- free tier: Free tunnel (registered users): permanently free, 1M bandwidth, 2 GB traffic per month, HTTP/TCP/UDP tunnels, random domain or random TCP/UDP port, forced domain/port change at intervals. [translated] | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 GB per month on the free tunnel.; ingress: udp | metered: yes | free allowance: 2 GB per month on the free tunnel. | source: [1]
- identity: any-phone | detail: Registration takes a mobile phone number as the account name, a password, an email address for notifications, a nickname and an SMS verification code. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 2 GB per month [1]
  - per-ip-shaping: 1 Mbps [1]
- limits note: the free tunnel's random domain and TCP/UDP port are force-changed at irregular intervals
- binding note: 2 GB per month fails 1 TiB by a factor of about 550, and the 1 Mbps cap would fail it too: 1 Mbps sustained is roughly 0.32 TB per month.
- interface detail: Vendor client for Windows/Linux/macOS plus a web console.
- tooling: vendor client plus frpc-compatible config
- composes with: Not viable as a WG endpoint because the port is not stable.
- reliability: Random public port is reassigned at intervals, so any fixed endpoint stops resolving.
- notes: The port-insecurity sentence is the interesting part for UDP: a WG endpoint written into a conf file goes stale without notice. The nodeloc roundup separately warns each free tunnel lasts only 3 days, which contradicts the vendor's 'permanently free' label; the vendor says the tunnel persists but the address changes.
- evidence note: All three numbers are on the vendor's own pricing block. A probe would only confirm the port rotation interval.
- extras:
  - wg_path: inside-udp
  - wg_detail: The free tier advertises UDP tunnels on a random port; a WG handshake can be carried, but the port is reassigned at intervals, so a WG endpoint would need reconfiguration each time.
  - ingress: udp
  - volume_tib_month: 0.0018
  - volume_stated: 2 GB per month on the free tunnel.
  - bytes_transit: yes
  - transit_note: NATAPP relays through domestic nodes.
- evidence:
  - [1] 2026-10-23: free tunnel is 1 Mbps, 2 GB per month, random port, force-changed at intervals
  - [1] 2026-11-25: the free tunnel is permanently free at 1M bandwidth and 2 GB of traffic a month over http, tcp and udp, with a random domain or port force-changed at irregular intervals | capture: sha256:84f1489e3c9c741dbafc8c0db35b0a4a44064b3f8b3ae87c2cee29a7f304e139 | quote: 免费隧道(注册用户) 永久免费 1M带宽 流量2G/月 提供http,tcp,udp全隧道穿透 随机域名/随机TCP,UDP端口 不定时强制更换域名/端口
  - [1] 2026-11-25: the free tunnel's random domain and TCP/UDP port are force-changed at irregular intervals | capture: sha256:84f1489e3c9c741dbafc8c0db35b0a4a44064b3f8b3ae87c2cee29a7f304e139 | quote: 随机域名/随机TCP,UDP端口 不定时强制更换域名/端口
  - [2] 2026-11-25: registration needs a mobile phone number as the account, a password, an email address, a nickname and an SMS code | capture: sha256:51cb8ac042fb8b8654d89192959ff8992517d6199416b7232cec08549fd6f254 | quote: 您首先需要注册一个账号(手机号)成为NATAPP用户。当您注册时，您需要至少向我们提供您准备使用的账号(手机号)、密码、电子邮箱地址（接收通知）,昵称，我们将通过发送短信验证码。
- sources:
  - [1] https://natapp.cn/
  - [2] https://natapp.cn/register
