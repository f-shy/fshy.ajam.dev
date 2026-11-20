# Solar Proxy

> solar-proxy.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/solar-proxy/ | JSON https://fshy.ajam.dev/api/v1/entity/solar-proxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Solar Proxy

- `egress/solar-proxy` | fails-egress | evidence documented | binding none | category Bedrock client gateway | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://solar-proxy.com/
- price unstated
- free tier: A Minecraft Bedrock proxy for connecting to featured servers, Realms, and friends' worlds. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance and no pricing are published; the page is 81 words and names no plan.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'Connect Minecraft with the device code first (More -> Account)', which is a Microsoft account device-code flow. | country: None
- interface: unknown
- binding note: The page offers a client-side gateway with Server IP and Port fields and a list of featured servers. It issues no address to a server owner, so no quota is ever the constraint.
- interface detail: A web connect form; no API is described.
- tooling: Web page and app; no agent
- composes with: Nothing to chain: it is a player-side hop.
- reliability: Latency to the featured servers is shown per server; nothing is stated about a locally run server.
- notes: Named here because a search for a free Bedrock proxy returns it near the top and a reader would otherwise re-open it. It is the console/mobile client problem again: the proxy sits in front of the player, not in front of the server.
- evidence note: The page states what the product is and shows no server-side product; whether a paid tier exists is unread because no pricing page is linked.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard and no customer endpoint.
  - ingress: none
  - volume_stated: No byte allowance and no pricing are published; the page is 81 words and names no plan.
  - bytes_transit: yes
  - transit_note: The Solar Proxy service relays the player's connection.
- evidence:
  - [1] 2026-10-23: 'Solar Proxy - A Minecraft Bedrock proxy for connecting to featured servers, Realms, and friends' worlds.'
  - [1] 2026-10-23: The interface offers 'Server IP', 'Port' and 'Connect Minecraft with the device code first (More -> Account)', and lists HIVE GAMES, LIFEBOAT, MEGA SMP, CUBECRAFT, GALAXITE and MINEVILLE as featured servers
- sources:
  - [1] https://solar-proxy.com/
