# Tinfoil

> tinfoil.sh | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tinfoil/ | JSON https://fshy.ajam.dev/api/v1/entity/tinfoil.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tinfoil (Compute)

- `compute/tinfoil` | paid-only | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-25T11:17:42.693Z (live) | stale on 2026-12-26
- url https://tinfoil.sh
- free tier: no free tier published: the page lists Chat at $20/month, Inference at usage-based pricing, Containers at usage-based pricing, and Bunkers at $0.32/hour plus storage | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no plan and no price appear in the extracted body; capacity is the vendor's own multi-GPU infrastructure [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and describes verifiably private inference on the vendor's own multi-GPU hardware, with no plan or price. That confirms paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an inference API answers tokens; there is no machine to hold
  - free_tier_kind: none
  - granularity.min_billed_s: 3600
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Featured in a Llama case study as the only multi-GPU infrastructure offering production-ready, verifiably private AI' with a 'Supported hardware' section; no plan and no price in the extracted body
  - [1] 2026-11-25: the page lists Chat at $20/month, Inference and Containers at usage-based pricing, and Bunkers at $0.32/hour plus storage, with no free tier | capture: sha256:13698222c8ec6740f6ab0ed3a5695b9a89cdee2be389a31f8c3c2aa72d50c03b | quote: Chat ... $20/month ... Inference ... Usage-based pricing ... Containers ... Usage-based pricing ... Bunkers ... $0.32/hour + storage
  - [1] 2026-11-25: the page still lists all four paid products and their stated prices with no free tier | capture: sha256:13698222c8ec6740f6ab0ed3a5695b9a89cdee2be389a31f8c3c2aa72d50c03b | quote: Chat ... $20/month ... Inference ... Usage-based pricing ... Containers ... Usage-based pricing ... Bunkers ... $0.32/hour + storage
- sources:
  - [1] https://tinfoil.sh

## Tinfoil (Inference)

- `inference/tinfoil` | paid-only | evidence documented | binding volume-quota | category private inference endpoint and chat, paid
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://tinfoil.sh/pricing
- free tier: no free inference allowance stated: Tinfoil Chat is USD 20 per month and the inference API requires an API key; no free-token quota appears on the pages read | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key is obtained to use Tinfoil Inference; signup fields not stated on the docs pages read
- interface: rest
- limits:
  - volume-quota (binding): Tinfoil Chat is USD 20/month; inference requires an API key; no free allowance published [1]
- binding note: no free tokens stated, so payment binds first
- endpoint: https://inference.tinfoil.sh/v1
- tooling: an OpenAI-compatible key plus the Tinfoil SDKs that verify enclave attestations
- composes with: pairs with an OpenAI-compatible agent through a key on a paid plan
- reliability: no reliability event recorded
- notes: privacy-focused enclave inference sold as a USD 20/month chat plan and a keyed API; no free tier found.
- evidence:
  - [1] 2026-11-18: Tinfoil Chat is a paid monthly plan | capture: sha256:2ce224dd680bc24c1816ef01185d02534f1fb92bfe077727e429d3b21043f100 | quote: $20/month
- sources:
  - [1] https://tinfoil.sh/pricing
