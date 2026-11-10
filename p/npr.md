# NPR One API

> npr.org | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/npr/ | JSON https://fshy.ajam.dev/api/v1/entity/npr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NPR One API (NPR Developer Center)

- `data-apis/npr-one` | fails-identity | evidence reported | binding write-gated | category audio and news content API | tier Developer account (closed to new accounts)
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-11-18
- url https://dev.npr.org/
- free tier: none reachable: the developer center said it was not accepting new login accounts, and its host no longer resolves. | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: The legacy Story API is retired. Its successor, the Content Distribution Service, gives a key to member stations through NPR member partnership; no self-serve key is described.
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not assessed: no account can be opened to read content | metered: no | source: [1]
- identity: institution | detail: New developer logins were closed on the last copy of the developer center read; the successor service names member stations as its key holders.
- interface: rest
- limits:
  - write-gated (binding): new developer accounts are closed; a Content Distribution Service key goes to member stations through member partnership [1]
- binding note: No new account can be opened, so no rate or quota is reachable.
- interface detail: REST over HTTPS at listening.api.npr.org, identity.api.npr.org and authorization.api.npr.org, with an OAuth bearer token from the authorization service
- endpoint: https://listening.api.npr.org/v2/recommendations
- tooling: any HTTP client; NPR published a JavaScript SDK and a PHP backend proxy for token handling
- composes with: Audio recommendations and listening data for NPR One apps; the news text route is the Content Distribution Service, for member stations.
- reliability: The developer center host dev.npr.org failed DNS on 2026-11-03; the API hosts still answer HTTP 401 without a token; the Story API is retired.
- notes: Storage: no storage term was readable because the developer center host does not resolve. Bulk path: none found.
- evidence note: The closed-registration notice is read from an archived copy of the developer center dated 2024-07-14, and the host no longer resolves, so the present state of registration is inferred; the API hosts answering 401 shows the service is up for existing holders.
- evidence:
  - [2] 2026-11-02: the developer center was not accepting new login accounts (archived copy dated 2024-07-14) | capture: sha256:2ad4639e905174566641fe9967d1e361856fecec3f07828c64a4f201c0363020 | quote: We are currently not accepting new login accounts, but existing users can continue to access this service.
  - probe:https://dev.npr.org/ 2026-11-03: the developer center host failed DNS | capture: sha256:60507351394fc1e8624e6e229a1f0d8f8247987441aa5104ff9cea959265d279 | quote: "error": "dns"
  - probe:https://listening.api.npr.org/v2/recommendations 2026-11-03: the listening API host answers HTTP 401 without a token | capture: sha256:9ecdf9b7337b5af72b9a1b5bb4f792ecc6fe370792dd1801cc5f8e92c6264fcc | quote: "status": 401
  - [3] 2026-11-02: the Story API is retired | capture: sha256:d5bee0e1f1b81f16d603e78b278a80392196b4eb576ab60ad06cfc6f4bb08358 | quote: After over 15 years of service, Story API is retiring! As a result, we are no longer supporting this page.
  - [4] 2026-11-02: the successor service gives keys to member stations through member partnership | capture: sha256:23b4f0d37a824ccb53de4a10e1c0ddc6ffb479fbb0b488e996c51255d8d48424 | quote: If you are a Member Station and need a CDS key, reach out to [Member Partnership](https://studio.npr.org/s/support-home).
- sources:
  - [1] https://dev.npr.org/
  - [2] https://web.archive.org/web/20240714235112/http://dev.npr.org/
  - [3] https://legacy.npr.org/api/index
  - [4] https://npr.github.io/content-distribution-service/getting-started.html
