# Hightail

> hightail.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hightail/ | JSON https://fshy.ajam.dev/api/v1/entity/hightail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hightail

- `debrid/hightail` | fails-quota | evidence documented | binding per-object-cap | category file sharing service (free Lite plan, paid Pro and Teams) | tier lite
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://www.hightail.com/pricing
- price USD 12 per month (Pro, billed annually), unlimited storage | parsed USD 12/mo
- free tier: Lite, free: upload files up to 100MB, 2GB storage, send file expiration 7 days. | unit: GB | metered on: stored-bytes | read on: 2026-11-03 | source: [1] | note: The page marks Lite 'Always free'.
- per-object cap: Upload files up to 100MB | bytes: 104857600 | source: [1] | note: bytes = 100 x 1024^2; Pro 25GB, Teams 50GB.
- retention: | Send file expiration | 7 Days | | days: 7 | source: [1] | note: Pro and Teams: configurable, no expiration.
- egress: No download allowance is printed. | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: Lite has a 'Sign up for Lite' button; the sign-up form fields were not read, so email is assumed and unverified.
- interface: unknown
- limits:
  - per-object-cap (binding): 100MB Lite, 25GB Pro, 50GB Teams [1]
  - volume-quota: 2GB storage on Lite, unlimited on Pro and Teams [1]
  - retention-clamped: 7 days on Lite [1]
- binding note: 100MB per file on the free plan is the first limit.
- interface detail: Web and desktop upload with sync from Dropbox, Google Drive and OneDrive; no public API listed on the pricing page.
- tooling: Browser as read.
- composes with: 100MB per file on the free plan is small; Pro raises the cap to 25GB with unlimited storage.
- reliability: The Pro price is billed annually.
- evidence note: Pricing page read on 2026-11-03. The sign-up form was not read.
- extras:
  - plans: Lite free; Pro $12/month billed annually; Teams $24/user/month billed annually
- evidence:
  - [1] 2026-11-03: the Lite plan caps a file at 100MB | capture: sha256:6ec46cecd6095de5c8f9bfd1f711762c54e791221aaae4c47d6a22b678893a76 | quote: Upload files up to 100MB
  - [1] 2026-11-03: Lite files expire after 7 days | capture: sha256:6ec46cecd6095de5c8f9bfd1f711762c54e791221aaae4c47d6a22b678893a76 | quote: | Send file expiration | 7 Days |
  - [1] 2026-11-03: Pro costs $12 a month billed annually | capture: sha256:6ec46cecd6095de5c8f9bfd1f711762c54e791221aaae4c47d6a22b678893a76 | quote: $12/month*
- sources:
  - [1] https://www.hightail.com/pricing
