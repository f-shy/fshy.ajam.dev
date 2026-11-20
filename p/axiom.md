# Axiom

> axiom.co | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/axiom/ | JSON https://fshy.ajam.dev/api/v1/entity/axiom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Axiom

- `dev-services/axiom` | qualifies-with-caveat | evidence documented | binding volume-quota | category log, event and trace store queried with APL | tier Personal
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:37:34.243Z (live) | stale on 2026-12-03
- url https://axiom.co/pricing
- free tier: Personal, USD 0/month, permanent, no credit card: 500 GB/mo data loading compute, 10 GB-hours query compute, 25 GB storage, 30-day retention, full APL access, all integrations; 3 datasets, 256 fields per dataset, 1 user, 3 monitors, US edge only | unit: GB | metered on: uploaded-bytes | read on: 2026-10-30 | source: [1] | note: 500 GB a month is both the free allowance and the maximum data loading on Personal. One GB-hour of query compute is roughly the cost of scanning 1 GB with moderate complexity. Axiom Cloud, the paid plan, is USD 25/month plus usage and includes 1,000 GB of loading, 100 GB-hours of query and 100 GB of storage.
- per-object cap: 1 MB per field, 200 bytes per field name, at most 10,000 events per ingest batch; 256 fields per dataset on Personal | source: [2] | note: The cap is per field, not per event, and applies on every plan.
- retention: Maximum data retention 30 days on Personal | days: 30 | source: [2]
- egress: All plans include unlimited bandwidth and API access, per the limits page; reading data back is paid in query compute, 10 GB-hours a month on Personal | metered: no | source: [2]
- identity: email | detail: The sign-in page creates an account on the first sign-in and e-mails a login link; the pricing page states Personal needs no credit card, and Axiom's Terraform page states that all a free account needs is an e-mail address. A public endpoint also creates a temporary organization with no sign-in: it is deleted with its data after 24 hours unless a person claims it, and claiming it creates an account when none exists.
- interface: rest
- limits:
  - volume-quota (binding): 10 GB-hours of query compute a month [2]
  - volume-quota (binding): 500 GB / month data loading, also the maximum on Personal [2]
  - volume-quota (binding): 25 GB storage; 3 datasets; 1 user [2]
  - retention-clamped: 30 days maximum retention [2]
  - per-object-cap: 1 MB per field; 10,000 events per batch [2]
