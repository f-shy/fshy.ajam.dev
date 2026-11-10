# HDX

> humdata.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/humdata/ | JSON https://fshy.ajam.dev/api/v1/entity/humdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HDX — Humanitarian Data Exchange (UN OCHA)

- `storage/hdx-humanitarian-data-exchange` | qualifies-with-caveat | evidence reported | binding write-gated | category gov-igo-data-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.humdata.org/
- free tier: No published per-user or per-file quota anywhere in the docs. The platform hosts the files itself ('upload the data file directly to the HDX platform'), S3-backed. Aggregate catalog is 28,359 datasets and growing at organisational pace. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered public download. Direct GET on /dataset/<slug>/resource/<id>/download/<file>; no egress counter, no rate card, no CDN token. Files are anonymous to read. No login to download. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - write-gated (binding): reviewed by OCHA [1]
  - write-gated (binding): approval, not identity or payment [1]
- limits note: write-gated: you must belong to an HDX organisation with publishing rights. Any registered user may REQUEST a new organisation (`/org/request/new`) and the request is human-reviewed by OCHA. So the gate is editorial approval, not identity or payment.
- interface detail: CKAN 2.x action API (package_search / package_create / resource_create) plus the `hdx-python-api` wrapper, which is the documented write path.
- tooling: curl + API token, or `pip install hdx-python-api`. Write operations need an API token from the user profile; token is per-user, free, issued on signup.
- composes with: CKAN resource_create accepts a URL as well as a local file, so HDX can act as a metadata+mirror layer over another host. Public download URLs are stable and content-addressable by resource id. Reasonable as a serving tier.
- reliability: UN-operated, 10+ years of uptime, but editorial review means a rejection is silent and unbounded. No SLA on org approval, and an org can be removed for content outside humanitarian scope. Do not treat as primary durable storage.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'Only registered users can request to create a new organization. Open: https://data.humdata.org/org/request/new. If you are not logged in, you will see an error page.'
  - [1] 2026-10-21: 'To publish manually, you will need to upload the data file directly to the HDX platform... you must be logged in and belong to an HDX organization with publishing permissions.'
  - [3] 2026-10-21: HTTP 200, success:true, count 28359, i.e. the CKAN write API family is live on the same host
  - [4] 2026-10-21: 'Your organization must exist on HDX, and you need to be an editor or admin of it' — confirms programmatic publish is real, not UI-only
- sources:
  - [1] https://docs.humdata.org/publish/publish-data/preparing-and-publishing-data
  - [2] https://docs.humdata.org/publish/publish-data/organizations-on-hdx
  - [3] https://data.humdata.org/api/3/action/package_search?rows=0
  - [4] https://docs.humdata.org/build/hdx-python-library
