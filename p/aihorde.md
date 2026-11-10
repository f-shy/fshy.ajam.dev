# AI Horde

> aihorde.net | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aihorde/ | JSON https://fshy.ajam.dev/api/v1/entity/aihorde.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AI Horde

- `compute/ai-horde` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:28.068Z (live) | stale on 2026-12-05
- url https://aihorde.net/
- free tier: Text and image generation on volunteer GPUs, free, with no account: the README says use API key '0000000000' for anonymous usage, with 'No need to register', and that 'anyone can use it for free, even anonymously'. Kudos never expire and can never be bought or sold. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous
- interface: rest
- limits:
  - request-rate (binding): Anonymous calls sit at the lowest priority and the service 'may be restricted for anonymous users during high load'. The measured pool on 2026-10-22 was 51 workers over 28 text models, so supply is thin and the queue, not a quota, is what limits a job: priority rises only with kudos, earned by contributing a GPU. [1]
- limits note: Anonymous calls sit at the lowest priority and the service 'may be restricted for anonymous users during high load'. The measured pool on 2026-10-22 was 51 workers over 28 text models, so supply is thin and the queue, not a quota, is what limits a job: priority rises only with kudos, earned by contributing a GPU.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The only way to raise priority is to run a worker, which needs a GPU; a rented GPU would earn kudos, but kudos earned per GPU-hour are not published, so the trade is unmeasured.
- reliability: no reliability event recorded
- notes: Two front ends share the API: Stable Horde for images and KoboldAI Horde for text. The measured model list is a catalog read without a key: it proves the pool is live and public, not that an anonymous generation completes, because a generation needs a POST and automated retrieval has no POST route. The 51-worker figure is one sample at 2026-10-22T15:34Z and volunteer pools swing by hour. A pseudonymous registered account starts at 25 kudos and outranks anonymous.
- extras:
  - facets.class: decentralized-free-inference
  - facets.free_tier_kind: perpetual
- evidence:
  - [2] 2026-10-22: probe record: status 200, 97 bytes, sha256 167f597e7d69, elapsed 899 ms, no challenge detected
  - [3] 2026-10-22: probe record, read with no API key: status 200, 3570 bytes, sha256 12f94b1ca5b0, and parsing the body gives 28 text models served by 51 workers, every model with at least one worker, median queue ETA 103 s, smallest models at ETA 0
  - [4] 2026-10-22: anonymous section: 'Use API key 0000000000', 'Lowest priority in generation queues', 'No need to register'
  - [4] 2026-10-22: kudos 'can never be bought or sold' and 'kudos never expire'
  - probe:aihorde.net 2026-11-04: the /api/v2 status endpoint answers JSON over HTTP, a REST interface | capture: sha256:6766c665ebe20a2ba0585107622843b0d41405fc0dfe3cf0729fc8c44fc16bf0 | quote: "content_type": "application/json"
- sources:
  - [1] https://aihorde.net/
  - [2] https://aihorde.net/api/v2/status/heartbeat
  - [3] https://aihorde.net/api/v2/status/models?type=text
  - [4] https://raw.githubusercontent.com/Haidra-Org/AI-Horde/main/README.md

## AI Horde (text generation)

- `inference/ai-horde-text` | qualifies-with-caveat | evidence documented | binding request-rate | category inference endpoint, volunteer GPU network, anonymous key
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:19.314Z (live) | stale on 2026-11-28
- url https://aihorde.net/
- free tier: Text generation on volunteer GPUs with no account: the README gives API key 0000000000 for anonymous use and 'No need to register'. Anonymous requests have the lowest priority and the service 'may be restricted for anonymous users during high load'. Kudos never expire. | unit: none | metered on: none | read on: 2026-10-28 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: the API key 0000000000 needs no registration; a registered account (OAuth2 login or a pseudonymous key) gets higher priority
- interface: rest
- limits:
  - request-rate (binding): no per-key quota is published for anonymous use; anonymous requests have the lowest priority and a request that finds no resources within the time limit times out. At the read: 97 text requests queued, 30 text workers on 64 text threads, 27861 tokens generated in the past minute [2]
  - request-rate (binding): per-model queue ETA across the 28 listed text models ran from 0 seconds to 516 seconds [3]
