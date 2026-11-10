# Hosting-Minecraft.pro

> hosting-minecraft.pro | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hosting-minecraft/ | JSON https://fshy.ajam.dev/api/v1/entity/hosting-minecraft.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hosting-Minecraft.pro

- `egress/hosting-minecraft-pro` | paid-only | evidence documented | binding write-gated | category game anycast proxy with a UDP tunnel | tier free
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://my.hosting-minecraft.pro/index.php?rp=%2Fannouncements%2F89
- price EUR 1/month minimum for the panel; proxy free with it | parsed USD 1.12/mo
- free tier: We are launching an analogue of TCPShield and NeoProtect, completely free. You only need to create a domain in the Minecraft server control panel. [translated] | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published for the proxy or the UDP tunnel. The cheapest plan that yields a panel domain is PROXY POWER from EUR 1 per month, listed as 'unlimited slots and traffic'.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: A hosting account with a Minecraft server: 'You only need to create a domain in the Minecraft server control panel', and the cheapest panel plan is EUR 1/month. | country: None
- interface: unknown
- limits:
  - write-gated (binding): the free anycast proxy and its UDP tunnel require a domain created in the provider's own Minecraft panel [1]
  - write-gated (binding): the feature is in beta: 'The feature is currently in BETA testing' with possible proxy restarts [1]
- binding note: The proxy is free but only for a server hosted in the provider's panel, so the first thing that fails is the account: a paid plan from EUR 1/month stands between an account and the free UDP tunnel. No volume figure exists to fail next.
- interface detail: A Minecraft hosting panel with a domain and proxy-protocol setting; no API is described.
- tooling: The vendor's game panel; no separate tunnel client
- composes with: Only composes with a server hosted there, so it replaces a free VM rather than sitting in front of one.
- reliability: Beta with proxy restarts announced; the vendor warns of bugs during testing. UDP tunnel drops were not reported here but the UDP path is the newest part.
- notes: Game hosting provider offering free Minecraft servers with UDP support for voice and Bedrock connections on managed instances.
- evidence note: The announcement and the price list were both read; whether the EUR 1 plan is enough to unlock the UDP tunnel, or a larger plan is required, is not stated.
- extras:
  - wg_path: unknown
  - wg_detail: No WireGuard mode. The UDP tunnel is sold for voice and Bedrock, so whether an arbitrary WireGuard datagram would pass is unstated.
  - ingress: udp
  - volume_stated: No byte allowance is published for the proxy or the UDP tunnel. The cheapest plan that yields a panel domain is PROXY POWER from EUR 1 per month, listed as 'unlimited slots and traffic'.
  - bytes_transit: yes
  - transit_note: The provider's anycast points carry the traffic to the hosted server.
- evidence:
  - [1] 2026-10-23: 'The ability to tunnel the UDP protocol for VOICE and Bedrock (geyser) FREE IN TWO CLICKS.' [translated]
  - [1] 2026-10-23: 'You only need to create a domain in the Minecraft server control panel.' [translated]
  - [2] 2026-10-23: The cheapest plan is PROXY POWER 'from 1 EUR per month' with 'Ports 5 pcs TCP/UDP', so there is no zero-cost path to the panel [translated]
  - [1] 2026-10-23: Anycast points listed as active: Germany (Frankfurt), Russia (Moscow), Russia (Saint Petersburg), Ukraine (Kyiv), Kazakhstan, Russia (Novosibirsk); Hong Kong 'under discussion'
- sources:
  - [1] https://my.hosting-minecraft.pro/index.php?rp=%2Fannouncements%2F89
  - [2] https://hosting-minecraft.pro/
