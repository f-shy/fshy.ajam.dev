# JFrog Artifactory

> jfrog.com | Storage, CI runners; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jfrog/ | JSON https://fshy.ajam.dev/api/v1/entity/jfrog.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JFrog Artifactory Cloud — free tier (historically 2 GB)

- `storage/jfrog-artifactory-cloud-free-tier` | fails-quota | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:06.406Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the legacy JFrog Free subscription includes 2 GB total storage, 10 GB/month transfer and 2,000 build minutes | capture: sha256:8781d0d22d8bd3bd19dab94f4ce0be0ab3941f3756cbca376f1fb24b92ffef33 | quote: The subscription is generous with 10GB of data transfer per month, 2,000 build minutes per month and 2GB total storage.
  - [2] 2026-11-19: the live SaaS pricing ladder starts at the paid Pro plan at $50 per month with no free row | capture: sha256:f9ecf0b64030e21a5bacfb3a899395de139ce195190e3cd8907b759068d62241 | quote: Pro $50 / Month (was $150 / Month, Save $100/mo)
- sources:
  - [1] https://jfrog.com/blog/5-steps-to-starting-devops-with-a-jfrog-free-subscription/
  - [2] https://jfrog.com/pricing/
  - [3] https://jfrog.com/solution-sheet/jfrog-container-registry/

## Shippable

- `ci-cd-runners/shippable` | dead | evidence documented | binding write-gated | category CI runner | tier historical hosted CI/CD service (end of life)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:19:24.678Z (live) | stale on 2026-12-20
- url https://docs.jfrog.com/releases/docs/pipeline-deprecation-end-of-life
- free tier: Historical hosted plan: free for all open-source projects and one private project with unlimited builds, stated on a preserved first-party pricing page from 2014. Paid plans were announced as coming soon and the hosted service has since ended; this is not a current offer | unit: unlimited | metered on: unstated | read on: 2026-11-19 | source: [1] | note: The preserved page states unlimited builds rather than a build-minute or build-count number, so the nearest unit term is unlimited. The offer is historical and the service no longer runs.
- per-object cap: unverified: no per-object cap is stated on the pages read; the service ran builds rather than storing objects | source: [2]
- retention: unverified: no build or build-log retention period is stated on the pages read | source: [2]
- egress: unverified: no egress allowance or per-gigabyte price is stated on the pages read. A self-hosted Server and bring-your-own-node option existed, but no hosted egress figure is established | metered: no | source: [2]
- identity: email | detail: The hosted service required no separately created account: sign-in used GitHub or Bitbucket credentials through OAuth, which the user authorized on first sign-in. The source-control account therefore carried an email identity. No card or phone requirement is established from the page read and no sign-up was performed
- interface: git, rest
- limits:
  - write-gated (binding): JFrog Pipelines reached end of life on May 1, 2026, and no longer receives updates, bug fixes, or security patches [3]
  - retention-clamped: a 30 day free pilot license was offered for the self-hosted Shippable Server, not for the hosted runner [2]
