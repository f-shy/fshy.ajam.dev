# Lynkr

> github.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-fast-editor/ | JSON https://fshy.ajam.dev/api/v1/entity/github-fast-editor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lynkr

- `inference/lynkr` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category self-hosted LLM gateway/proxy (self-hosted)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://github.com/Fast-Editor/Lynkr
- free tier: the gateway is free and open-source (Apache 2.0) and installs locally via npm; it routes simple requests to the user's own free local backends (Ollama, llama.cpp, LM Studio, vLLM), but serves no hosted capacity of its own | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no account; the gateway is installed locally from npm
- interface: rest
- binding note: the proxy itself has no hosted quota; capacity comes from backends the reader supplies
- endpoint: http://127.0.0.1:8081/v1
- tooling: npm install -g lynkr; a local OpenAI-compatible endpoint at 127.0.0.1:8081/v1
- composes with: pairs with a coding agent through the local gateway; the scarce link is the user's own local models or subscriptions it routes to
- reliability: no reliability event recorded
- notes: self-hosted last resort: a free routing proxy with no hosted inference capacity of its own.
- self hosted: yes
- evidence:
  - [1] 2026-11-18: free local backends provide 100% offline free usage through the gateway | capture: sha256:470cfeac31230a720ce4e4274a3507683382db99bf148346c894d7277297c98b | quote: 4 local providers for 100% offline, free usage. 14+ cloud providers for scale.
- sources:
  - [1] https://github.com/Fast-Editor/Lynkr
