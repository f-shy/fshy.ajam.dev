# Cathedral

> cathedral.computer | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cathedral/ | JSON https://fshy.ajam.dev/api/v1/entity/cathedral.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cathedral

- `compute/cathedral` | qualifies-with-caveat | evidence documented | binding volume-quota | category confidential sandbox | tier Pay-as-you-go confidential sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:55:06.271Z (live) | stale on 2026-12-26
- url https://cathedral.computer/pricing
- free tier: New accounts: one USD 20 trial credit, no card. The homepage may offer one sponsored starter: a 1 vCPU, 2 GiB confidential sandbox with network off that stops after ten minutes, which needs no sign-in or prepaid credit. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The USD 20 credit is a one-time account credit. The ten-minute sponsored starter is optional and appears only when the sponsored offer is available. No free recurring allowance is published.
- per-object cap: Disk is 50 GB, free, at every published size from 1 vCPU / 2 GiB to 8 vCPU / 16 GiB; the per-sandbox disk cap is not stated beyond that. | source: [1]
- retention: Billing starts when the sandbox is booked and stops when it is deleted or reaches its stop time; deletion removes its files. No separate retention period for stored files is published. | source: [1]
- egress: The pricing page prices memory-hours only and states no egress allowance or per-GB price; the console lets the caller lock egress and allow hosts one at a time. | metered: no | source: [1]
- identity: email | detail: The paid console asks the user to sign in with Google or an email link, and prepaid credit is added by card on Stripe before the first paid create. The sign-in flow is described on the docs page; an API key for server use is created on the Keys page.
- interface: rest, cli, browser
- limits:
  - volume-quota (binding): USD 20 one-time trial credit for new accounts, no card [1]
  - request-rate: 600 starts per minute and 1,000 confidential sandboxes at once [1]
  - retention-clamped: the optional sponsored starter is a 1 vCPU / 2 GiB sandbox with network off that stops after ten minutes [2]
- limits note: A paid create needs a spend cap above zero and credit covering the sandbox's lifetime at its hourly rate. Per-key rate limits are not enforced yet, and a key carries an approved budget and expiry.
- binding note: The one-time USD 20 credit is what runs out first for a new account: at the USD 0.01 per hour rate it is 2,000 sandbox-hours, before the 1,000-at-once or 600-starts-per-minute platform limits.
- interface detail: REST API at https://cathedral.computer/v1, the ctcli command-line client and a web console; confidential sandboxes have no SSH today and run each line of the console terminal through a line-mode terminal API.
- tooling: ctcli command-line client; REST API with a cat_sk_* API key sent as a bearer token.
- composes with: A paid sandbox can run an agent task and return signed command receipts; an agent can obtain a budgeted key by device login, and files must be saved elsewhere before the sandbox is deleted.
- reliability: Several catalogue products and the pool-claim path are marked Coming soon; one-shot runs are retired; there is no SSH into a confidential sandbox today and no public hardware attestation per room, only an attestation of the machine when it joins the pool.
- notes: The price is USD 0.0025 per GiB-hour at every size, so 2 vCPU / 4 GiB is USD 0.01 an hour and 730 hours is USD 7.30. A new account's USD 20 credit covers 2,000 hours of that size at list price. The ten-minute sponsored starter is anonymous but optional and may not be offered. The hosted sandbox needs prepaid card credit for the first paid create.
- evidence note: The rate, size table, trial credit, platform limits, sign-in methods and prepaid credit requirement were read from first-party pages.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 50
  - billing_model: per-second, prepaid credit
  - free_tier_kind: one-time-credit
  - term: no minimum
  - price_arithmetic: USD 0.0025 per GiB-hour x 4 GiB = USD 0.01/hour; USD 20 / USD 0.01 = 2,000 hours
  - status: live, pay-as-you-go; several catalogue SKUs marked Coming soon
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: published ports and ssh for non-confidential sandboxes; egress allowlisted per host
  - session_cap.restart_required: no
  - session_cap.note: paid sandbox stops at its booked stop time; the optional sponsored starter stops after ten minutes
