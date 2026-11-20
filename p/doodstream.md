# DoodStream

> doodstream.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/doodstream/ | JSON https://fshy.ajam.dev/api/v1/entity/doodstream.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DoodStream

- `storage/doodstream` | fails-quota | evidence inferred | binding retention-clamped | category media
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:22:27.191Z (live) | stale on 2026-12-05
- url https://doodstream.com
- free tier: Unlimited working storage and traffic on all plans, per the plans page | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Premium accounts upload up to 20 GB per file; the free-account per-file cap is unverified: not stated on the pages read | source: [1] | note: the premium plan lists 'Upload up to 20 GB per file'; no per-file cap for free accounts is stated on the homepage or the premium page
- retention: Inactive videos of free users are removed after 60 days; premium users' videos are never removed | days: 60 | source: [1] | note: homepage FAQ, question 'Do you remove inactive videos?'; the premium plan page lists 'Files never expire'
- egress: No stated cap; ad-monetised. Premium bandwidth sold to remove ads/logo. | metered: no
- identity: email
- interface: rest
- limits:
  - retention-clamped (binding): inactive videos of free users are removed after 60 days [1]
- limits note: Video hosting; the FAQ answers the question 'Do you remove inactive videos?' with removal after 60 days for free users and never for premium users. The premium plan lists 'Files never expire'.
- binding note: inactive videos of free users are removed after 60 days; premium users' videos are never removed
- interface detail: rest
- tooling: API exists (api key based) but is not documented on the pages reachable here; community uploaders (mirror-leech bots) integrate it.
- composes with: Free accounts x unlimited storage. Same video-only limitation as Streamtape.
- reliability: Byte fidelity lost to transcoding.
- notes: 'Unlimited Storage' (marketing claim on the homepage).
- evidence note: the retention period (60 days for free users) is stated on the homepage FAQ, read 2026-11-04; the premium per-file cap and the working storage and traffic statement are on the premium page
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'Unlimited Storage' (marketing claim on the homepage).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Unlimited Storage' feature bullet
  - [2] 2026-10-21: 'we may, but shall not be obligated to: (i) delete or deactivate your account ... (iii) remove and/or delete any of your User Submissions'
  - [1] 2026-10-21: probe: GET -> 200
  - [3] 2026-11-03: every plan, free included, lists unlimited working storage and traffic | capture: sha256:5b92aa9c787a1f86590e8e0cb78b399fe27a0408476fbead480245f4cc47af8d | quote: All plans include unlimited working storage and traffic.
  - [1] 2026-11-03: free users' videos are removed after 60 days; premium users' videos are never removed | capture: sha256:cbd0fd95e9d1fca496cd6255a68a47e884d75dcbf815e9597e6fe9bbe22c1714 | quote: Yes, for free users it will removed after 60 days and for premium users videos will never be removed.
  - [3] 2026-11-03: the premium account lists a 20 GB per-file upload cap | capture: sha256:5b92aa9c787a1f86590e8e0cb78b399fe27a0408476fbead480245f4cc47af8d | quote: Upload up to 20 GB per file
  - [1] 2026-11-03: the FAQ says there is no bandwidth limitation; premium bandwidth removes player ads | capture: sha256:cbd0fd95e9d1fca496cd6255a68a47e884d75dcbf815e9597e6fe9bbe22c1714 | quote: No, there is no bandwidth limitations.
  - [1] 2026-11-04: the FAQ question asks about inactive videos; the answer is 60 days for free users, never for premium users | capture: sha256:561890d98f6e9ec7b1242297b0a01e3361f9dc2241887fa009258cc08a1faba2 | quote: Do you remove inactive videos?
  - [1] 2026-11-04: free users' videos are removed after 60 days; premium users' videos are never removed | capture: sha256:cbd0fd95e9d1fca496cd6255a68a47e884d75dcbf815e9597e6fe9bbe22c1714 | quote: Yes, for free users it will removed after 60 days and for premium users videos will never be removed.
  - [3] 2026-11-04: the premium account lists a 20 GB per-file upload | capture: sha256:5b92aa9c787a1f86590e8e0cb78b399fe27a0408476fbead480245f4cc47af8d | quote: Upload up to 20 GB per file
  - [2] 2026-11-04: the terms permit deleting an account | capture: sha256:b2cda3b25736dfe388cb852ac6f7fd2bcbfa7e355c4582e9f21b05022eb74615 | quote: we may, but shall not be obligated to: (i) delete or deactivate your account and (ii) block your e-mail
- sources:
  - [1] https://doodstream.com/
  - [2] https://doodstream.com/tos
  - [3] https://doodstream.com/premium
