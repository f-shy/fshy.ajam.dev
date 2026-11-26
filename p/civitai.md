# civitai

> civitai.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/civitai/ | JSON https://fshy.ajam.dev/api/v1/entity/civitai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Civitai — model version files (the 'arbitrary 65 GiB blob' hub)

- `storage/civitai-model-version-files` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T09:54:57.892Z (live) | stale on 2026-12-10
- url https://civitai.com
- free tier: No published per-account or per-file byte quota. Its own Data Storage Policy states: 'By default, uploaded content will be stored indefinitely with the exception of input and output files related to model training.' Empirically: a single file of 65.83 GiB exists in production, and single free accounts hold 453 GiB (Lykon, 212 models) and 97 GiB (NanashiAnon, 412 models). | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: single file of 65.83 GiB | bytes: 70684424273 | source: [1] | note: no per-file byte cap is published; the data-storage policy states retention only, and the API reference reports a per-file size in a sizeKB field without stating a cap
- retention: By default, uploaded content will be stored indefinitely with the exception of input and output files related to model training that occurs from Civitai. | source: [1] | note: uploaded content is stored indefinitely by default; training input files are kept 30 days and training output files 30 days after the job completes
- egress: Unmetered; downloads 307-redirect to civitai-delivery-worker-prod...r2.cloudflarestorage.com with a 24 h X-Amz-Expires, then serve 206 with Accept-Ranges: bytes. No per-GB egress charge exists on any Civitai page. | metered: no
- identity: institution
- interface: rest, rclone, cli
- limits:
  - per-object-cap (binding): single file of 65.83 GiB [1]
- limits note: Per-object-cap: >=65.83 GiB observed, no published number. THE BINDING CONSTRAINT IS NOT SIZE. It is a per-object access flag plus NSFW gating: creators may set 'require login to download', and such files return HTTP 401 with body {"error":"Unauthorized","message":"The creator of this asset requires you to be logged in to download it"} on BOTH ranged and full GETs (verified consistent. No ranged-lies-while-full-gates behaviour, unlike some round-1 hosts). Of 20 large models sampled, 12 were anonymous-206 and 8 were 401. Training-data retention is a separate, much shorter clause: inputs and training outputs are 30 days. Published per-account storage: Vault is paid-only (Bronze 100 GB / Silver 250 GB / Gold 500 GB) and is a separate product from model hosting.
- interface detail: rest
- tooling: Public REST API v1 (no auth for reads/metadata): /api/v1/models, /api/v1/model-versions/{id}, /api/v1/model-versions/by-hash/{sha256}. Download via GET /api/download/models/{versionId}. Working clients: civitai/cli (official, `civitai download` needs a token), RtypeStudios/CivitAI-Model-Archiver. No rclone backend.
- composes with: Free accounts carry no stated limit and each holds the same allowance. Models per account and versions per model are unlimited, with a per-file ceiling >=65.8 GiB. 30 TiB = ~460 files at the observed 65.8 GiB ceiling, i.e. one account pushing ~460 'models'. Verified excess-use precedent already on the platform: model 1219185 is literally titled 'hunyuanvideo-lora-training-wsl-ubuntu-system-backup' and is a 65.83 GiB zip of a WSL Ubuntu install uploaded as type 'Other'.
- reliability: Downloads are reliable and hash-exact when ungated: a full 13,649,928-byte fetch matched the API-advertised SHA-256 exactly (8184D4BA..). Rate: sustained 20 ranged GETs with no 429. The trap is silent partial bodies. A curl without -f writes the 106-byte JSON 401 body to disk as if it were your file, so every download must be hash-checked.
- notes: the same as the free tier
- evidence:
  - withheld 2026-10-21: probe: GET civitai.com/api/v1/model-versions/2752735 -> file 46,149,344,974 bytes (43.0 GiB); GET /api/download/models/2752735 -r 0-1023 -L -> 307 -> 206 Content-Range: bytes 0-1023/46149344974
  - withheld 2026-10-21: probe: full GET /api/download/models/171989 -> 13,649,928 bytes, sha256sum = 8184D4BA9DA2B849638531F3DEF563AD2A0AB695B97FBB74F80AC099F2EB7396 = API hashes.SHA256 (MATCH)
  - withheld 2026-10-21: probe: GET /api/download/models/493690 -> 401, 106 bytes, {"error":"Unauthorized","message":"The creator of this asset requires you to be logged in to download it"}
  - withheld 2026-10-21: probe: 20-model sample of >35 GiB files -> 12x 206 anonymous, 8x 401 (creator-gated); size is not the gate
  - withheld 2026-10-21: probe: model 1219185 = 'hunyuanvideo-lora-training-wsl-ubuntu-system-backup', 65.83 GiB zip, type 'Other'
  - withheld 2026-10-21: probe: paginated /api/v1/models?username=Lykon -> 212 models, 358 files, 452.7 GiB in ONE free account
  - [1] 2026-10-21: 'uploaded content will be stored indefinitely ... except input and output files related to model training' (30 days for those)
  - [1] 2026-11-19: the data-storage policy states indefinite retention except training files | capture: sha256:d1130bf3b47a788334efc33253f7b9f1ed4136f236f0c0f94f292ed579f04ee4 | quote: By default, uploaded content will be stored indefinitely with the exception of input and output files related to model training that occurs from Civitai.
  - [1] 2026-11-19: the data-storage policy states the 30-day retention of training input files | capture: sha256:d1130bf3b47a788334efc33253f7b9f1ed4136f236f0c0f94f292ed579f04ee4 | quote: By default, this data will be retained for 30 days to allow for future re-use in the LoRA Trainer
  - [2] 2026-11-25: the API reference example reports a per-file size in a sizeKB field and states no cap | capture: sha256:9d68bef698f2165d7814a1366f1f0dc5648abacf4c5b9f9454e62b161673ab36 | quote: "sizeKB": 6775430.35,
  - [1] 2026-11-25: the data-storage policy states retention and no per-object size cap | capture: sha256:681fb17c73b93cdfcaf61651ad4702f5509b47ec8b17cde290ce4f9fd1111863 | quote: By default, uploaded content will be stored indefinitely with the exception of input and output files related to model training that occurs from Civitai.
  - [1] 2026-11-25: the policy states 30-day retention for training outputs | capture: sha256:681fb17c73b93cdfcaf61651ad4702f5509b47ec8b17cde290ce4f9fd1111863 | quote: The images and models that result from completion of training will be retained for 30 days after the completion of the training job.
  - [1] 2026-11-25: the data policy still states indefinite retention except for training files | capture: sha256:681fb17c73b93cdfcaf61651ad4702f5509b47ec8b17cde290ce4f9fd1111863 | quote: By default, uploaded content will be stored indefinitely with the exception of input and output files related to model training that occurs from Civitai.
  - [1] 2026-11-25: the policy states 30-day retention for training inputs | capture: sha256:681fb17c73b93cdfcaf61651ad4702f5509b47ec8b17cde290ce4f9fd1111863 | quote: By default, this data will be retained for 30 days to allow for future re-use in the LoRA Trainer, unless you elect (and have the appropriate ownership rights) to share your dataset publicly.
