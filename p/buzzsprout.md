# buzzsprout

> buzzsprout.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/buzzsprout/ | JSON https://fshy.ajam.dev/api/v1/entity/buzzsprout.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## buzzsprout — free plan

- `storage/buzzsprout-free-plan` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:06.017Z (live) | stale on 2026-12-04
- url https://www.buzzsprout.com/help/231-what-is-included-in-the-free-plan
- free tier: none reachable: 2 hours of upload per month AND episodes are deleted from the feed after 90 days (with a further 90-day 'safety net' before permanent removal). It is a demo tier, not storage. Also… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: not-storage
  - dead_end.why: 2 hours of upload per month AND episodes are deleted from the feed after 90 days (with a further 90-day 'safety net' before permanent removal). It is a demo tier, not storage. Also…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 2 hours of upload per month AND episodes are deleted from the feed after 90 days (with a further 90-day 'safety net' before permanent removal). It is a demo tier, not storage. Also…
  - [2] 2026-10-21: cited as the basis of the rejection: 2 hours of upload per month AND episodes are deleted from the feed after 90 days (with a further 90-day 'safety net' before permanent removal). It is a demo tier, not storage. Also re-encode
  - [1] 2026-11-19: the first-party help page still states two hours of upload per cycle and 90-day hosting on the free plan | capture: sha256:7058ca94287007561ebed24a1c9db99cc9cd951467cd7be94a632f6b7263ebf5 | quote: On the free plan, you’ll be able to upload two hours of content each cycle. We’ll host any episodes you upload for 90 days.
  - [1] 2026-11-19: the first-party help page confirms a further 90-day safety net before permanent removal of expired episodes | capture: sha256:7058ca94287007561ebed24a1c9db99cc9cd951467cd7be94a632f6b7263ebf5 | quote: We'll keep them in a safety net for another 90 days before permanent removal.
- sources:
  - [1] https://www.buzzsprout.com/help/231-what-is-included-in-the-free-plan
  - [2] https://www.buzzsprout.com/help/163-audio-optimization
