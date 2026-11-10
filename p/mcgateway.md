# MCGateway

> mcgateway.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mcgateway/ | JSON https://fshy.ajam.dev/api/v1/entity/mcgateway.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MCGateway

- `egress/mcgateway` | fails-egress | evidence documented | binding none | category Bedrock console gateway (Xbox Live friend bot) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://mcgateway.net/
- price USD 0
- free tier: The core MCGateway transfer service is free and is intended to remain free. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published and none would apply: the service is a bot the player friends, not a port.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: An Xbox Live account to friend the bot: 'Add an available MCGateway bot, wait for the automatic friend acceptance, then join MCGateway Hub.' No Microsoft password is asked for. | country: None
- interface: unknown
- limits:
  - write-gated: the transfer requires an access bot to accept a friend request first; no address is issued to the server owner [1]
- binding note: There is no public address or port to meter, so no byte allowance is ever reached. The gate is the shape of the service: a player joins a bot's world and is transferred from inside the game.
- interface detail: No API is described; access is through the Minecraft Friends tab and a Discord for server-owner tickets.
- tooling: Minecraft client only; no agent, no CLI
- composes with: Composes with any Bedrock host, including one behind another vendor's UDP tunnel, but adds nothing itself.
- reliability: Friend acceptance 'usually takes around 20 to 30 seconds and can take up to 60 seconds'; a stale Friends list needs a game restart; the bot fleet is the only path.
- notes: DNS and proxy utility for console Minecraft players to connect to external Bedrock servers without requiring server-side port forwarding configuration.
- evidence note: The join flow is quoted in full on the front page; whether a server owner can obtain any address was checked on the front page only, and the detailed guide was not read.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard and no address to reach: the transfer runs inside Minecraft's Friends list.
  - ingress: none
  - volume_stated: No byte allowance is published and none would apply: the service is a bot the player friends, not a port.
  - bytes_transit: yes
  - transit_note: The bot's Xbox Live session relays the player into the destination server.
- evidence:
  - [1] 2026-10-23: 'Add an access bot, join the MCGateway Hub through your Friends tab, and choose where you want to go.'
  - [1] 2026-10-23: 'Open the Hub menu with the robot or Ender Pearl, choose Add Server, enter the Bedrock IP and port, then transfer.' The destination is dialled by the bot, not by the player
  - [1] 2026-10-23: 'The core MCGateway transfer service is free and is intended to remain free.'
- sources:
  - [1] https://mcgateway.net/
