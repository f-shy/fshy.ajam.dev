# RuWeb

> ruweb.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ruweb/ | JSON https://fshy.ajam.dev/api/v1/entity/ruweb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RuWeb

- `compute/ruweb` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://ruweb.net/test-vds
- free tier: Six days of VPS free, activated automatically once the balance is topped up, with the deposit staying on the balance afterwards for any order or transfer to another account. The amount is stated as RUB 300 in the body of the trial page and as RUB 200 twice in the same page's questions, and the promotions page says RUB 300 for a VPS and RUB 100 for shared hosting, so the provider publishes three numbers for one deposit. Ports 25 and 465 are closed until the trial is converted to a paid order, and on tariffs from KVMz-PROF upward the test needs support approval. The cheapest paid shape is advertised from RUB 169 a month, with European and non-CIS locations sold from the same catalogue. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: deposit-gated-trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: the trial is gated on a deposit rather than a document: six days of VPS activate automatically once the balance is topped up, with RUB 300 named in the body of the trial page, RUB 200 twice in the same page's FAQ, and RUB 300 for a VPS on the promotions page, and the deposit stays on the balance or is refunded on request. The record does not name the payment rail, whether a card is required, any hold, or whether debit or prepaid cards are accepted
- interface: unknown
- limits:
  - write-gated (binding): The deposit is the gate and the closed mail ports are the design constraint: six days of a machine that cannot send mail is a web-hosting trial rather than a server trial, and the RUB 169 floor plan is sized for a site, not for a transfer workload. [1]
- limits note: The deposit is the gate and the closed mail ports are the design constraint: six days of a machine that cannot send mail is a web-hosting trial rather than a server trial, and the RUB 169 floor plan is sized for a site, not for a transfer workload.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At RUB 169 a month this is the cheapest 24/7 machine found in this category, and the deposit composes with the trial: RUB 300 covers nearly two months of the floor plan after the six free days, so the first paid month is already funded by money that was never a fee.
- reliability: no reliability event recorded
- notes: RuWeb provides VPS hosting starting from RUB 169 monthly. Activation of trial credits requires a minimum deposit top-up via supported payment methods.
- extras:
  - facets.class: regional-low-floor
  - facets.free_tier_kind: deposit-gated-trial
  - facets.shape.gpu_count: 0
  - facets.shape.note: the trial covers any tariff; the published floor is RUB 169 a month
- evidence:
  - [1] 2026-10-22: six-day free trial activated automatically after a top-up, with RUB 300 named in the body and RUB 200 named twice in the FAQ on the same page, ports 25 and 465 closed until payment, and the top-up remaining on the balance or transferable, quoted and translated
  - [2] 2026-10-22: the promotions page states RUB 300 for the VPS trial and RUB 100 for the shared-hosting trial, with the deposit refunded on request if the offer terms were not breached, quoted and translated
  - [3] 2026-10-22: the catalogue is titled as Linux VPS from RUB 169 a month, the lowest monthly figure found for an addressed 24/7 machine
- sources:
  - [1] https://ruweb.net/test-vds
  - [2] https://ruweb.net/promotions
  - [3] https://ruweb.net/vps-linux
