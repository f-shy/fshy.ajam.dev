# Phala Cloud

> phala.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/phala/ | JSON https://fshy.ajam.dev/api/v1/entity/phala.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Phala Cloud

- `compute/phala-cloud` | paid-only | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-24T13:21:01.720Z (live) | stale on 2026-12-25
- url https://cloud.phala.com/about/pricing
- free tier: no free tier: the smallest CPU instance is 1 vCPU / 2 GB at USD 0.058 an hour; storage is USD 0.000139 per GB an hour while the machine runs or is stopped, billed by the minute with no subscription or minimum. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable: the unit is a machine; the smallest disk is 20 GB and the smallest CPU shape is 1 vCPU / 2 GB | source: [1]
- retention: the data of a stopped machine is kept for 30 days after the Balance reaches zero; after that it may be deleted | source: [1]
- egress: Each machine includes bandwidth based on its size; no per-GB egress allowance or rate is published | metered: no | source: [1]
- identity: card | detail: Signup is with GitHub, Google or email and password; a card or a Balance top-up is added next. Adding a card runs a refundable USD 1 check. Some new workspaces are offered a welcome credit when they add a card; phone number and identity document are not asked for on the page read.
- interface: ssh
- limits:
  - write-gated (binding): The documentation's first step after signup is 'add a card or top up your Balance to start deploying', so no CVM exists without a payment instrument. [2]
- limits note: The documentation's first step after signup is 'add a card or top up your Balance to start deploying', so no CVM exists without a payment instrument.
- binding note: the same as limits note
- interface detail: SSH on dev OS images through the CLI gateway tunnel with an SSH key; a Cloud API and a public HTTPS gateway for deployed services
- tooling: the phala CLI, Cloud API and an SSH client; the CLI handles the SSH gateway tunnel
- composes with: Phala is the cheapest attested-TEE lane found among the category's DePIN records, but it is a prepaid invoice rather than a credit, so it does not chain with a zero-budget start.
- reliability: no reliability event recorded
- notes: Private AI inference is a separate metered product billed from the workspace Balance; gifted credits do not pay for it. A TEE model endpoint is listed at https://inference.phala.com/v1.
- extras:
  - facets.class: paid-cloud
  - facets.shape.gpu_class: H100/H200/B300 TEE
