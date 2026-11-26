# shutterfly

> shutterfly.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shutterfly/ | JSON https://fshy.ajam.dev/api/v1/entity/shutterfly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## shutterfly

- `storage/shutterfly` | paid-only | evidence documented | binding retention-clamped | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-04T01:24:40.824Z (live) | stale on 2026-12-05
- url https://www.shutterfly.com/alp/photo-storage/
- free tier: unlimited photo storage for active customers; the account stays active with one purchase at least once every 18 months | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: photos are stored while the account is active; one purchase at least once every 18 months keeps it active | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: a purchase at least once every 18 months keeps the account active; sign-up fields: unverified: behind a sign-up
- interface: unknown
- limits:
  - retention-clamped (binding): unlimited photo storage only while the account is active: one purchase at least once every 18 months [1]
- binding note: photo storage is unlimited for active customers and the account stays active with one purchase at least once every 18 months
- interface detail: not documented
- tooling: upload from a desktop computer, a smartphone or a Facebook account; a public API, WebDAV or rclone backend is not documented on the vendor storage page
- composes with: not recorded
- reliability: unlimited photo storage is a benefit of active customers; one purchase at least once every 18 months keeps the account active
- notes: unlimited photo storage for active customers; one purchase at least once every 18 months keeps the account active
- evidence note: documented from the vendor page captured on 2026-11-03 (https://www.shutterfly.com/alp/photo-storage/): unlimited photo storage is a benefit of active customers, the account stays active with one purchase at least once every 18 months, and uploads come from a desktop computer, a smartphone or a Facebook account; the sign-up fields stay unverified behind a sign-up
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'Unlimited' photo storage, but it is conditioned on a purchase at least once every 18 months and is web/app-only with no API, WebDAV or rclone backend — fails both the free filter and the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Unlimited' photo storage, but it is conditioned on a purchase at least once every 18 months and is web/app-only with no API, WebDAV or rclone backend — fails both the free filter and the…
  - [1] 2026-11-03: unlimited photo storage requires one purchase at least once every 18 months | capture: sha256:10a0409fd6007044859eb7e1e9cf30a6312db5847520f4532a92b067141a1740 | quote: Simply make one purchase at least once every 18 months to keep your account active and enjoy the benefits of unlimited photo storage with Shutterfly.
  - [1] 2026-11-03: upload sources are a desktop computer, a smartphone or a Facebook account | capture: sha256:10a0409fd6007044859eb7e1e9cf30a6312db5847520f4532a92b067141a1740 | quote: Use your desktop computer, smartphone, or even your Facebook account to upload from and store your photos online with whatever option works best for you.
  - [1] 2026-11-03: unlimited photo storage is a benefit of active customers | capture: sha256:10a0409fd6007044859eb7e1e9cf30a6312db5847520f4532a92b067141a1740 | quote: Shutterfly offers unlimited, photo storage as a benefit to our active customers.
- sources:
  - [1] https://www.shutterfly.com/alp/photo-storage/
