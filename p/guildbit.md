# GuildBit

> guildbit.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/guildbit/ | JSON https://fshy.ajam.dev/api/v1/entity/guildbit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GuildBit

- `egress/guildbit` | fails-egress | evidence documented | binding none | category voice server hosting (Mumble) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:29.662Z (live) | stale on 2026-12-26
- url https://www.guildbit.com/
- price USD 0
- free tier: GuildBit is a free service to deploy temporary Mumble servers for your group. | unit: users | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: the server runs for a chosen duration of 1 to 4 hours; the duration can be extended up to 3 times | source: [1]
- egress: 'Free servers are currently limited to 15 slots.' No bandwidth figure is published. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: The landing page offers 'Generate Password' and a deploy action; no account is named before deployment. | country: None
- interface: unknown
- limits:
  - volume-quota: no byte allowance published; 15 slots on the free server [1]
- binding note: Fifteen slots is the published ceiling and no bandwidth is published; because GuildBit hosts the server, no volume of traffic passes through a port under the account's control.
- interface detail: A web form that generates a password and deploys a server.
- tooling: Browser only
- composes with: Useful only if a voice server is wanted rather than a path to its own.
- reliability: Servers are described as temporary; the service is donation funded.
- notes: Free hosted Mumble voice server provider. Provides managed Mumble voice servers on shared infrastructure rather than arbitrary UDP port forwarding.
- evidence note: The front page settles what the product is; whether a deployed server can be pointed at an external host was not tested and is unlikely.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard; the service runs the server rather than forwarding a port to one.
  - ingress: none
  - volume_stated: 'Free servers are currently limited to 15 slots.' No bandwidth figure is published.
  - bytes_transit: no
  - transit_note: Voice traffic terminates on GuildBit's own Mumble process.
- evidence:
  - [1] 2026-10-23: 'GuildBit is a free service to deploy temporary Mumble servers for your group. The service is completely funded by donations and upgrades.'
  - [1] 2026-10-23: 'Free servers are currently limited to 15 slots'
  - [1] 2026-11-25: free servers are still limited to 15 slots and no byte allowance is published | capture: sha256:1a79e2d5429c37283f0f725592e3dc8365c735f4af28216668b48ddb1d700e84 | quote: Free servers are currently limited to 15 slots
  - [2] 2026-11-25: a server runs for a chosen duration of 1 to 4 hours and can be extended up to 3 times | capture: sha256:0fd71c8873824aead6f5bbb063065b7dd7862da98ae3b6ae570a648b8f8bc229 | quote: Choose a duration for the server. From 1 to 4 hours. ... You may also extend the server duration up to 3 times!
  - [1] 2026-11-25: free servers are still limited to 15 slots, the published ceiling | capture: sha256:1a79e2d5429c37283f0f725592e3dc8365c735f4af28216668b48ddb1d700e84 | quote: Free servers are currently limited to 15 slots
- sources:
  - [1] https://www.guildbit.com/
  - [2] https://www.guildbit.com/how-it-works
