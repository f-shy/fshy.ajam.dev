# Jenkins

> jenkins.io | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jenkins/ | JSON https://fshy.ajam.dev/api/v1/entity/jenkins.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jenkins

- `ci-cd-runners/jenkins-cloud` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category CI software | tier open source automation server (no hosted tier)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:46:16.148Z (live) | stale on 2026-12-20
- url https://www.jenkins.io/doc
- free tier: The Jenkins project publishes no hosted Jenkins Cloud service and no price list; the open source automation server is free software the user installs and runs, so the cost is a machine the user provides | unit: none | metered on: none | read on: 2026-11-19 | source: [1] | note: the name 'Jenkins Cloud' names no hosted offer: a project maintainer writes on the first-party community forum that 'The open source project only has the open source self on prem install', and the download page only links out to public cloud vendors' own installation guides. Commercial managed distributions such as CloudBees CI are quoted separately and are not a Jenkins project offer.
- per-object cap: unverified: no first-party page read states a per-object or per-build-size cap; the limit is whatever the host and the configured agent allow | source: [2]
- retention: whatever the controller and agent hosts retain; workspaces may not be cleaned up automatically after inactivity | source: [3] | note: the pipeline book warns that depending on configuration some workspaces may not get automatically cleaned up after a period of inactivity; no fixed retention period is stated
- egress: whatever the machine the user runs the controller and agents on charges for outbound traffic; no hosted allowance or price is stated | metered: no | source: [2]
- identity: anonymous | detail: the software needs no account, email, phone, card or institution to download and run; the first admin user is created locally during the post-installation setup wizard on the user's own controller
- interface: rest, cli, ssh, browser, git
- limits:
  - write-gated (binding): no hosted tier exists, so the path is a self-hosted deployment the user installs and runs [4]
