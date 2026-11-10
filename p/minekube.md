# Minekube Connect

> minekube.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/minekube/ | JSON https://fshy.ajam.dev/api/v1/entity/minekube.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Minekube Connect

- `egress/minekube-connect` | fails-egress | evidence documented | binding none | category game reverse proxy (Minecraft TCP edge) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://connect.minekube.com/
- price USD 0
- free tier: A global gateway to a DDoS-protected developer platform with public domains for localhost. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published on the front page.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: An account on app.minekube.com, plus a connector plugin or the Gate agent on the origin. The register form was not read. | country: None
- interface: cli
- limits:
  - write-gated: reaching the network requires running a connector (plugin or Gate) on the origin [1]
- binding note: Operates as a TCP reverse proxy for Minecraft servers. Assigns public domains to private origins without requiring public IP addresses.
- interface detail: Download the Connect plugin or run the Gate connector; a dashboard at app.minekube.com issues the public domain.
- tooling: Connect plugin or the Gate connector on the origin
- composes with: Gives a localhost Minecraft server a public hostname over an outbound connection, so it composes with a free VM that has no inbound ports.
- reliability: Traffic passes a shared superproxy; the origin runs a connector that holds the connection open.
- notes: Minecraft TCP reverse proxy designed to expose local game servers via domain routing without public IP configuration.
- evidence note: The vendor's own words describe a TCP edge. A Bedrock path, if one exists behind the connector, would change the record and would need its docs pages read.
- extras:
  - wg_path: none
  - wg_detail: A Minecraft TCP edge network; no UDP ingress is described.
  - ingress: tcp
  - volume_stated: No byte allowance is published on the front page.
  - bytes_transit: yes
  - transit_note: Minekube's superproxy carries the game traffic
- evidence:
  - [1] 2026-10-23: Minekube Connect is described as 'a cloud-native Minecraft TCP edge network' giving public domains for localhost, reached by a self-hosted Connector
- sources:
  - [1] https://connect.minekube.com/
