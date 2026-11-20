# mudcat

> mudcat.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mudcat/ | JSON https://fshy.ajam.dev/api/v1/entity/mudcat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mudcat

- `egress/mudcat` | fails-quota | evidence documented | binding retention-clamped | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.mudcat.io/
- price USD 0
- free tier: Yes. You can use it for free. However, in the case of free users, there are restrictions on usage time, transmission speed, and amount of transmission data. | unit: unlimited | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The vendor states restrictions on usage time, transmission speed, and amount of transmission data, with no numbers published. The support forum answers the same question with: At this moment, no restriction because it is under alpha status.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: The client assigns a Device UUID and needs no account, email or card on the page read; the download page lists only operating-system binaries. | country: None
- interface: cli
- limits:
  - retention-clamped (binding): Access Domain TTL: valid for 8.00 hours for TCP and UDP tunnels [1]
  - volume-quota: unpublished restriction on amount of transmission data [1]
- binding note: Free tier port lease expires after 8 hours. Data volume policies are unstated in published terms.
- interface detail: ./mudcat udp --local-port 25565 --remote-port 25566.
- tooling: Single binary from mudcat.io/download, subcommands tcp, http and udp.
- composes with: Carries a WireGuard handshake to a free VM, or exposes a game server directly; the 8-hour hostname means it needs a supervisor that re-registers and re-points DNS.
- reliability: Alpha software at version 0.0.3; hostnames expire every 8 hours; the vendor reserves the right to cap time, speed and data without publishing numbers.
- notes: The alpha status is the important fact: the free tier works today with no stated cap, and the caps are promised but unwritten. Version 0.0.3 and a 2024 forum thread mean this is not a 2026 launch, only a 2026-live one. The conservative verdict is kept: the 8-hour lease and an unpublished byte cap both defeat the test, and neither can be designed against.
- evidence note: The free-tier byte and speed limits are unpublished; one measured transfer and a reconnect after 8 hours would move this from documented to measured.
- extras:
  - wg_path: inside-udp
  - wg_detail: The vendor documents a UDP forwarding mode: Forwarding: UDP 583-841-3346.mudcat.io:25566 -> 127.0.0.1:25565. A WireGuard handshake is an opaque UDP datagram and passes through that path.
  - ingress: tcp+udp
  - volume_stated: The vendor states restrictions on usage time, transmission speed, and amount of transmission data, with no numbers published. The support forum answers the same question with: At this moment, no restriction because it is under alpha status.
  - bytes_transit: yes
  - transit_note: A Mudfish-operated remote access node forwards the datagrams.
- evidence:
  - [1] 2026-10-23: HTTP, TCP and UDP port sharing; UDP example with an 8-hour Access Domain TTL; free use with unpublished restrictions on time, speed and data.
  - [2] 2026-10-23: Vendor staff answer of 2024-08-13 that there is no restriction while the service is in alpha, which means the published restriction has no number behind it.
  - [3] 2026-10-23: Client version 0.0.3 for Windows, macOS and Linux, which supports the alpha reading.
  - [4] 2026-10-23: 'Yes, it can be used free of charge. However, in the case of free users there are restrictions on usage time, transmission speed, amount of transmitted data and so on'; no figure is published
- sources:
  - [1] https://www.mudcat.io/
  - [2] https://forums.mudfish.net/t/what-are-the-restrictions-on-mudcat-free-version/75027
  - [3] https://www.mudcat.io/download
  - [4] https://mudcat.io/
