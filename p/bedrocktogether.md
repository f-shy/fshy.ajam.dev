# BedrockTogether

> bedrocktogether.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bedrocktogether/ | JSON https://fshy.ajam.dev/api/v1/entity/bedrocktogether.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BedrockTogether

- `egress/bedrocktogether` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category console LAN proxy (phone app) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://bedrocktogether.net/
- price USD 0
- free tier: BedrockTogether lets you join any Bedrock Edition server from Minecraft on Xbox, PlayStation and Nintendo Switch - no PC and no DNS changes required. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published and none applies: the app runs on the player's phone and the vendor carries nothing.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account: an App Store or Play Store install. | country: None
- interface: unknown
- binding note: The app is a LAN bridge on the player's phone, so no host gets a public endpoint and no quota is ever met.
- interface detail: A mobile app with a three-step join flow.
- tooling: iOS and Android app
- composes with: Sits in front of whatever UDP path the host already has; adds none.
- reliability: The phone must stay on the same network as the console for the LAN method; the Switch needs the Xbox Live broadcast method instead.
- notes: Mobile proxy application that connects to remote Minecraft Bedrock servers and re-broadcasts them as local LAN games. Operates client-side on local devices rather than providing a hosted public UDP endpoint.
- evidence note: The page states the mechanism plainly; whether the app also offers a hosted relay mode is not stated and was not tested.
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: No WireGuard; the app proxies on the player's own network.
  - ingress: none
  - volume_stated: No byte allowance is published and none applies: the app runs on the player's phone and the vendor carries nothing.
  - bytes_transit: overlay-only
  - transit_note: Player traffic goes phone to server; the app is a local relay on the player side.
- evidence:
  - [1] 2026-10-23: 'BedrockTogether runs on your phone and puts any Bedrock server in front of your console - no PC, no DNS rerouting, no router settings.'
  - [1] 2026-10-23: 'BedrockTogether makes any Minecraft Bedrock Edition server appear as a LAN game on Xbox, PlayStation & Nintendo Switch.'
- sources:
  - [1] https://bedrocktogether.net/
