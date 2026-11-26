# gpt4all

> gpt4all.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gpt4all/ | JSON https://fshy.ajam.dev/api/v1/entity/gpt4all.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gpt4all / jan / lm studio / weights.gg (the 'desktop llm app' hubs)

- `storage/gpt4all-jan-lm-studio-weights-gg` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:51.192Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/gpt4all.md
- free tier: none reachable: GPT4All runs open-source language models locally on the user's own machine; it is a local application, not a storage host: "runs open-source language models on Windows, macOS, and Linux—with full customization, local document chat (LocalDocs)" | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the GPT4All documentation states no per-object size cap for remote storage | note: not applicable
- retention: stated-absent: the GPT4All documentation describes a local desktop application and states no retention period for remotely stored bytes
- egress: stated-absent: the GPT4All documentation states no egress price or transfer quota for remotely stored bytes | metered: no
- identity: email
- interface: cli
- interface detail: Local desktop application plus a Python library that downloads and loads GGUF model files onto the user's own machine; no remote storage interface is stated
- tooling: not documented
- composes with: stated-absent: GPT4All is a local desktop application and Python library for running models, with no documented remote byte-storage chaining
- reliability: All four are distribution front-ends, not storage: gpt4all.io 301s to nomic.ai/gpt4all and its model catalogue is a static JSON in a GitHub repo (gpt4all-chat/metadata/models3.json, 40 KB).
- notes: All four are distribution front-ends, not storage: gpt4all.io 301s to nomic.ai/gpt4all and its model catalogue is a static JSON in a GitHub repo (gpt4all-chat/metadata/models3.json, 40 KB)…
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: All four are distribution front-ends, not storage: gpt4all.io 301s to nomic.ai/gpt4all and its model catalogue is a static JSON in a GitHub repo (gpt4all-chat/metadata/models3.json, 40 KB)…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: All four are distribution front-ends, not storage: gpt4all.io 301s to nomic.ai/gpt4all and its model catalogue is a static JSON in a GitHub repo (gpt4all-chat/metadata/models3.json, 40 KB)…
  - [1] 2026-11-19: GPT4All is a local application that runs models on the user's own machine, not a storage host | capture: sha256:3ebae6284d11876b61ff21f47e31d541f73574a4180ec984c80b6efc61eb5b2b | quote: GPT4All runs open-source language models on Windows, macOS, and Linux—with full customization, local document chat (LocalDocs)
  - [1] 2026-11-19: the first-party site describes local on-device operation, so it is not a storage host | capture: sha256:3ebae6284d11876b61ff21f47e31d541f73574a4180ec984c80b6efc61eb5b2b | quote: GPT4All delivers private, high-performance AI right on your device—no cloud required, no data leaves your machine.
  - [2] 2026-11-19: GPT4All is a local desktop application and Python library, not a remote byte store; no storage client interface is stated | capture: sha256:6711e944532dc186bb5292b5fde98df4cf750c12c66956d89f7238ec646a0317 | quote: GPT4All runs large language models (LLMs) privately on everyday desktops & laptops.
  - [2] 2026-11-19: the models run locally in a downloaded application, with no remote storage interface | capture: sha256:6711e944532dc186bb5292b5fde98df4cf750c12c66956d89f7238ec646a0317 | quote: No API calls or GPUs required - you can just download the application
  - [2] 2026-11-19: the app runs locally and states no remote retention term | capture: sha256:6711e944532dc186bb5292b5fde98df4cf750c12c66956d89f7238ec646a0317 | quote: GPT4All runs LLMs as an application on your computer.
- sources:
  - [1] https://gpt4all.io/
  - [2] https://docs.gpt4all.io/
