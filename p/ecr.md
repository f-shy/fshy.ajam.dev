# Amazon ECR Public

> ecr.aws | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ecr/ | JSON https://fshy.ajam.dev/api/v1/entity/ecr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Amazon ECR Public

- `storage/amazon-ecr-public` | qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gallery.ecr.aws
- free tier: 50 GB per month of always-free storage for public repositories: 'Both new and existing customers get 50 GB per month of always-free storage for their public repositories.' Past 50 GB it is not blocked. Storage is billed to the repository owner: pricing table 'All storage / month .. per GB' resolves via AWS's price API to $0.1000000000/GB-month. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Half-free, and the free half is generous: 'You can anonymously (without using an AWS account) transfer 500 GB of data to the Internet from a public repository each month for free. If you sign up for an AWS account, or authenticate to Amazon ECR with an existing AWS account, you can transfer 5 TB of data to the Internet from a public repository each month for free.' Past that: 'Greater than 5 TB / month to non AWS Regions | $0.09 per GB'. Anonymous overage is not billed, it is refused: 'Up to 500 GB/month can be transferred out to non-AWS destinations to clients that have not authenticated (that is, anonymously). After that limit is reached, no further anonymous data transfer is allowed.' Zero egress cost to AWS compute in any region. | metered: yes | free allowance: 5 TB per month
- identity: institution
- interface: oci, cli
- limits note: Max layer size 10,000 MiB; max layer part 10 MiB; 100,000 images/repo; 1,000 tags/image; unauthenticated pulls rate-limited to 1/s and capped at 500 GB/month per source IP; authenticated pulls 10/s. Repos are always publicly listable. 'Using a repository policy to deny access to view or pull from a public repository is not supported.'.
- interface detail: oci
- tooling: docker/skopeo/oras/crane; ORAS pushes arbitrary blobs as OCI artifacts. AWS CLI for auth (aws ecr-public get-login-password).
- composes with: 50 GB x N AWS accounts. Egress is per-downloader-IP for anonymous pulls and 5 TB/month for any authenticated AWS account, so a single account gives 5 TB/mo of public egress, and each additional free AWS account gives another 5 TB/mo as the authenticated client. Storage is only 50 GB/account, so the economics are inverted versus most registries: egress scales, storage does not.
- reliability: Very stable; the 1 pull/s anonymous rate limit is the thing that bites bulk fetches (a parallel fetcher must spread across IPs or authenticate).
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 50 GB always-free public storage; 500 GB/mo anonymous egress, 5 TB/mo authenticated, $0.09/GB beyond
  - [2] 2026-10-21: 'unauthenticated image pulls 1 per second', max layer 10,000 MiB
  - [3] 2026-10-21: rateCode zY12MU_... price 0.1000000000 (storage $/GB-mo)
  - [4] 2026-10-21: probe: GET -> 401 with Www-Authenticate: Bearer realm="https://public.ecr.aws/token/"; GET /token/?service=public.ecr.aws&scope=repository:amazonlinux/amazonlinux:pull -> {"token":...}; GET /v2/amazonlinux/amazonlinux/manifests/latest with that Bearer -> 200, Content-Type application/vnd.docker.distribution.manifest.list.v2+json
- sources:
  - [1] https://aws.amazon.com/ecr/pricing/
  - [2] https://docs.aws.amazon.com/AmazonECR/latest/public/public-service-quotas.html
  - [3] https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ecr/USD/current/ecr.json
  - [4] https://public.ecr.aws/v2/