- limits note: The hosted free plan stated unlimited builds without a build-minute number; no request-rate or per-object figure was published on the pages read.
- binding note: The successor product's end of life stops new builds for every plan, so discontinuation binds before any historical pilot or build limit.
- interface detail: A connected source-control repository drove builds on the hosted service. A REST API under docs.shippable.com/platform/api described programmatic access; the service has reached end of life. A separately named product at shippable.dev is a code scanner rather than a CI runner and is not this offer.
- endpoint: unverified: no current hosted API endpoint remains after the end of life
- tooling: A hosted CI/CD platform where the vendor spun up build machines called Minions for each build. A self-hosted Server and bring-your-own-node option existed as secondary choices; neither is the hosted offer documented here.
- composes with: A push to a connected GitHub or Bitbucket repository started a build on vendor-run build machines. The product was made part of JFrog Pipelines, which also reached end of life, so this chain no longer runs on Shippable.
- reliability: The hosted CI service was acquired and made part of JFrog Pipelines, which reached end of life on May 1, 2026 and no longer receives updates or support.
- notes: A hosted CI/CD service that was acquired by JFrog in 2019, made part of JFrog Pipelines and discontinued with that product on May 1, 2026. The current shippable.dev domain serves a code scanner and is a different offer, not a runner. A self-hosted Server and bring-your-own-node option were secondary choices and never the hosted offer.
- evidence note: The end-of-life notices and the historical Shippable documentation are first-party pages captured and quoted. No build was run and no account was opened. The historical build-minute free allowance is not stated on any first-party page read and is unverified.
- evidence:
  - [3] 2026-11-19: the successor to Shippable reached end of life on May 1, 2026 | capture: sha256:5ff0346c7286b5da2d1169ece8415656bdba88d831903dd2c5e9d63c7cdf6532 | quote: JFrog Pipelines reached end of life on May 1, 2026, and no longer receives updates, bug fixes, or security patches.
  - [3] 2026-11-19: the end of life covers both hosted and self-managed deployments | capture: sha256:5ff0346c7286b5da2d1169ece8415656bdba88d831903dd2c5e9d63c7cdf6532 | quote: JFrog Pipelines, the CI/CD orchestration product within the JFrog Platform, has reached official end of life. Both SaaS and self-managed deployments are affected.
  - [4] 2026-11-19: the vendor product page marks the successor as sunset | capture: sha256:cc9aa1aa0b5f04113ad53ffefe459222165ac427678b68b3f5e2bb19c9c63b0e | quote: JFrog Pipelines is currently sunset as we focus on new and exciting things at JFrog.
  - [5] 2026-11-19: JFrog folded the Shippable CI/CD tool into JFrog Pipelines | capture: sha256:032cf9634f852c4f6c8a9738ed4aae85c6af06a2620ad9ee7f17090fcc34a5dd | quote: to blend Shippable's CI/CD tool into the JFrog Platform following the successful acquisition
  - [5] 2026-11-19: the first-party blog confirms the sunset date of the successor | capture: sha256:032cf9634f852c4f6c8a9738ed4aae85c6af06a2620ad9ee7f17090fcc34a5dd | quote: JFrog Pipelines is sunset and will not be supported as of May 2026.
  - [1] 2026-11-19: the historical hosted free plan covered open source and one private project with unlimited builds | capture: sha256:966f66a7ece314829734d57c924abde8b9ad0ce101b83d068026a37d50c899c9 | quote: FREE PLAN : Unlimited builds for all open source and one private project!!
  - [2] 2026-11-19: Shippable was a hosted CI/CD service | capture: sha256:cd862ca65539bf3af92fcb2c21c7fb18ef712f72b1c2a517609f7d266fe6a65f | quote: Shippable is a DevOps Assembly Lines Platform that helps developers and DevOps teams achieve CI/CD and make software releases frequent, predictable, and error-free.
  - [2] 2026-11-19: the hosted sign-in gate was a GitHub or Bitbucket OAuth account, with no separate account creation | capture: sha256:cd862ca65539bf3af92fcb2c21c7fb18ef712f72b1c2a517609f7d266fe6a65f | quote: You can [sign in](https://app.shippable.com/) using your GitHub or Bitbucket credentials. We use OAuth authentication so you will need to authorize Shippable the first time you sign in.
  - [2] 2026-11-19: a hosted SaaS lane and a self-hosted Server existed; the hosted lane is the offer recorded here | capture: sha256:cd862ca65539bf3af92fcb2c21c7fb18ef712f72b1c2a517609f7d266fe6a65f | quote: Shippable is available as a [Hosted SaaS offering](https://app.shippable.com/) as well as a [Server](http://docs.shippable.com/platform/server/overview).
  - [2] 2026-11-19: the hosted service ran builds on vendor-spun build machines | capture: sha256:cd862ca65539bf3af92fcb2c21c7fb18ef712f72b1c2a517609f7d266fe6a65f | quote: Minions are the build machines that are spun up to run your builds on Shippable Hosted.
  - [2] 2026-11-19: the self-hosted Server had a 30 day free pilot, distinct from the hosted runner | capture: sha256:cd862ca65539bf3af92fcb2c21c7fb18ef712f72b1c2a517609f7d266fe6a65f | quote: We offer a 30 day free pilot license for Shippable Server to help organizations evaluate it.
  - probe:https://app.shippable.com 2026-11-19: the former hosted app address did not resolve on 2026-11-19 | capture: sha256:2d617d6bb5d6e04ee3cfbb827282d54ccdffd49b1f85d99cc08a83beac2cf73b | quote: "status": null
  - [6] 2026-11-19: the current shippable.dev product is a code scanner running local scans, not a hosted CI runner | capture: sha256:67c8cbc7ac42f8269ec506a650e33b13fddea9e21fb41c9e96f3b708dfb839d2 | quote: Local scans run on your machine. Only package names and versions go to the OSV vulnerability database.
- sources:
  - [1] https://web.archive.org/web/20140109110858/https://www.shippable.com/Pricing
  - [2] https://web.archive.org/web/20190225092810/http://docs.shippable.com/
  - [3] https://docs.jfrog.com/releases/docs/pipeline-deprecation-end-of-life
  - [4] https://jfrog.com/pipelines
  - [5] https://jfrog.com/blog/jfrog-devops-platform
  - [6] https://shippable.dev/pricing

## JFrog Artifactory Community Edition (CE for C/C++) / Artifactory OSS — self-hosted

- `storage/jfrog-artifactory-community-edition-artifactory-oss-self` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:22.253Z (live) | stale on 2026-11-25
- url https://jfrog.com/community/download-artifactory-oss/
- free tier: This product gives all the power and flexibility of the Artifactory repository for Conan and generic binaries to the C/C++ world completely free of charge to any software team. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
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
- notes: Free of charge, self-hosted, no storage cap of any kind: the quota is whatever disk/object-store you attach. 'This product gives all the power and flexibility of the Artifactory repository for Conan and generic binaries to the C/C++ world completely free of charge.' OSS edition likewise downloadable and free.
- evidence note: the Conan and generic repository edition is stated as completely free of charge on the JFrog announcement
- self hosted: yes
- evidence:
  - [1] 2026-10-21: read live: 'completely free of charge to any software team'; 'containing support only for Conan and generic repositories'
  - [2] 2026-10-21: read live: 'It is completely free, and features a WebUI, advanced authentication and permissions ... a REST API, a generic CLI tool and generic repositories to host any kind of source or binary artifact'
  - [3] 2026-10-21: read live: live download links for OSS (tar.gz, rpm, deb, docker, helm) — the free edition is still shipping
  - [1] 2026-11-09: the Conan and generic repository edition is free of charge to any software team | capture: sha256:65f550fe42b8015a182cc5e5ae25838527a7f27f933d5fbfab3fa08b3787b257 | quote: This product gives all the power and flexibility of the Artifactory repository for Conan and generic binaries to the C/C++ world completely free of charge to any software team.
- sources:
  - [1] https://jfrog.com/blog/announcing-jfrog-artifactory-community-edition-c-c/
  - [2] https://docs.conan.io/2/tutorial/conan_repositories/setting_up_conan_remotes/artifactory/artifactory_ce_cpp.html
  - [3] https://jfrog.com/community/download-artifactory-oss/
