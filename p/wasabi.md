# Wasabi Hot Cloud Storage

> wasabi.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wasabi/ | JSON https://fshy.ajam.dev/api/v1/entity/wasabi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wasabi Hot Cloud Storage

- `storage/wasabi-hot-cloud-storage` | qualifies-with-caveat | evidence documented | binding volume-quota | category S3-compatible hot object storage
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T01:57:50.875Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://wasabi.com/pricing
- price USD 7.99 per TB per month on Pay as You Go, billed per GB per day for actual usage, with a minimum monthly charge tied to 1 TB of active storage per account and a 90-day minimum storage duration; Reserved Capacity Storage is a fixed-rate block from 25 TB on a 1-, 3- or 5-year term, with discounts set by capacity and term and a 30-day minimum storage duration | parsed USD 7.99/TB-mo
- free tier: 1 TB minimum monthly charge; RCS 25 TB+ blocks | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: no egress or API request fee on Pay as You Go or Reserved Capacity Storage, under the free egress policy: monthly egress up to the active storage volume fits the policy, monthly egress above it does not, and use above the policy on a regular basis may lead Wasabi to limit or suspend the service | metered: no | free allowance: monthly egress up to the active storage volume of the account
- identity: card | detail: a credit or debit card: upgrading to Pay as You Go asks for billing card details, and the trial period ends when a credit card is submitted
- interface: s3-compatible, rclone, cli
- limits:
  - volume-quota (binding): monthly egress up to the active storage volume under the free egress policy; above it on a regular basis the service may be limited or suspended [2]
- limits note: 90-day minimum storage duration (pay-as-you-go). Minimum monthly charge tied to 1 TB active storage. Free trial is only 100 GB/30 days on a company email domain, 10 GB/14 days on Gmail. Not a route to free capacity.
- binding note: monthly egress above the active storage volume falls outside the free egress policy, so the bytes read out in a month cannot exceed the bytes stored without risking a limit or a suspension; the storage price and the 90-day minimum storage duration come after it
- interface detail: S3 API
- tooling: rclone, aws-cli, restic, Veeam
- composes with: direct S3 origin; Cloudflare-compatible
- reliability: under the free egress policy, egress above the active storage volume on a regular basis may lead to the service being limited or suspended; under the free API request policy, a non-validated application that loads the service inefficiently may be limited or suspended; a deleted or overwritten object is billed as deleted storage until it reaches the 90-day minimum storage duration
- notes: the same as the free tier
- evidence note: the Pay as You Go and Reserved Capacity rows, the egress and API fee line, the minimum monthly charge and the contract term are quoted from the first-party pricing table, and the free egress policy from the first-party pricing FAQ
- extras:
  - price_verbatim: $7.99/TB/mo at every tier, egress and requests $0. ≈€6.89/TB.
