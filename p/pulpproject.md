# Pulp

> pulpproject.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pulpproject/ | JSON https://fshy.ajam.dev/api/v1/entity/pulpproject.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pulp (pulpcore) — self-hosted

- `storage/pulp-self-hosted` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://pulpproject.org/
- free tier: Free open-source (GPL) self-hosted repository server; no quota because there is no vendor. 'Pulp is an open source project that makes it easy for developers to fetch, upload, organize and distribute Software Packages on-prem or in the cloud.' | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free by construction. Self-hosted; you pay (or don't) for your own bandwidth. | metered: no
- identity: anonymous
- interface: rest, oci, cli
- limits note: No vendor limits. Operationally: you must run Postgres + object storage + workers; 'unlimited' means 'as much disk as you attach'. No built-in public/anonymous CDN.
- interface detail: rest (pulpcore REST API), plus repository endpoints for rpm/deb/python/container/generic; also ships OCI images of itself
- tooling: pulpcore REST API + `pulp-cli`, plus `podman`/`docker` for the container deploy and standard package clients against published repos. Documented at pulpproject.org/pulpcore/docs/. It is also the backend Fedora COPR uses, which is a working-scale endorsement.
- composes with: Same self-hosted arithmetic: unlimited instances × your disk. Notably it is the engine under COPR's Pulp backend, so its per-repo retention setting (`retain_package_versions`) is the lever that makes 'unlimited' repos actually behave like storage.
- reliability: Very reliable (Red Hat-backed, used by COPR); the cost is operational complexity, not data loss.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: read live: 'Pulp is an open source project that makes it easy for developers to fetch, upload, organize and distribute Software Packages on-prem or in the cloud'
  - [2] 2026-10-21: read live: COPR uses a 'Pulp backend', and Pulp's `retain_package_versions` repository setting controls retention — evidence Pulp runs at Fedora scale
- sources:
  - [1] https://pulpproject.org/
  - [2] https://docs.copr.fedorainfracloud.org/user_documentation.html
