# Streamlit Community

> streamlit.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/streamlit/ | JSON https://fshy.ajam.dev/api/v1/entity/streamlit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Streamlit Community Cloud

- `storage/streamlit-community-cloud` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://share.streamlit.io
- free tier: 'Storage: No minimum, 50GB maximum' per app. But the filesystem is the build container, not durable storage. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: until the instance is recycled; not persistent | source: [1] | note: not stated
- egress: Free; apps are public by default with no transfer meter. | metered: no
- identity: email
- interface: rest
- limits note: 690 MB min / 2.7 GB max RAM; 50 GB max storage; app code must come from GitHub; apps sleep when unused; 'these limits may change at any time without notice'.
- interface detail: rest
- tooling: Apps deploy from a GitHub repo; the app process is an HTTP server, so anything it can read it can serve. No storage API.
- composes with: None. The 50 GB is a ceiling on what the container can hold, not an allocation you can write to and keep.
- reliability: Ephemeral build filesystem. Any file written at runtime is lost on reboot/redeploy. Useful only as a free public egress proxy in front of someone else's storage.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'Storage: No minimum, 50GB maximum' per app — but the filesystem is the build container, not durable storage.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Memory: 690MB minimum, 2.7GBs maximum'; 'Storage: No minimum, 50GB maximum'
  - [2] 2026-10-21: over-limit apps are throttled/stopped
- sources:
  - [1] https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app
  - [2] https://docs.streamlit.io/knowledge-base/deploy/resource-limits

## streamlit community cloud as storage

- `storage/streamlit-community-cloud-as-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app
- free tier: none reachable: Listed as a candidate for the serving angle only. The 50 GB 'storage' maximum is the container's disk ceiling, not an allocation: files written at runtime are lost on reboot and apps sleep. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Listed as a candidate for the serving angle only. The 50 GB 'storage' maximum is the container's disk ceiling, not an allocation: files written at runtime are lost on reboot and apps sleep.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Listed as a candidate for the serving angle only. The 50 GB 'storage' maximum is the container's disk ceiling, not an allocation: files written at runtime are lost on reboot and apps sleep.
- sources:
  - [1] https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app
