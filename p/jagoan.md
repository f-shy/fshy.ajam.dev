# Jagoan Cloud

> jagoan.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jagoan/ | JSON https://fshy.ajam.dev/api/v1/entity/jagoan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jagoan Cloud

- `compute/jagoan-cloud` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T06:20:47.021Z (live) | stale on 2026-12-05
- url https://jagoan.cloud/registration/
- free tier: IDR 150,000 of credit for a 30-day trial, granted on registration with an email address, advertised on the registration form itself as 'Get Free IDR 150.000 Credit Bonus for 30 Days Trial'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-shot-credit
- per-object cap: not applicable | source: [1]
- retention: The credit expires after 30 days and the account is an OVZ NAT container with a 20 Mbps cap and no public IPv4 until it is upgraded to paid, so the free unit is time-boxed and reaches the network only over IPv6. | source: [1]
- egress: not published: no egress allowance or overage price on https://jagoancloud.com/harga-managed-vps/ or on the registration page, read 2026-11-04 | metered: no | source: [1]
- identity: any-phone | detail: the registration form marks Name, Email, Phone, City, Company Size and Job Title as required; no card field is on the form; whether the phone number is verified is not stated
- interface: ssh, cli
- limits:
  - retention-clamped (binding): The credit expires after 30 days and the account is an OVZ NAT container with a 20 Mbps cap and no public IPv4 until it is upgraded to paid, so the free unit is time-boxed and reaches the network only over IPv6. [1]
- limits note: The credit expires after 30 days and the account is an OVZ NAT container with a 20 Mbps cap and no public IPv4 until it is upgraded to paid, so the free unit is time-boxed and reaches the network only over IPv6.
- binding note: the same as limits note
- interface detail: dashboard plus SSH (Web SSH) to nodes and a kubectl client against a Remote API endpoint with an access token, as documented for Kubernetes clusters on the platform
- tooling: the provider documents the kubectl client, per the cluster access page: "kubectl"
- composes with: IDR 150,000 is about USD 9 at the shown rate, which is one month of a 768 MB instance; the free tier therefore buys exactly the trial period and nothing that survives it, and it composes with a paid IDR 45,182 box only by upgrading.
- reliability: no reliability event recorded
- notes: The Indonesian market is the most active source of free VPS offers found among evaluated offerings, and most of them are small operators with no English page. Jagoan is the most durable of them because it is the free arm of a long-established host with a published paid ladder. The IPv6-only free tier with NAT IPv4 is the real constraint: the box is reachable, but not as a server with a stable inbound address until money changes hands.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: one-shot-credit
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the registration page headline reads 'Get Free IDR 150.000 Credit Bonus for 30 Days Trial', quoted from the vendor's own signup form
  - [2] 2026-10-22: a user report states the free account is 'OVZ NAT VPS' with a '20Mbps' cap, no public IPv4 on the free tier, and that a '768MB' instance roughly consumes the IDR 150,000 over a month; the lowest paid tier is '45182IDR' for 1 core, 128 MB and 50 GB at 200 Mbps unlimited, reported
  - [3] 2026-10-22: the paid ladder beside it: 'Nebula' 2 Core / 2 GB / 40 GB at 'Rp. 100.000 /bln' after discount from Rp. 200.000, with a 30-day money-back guarantee, quoted
  - [4] 2026-11-04: the pricing page prices storage per GB-month and carries no traffic-out allowance or price | capture: sha256:389646bfd65cfb6bbd9a6a468d9a8268845df759d49a8232efdf02435de66360 | quote: Biayanya adalah Rp 3.000,- per 1 GB tiap bulan.
  - [5] 2026-11-04: the registration form marks a phone number as required | capture: sha256:1af94ecf9c73d8016506d74e69896093923ca64b7e72e3ebd4b41b939024ea5f | quote: Phone *
  - [5] 2026-11-04: the registration form now advertises a 14-day trial credit with no amount | capture: sha256:1af94ecf9c73d8016506d74e69896093923ca64b7e72e3ebd4b41b939024ea5f | quote: Get Free Credit Bonus for 14 Days Trial
  - [6] 2026-11-04: the provider's own docs tell the user to reach nodes over SSH and to use kubectl against a Remote API endpoint with an access token | capture: sha256:ffcad3577ffc73e08a32ed63ad60060912a6867ca169036346d79ac2688b53e0 | quote: cukup sambungkan ke node yang diperlukan melalui SSH.
  - [6] 2026-11-04: the cluster access page names the kubectl client | capture: sha256:ffcad3577ffc73e08a32ed63ad60060912a6867ca169036346d79ac2688b53e0 | quote: Kamu bisa langsung mulai bekerja dengan cluster menggunakan kubectl, cukup sambungkan ke node yang diperlukan melalui SSH.
- sources:
  - [1] https://jagoan.cloud/registration/
  - [2] https://maobuni.com/2022/09/02/jagoan-freevps/
  - [3] https://www.jagoanhosting.com/harga-vps/
  - [4] https://jagoancloud.com/harga-managed-vps/
  - [5] https://jagoancloud.com/registration/
  - [6] https://jagoancloud.com/docs/docs/cluster-access/
