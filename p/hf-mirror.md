# hf-mirror.com

> hf-mirror.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hf-mirror/ | JSON https://fshy.ajam.dev/api/v1/entity/hf-mirror.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hf-mirror.com / hf-mirror.net (Hugging Face mirror — read-only proxy)

- `storage/hf-mirror-com-hf-mirror-net` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hf-mirror.com
- free tier: None of its own. It is a transparent reverse proxy. | unit: none | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 50 GB/file | bytes: 50000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and anonymous for reads; resolves to HF's own CDN. Not applicable as a storage delta. The bytes live on HF, which is already known and excluded as a discovery. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 50 GB/file [1]
- limits note: per-object-cap: inherits HF (50 GB/file at the time of the linked HF issues). Retention: inherits HF. Write path is redirected straight to huggingface.co, not mirrored: probe POST /api/repos/create -> 308 Location: https://huggingface.co/api/repos/create. So the mirror gives you nothing new to store INTO.
- interface detail: rest
- tooling: Drop-in hostname swap: HF_ENDPOINT=https://hf-mirror.com for huggingface_hub / hf_transfer / rclone (rclone 'hf' backend points at it).
- composes with: Functions as an edge cache mirror for Hugging Face datasets. Provides an alternate delivery route for downloads, while terms exclude hotlinking and intentional exhaustion of shared bandwidth.
- reliability: Reads work; One probe returned a bare 200 with an HTML body from the LFS batch endpoint rather than JSON. Parse the body, not the status.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: None of its own — it is a transparent reverse proxy.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: (last revised 2026-09-11) — proxy-only positioning, no storage offered, no upload surface
  - withheld 2026-10-21: probe: GET hf-mirror.com/HPAI-BSC/Llama3.1-Aloe-Beta-8B/resolve/main/LICENSE -r 0-99 -L -> 308 (Caddy) -> 307 to HF CDN
  - [2] 2026-10-21: probe: POST hf-mirror.com/api/repos/create -> 308 Location: (writes are not mirrored)
- sources:
  - [1] https://hf-mirror.net/terms.html
  - [2] https://huggingface.co/api/repos/create
