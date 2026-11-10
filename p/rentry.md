# Rentry.co

> rentry.co | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rentry/ | JSON https://fshy.ajam.dev/api/v1/entity/rentry.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rentry.co

- `storage/rentry-co` | fails-quota | evidence reported | binding write-gated | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:15.278Z (live) | stale on 2026-11-18
- url https://rentry.co
- free tier: 200,000 characters per entry (hard, enforced at API), unlimited entries, no account required. Entries kept 'forever' unless they break rules. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Entries are kept forever unless they break the rules, in which case they might be deleted, or the owner deletes them. | source: [1] | note: not stated
- egress: free direct GET, no metering; behind Cloudflare so it is CDN-cacheable at the edge. | metered: no
- identity: anonymous
- interface: rest, cli
- limits:
  - request-rate: roughly 10 anonymous creations per minute per IP (429 status when exceeded) [2]
  - write-gated (binding): Application and stated in the 400 error, so silent truncation does not happen. Writes fail. [1]
- limits note: 200,000 chars per entry; custom URL 2-100 chars; edit_code required to modify; no per-account quota and no per-IP cap observed (8 rapid anonymous POSTs all returned 200); URL squatting reclaimed after 12 months idle.
- interface detail: rest
- tooling: Official Python client github.com/radude/rentry (593 stars) + pip package 'rentry'; single-file CLI with zero dependencies.
- composes with: Unlimited anonymous entries x 200,000 chars (~150 KB of base64 binary after the 4/3 encoder penalty). To reach 500 GB you would need ~3.5M entries, so this is a control-plane / manifest store, not a data tier. Unless an unlimited free identity source is added, and even then the operator's storage is the ceiling.
- reliability: Anonymous creation is limited per IP to roughly 10 per minute (429); the per-entry text ceiling is enforced by the application and a write above it fails with a 400. Bulk write volume at the creation limit is the untested risk.
- notes: the same as the free tier
- evidence note: pages captured 2026-11-03: https://github.com/radude/rentry, https://rentry.co/what, https://rentry.co/user-account/membership; the per-IP creation limit rests on a third-party client README, so the rung stays reported
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 200,000 characters per entry (hard, enforced at API), unlimited entries, no account required. Entries kept 'forever' unless they break rules.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '200000 characters for text field', 'Your entries will be kept forever'
  - [3] 2026-10-21: probe: POST with form fields url/edit_code/text -> {"status":"200","url":"https://rentry.co/n7f74b9t","edit_code":"..."}; page then contained the probe string
  - withheld 2026-10-21: probe: POST with 293,336 chars -> {"status": "400", "errors": "Ensure text field has at most 200000 characters (it has 293336)."}
  - withheld 2026-10-21: probe: 8 sequential anonymous creations -> 200 x8, no rate limit
  - [2] 2026-11-03: entries are created anonymously, limited per IP | capture: sha256:7d6b0c28d536e7c4db5cd27ed4f766198cdad3a22d27f7e2b65eb8186b1f1695 | quote: Anonymous creation is rate-limited per IP, roughly 10 per minute on rentry.co and configurable per instance.
  - [2] 2026-11-03: the documented per-IP creation limit is about 10 per minute | capture: sha256:7d6b0c28d536e7c4db5cd27ed4f766198cdad3a22d27f7e2b65eb8186b1f1695 | quote: Anonymous creation is rate-limited per IP, roughly 10 per minute on rentry.co and configurable per instance.
  - [2] 2026-11-03: the limit is stated in the API reference | capture: sha256:7d6b0c28d536e7c4db5cd27ed4f766198cdad3a22d27f7e2b65eb8186b1f1695 | quote: Anonymous creation is rate-limited per IP, roughly 10 per minute on rentry.co and configurable per instance.
  - [1] 2026-11-03: retention is unbounded unless the rules are broken | capture: sha256:301b14b44d59110df3e0d106814e3867ff9952f35274e138d6b67ed6a0772195 | quote: Your entries will be kept forever. Unless they break the rules, in which case they might get deleted.
  - [2] 2026-11-03: the creation limit is about 10 per minute per IP | capture: sha256:7d6b0c28d536e7c4db5cd27ed4f766198cdad3a22d27f7e2b65eb8186b1f1695 | quote: Anonymous creation is rate-limited per IP, roughly 10 per minute on rentry.co and configurable per instance.
  - [4] 2026-11-03: an optional account is created from an email address; the membership price is behind this sign-in | capture: sha256:0aa44b9024b1defdfa3ba6d65d7de251234e4f9d70ab75a1bf3fcb2a96af7d6d | quote: Enter your email to sign in to your existing account or create a new one.
  - [1] 2026-11-03: the per-entry limit is 200000 characters and entries are kept forever | capture: sha256:301b14b44d59110df3e0d106814e3867ff9952f35274e138d6b67ed6a0772195 | quote: 200000 characters for text field.
- sources:
  - [1] https://rentry.co/what
  - [2] https://github.com/radude/rentry
  - [3] https://rentry.co/api/new
  - [4] https://rentry.co/user-account/membership
