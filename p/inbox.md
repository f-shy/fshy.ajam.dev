# inbox.eu free

> inbox.eu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inbox/ | JSON https://fshy.ajam.dev/api/v1/entity/inbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## inbox.eu free

- `storage/inbox-eu-free` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:24.330Z (live) | stale on 2026-11-18
- url https://help.inbox.eu/mailbox-size?language=en
- free tier: None reachable: Messaging docs say 20 GB ("Mailbox size .. is the same - 20Gb") but the pricing page's 100 GB is the 30-day Business trial with a 3-emails-per-day send throttle. Classic trial-vs-free co. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: unverified: the vendor pages state no download or egress allowance or price; the free plan sends up to 3 emails per day. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the 2026-11-03 evidence rows read the vendor pages https://www.inbox.eu/en/pricing/ (free plan send throttle) and https://help.inbox.eu/mailbox-size?language=en (mailbox size); the vendor pages state no download or egress allowance, so the egress verdict is not supported by a vendor quote
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Messaging docs say 20 GB ("Mailbox size ... is the same - 20Gb") but the pricing page's 100 GB is the 30-day Business trial with a 3-emails-per-day send throttle — classic trial-vs-free…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Messaging docs say 20 GB ("Mailbox size ... is the same - 20Gb") but the pricing page's 100 GB is the 30-day Business trial with a 3-emails-per-day send throttle — classic trial-vs-free co
  - [2] 2026-10-21: cited as the basis of the rejection: Messaging docs say 20 GB ("Mailbox size ... is the same - 20Gb") but the pricing page's 100 GB is the 30-day Business trial with a 3-emails-per-day send throttle — classic trial-vs-free co
  - [2] 2026-11-03: the free plan limits sending to 3 emails per day; no download or egress allowance or price is stated | capture: sha256:8242bf88260d0a0eed9ce7b70a21dc6c67bf96beb2d2a4eb95f527a997c5be72 | quote: With the free plan, you can send up to 3 emails per day with a limited number of recipients per message.
  - [1] 2026-11-03: mailbox size is 20 GB | capture: sha256:4a12b3ef1ec90e6cc74b96ab3933d132b00994e5f3e6d0acdc88bc90662d14af | quote: is the same - 20Gb
- sources:
  - [1] https://help.inbox.eu/mailbox-size?language=en
  - [2] https://www.inbox.eu/en/pricing/
