# portmap.io

> portmap.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/portmap/ | JSON https://fshy.ajam.dev/api/v1/entity/portmap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## portmap.io

- `egress/portmap-io` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category udp port forward (OpenVPN-based, hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://portmap.io/
- price USD 0
- free tier: Free: One configuration setting, One forwarding rule, Random external port, Auto-generated domain name | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Unlimited bandwidth' is a core feature line on the product page; no rate or tolerance is published; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: an account that generates an OpenVPN configuration or SSH key: 'Create a configuration file for OpenVPN or SSH key using the Generate button' | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): unlimited bandwidth stated, no rate published [1]
- binding note: The byte allowance is unlimited by statement, so the first real failure is that the free plan's external port is random and custom external ports are a Premium feature. That is a paywall on the one property a WireGuard endpoint needs, and it is not one of the seven vocabulary kinds.
- interface detail: OpenVPN config or SSH key plus a mapping rule created in the dashboard or by the API
- tooling: OpenVPN or SSH plus the portmap.io REST API and client
- composes with: one rule is one port, so it composes with exactly one WireGuard interface
- reliability: the free rule's external port is allocated by the operator and can in principle be reassigned; the tunnel is an OpenVPN session that must stay up
- notes: Port forwarding service providing free OpenVPN and WireGuard configurations. Free tier assigns one random external port; custom port numbers between 1024 and 65535 require paid configurations.
- evidence note: Whether the random port survives a reconnect is not stated anywhere on the site, which is the open question that decides the verdict. Raise by creating a free rule, noting the port, restarting the VPN, and reading the port again.
- extras:
  - wg_path: inside-udp
  - wg_detail: the rule forwards UDP: 'You can forward HTTP traffic to your local web-server as well as any TCP or UDP traffic.' The public port is random on the free plan and chosen on Premium.
  - ingress: tcp+udp
  - volume_stated: 'Unlimited bandwidth' is a core feature line on the product page; no rate or tolerance is published
  - bytes_transit: yes
  - transit_note: the portmap.io server terminates the VPN and forwards the rule's traffic
- evidence:
  - [1] 2026-10-23: free plan is one rule with a random external port; Premium USD 3.99/month adds custom external ports; 'Unlimited bandwidth'; TCP or UDP forwarding over OpenVPN
  - [2] 2026-10-23: 'What ports can I forward on Premium plan? The port number must be in range [1024-65535] and not occupied by another user', and 'Basic plan which allows only one mapping rule is unlimited'
- sources:
  - [1] https://portmap.io/
  - [2] https://portmap.io/support
