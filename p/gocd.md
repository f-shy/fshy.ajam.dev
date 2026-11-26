# GoCD

> gocd.org | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gocd/ | JSON https://fshy.ajam.dev/api/v1/entity/gocd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GoCD

- `ci-cd-runners/gocd` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category CI software
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:46:16.196Z (live) | stale on 2026-12-20
- url https://www.gocd.org/
- free tier: Apache-2.0 open-source software with no licence fee and no metered quota: the user downloads and runs a server and at least one agent on a machine the user provides. The Test Drive is a local, download-and-run evaluation instance, not a hosted service | unit: none | metered on: none | read on: 2026-11-19 | source: [1] | note: there is no hosted lane to denominate; the only cost is the machine the user runs the server and agents on
- per-object cap: not applicable: there is no hosted service to impose a single-object cap; pipeline and artifact limits are set by the user's own server configuration | source: [2]
- retention: whatever the machine running the GoCD server and agents retains; the software imposes no fixed retention period | source: [2]
- egress: whatever the machine running the GoCD server and agents charges for outbound traffic; the software meters and caps no traffic itself | metered: no | source: [1]
- identity: anonymous | detail: the software downloads and runs with no account: the download page links installers and images directly with no sign-up, and a newly installed GoCD server does not require users to authenticate. Optional password-file or LDAP/AD authentication is configured locally by the operator; the Test Drive is a local installer needing no registration
- interface: git, rest, cli
- limits:
  - write-gated (binding): no hosted tier exists, so the path is a self-hosted deployment of a server plus at least one agent [2]
- binding note: the binding constraint is the need to install and operate a server and agent on a machine the user provides, since the vendor offers no hosted runner that could be used instead
- interface detail: a material is usually a source repository (Git, SVN, Mercurial) that the server polls for commits, and a timer or pipeline dependency can also trigger a run. A REST API at go-server-url:8154/go/api reads configuration and build history and can update configuration and execute builds; the API reference offers Shell bindings and curl examples
- endpoint: https://go-server-url:8154/go/api (the host is the user's own server)
- tooling: the user installs and runs the GoCD Server and one or more GoCD Agent daemons on a rented or free machine, from OS installers, Zip archives, Docker images or a Kubernetes Helm chart; the agent polls the server for work and executes the build tasks
- composes with: no hosted runner lane exists: the Test Drive is a local download-and-run evaluation instance, described as for evaluation purposes only and not for production. The self-hosted server and agents are the last resort; pair them with a free or rented machine. Pipelines can be triggered by Git commits, a timer or an upstream pipeline, and driven through the REST API
- reliability: the host, its bill and its uptime belong to whoever runs the instance, so no reliability event at a provider applies to this record; the Test Drive is explicitly for evaluation, not production use
- notes: GoCD is a continuous delivery server the user installs and runs; there is no vendor-hosted runner lane. The vendor's Test Drive is a local download-and-run evaluation instance, not a hosted service, so it does not count as a hosted offer. Build container CPU, memory, outbound network access and any fixed artifact retention are set by the user's own server configuration and are unverified.
- evidence note: the software's own pages were read and quoted: the download page, the installation page, the API reference, the concepts page and the authentication page. GoCD is software the user installs and runs; there is no hosted runner lane, and the Test Drive is a local installer rather than a hosted service. No build was run, so build container CPU, memory and outbound network behaviour are unverified
- self hosted: yes
- evidence:
  - [1] 2026-11-19: running GoCD requires the user to run both a server and at least one agent | capture: sha256:78f7f1de3ed3d469a4df8efb95ea3c3533df7a5a14a23f9dda287faa1d3b8320 | quote: To run GoCD, you'll need both server and agent
  - [1] 2026-11-19: the server is distributed as a Docker image the user runs themselves | capture: sha256:78f7f1de3ed3d469a4df8efb95ea3c3533df7a5a14a23f9dda287faa1d3b8320 | quote: docker run -d -p8153:8153 gocd/gocd-server:v26.1.0
  - [2] 2026-11-19: GoCD is installable software made of a server and agents, not a hosted service | capture: sha256:c486df0fc95f361afec443d3dcf08575149f4547744b7059e44128a383e12a47 | quote: GoCD consists of two installable components. The GoCD Server and one or more GoCD Agents.
  - [3] 2026-11-19: the Test Drive is an evaluation-only experience, not a production hosted lane | capture: sha256:9c933f6d49e59bc80ff5e291fcfdc6d5102d0eff2cf35af72d5fd3b95ba6465a | quote: This is for evaluation purposes only, and not intended for production use.
  - [3] 2026-11-19: the Test Drive leads to a download-and-install of the user's own server, confirming it is not hosted | capture: sha256:9c933f6d49e59bc80ff5e291fcfdc6d5102d0eff2cf35af72d5fd3b95ba6465a | quote: Once you've finished exploring our test drive, we recommend downloading and installing GoCD following our introduction to setting up your own GoCD server
  - [4] 2026-11-19: GoCD is Apache-2.0 open-source software | capture: sha256:10f60f6c2f25aeef77f27a0028a6690929d14149a160f312ee71b782227ea76d | quote: GoCD is an open source project, sponsored by Thoughtworks, Inc. under the Apache License, Version 2.0.
  - [5] 2026-11-19: a freshly installed server needs no account or sign-in, so registration is anonymous | capture: sha256:d3b3c9bcdfa81687023fb0f2222d52d238c33bab841ddec96f3619f10bdce90a | quote: A newly installed GoCD server does not require users to authenticate.
  - [6] 2026-11-19: a REST API exposes configuration, build history and build execution on the user's server | capture: sha256:8fb13a4890eb0ccf8867c73067b3dd4c47cc5b6593b85cbd72a12a8c92e1aa69 | quote: You can use our API to access GoCD API endpoints, which can get information about the server’s configuration and build history. In addition it can be used to update configuration and execute builds.
  - [7] 2026-11-19: Git repositories are a source material the server polls to trigger pipelines | capture: sha256:92022d225b1d9f56c6cf6bea0720a6c2a6a9a798034a19413291a08d7b1b8c08 | quote: Often, it is a source code material repository (Git, SVN, Mercurial, etc). The GoCD Server continuously polls configured materials
- sources:
  - [1] https://www.gocd.org/download/
  - [2] https://docs.gocd.org/current/installation/
  - [3] https://www.gocd.org/test-drive-gocd
  - [4] https://github.com/gocd/gocd
  - [5] https://docs.gocd.org/current/configuration/dev_authentication.html
  - [6] https://api.gocd.org/current
  - [7] https://docs.gocd.org/current/introduction/concepts_in_go.html
