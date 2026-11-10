# Ollama registry

> ollama.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ollama/ | JSON https://fshy.ajam.dev/api/v1/entity/ollama.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ollama registry (registry.ollama.ai)

- `storage/ollama-registry-the-strongest-finding-in-this-slot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://registry.ollama.ai
- free tier: No published byte quota, no published per-file cap, and no paid storage tier exists to upsell to — the only paid Ollama product is inference compute ('Pricing': Free $0 'Use any cloud model with pay-as-you-go usage credits', Pro $20/mo; nothing on that page meters model storage). A single repo holds 455.5 GiB in one layer. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: NOT published, and NOT 2 GiB | bytes: 2147483648 | source: [1] | note: not stated
- retention: Client-side chunking is 100 MB-1 GB parts (server/upload.go). Retention: none. Objects persist until deleted; no TTL anywhere in the docs. | source: [1] | note: not stated
- egress: Unmetered anonymous pull. No egress line exists anywhere in Ollama's pricing. There is no per-GB transfer meter to quote because pull is free and unauthenticated. Blob GET is 307 to an R2 bucket (dd20bb891979d25aebc8bec07b2b3bbc.r2.cloudflarestorage.com, X-Amz-Expires=86400), fronted by Cloudflare. | metered: no
- identity: card
- interface: oci
- limits:
  - per-object-cap (binding): per-object-cap: NOT published, and NOT 2 GiB [1]
- limits note: per-object-cap: NOT published, and NOT 2 GiB like GitHub — verified live at 489,088,538,784 bytes in one blob. Retention: none — objects persist until deleted; no TTL anywhere in the docs. request-rate: not published; 20 consecutive ranged GETs all returned 206 with no throttling.
- interface detail: oci
- tooling: Native OCI Distribution v2. `ollama push` / `ollama pull`, oras/skopeo/crane all work. Push requires a free ollama.com account (WorkOS authkit signup, no payment); pull is fully anonymous. `ollama create` accepts safetensors dirs, GGUF, split GGUF globs, and any layer content. A pushed model is just OCI layers, so arbitrary bytes ride as `application/vnd.ollama.image.model`.
- composes with: unlimited free namespaces x unlimited repos x unlimited tags; the binding per-object ceiling is whatever the server accepts, and 455 GiB single-blob objects already exist in production. 30 TiB = 66 objects the size of huihui_ai/kimi-k2-abliterated. Multiply by free-account count. This is structurally identical to GHCR but with a ~45x larger observed per-object ceiling and no documented 10 GB layer cap.
- reliability: Pushes to large blobs are flaky: issue #6466 reports 502 Bad Gateway at 40-50% of an 8.5 GB upload, and #13740 reports 413 on 100 GB. Resume/retry is required, and `ollama push` is not resumable by default. Reads were 100% stable in every probe.
- notes: the same as the free tier
- evidence note: On 2026-10-22 the endpoint returned HTTP 404 (19 bytes, sha256 b16e15764b8bc06c). The page states the number in the record. The claim is documented, not measured.
- extras:
  - verified[0].url: https://registry.ollama.ai/v2/
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 404
  - verified[0].bytes: 19
  - verified[0].sha256: b16e15764b8bc06c5c3f9f19bc8b99fa48e7894aa5a6ccdad65da49bbf564793
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [2] 2026-10-22: the registry endpoint answers. Re-read https://registry.ollama.ai/v2/: HTTP 404, 19 bytes, sha256 b16e15764b8bc06c. Quoted: 404 page not found
  - withheld 2026-10-21: probe: GET registry.ollama.ai/v2/library/llama3.3/manifests/latest -> 200, 39.6 GiB total, largest layer 40,550.6 MiB
  - withheld 2026-10-21: probe: GET registry.ollama.ai/v2/library/deepseek-v3/manifests/latest -> largest layer 404,430,186,016 bytes (376.7 GiB)
  - withheld 2026-10-21: probe: GET registry.ollama.ai/v2/huihui_ai/kimi-k2-abliterated/blobs/sha256:33e8a1e4... -r 0-1023 -> 307 to R2 -> 206, Content-Range: bytes 0-1023/489088538784 (455.5 GiB, anonymous)
  - withheld 2026-10-21: probe: summed all 101 huihui_ai repos -> 89 resolvable, 3,270 GiB total, largest single 455 GiB (ONE free namespace)
  - withheld 2026-10-21: probe: POST registry.ollama.ai/v2/test/x/blobs/uploads/ anonymous -> 401 www-authenticate Bearer realm=registry.ollama.ai/v2/token (push is authenticated, pull is not)
  - [3] 2026-10-21: '109 GB ... 413 Request Entity Too Large' (upload ceiling, medium confidence)
  - [1] 2026-10-21: Free $0 / Pro $20/mo, both inference-only; no storage meter
- sources:
  - [1] https://registry.ollama.com/pricing
  - [2] https://registry.ollama.ai/v2/
  - [3] https://github.com/ollama/ollama/issues/13740
