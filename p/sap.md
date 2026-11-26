# SAP Business

> sap.com | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sap/ | JSON https://fshy.ajam.dev/api/v1/entity/sap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SAP Business Technology

- `compute/sap-business-technology` | trial-only | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T04:45:13.523Z (live) | stale on 2026-12-19
- url https://developers.sap.com/concepts/btp-free-tier-service-plans/
- free tier: "When using Kyma, the free plan is available only once in a global account for up to 30 days." Quoted from the pricing page: "SAP BTP trial is a non-commercial, time-limited offering that gives you 90 days... At the end of the trial period, your SAP BTP trial account will be shut down." | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-credit
- per-object cap: not applicable | source: [1]
- retention: Kyma, the managed Kubernetes runtime, is free once per global account and only for 30 days, and the free tier model itself needs a Pay-As-You-Go or enterprise agreement account, so there is no renewable free cluster. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: cli
- limits:
  - retention-clamped (binding): Kyma, the managed Kubernetes runtime, is free once per global account and only for 30 days, and the free tier model itself needs a Pay-As-You-Go or enterprise agreement account, so there is no renewable free cluster. [1]
- limits note: Kyma, the managed Kubernetes runtime, is free once per global account and only for 30 days, and the free tier model itself needs a Pay-As-You-Go or enterprise agreement account, so there is no renewable free cluster.
- binding note: the same as limits note
- interface detail: btp CLI (command line client) for account administration, an alternative to the SAP BTP cockpit web console; the cf CLI is used to enable Cloud Foundry; SSH and REST access not read
- tooling: btp CLI (the SAP BTP command line client, with JSON output for scripting) and the cf CLI for Cloud Foundry
- composes with: Nothing durable. A 30-day Kyma cluster is enough to test a manifest once, and the 90-day trial covers the build, which is the shape of a trial rather than a platform to run on.
- reliability: no reliability event recorded
- notes: The widely quoted '4 GB of free memory' figure was not confirmed on any page read and is deliberately absent rather than repeated.
- extras:
  - facets.class: refutation-trial-only
  - facets.free_tier_kind: trial-credit
  - session_cap.note: no sandbox session clock published; the free plan lifetime is an account plan term, not a session clock
- evidence:
  - [2] 2026-10-22: "When using Kyma, the free plan is available only once in a global account for up to 30 days", and a trial account runs 90 days, quoted
  - [3] 2026-10-22: the free tier model is "a commercial model that can be accessed by signing up for an SAP BTP Enterprise Agreement or Pay-As-You-Go"; the trial is shut down after 90 days with data deleted, quoted
  - [4] 2026-10-22: the Kyma enablement path selects a plan called free for kymaruntime, which is the plan the 30-day rule applies to
  - [5] 2026-11-03: a CLI and a web cockpit both exist | capture: sha256:dc146e0e7a54b96bbbeb64c650e99c31f99e35478e5a525ad89f9f4e5610ddad | quote: It is an alternative to the SAP BTP cockpit for users who like to work in a terminal or want to automate operations using scripts.
  - [2] 2026-11-03: the trial and free-tier page states durations and no egress allowance or egress price | capture: sha256:aa52d87e9f3ffdd6daad0021baa9d9f904c1466bca3ae52c2f98593c305f589b | quote: When using Kyma, the free plan is available only once in a global account for up to 30 days.
  - [5] 2026-11-04: the btp CLI is documented beside the cockpit web console | capture: sha256:dc146e0e7a54b96bbbeb64c650e99c31f99e35478e5a525ad89f9f4e5610ddad | quote: It is an alternative to the SAP BTP cockpit for users who like to work in a terminal or want to automate operations using scripts.
  - [5] 2026-11-04: the page names the BTP CLI and the cf CLI | capture: sha256:dc146e0e7a54b96bbbeb64c650e99c31f99e35478e5a525ad89f9f4e5610ddad | quote: This chapter lists the commands of the BTP CLI and the cf CLI that you need to create a subaccount and enable Cloud Foundry.
  - [1] 2026-11-18:  | capture: sha256:abb665f771d07acfa8d4cb4505ac41d2db75b7ae6eb78b3c00e6c6b1371a5dbc | quote: Free Tier Service Plans on SAP BTP
- sources:
  - [1] https://developers.sap.com/concepts/btp-free-tier-service-plans/
  - [2] https://github.com/SAP-docs/btp-cloud-platform/blob/main/docs/10-concepts/trial-accounts-and-free-tier-046f127.md
  - [3] https://www.sap.com/products/technology-platform/pricing.html
  - [4] https://developers.sap.com/tutorials/cp-kyma-getting-started/
  - [5] https://github.com/SAP-docs/btp-cloud-platform/blob/main/docs/50-administration-and-ops/account-administration-using-the-sap-btp-command-line-interface-btp-cli-7c6df2d.md

## SAP AI Core

- `inference/sap-ai-core` | paid-only | evidence documented | binding write-gated | category managed inference on an enterprise platform
- needs card no, phone no, ID no, institution yes | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://help.sap.com/docs/sap-ai-core
- free tier: No free inference allowance stated on the SAP AI Core documentation: it is an SAP Business Technology Platform service, and pricing is published in the SAP Discovery Center service catalog. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: institution | detail: SAP BTP account and service instance; the docs point pricing to the SAP Discovery Center, with no self-serve free inference grant documented
- interface: rest
- limits:
  - write-gated (binding): requires an SAP BTP subaccount and service key; no free inference allowance stated [1]
- endpoint: https://api.ai.{region}.ml.hana.ondemand.com/v2
- tooling: the SAP AI Core SDK or REST API with a service key from a BTP subaccount
- composes with: access requires an SAP BTP account, so there is no self-serve free inference tier documented here
- reliability: pricing details are published off-site in the SAP Discovery Center; no numeric free quota could be read from the captured page
- notes: The Discovery Center service-catalog page returned a 'resource not found' body; no free-tier value could be verified beyond the documentation landing page.
- evidence:
  - [1] 2026-11-18: SAP AI Core is an enterprise AI platform service and pricing is published separately | capture: sha256:7895586064e0aa5c1119b91b0dde8c3d45ab84112b6b8c033bce7b62c6a3c979 | quote: SAP AI Core helps you to develop and productize AI functions
- sources:
  - [1] https://help.sap.com/docs/sap-ai-core
