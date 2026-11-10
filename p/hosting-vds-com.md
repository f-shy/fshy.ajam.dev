# Hosting-VDS.com

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hosting-vds-com/ | JSON https://fshy.ajam.dev/api/v1/entity/hosting-vds-com.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hosting-VDS.com

- `compute/hosting-vds-com` | fails-identity | evidence reported | binding write-gated | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://lowendtalk.com/discussion/207701/scam-alert-hosting-vds-com
- free tier: A Russian-market VPS seller that accepts ordinary registration and payment from anyone and then, once the order is placed, requires phone verification with a Russian mobile number only, a condition not stated during signup. The buyer in the report could not verify, received no server, and was refused a refund. This is the clearest case in evaluated offerings of identity as the binding constraint: the quota was available, the payment cleared, and the door closed at verification. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | detail: a Russian mobile number for phone verification, demanded after registration and payment have completed and not disclosed at signup: the LowEndTalk report states registration and payment completed normally, then phone verification with a Russian mobile number was required, the server was never delivered and no refund was made. The payment route is the one the buyer had already cleared; no card type, hold amount or debit acceptance is stated. One reporting buyer only, so this is reported rather than documented | country: RU
- interface: unknown
- limits:
  - write-gated (binding): The gate is a Russian mobile number demanded after the money has moved, which is the worst placement of an identity check because it costs the buyer the transaction rather than the signup; nothing about capacity or price decides this provider. [1]
- limits note: The gate is a Russian mobile number demanded after the money has moved, which is the worst placement of an identity check because it costs the buyer the transaction rather than the signup; nothing about capacity or price decides this provider.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: part of the free tier
- composes with: It composes with nothing: the value of the record is that it marks a provider where a foreign buyer loses the payment rather than the order, so the subsequent evaluation does not spend a card authorisation to find out.
- reliability: no reliability event recorded
- notes: One reporting buyer, so the rung is reported and the pattern rests on a single account; a second independent report would move it. Two neighbours found in the same search and not recorded separately: 4vps.su, where a published complaint says a VDS was paid for and never worked, with no refund and a ticket left unanswered, and Digital-VM, reported on the same forum as having operated earlier as Virpus and shut down a paying customer's second server when a payment dispute was raised.
- extras:
  - facets.class: identity-gate-failure
  - facets.free_tier_kind: none
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: a July 2025 LowEndTalk post reports that registration and payment completed normally, that phone verification with a Russian mobile number was then required and had not been disclosed, that the server was never delivered and no refund was made, and that the support reply was abusive
- sources:
  - [1] https://lowendtalk.com/discussion/207701/scam-alert-hosting-vds-com