- limits note: no vendor-enforced request rate, pull count, object cap or retention clamp was found on the first-party pages read; the only gate is that the user must provide and operate a host
- binding note: there is no hosted lane to sign up for: the first gate is obtaining and operating a machine for the controller and agents, not a request or build quota
- interface detail: a REST-like remote access API under .../api/, a CLI client (.jar file) reachable over SSH or WebSocket, a web interface, and a Jenkinsfile kept in the project's source control repository
- endpoint: the API lives under the installation's own .../api/ path; there is no shared public endpoint because the user runs the controller
- tooling: the user installs and runs the Jenkins controller and one or more agents on a rented or free machine, from a WAR file, native package, installer or Docker image; pipelines are defined in a Jenkinsfile, driven through the web UI, the CLI client or the REST-like remote access API
- composes with: a Jenkinsfile in a Git repository defines a pipeline that can be triggered by a source control change or by an HTTP POST to the remote API and runs on a controller and agents the user operates; managed Jenkins distributions sold by other vendors are separate offers and are not needed to run the free software
- reliability: unverified: no first-party page read states an uptime commitment, ban policy or throttling for the software itself; the host, its bill and its uptime belong to whoever runs the instance, and the project publishes frequent security advisories for the controller and its plugins
- notes: The name 'Jenkins Cloud' does not correspond to a hosted first-party offer. The Jenkins project distributes free, self-hosted automation software that the user installs and runs on a machine they provide; no hosted signup, free tier, price list or metered quota exists. Qualifies-with-caveat because the software is usable without a card, phone or institution but the whole cost and operation of a host falls on the user. Managed Jenkins sold by third parties is outside this record.
- evidence note: every value is quoted from first-party jenkins.io pages and the project's own community forum; no controller was installed and no build was run, so the hardware, retention and outbound network behaviour of any particular deployment are unverified
- self hosted: yes
- evidence:
  - [2] 2026-11-19: Jenkins is open-source automation software that the user deploys, not a hosted service | capture: sha256:5f52261b69ddc3e79c5fad7267c1f8940b3ff632434edff22c82d89991feb939 | quote: Jenkins is a self-contained, open source automation server which can be used to automate all sorts of tasks related to building, testing, and delivering or deploying software.
  - [2] 2026-11-19: the user installs and runs Jenkins on a machine they provide | capture: sha256:5f52261b69ddc3e79c5fad7267c1f8940b3ff632434edff22c82d89991feb939 | quote: Jenkins can be installed through native system packages, Docker, or even run standalone by any machine with a Java Runtime Environment (JRE) installed.
  - [1] 2026-11-19: the project describes Jenkins as an open-source automation server with plugins | capture: sha256:e5e5b8ed2404ef610f4c5a2f7a5f2158ddaa97ac77bad9b7509ebd6af564b038 | quote: The leading open source automation server, Jenkins provides hundreds of plugins to support building, deploying and automating any project.
  - [1] 2026-11-19: a browser web interface configures the installation | capture: sha256:e5e5b8ed2404ef610f4c5a2f7a5f2158ddaa97ac77bad9b7509ebd6af564b038 | quote: Jenkins can be easily set up and configured via its web interface, which includes on-the-fly error checks and built-in help.
  - [5] 2026-11-19: the distribution forms are installable artefacts, not a hosted signup | capture: sha256:f89271c732660c0e16827f816b4f6b1a798050ee09675c61783006b3a7ce939b | quote: Jenkins is distributed as WAR files, native packages, installers, and Docker images.
  - [5] 2026-11-19: the cloud paths are vendor installation guides rather than a Jenkins-hosted cloud | capture: sha256:f89271c732660c0e16827f816b4f6b1a798050ee09675c61783006b3a7ce939b | quote: Many public cloud vendors provide their own Jenkins installation guides and packages.
  - [6] 2026-11-19: the project grants the software free of charge with no licence fee | capture: sha256:b05eebde7eb547c2313927bf07352feaa013197499c4ce68d55cc3ff10e6582c | quote: Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
  - [4] 2026-11-19: a project maintainer states there is no Jenkins Cloud hosted version | capture: sha256:cbdc45e94a5faf10e822f34d926976f551f5d10e7c85423d0cb3f89b84244467 | quote: The open source project only has the open source self on prem install.
  - [4] 2026-11-19: the question of a Jenkins cloud price list is raised on the project's own forum | capture: sha256:cbdc45e94a5faf10e822f34d926976f551f5d10e7c85423d0cb3f89b84244467 | quote: If we have Jenkins cloud what are the pricing/subscription details for it?
  - [7] 2026-11-19: a REST-like remote access API is available | capture: sha256:878a631303a2e16d36b006c5facfa0ca3a068f2afb6451ac018dce81bc074b9a | quote: Remote access API is offered in a REST-like style.
  - [7] 2026-11-19: the remote API can trigger builds programmatically | capture: sha256:878a631303a2e16d36b006c5facfa0ca3a068f2afb6451ac018dce81bc074b9a | quote: 2. trigger a new build
  - [8] 2026-11-19: a CLI is reachable over SSH or a client jar | capture: sha256:87222add01707f7938ad39fd23c8d61b38a12a5220e6ada9b891f346913dd951 | quote: The command line interface can be accessed over SSH or with the Jenkins CLI client, a `.jar` file distributed with Jenkins.
  - [3] 2026-11-19: pipelines are defined in a Jenkinsfile kept in source control | capture: sha256:14c2521c61a1186734610ac3f2a08622b342756a004f73160b60532adfe976a4 | quote: The definition of a Jenkins Pipeline is written into a text file (called a [`Jenkinsfile`](https://www.jenkins.io/doc/book/pipeline/jenkinsfile)) which in turn can be committed to a project's source control repository.
  - [3] 2026-11-19: retention of build workspaces depends on the configuration and is not a fixed period | capture: sha256:14c2521c61a1186734610ac3f2a08622b342756a004f73160b60532adfe976a4 | quote: Depending on your Jenkins configuration, some workspaces may not get automatically cleaned up after a period of inactivity.
- sources:
  - [1] https://www.jenkins.io/
  - [2] https://www.jenkins.io/doc
  - [3] https://www.jenkins.io/doc/book/pipeline/
  - [4] https://community.jenkins.io/t/jenkins-onpremise-and-cloud/1912
  - [5] https://www.jenkins.io/download/
  - [6] https://www.jenkins.io/license/
  - [7] https://www.jenkins.io/doc/book/using/remote-access-api/
  - [8] https://www.jenkins.io/doc/book/managing/cli/
