# KeylessAI

> keylessai.thryx.workers.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/keylessai-thryx-workers-dev/ | JSON https://fshy.ajam.dev/api/v1/entity/keylessai-thryx-workers-dev.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KeylessAI

- `inference/keylessai` | dead | evidence measured | binding none | category inference gateway, keyless router over Pollinations and Api.Airforce, host gone
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:18.974Z (live) | stale on 2026-11-28
- url https://keylessai.thryx.workers.dev/v1
- free tier: documented as an OpenAI-compatible endpoint with zero API keys and zero signup routing to keyless upstream providers; the workers.dev host no longer resolves and the GitHub repository answers 404 | unit: none | metered on: none | read on: 2026-10-28 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: the offer was keyless: zero API keys and zero signup per the package page
- interface: rest
- limits note: no rate or quota binds: the host does not resolve
- endpoint: https://keylessai.thryx.workers.dev/v1/chat/completions
- tooling: any OpenAI-compatible client with a placeholder key; the same router could run locally via npx, which is software on the caller's own machine
- composes with: no chain exists: the hosted worker does not resolve
- reliability: the host keylessai.thryx.workers.dev fails DNS resolution and the GitHub repository lordbasilaiassistant-sudo/keylessai answers 404
- notes: dead cause: dead-service; the package page named Pollinations and Api.Airforce as the keyless upstreams
- evidence note: two keyless GETs to the host both failed at DNS; the repository page was read once
- probe:
  - records[0].probe_id: keylessai-models-get
  - records[0].method: GET
  - records[0].url: https://keylessai.thryx.workers.dev/v1/models
  - records[0].error: dns
  - records[0].probed_at: 2026-10-28T04:45:27.962Z
  - records[1].probe_id: keylessai-root-get
  - records[1].method: GET
  - records[1].url: https://keylessai.thryx.workers.dev/
  - records[1].error: dns
  - records[1].probed_at: 2026-10-28T04:45:28.971Z
- evidence:
  - [1] 2026-10-28: the package page documented the keyless hosted endpoint | capture: sha256:a8751dbcdbd0b350e87244c4bcdedc348fdc9370de65674a9e9ec26960e0977d | quote: A drop-in OpenAI-compatible endpoint with zero API keys, zero signup, zero cost, and zero user compute.
  - [1] 2026-10-28: the documented hosted base URL | capture: sha256:a8751dbcdbd0b350e87244c4bcdedc348fdc9370de65674a9e9ec26960e0977d | quote: Point your OpenAI client at `https://keylessai.thryx.workers.dev/v1`
  - [2] 2026-10-28: a GET to the documented host failed at DNS resolution | capture: sha256:9127e53059165295b14e10b10374c3eaf49bcc049923237cadf2eae59eca19fb | quote: error: dns
  - [3] 2026-10-28: the GitHub repository page answered 404 | capture: sha256:81cb4b2b5ed06adb133ef6805631fca83be93c0a6287be3950eee225ff20420c | quote: 404 “This is not the web page you are looking for”
- sources:
  - [1] https://www.npmjs.com/package/keylessai
  - [2] https://keylessai.thryx.workers.dev/v1/models
  - [3] https://github.com/lordbasilaiassistant-sudo/keylessai
