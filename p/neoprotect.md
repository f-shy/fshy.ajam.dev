# NeoProtect

> neoprotect.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neoprotect/ | JSON https://fshy.ajam.dev/api/v1/entity/neoprotect.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NeoProtect (GameShield)

- `egress/neoprotect` | paid-only | evidence documented | binding none | category game L4/L7 reverse proxy (Minecraft) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:31.197Z (live) | stale on 2026-12-26
- url https://neoprotect.net/gameshield
- price USD 0
- free tier: A permanently free Basic shield, then plan-based tiers that add bandwidth, domains, backends and advanced protection. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte figure is published for the free Basic shield: 'Plan limits and exact pricing are shown in the order process on our panel.'; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: An account at panel.neoprotect.net. The register form was not opened, so the required fields are unread. | country: None
- interface: rest
- limits note: the free Basic plan is '1 GameShield, Minecraft Java'; 'Bedrock / Geyser protection' is listed only on the plan-based tier
- binding note: Bedrock protection requires a paid plan, and the default RakNet port 19132 requires at least the Neo plan, so the plan tier is the constraint.
- interface detail: Self-serve panel at panel.neoprotect.net; API keys are a plan-based feature.
- tooling: DNS record in the panel, no client or plugin to install
- composes with: Point a domain at the shield and keep the origin hidden; no tunnel or agent, so it needs a public origin rather than composing with a private VM.
- reliability: Bedrock traffic on the paid tier needs both TCP and UDP open from NeoProtect's published IP list; the default 19132 allocation is manual.
- notes: DDoS protection proxy for Minecraft. Free tier supports Java edition over TCP and DNS routing. UDP forwarding on port 19132 and WebRTC requires paid plans.
- evidence note: The free-tier contents and the Bedrock gating are quoted from first-party pages. What the free shield's actual bandwidth allowance is would only come from the order flow behind a login.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard offering, and the free tier publishes no UDP port to put one behind.
  - ingress: tcp
  - volume_stated: No byte figure is published for the free Basic shield: 'Plan limits and exact pricing are shown in the order process on our panel.'
  - bytes_transit: yes
  - transit_note: NeoProtect's GameShield edge proxies the game traffic
- evidence:
  - [1] 2026-10-23: The Basic free plan is '1 GameShield, Minecraft Java'; 'Bedrock / Geyser protection' appears only under the plan-based tier, and voice proxies only under Enterprise
  - [2] 2026-10-23: Protecting Bedrock players requires a paid plan, and the default 19132 port requires at least the Neo plan; 19132 UDP is RakNet and 19132 TCP is NetherNet
  - [1] 2026-10-23: Plan limits and exact pricing are shown in the order process on the panel
  - [1] 2026-11-25: no plan limit or price is published on the page; both are shown at order time | capture: sha256:c97eede7328cefabd70eff6b896d8427fedba619fa08b4b403cda8c9ff753b61 | quote: Plan limits and exact pricing are shown in the order process on our panel.
  - [1] 2026-11-25: the free Basic plan lists one Minecraft Java shield; Bedrock and Geyser protection are listed only on the plan-based tier | capture: sha256:c97eede7328cefabd70eff6b896d8427fedba619fa08b4b403cda8c9ff753b61 | quote: - 1 GameShield, Minecraft Java ... - Bedrock / Geyser protection
  - [2] 2026-11-25: Bedrock protection requires a paid plan and the default RakNet port 19132 requires at least the Neo plan | capture: sha256:43f16b7a3e16412860f1c03c417b469973045d7c85cd3820ab07b6d6e329aa51 | quote: Protecting Bedrock players requires a paid plan. Requesting the default RakNet port (19132) requires at least the Neo plan.
  - [1] 2026-11-25: the Basic shield is permanently free and the other tiers are plan-based | capture: sha256:c97eede7328cefabd70eff6b896d8427fedba619fa08b4b403cda8c9ff753b61 | quote: A permanently free Basic shield, then plan-based tiers that add bandwidth, domains, backends and advanced protection.
- sources:
  - [1] https://neoprotect.net/gameshield
  - [2] https://docs.neoprotect.net/gameshield/bedrock/
