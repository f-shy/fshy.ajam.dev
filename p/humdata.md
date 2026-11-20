# HDX

> humdata.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/humdata/ | JSON https://fshy.ajam.dev/api/v1/entity/humdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HDX — Humanitarian Data Exchange (UN OCHA)

- `storage/hdx-humanitarian-data-exchange` | qualifies-with-caveat | evidence reported | binding write-gated | category gov-igo-data-portal
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:18.129Z (live) | stale on 2026-11-25
- url https://data.humdata.org/
- free tier: No published per-user or per-file quota anywhere in the docs. The platform hosts the files itself ('upload the data file directly to the HDX platform'), S3-backed. Aggregate catalog is 28,359 datasets and growing at organisational pace. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: If you are uploading a file onto HDX we recommend that you keep file size to under 300MB. | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered public download. Direct GET on /dataset/<slug>/resource/<id>/download/<file>; no egress counter, no rate card, no CDN token. Files are anonymous to read. No login to download. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - write-gated (binding): All organizations are vetted by the HDX team to ensure they are trusted sources of relevant data. [2]
  - write-gated (binding): approval, not identity or payment [1]
- limits note: write-gated: you must belong to an HDX organisation with publishing rights. Any registered user may REQUEST a new organisation (`/org/request/new`) and the request is human-reviewed by OCHA. So the gate is editorial approval, not identity or payment.
- interface detail: CKAN 2.x action API (package_search / package_create / resource_create) plus the `hdx-python-api` wrapper, which is the documented write path.
- tooling: curl + API token, or `pip install hdx-python-api`. Write operations need an API token from the user profile; token is per-user, free, issued on signup.
- composes with: CKAN resource_create accepts a URL as well as a local file, so HDX can act as a metadata+mirror layer over another host. Public download URLs are stable and content-addressable by resource id. Reasonable as a serving tier.
- reliability: UN-operated, 10+ years of uptime, but editorial review means a rejection is silent and unbounded. No SLA on org approval, and an org can be removed for content outside humanitarian scope. Do not treat as primary durable storage.
- notes: the same as the free tier
- evidence note: If you are uploading a file onto HDX we recommend that you keep file size to under 300MB.
- evidence:
  - [2] 2026-10-21: 'Only registered users can request to create a new organization. Open: https://data.humdata.org/org/request/new. If you are not logged in, you will see an error page.'
  - [1] 2026-10-21: 'To publish manually, you will need to upload the data file directly to the HDX platform... you must be logged in and belong to an HDX organization with publishing permissions.'
  - [3] 2026-10-21: HTTP 200, success:true, count 28359, i.e. the CKAN write API family is live on the same host
  - [4] 2026-10-21: 'Your organization must exist on HDX, and you need to be an editor or admin of it' — confirms programmatic publish is real, not UI-only
  - [1] 2026-11-09: The publishing page states the size guidance this record relies on. | capture: sha256:8ef02ac622a8473ec2256b6a602c4672e13edbc56946601ce78f726bed945d1d | quote: If you are uploading a file onto HDX we recommend that you keep file size to under 300MB.
  - [2] 2026-11-09: The organizations page states that the HDX team vets every organization. | capture: sha256:c7a0081b0a3bdf73f76b6f326c5a4c4c0abd1f1e0f18c42e345fd7250886b8e0 | quote: All organizations are vetted by the HDX team to ensure they are trusted sources of relevant data.
  - [3] 2026-11-09: the package_search endpoint reports a catalog count of 30,039 | capture: sha256:e42f200b0adf19e2da4c28e2886fda9051fd949fd2726ca32114557b9acad475 | quote: "count": 30039
  - [2] 2026-11-09: the page states the confirmed value | capture: sha256:c7a0081b0a3bdf73f76b6f326c5a4c4c0abd1f1e0f18c42e345fd7250886b8e0 | quote: If they are already registered on HDX, they will be added immediately. If not, they will receive an email invitation.
- sources:
  - [1] https://docs.humdata.org/publish/publish-data/preparing-and-publishing-data
  - [2] https://docs.humdata.org/publish/publish-data/organizations-on-hdx
  - [3] https://data.humdata.org/api/3/action/package_search?rows=0
  - [4] https://docs.humdata.org/build/hdx-python-library
