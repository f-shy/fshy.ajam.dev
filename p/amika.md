# Amika

> amika.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/amika/ | JSON https://fshy.ajam.dev/api/v1/entity/amika.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Amika

- `compute/amika` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card unknown, phone no, ID no, institution no | verified 2026-11-04T15:51:56.484Z (live) | stale on 2026-12-05
- url https://www.amika.dev/pricing
- free tier: $50 of credits per organisation, unlimited sandboxes on the user's own machines at no charge, up to 10 concurrent service-account sandboxes and 3 active users a month. | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page prices hosted compute, memory and storage per hour and lists no egress allowance or per-GB overage | metered: no | source: [1]
- identity: email | detail: an email address and a name at sign-up: the join form asks 'First name Last name Email Continue' and offers 'Continue with Google' or GitHub in place of the email, and it carries no phone field. Whether a payment method is asked for while the free plan's credits are claimed is unverified: behind a sign-up; neither the join page nor https://www.amika.dev/pricing publishes one.
- interface: ssh, cli, rest
- limits:
  - request-rate (binding): 3 active users a month on Free and 10 concurrent service-account sandboxes [1]
  - per-object-cap: past 3 active users the whole organisation moves to Team at $30 an active user a month [1]
- interface detail: SSH, the CLI and the API; a TypeScript SDK (@amika/sdk) and a web UI also exist
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The free tier includes USD 50 of credits and up to 10 concurrent service-account sandboxes, which the vendor meters; the unlimited sandboxes run on machines the user supplies.
- evidence note: the pricing page was read on 2026-10-22. The free grant is USD 50 of credits, and the important half is that hours on the user's own machines are never charged on any plan, which makes the hosted credit a convenience rather than the capacity.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: hosted sandboxes bill per second; hours on a user's own machines are never charged and have no clock
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
  - [2] 2026-11-04: docs ship a CLI and SDKs | capture: sha256:c3b14401a9f105c469d5eb3e92aeca33825a79a0eb205874c47dda6287654d2b | quote: [Install](https://docs.amika.dev/install.md): Install the Amika CLI and SDKs.
  - [1] 2026-11-04: the hosted rate table has compute, memory and storage rows and no network row | capture: sha256:3bb1cab29d9cbbd2bb46fa157e861d3eeb189c2e93976cac37606a86cdc7ff7c | quote: | Storage (GiB) | $0.0001134 / h | $0.0000000315 / s |
  - [3] 2026-11-04: the sign-up form collects a name and an email address, with GitHub and Google as alternatives | capture: sha256:77cdd42f222a06849f638739366f376858ab130dac56ffd08651f19065faaac4 | quote: First name Last name Email Continue
  - [3] 2026-11-04: Google OAuth is offered beside the email form, so an email address is the documented route rather than the only one | capture: sha256:77cdd42f222a06849f638739366f376858ab130dac56ffd08651f19065faaac4 | quote: Continue with Google
  - [4] 2026-11-04: the documented start is a sign-up at the same form | capture: sha256:2ac0c497fbdbfb70bc1ccb11c71746511028298fb7ac4c49d17406af8b91be96 | quote: Sign up at [https://app.amika.dev/signup](https://app.amika.dev/signup) and follow onboarding.
- sources:
  - [1] https://www.amika.dev/pricing
  - [2] https://docs.amika.dev/llms.txt
  - [3] https://app.amika.dev/signup
  - [4] https://docs.amika.dev/quickstart.md
