# Aptabase

> aptabase.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aptabase/ | JSON https://fshy.ajam.dev/api/v1/entity/aptabase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aptabase

- `dev-services/aptabase` | qualifies-with-caveat | evidence documented | binding volume-quota | category analytics for mobile and desktop apps (SDKs, hosted) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://aptabase.com/pricing
- free tier: Free plan: 20,000 events per month with no credit card required; unlimited apps, EU or US data residency, built-in and live dashboards, session timeline and CSV export; there are no overage fees and past the limit analytics are paused until the start of the next month | unit: requests | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The unit is the event: every call to the SDK's track function counts as one, and nothing is tracked automatically. The vocabulary has no events term, so requests is the nearest. The next plan is USD 10 a month for 200,000 events.
- per-object cap: unverified: no per-event size is stated on the pages read
- retention: unverified: no retention period is stated on the pages read
- egress: Export to CSV is included on every plan; no export allowance or price beyond that is stated | metered: no | source: [1]
- identity: email | detail: The pricing page states no credit card is required for the free plan; the sign-up page offers GitHub or Google sign-in, or a name and an email address that receives a magic link, in the EU or the US region.
- interface: unknown
- limits:
  - volume-quota (binding): 20,000 events per month; past it analytics are paused until the start of the next month [1]
- binding note: The 20,000-event monthly cap is the only stated quota, and exceeding it pauses collection instead of billing.
- interface detail: Events are sent by SDKs for popular platforms and read in the built-in dashboard or exported to CSV; no REST read API is named on the pages read, and the interface vocabulary has no term for an SDK-only service.
- tooling: SDKs for popular platforms, the dashboard and CSV export
- composes with: Usage events from a desktop or mobile app, up to 20,000 a month, kept in the EU or the US region.
- reliability: past 20,000 events a month analytics are temporarily disabled until the start of the next month; an email warns before the limit
- notes: Paid plans start at USD 10 a month for 200,000 events; the free plan is the lowest step of the same event ladder.
- evidence note: The plan, the overage rule and the sign-up methods are quoted from first-party pages. No account was opened, so retention and any later sign-up step are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the free plan needs no credit card | capture: sha256:eae4c9a8322b5a41f363639d05c7ad6054537337d64967c89d1613935902c707 | quote: Start free and pay when you grow. No credit card required for the free plan.
  - [1] 2026-11-01: the free plan includes 20,000 events a month | capture: sha256:eae4c9a8322b5a41f363639d05c7ad6054537337d64967c89d1613935902c707 | quote: | 20,000 | Free |
  - [1] 2026-11-01: the next plan is USD 10 a month for 200,000 events | capture: sha256:eae4c9a8322b5a41f363639d05c7ad6054537337d64967c89d1613935902c707 | quote: | 200,000 | $10/month |
  - [1] 2026-11-01: there are no overage fees and analytics pause until the next month once the limit is exceeded | capture: sha256:eae4c9a8322b5a41f363639d05c7ad6054537337d64967c89d1613935902c707 | quote: There are no overage fees. We email you when you're close to your plan's monthly limit; if you exceed it, analytics are temporarily paused until the start of the next month.
  - [1] 2026-11-01: each call to the track function counts as one event and nothing is tracked automatically | capture: sha256:eae4c9a8322b5a41f363639d05c7ad6054537337d64967c89d1613935902c707 | quote: Every call to the SDK's track function counts as one event. Nothing is tracked automatically, so you decide exactly how many events your app sends.
  - [1] 2026-11-01: every plan includes unlimited apps, EU or US data residency, dashboards, CSV export and SDKs | capture: sha256:eae4c9a8322b5a41f363639d05c7ad6054537337d64967c89d1613935902c707 | quote: - Unlimited Apps - EU or US data residency - Built-in Dashboard - Live View Dashboard - Session Timeline - Export to CSV - SDKs for popular platforms
  - [2] 2026-11-01: the sign-up page offers GitHub, Google or a name and an email address with a magic link | capture: sha256:ba12d2c5d1ad6bfc22837219f2edcbd7d66ec25ecd6dc18a28e07e95b692bf41 | quote: Continue with GitHub Continue with Google OR Name Email Address Send magic link
- sources:
  - [1] https://aptabase.com/pricing
  - [2] https://eu.aptabase.com/auth/register