- binding note: 10 GB-hours of query compute is roughly 10 GB scanned a month, against 500 GB that can be loaded, so querying runs out long before ingest.
- interface detail: REST API with JSON bodies: ingest and query at the edge deployment's base domain (us-east-1.aws.edge.axiom.co for the US edge, the only edge Personal supports), every other endpoint at https://api.axiom.co, authorised with an API token or a personal access token. api.axiom.co answered 401 to /v2/datasets without a token. OpenTelemetry data is accepted as OTLP over HTTP at https://AXIOM_DOMAIN/v1/traces, /v1/logs and /v1/metrics, where AXIOM_DOMAIN is the base domain of the edge deployment; the metrics endpoint takes Protobuf or JSON.
- endpoint: part of interface detail
- tooling: curl or any HTTP client with a Bearer token, and OpenTelemetry exporters
- composes with: A 30-day searchable store for the logs of free compute services, up to 500 GB loaded a month, with only about 10 GB of it scanned by queries a month.
- reliability: An event that would exceed a dataset's field limit is rejected with an error; strings over the field size are replaced with a placeholder.
- notes: 500 GB a month of free ingest, against 100 GB on New Relic's free tier and 3 GB on Better Stack's, held back by a 10 GB-hour query budget and 25 GB of storage.
- evidence note: Every limit is quoted from a first-party page, and the API host answered 401 without a token. No account was opened; an authenticated ingest and query from a Personal account would move it to measured.
- evidence:
  - [1] 2026-10-30: Personal is permanent and needs no credit card | capture: sha256:61291fd03870a9bbaf215ae35fe5b5a044a9174efe014aa14889ac1e8a48b75c | quote: Permanent. No credit card required.
  - [1] 2026-10-30: Personal includes 500 GB a month of data loading | capture: sha256:61291fd03870a9bbaf215ae35fe5b5a044a9174efe014aa14889ac1e8a48b75c | quote: 500 GB/mo data loading compute
  - [1] 2026-10-30: Personal includes 10 GB-hours of query compute | capture: sha256:61291fd03870a9bbaf215ae35fe5b5a044a9174efe014aa14889ac1e8a48b75c | quote: 10 GB-hours query compute
  - [1] 2026-10-30: Personal keeps data 30 days | capture: sha256:61291fd03870a9bbaf215ae35fe5b5a044a9174efe014aa14889ac1e8a48b75c | quote: 30-day retention
  - [2] 2026-10-30: Personal has 25 GB of free storage against 100 GB on Axiom Cloud | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Always Free storage | 25 GB | 100 GB |
  - [2] 2026-10-30: Personal has 10 GB-hours of query compute a month | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Always Free query compute | 10 GB-hours / month | 100 GB-hours / month |
  - [2] 2026-10-30: 500 GB a month is the maximum data loading on Personal | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Maximum data loading | 500 GB / month | – |
  - [2] 2026-10-30: retention is at most 30 days on Personal | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Maximum data retention | 30 days | Custom |
  - [2] 2026-10-30: Personal allows 3 datasets | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | [Datasets](https://axiom.co/docs/reference/datasets) | 3 | 100 * |
  - [2] 2026-10-30: Personal allows 256 fields per dataset | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Fields per dataset | 256 | 1,024 * |
  - [2] 2026-10-30: Personal allows 1 user | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Users | 1 | 1,000 * |
  - [2] 2026-10-30: Personal allows 3 monitors | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | [Monitors](https://axiom.co/docs/monitor-data/monitors) | 3 | 500 * |
  - [2] 2026-10-30: Personal supports the US edge only | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | [Supported edge deployments](https://axiom.co/docs/reference/edge-deployments) | US | US |
  - [2] 2026-10-30: all plans include unlimited bandwidth and API access | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: All plans include unlimited bandwidth, API access, and data sources
  - [2] 2026-10-30: a field is at most 1 MB | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Maximum field size | 1 MB |
  - [2] 2026-10-30: a batch holds at most 10,000 events | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Maximum events in a batch | 10,000 |
  - [2] 2026-10-30: a field name is at most 200 bytes | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Maximum field name length | 200 bytes |
  - [2] 2026-10-30: an event over the field limit is rejected | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: If you ingest a new event that would exceed the allowed number of fields in a dataset, Axiom returns an error and rejects the event.
  - [2] 2026-10-30: oversize strings are replaced with a placeholder | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: Replaces strings that are too long with `<invalid string: too long>`.
  - [2] 2026-10-30: OpenTelemetry metrics are sent to a /v1/metrics endpoint | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: to the `/v1/metrics` endpoint
  - [3] 2026-10-30: one GB-hour is roughly scanning 1 GB | capture: sha256:44a3cf26981ebcf414a5f7fb28e8a800419115b58fb810b8dbd16f2c827862f4 | quote: One GB-hour is roughly equivalent to scanning 1 GB of data with moderate complexity.
  - [3] 2026-10-30: Axiom Cloud has a USD 25 monthly platform fee | capture: sha256:44a3cf26981ebcf414a5f7fb28e8a800419115b58fb810b8dbd16f2c827862f4 | quote: Every Axiom Cloud organization pays a platform fee of $25 per month, which includes free allowances for light usage.
  - [2] 2026-10-30: Axiom Cloud includes 1,000 GB of loading and 100 GB-hours of query a month | capture: sha256:d355c2d953e49c603ea098d0340442079793cb88b2ae1297a50a52173172cdd6 | quote: | Always Free data loading | 500 GB / month | 1,000 GB / month |
  - [4] 2026-10-30: the first sign-in creates the account and e-mails a login link | capture: sha256:5be870718e68d192940fe492708d832ec1d842afc2d1eb7a590edc76cab27dc1 | quote: New to Axiom? Just sign in. We'll create your account and email you a login link.
  - [5] 2026-10-30: the API is REST with JSON | capture: sha256:9491a9b89bb46c25108e90dbc0a27cbe4bf006e1935c483741d696f81ca2b27a | quote: Axiom API follows the REST architectural style and uses JSON for serialization.
  - [5] 2026-10-30: the US edge's base domain for ingest and query | capture: sha256:9491a9b89bb46c25108e90dbc0a27cbe4bf006e1935c483741d696f81ca2b27a | quote: | `US East 1 (AWS)` | `us-east-1.aws.edge.axiom.co` |
  - probe:https://api.axiom.co/v2/datasets 2026-10-31: the API host answers 401 without a token | capture: sha256:54729776f4590f58b0e85d3779936bc8e6031d99379930187c583ea53c950985 | quote: "status": 401
  - [6] 2026-11-01: an unclaimed temporary organization is deleted with its data after 24 hours | capture: sha256:c01d3f41dd24095b192cadefa02eadd8aaa441aa0dc163ec5238327e0632c59b | quote: If nobody claims the organization within 24 hours, Axiom permanently deletes it together with all its data.
  - [7] 2026-11-01: the OTLP metrics endpoint takes Protobuf or JSON | capture: sha256:0b8e237f8c23869bddc156e7441a595da00027e36f22f2ada55dca301a6cdf67 | quote: The `/v1/metrics` endpoint accepts OTLP data encoded as Protobuf (`application/x-protobuf`) or JSON (`application/json`).
  - [6] 2026-11-01: the endpoint that creates a temporary organization needs no authentication | capture: sha256:c01d3f41dd24095b192cadefa02eadd8aaa441aa0dc163ec5238327e0632c59b | quote: The endpoint is public: no authentication header is required.
  - [6] 2026-11-01: claiming a temporary organization creates an account when the person has none | capture: sha256:c01d3f41dd24095b192cadefa02eadd8aaa441aa0dc163ec5238327e0632c59b | quote: If you don’t have an Axiom account yet, one is created as part of the flow.
  - [7] 2026-11-01: OTLP/HTTP traces go to /v1/traces on the edge deployment's base domain | capture: sha256:0b8e237f8c23869bddc156e7441a595da00027e36f22f2ada55dca301a6cdf67 | quote: Traces: `https://AXIOM_DOMAIN/v1/traces`
  - [7] 2026-11-01: OTLP/HTTP logs go to /v1/logs on the edge deployment's base domain | capture: sha256:0b8e237f8c23869bddc156e7441a595da00027e36f22f2ada55dca301a6cdf67 | quote: Logs: `https://AXIOM_DOMAIN/v1/logs`
  - [8] 2026-11-01: a free Axiom account needs only an e-mail address to sign up | capture: sha256:9eb2f2d6a15a21552e9b82cfd3da24a120765d2adb7750e26f85aa8b1555d35a | quote: Sign up for a free Axiom account. All you need is an email address.
- sources:
  - [1] https://axiom.co/pricing
  - [2] https://axiom.co/docs/reference/limits
  - [3] https://axiom.co/pricing/llms.txt
  - [4] https://app.axiom.co/register
  - [5] https://axiom.co/docs/restapi/introduction
  - [6] https://axiom.co/docs/console/intelligence/agent-created-orgs
  - [7] https://axiom.co/docs/send-data/opentelemetry
  - [8] https://axiom.co/docs/apps/terraform