- sources:
  - [1] https://civitai.com/content/training/data-policy
  - [2] https://developer.civitai.com/site/reference/model-versions

## civitai training-data / lora-dataset path (as a storage vector)

- `storage/civitai-training-data-lora-dataset-path` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:07.131Z (live) | stale on 2026-12-04
- url https://civitai.com/content/training/data-policy
- free tier: none reachable: The cheapest-sounding Civitai surface is the shortest-lived: 'this data will be retained for 30 days', and training outputs 'retained for 30 days after the completion of the training job'.… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The cheapest-sounding Civitai surface is the shortest-lived: 'this data will be retained for 30 days', and training outputs 'retained for 30 days after the completion of the training job'.…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The cheapest-sounding Civitai surface is the shortest-lived: 'this data will be retained for 30 days', and training outputs 'retained for 30 days after the completion of the training job'.…
  - [2] 2026-10-21: cited as the basis of the rejection: The cheapest-sounding Civitai surface is the shortest-lived: 'this data will be retained for 30 days', and training outputs 'retained for 30 days after the completion of the training job'. C
  - [1] 2026-11-19: training outputs are still retained for only 30 days, matching the recorded rejection | capture: sha256:d1130bf3b47a788334efc33253f7b9f1ed4136f236f0c0f94f292ed579f04ee4 | quote: The images and models that result from completion of training will be retained for 30 days after the completion of the training job.
- sources:
  - [1] https://civitai.com/content/training/data-policy
  - [2] https://civitai.com/articles/11969/

## civitai vault (paid tier)

- `storage/civitai-vault` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:07.131Z (live) | stale on 2026-12-04
- url https://education.civitai.com/civitais-guide-to-vault/
- free tier: none reachable: The obvious 'personal unlimited storage' feature on Civitai is paid and capped: Free has 'No access to Vault'; Bronze $10/mo = 100 GB, Silver = 250 GB, Gold = 500 GB. It is also… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The obvious 'personal unlimited storage' feature on Civitai is paid and capped: Free has 'No access to Vault'; Bronze $10/mo = 100 GB, Silver = 250 GB, Gold = 500 GB. It is also…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The obvious 'personal unlimited storage' feature on Civitai is paid and capped: Free has 'No access to Vault'; Bronze $10/mo = 100 GB, Silver = 250 GB, Gold = 500 GB. It is also…
  - [2] 2026-10-21: cited as the basis of the rejection: The obvious 'personal unlimited storage' feature on Civitai is paid and capped: Free has 'No access to Vault'; Bronze $10/mo = 100 GB, Silver = 250 GB, Gold = 500 GB. It is also download-deg
  - [1] 2026-11-19: the free tier still has no Vault access, matching the recorded paid-only rejection | capture: sha256:cdaea810fd65a9f09f6294a53eee8dfad85d0f89819a8a0ed8dba2d732aae346 | quote: | Free | No access to Vault |
  - [2] 2026-11-19: the cheapest paid membership is Bronze at $10 per month, matching the recorded tier pricing | capture: sha256:83604f37d8c173b04232ccfe45b73ae22240ee01eb8b3b1f51e109587de8088a | quote: Bronze $10 / mo
- sources:
  - [1] https://education.civitai.com/civitais-guide-to-vault/
  - [2] https://civitai.com/pricing
