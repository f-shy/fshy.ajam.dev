# JFrog Artifactory

> jfrog.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jfrog/ | JSON https://fshy.ajam.dev/api/v1/entity/jfrog.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JFrog Artifactory Cloud — free tier (historically 2 GB)

- `storage/jfrog-artifactory-cloud-free-tier` | fails-quota | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://jfrog.com/pricing/
- free tier: 2 GB total storage + 10 GB/month data transfer on the legacy 'JFrog Free' cloud subscription. That tier is no longer generally available: JFrog's own blog now carries the banner 'The below post showcases the JFrog Platform Free Tier, which is currently limited for new sign-ups.' The live pricing page has no free tier at all. The entry point is Pro at $50/mo with 25 GB base consumption. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 2 GB total storage (not per month. A Stack Overflow answer from a JFrog employee confirms it is total, and you must delete to reclaim); 10 GB/month transfer; 2,000 build minutes; 21-day inactivity deactivation. | days: 21 | source: [1] | note: not stated
- egress: 10 GB/month included on the legacy free tier; beyond that the platform bills 'Consumption = Storage + Transfer' against the included base. Not free, not Cloudflare-coverable. | metered: no | free allowance: 10 GB per month
- identity: card
- interface: rest, oci, cli
- limits note: 2 GB total storage (not per month. A Stack Overflow answer from a JFrog employee confirms it is total, and you must delete to reclaim); 10 GB/month transfer; 2,000 build minutes; 21-day inactivity deactivation.
- interface detail: rest (Artifactory REST), JFrog CLI, native package clients, OCI
- tooling: JFrog CLI, `curl -T`, `docker push`, `twine upload`. Best-in-class tooling, which is why the 2 GB cap is such a shame.
- composes with: Previously: one free cloud instance per account, × unlimited accounts, at 2 GB each. Now gated: 'limited for new sign-ups', and accounts are deactivated after '21 days with no data transfer activity'. So a dormant bulk store dies.
- reliability: Repeated policy churn (free tier gated, then 2 GB → 25 GB Pro) plus inactivity deactivation makes it unsafe as storage.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 2 GB total storage + 10 GB/month data transfer on the legacy 'JFrog Free' cloud subscription. That tier is no longer generally available: JFrog's own blog now carries the banner 'The below post showcases the JFrog Platform Free Tier, which is currently limited for new sign-ups.' The live pricing page has no free tier at all — the entry point is Pro at $50/mo with 25 GB base consumption.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'currently limited for new sign-ups'; 'The subscription is generous with 10GB of data transfer per month, 2,000 build minutes per month and 2GB total storage'; 'accounts that experience 21 days with no data transfer activity will be deactivated'
  - [2] 2026-10-21: read live 2026-10-21: plan ladder is Pro 25 GB base / Enterprise 125 GB base; no free row anywhere, entry price $50/month
  - [3] 2026-10-21: read live: 'The Cloud version includes 2GB of peak data storage, 10GB of monthly data transfer'
- sources:
  - [1] https://jfrog.com/blog/5-steps-to-starting-devops-with-a-jfrog-free-subscription/
  - [2] https://jfrog.com/pricing/
  - [3] https://jfrog.com/solution-sheet/jfrog-container-registry/

## JFrog Artifactory Community Edition (CE for C/C++) / Artifactory OSS — self-hosted

- `storage/jfrog-artifactory-community-edition-artifactory-oss-self` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://jfrog.com/community/download-artifactory-oss/
- free tier: Free of charge, self-hosted, no storage cap of any kind: the quota is whatever disk/object-store you attach. 'This product gives all the power and flexibility of the Artifactory repository for Conan and generic binaries to the C/C++ world completely free of charge.' OSS edition likewise downloadable and free. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free by construction. You serve it from your own host/object store, so egress is your bill (or zero behind Cloudflare). Not a hosted egress concession. | metered: no
- identity: email
- interface: rest, oci, cli
- limits note: CE for C/C++ is restricted to Conan + generic repository types only (no Docker/Maven/npm); OSS edition likewise feature-stripped. No HA, no S3 blob store on CE. Requires you to run Java + Postgres/derby and to pay for the bytes.
- interface detail: rest (Artifactory REST API), plus every native protocol it supports: docker/OCI, maven, npm, pypi, nuget, generic, conan; JFrog CLI
- tooling: JFrog CLI (`jf rt upload`), `curl -T` against the REST API, `oras`/`docker push` for OCI, and any package client. Real, first-party, actively maintained.
- composes with: Not really chainable as free storage: each instance consumes your own disk. The only 'multiplier' is running it on someone else's free compute/disk, which is a different niche (IaaS), not an artifact-manager finding.
- reliability: Mature, no data-vanishing risk; the catch is that 'free' means free software, not free storage. You are the storage provider.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: read live: 'completely free of charge to any software team'; 'containing support only for Conan and generic repositories'
  - [2] 2026-10-21: read live: 'It is completely free, and features a WebUI, advanced authentication and permissions ... a REST API, a generic CLI tool and generic repositories to host any kind of source or binary artifact'
  - [3] 2026-10-21: read live: live download links for OSS (tar.gz, rpm, deb, docker, helm) — the free edition is still shipping
- sources:
  - [1] https://jfrog.com/blog/announcing-jfrog-artifactory-community-edition-c-c/
  - [2] https://docs.conan.io/2/tutorial/conan_repositories/setting_up_conan_remotes/artifactory/artifactory_ce_cpp.html
  - [3] https://jfrog.com/community/download-artifactory-oss/
