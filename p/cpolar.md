# cpolar

> cpolar.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cpolar/ | JSON https://fshy.ajam.dev/api/v1/entity/cpolar.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cpolar

- `egress/cpolar` | fails-egress | evidence documented | binding per-ip-shaping | category tcp port forward | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T15:23:40.713Z (live) | stale on 2026-12-26
- url https://www.cpolar.com/pricing
- price USD 0
- free tier: Free edition: permanently free, 1 Mbps, random URL subdomain, random TCP port, HTTP / TCP tunnel support, 1 online cpolar process, 4 tunnels per process. [translated] | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte quota on any plan: every plan is sold with traffic not limited. The free plan's 1 Mbps caps a saturated month at about 324 GB.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: The sign-up form has fields for user name, login email, contact phone, password and invite code; the pricing FAQ defines one online process as one email account running on one machine, so more machines need more email accounts. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): 1 Mbps on the free plan [1]
  - request-rate: connection-rate limit per tunnel endpoint; excess HTTP connections get 429, excess TCP connections are closed [1]
  - request-rate: 1 online process and 4 tunnels on the free plan [1]
- binding note: Traffic is unlimited but 1 Mbps is 10.5 GB/day, about 324 GB over 30 days, against 3.24 Mbps for 1 TiB/month. The shaping binds three times.
- interface detail: Web UI on localhost:9200 after install, a CLI with authtoken authentication, and a dashboard at dashboard.cpolar.com.
- tooling: vendor client on Windows/Linux/NAS/ARM, authenticating with a token from the dashboard; wg-quick cannot attach to it
- composes with: Carries HTTP and TCP only, so it composes with a web service or an SSH control channel and not with WireGuard.
- reliability: Exceeding the connection rate limit returns 429 on HTTP and silently closes TCP and TLS connections; the vendor documents neither the threshold nor a reset window.
- notes: The best-identified Chinese tunnel vendor in English lists, with an email-only account, and the only one here with a documentation set large enough to make the absence of UDP meaningful. No English pricing arm was found: www.cpolar.com/en/pricing returns 404 and the only pricing page is the Chinese one.
- evidence note: Pricing table read first-party and the whole documentation site searched for UDP with zero hits. A negative search is strong evidence here because the same docs page documents TCP, HTTP and TLS tunnels by name.
- extras:
  - wg_path: none
  - wg_detail: No UDP reconstruction exists: the pricing page lists only HTTP and TCP tunnels, and an 87 KB full-text read of the documentation site at /docs contains no occurrence of UDP at all.
  - ingress: tcp
  - volume_stated: No byte quota on any plan: every plan is sold with traffic not limited. The free plan's 1 Mbps caps a saturated month at about 324 GB.
  - bytes_transit: yes
  - transit_note: Vendor relays in mainland China carry the tunnel.
- evidence:
  - [1] 2026-10-23: free plan is 1 Mbps, random subdomain, random TCP port, HTTP/TCP tunnels only, 1 process, 4 tunnels; all plans state traffic is not limited
  - [2] 2026-10-23: 86941-byte documentation read contains no occurrence of UDP
  - [3] 2026-11-25: the sign-up form has a contact phone field | capture: sha256:2f9b3ff4063bc7fbb6f72c73ff02fda13fdd129bbe937b01eee80ed5b512d5ca | quote: 联系电话
  - [1] 2026-11-25: the free plan is 1 Mbps | capture: sha256:8c901115ae4fbf129b02b4488691900623265428b579950de6bb9fca02ea9ac3 | quote: ## 1Mbps
  - [1] 2026-11-25: excess HTTP connections get a 429 response | capture: sha256:8c901115ae4fbf129b02b4488691900623265428b579950de6bb9fca02ea9ac3 | quote: cpolar将对超出速率限制的HTTP连接返回` 429 `响应。
  - [1] 2026-11-25: all plans state traffic is not limited | capture: sha256:8c901115ae4fbf129b02b4488691900623265428b579950de6bb9fca02ea9ac3 | quote: 所有套餐均附带21天退款保证，且不限制流量
- sources:
  - [1] https://www.cpolar.com/pricing
  - [2] https://www.cpolar.com/docs
  - [3] https://dashboard.cpolar.com/signup
