# The Vibe Hosting

> thevibehosting.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thevibehosting/ | JSON https://fshy.ajam.dev/api/v1/entity/thevibehosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## The Vibe Hosting

- `compute/the-vibe-hosting` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox
- needs card no, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://thevibehosting.com/
- free tier: A root Ubuntu container on an HTTPS subdomain, created by one unauthenticated POST. Quoted: 'no signup, no API key to configure'; 'Runs a 256 MB RAM server 24/7 all month - free' without a phone; with a verified phone 'Runs a 512 MB RAM server 24/7 all month - free' plus '$2.25/mo free credit', '2 GB RAM ceiling / server', 'unlimited servers'. Past the credit: 'RAM $0.005 / GB-hour (awake only) - Egress $0.10 / GB - Disk $0.25 / GB-month - CPU free'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Each project runs in a gVisor-sandboxed container with hard CPU/RAM limits' and 'Outbound SMTP is blocked and abuse is suspended', quoted | metered: yes | source: [1]
- identity: anonymous | detail: nothing: the page states 'No signup, no API key to configure, no MCP to install', and an api_key 'is issued automatically on the first POST /create call', so the 256 MB always-on server needs no account at all. A verified phone is optional and raises the allowance to 512 MB and the free credit to $2.25 a month. Because the creation step takes no account, it takes no card, no hold and no ID document either; paid credit is the only place a payment method could enter, and its rails are not stated.
- interface: ssh, rest
- limits:
  - volume-quota (binding): the free credit is a monthly USD allowance (0.90 anonymous, 2.25 with a phone), so disk at USD 0.25 per GB-month exhausts it first: 3.6 GB of disk alone consumes the phone-verified allowance. [1]
- limits note: the free credit is a monthly USD allowance (0.90 anonymous, 2.25 with a phone), so disk at USD 0.25 per GB-month exhausts it first: 3.6 GB of disk alone consumes the phone-verified allowance.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the box is reachable with no account at all, so it can host the always-on piece, a cron worker or an SSH rendezvous that a scale-to-zero free tier cannot; the api_key issued on the first call is the only credential to keep.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says '2-core, 512 MB server 24/7 with a verified phone'. The vendor publishes no core count and bills CPU as free, so '2-core' is the aggregator's figure, not the vendor's, and is not recorded here. The anonymous 256 MB tier is the more interesting half and the aggregator omits it. Two servers per IP is the anonymous ceiling. Operating history is unknown: this is a young single-operator service and no suspension report was found, so an operator that keeps prepaid credit is an open risk, not an observed event.
- extras:
  - facets.class: new-provider
  - facets.free_tier_kind: recurring-credit
  - facets.shape.ram_gib: 0.5
- evidence:
  - [1] 2026-10-22: 'No signup, no API key to configure, no MCP to install. You get root in seconds and an api_key (vibe_...) is issued automatically on the first POST /create call', quoted
  - [1] 2026-10-22: price table: '512 MB RAM $0/mo gross $1.80 - free credit', '1 GB RAM $1.35/mo', '2 GB RAM $4.95/mo', '4 GB RAM $12.15/mo', quoted
  - [1] 2026-10-22: 'A verified phone raises it to $2.25/month, up to 2 GB RAM (4 GB with paid credit), always-on servers and your own domains', quoted
  - [1] 2026-10-22: 'Each project runs in a gVisor-sandboxed container with hard CPU/RAM limits' and 'Outbound SMTP is blocked and abuse is suspended', quoted
- sources:
  - [1] https://thevibehosting.com/
