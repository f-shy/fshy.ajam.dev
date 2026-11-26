# IndiShare

> indishare.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/indishare/ | JSON https://fshy.ajam.dev/api/v1/entity/indishare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IndiShare

- `debrid/indishare` | dead | evidence documented | binding none | category former file host, now dead | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:43.323Z (live) | stale on 2026-12-26
- url https://indishare.org/
- free tier: Not applicable: no service is served. indishare.org is an expired domain whose page says 'This domain is expired. If you are the domain owner please click here to renew it.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
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
- reliability: Two hostnames, two failures: an expired-domain notice on .org, and a 401 from a parked redirect on .me. The name circulates in host lists and in debrid broker manifests, so a client may still see it offered.
- evidence note: Both hostnames were fetched and the artefacts are quoted in the evidence rows. The record does not claim when it died, only that it was dead when read.
- extras:
  - failure_modes_seen: origin 523 on .org; ad-park redirect on .me
  - death.on: 2026-11-25
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-23: the origin answered HTTP 523 (Cloudflare could not reach the origin server), so no site was served
  - [2] 2026-10-23: the .me hostname redirected to http://ww547.indishare.me/?tkn=... and served a keyword-ad landing page ('Who Has The Best Car Insurance', 'Find Low Cost Car Insurance Now'), the classic domain-squat footprint
  - [1] 2026-11-25: the indishare.org domain has expired and serves a registrar notice instead of a host service | capture: sha256:edd2a899fe4c89456915a7798ea8d28f558b74babe9dcdae71d6dc08bc19fd11 | quote: This domain is expired. If you are the domain owner please click here to renew it.
  - [1] 2026-11-25: no service is offered under the indishare.org name | capture: sha256:edd2a899fe4c89456915a7798ea8d28f558b74babe9dcdae71d6dc08bc19fd11 | quote: This domain is expired. If you are the domain owner please click here to renew it.
  - probe:https://indishare.me/ 2026-11-25: the .me hostname redirects to a parked page that answers 401 | capture: sha256:7ceadaf98e2df280917c7cae105bc4b9d34c91c3836391c794ae405e23e91bc7 | quote: "status": 401,
  - [1] 2026-11-25: the host is an expired domain with no service | capture: sha256:edd2a899fe4c89456915a7798ea8d28f558b74babe9dcdae71d6dc08bc19fd11 | quote: This domain is expired. If you are the domain owner please click here to renew it.
- sources:
  - [1] https://indishare.org/
  - [2] https://indishare.me/
