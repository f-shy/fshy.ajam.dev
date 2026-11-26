# Amika

> amika.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/amika/ | JSON https://fshy.ajam.dev/api/v1/entity/amika.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Amika

- `compute/amika` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-24T11:38:08.094Z (live) | stale on 2026-12-25
- url https://www.amika.dev/pricing
- free tier: Free is $0 a month with up to 3 members, unlimited member sandboxes on the user's own machines (uncharged on every plan) and 10 concurrent API sandboxes; Amika cloud compute is charged by the second on every plan. The old $50 credit grant is no longer listed. | unit: mixed | metered on: wall-clock | read on: 2026-11-24 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page prices hosted compute, memory and storage per hour and lists no egress allowance or per-GB overage | metered: no | source: [1]
- identity: email | detail: unverified: the sign-up page read on 2026-11-24 displays no registration fields; the terms name a main email address on the account and the CLI login reference describes browser device authorization, but neither states the fields sign-up asks for. No payment method is published for Free.
- interface: ssh, cli, rest
- limits:
  - request-rate (binding): up to 3 members on Free, with unlimited member sandboxes and 10 concurrent API sandboxes [1]
  - per-object-cap: Team is $100 a month with 3 members included and $30 for each additional member; Scale is $500 a month [1]
- interface detail: SSH, the CLI and the API; a TypeScript SDK (@amika/sdk) and a web UI also exist
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The 2026-11-04 pricing page listed USD 50 of credits per organization on Free; the page read on 2026-11-24 lists no credit. Free keeps up to 10 concurrent API sandboxes, and the unlimited member sandboxes run on machines the user supplies.
- evidence note: the pricing page was read on 2026-11-24. The USD 50 grant listed on 2026-11-04 is no longer on the page, and the important half is that hours on the user's own machines are never charged on any plan, which makes any hosted credit a convenience rather than the capacity.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no maximum session or idle reap published; hosted rigs bill per second and are stopped by the user
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
  - ps.price: a user's own machines hold the state; hosted sandboxes bill per second
  - ps.durability: a user's own hardware
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: as long as the machine exists
  - net.out: yes
  - net.in: yes
  - net.ports: SSH, CLI and API
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$50 of credits per organization to start' and 'Unlimited sandboxes on any number of your own machines' and 'Up to 10 concurrent service-account sandboxes' and 'Free allows 3 a month' active users, and 'Sandboxes there run on every plan and their hours are never charged', quoted
  - [1] 2026-11-04: the Free plan lists SSH, the CLI and the API as ways to connect | capture: sha256:3bb1cab29d9cbbd2bb46fa157e861d3eeb189c2e93976cac37606a86cdc7ff7c | quote: Connect from Cursor, Codex, SSH, the CLI, or the API
  - [1] 2026-11-04: the hosted rate table has compute, memory and storage rows and no network row | capture: sha256:3bb1cab29d9cbbd2bb46fa157e861d3eeb189c2e93976cac37606a86cdc7ff7c | quote: | Storage (GiB) | $0.0001134 / h | $0.0000000315 / s |
  - [2] 2026-11-04: the sign-up form collects a name and an email address, with GitHub and Google as alternatives | capture: sha256:77cdd42f222a06849f638739366f376858ab130dac56ffd08651f19065faaac4 | quote: First name Last name Email Continue
  - [3] 2026-11-04: the documented start is a sign-up at the same form | capture: sha256:2ac0c497fbdbfb70bc1ccb11c71746511028298fb7ac4c49d17406af8b91be96 | quote: Sign up at [https://app.amika.dev/signup](https://app.amika.dev/signup) and follow onboarding.
  - [4] 2026-11-18:  | capture: sha256:9c72b1c54c7683816fcc296faf20798f52f9bc55dd194ebd14becf9bdcf00ea8 | quote: wait ... polls every 3 seconds until the rig is `stopped` ... for up to 15 minutes
  - [1] 2026-11-24: the Free plan is $0 a month and aimed at machines the user supplies | capture: sha256:c7d1a482610eb3dda349ff6efb407a157ba19448b1f3235761f84ecca98d37ac | quote: For small teams on their own machines $0 / mo
  - [1] 2026-11-24: Free allows 10 concurrent API sandboxes | capture: sha256:c7d1a482610eb3dda349ff6efb407a157ba19448b1f3235761f84ecca98d37ac | quote: API sandboxes 10 at a time
  - [1] 2026-11-24: Team includes 3 members and charges $30 for each further member | capture: sha256:c7d1a482610eb3dda349ff6efb407a157ba19448b1f3235761f84ecca98d37ac | quote: Members 3 included, then $30 each
  - [2] 2026-11-24: the captured sign-up page does not display the registration fields | capture: sha256:eacc704e1573dd2f7d4e22ef49b2f971beaba26541fa90c890cdbb895aeb4c40
  - [1] 2026-11-24: sandboxes on machines the user supplies are not charged on any plan | capture: sha256:c7d1a482610eb3dda349ff6efb407a157ba19448b1f3235761f84ecca98d37ac | quote: Your machines: free
  - [1] 2026-11-24: hosted storage is $0.0001134 per GiB-hour | capture: sha256:c7d1a482610eb3dda349ff6efb407a157ba19448b1f3235761f84ecca98d37ac | quote: | Storage (GiB) | $0.0001134 / h | $0.0000000315 / s |
  - [1] 2026-11-24: the vendor names the web UI, CLI and MCP as ways to start a sandbox | capture: sha256:c7d1a482610eb3dda349ff6efb407a157ba19448b1f3235761f84ecca98d37ac | quote: Started by a person, whether that's the web UI, CLI, or MCP.
  - [1] 2026-11-24: the hosted rate table prices compute, memory and storage and lists no network charge | capture: sha256:c7d1a482610eb3dda349ff6efb407a157ba19448b1f3235761f84ecca98d37ac | quote: Amika cloud: charged by the second for vCPU, RAM, and storage (pricing below)
- sources:
  - [1] https://www.amika.dev/pricing
  - [2] https://app.amika.dev/signup
  - [3] https://docs.amika.dev/quickstart.md
  - [4] https://docs.amika.dev/llms.txt