- binding note: the queue binds: anonymous jobs wait behind jobs from accounts holding kudos, and a job not served within the time limit times out
- endpoint: https://aihorde.net/api/
- tooling: REST API at https://aihorde.net/api/; any client that sends the key 0000000000 for anonymous use
- composes with: text jobs are served by whichever volunteer worker hosts the requested model, so the per-model queue ETA, not a quota, decides latency
- reliability: anonymous requests are the first restricted under high load, and a job not served within the time limit times out
- notes: Image generation on the same network is a separate offer (compute/ai-horde). The text catalogue changes with whichever volunteers are online.
- evidence note: that an anonymous generation completes with the key 0000000000 is documented and not measured; the pool figures are first-party API listings read once
- evidence:
  - [1] 2026-10-28: anonymous use is the key 0000000000 | capture: sha256:d69fdfd645939912016a2bbfdc5ed7e9bb89c415d04146fe9b027c10638d7748 | quote: - Use API key '0000000000'
  - [1] 2026-10-28: anonymous use needs no registration | capture: sha256:d69fdfd645939912016a2bbfdc5ed7e9bb89c415d04146fe9b027c10638d7748 | quote: - No need to register
  - [1] 2026-10-28: anonymous requests have the lowest queue priority | capture: sha256:d69fdfd645939912016a2bbfdc5ed7e9bb89c415d04146fe9b027c10638d7748 | quote: - Lowest priority in generation queues
  - [1] 2026-10-28: anonymous access can be restricted under load | capture: sha256:d69fdfd645939912016a2bbfdc5ed7e9bb89c415d04146fe9b027c10638d7748 | quote: - Service may be restricted for anonymous users during high load
  - [1] 2026-10-28: use is free, including anonymously, and kudos never expire | capture: sha256:d69fdfd645939912016a2bbfdc5ed7e9bb89c415d04146fe9b027c10638d7748 | quote: anyone can use it for free, even [anonymously](https://github.com/Haidra-Org/haidra-assets/blob/main/docs/definitions.md#anonymous), and kudos never expire
  - [4] 2026-10-28: a request not served within the time limit times out | capture: sha256:b50fb2ad2f38d414fc953a13f1f742c267c3a6aea82d9f643abb043070db819a | quote: If there are not enough resources to fulfill a request within a certain time limit, the request will time out and you will have to try again.
  - [5] 2026-10-28: the anonymous key can use generation with the lowest priority | capture: sha256:c187030e08f828054eb1ccfbc9f14fd45002d856d4f46a95e953d2c8420c86ac | quote: They can use the generation capabilities of the AI horde, but they have the lowest priority.
  - [2] 2026-10-28: text queue and worker counts at the read: 97 queued text requests, 30 text workers, 64 text threads | capture: sha256:67987aa0a8354c6bcd22d82ad71474503aac7dc6dc9884a0ab888d226b68c763 | quote: "queued_text_requests":97,"worker_count":21,"text_worker_count":30,"thread_count":22,"text_thread_count":64
  - [2] 2026-10-28: 27861 tokens were generated in the past minute against 33289 queued tokens | capture: sha256:67987aa0a8354c6bcd22d82ad71474503aac7dc6dc9884a0ab888d226b68c763 | quote: "queued_tokens":33289.0,"past_minute_tokens":27861.0
  - [3] 2026-10-28: the slowest listed text model had a queue ETA of 516 seconds; the listing holds 28 text models, counted from the response, and the fastest had an ETA of 0 | capture: sha256:aae0fef5abb8fbade255ce0ecb40e836577bbe1e445238007e6e97fac1f60741 | quote: {"performance":12.4,"queued":6402.0,"jobs":14.0,"eta":516,"type":"text","name":"aphrodite\/TheDrummer\/Behemoth-128B-v3-4.25bpw-h6-exl3","count":1}
  - probe:https://aihorde.net/api/ 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 405 at the recorded base URL, so the endpoint is not a completion route | capture: sha256:5539492a46abeb2fe344ac04c19c43d195a6688a22cef999ef8dbef766e611e2 | quote: "status": 405
- sources:
  - [1] https://raw.githubusercontent.com/Haidra-Org/AI-Horde/main/README.md
  - [2] https://aihorde.net/api/v2/status/performance
  - [3] https://aihorde.net/api/v2/status/models?type=text
  - [4] https://raw.githubusercontent.com/Haidra-Org/haidra-assets/main/docs/kudos.md
  - [5] https://raw.githubusercontent.com/Haidra-Org/haidra-assets/main/docs/definitions.md
