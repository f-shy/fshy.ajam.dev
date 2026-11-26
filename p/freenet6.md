# Freenet6

> freenet6.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freenet6/ | JSON https://fshy.ajam.dev/api/v1/entity/freenet6.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Freenet6 (gogo6)

- `egress/freenet6` | dead | evidence reported | binding none | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:23:44.599Z (live) | stale on 2026-12-10
- url http://freenet6.net/
- price USD 0
- free tier: the service closed in 2016; the announcement is titled 'gogoNET and Freenet6 Closing Down' and the domain now returns an HTTP 200 with an empty body | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable: the service is closed; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: not applicable: no signup exists | country: None
- interface: unknown
- binding note: The provider is dead, so no constraint is reached at any volume. It stays in the record because it is still the second entry in most lists of tunnel brokers and because the gogoc client it required was still packaged until 2022.
- interface detail: no interface is published: the domain answers HTTP 200 with a 0-byte body
- tooling: the gogoc client port was deleted from FreeBSD ports on 2022-04-30; other package trees were not checked
- composes with: not applicable
- reliability: gogoNET announced on 2016-04-14 that Freenet6 would stop accepting new users and its future operation was unknown
- notes: Kept as the canonical dead entry: any list of brokers that still names Freenet6 or gogo6 is stale, and a user it required (gogoc, formerly Gateway6) is gone from the package trees.
- evidence note: Service termination was announced in 2016. Provider domain returns HTTP 200 with an empty body.
- extras:
  - wg_path: none
  - wg_detail: not applicable: the service predates WireGuard and closed in 2016
  - ingress: none
  - volume_stated: not applicable: the service is closed
  - bytes_transit: no
  - transit_note: not applicable
- evidence:
  - [2] 2026-10-23: forwarded announcement 'gogoNET and Freenet6 Closing Down', dated 2016-04-14
  - [1] 2026-10-23: HTTP 200 with an empty body: 'the origin returned an empty body, so there is nothing to read', Last-Modified 2026-07-17
  - [3] 2026-10-23: the gogoc port was deleted on 2022-04-30 because 'Services were discontinued in 2016'
  - probe:http://freenet6.net/ 2026-11-25: the domain returns an empty body | capture: sha256:d5d9c396c7e5f40e8c6fc832391a1c640f5edd5484fc2b7416a2e148eaf6598b | quote: "bytes": 0
  - [3] 2026-11-25: the gogoc port was deleted from FreeBSD ports on 2022-04-30 | capture: sha256:2ae36b083cecb3536d44324c90f49fa288eb0836deba3bc02114aaf1c8d5cf34 | quote: port deleted on 2022-04-30
  - [2] 2026-11-25: the 2016-04-14 announcement that Freenet6 stops accepting new users | capture: sha256:35ad04c18d9de6517f55096611088444d9a784d46cb65d7d4610185cc7ce9d98 | quote: The Freenet6 service will also stop accepting new users and it is unknown how long it will continue to operate for existing users.
  - [3] 2026-11-25: FreeBSD ports records the gogo6 services as discontinued in 2016 | capture: sha256:2ae36b083cecb3536d44324c90f49fa288eb0836deba3bc02114aaf1c8d5cf34 | quote: REASON: Has expired: Services were discontinued in 2016
  - [3] 2026-11-25: services were discontinued in 2016 | capture: sha256:2ae36b083cecb3536d44324c90f49fa288eb0836deba3bc02114aaf1c8d5cf34 | quote: REASON: Has expired: Services were discontinued in 2016
- sources:
  - [1] http://freenet6.net/
  - [2] https://mail.lacnic.net/pipermail/lacnog/2016-April/004464.html
  - [3] https://www.freshports.org/net/gogoc/
