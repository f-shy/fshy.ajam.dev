# swizzin.net

> swizzin.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/swizzin/ | JSON https://fshy.ajam.dev/api/v1/entity/swizzin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## swizzin.net

- `debrid/swizzin-net-shared-slot` | paid-only | evidence reported | category shared seedbox (managed slots, Netherlands) | tier shared slot (from USD 15.95/month)
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.242Z (live) | stale on 2026-11-18
- url https://swizzin.net/
- free tier: No free tier and no trial is published on the archived home page; shared slots start at USD 15.95 per month with a 7-day money-back guarantee. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The live site answered HTTP 503 on 2026-11-03; the page was read from a 2026-09-12 archive copy.
- per-object cap: unverified: the plan page https://swizzin.net/plans/ was not read | source: [1]
- retention: unverified: no retention statement on the archived home page | source: [1]
- egress: unverified: bandwidth terms are on the plan page, which was not read | metered: no | source: [1]
- identity: email | detail: unverified: the sign-up page was not read; a paid order with an account is implied by the money-back guarantee. | country: None
- interface: ssh
- limits note: unverified: storage and bandwidth per plan are on the plan page, which was not read.
- interface detail: 'All shared slots come with SSH access standard' plus a web dashboard that tracks disk, bandwidth and application status.
- tooling: SSH shell on the slot, the swizzin web dashboard and 19 supported apps
- composes with: A shared seedbox slot with SSH access, so a rsync or scp pull over SSH is possible; the quota and bandwidth terms are unverified
- reliability: The live home page answered HTTP 503 on 2026-11-03; the archive copy dates from 2026-09-12.
- notes: The vendor's plan page https://swizzin.net/plans/ holds the storage and bandwidth per slot.
- evidence note: The price and the SSH access come from an archive copy of the vendor home page; the live page was unavailable and the plan page was not read.
- extras:
  - minimum_term: unverified
  - trial_card_required: no trial is published
- evidence:
  - [1] 2026-11-03: shared slots start at USD 15.95/month with a 7-day money-back guarantee (archive copy of 2026-09-12) | capture: sha256:d1b394338299dc9dfe3f1804624365dac4112a9be12b07236cfe526e79b93a5a | quote: Optimized Seedbox Solutions Starting at $15.95/month* *7-Day money-back guarantee
  - [1] 2026-11-03: every shared slot has SSH access | capture: sha256:d1b394338299dc9dfe3f1804624365dac4112a9be12b07236cfe526e79b93a5a | quote: All shared slots come with SSH access standard, so you're free to install your own applications and services or setup your own cron jobs.
- sources:
  - [1] https://swizzin.net/
