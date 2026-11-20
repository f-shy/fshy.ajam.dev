# Internxt

> internxt.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/internxt/ | JSON https://fshy.ajam.dev/api/v1/entity/internxt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Internxt — 100 TB lifetime via StackSocial

- `storage/internxt-100-tb-lifetime-via-stacksocial` | paid-only | evidence documented | binding volume-quota | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-11-04T01:24:26.447Z (live) | stale on 2026-12-05
- url https://internxt.com/lifetime
- price USD 9.75 per TB one-time (lifetime, not monthly): 100 TB for USD 974.97 on StackSocial
- free tier: 1 GB of storage for life with a free account (name and email address) | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: no per-file size is stated on the listing; 100 TB is the total storage of the plan | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered per-GB in published terms; zero-knowledge encrypted shards. No egress line quoted. | metered: yes
- identity: email | detail: name and email address; the vendor states no identity or email verification is required to start
- interface: rest, webdav, rclone, cli
- limits:
  - volume-quota (binding): 100 TB cap [1]
- limits note: 100 TB cap, new users only, codes not stackable. CRITICAL: the StackSocial listing states the plan 'does not include ... CLI, WebDAV ... which are sold separately by Internxt'. The 100 TB SKU is web/app-only unless you buy the add-ons.
- binding note: the plan holds up to 100 TB in total for one payment; the StackSocial listing says codes are not stackable
- interface detail: rest
- tooling: Rclone backend `internxt` (added v1.73) + WebDAV + CLI. BUT the rclone docs carry an explicit caveat: 'The Internxt backend may not work with all account types.'.
- composes with: $9.75/TB. By far the cheapest real per-TB lifetime figure found. Codes are explicitly NOT stackable, so 100 TB is the hard ceiling per purchase; separate accounts would be separate purchases.
- reliability: Post-quantum E2E encryption means a lost password is unrecoverable. The deal channel covering Internxt carries a warning that 'they can scam you by closing account with no reason'; in plain terms, a buyer's report that the account can be closed without a stated reason. The rclone/WebDAV exclusion on this specific SKU is the practical killer for programmatic use.
- notes: Free: 1 GB for life. Paid: 100 TB lifetime, one-time payment, on StackSocial.
- evidence note: documented from vendor pages read on 2026-11-03: the 1 GB free allowance and the sign-up fields (https://internxt.com/pricing), and the 100 TB total of the lifetime plan (the StackSocial listing). Egress, retention, per-object cap and the rclone note were not read on that date.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 100 TB lifetime, $974.97 (suggested $9,900, 90% off) on StackSocial. Vendor's own direct tiers are 1 TB / 2 TB / 5 TB / 10 TB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Deal Price $974.97 ... available to new users ONLY ... Codes are NOT stackable ... does not include ... CLI, WebDAV', fetched 2026-10-21
  - [2] 2026-10-21: 'The Internxt backend may not work with all account types'
  - [3] 2026-10-21: 'Internxt 5 TB $799 ... plans stackable to 100 TB on one account' (contradicts the StackSocial 'not stackable')
  - [4] 2026-11-03: the free membership gives 1GB for life | capture: sha256:35ba783a0bc18310809ee71a4bef15fb0592b54c2060cd7dfcf1e5318a273e8d | quote: There, you will instantly get 1GB of free storage for life with a free Internxt membership.
  - [4] 2026-11-03: the free allowance is stated in GB | capture: sha256:35ba783a0bc18310809ee71a4bef15fb0592b54c2060cd7dfcf1e5318a273e8d | quote: There, you will instantly get 1GB of free storage for life with a free Internxt membership.
  - [1] 2026-11-03: the StackSocial listing is a single 100TB lifetime code that is not stackable | capture: sha256:b2da48abcf8bfa8656e85ee120fae8dc1cd370512df7949548e2be0973dac405 | quote: - Codes are NOT stackable.
  - [1] 2026-11-03: the StackSocial price is 974.97 USD | capture: sha256:098d9b4ad357da2e61da727d9888ead78f6fa515ca7fffb9172d40698690642a | quote: "priceCurrency":"USD","price":"974.97"
  - [1] 2026-11-03: 100TB is the total storage of the plan, not a per-file size | capture: sha256:b2da48abcf8bfa8656e85ee120fae8dc1cd370512df7949548e2be0973dac405 | quote: - This gives you up to 100TB of Internxt Drive's award-winning post-quantum zero-knowledge encrypted cloud storage for life, with a unique, one-time payment.
  - [1] 2026-11-03: 100TB is the total storage of the plan | capture: sha256:b2da48abcf8bfa8656e85ee120fae8dc1cd370512df7949548e2be0973dac405 | quote: - This gives you up to 100TB of Internxt Drive's award-winning post-quantum zero-knowledge encrypted cloud storage for life, with a unique, one-time payment.
  - [1] 2026-11-03: codes are not stackable | capture: sha256:b2da48abcf8bfa8656e85ee120fae8dc1cd370512df7949548e2be0973dac405 | quote: - Codes are NOT stackable.
  - [1] 2026-11-03: 100TB is total storage | capture: sha256:b2da48abcf8bfa8656e85ee120fae8dc1cd370512df7949548e2be0973dac405 | quote: - This gives you up to 100TB of Internxt Drive's award-winning post-quantum zero-knowledge encrypted cloud storage for life, with a unique, one-time payment.
  - [1] 2026-11-03: 100TB is total storage, so there is no per-file byte cap on the listing | capture: sha256:b2da48abcf8bfa8656e85ee120fae8dc1cd370512df7949548e2be0973dac405 | quote: - This gives you up to 100TB of Internxt Drive's award-winning post-quantum zero-knowledge encrypted cloud storage for life, with a unique, one-time payment.
  - [4] 2026-11-03: sign-up needs a name and an email address, with no identity verification | capture: sha256:35ba783a0bc18310809ee71a4bef15fb0592b54c2060cd7dfcf1e5318a273e8d | quote: To sign up, simply enter a name and email address. No identity nor email verification is required to start using Internxt's services.
  - [4] 2026-11-03: the vendor's own FAQ says lifetime plans are stackable up to 100 TB on one account, which differs from the StackSocial code terms | capture: sha256:35ba783a0bc18310809ee71a4bef15fb0592b54c2060cd7dfcf1e5318a273e8d | quote: Yes, you can add up to 100 TB of storage to your Internxt lifetime membership. Internxt lifetime plans are stackable.
  - [1] 2026-11-03: the 100 TB allowance is sold for 974.97 USD; the free allowance is 1 GB | capture: sha256:098d9b4ad357da2e61da727d9888ead78f6fa515ca7fffb9172d40698690642a | quote: "priceCurrency":"USD","price":"974.97"
  - [1] 2026-11-03: CLI and WebDAV are excluded from the 100 TB listing | capture: sha256:b2da48abcf8bfa8656e85ee120fae8dc1cd370512df7949548e2be0973dac405 | quote: - It does not include other products or features, such as but not limited to Internxt Mail, Meet, CLI, WebDAV, Cleaner, Backups, Password-Protected File Sharing, Advanced Sharing, AI, File versioning, or Antivirus, which are sold separately by Internxt.
  - [4] 2026-11-04: the free membership gives 1 GB for life | capture: sha256:35ba783a0bc18310809ee71a4bef15fb0592b54c2060cd7dfcf1e5318a273e8d | quote: There, you will instantly get 1GB of free storage for life with a free Internxt membership.
  - [1] 2026-11-04: 100 TB is the total storage of the paid lifetime plan | capture: sha256:b2da48abcf8bfa8656e85ee120fae8dc1cd370512df7949548e2be0973dac405 | quote: - This gives you up to 100TB of Internxt Drive's award-winning post-quantum zero-knowledge encrypted cloud storage for life, with a unique, one-time payment.
  - [4] 2026-11-04: sign-up needs a name and an email address | capture: sha256:35ba783a0bc18310809ee71a4bef15fb0592b54c2060cd7dfcf1e5318a273e8d | quote: To sign up, simply enter a name and email address. No identity nor email verification is required to start using Internxt's services.
- sources:
  - [1] https://www.stacksocial.com/sales/internxt-cloud-storage-lifetime-subscription-100tb
  - [2] https://raw.githubusercontent.com/rclone/rclone/master/docs/content/internxt.md
  - [3] https://www.dealkeep.io/blog/lifetime-cloud-storage
  - [4] https://internxt.com/pricing
