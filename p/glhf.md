# GLHF

> glhf.chat | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/glhf/ | JSON https://fshy.ajam.dev/api/v1/entity/glhf.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GLHF (glhf.chat)

- `inference/glhf` | dead | evidence measured | binding none | category inference, usage-billed open-model hosting, renamed Synthetic, old host failing
- identity a placeholder: card and phone unknown | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://glhf.chat/pricing
- free tier: none now: the glhf.chat host answers HTTP 526 and the product is renamed Synthetic, a $30 a month subscription; the 2025-01-01 billing launch granted $10 of credit to beta users | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: unverified: the sign-up page does not load (HTTP 526), so what registration asked for cannot be read; the kind is the nearest term
- interface: rest
- limits note: no rate or quota can be read: the host answers HTTP 526
- binding note: no limit binds: the old host does not serve
- endpoint: https://glhf.chat/api/openai/v1/chat/completions
- tooling: OpenAI-compatible client; the rebrand post says the old API base URLs keep working, and the new base URL is api.synthetic.new
- composes with: successor product Synthetic (synthetic.new)
- reliability: on 2026-11-04 the old API path glhf.chat/api/openai/v1/chat/completions answered HTTP 526 and api.glhf.chat failed TLS verification (certificate not valid for the host name), while the vendor's rebrand post says the old API base URLs should continue to work without interruption
- notes: dead cause: dead-service; the product continues as Synthetic (synthetic.new), which lists a $30 a month subscription and no free tier on its pricing page
- evidence note: the 526 answers are probe records; the rename is a first-party post
- evidence:
  - probe:glhf.chat 2026-11-04: the root host answered HTTP 526 | capture: sha256:01fba5ae72d26d2578156eb40bd8ab718d948be6db56b98907383c6dbb8d3c8f | quote: "status": 526
  - [1] 2026-11-04: the vendor retired the glhf.chat name for Synthetic | capture: sha256:a7634dcdb51ebb39457827ce9f3fbf696098e5a3bfb8951a9f6ab8ecb9858ef9 | quote: We're renaming ourselves from glhf.chat to Synthetic!
  - [2] 2026-11-04: the successor lists a $30 a month subscription plan | capture: sha256:2901e22bda1622cd203dc6fc95a248c99251ae9482b4fa0824784b9b5106145a | quote: $30/month
  - [3] 2026-11-04: the billing launch of 2025-01-01 ended the free beta and granted $10 credits | capture: sha256:e70d2371e199208eac39e59fecb14861d9b9e5174aec2140b1028b57a2f9b671 | quote: We're giving everyone who tried the site during the free beta $10 in credits to try it out
  - probe:glhf.chat/api 2026-11-04: the old API path answered HTTP 526 | capture: sha256:fb88deb1687b72617e2fd4633d03b9d4a678aaa7629327f5c23de4b5fd21df93 | quote: "status": 526
  - probe:api.glhf.chat 2026-11-04: api.glhf.chat failed TLS verification | capture: sha256:386915e03d3fe07d2b031022954f6e92f286d6e8aec95cd132e7e91da3164734 | quote: "error": "tls_untrusted"
  - probe:api.synthetic.new 2026-11-04: the successor API host answered HTTP 200 on its models path | capture: sha256:8202bb410af556612a4f406586b58d74ce7552c750dabc4b0019c89360fe1559 | quote: "status": 200
  - [1] 2026-11-04: the vendor states the old API base URLs keep working | capture: sha256:e1878c5579915b3ec4422a64ec107cbbe00ace35c3a428992bc9ccc7d7f5675f | quote: our old API base URLs should also continue to work without interruption
- sources:
  - [1] https://synthetic.new/blog/rebrand
  - [2] https://synthetic.new/pricing
  - [3] https://glhf.chat/newsletter/entries/billing-launch
