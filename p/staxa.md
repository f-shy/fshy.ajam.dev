# Staxa

> staxa.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/staxa/ | JSON https://fshy.ajam.dev/api/v1/entity/staxa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Staxa

- `compute/staxa` | qualifies-with-caveat | evidence documented | binding per-object-cap | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:58.527Z (live) | stale on 2026-12-05
- url https://staxa.dev/
- free tier: Free plan is a sandbox: '$0 - Tenants included 2 - Services per tenant 2 - Sizes Small - Concurrent builds 1 - Private registries 0 - Network rules per tenant 0 - Custom domains No - Extra tenant USD 5/mo'. Paid plans start at 'USD 49/month'. A tenant is an app, a database, a subdomain and TLS in its own Kubernetes namespace. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): each tenant is one 'Small' tier, which the API documentation's example payload puts at a 500m CPU limit, 512Mi memory limit and 5Gi storage, and the free plan allows two of them with no custom domains. [1]
- limits note: each tenant is one 'Small' tier, which the API documentation's example payload puts at a 500m CPU limit, 512Mi memory limit and 5Gi storage, and the free plan allows two of them with no custom domains.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: two isolated namespaces, each with its own database and TLS, is enough to run a staging and a production copy of one small service, which most free tiers refuse to give as two separate environments.
- reliability: no reliability event recorded
- notes: Routes tried: read /pricing (login wall), archive /pricing at 2026-09 (no capture; Wayback and Cloudflare scan both empty), search on the site name, which returned the pricing table text verbatim. The free tier numbers are quoted from the indexed text of the vendor page, not from a live render. Tier sizes are not published as a table; the 500m / 512Mi / 5Gi shape comes from the API documentation's example payload and is indicative.
- extras:
  - facets.class: new-provider
  - facets.free_tier_kind: free-forever
  - facets.shape.vcpu: 0.5
  - facets.shape.ram_gib: 0.5
- evidence:
  - [1] 2026-10-22: pricing table text returned by the search index for the site: 'Free ... $0 Sandbox plan - Tenants included 2 - Services per tenant 2 - Sizes Small - Concurrent builds 1 ... Custom domains No ... Extra tenant $5/mo', quoted
  - [1] 2026-10-22: 'The Free plan includes 2 tenants. Paid plans from $49/month.', quoted
  - [2] 2026-10-22: 'resource_size: Resource tier: small, medium, large' with default 'small'; the documented tenant payload shows cpu_limit '500m', memory_limit '512Mi', storage_limit '5Gi' for a small tenant
  - [1] 2026-11-03: REST API and dashboard on every plan | capture: sha256:20865f563b549173eb3836def9035e1eeac2f1d5ba227aa14c24790438a1c8df | quote: Every plan includes namespace isolation, the dashboard and the full REST API.
  - [2] 2026-11-03: the API docs publish a REST API with bearer API keys; the docs state an egress_mode setting but no egress allowance or price | capture: sha256:ab150be429263589ee0b7b093e9207a2b4ce96efe4d62334db716afdb0b08ab9 | quote: Everything the dashboard does is an HTTP call you can make yourself. Authenticate with an API key as a bearer token.
- sources:
  - [1] https://staxa.dev/
  - [2] https://staxa.dev/docs
