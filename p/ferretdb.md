# FerretDB Cloud

> ferretdb.io | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ferretdb/ | JSON https://fshy.ajam.dev/api/v1/entity/ferretdb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FerretDB Cloud

- `databases-kv/ferretdb-cloud` | qualifies-with-caveat | evidence documented | binding retention-clamped | category managed MongoDB-compatible document database (FerretDB proxy over PostgreSQL) | tier Free Tier
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:46:18.052Z (live) | stale on 2026-12-20
- url https://docs.ferretdb.io/installation/ferretdb-cloud/
- free tier: A Free Tier is offered for developers, students and small projects; its numeric storage or request allowance is not published on first-party pages. Free Tier instances are temporary and may be stopped or deleted if inactive, and TLS/SSL is not supported on Free Tier instances. | unit: mixed | metered on: unstated | read on: 2026-11-19 | source: [1] | note: The first-party Cloud docs name a Free Tier but publish no storage or request quota; a plan subscription is activated only on approval. A size quoted by third parties is not used here.
- per-object cap: unverified: no per-object or storage cap is published on the first-party Cloud docs or the signup page | source: [1] | note: No numeric cap appears on the first-party pages captured; a value only an approved account would show is not asserted.
- retention: Free Tier instances are temporary and may be stopped or deleted if inactive. | source: [1] | note: The docs give no inactivity threshold in days, so days is null; deletion is conditional on inactivity rather than a fixed countdown.
- egress: unverified: no first-party egress allowance, quota or price for FerretDB Cloud is published on the Cloud docs or signup page | metered: no | source: [1]
- identity: email | detail: FerretDB Cloud signup marks Name, Email, Company Name and Password as required and Company URL as optional, then asks the user to click an email verification link. The docs say the user is notified by email upon approval of the chosen plan. No card, phone or ID document is requested at signup.
- interface: cli, browser
- limits:
  - retention-clamped (binding): Free Tier instances are temporary and may be stopped or deleted if inactive [1]
  - per-object-cap: unverified: no numeric storage or object cap is published for the Free Tier [1]
- binding note: No numeric quota is published; the first constraint on a free instance is that it may be stopped or deleted while inactive, and it has no TLS.
- interface detail: A MongoDB wire-protocol endpoint reached by a mongodb:// connection string whose username, password and endpoint are shown in the instance dashboard. Free Tier connects without TLS; paid tiers require ?tls=true. A web dashboard manages deployments.
- tooling: any MongoDB-compatible client (mongosh, MongoDB Compass, official MongoDB drivers)
- composes with: A hosted FerretDB endpoint is reachable from any MongoDB driver without changing client code; the open-source FerretDB proxy that the user installs and runs on a rented or free machine is the last-resort option if the hosted tier is not approved.
- reliability: Free Tier instances are temporary and may be stopped or deleted if inactive; TLS/SSL is not supported on Free Tier, while Pro, Enterprise and Bring Your Own Account Enterprise tiers require TLS.
- notes: A hosted MongoDB-compatible document database with a Free Tier, but the free instance is temporary, has no TLS, and a plan needs approval. No dollar price and no numeric free allowance are published on first-party pages; the self-hosted open-source FerretDB proxy is the last resort, not the offer this record describes.
- evidence note: All stated values are from first-party FerretDB documentation and the FerretDB Cloud signup page captured on 2026-11-19. The free-tier allowance is not stated by either source and is left unverified.
- self hosted: no
- evidence:
  - [1] 2026-11-19: FerretDB Cloud is a hosted managed database service, not self-hosted software | capture: sha256:63cad5bb784a25e737e8b8061e3ce61b824b6be6b14d3921c68c68aba02bed56 | quote: FerretDB Cloud is a managed service that lets you create, deploy, and manage FerretDB instances in the cloud.
  - [1] 2026-11-19: the Free Tier has no TLS; paid tiers require ?tls=true | capture: sha256:63cad5bb784a25e737e8b8061e3ce61b824b6be6b14d3921c68c68aba02bed56 | quote: TLS/SSL connections are not supported in Free tier instances - Ensure to connect without adding (`?tls=true`) to the connection string.
  - [1] 2026-11-19: free instances can be stopped or deleted on inactivity | capture: sha256:63cad5bb784a25e737e8b8061e3ce61b824b6be6b14d3921c68c68aba02bed56 | quote: Free Tier instances are temporary and may be stopped or deleted if inactive.
  - [1] 2026-11-19: a subscription plan is activated only after approval | capture: sha256:63cad5bb784a25e737e8b8061e3ce61b824b6be6b14d3921c68c68aba02bed56 | quote: You will be notified by email upon approval.
  - [2] 2026-11-19: the signup form requires a name | capture: sha256:efdf3453d2cbd170d71c0ade069d00129fabedb5362332d65cbfdaed040fe4ab | quote: Name \*
  - [2] 2026-11-19: the signup form requires a company name and no card or phone | capture: sha256:efdf3453d2cbd170d71c0ade069d00129fabedb5362332d65cbfdaed040fe4ab | quote: Company Name \*
- sources:
  - [1] https://docs.ferretdb.io/installation/ferretdb-cloud/
  - [2] https://cloud.ferretdb.com/signup
