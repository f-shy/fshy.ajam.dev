# OwnServer

> kumassy.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kumassy/ | JSON https://fshy.ajam.dev/api/v1/entity/kumassy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OwnServer

- `egress/ownserver` | dead | evidence documented | binding none | category tcp+udp tunnel for local game servers (hosted, Japan) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://ownserver.kumassy.com/
- price USD 0
- free tier: [translated] Headline: 'A game server you can use for free, without limits'. The feature list gives 'Free' and 'Unlimited' as separate items, and the mechanism section says: 'When you start the OwnServer Client, a dedicated secure tunnel is created between OwnServer and your computer, and a public address dedicated to your server is issued.' | unit: unlimited | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: [translated] 'A game server you can use for free, without limits', with 'Unlimited' as a feature heading. No byte figure, no rate, no session length.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: [translated] The documented flow is: download the OwnServer Client, download the game server program, start the OwnServer Client, play with friends. No account, email or payment step appears in it. | country: None
- interface: unknown
- binding note: Nothing binds: the service is suspended. The announcement dated 2026/04/06 says operation has stopped temporarily and no restart date is set.
- interface detail: [translated] 'OwnServer Client' is a per-OS desktop download; the page documents no API, no command line and no configuration file.
- tooling: the vendor's own desktop client only (Windows, Linux x86_64/ARM, macOS Intel/Apple Silicon builds listed); no CLI flag, no API, no .conf
- composes with: none while suspended; if it reopens it would be the only free Japanese host that publishes an arbitrary local TCP or UDP port without an account.
- reliability: Suspended 2026-04-06 for stated stability and security problems; a client-side connection drop was patched with auto-reconnect in v0.10.0 (2025-04-20), which is the class of failure that preceded the suspension.
- notes: Japanese tunneling provider supporting TCP and UDP forwarding. Live endpoints returned HTTP 530 on 2026-10-23. Archived documentation from 2026-04-14 describes custom game server forwarding.
- evidence note: Service suspension notice is documented on the vendor front page.
- extras:
  - wg_path: none
  - wg_detail: A closed-source desktop client issues a public address for a local server; it does not hand out a WireGuard configuration, and a user is the only documented way in.
  - ingress: tcp+udp
  - volume_stated: [translated] 'A game server you can use for free, without limits', with 'Unlimited' as a feature heading. No byte figure, no rate, no session length.
  - bytes_transit: yes
  - transit_note: The vendor relays between the issued public address and the local machine.
- evidence:
  - [1] 2026-10-23: [translated] '2026/04/06: we had been publishing the service on a trial basis, but because there are many problems with stability and security we are temporarily suspending provision of the service. The restart date is undecided.'
  - [1] 2026-10-23: The front page lists 'Free' and 'Unlimited' as features and describes a client-created tunnel that issues a public address for the local game server.
- sources:
  - [1] https://web.archive.org/web/20260414224601/http://ownserver.kumassy.com/
  - [2] https://ownserver.kumassy.com/
