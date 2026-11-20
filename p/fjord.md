# Fjord Commons

> fjord.sh | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fjord/ | JSON https://fshy.ajam.dev/api/v1/entity/fjord.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fjord Commons (Forgejo)

- `storage/fjord-commons` | qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:27.692Z (live) | stale on 2026-12-04
- url https://fjord.sh/commons
- disagrees on verdict: `storage/fjord-commons` says qualifies-with-caveat, `storage/fjord-commons-2` says fails-quota
- free tier: 5 GB per account; up to 25 repositories, public or private | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No metered egress stated for Commons; instance is 'One shared box on Hetzner ... behind Cloudflare'. Free tier described as permanent, no trial clock. | metered: yes
- identity: email | detail: the Fjord account registration form asks for an email address and a password (minimum 8 characters) and shows a Cloudflare Turnstile widget; no card or phone field is shown
- interface: rest, ssh, git
- limits note: 25 repos/account; 5 GB; LFS disabled; CI 2000 minutes/month pooled across ALL of Commons, 20 min/job; CI on public repos only.
- interface detail: rest
- tooling: Forgejo API, git over HTTPS and SSH, webhooks. Git LFS explicitly NOT enabled (removes one storage pool).
- composes with: Provides 5 GB storage per registered account, requiring independent Fjord user registrations for each allocation.
- reliability: Explicitly shared infrastructure on a single Hetzner box with nightly backups described as DR-only, not per-account restore. Community support only.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Repositories Up to 25 repositories ... Storage 5 GB per account; Git LFS is not enabled'; 'It is free because it is shared, and it stays free' (not a trial)
  - [1] 2026-10-21: 'One shared box on Hetzner ... behind Cloudflare', backups 'disaster recovery, not per-account restore'
  - [1] 2026-11-19: Commons still offers 5 GB per account and up to 25 repositories with LFS disabled | capture: sha256:cc5d988dbe91cf7dcc19d61e34baabb812f9d6fcdf93bd2d48e729d0dc43fd44 | quote: Repositories Up to 25 repositories, public or private Storage 5 GB per account; Git LFS is not enabled
  - [1] 2026-11-19: the free tier has no trial clock | capture: sha256:cc5d988dbe91cf7dcc19d61e34baabb812f9d6fcdf93bd2d48e729d0dc43fd44 | quote: No. There is no clock, no expiry date, and no point where Commons stops working unless you pay.
  - [2] 2026-11-19: the signup form requires an email address | capture: sha256:94f9857e4e3ca1c64e8de2eb27b17a5e9291020016adc355933fe8bf757a6355 | quote: <input id="email" type="email" name="email" autocomplete="username" value="" required autofocus/></div>
- sources:
  - [1] https://fjord.sh/commons
  - [2] https://fjord.sh/register

## fjord commons (hosted forgejo)

- `storage/fjord-commons-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:38.132Z (live) | stale on 2026-12-04
- url https://fjord.sh/commons
- disagrees on verdict: `storage/fjord-commons` says qualifies-with-caveat, `storage/fjord-commons-2` says fails-quota
- free tier: none reachable: 5 GB per account and 'Git LFS is not enabled' at all. Free and non-expiring, but the LFS layer is simply absent. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB per account and 'Git LFS is not enabled' at all. Free and non-expiring, but the LFS layer is simply absent.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 GB per account and 'Git LFS is not enabled' at all. Free and non-expiring, but the LFS layer is simply absent.
  - [1] 2026-11-19: the hosted Forgejo Commons page still states 5 GB per account with Git LFS disabled | capture: sha256:cc5d988dbe91cf7dcc19d61e34baabb812f9d6fcdf93bd2d48e729d0dc43fd44 | quote: Storage 5 GB per account; Git LFS is not enabled
  - [1] 2026-11-19: the Commons account is free with no expiry | capture: sha256:cc5d988dbe91cf7dcc19d61e34baabb812f9d6fcdf93bd2d48e729d0dc43fd44 | quote: No. There is no clock, no expiry date, and no point where Commons stops working unless you pay. It is free because it is shared, and it stays free.
- sources:
  - [1] https://fjord.sh/commons