- evidence:
  - [3] 2026-10-22: signup with GitHub, Google or email, then 'add a card or top up your Balance to start deploying'
  - [3] 2026-11-24: the quick start states the signup methods and the card or top-up gate | capture: sha256:547383fb36172cc3886adeeb84120e205a786db9b4d23a3743102cc81a5c2a54 | quote: Sign up at [cloud.phala.com/register](https://cloud.phala.com/register) with GitHub, Google, or email. Then add a card or top up your Balance to start deploying.
  - [1] 2026-11-24: Phala CPU instances are billed by the minute with no subscription or minimum | capture: sha256:65f24b97da90c9be2d90f961364c42c44d2900479b7fc6edaa87a6a64adb2b47 | quote: Prices are shown per hour. We charge only for the minutes your machine runs. There is no subscription and no minimum.
  - [1] 2026-11-24: the smallest disk on a Phala CVM is 20 GB | capture: sha256:65f24b97da90c9be2d90f961364c42c44d2900479b7fc6edaa87a6a64adb2b47 | quote: - The smallest disk is 20 GB.
  - [4] 2026-11-24: stopped-machine data is retained for 30 days | capture: sha256:70cb9b8dc15072db3f2990d992c9387144802756e5eb13fc80682c2717dd71c0 | quote: - We keep the data of stopped machines for 30 days. After that, we may delete it.
  - [1] 2026-11-24: bandwidth is included with each machine and no per-GB rate is published | capture: sha256:65f24b97da90c9be2d90f961364c42c44d2900479b7fc6edaa87a6a64adb2b47 | quote: - Each machine includes bandwidth based on its size.
  - [5] 2026-11-24: SSH access to a CVM is documented with an SSH key on dev OS images | capture: sha256:eda5ca4f6beffe9378405a5c87be92f6e7407ab1f9387fae383af7a3fb73b19e | quote: SSH works only on dev OS images. Select "dstack-dev" when you create your CVM. Production images have SSH turned off for security. You sign in with an SSH key. Passwords do not work.
  - [5] 2026-11-24: the documented SSH route is through the CLI's gateway tunnel | capture: sha256:eda5ca4f6beffe9378405a5c87be92f6e7407ab1f9387fae383af7a3fb73b19e | quote: The Phala CLI connects you through the secure gateway tunnel in one command.
  - [5] 2026-11-24: the vendor documents a CLI as a user for SSH access | capture: sha256:eda5ca4f6beffe9378405a5c87be92f6e7407ab1f9387fae383af7a3fb73b19e | quote: The Phala CLI connects you through the secure gateway tunnel in one command.
  - [2] 2026-11-24: a card or a top-up is needed before deployment, with a refundable USD 1 card check | capture: sha256:deee52480c34ecb1d2c6d712d24cd639d0d493998ff5f1096be2591b9c4d1c4c | quote: After registration, set up your workspace. Add a card, or skip it and top up your Balance instead. When you add a card, we charge \$1 to check it and refund it right after.
  - [2] 2026-11-24: the registration gate is a social login or an email address and password | capture: sha256:deee52480c34ecb1d2c6d712d24cd639d0d493998ff5f1096be2591b9c4d1c4c | quote: Sign up with GitHub, Google, or email and password. Registration takes under a minute.
  - [1] 2026-11-24: Private AI inference is paid from the workspace Balance rather than gifted credit | capture: sha256:65f24b97da90c9be2d90f961364c42c44d2900479b7fc6edaa87a6a64adb2b47 | quote: Private AI is paid from your Balance.
  - [6] 2026-11-24: the smallest CPU instance is 1 vCPU / 2 GB at USD 0.058 an hour | capture: sha256:ee3f7825d1a3eb0445d5205f6db6cf5724301adbf0dfbad62f75f4344b913ca2 | quote: | tdx.small | Small TDX Instance | 1 | 2 GB | $0.058 |
  - [1] 2026-11-24: storage is charged per GB-hour while the machine runs or is stopped | capture: sha256:65f24b97da90c9be2d90f961364c42c44d2900479b7fc6edaa87a6a64adb2b47 | quote: Storage costs $0.000139 per GB per hour, which is about $0.10 per GB per month.
  - [2] 2026-11-24: registration is followed by a card or top-up gate | capture: sha256:deee52480c34ecb1d2c6d712d24cd639d0d493998ff5f1096be2591b9c4d1c4c | quote: After registration, set up your workspace. Add a card, or skip it and top up your Balance instead.
  - [4] 2026-11-24: stopped-machine data is retained 30 days | capture: sha256:70cb9b8dc15072db3f2990d992c9387144802756e5eb13fc80682c2717dd71c0 | quote: - We keep the data of stopped machines for 30 days. After that, we may delete it.
  - [5] 2026-11-24: the CLI is the client for SSH access to a CVM | capture: sha256:eda5ca4f6beffe9378405a5c87be92f6e7407ab1f9387fae383af7a3fb73b19e | quote: That's it. The CLI handles the gateway tunnel and SSH configuration automatically.
  - [1] 2026-11-24: the live CPU instance rates and billing rules are stated on this page | capture: sha256:65f24b97da90c9be2d90f961364c42c44d2900479b7fc6edaa87a6a64adb2b47 | quote: Prices are shown per hour. We charge only for the minutes your machine runs. There is no subscription and no minimum.
  - probe:https://inference.phala.com/v1 2026-11-24: the TEE inference base path answered HTTP 404 | capture: sha256:c29dbcd559efebbbc5fdf0351e1f840d3a6808283bbd94d6b13087af9f5db757 | quote: "status": 404
- sources:
  - [1] https://cloud.phala.com/about/pricing
  - [2] https://docs.phala.com/phala-cloud/getting-started/sign-up-for-cloud-account.md
  - [3] https://docs.phala.network/phala-cloud/getting-started
  - [4] https://cloud.phala.com/about/billing
  - [5] https://docs.phala.com/phala-cloud/networking/enable-ssh-access.md
  - [6] https://cloud.phala.com/about/instance-types
