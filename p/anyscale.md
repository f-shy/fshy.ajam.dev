# Anyscale

> anyscale.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anyscale/ | JSON https://fshy.ajam.dev/api/v1/entity/anyscale.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Anyscale

- `compute/anyscale` | qualifies-with-caveat | evidence documented | binding volume-quota | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-06T17:18:19.273Z (live) | stale on 2026-12-07
- url https://www.anyscale.com/pricing
- free tier: USD 100 of credit on a new account, from 'Get started with $100 credit'; the sign-up page heading renders 'Use work email for' with no amount. Per hour the rate card gives an NVIDIA L4 at AC 0.9542 and an NVIDIA A100 at AC 4.9591, with no memory size stated for the A100. H100, L40S and RTX 4090: not listed, the H, B and GB families carrying only a 'Contact Us' control. No GPU hour can be derived from the credit: every rate is in AC and the page publishes no AC-to-dollar rate. | unit: credits | metered on: wall-clock | read on: 2026-11-06 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a work email address is what the signup heading asks for; the credit attaches to an organisation rather than a person
- interface: unknown
- limits:
  - volume-quota (binding): USD 100 of Anyscale credits on a new account [1]
- limits note: the credit is denominated in the vendor's own currency on the rate card
- binding note: USD 100 is the balance, and the work-email gate decides whether the account exists at all
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the credit is a Ray control plane over rented GPUs, so it composes with any object store the jobs read from; it does not compose with a second Anyscale account, because the credit attaches to an organisation and one account is allowed per organisation.
- reliability: no reliability event recorded
- notes: The rate card is denominated in AC, not USD, and no AC-to-dollar rate is published, so the credit converts into no GPU hour. The sign-up page renders 'Use work email for' with no amount after it, so the USD 100 credit rests on the pricing page alone.
- evidence note: the pricing page was read on 2026-10-23; it states the $100 and the work-email gate, but every rate is quoted in AC rather than dollars
- extras:
  - facets.class: signup-credit
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_class: T4
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-23: quoted: 'Get started with $100 credit' and 'Use work email for $100 free credits'
  - [1] 2026-10-23: quoted rates: 'CPU Only - AC 0.0135 /hr', 'NVIDIA T4 - AC 0.5682 /hr'
  - [1] 2026-11-06: the A100 instance on the rate card is billed at AC 4.9591 an hour, with no memory size stated | capture: sha256:6b59a2ecd8ff4053d4c0de697d0c7081d352fc63795e64641e566c5ca026a2e9 | quote: AC 4.9591 /hr
  - [1] 2026-11-06: the offer is a credit balance on a new account | capture: sha256:6b59a2ecd8ff4053d4c0de697d0c7081d352fc63795e64641e566c5ca026a2e9 | quote: Get started with $100 credit
  - [1] 2026-11-06: the L4 instance is still AC 0.9542 an hour | capture: sha256:6b59a2ecd8ff4053d4c0de697d0c7081d352fc63795e64641e566c5ca026a2e9 | quote: AC 0.9542 /hr
  - [1] 2026-11-06: the pricing page states the USD 100 credit on a new account | capture: sha256:6b59a2ecd8ff4053d4c0de697d0c7081d352fc63795e64641e566c5ca026a2e9 | quote: Get started with $100 credit
  - [1] 2026-11-06: the one-time credit on a new account is USD 100, unchanged | capture: sha256:6b59a2ecd8ff4053d4c0de697d0c7081d352fc63795e64641e566c5ca026a2e9 | quote: Get started with $100 credit
  - [2] 2026-11-06: the sign-up page heading asks for a work email and renders no credit amount | capture: sha256:980ca08aa08bc780ab7e0f841041501572ed7c0cac152ee91d3ec58bb9f0c94f | quote: # Use work email for
- sources:
  - [1] https://www.anyscale.com/pricing
  - [2] https://authkit.anyscale.com/
