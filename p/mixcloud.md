# Mixcloud

> mixcloud.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mixcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/mixcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mixcloud — Basic tier (unlimited drafts)

- `storage/mixcloud-basic-tier` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:11.736Z (live) | stale on 2026-12-10
- url https://www.mixcloud.com
- free tier: 10 published shows (>15 min) + 10 published tracks (<=15 min). But: 'there's currently no limit to the number of uploads you can have in your drafts'. Drafts are uploaded, stored, and private. That is the actual finding: published storage is capped at 20 items, unpublished storage is uncapped. | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GB ceiling | bytes: 4000000000 | source: [1] | note: Choose a file over 15 minutes in length (max 4GB) to upload.
- retention: source: [1] | note: Don't worry - we won't delete your previous uploads, and there's currently no limit to the number of uploads you can have in your drafts.
- egress: Free streaming for listeners; no egress charge to the creator, but drafts are not publicly downloadable at all, so 'egress' is the wrong axis. A draft has no delivery surface. | metered: no
- identity: email
- interface: rclone
- limits:
  - per-object-cap (binding): 4 GB ceiling [1]
- limits note: 4 GB max per show file; shows must be >15 min, tracks <=15 min (so the 4 GB ceiling only applies to long files); 10 published shows + 10 published tracks; RSS-fed podcasts also count toward the 10-show cap ('only the 10 most recent shows will display').
- interface detail: wrapper-only
- tooling: No public API. Desktop-only upload for tracks ('only available through the desktop platform and not the Mixcloud app'); shows upload from web. No rclone backend, no client library found.
- composes with: Unlimited drafts x 4 GB per show x N free accounts. Whether drafts are garbage-collected is not stated. The FAQ only says previous uploads are not deleted when you exceed the publish cap, which is a different promise from 'drafts are kept forever'.
- reliability: Mixcloud is a streaming platform: shows are transcoded for playback and there is no original-file download link on Basic. Drafts are inaccessible to anyone but the uploader, which means they are storage but not retrieval. A draft is only recoverable by publishing it, and publishing consumes one of the 10 slots.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Creators on the basic tier can have a total of 10 published shows (over 15 minutes long), and 10 published tracks'; 'we won't delete your previous uploads, and there's currently no limit to the number of uploads you can have in your drafts'
  - [2] 2026-10-21: 'Choose a file over 15 minutes in length (max 4GB)'; 'Lossless and lossy formats are supported ... WAV, AIFF, FLAC or AAC, OGG, M4A, MP2, MP3 and WMA'
  - [1] 2026-11-19: the FAQ states the basic-tier published show and track caps | capture: sha256:0119ae2e7d8de06382e01b88bdccd67d8d6fb8d782a6af2b472a50c98fab873c | quote: Creators on the basic tier can have a total of 10 published shows (over 15 minutes long), and 10 published tracks (up to 15 minutes long).
  - [1] 2026-11-19: the FAQ states unlimited uploads in drafts | capture: sha256:0119ae2e7d8de06382e01b88bdccd67d8d6fb8d782a6af2b472a50c98fab873c | quote: Don't worry - we won't delete your previous uploads, and there's currently no limit to the number of uploads you can have in your drafts.
  - [2] 2026-11-19: the upload guide states the 4 GB per-file ceiling | capture: sha256:a0f5968b56bb2b089d2f0bc39e41625e115ffe4a687400802203a36b4e332b33 | quote: Choose a file over 15 minutes in length (max 4GB) to upload.
  - [1] 2026-11-25: previous uploads are not deleted when the publish limit is reached and drafts have no stated count limit | capture: sha256:c96d3f3fbe89b4e61c3ec614c5fea165153ac2dbf9f62c135af8fb19bcdecb36 | quote: Don't worry - we won't delete your previous uploads, and there's currently no limit to the number of uploads you can have in your drafts.
  - [2] 2026-11-25: the upload guide states a 4 GB ceiling for show files | capture: sha256:29e214cabcfb93faf6f7aad6803ec360b2de797215bb29c4d31be7d9a5958c16 | quote: Choose a file over 15 minutes in length (max 4GB) to upload.
- sources:
  - [1] https://help.mixcloud.com/hc/en-us/articles/6617808567708-FAQ-Publishing-limits
  - [2] https://help.mixcloud.com/hc/en-us/articles/360005918580-How-do-I-upload-on-Mixcloud