- evidence:
  - [1] 2026-10-21: '$7.99 TB/month', 'Egress & API fees $0', 'Minimum storage duration 90 days', 'Minimum monthly charge Yes, tied to 1TB active storage per account'
  - withheld 2026-10-21: same page — free trial: 'Company email domain: 100 GB for 30 days; Freemail Domain: 10 GB for 14 days'
  - [1] 2026-10-30: Pay as You Go is USD 7.99 per TB per month; Reserved Capacity discounts depend on the capacity and the term; the same table gives the billing basis, minimum duration and minimum charge | capture: sha256:7c80b45579da69df1114c7d9c9d9a44ee1833e4b93faf2fe13b2ceebd22e8181 | quote: | Price per TB | $7.99/month | Discounts determined by both the storage capacity purchased and the contract term length |
  - [2] 2026-10-30: free egress is bounded by the active storage volume each month | capture: sha256:29e7011551e06ea9d40f2f3102982e0ad533420100f53974e641c958af416c4c | quote: If your monthly egress data transfer is greater than your active storage volume, then your storage use case is not a good fit for Wasabi’s free egress policy
  - [2] 2026-10-30: monthly egress up to the active storage volume fits the free egress policy | capture: sha256:29e7011551e06ea9d40f2f3102982e0ad533420100f53974e641c958af416c4c | quote: If your monthly egress data transfer is less than or equal to your active storage volume, then your storage use case is a good fit for Wasabi’s free egress policy
  - [2] 2026-10-30: egress beyond the policy on a regular basis may lead to the service being limited or suspended | capture: sha256:29e7011551e06ea9d40f2f3102982e0ad533420100f53974e641c958af416c4c | quote: If your use case exceeds the guidelines of our free egress policy on a regular basis, we reserve the right to limit or suspend your service.
  - [2] 2026-10-30: the egress guideline is the stored volume per monthly billing cycle; the same page gives the 90-day minimum storage duration | capture: sha256:29e7011551e06ea9d40f2f3102982e0ad533420100f53974e641c958af416c4c | quote: For example, if you store 100 TB with Wasabi and download (egress) 100 TB or less within a monthly billing cycle, then your storage use case is a good fit for our policy.
  - [3] 2026-10-30: a paid account starts when a credit card is submitted, which ends the trial; the upgrade screen asks for credit or debit card details | capture: sha256:0c57f82584a97c5cef97da4e4cd970aa6453ea7e1259f9b3ff1bed638f34b3ab | quote: In summary, you will never be charged for any type of usage during the trial period, but the trial period ends when you submit a credit card and become a paid subscriber.
  - [2] 2026-10-30: an inefficient non-validated application may be limited or suspended; the same page gives the egress policy and the 90-day deleted-storage charge | capture: sha256:29e7011551e06ea9d40f2f3102982e0ad533420100f53974e641c958af416c4c | quote: If you are using a non-validated application that imposes an inefficient and unreasonable load on the Wasabi service, we reserve the right to limit or suspend your service
  - [1] 2026-10-30: the pricing table is first-party and prints the egress and API fee line as USD 0 on both models | capture: sha256:7c80b45579da69df1114c7d9c9d9a44ee1833e4b93faf2fe13b2ceebd22e8181 | quote: | Egress & API fees | $0 | $0 |
  - [4] 2026-10-30: the trial needs no card; the sign-up form asks for first and last name, phone number, company name, work email address and country, and MFA is required on a trial account | capture: sha256:1d986e4259a5a89260671af47a21692d9de49646b7710c394b7ca7ec3b879528 | quote: You can use your free trial to store data without the requirement of a credit card.
  - [5] 2026-10-30: the trial holds 100 GB for 30 days on a company email domain and 10 GB for 14 days on a freemail domain, with no credit card | capture: sha256:29b4cf5fdc60f12c6760ce380b151ce3a401c1330f7a826d70147f0af4499055 | quote: Company email domain: 100 GB for 30 days
  - [1] 2026-10-30: Pay as You Go carries a minimum monthly charge tied to 1 TB of active storage; Reserved Capacity starts at 25 TB and Pay as You Go lists a credit card as its contract term | capture: sha256:7c80b45579da69df1114c7d9c9d9a44ee1833e4b93faf2fe13b2ceebd22e8181 | quote: | Minimum monthly charge | Yes, tied to 1TB active storage per account | No separate minimum. Cost fixed to purchased block |
  - [5] 2026-11-04: the trial needs no credit card | capture: sha256:f91a5afa4272e0ea284dd05d2229609b001f5beb62e859f552de7e662628828b | quote: No credit card required to get started
  - [1] 2026-11-04: Pay as You Go is USD 7.99 per TB per month | capture: sha256:7c80b45579da69df1114c7d9c9d9a44ee1833e4b93faf2fe13b2ceebd22e8181 | quote: | Price per TB | $7.99/month | Discounts determined by both the storage capacity purchased and the contract term length |
  - [1] 2026-11-04: egress and API fees are USD 0 on both models | capture: sha256:7c80b45579da69df1114c7d9c9d9a44ee1833e4b93faf2fe13b2ceebd22e8181 | quote: | Egress & API fees | $0 | $0 |
- sources:
  - [1] https://wasabi.com/pricing
  - [2] https://wasabi.com/pricing/faq
  - [3] https://docs.wasabi.com/docs/upgrading-to-a-paid-plan
  - [4] https://docs.wasabi.com/docs/signing-up-for-wasabi
  - [5] https://wasabi.com/free-trial
