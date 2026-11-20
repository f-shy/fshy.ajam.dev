# Netmaker

> netmaker.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netmaker/ | JSON https://fshy.ajam.dev/api/v1/entity/netmaker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Netmaker

- `egress/netmaker` | self-hosted, last resort | verdict fails-egress | evidence documented | binding request-rate | category WireGuard management (private only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.netmaker.io/pricing
- price USD 0
- free tier: Community: 'Free', '1 Netmaker Server', '3 users', '10 nodes', '10 external clients', '2 Networks'. | unit: users | metered on: identity-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance in any plan; the plans count users, nodes, clients and networks.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: A Netmaker account is required for the hosted console. The Community plan operates on self-hosted infrastructure. | country: None
- interface: cli
- limits:
  - request-rate (binding): The 3-user and 10-node caps are the published meters and the vocabulary has no token for a count; request-rate is the nearest. No byte meter exists and nothing listens publicly. [1]
- binding note: The 3-user and 10-node caps are the published meters and the vocabulary has no token for a count; request-rate is the nearest. No byte meter exists and nothing listens publicly.
- interface detail: netclient join, plus the console
- tooling: netclient, netmaker server, Kubernetes operator
- composes with: the mesh half of a two-part chain; it needs Caddy, Traefik or Pangolin on a public host to finish the job
- reliability: the public-facing half of any deployment is a reverse proxy the operator runs, not a Netmaker feature
- notes: WireGuard mesh overlay platform. Ingress Proxy forwards traffic between Netmaker mesh nodes; exposing services to the public internet requires deploying external reverse proxies.
- self hosted: yes
- extras:
  - wg_path: unknown
  - wg_detail: The free plan counts '10 external clients', which is the slot where WireGuard configs are handed out, but no page read states that a .conf is issued, so the export path stays unproven.
  - ingress: none
  - volume_stated: No byte allowance in any plan; the plans count users, nodes, clients and networks.
  - bytes_transit: unknown
  - transit_note: WireGuard peer to peer where possible, with Relay fallback for nodes that cannot connect directly
- evidence:
  - [1] 2026-10-23: Community is Free with 1 server, 3 users, 10 nodes, 10 external clients and 2 networks
  - [2] 2026-10-23: publishing publicly needs a third component: 'deploy a reverse proxy server in the cloud', 'deploy a Netmaker node on that server', and then 'your service will now be accessible to the internet', read through the search index
  - [3] 2026-10-23: Netmaker's own 'Cluster Ingress' is internal: 'Expose Kubernetes services to devices on your Netmaker network'
- sources:
  - [1] https://www.netmaker.io/pricing
  - [2] https://learn.netmaker.io/how-to-guides/how-to-use-netmaker-with-a-reverse-proxy
  - [3] https://docs.netmaker.io/docs/features/k8s-operator
