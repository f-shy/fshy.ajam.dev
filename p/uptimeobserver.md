# UptimeObserver

> uptimeobserver.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uptimeobserver/ | JSON https://fshy.ajam.dev/api/v1/entity/uptimeobserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UptimeObserver

- `dev-services/uptimeobserver` | qualifies-with-caveat | evidence documented | binding request-rate | category uptime, SSL, DNS, port and domain monitoring with status pages | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://uptimeobserver.com/pricing
- free tier: Free plan: 20 monitors at a 5-minute interval, 1 status page with a custom domain, HTTPS, SSL, domain name, DNS and port monitoring, email alerts to 1 recipient, Telegram, Pushover, Slack and Discord alerts and 2 webhook alerts | unit: objects | metered on: object-count | read on: 2026-11-01 | source: [1] | note: The unit counted is the monitor. The paid plans carry a 14-day free trial: Indie is EUR 5 a month for 50 monitors at 1-minute checks and Pro is EUR 20 a month for 200 monitors at 30-second checks.
- per-object cap: not applicable: a monitor checks a target; nothing is stored per object
- retention: unverified: no history retention period is stated on the pricing page
- egress: not applicable: an outbound checker; no export or API access is named on the pricing page | metered: no | source: [1]
- identity: email | detail: The register form asks for a first name, a last name, an email address and a password; the pricing page states no credit card term for the Free plan, whose button is Get Started where the paid plans say Start Free Trial. Whether a later step asks for a card or a phone number is unverified: behind a sign-up.
- interface: unknown
- limits:
  - volume-quota: 20 monitors on Free [1]
  - request-rate (binding): 5-minute monitoring interval on Free [1]
- limits note: Free has 1 status page, 1 email alert recipient and 2 webhook alerts.
- binding note: The 5-minute interval sets the detection delay of every monitor and binds before the 20-monitor cap for an app that needs faster detection.
- interface detail: The pricing page names no API for any plan, so the Free plan is reached through the web app and its alert channels; the interface vocabulary has no term for a browser-only service.
- tooling: the web app, public status pages and the alert channels
- composes with: External HTTPS, SSL, DNS and port checks every 5 minutes on up to 20 endpoints of free-hosted services, with Telegram, Slack, Discord or webhook alerts and one status page on a custom domain.
- reliability: no throttle, ban or data loss is stated on the pages read
- notes: The Free card lists status pages with custom domains.
- evidence note: Plan limits are quoted from the first-party pricing page and the sign-up fields from the register page. No account was opened, so the card term and later steps are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Free plan has 20 monitors at a 5-minute interval and 1 status page | capture: sha256:739fa8d453438391f02745c7ae533b0e087987a9d1d70d1e7e929fc1a20b9cc5 | quote: Perfect for getting started. - 20 Monitors - 5 min. monitoring interval - 1 Status Page
  - [1] 2026-11-01: the Free plan has 1 email recipient, Telegram, Pushover, Slack and Discord alerts, 2 webhook alerts and status pages with custom domains | capture: sha256:739fa8d453438391f02745c7ae533b0e087987a9d1d70d1e7e929fc1a20b9cc5 | quote: - 1 Email Alert Recipients - Telegram Alerts - Pushover Alerts - Slack Alerts - Discord Alerts - 2 Webhook Alerts - Status Pages with Custom Domains
  - [1] 2026-11-01: the Free plan covers HTTPS, SSL, domain name, DNS and port monitoring | capture: sha256:739fa8d453438391f02745c7ae533b0e087987a9d1d70d1e7e929fc1a20b9cc5 | quote: - HTTPS Monitoring - SSL Monitoring - Domain Name Monitoring - DNS Monitoring - Port Monitoring - Email Alerts
  - [1] 2026-11-01: the paid plans carry a 14-day free trial | capture: sha256:739fa8d453438391f02745c7ae533b0e087987a9d1d70d1e7e929fc1a20b9cc5 | quote: 14-day free trial. Cancel or change plans at any time.
  - [1] 2026-11-01: Indie costs EUR 5 a month for 50 monitors at 1-minute checks | capture: sha256:739fa8d453438391f02745c7ae533b0e087987a9d1d70d1e7e929fc1a20b9cc5 | quote: Most Popular 5€ /mo For indie makers and small teams. - 50 Monitors - 1 min. monitoring interval
  - [1] 2026-11-01: Pro costs EUR 20 a month for 200 monitors at 30-second checks | capture: sha256:739fa8d453438391f02745c7ae533b0e087987a9d1d70d1e7e929fc1a20b9cc5 | quote: 20€ /mo For growing teams that need more. - 200 Monitors - 30 sec. monitoring interval
  - [2] 2026-11-01: the register form asks for a first name, a last name, an email address and a password | capture: sha256:bceba14a4e49750b8be89b0ef3543c5461da6ddeb962574343b72be8f7a64fe7 | quote: First name is required Last name \* Last name is required Email \* Email is required Password \* Password is required
- sources:
  - [1] https://uptimeobserver.com/pricing
  - [2] https://app.uptimeobserver.com/auth/register/0
