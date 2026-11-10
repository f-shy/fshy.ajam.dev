# Bugfender

> bugfender.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bugfender/ | JSON https://fshy.ajam.dev/api/v1/entity/bugfender.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bugfender

- `dev-services/bugfender` | qualifies-with-caveat | evidence documented | binding retention-clamped | category remote logging for mobile and web apps (hosted) | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://bugfender.com/pricing/
- free tier: Free plan: 100K logs daily, 2,000 customer devices, unlimited user accounts and apps, 24 hours of retention, remote logging and native SDKs for mobile and web; no crash reporting, no API access and no webhooks | unit: mixed | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The allowance mixes a daily count of logs with a count of customer devices, so no single unit of the vocabulary fits. The Team plan keeps logs 7 days and adds crash reporting; the Pro plan keeps them 30 days and adds API access, webhooks and log archiving to an S3 bucket.
- per-object cap: unverified: no per-log-line size is stated on the pages read
- retention: 24 hours on Free, against 7 days on Team and 30 days on Pro | days: 1 | source: [1]
- egress: logs are read in the dashboard; API access, webhooks and log archiving to an S3 bucket are not part of Free | metered: no | source: [1]
- identity: email | detail: The sign-up page states no credit card is needed and asks for a name, an email address and a password, or GitHub sign-in. Whether a later step asks for a phone number is unverified: behind a sign-up.
- interface: unknown
- limits:
  - volume-quota: 100K logs daily and 2,000 customer devices on Free [1]
  - retention-clamped (binding): 24 hours of retention on Free [1]
- limits note: Free has no crash reporting, no API access, no webhooks and no log archiving to S3.
- binding note: Logs disappear after 24 hours, so the free tier is a one-day debugging window whatever the volume.
- interface detail: Logs are sent by native SDKs for mobile and web and read in the dashboard; the pricing table lists API access from the Pro plan, so the Free plan has no API, and the interface vocabulary has no term for an SDK-only service.
- tooling: native SDKs for mobile and web, and the web dashboard
- composes with: Remote logs from the devices of a free-hosted mobile or web app for 24 hours, up to 100K log lines a day, without a self-run log pipeline.
- reliability: logs older than 24 hours are deleted on the Free plan
- evidence note: Plan limits are quoted from the first-party pricing page and the sign-up fields from the sign-up page. No account was opened, so any later sign-up step is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: Free has 2,000 customer devices against unlimited on the paid plans | capture: sha256:e95b745f728ed007e82768c8759d2744c2cd6336b15f68ab9285b3f589828905 | quote: | Customer devices | 2,000 | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-01: Free allows 100K logs daily | capture: sha256:e95b745f728ed007e82768c8759d2744c2cd6336b15f68ab9285b3f589828905 | quote: | Logs | 100K daily | From 10M / month | From 10M / month | From 10M / month |
  - [1] 2026-11-01: retention is 24 hours on Free, 7 days on Team and 30 days on Pro | capture: sha256:e95b745f728ed007e82768c8759d2744c2cd6336b15f68ab9285b3f589828905 | quote: | Retention | 24 hours | 7 days | 30 days | Custom |
  - [1] 2026-11-01: Free has unlimited user accounts | capture: sha256:e95b745f728ed007e82768c8759d2744c2cd6336b15f68ab9285b3f589828905 | quote: | User accounts | Unlimited | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-01: Free has unlimited apps | capture: sha256:e95b745f728ed007e82768c8759d2744c2cd6336b15f68ab9285b3f589828905 | quote: | Apps | Unlimited | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-01: Free has remote logging and no crash reporting, which starts on the Team plan | capture: sha256:e95b745f728ed007e82768c8759d2744c2cd6336b15f68ab9285b3f589828905 | quote: | Remote logging | ✓ | ✓ | ✓ | ✓ | | Crash reporting | | ✓ | ✓ | ✓ |
  - [1] 2026-11-01: Free has a native SDK for mobile and web | capture: sha256:e95b745f728ed007e82768c8759d2744c2cd6336b15f68ab9285b3f589828905 | quote: | Native SDK for mobile and web | ✓ | ✓ | ✓ | ✓ |
  - [1] 2026-11-01: API access, webhooks and log archiving to S3 start on the Pro plan | capture: sha256:e95b745f728ed007e82768c8759d2744c2cd6336b15f68ab9285b3f589828905 | quote: | Log archiving to S3 bucket | | | ✓ | ✓ | | API access | | | ✓ | ✓ | | Webhooks | | | ✓ | ✓ |
  - [2] 2026-11-01: the free sign-up states no credit card is needed | capture: sha256:a3259383c20063f0e67bc61f8e72c78674aba56316975dcaa75e7f37835ab225 | quote: Create your free Bugfender account in seconds. No credit card needed.
  - [2] 2026-11-01: the sign-up form asks for a name, an email and a password, with GitHub sign-in | capture: sha256:a3259383c20063f0e67bc61f8e72c78674aba56316975dcaa75e7f37835ab225 | quote: Name Email Password show OR SIGN UP WITH github GitHub
- sources:
  - [1] https://bugfender.com/pricing/
  - [2] https://dashboard.bugfender.com/signup?plan=free
