# PCDeploy

> pcdeploy.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pcdeploy/ | JSON https://fshy.ajam.dev/api/v1/entity/pcdeploy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PCDeploy

- `egress/pcdeploy` | dead | evidence unverified | binding none | category game tunnel (claimed UDP and TCP) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T10:32:54.109Z (live) | stale on 2026-11-18
- url https://pcdeploy.net/
- price USD 0 (claimed)
- free tier: Yes. PCDeploy is completely free to use. Premium subscriptions with added functionality are planned to be added in the future. | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance appears in the copy preserved in the search index; the page itself could not be read.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Presumed, not observed: the indexed copy describes an account-based .exe, and the site never loaded, so the signup fields are unread. | country: None
- interface: unknown
- limits:
  - write-gated: one server at a time: 'Right now, only one server can be run at a time.' [1]
- binding note: Service endpoints are inactive. Historical documentation described single-server UDP proxying.
- interface detail: A .exe that asks for the port and returns a public address, per the indexed copy.
- tooling: A Windows .exe in the surviving copy
- composes with: Nothing until the host answers again.
- reliability: pcdeploy.net does not resolve: DNS-over-HTTPS answered NXDOMAIN (Status 3) for its A record on 2026-10-30, with the .net zone SOA as the authority, so the .net zone holds no delegation for the name.
- notes: Historical proxy tool designed for game server hosting. Service endpoints are inactive.
- evidence note: The death is measured: on 2026-10-30 DNS-over-HTTPS queries for the A record of pcdeploy.net answered NXDOMAIN at two public resolvers (Cloudflare and Google), with the .net zone SOA as the authority, and the .net registry's RDAP service answered HTTP 404 for the domain. The rung stays unverified because the offer text (free use, UDP and TCP forwarding, one server at a time) comes from a search-index copy of the vendor page, and the page itself cannot be read while the domain is unregistered.
- extras:
  - wg_path: unknown
  - wg_detail: The surviving copy claims UDP forwarding, which would carry WireGuard, but the site never loaded.
  - ingress: tcp+udp
  - volume_stated: No byte allowance appears in the copy preserved in the search index; the page itself could not be read.
  - bytes_transit: yes
  - transit_note: The vendor's servers were to sit between the home network and the players.
  - death.on: 2026-10-30
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-23: 
  - [1] 2026-10-23: The search index still holds copy dated this week: 'PCDeploy works for any game with self-hosted community servers ... It works for both UDP and TCP connections' and 'Right now, only one server can be run at a time.'
  - [1] 2026-10-23: The Wayback Machine returned no capture at 2026-06 and Cloudflare URL Scanner held no scan in its last 30 days
  - probe:https://8.8.8.8/resolve?name=pcdeploy.net&type=A 2026-10-30: a DNS-over-HTTPS query to 8.8.8.8 for the A record of pcdeploy.net answered Status 3 (NXDOMAIN) on 2026-10-30, with the .net zone SOA as the authority | capture: sha256:b38f1c565eafee25652ea392b64a22119df0d1aaa853db12e63a6f719f2c49ec | quote: "Status":3
  - probe:https://1.1.1.1/dns-query?name=pcdeploy.net&type=A 2026-10-30: a DNS-over-HTTPS query to 1.1.1.1 for the A record of pcdeploy.net answered Status 3 (NXDOMAIN) on 2026-10-30, with the .net zone SOA as the authority | capture: sha256:7d4e072889aa4d63efd22f2e31974b5c9f1c7dc6b4d3aaf62f72c8646ecce7b2 | quote: "Status":3
  - probe:https://rdap.verisign.com/net/v1/domain/pcdeploy.net 2026-10-30: the .net registry's RDAP service answered HTTP 404 with a 0-byte body for the domain pcdeploy.net on 2026-10-30: the registry holds no registration for the name | capture: sha256:9fc056fd23f7c438e880a7d19cd21601c5ecbf4861c5199df1c43f6e1104bfae | quote: "status": 404
  - probe:https://8.8.8.8/resolve?name=pcdeploy.net&type=A 2026-11-03: a public DNS-over-HTTPS resolver answered DNS status 3 (NXDOMAIN) for the A record of pcdeploy.net on 2026-11-03, with the .net zone SOA as the authority | capture: sha256:82cde158871b64cad76e6e71fe9f047a4299cd148862b0f86344056344e98ff1 | quote: "Status":3
  - probe:https://1.1.1.1/dns-query?name=pcdeploy.net&type=A 2026-11-03: a second public DNS-over-HTTPS resolver also answered DNS status 3 (NXDOMAIN) for pcdeploy.net on 2026-11-03 | capture: sha256:38447c5b4dd2fb9123867fc26550ecc714ef57993f63cbef6f8a927658623611 | quote: "Status":3
  - probe:https://rdap.verisign.com/net/v1/domain/pcdeploy.net 2026-11-03: the .net registry RDAP service answered HTTP 404 for pcdeploy.net on 2026-11-03: the registry holds no registration for the name | capture: sha256:084907c9b18593a85fbfe7208b56d362c913216da271defba3be6279cd887a40 | quote: "status": 404
- sources:
  - [1] https://pcdeploy.net/
