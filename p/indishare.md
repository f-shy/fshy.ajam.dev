# IndiShare

> indishare.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/indishare/ | JSON https://fshy.ajam.dev/api/v1/entity/indishare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IndiShare

- `debrid/indishare` | dead | evidence documented | binding none | category former file host, now dead | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:39:12.321Z (live) | stale on 2026-11-23
- url https://indishare.org/
- free tier: Not applicable: no service is served. indishare.org answers a Cloudflare 523 at the origin and indishare.me serves a keyword-advert landing page. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: Not applicable. | source: [1]
- retention: The free 15-day retention the brand was known for is gone with the host; nothing is stored. | source: [1]
- egress: None. | metered: no | source: [1]
- identity: anonymous | detail: No registration surface exists to price.
- interface: unknown
- limits note: No constraint applies.
- binding note: Nothing transfers.
- interface detail: No service to reach. The .me hostname returns a redirect to ww547.indishare.me, an ad page whose only links are keyword campaigns.
- tooling: Nothing to tool against.
- composes with: An Indian PPD host that index posts used, and that no longer resolves to a working upload or download path. Any surviving link to it is a dead link, not a retrieval path.
- reliability: Two hostnames, two failures: 523 at the origin on .org, and a parked keyword-ad page on .me. The name circulates in host lists and in debrid broker manifests, so a client may still see it offered.
- evidence note: Both hostnames were fetched and the artefacts are quoted in the evidence rows. The record does not claim when it died, only that it was dead when read.
- extras:
  - failure_modes_seen: origin 523 on .org; ad-park redirect on .me
- evidence:
  - [1] 2026-10-23: the origin answered HTTP 523 (Cloudflare could not reach the origin server), so no site was served
  - [2] 2026-10-23: the .me hostname redirected to http://ww547.indishare.me/?tkn=... and served a keyword-ad landing page ('Who Has The Best Car Insurance', 'Find Low Cost Car Insurance Now'), the classic domain-squat footprint
- sources:
  - [1] https://indishare.org/
  - [2] https://indishare.me/
