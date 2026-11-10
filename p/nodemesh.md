# NodeMesh

> nodemesh.app | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nodemesh/ | JSON https://fshy.ajam.dev/api/v1/entity/nodemesh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NodeMesh

- `egress/nodemesh` | qualifies-with-caveat | evidence documented | binding none | category game server control plane with a UDP traffic relay | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:53:00.067Z (live) | stale on 2026-12-05
- url https://nodemesh.app/games/minecraft-bedrock
- price USD 0 for the first node
- free tier: One host - your own PC - is free with no time limit, for as many game servers as your hardware can run: the web panel and console, the config editor, the mod manager, auto-restart on crash and the traffic relay. | unit: mixed | metered on: none | read on: 2026-10-23 | source: [1] | note: extra BYOH nodes consume NMC credits, which the vendor grants and which cannot be bought
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published anywhere read: 'Your first BYOH node is completely free - no time limits, no credit card, all features included.'; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: A signup with a verified email: 'Create a free account', and crash alerts go to 'your verified email'. | country: None
- interface: unknown
- limits:
  - volume-quota: no byte allowance published for the traffic proxy [2]
- binding note: Nothing published caps 1 TiB/month, so the volume test can be neither failed nor passed from documents. The named constraint is the one the vendor states instead of a quota: the relay is 'Not DDoS protection', and in relay mode 'The game sees every player as one local address, so IP bans don't work.'
- interface detail: An agent binary plus a web panel; the pages read describe no public API and no tunnel-only command.
- tooling: nodemesh agent (sudo install script on Linux), web panel, console; no standalone tunnel CLI is documented
- composes with: The agent is the only thing that must run, so it fits a free Linux VM; the game server itself is installed by the platform.
- reliability: Relay mode collapses every player to one local address, so per-player IP bans stop working; the vendor says the relay is not DDoS protection; a node that goes offline pauses its servers and disconnects players.
- notes: Beta, stated on the page: 'you can create this server today, but we have not run it on our own hardware yet'. The free unit is one host, so a second machine needs credits. The relay is documented for game servers; the site does not offer a generic arbitrary-UDP port, so whether a non-game UDP listener works behind it is unstated.
- evidence note: Running the agent and pushing a counted volume through the proxy would show whether an unpublished cap or throttle exists, and a probe record would make this measured.
- extras:
  - wg_path: inside-udp
  - wg_detail: No WireGuard mode of its own; the relay is documented as carrying UDP, so a WireGuard datagram to the proxy address is the same path. Untested.
  - ingress: tcp+udp
  - volume_stated: No byte allowance is published anywhere read: 'Your first BYOH node is completely free - no time limits, no credit card, all features included.'
  - bytes_transit: yes
  - transit_note: NodeMesh's edge proxy carries the player traffic; the origin only makes an outbound connection.
- evidence:
  - [1] 2026-10-23: 'Bedrock uses UDP on port 19132 (IPv4) and 19133 (IPv6). The relay forwards them to your PC, so you make no changes to your router.'
  - [2] 2026-10-23: 'TCP and UDP both supported' under Traffic Proxy, and 'Included free with your first BYOH node'
  - [2] 2026-10-23: In relay mode: 'The game sees every player as one local address, so IP bans don't work.' and 'Not DDoS protection.'
  - [3] 2026-10-23: 'Your first BYOH node is completely free - no time limits, no credit card, all features included.' and 'This is free forever - not just during beta.'
  - [3] 2026-10-23: Extra nodes 'cost 5 NMC/month each', so the free unit is one node rather than a byte count
  - [2] 2026-10-23: The agent install is 'curl -sSL https://install.nodemesh.app | sudo sh', and the origin must be Linux: 'It needs a Linux host'
  - [3] 2026-11-03: the free first node includes the traffic proxy, with no byte or time limit stated | capture: sha256:d60c137e85231d1a04f63cee739b460e6d6abcad93f44004b641d460fc3ff341 | quote: Your first BYOH node with as many game servers as your hardware can run, traffic proxy, full web panel, console, file manager, config editor, mod manager, crash detection, and email notifications.
  - [4] 2026-11-03: NMC cannot be purchased; the vendor grants it | capture: sha256:dfa6af4387ba18fa8e9812d1ff3659846ba0cd8a4df0e176f5dcc0c13cbcecf5 | quote: There is currently no payment or purchase — NMC is granted by the NodeMesh team, and you cannot buy it.
  - [4] 2026-11-03: the free node is not stopped when the NMC balance reaches zero | capture: sha256:dfa6af4387ba18fa8e9812d1ff3659846ba0cd8a4df0e176f5dcc0c13cbcecf5 | quote: Servers on your free BYOH node are never stopped for balance reasons.
  - [3] 2026-11-04: the pricing page states the first node with traffic proxy is free forever and publishes no byte cap | capture: sha256:d60c137e85231d1a04f63cee739b460e6d6abcad93f44004b641d460fc3ff341 | quote: This is free forever — not just during beta.
- sources:
  - [1] https://nodemesh.app/games/minecraft-bedrock
  - [2] https://nodemesh.app/docs
  - [3] https://nodemesh.app/pricing
  - [4] https://nodemesh.app/terms
