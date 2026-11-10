# sourcehut

> sr.ht | CI runners, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sr/ | JSON https://fshy.ajam.dev/api/v1/entity/sr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SourceHut builds.sr.ht

- `ci-cd-runners/sourcehut-builds` | paid-only | evidence documented | binding write-gated | category CI runner | tier paid account
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:00:39.390Z (live) | stale on 2026-12-05
- url https://man.sr.ht/builds.sr.ht/
- free tier: no free allowance: builds.sr.ht requires a paid account (EUR 4 or USD 4 a month at the lowest tier, every tier with the same service and limits) for users registered on or after 2021-05-01; free service is issued to a user who emails support explaining that they cannot pay | unit: none | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: 1 GiB per artifact file; the hosted build time limit is not published, the documented SSH message reads 'Your VM will be terminated 4 hours from now', and the software's example configuration sets a 45-minute maximum build duration | bytes: 1073741824 | source: [2]
- retention: artifacts are uploaded only for successful jobs and pruned after 90 days | days: 90 | source: [2]
- egress: unverified: no egress terms were found in the pages read | metered: no | source: [1]
- identity: card | detail: a meta.sr.ht account registered as a maintainer with payment by credit card, SEPA direct debit, iDEAL or Bancontact; free service is issued on an emailed request to support; a contributor account without payment cannot submit builds
- interface: git, ssh, graphql, cli
- limits:
  - write-gated (binding): submitting build jobs needs a paid account; free service only after an emailed request to support [3]
  - per-object-cap: 1 GiB per artifact file [2]
  - retention-clamped: artifacts pruned after 90 days, uploaded only for successful jobs [2]
