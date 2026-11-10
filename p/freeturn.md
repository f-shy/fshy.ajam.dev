# freeturn.net

> freeturn.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freeturn/ | JSON https://fshy.ajam.dev/api/v1/entity/freeturn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## freeturn.net

- `storage/freeturn-net` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:09:47.044Z (inherited) | stale on 2026-11-14
- url https://freeturn.net/
- free tier: not stated: https://freeturn.net/ does not resolve; public resolvers answer NXDOMAIN (Status 3) for freeturn.net | unit: none | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: freeturn.net redirected with HTTP 301 to fastturn.net, a paid TURN service, by 2024-12-31, served an expired-domain page on 2025-11-17, and does not resolve on 2026-10-30
- notes: free TURN relay: the archived page of 2024-05-27 listed a Free Plan at USD 0 forever with 1000 MBit/s and unlimited bandwidth; the domain then redirected to the paid fastturn.net and has since lapsed
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: freeturn.net does not resolve and holds no .net registration; the free TURN service ended
  - dead_end.retry_when: never; the domain lapsed. Re-open only if the free service is relaunched
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-10-30
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: 
  - probe:https://8.8.8.8/resolve?name=freeturn.net&type=A 2026-10-30: a public resolver answers NXDOMAIN (Status 3) for freeturn.net, with the .net registry as authority | capture: sha256:373948ca61bd2fca5168d9a68ff5a7f0b674ef326969b41d85bc33cc7700bf61 | quote: {"Status":3,"TC":false
  - probe:https://8.8.8.8/resolve?name=freeturn.net&type=A 2026-10-30: the resolver answered the query with HTTP 200, so the NXDOMAIN is its answer | capture: sha256:22053797e11508803d81f7d29ae48b96d6e641f35f212e75f7d8bac7e8dd2060 | quote: "status": 200
  - probe:https://1.1.1.1/dns-query?name=freeturn.net&type=A 2026-10-30: a second public resolver answers NXDOMAIN (Status 3) for freeturn.net | capture: sha256:0bfcd1dd7e49900d420cdeb7eda99463e39e7abe0b9aad6611e7c61c90178a64 | quote: {"Status":3,"TC":false
  - [2] 2026-10-30: the .net registry RDAP service holds no registration for freeturn.net | capture: sha256:e7a201f9cb8a1a55b51b370f744637e425d1f26cec240353c37a7dfb3050016d | quote: HTTP/1.1 404 Not Found
  - [3] 2026-10-30: the archived copy of 2025-11-17 is a registrar page for an expired domain | capture: sha256:b4b7e716000acce9c5f2bd4ad1e74e260f40552d2e2e3bfa579f80de8080e2da | quote: Your domain has expired. Please log in to your Spaceship account to renew it.
  - [4] 2026-10-30: on 2024-12-31 freeturn.net answered HTTP 301 with a redirect to https://fastturn.net/ | capture: sha256:af844f2ffa3ad9a11c5c36ad9bd5d061da5e25a9e68cfd3da0bf5461360c4d77 | quote: Got an HTTP 301 response at crawl time
  - [5] 2026-10-30: the archived page of 2024-05-27 listed a Free Plan with 1000 MBit/s and unlimited bandwidth | capture: sha256:e45296af846c42dde41e3460bee4119b970d5414564ec9612ff4a8c1c01e03fe | quote: 1000 MBit/s · Unlimited Bandwidth · No logging
  - [6] 2026-10-30: fastturn.net, the redirect target, sells paid plans with 25 GB of TURN traffic per month | capture: sha256:6be2eef16e08b1f9a3f5e9235e5462a9d9d2b20451515cc29dfe363e78db1609 | quote: Our plans include unlimited STUN connections and 25 GB of TURN traffic per month.
- sources:
  - [1] https://freeturn.net/
  - [2] https://rdap.verisign.com/net/v1/domain/freeturn.net
  - [3] https://web.archive.org/web/2025/https://freeturn.net/
  - [4] https://web.archive.org/web/2024/https://freeturn.net/
  - [5] https://web.archive.org/web/20240601000000/https://freeturn.net/
  - [6] https://fastturn.net/
