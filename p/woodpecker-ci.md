# Woodpecker CI

> woodpecker-ci.org | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/woodpecker-ci/ | JSON https://fshy.ajam.dev/api/v1/entity/woodpecker-ci.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Woodpecker CI (self-hosted)

- `ci-cd-runners/woodpecker-selfhost` | self-hosted, last resort | verdict qualifies | evidence documented | binding none | category CI software
- needs card no, phone no, ID no, institution no | verified 2026-11-06T19:14:28.504Z (live) | stale on 2026-12-07
- url https://woodpecker-ci.org/docs/intro
- free tier: Apache-2.0 software with no licence fee and no metered quota; the agents run on hardware the operator provides, so the cost is the host | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: a pipeline is killed at 60 minutes by default, and the maximum a repo setting can set is 120 minutes by default | source: [2] | note: by default, the maximum workflows that are executed in parallel on an agent is 1
- retention: whatever the agent host retains | source: [3]
- egress: whatever the agent host charges | metered: no | source: [3]
- identity: anonymous | detail: the software needs no account; the forge it authenticates against does
- interface: git, cli
- limits:
  - per-object-cap: a pipeline is killed at 60 minutes by default, and the maximum a repo setting can set is 120 minutes by default [2]
- limits note: by default, the maximum workflows that are executed in parallel on an agent is 1
- interface detail: a server plus one or more agents; a .woodpecker.yml pipeline; the woodpecker-cli
- tooling: docker, podman, or a local backend on the agent host
- composes with: pair it with a free VM: the pipeline timeout is the wall clock, 60 minutes by default and at most 120 minutes from the repo settings
- reliability: the host, its bill and its uptime belong to whoever runs the instance, so no reliability event at a provider applies to this record
- notes: The pipeline timeout is the only wall clock the software imposes, and the repo can raise it to 120 minutes by default; the cost is a machine rather than a minute. Whether that is cheaper depends on the VM, which is the compute topic's question and not this one's.
- evidence note: the project's own intro page and its repository licence were read, and Codeberg documents that it runs Woodpecker in production. The intro page does not state the licence, which is why the repository is cited separately.
- self hosted: yes
- evidence:
  - [3] 2026-10-22: a server plus one or more agents, self-hosted, and 'lightweight and even runs on a Raspberry Pi'; the page names neither the licence nor a hosted instance
  - [1] 2026-10-22: the project repository is licensed Apache-2.0, as GitHub's licence field for it reports
  - [4] 2026-10-22: Codeberg's hosted instance is Woodpecker, and self-hosted agents can be attached to it
  - [2] 2026-11-06: a pipeline is killed at 60 minutes by default and the repo setting is capped at 120 minutes by default | capture: sha256:e5756a4fdfb6832c692b7bfbc58562fd98196178cee63121f2f042c8c4f5a6d5 | quote: - Default: 60 ... The default time for a repo in minutes before a pipeline gets killed ... - Default: 120 ... The maximum time in minutes you can set in the repo settings before a pipeline gets killed
  - [5] 2026-11-06: an agent runs one workflow at a time by default | capture: sha256:90cea2f6b72ea0b711a1688a617d5c3c2a1abfe85947659dff967b0552ad60f4 | quote: By default, the maximum workflows that are executed in parallel on an agent is 1.
- sources:
  - [1] https://github.com/woodpecker-ci/woodpecker
  - [2] https://woodpecker-ci.org/docs/administration/configuration/server
  - [3] https://woodpecker-ci.org/docs/intro
  - [4] https://docs.codeberg.org/ci/
  - [5] https://woodpecker-ci.org/docs/administration/configuration/agent
