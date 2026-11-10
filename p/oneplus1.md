# Public Ollama instances

> oneplus1.top | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oneplus1/ | JSON https://fshy.ajam.dev/api/v1/entity/oneplus1.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Public Ollama instances

- `inference/public-ollama-instances` | fails-quota | evidence reported | binding none | category inference endpoint, third-party host
- needs card no, phone no, ID no, institution no | verified 2026-10-28T05:28:44.553Z (live) | stale on 2026-11-12
- url https://freeollama.oneplus1.top/
- free tier: lists of bare IP:port endpoints running Ollama with no authentication. The list host answered 200 with a 138-byte nginx 404 page on 2026-10-22, so the live list was not readable; the archived copy of 2026-05-21 shows the list's shape | unit: none | metered on: none | read on: 2026-10-22 | source: [1] | note: the live host returns a 404 body, not the list. Plain http returns 200 with 138 bytes; https fails the TLS principal-name check. The archived capture of 2026-05-21T16:07:33Z carries 39612 bytes titled 'Awesome Free Ollama' with a table of Server Address, Deployed Models and Last Updated, and the list's own warning that the services are exposed by misconfiguration
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no account at all; the endpoint is an exposed daemon
- interface: rest
- limits note: no rate or quota binds: the gate is access, not allowance. The software's published defaults are a queue of 512 requests (OLLAMA_MAX_QUEUE) before it answers 503 and 1 parallel request per loaded model (OLLAMA_NUM_PARALLEL); each instance's operator sets both.
- endpoint: http://IP:11434/v1/chat/completions
- tooling: any OpenAI-compatible client; curl against POST {base}/chat/completions
- composes with: no chain exists: there is no operator to promise a quota, so the scarce link is availability itself
- reliability: the list host itself stopped serving the list between 2026-05-21 and 2026-10-22, and the list warns that its entries are exposed by misconfiguration and unreliable. An instance is one operator's machine with no allowance and no notice before it stops
- notes: Two candidates explain the 404: the project moved, or it closed. The archive shows a working hourly-updated list in May, and no redirect is served today, so a move is not demonstrated and a closure is the simpler reading. Either way the record cannot promise an endpoint, which is why the verdict stays fails-quota: an address that may vanish hourly with no operator is not a quota. This record is stale by design: its only evidence for the list's shape is an archived capture 154 days old, because the live host serves a 404 page. The category claim is the archive plus the list's own warning. Re-read it when the host serves a list again.
- evidence note: the list's shape is from an archived capture and the live host no longer serves it, so no endpoint from this category was called. The category claim rests on the archive plus the list's own warning, which is third-party in both directions
- evidence:
  - [1] 2026-10-22: plain http returned 200 with a 138-byte nginx 404 page; https failed the TLS principal-name check. The list itself was not served, so this route is closed today
  - [2] 2026-05-21: the archived page is titled 'Awesome Free Ollama' and carries a table of Server Address, Deployed Models, Check Service and Last Updated, updated hourly, with the note 'It is not recommended to use these services as they may be unreliable'
  - [3] 2026-10-28: the Ollama FAQ gives a default queue of 512 requests before rejection; the same page gives OLLAMA_NUM_PARALLEL default 1 and says an overloaded server responds with 503 | capture: sha256:799c4f0830f93fe8a466e5953e75969770357ad590f98cf6684796bc3c6123eb | quote: * `OLLAMA_MAX_QUEUE` - The maximum number of requests Ollama will queue when busy before rejecting additional requests. The default is 512
  - probe:http://freeollama.oneplus1.top/ 2026-10-28: plain http returned 200 with a 138-byte text/html body from nginx (content-length 138, last-modified 2024-10-09), the same stub as before; https failed certificate verification with a hostname mismatch; no instance list was served and no instance was called
- sources:
  - [1] https://freeollama.oneplus1.top/
  - [2] https://web.archive.org/web/20260521160733/https://freeollama.oneplus1.top/
  - [3] https://docs.ollama.com/faq
