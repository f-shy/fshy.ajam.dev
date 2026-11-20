# datachain

> domore.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/domore/ | JSON https://fshy.ajam.dev/api/v1/entity/domore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## datachain / datachain studio (iterative)

- `storage/datachain-datachain-studio` | self-hosted, last resort | verdict dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:52.047Z (live) | stale on 2026-12-04
- url https://domore.ai/tools/iterative.ai
- free tier: none reachable: Service is a Python data-context and lineage catalogue over S3, GCS, and Azure. The user installs and runs the DataChain SDK against their own object-storage buckets; it provides no managed storage capacity. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the DataChain page states no per-object size cap | source: [1] | note: not applicable
- retention: stated-absent: the DataChain page states no retention period, because files remain in the user's own object storage | source: [1]
- egress: stated-absent: the DataChain page states no egress terms; files stay in the user's own object storage | metered: no
- identity: email
- interface: unknown
- interface detail: a Python SDK data-context layer that reads files in S3, Google Cloud Storage and Azure; it holds no storage capacity of its own
- tooling: not documented
- composes with: it is a catalogue over existing S3, Google Cloud Storage and Azure buckets and composes with those stores rather than holding bytes itself
- reliability: Service is a Python data-context and lineage catalogue over S3, GCS, and Azure. It provides no managed storage capacity and requires user-provided buckets.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- self hosted: yes
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: It provides zero bytes and requires you to bring a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: It provides zero bytes and requires you to bring a buck
  - [1] 2026-11-19: DataChain is a data-context and lineage layer over files in object storage, not a provider of managed storage bytes | capture: sha256:299477eaec15ed07612ec5936b890b447b3ba3e47be58c111e35b9169ce6f520 | quote: DataChain captures metadata, LLM summaries, statistics, code, and lineage for files that remain in object storage.
  - [1] 2026-11-19: the user installs and runs the SDK against their own object storage buckets | capture: sha256:299477eaec15ed07612ec5936b890b447b3ba3e47be58c111e35b9169ce6f520 | quote: Install the DataChain SDK and point a Python pipeline at files in S3, Google Cloud Storage, or Azure.
- sources:
  - [1] https://domore.ai/tools/iterative.ai
