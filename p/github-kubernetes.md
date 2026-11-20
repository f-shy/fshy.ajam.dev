# microsoft mcr

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-kubernetes/ | JSON https://fshy.ajam.dev/api/v1/entity/github-kubernetes.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## microsoft mcr / registry.k8s.io / icr.io / docker.elastic.co / registry.ope

- `storage/microsoft-mcr-registry-k8s-io-icr-io-docker-elastic-co-r` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:49.636Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/github-kubernetes.md
- free tier: none reachable: All are read-only or reject auth-less writes. Probed anonymously: mcr.microsoft.com and registry.opensuse.org answer /v2/ with 200 but an anonymous POST blobs/uploads returns 411 (length… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the first-party page states no per-object size cap on the first-party registry pages | note: not applicable
- retention: stated-absent: the first-party page states no a retention period for stored image layers on the registry.k8s.io page
- egress: There is NO uptime SLA as this is a free, volunteer managed service; traffic is sent to GCP and AWS thanks to their donations. | metered: no
- identity: email
- interface: oci, rest
- interface detail: OCI distribution registry with an HTTP /v2/ API used by Docker and Skopeo
- tooling: not documented
- composes with: Mirroring to a location you control is recommended; API endpoints, IP addresses and backing services may change at any time.
- reliability: These registries are read-only or reject auth-less writes. mcr.microsoft.com answers GET /v2/ with HTTP 200 anonymously (an empty JSON body), and registry.k8s.io requires a bearer token at /v2/; neither accepts an anonymous writable store.
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: All are read-only or reject auth-less writes. Probed anonymously: mcr.microsoft.com and registry.opensuse.org answer /v2/ with 200 but an anonymous POST blobs/uploads returns 411 (length…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: All are read-only or reject auth-less writes. Probed anonymously: mcr.microsoft.com and registry.opensuse.org answer /v2/ with 200 but an anonymous POST blobs/uploads returns 411 length…
  - probe:https://mcr.microsoft.com/v2/ 2026-11-19: anonymous GET /v2/ on MCR returns 200, consistent with a read-only public mirror | capture: sha256:7fc7f932c0c090ce8d13b10532d0768f5b679b2e8362ae97ed2a1f68317d5f34 | quote: "status": 200
  - probe:https://registry.k8s.io/v2/ 2026-11-19: registry.k8s.io requires a bearer token at /v2/, so no anonymous write path exists | capture: sha256:50c88d54b84fc4e7e93576980d3df0d35fad57a592dc680ee0e250884d403471 | quote: "status": 401
  - [1] 2026-11-19: the registry.k8s.io first-party README states it serves an OCI-compliant registry | capture: sha256:759a4b183187812fb9771b736bcda2ecad617f504d1fc251b55b2de95bc7e050 | quote: Other than `registry.k8s.io` serving an [OCI](https://github.com/opencontainers/distribution-spec) compliant registry: API endpoints, IP addresses, and backing services used are subject to change at anytime
  - [2] 2026-11-19: the IBM Container Registry first-party page states an OCI distribution interface used by Docker and Skopeo | capture: sha256:690ae67578eb5bdeeb477009fde80a2ad12d8950cb1378b7851a7ff5cebfda1c | quote: IBM Cloud® Container Registry supports the Open Container Initiative - [OCI](https://opencontainers.org/) distribution specification so that you can use common tools such as Docker and Skopeo to interact with your images.
  - [1] 2026-11-19: the registry.k8s.io first-party README states there is no uptime SLA | capture: sha256:759a4b183187812fb9771b736bcda2ecad617f504d1fc251b55b2de95bc7e050 | quote: Please note that there is NO uptime SLA as this is a free, volunteer managed service
- sources:
  - [1] https://github.com/kubernetes/registry.k8s.io
  - [2] https://icr.io/
