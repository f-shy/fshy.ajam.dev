# ArangoDB Oasis

> arango.ai | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arango/ | JSON https://fshy.ajam.dev/api/v1/entity/arango.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ArangoDB Oasis (Arango Managed Platform)

- `databases-kv/arangodb-oasis` | trial-only | evidence documented | binding retention-clamped | category managed multi-model database: graph, document, key-value, vector and search | tier Free-to-Try (Arango Managed Platform)
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T00:19:24.755Z (live) | stale on 2026-12-20
- url https://docs.arango.ai/arangodb/stable/get-started/set-up-a-cloud-instance
- free tier: 14-day free-to-try tier: one project, one small deployment of 4GB, local backups, and one notebook; no credit card required; the deployment is automatically deleted after the trial | unit: GB | metered on: wall-clock | read on: 2026-11-19 | source: [1] | note: A time-boxed 14-day trial, not a permanent free tier. The 4GB is the trial deployment size; the docs page gives no per-object cap. The FAQ calls the small Ohio deployment 52ct/hr once the trial ends, and the Developer-deployment blog gives 0.058 USD per hour or 42.2 USD per month for a single-server node.
- per-object cap: unverified: no per-object size cap is stated on the free-tier pages read; the 4GB figure is the deployment size, not a single-object limit | source: [1] | note: ArangoDB is a document store, so the relevant ceiling is the deployment storage; no document-size cap was published on the pages read.
- retention: the free deployment is automatically deleted after the 14-day trial; all data including backups is lost if the account is not converted to a paying one | days: 14 | source: [2] | note: The trial deletion clock is the binding constraint: there is no perpetual free lane to fall back to at day 15.
- egress: network traffic and backup storage are charged separately from the compute price on paid deployments; no number for egress is published on the first-party pages read, and the free tier gives no egress allowance or per-GB rate | metered: yes | source: [3]
- identity: any-phone | detail: signup asks for an email address required for email verification; if the email is from a public provider such as Hotmail, a mobile phone number is required for SMS verification, and one mobile number cannot be used for multiple accounts. GitHub, Google and Microsoft sign-in are also offered, which avoids the phone step. No card is needed: the FAQ states 'You can sign up on Arango Managed Platform for free without the need to enter a credit card.'
- interface: rest, cli
- limits:
  - retention-clamped (binding): the free deployment is automatically deleted after 14 days, and all data including backups is lost if not converted to a paying account [2]
  - volume-quota: one project and one small deployment of 4GB on the free-to-try tier [1]
  - write-gated: a public email service address triggers a required mobile phone number verified by SMS; one mobile number is bound to one account and cannot be reused [1]
