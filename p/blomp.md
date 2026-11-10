# Blomp

> blomp.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blomp/ | JSON https://fshy.ajam.dev/api/v1/entity/blomp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blomp (AIN/Blomp Cloud Storage)

- `storage/blomp` | qualifies | evidence reported | binding per-object-cap | category object-storage (OpenStack Swift) + consumer drive
- needs card no, phone no, ID no, institution no | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.blomp.com/
- price $1.00/TB/mo at 10 TB ($9.99) and at 100 TB ($99.99) — the flat $1/TB/mo floor makes it scale linearly, unlike promo pricing; $1.50/TB/mo at 2 TB ($2.99); $1.98/TB/mo at 500 GB ($11.88/yr) | parsed USD 1/TB-mo
- free tier: 40 GB free on signup, advertised and confirmed as 'Get Up to 400 GB for Free'. +40 GB per friend who joins and stays active, i.e. 40 GB x 10 referrals = 400 GB. Referral ceiling 400 GB is a hard stop on a single account; past that you buy (500 GB $11.88/yr, 2 TB $2.99/mo, 10 TB $9.99/mo). | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object: 5 GB | bytes: 5000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No transfer fees. Pricing page states 'Transfer fees: None' for 500 GB and for the 100/250/500 TB tiers ('Nu-uh!', 'Not gonna happen', 'Don't even think about it'). No egress meter documented anywhere on site. | metered: no
- identity: email | detail: email
- interface: rclone
- limits:
  - write-gated: invited account must log in at least once a year or the granter loses the 40 GB [1]
  - per-object-cap (binding): per-object: 5 GB [1]
- limits note: Per-object: 5 GB+ uploads fail through rclone with 'Operation Forbidden' or 'Too Large Object' unless chunk_size is set correctly. CyberDuck works because it segments at 1 GB (forum.rclone.org/t/blomp-unable-to-upload-5gb-files/42498, 2023-10-24, unresolved in-thread). Referral space is retention-clamped: invited account must log in at least once a year or the granter loses the 40 GB.
- interface detail: swift
- tooling: Upstream rclone backend. rclone's own source describes the swift backend as 'OpenStack Swift (Rackspace Cloud Files, Blomp Cloud Storage, Memset Memstore, OVH)' — Blomp is named inside rclone's registration string, i.e. first-class, not a fork. Also works with CyberDuck (segments large files at 1 GB). Auth: auth=https://authenticate.ain.net, auth_version=2, tenant=storage, user=<email>. Container name <user@example.com>. A purpose-built third-party doc site exists (blompuser.github.io/blomp-cloud-storage-docs) recommending swift+chunker+crypt+compress stacking.
- composes with: The referral ladder is the point: 40 GB per self-invited account x unlimited accounts. Nodeloc's thread documents the operator doing exactly this ('换个邮箱和IP，就又能增加40G，以此类推，可以一直加到400G'), 19 posts, several confirming it works and one (post 18) warning that invited users must log in annually or the space is reclaimed. Beyond that, rclone chunker + crypt + 40 GB shards turns a 20 TB archive into ~40 TB of chunks spread over ~100 accounts.
- reliability: Two independent red flags: a nodeloc poster notes Blomp 'literally copied pCloud's marketing copy' and later changed it; the referral model means capacity is revoked silently on annual-login failure. The Swift 5 GB boundary is real and has been open since at least Oct 2023.
- notes: the same as the free tier
- evidence note: Re-read 2026-10-22: the page answers and the claim holds; the rung is unchanged because the read establishes the page, not the enforcement.
- extras:
  - price_verbatim: $1.00/TB/mo at 10 TB ($9.99) and at 100 TB ($99.99) — the flat $1/TB/mo floor makes it scale linearly, unlike promo pricing; $1.50/TB/mo at 2 TB ($2.99); $1.98/TB/mo at 500 GB ($11.88/yr)
  - superseded_evidence[0].url: https://www.nodeloc.com/t/topic/75952
  - superseded_evidence[0].date: 2026-01-23
  - superseded_evidence[0].proved: self-referral to 400 GB, email+IP change required, annual-login reclamation (post 18), thread dated 2026-01-23
  - superseded_evidence_note: Rows that are older than the topic's 180-day evidence window. They are kept as the historically read statement and are not evidence for the current claim; the current claim rests on the 2026-10-22 re-read in evidence[]. Nothing was deleted.
- evidence:
  - [1] 2026-10-21: '40 – 400 GB / Free / 40 GB of Storage / Up to 400 GB / Add 40GB for every friend who joins and stays active'; paid tiers 500 GB $11.88/Year, 2 TB $2.99/Month, 10 TB $9.99/Month
  - [2] 2026-10-21: rclone comparison table: 500 GB $0.99/mo, 100,000 GB $99.99/mo, 250,000 GB $249.99/mo, 500,000 GB $499.99/mo, 'Transfer fees: None' on every row, 'As low as $0.95 per TB/month', 'Three Availability Zones – three copies'
  - [3] 2026-10-21: Swift backend description explicitly names 'Blomp Cloud Storage' among commercial implementations
  - [4] 2026-10-21: registration string 'OpenStack Swift (Rackspace Cloud Files, Blomp Cloud Storage, Memset Memstore, OVH)'
  - [5] 2026-10-21: working rclone.conf for Blomp, posted 2026-04-25
  - [6] 2026-10-21: PROBE — HTTP/1.1 200, 341 bytes, x-openstack-request-id present (live Keystone)
  - [7] 2026-10-21: PROBE POST with bogus creds — 401, 114 bytes, {"error":{"code":401,"title":"Unauthorized"}} (a real auth gate, not a 200-with-error-body)
  - [2] 2026-10-22: re-read 2026-10-22 (HTTP 200, 1,682 B): the page answers and carries the Blomp plan ladder
- sources:
  - [1] https://www.blomp.com/
  - [2] https://www.blomp.com/cloud-storage
  - [3] https://rclone.org/swift/
  - [4] https://github.com/rclone/rclone/blob/master/backend/swift/swift.go
  - [5] https://support.blomp.com/viewtopic.php?t=4001
  - [6] https://authenticate.ain.net/
  - [7] https://authenticate.ain.net/v2.0/tokens
