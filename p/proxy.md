# pgrok

> proxy.jetzt | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxy/ | JSON https://fshy.ajam.dev/api/v1/entity/proxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pgrok (proxy.jetzt)

- `egress/pgrok-fork` | dead | evidence documented | binding none | category http/tcp tunnel (archived ngrok 1.0 fork) | tier dead
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.proxy.jetzt/
- price USD 0
- free tier: Free Introspected tunnels to localhost, like ngrok but free and unlimited | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'free and unlimited' in the repository description; the host serving it is a GitHub mirror, not a live relay.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no signup described; the project is archived. | country: None
- interface: cli
- binding note: Nothing binds because the relay is not operating: the page is the archived repository README and the aggregator marks it archived.
- interface detail: ngrok 1.0 style client.
- tooling: archived binary.
- composes with: none
- reliability: Archived upstream; no relay observed.
- notes: Self-hosted reverse proxy fork. Public relay endpoint proxy.jetzt was discontinued and redirects to the source repository.
- evidence note: Public demo relay is discontinued; source repository remains available for self-hosting.
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: 'free and unlimited' in the repository description; the host serving it is a GitHub mirror, not a live relay.
  - bytes_transit: no
  - transit_note: none observed
- evidence:
  - [1] 2026-10-23: page serves the jerson/pgrok GitHub README: 'Free Introspected tunnels to localhost, like ngrok but free and unlimited'; 'Expose any tcp service ... on a random port of ejemplo.me'
- sources:
  - [1] https://www.proxy.jetzt/
