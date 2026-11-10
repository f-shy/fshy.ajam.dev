# Drone CI

> drone.io | Storage, CI runners, Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/drone/ | JSON https://fshy.ajam.dev/api/v1/entity/drone.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## drone ci (cloud.drone.io)

- `storage/drone-ci` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T00:32:21.383Z (inherited) | stale on 2026-11-18
- url https://docs.drone.io/
- free tier: none: cloud.drone.io is not accepting new registrations, with no target date to reopen (vendor support reply, April 2022) | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: cloud.drone.io is not accepting new registrations, with no target date to reopen (vendor support reply, April 2022); the address still answers and its sign-in hands off to GitHub, so the service is closed to new accounts rather than gone. It is a CI service and documents no storage surface
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: registration-closed
  - dead_end.why: The hosted cloud service is effectively gone — cloud.drone.io returns 303 with no usable public artifact surface. Drone now ships as self-hosted Community/Enterprise Edition only, so there…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The hosted cloud service is effectively gone — cloud.drone.io returns 303 with no usable public artifact surface. Drone now ships as self-hosted Community/Enterprise Edition only, so there…
  - [2] 2026-10-21: cited as the basis of the rejection: The hosted cloud service is effectively gone — cloud.drone.io returns 303 with no usable public artifact surface. Drone now ships as self-hosted Community/Enterprise Edition only, so there i
  - [3] 2026-11-03: the vendor's support reply of 14 April 2022: cloud.drone.io takes no new registrations | capture: sha256:bf03461be8e8b4d40e69394cbbbd2d933c75ffe5ca52ebfa6d6cd62f9aad56e5 | quote: Currently, [cloud.drone.io](http://cloud.drone.io) is not accepting new registrations.
  - [4] 2026-11-03: the cloud.drone.io sign-in still answers and hands off to a GitHub OAuth sign-in for the cloud.drone.io app | capture: sha256:51ca33de43c325cedac3606278b49b17fed05bf3fb4c43f326d3bbff9e8726f6 | quote: to continue to cloud.drone.io
  - probe:cloud.drone.io 2026-11-03: cloud.drone.io answers: the root redirects (303) to /welcome, which returns HTTP 200 | capture: sha256:741eb5effc80f795e2c357bee1ebcde43ecf25417690d9a0c9f14dda8844f606 | quote: "status": 200
- sources:
  - [1] https://docs.drone.io/
  - [2] https://cloud.drone.io/
  - [3] https://drone.discourse.group/t/user-registration-is-disabled-on-cloud-drone-io/11904
  - [4] https://cloud.drone.io/login

## Drone CI (CI runners)

- `ci-cd-runners/drone-ci` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category CI software
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:32:21.382Z (live) | stale on 2026-12-04
- url https://www.drone.io/
- free tier: free software, no hosted lane: the Open Source Edition is Apache 2.0 with no licence fee and is built from source, and the Enterprise Edition image is free for individuals; cloud.drone.io is not accepting new registrations | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: there is no hosted service to cap
- retention: not applicable | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: the software needs no account
- interface: git, cli
- limits:
  - write-gated (binding): no hosted tier exists, so the path is a self-hosted deployment [2]