- limits note: the hosted runner size and per-user concurrency are not published; the build image control script boots each VM with 2 CPUs and 4096 MB of memory unless configured otherwise, and a build host of 16 cores and 128 GB supports up to 16 parallel build slots; a failed build's VM stays up 10 more minutes for SSH
- binding note: nothing runs without a payment or an aid grant; once paid, every tier has the same service limits
- interface detail: a YAML build manifest submitted through the API, the web form at builds.sr.ht/submit, a manifest in a git.sr.ht or hg.sr.ht repository, patches sent to a mailing list, or the hut CLI; SSH into a running or failed build VM
- tooling: full virtual machines with root through sudo, on x86_64 images (the only native architecture in the image table); the hut CLI. SourceHut is AGPL-3.0 software the user can install and run on a rented or free machine, which comes after the hosted service
- composes with: a paid or aid-granted account gets full VMs with root and SSH access; artifacts leave through the jobs page and are pruned at 90 days
- reliability: the service is in public alpha; from the beta, unpaid accounts become read-only for their own projects, with at least 60 days notice by email; pricing is set to change after the alpha
- notes: Not free hosted CI: builds.sr.ht has needed a paid account since 2021-05-01, at EUR 4 or USD 4 a month for the whole service, with free service granted on an emailed request. The hosted runner size, job time limit and concurrency are not published; the repository defaults are 2 CPUs, 4096 MB and 45 minutes.
- evidence note: the pricing, billing FAQ, builds billing-change, alpha, builds and manifest pages were read and quoted on 2026-10-30; runner size and the 45-minute timeout come from the open-source repository's defaults, not from the hosted service, and no build was run.
- evidence:
  - [1] 2026-10-30: builds.sr.ht requires payment | capture: sha256:b2c866d2b73759d911ec46fe4ecce60f0f4fc6cfae4692d7f5b019f68bbe9494 | quote: | builds.sr.ht | Required | chat.sr.ht | Required |
  - [1] 2026-10-30: the lowest tier is EUR 4 or USD 4 a month | capture: sha256:b2c866d2b73759d911ec46fe4ecce60f0f4fc6cfae4692d7f5b019f68bbe9494 | quote: | Amateur hackers | €4/mo† | $4/mo |
  - [3] 2026-10-30: submitting build jobs needs a paid account | capture: sha256:784c327f2a7926dddda17681f175b0ef0e70c1c7c01e9b821fd9638ad9c83628 | quote: To create repositories, mailing lists, trackers, or submit build jobs, you will need to pay for your account.
  - [3] 2026-10-30: free service is issued on an emailed request | capture: sha256:784c327f2a7926dddda17681f175b0ef0e70c1c7c01e9b821fd9638ad9c83628 | quote: you can simply send us an email explaining your situation, and you will be issued free service.
  - [3] 2026-10-30: every tier has the same limits | capture: sha256:784c327f2a7926dddda17681f175b0ef0e70c1c7c01e9b821fd9638ad9c83628 | quote: There is no difference between any of the plans: they all have access to the same level of service, and the same service limits.
  - [3] 2026-10-30: payment by credit card | capture: sha256:784c327f2a7926dddda17681f175b0ef0e70c1c7c01e9b821fd9638ad9c83628 | quote: - Major credit cards
  - [3] 2026-10-30: payment by SEPA direct debit | capture: sha256:784c327f2a7926dddda17681f175b0ef0e70c1c7c01e9b821fd9638ad9c83628 | quote: SEPA direct debits
  - [3] 2026-10-30: the software is AGPL-3.0 | capture: sha256:784c327f2a7926dddda17681f175b0ef0e70c1c7c01e9b821fd9638ad9c83628 | quote: sr.ht is 100% free software, mostly licensed under the GNU Affero General Public license (aka AGPL 3.0).
  - [4] 2026-10-30: builds became paid for users registered from 2021-05-01 | capture: sha256:0ed15eb13d462403c0c49f9a6f2b11780cfa290d76ec656ef0117672d34b8180 | quote: All new users who register on or after 2021-05-01 will be required to pay for their account to use builds.sr.ht.
  - [5] 2026-10-30: a maintainer account is a paid account with financial aid available | capture: sha256:b9042fcca29a51668bc0a37b7a5c3472ed85124c9dadc8e0c7e8b6b289a2a082 | quote: Projects hosted on sourcehut are expected to pay for their account. Financial aid is available for those in need.
  - [6] 2026-10-30: builds run in full VMs with root | capture: sha256:c4ac25cbf4a3689edfe2f30997e3b013ce000dcc92a1d7ce249fde1d5cddd2f3 | quote: These are full virtual machines with relatively broad permissions offered to users
  - [6] 2026-10-30: the documented SSH session message names a 4-hour termination | capture: sha256:c4ac25cbf4a3689edfe2f30997e3b013ce000dcc92a1d7ce249fde1d5cddd2f3 | quote: Your VM will be terminated 4 hours from now, or when you log out.
  - [6] 2026-10-30: manifests are submitted through the API or the website | capture: sha256:c4ac25cbf4a3689edfe2f30997e3b013ce000dcc92a1d7ce249fde1d5cddd2f3 | quote: these manifests are submitted via the API or ad-hoc on the website
  - [7] 2026-10-30: an SSH session lasts until the normal build time limit | capture: sha256:3b2c43240590c262e34983c66cdc8415458d000aab53bd0655bd9865ec06fc26 | quote: we keep the VM alive until you log out or until your normal build time limit has elapsed.
  - [2] 2026-10-30: 1 GiB per artifact, pruned after 90 days | capture: sha256:daf7002ac828a390aefb835fc2a3b16f17e44b4f0708edf1d8a1fbfe4869bf12 | quote: The maximum allowed file size of an artifact file is 1 GiB. Artifacts are only uploaded for successful jobs and are pruned after 90 days.
  - [8] 2026-10-30: x86_64 is the supported native architecture | capture: sha256:0c385517baef4e87d4aefbe264ec3208ebff1b99b5be345e9ce744d24419f8aa | quote: | `arch: x86_64` (default) | ✓ | ✓ | daily |
  - [9] 2026-10-30: a build host supports up to 16 parallel build slots | capture: sha256:817a61b0f6e0543aed2b2f052bbff95413e292adef7a8c80d392244b91c55d89 | quote: This configuration supports up to 16 parallel build slots.
  - [10] 2026-10-30: the control script boots each build VM with 2 CPUs | capture: sha256:f99f74a7ac8407f81520cb495cfd6eb921ba86e4e56bd862a0b3af53f82b06b5 | quote: -smp cpus=2 \
  - [10] 2026-10-30: the control script defaults to 4096 MB of memory | capture: sha256:f99f74a7ac8407f81520cb495cfd6eb921ba86e4e56bd862a0b3af53f82b06b5 | quote: -m ${MEMORY:-4096} \
  - [11] 2026-10-30: the example configuration sets a 45-minute maximum build duration | capture: sha256:7551b93f29ab225daf873adca23253135fe4fee6f8190ec94f5e8c524a2bf187 | quote: timeout=45m
  - [12] 2026-10-30: unpaid accounts become read-only from the beta with 60 days notice | capture: sha256:9aa72cbabb5f65b42d11142bf81eb5899b130d69eb1277d877e0a161279999a0 | quote: From the beta onwards, unpaid accounts will be limited to read-only access to their own projects. Affected users will be emailed at least 60 days in advance of the transition.
  - [2] 2026-11-02: the artifact size cap and the 90-day pruning are unchanged | capture: sha256:daf7002ac828a390aefb835fc2a3b16f17e44b4f0708edf1d8a1fbfe4869bf12 | quote: The maximum allowed file size of an artifact file is 1 GiB. Artifacts are only uploaded for successful jobs and are pruned after 90 days.
  - [3] 2026-11-04: build jobs need a paid account | capture: sha256:784c327f2a7926dddda17681f175b0ef0e70c1c7c01e9b821fd9638ad9c83628 | quote: To create repositories, mailing lists, trackers, or submit build jobs, you will need to pay for your account.
  - [2] 2026-11-04: 1 GiB artifact cap | capture: sha256:daf7002ac828a390aefb835fc2a3b16f17e44b4f0708edf1d8a1fbfe4869bf12 | quote: The maximum allowed file size of an artifact file is 1 GiB.
