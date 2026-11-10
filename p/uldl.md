# uldl.sh

> uldl.sh | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uldl/ | JSON https://fshy.ajam.dev/api/v1/entity/uldl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## uldl.sh

- `storage/uldl-sh` | fails-quota | evidence documented | binding volume-quota | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:45.963Z (live) | stale on 2026-12-05
- url https://uldl.sh
- price USD 500 per TB-month at the announced Pro plan (10GB for USD 5 per month, listed as Coming Soon) | parsed USD 500/TB-mo
- free tier: 250MB free storage, 4.5MB max file size, unlimited uploads per day; the Free plan is rate limited and keeps files for 365 days | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 4.5 MB max per file | bytes: 4500000 | source: [1] | note: not stated
- retention: Free plan: 365 day retention; the announced Pro plan (listed as Coming Soon): unlimited retention | source: [1] | note: not stated
- egress: free direct GET from uldl.sh; no metering stated. | metered: no
- identity: anonymous | detail: unverified: the docs state the access key is generated when you sign up; the sign-up form sits behind the dashboard login and was not seen
- interface: rest
- limits:
  - per-object-cap: 4.5MB per file [1]
  - volume-quota (binding): 250MB of storage on the Free plan [1]
  - retention-clamped: 365 days of retention on the Free plan [1]
- limits note: 4.5 MB per file; 250 MB per name; unlimited uploads/day.
- binding note: the Free plan holds 250MB of storage with a 4.5MB per-file cap and 365 day retention; the paid tier is announced at 10GB for $5 per month, listed as Coming Soon
- interface detail: rest
- tooling: curl -X POST https://uldl.sh/<name> -d @- ; MCP connector offered for agents. Versioning of files is supported.
- composes with: Unlimited distinct namespaces x 250 MB each. The namespace is free and unauthenticated, so it multiplies like a bucket-per-name. 500 GB would need 2,000 namespaces and 111,000 files at the 4.5 MB cap.
- reliability: Tiny per-file cap (4.5 MB) means the multiplier is the namespace count, not file size; namespace squatting is first-come and unauthenticated. New/small operator.
- notes: 250 MB free storage per name, 4.5 MB max per file, unlimited uploads/day. No account needed. The 'username' in the URL is claimed on first POST.
- evidence note: read 2026-11-03: https://uldl.sh/ (Free plan 250MB storage, 4.5MB max file size, 365 day retention; Pro 10GB Coming Soon) and https://uldl.sh/docs (access key generated at sign-up), both vendor pages; the sign-up form was not seen.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 250 MB free storage per name, 4.5 MB max per file, unlimited uploads/day. No account needed — the 'username' in the URL is claimed on first POST.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '4.5MB max file size', '∞ uploads/day', '250MB free storage'
  - [2] 2026-10-21: 'echo "hello world" | curl -X POST https://uldl.sh/yourname -d @-' returns https://uldl.sh/yourname/abc123
  - [1] 2026-11-03: the Free plan includes 250MB of storage; the page also states 4.5MB max file size, an infinity-sign uploads/day and 365 day retention | capture: sha256:1bae9c154eda7dcc75bfdecfd8a0cd59cb786ff61dd2c31ac796c1ea07193076 | quote: - 250MB storage
  - [1] 2026-11-03: the free storage figure is 250MB | capture: sha256:1bae9c154eda7dcc75bfdecfd8a0cd59cb786ff61dd2c31ac796c1ea07193076 | quote: 250MB
  - [1] 2026-11-03: the Free plan lists 365 day retention, 250MB storage and a 4.5MB max file size | capture: sha256:1bae9c154eda7dcc75bfdecfd8a0cd59cb786ff61dd2c31ac796c1ea07193076 | quote: - 365 day retention
  - [1] 2026-11-03: the announced Pro plan lists 10GB of storage at $5/month, marked Coming Soon | capture: sha256:1bae9c154eda7dcc75bfdecfd8a0cd59cb786ff61dd2c31ac796c1ea07193076 | quote: - 10GB storage
  - [2] 2026-11-03: an access key is generated at sign-up, so the earlier no-account claim is not on the current pages | capture: sha256:b99db108ad3f755ba26043c48c18646a1aa96711c611519180992fef60ce67d6 | quote: Your access key is a unique 24-character token generated when you sign up.
  - [1] 2026-11-03: the max file size is 4.5MB | capture: sha256:1bae9c154eda7dcc75bfdecfd8a0cd59cb786ff61dd2c31ac796c1ea07193076 | quote: 4.5MB
  - [1] 2026-11-03: the Free plan lists 250MB storage, 4.5MB max file size and 365 day retention; the Pro plan at $5/month lists 10GB storage and is marked Coming Soon | capture: sha256:1bae9c154eda7dcc75bfdecfd8a0cd59cb786ff61dd2c31ac796c1ea07193076 | quote: - 250MB storage
  - [1] 2026-11-04: the Free plan includes 250MB of storage | capture: sha256:1bae9c154eda7dcc75bfdecfd8a0cd59cb786ff61dd2c31ac796c1ea07193076 | quote: - 250MB storage
- sources:
  - [1] https://uldl.sh/
  - [2] https://uldl.sh/docs