- interface detail: a server and one or more runners that the user installs; a runner is a standalone daemon that polls the server for pipelines, and the server signs users in through a forge such as GitHub, GitLab, Gitea or Bitbucket
- tooling: the user installs and runs the drone-server (the Enterprise Edition image from Docker Hub, or the Open Source Edition built from source with the oss build tag) and one or more runner daemons on a rented or free machine
- composes with: for a hosted lane, the vendor's support reply points cloud.drone.io users to its hosted Harness CI (ci-cd-runners/harness-ci-free); the self-hosted last resort is Woodpecker, the maintained fork of the same design
- reliability: cloud.drone.io is not accepting new registrations, with no target date to reopen (vendor support reply, April 2022); its sign-in still answers and hands off to GitHub. The vendor keeps Drone as a snapshot branch of harness/harness and presents Harness Open Source as its next generation
- evidence note: the editions and their pricing are quoted from docs.drone.io/enterprise and drone.io/enterprise/opensource; the closed registration of cloud.drone.io is quoted from the vendor's support forum, the newest first-party statement found
- self hosted: yes
- evidence:
  - [2] 2026-10-22: Woodpecker is presented as the community continuation of the Drone CI design, with a server and agents
  - [3] 2026-10-30: the Open Source Edition is free software under Apache 2.0; the same page says the Enterprise Edition is free for individuals | capture: sha256:4685dd24a188e4cf139d2bb4ef3f6c960cc45f44150ddbe16435deab52bf0adb | quote: The Open Source Edition is Free and Open Source software licensed under the Apache2 License.
  - [4] 2026-10-30: drone.io lists the open-source edition's pricing as Free, licence Apache 2.0 | capture: sha256:22d790f8a3f91a62c10df4b55dd6a2250456bfcd2ed7fa50d532ebe61d8d8cfc | quote: Pricing [Free](https://docs.drone.io/server/overview/)
  - [5] 2026-10-30: the vendor's support reply of 14 April 2022: cloud.drone.io takes no new registrations, with no target date | capture: sha256:bf03461be8e8b4d40e69394cbbbd2d933c75ffe5ca52ebfa6d6cd62f9aad56e5 | quote: Currently, [cloud.drone.io](http://cloud.drone.io) is not accepting new registrations.
  - [6] 2026-10-30: the cloud.drone.io login redirects to a GitHub OAuth sign-in for the cloud.drone.io app | capture: sha256:c3834026f822ee2084be8e9141bda47b62c3e21b2e7cb3737e91c573577cb5cf | quote: to continue to cloud.drone.io
  - [7] 2026-10-30: the vendor presents Harness Open Source as the next generation of Drone and keeps Drone on a drone branch | capture: sha256:df8df25a18d6d26c9437046188a53398aa218ade7b2b92f4a9689ea08aae6e89 | quote: Harness Open Source represents a massive investment in the next generation of Drone.
  - [8] 2026-10-30: Drone is a server plus runner daemons that poll it, installed against a source control provider | capture: sha256:61173b9e8646bc16e77f21b2a8a85c6f3a11aa62c0bbf2c3ee1fdc8ba334d334 | quote: A runner is a standalone daemon that polls the server for pending pipelines to execute.
  - [3] 2026-10-30: the Open Source Edition is built from source; the Enterprise Edition downloads from Docker Hub | capture: sha256:4685dd24a188e4cf139d2bb4ef3f6c960cc45f44150ddbe16435deab52bf0adb | quote: There is no official distribution of the Open Source Edition.
  - [3] 2026-10-30: the vendor documents its editions on docs.drone.io/enterprise | capture: sha256:4685dd24a188e4cf139d2bb4ef3f6c960cc45f44150ddbe16435deab52bf0adb | quote: There are two versions of Drone.
  - [1] 2026-10-30: the software downloads with no account, sales contact or trial licence | capture: sha256:8cb9169fa90cd9756a86bcb38f95ddad600b0e8d69c5fff39d9ee6b473ee2c20 | quote: Download our official Docker image or build from source. No need to talk with a sales person or request a trial license.
  - [5] 2026-11-03: the same reply points cloud.drone.io users to the vendor's hosted CI on harness.io | capture: sha256:bf03461be8e8b4d40e69394cbbbd2d933c75ffe5ca52ebfa6d6cd62f9aad56e5 | quote: or check out our hosted CI solution at: [Continuous Integration Platform: Self-Service & On-Demand](https://harness.io/products/continuous-integration)
  - [5] 2026-11-03: the vendor's support reply of 14 April 2022: cloud.drone.io takes no new registrations | capture: sha256:bf03461be8e8b4d40e69394cbbbd2d933c75ffe5ca52ebfa6d6cd62f9aad56e5 | quote: Currently, [cloud.drone.io](http://cloud.drone.io) is not accepting new registrations.
  - [5] 2026-11-03: the vendor gave no target date to reopen registration | capture: sha256:bf03461be8e8b4d40e69394cbbbd2d933c75ffe5ca52ebfa6d6cd62f9aad56e5 | quote: We don’t have a target date for when [cloud.drone.io](http://cloud.drone.io) will accept new registrations.
  - probe:cloud.drone.io 2026-11-03: cloud.drone.io answers: the root redirects (303) to /welcome, which returns HTTP 200 | capture: sha256:741eb5effc80f795e2c357bee1ebcde43ecf25417690d9a0c9f14dda8844f606 | quote: "status": 200
- sources:
  - [1] https://www.drone.io/
  - [2] https://woodpecker-ci.org/docs/intro
  - [3] https://docs.drone.io/enterprise/
  - [4] https://www.drone.io/enterprise/opensource
  - [5] https://drone.discourse.group/t/user-registration-is-disabled-on-cloud-drone-io/11904
  - [6] https://cloud.drone.io/login
  - [7] https://github.com/harness/drone
  - [8] https://docs.drone.io/server/overview/

## Drone CI (Compute)

- `compute/drone-ci` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category CI runner
- needs card no, phone no, ID no, institution no | verified 2026-10-30T12:41:24.477Z (live) | stale on 2026-11-30
- url https://cloud.drone.io
- duplicate of `ci-cd-runners/drone-ci`
- free tier: free software, no hosted lane: the Open Source Edition is Apache 2.0 with no licence fee and is built from source, and the Enterprise Edition image is free for individuals; cloud.drone.io is not accepting new registrations | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none-hosted
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous | detail: the software downloads with no account or trial licence; the closed hosted lane cloud.drone.io signs in through GitHub
- interface: unknown
- limits:
  - write-gated (binding): The missing hosted service fails first: there is no registration path, so the hosted capacity is zero, and the only way to use Drone is to run the server and agents on machines the user supplies. [1]
- limits note: The missing hosted service fails first: there is no registration path, so the hosted capacity is zero, and the only way to use Drone is to run the server and agents on machines the user supplies.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None. It is a piece of software that needs a machine.
- reliability: no reliability event recorded
- notes: Classified as paid-only rather than dead because the software is alive and maintained; what is gone is the hosted lane, and the two lead a reader to different decisions. This is the case an earlier rule is written for: a provider whose software is fine and whose free hosted capacity does not exist. The 2022 forum date is also the staleness warning: a 200 on the domain would have read as live to any check that did not look for a registration path.
- self hosted: yes
- extras:
  - facets.class: ci-runner-capacity
  - facets.free_tier_kind: none-hosted
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: HTTP 200 with a Cloudflare front, and no registration route
  - [2] 2026-10-22: 'Unable to register with my github account on cloud.drone.io', posted 13 April 2022, and the thread title is the maintainers' own statement of the state
  - [3] 2026-10-22: 'Drone is a self-service Continuous Integration platform for busy development teams' with pipelines running in containers; the site sells the software and offers no hosted tier
  - [4] 2026-10-22: the repository now describes Harness Open Source as 'an end-to-end developer platform with Source Control Management, CI/CD Pipelines, Hosted Developer Environments, and Artifact Registries', last pushed 2026-10-22
  - [5] 2026-10-30: the Open Source Edition is free software under Apache 2.0 | capture: sha256:4685dd24a188e4cf139d2bb4ef3f6c960cc45f44150ddbe16435deab52bf0adb | quote: The Open Source Edition is Free and Open Source software licensed under the Apache2 License.
  - [6] 2026-10-30: drone.io lists the open-source edition's pricing as Free, licence Apache 2.0 | capture: sha256:22d790f8a3f91a62c10df4b55dd6a2250456bfcd2ed7fa50d532ebe61d8d8cfc | quote: Pricing [Free](https://docs.drone.io/server/overview/)
  - [3] 2026-10-30: the software downloads with no account, sales contact or trial licence | capture: sha256:8cb9169fa90cd9756a86bcb38f95ddad600b0e8d69c5fff39d9ee6b473ee2c20 | quote: Download our official Docker image or build from source. No need to talk with a sales person or request a trial license.
  - [2] 2026-10-30: cloud.drone.io takes no new registrations, so no hosted capacity is reachable | capture: sha256:bf03461be8e8b4d40e69394cbbbd2d933c75ffe5ca52ebfa6d6cd62f9aad56e5 | quote: Currently, [cloud.drone.io](http://cloud.drone.io) is not accepting new registrations.
- sources:
  - [1] https://cloud.drone.io
  - [2] https://drone.discourse.group/t/user-registration-is-disabled-on-cloud-drone-io/11904
  - [3] https://www.drone.io/
  - [4] https://api.github.com/repos/harness/drone
  - [5] https://docs.drone.io/enterprise/
  - [6] https://www.drone.io/enterprise/opensource