- sources:
  - [1] https://sourcehut.org/pricing/
  - [2] https://man.sr.ht/builds.sr.ht/manifest.md
  - [3] https://man.sr.ht/billing-faq.md
  - [4] https://man.sr.ht/ops/builds.sr.ht-migration.md
  - [5] https://meta.sr.ht/register
  - [6] https://man.sr.ht/builds.sr.ht/
  - [7] https://drewdevault.com/blog/Introducing-shell-access-for-builds/
  - [8] https://man.sr.ht/builds.sr.ht/compatibility.md
  - [9] https://man.sr.ht/ops/provisioning.md
  - [10] https://git.sr.ht/~sircmpwn/builds.sr.ht/blob/master/images/control
  - [11] https://git.sr.ht/~sircmpwn/builds.sr.ht/blob/master/config.example.ini
  - [12] https://sourcehut.org/alpha-details/

## sourcehut (sr.ht)

- `storage/sourcehut` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://man.sr.ht/git.sr.ht/
- free tier: none reachable: No published quota, but the resource guidance is 'aim to have repos no larger than the Linux kernel git repo, which is 6 GiB' and 'Don't store lots of large binary objects'. Payment is… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published quota, but the resource guidance is 'aim to have repos no larger than the Linux kernel git repo, which is 6 GiB' and 'Don't store lots of large binary objects'. Payment is…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No published quota, but the resource guidance is 'aim to have repos no larger than the Linux kernel git repo, which is 6 GiB' and 'Don't store lots of large binary objects'. Payment is…
  - [2] 2026-10-21: cited as the basis of the rejection: No published quota, but the resource guidance is 'aim to have repos no larger than the Linux kernel git repo, which is 6 GiB' and 'Don't store lots of large binary objects'. Payment is expec
  - [3] 2026-10-21: cited as the basis of the rejection: No published quota, but the resource guidance is 'aim to have repos no larger than the Linux kernel git repo, which is 6 GiB' and 'Don't store lots of large binary objects'. Payment is expec
- sources:
  - [1] https://man.sr.ht/git.sr.ht/
  - [2] https://sourcehut.org/alpha-details/
  - [3] https://sourcehut.org/pricing/

## sourcehut (sr.ht) git

- `storage/sourcehut-git` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://man.sr.ht/git.sr.ht/
- free tier: None reachable: No Git LFS support at all. The project's own guidance is 'aim to have repos no larger than the Linux kernel git repo, which is 6 GiB' and 'Don't store lots of large binary objects in your r. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No Git LFS support at all — the project's own guidance is 'aim to have repos no larger than the Linux kernel git repo, which is 6 GiB' and 'Don't store lots of large binary objects in your…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No Git LFS support at all — the project's own guidance is 'aim to have repos no larger than the Linux kernel git repo, which is 6 GiB' and 'Don't store lots of large binary objects in your…
- sources:
  - [1] https://man.sr.ht/git.sr.ht/