- binding note: the 14-day automatic deletion with no perpetual free lane is what fails first; the 4GB deployment size and the phone gate matter only within that window
- interface detail: the ArangoDB HTTP REST API over TLS, with official drivers for major languages; a web UI (ArangoDB web interface) and a notebook; the FAQ states all ArangoDB drivers are supported as long as TLS is supported
- tooling: any ArangoDB driver over HTTPS (arangojs, python-arango, go-driver and others); the built-in web UI and notebook; rclone does not apply
- composes with: a managed graph, document and key-value store that can sit behind a free frontend or worker for a public endpoint; Foxx services cannot call the internet by default on the managed platform, which limits server-side chaining unless enabled on request
- reliability: the free deployment is deleted at day 14 with all data and backups; single-server and Developer deployments have no high availability and can be restarted at any time; deployments cannot be paused to reduce cost
- notes: ArangoDB Oasis (now Arango Managed Platform) has no perpetual free tier. Its only free route is a 14-day trial with one 4GB deployment, deleted with all data at the end. A public email provider triggers an SMS phone gate bound one-to-one to an account; a GitHub, Google or Microsoft sign-in avoids that gate. The free self-managed Community Edition is software the reader installs and runs, so it is not a hosted offer and is not the answer here. Paid hourly rates begin at 0.058 USD per hour for a single-server Developer deployment and 52ct/hr for a small deployment in Ohio.
- evidence note: six first-party pages were read on 2026-11-19: the quick-start docs, the FAQ, the pricing page, the terms page, the AMP overview and the Developer-deployment blog. The free-tier 4GB and 14-day figures, the identity fields and the deletion clause are quoted from those pages. No probe was run, so the rung stays documented.
- evidence:
  - [1] 2026-11-19: the free tier is a 14-day trial with one 4GB deployment, one project, local backups and one notebook, deleted after the trial | capture: sha256:29de8baf1991c87306234edc93aac5229ac0a28806acbb76a77d4b3193cda854 | quote: comes with a free-to-try tier that lets you test the Arango cloud for free for 14 days. It includes one project and one small deployment of 4GB, local backups, and one notebook for learning and data science. After the trial period, your deployment is automatically deleted.
  - [1] 2026-11-19: an email address is required for registration | capture: sha256:29de8baf1991c87306234edc93aac5229ac0a28806acbb76a77d4b3193cda854 | quote: An email address, required for email verification.
  - [1] 2026-11-19: a phone number is required when the signup email is from a public email provider | capture: sha256:29de8baf1991c87306234edc93aac5229ac0a28806acbb76a77d4b3193cda854 | quote: A mobile phone number, required for SMS verification
  - [1] 2026-11-19: one phone number binds to a single account and blocks reuse | capture: sha256:29de8baf1991c87306234edc93aac5229ac0a28806acbb76a77d4b3193cda854 | quote: One mobile phone number is associated with one account and cannot be used for multiple accounts.
  - [2] 2026-11-19: no card is required to sign up and try the managed platform | capture: sha256:4aedb304109384561d710ec09604c0828829b517ac80a2e925028862f0dcdb06 | quote: You can sign up on Arango Managed Platform for free without the need to enter a credit card.
  - [2] 2026-11-19: the trial ends in deletion of the deployment and all its data and backups | capture: sha256:4aedb304109384561d710ec09604c0828829b517ac80a2e925028862f0dcdb06 | quote: After the free-to-try period ends, your deployment will be deleted. Note that, in that case, all data (including backups) will be lost.
  - [2] 2026-11-19: the managed offer has a programmatic REST/driver interface over TLS | capture: sha256:4aedb304109384561d710ec09604c0828829b517ac80a2e925028862f0dcdb06 | quote: Arango Managed Platform supports all ArangoDB drivers as long as TLS is supported.
  - [2] 2026-11-19: the hourly price of a small deployment once the trial ends | capture: sha256:4aedb304109384561d710ec09604c0828829b517ac80a2e925028862f0dcdb06 | quote: As an example, a small deployment in Ohio (AWS) costs 52ct/hr.
  - [3] 2026-11-19: egress and backup storage are metered separately from the compute rate on paid deployments | capture: sha256:0ba68bb91033c625733a32d6b53eb95431892588be5a1747a65103ce03104f3e | quote: Similar to our OneShard and Sharded deployments, network traffic and backup storage is charged separately.
  - [3] 2026-11-19: the single-server Developer deployment hourly and monthly price | capture: sha256:0ba68bb91033c625733a32d6b53eb95431892588be5a1747a65103ce03104f3e | quote: A Developer deployment launched in AWS Ohio is available for as little as $ 0.058 per hour or $42.2 per month.
  - [3] 2026-11-19: the small single-server deployment has no high availability and may restart | capture: sha256:0ba68bb91033c625733a32d6b53eb95431892588be5a1747a65103ce03104f3e | quote: Developer deployments are not highly available and can be restarted at any time.
  - [4] 2026-11-19: Oasis is the former name of Arango Managed Platform, so the two names are one hosted offer | capture: sha256:89ecdb4eb506895a1caa5be406dfa287031d7e862daeed7893439391b935052d | quote: formerly called Oasis
- sources:
  - [1] https://docs.arango.ai/arangodb/stable/get-started/set-up-a-cloud-instance
  - [2] https://dashboard.arangodb.cloud/faq
  - [3] https://www.arangodb.com/2021/06/introducing-developer-deployments-on-arangodb-oasis
  - [4] https://docs.arango.ai/amp
