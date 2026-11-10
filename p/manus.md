# Manus Cloud

> manus.im | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/manus/ | JSON https://fshy.ajam.dev/api/v1/entity/manus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Manus

- `compute/manus` | qualifies-with-caveat | evidence documented | binding request-rate | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://help.manus.im/en/articles/11711111-what-is-the-current-membership-pricing-for-manus
- free tier: Manus Free: "Free Plan Price: $0/month", "Daily Refresh Credits: 300 credits provided daily", "Concurrent Tasks: Supports 1 concurrent task", "Free users only have access to Manus 2.0 Lite in Agent Mode", quoted | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): the daily 300 credits are also capped at 1,500 a month for free accounts, so the fifth day ends the allowance and the remaining 25 days serve nothing. [1]
- limits note: the daily 300 credits are also capped at 1,500 a month for free accounts, so the fifth day ends the allowance and the remaining 25 days serve nothing.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Manus produces artefacts while external file hosts can serve output data.
- reliability: no reliability event recorded
- notes: compute/manus-cloud-computer already records Manus Cloud Computer as paid-only at USD 30 a month for 2 vCPU, 4 GB and 70 GB. That record is about the persistent server, not the agent, and it would read as 'Manus has no free tier' unless this finding sits beside it. Merge into a single Manus record, not a second provider row. The unit here is a credit and the vendor publishes no credit-to-minute rate, so 1,500 monthly credits cannot be converted to hours. A one-time 1,000 credits are granted at signup, separate from the daily refresh. The 1,500 monthly cap is the number the marketing does not show.
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: recurring-allowance
- evidence:
  - [1] 2026-10-22: the Free plan block gives 300 daily refresh credits, 1 concurrent task and Manus 2.0 Lite only, quoted; Pro starts at USD 20 for 4,000 monthly credits
  - [2] 2026-10-22: "The monthly consumption limit for daily refresh credits for free users is set to 1,500 credits" quoted, and daily credits can only be used in the Lite mode
  - [3] 2026-10-22: daily credits must be claimed by logging in each day, are valid for that day only, and do not accumulate, quoted
  - [1] 2026-10-22: probe GET returned status 200, 126147 bytes, sha256 70442b0bb56d8d090f9a31dedcfd68c469f039c4b9c829e041adc25c9d0bad51, no challenge detected, at 2026-10-22T15:23:49Z
- sources:
  - [1] https://help.manus.im/en/articles/11711111-what-is-the-current-membership-pricing-for-manus
  - [2] https://help.manus.im/en/articles/11711097-what-are-the-rules-for-credits-consumption-and-how-can-i-obtain-them
  - [3] https://help.manus.im/en/articles/11985189-what-should-i-do-if-my-daily-refresh-credits-have-not-refreshed

## Manus Cloud Computer

- `compute/manus-cloud-computer` | paid-only | evidence documented | binding retention-clamped | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:22.321Z (live) | stale on 2026-11-22
- url https://help.manus.im/en/articles/15392078-understanding-cloud-computer-plans-and-billing
- free tier: no free tier: Cloud Computer is a persistent Ubuntu server on a subscription, $30 a month for 2 vCPU, 4 GB and 70 GB, $50 for 2 vCPU, 8 GB and 120 GB | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: $30 a month for 2 vCPU, 4 GB and 70 GB; $50 for 2 vCPU, 8 GB and 120 GB [1]
  - retention-clamped (binding): cancelling shuts the machine down and deletes the working files, installed tools and databases on it; only files already delivered into the chat survive [1]
- limits note: Session cap, idle-reap and network policy are not documented. Ranked partial.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: Cancellation terms govern resource retention.
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.vcpu: 2
  - shape.ram: 4
  - shape.disk: 70
  - shape.gpu_count: 1
  - shape.note: Standard at 2 vCPU, 4 GB and 70 GB; Advanced at 2 vCPU, 8 GB and 120 GB
  - session_cap.restart_required: no
  - session_cap.note: the machine runs continuously while the subscription is active; the clock is the subscription, and cancellation is a delete rather than a stop
  - free_tier_kind: none
  - ps.gib: 70
  - ps.price: included in the subscription
  - ps.durability: persistent VM disk, destroyed on cancellation
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the subscription term; cancellation deletes it
  - net.out: yes
  - net.in: yes
  - net.ports: a dedicated public IP address on every plan
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Standard Plan ($30/month): 2 vCPUs, 4 GB of RAM, and 70 GB of storage', 'Advanced Plan ($50/month): 2 vCPUs, 8 GB of RAM, and 120 GB of storage', 'maintaining an active subscription is required to keep your environment running', and on cancellation 'The persistent virtual machine will be shut down' and 'Your working files, installed tools, and databases ... will be deleted', quoted
- sources:
  - [1] https://help.manus.im/en/articles/15392078-understanding-cloud-computer-plans-and-billing