- evidence:
  - [1] 2026-11-25: the 2 vCPU / 4 GiB confidential sandbox is USD 0.01 an hour billed by the second | capture: sha256:bb1fd93c0da95bd895383e2392114950b72dce29622b2832d13f19b29e621010 | quote: $0.01 an hour for 2 vCPU and 4 GiB, billed by the second.
  - [1] 2026-11-25: new accounts get one USD 20 trial credit with no card | capture: sha256:bb1fd93c0da95bd895383e2392114950b72dce29622b2832d13f19b29e621010 | quote: New accounts: one $20 trial credit, no card
  - [1] 2026-11-25: the page states a 1,000-sandbox concurrent figure | capture: sha256:bb1fd93c0da95bd895383e2392114950b72dce29622b2832d13f19b29e621010 | quote: 1,000
  - [2] 2026-11-25: paid sign-in uses Google or an email link and prepaid credit is needed before the first paid create | capture: sha256:f63e89f2eb6e046801334b266f937ebca1917d166bc11cd5cdf60160d573375d | quote: sign in with Google or an email link
  - [2] 2026-11-25: the first paid create needs credit for its spend cap | capture: sha256:f63e89f2eb6e046801334b266f937ebca1917d166bc11cd5cdf60160d573375d | quote: Add prepaid credit at /account/ before your first paid create; that create needs credit for its spend cap.
  - [2] 2026-11-25: the optional sponsored starter is a 1 vCPU / 2 GiB sandbox with the network off that stops after ten minutes | capture: sha256:f63e89f2eb6e046801334b266f937ebca1917d166bc11cd5cdf60160d573375d | quote: a 1 vCPU, 2 GiB confidential sandbox with network off that stops after ten minutes
  - [3] 2026-11-25: the API key is created from the Keys page after signing in with Google or a secure email link | capture: sha256:02a7966770fba08ecad3e8a641149c91034dfba1ab1cb1fb9a5f4484ace89724 | quote: Open Keys and continue with Google or a secure email link
  - [4] 2026-11-25: prepaid credit is paid by card on Stripe | capture: sha256:cbc793d55e3908c18b68680b0cd0924fb934419289d168115183736fb5101cb9 | quote: Choose a one-time pack. You pay by card on Stripe.
  - [1] 2026-11-24: no plans, packs or minimums and the same rate at any fleet size | capture: sha256:5b636783e23ad53b260cfbba1dee64614563916566a97445c38af4fc1a020e7a | quote: No plans, no packs, no minimums, and the same price for one sandbox or 1,000 at once.
  - [1] 2026-11-24: the rate is USD 0.01 an hour for 2 vCPU and 4 GiB, billed by the second | capture: sha256:5b636783e23ad53b260cfbba1dee64614563916566a97445c38af4fc1a020e7a | quote: $0.01 an hour for 2 vCPU and 4 GiB, billed by the second.
  - [1] 2026-11-24: the 2 vCPU 4 GiB size includes 50 GB of disk | capture: sha256:5b636783e23ad53b260cfbba1dee64614563916566a97445c38af4fc1a020e7a | quote: 2 vCPU 4 GiB memory 50 GB disk
  - [5] 2026-11-24: the earlier free one-shot is retired and does not start a sandbox or charge | capture: sha256:309593bb02ba14313599bf7f47dc4de88e7030bf1ba505d94b5e25f0831e5996 | quote: The Attest one-shot is retired.
  - [4] 2026-11-24: sign-in is by email link or Google and creates the account | capture: sha256:df1857d9ed338a01641ee048c901d5ad077a551e04c12954bc5d8e7bfb52b4fd | quote: Email a one-time link or continue with Google. New here? That creates your account.
  - [4] 2026-11-24: credit is prepaid by card on Stripe | capture: sha256:df1857d9ed338a01641ee048c901d5ad077a551e04c12954bc5d8e7bfb52b4fd | quote: Choose a one-time pack. You pay by card on Stripe.
  - [3] 2026-11-24: an agent needs a key a person approves with a budget and prepaid credit; an agent cannot pay | capture: sha256:02a7966770fba08ecad3e8a641149c91034dfba1ab1cb1fb9a5f4484ace89724 | quote: You add prepaid credit at
  - [6] 2026-11-24:  | capture: sha256:15e370cb42a7cffba93461bbc09fe730db31f38f0cb7e0e89a1ddc5398e4256f | quote: # CATHEDRAL
- sources:
  - [1] https://cathedral.computer/pricing
  - [2] https://cathedral.computer/docs
  - [3] https://cathedral.computer/docs/keys/
  - [4] https://cathedral.computer/account/
  - [5] https://cathedral.computer/docs/sandboxes/one-shot/
  - [6] https://cathedral.com/pricing
