# Pulsetic

> pulsetic.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pulsetic/ | JSON https://fshy.ajam.dev/api/v1/entity/pulsetic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pulsetic

- `dev-services/pulsetic` | qualifies-with-caveat | evidence documented | binding volume-quota | category uptime monitoring and status pages with real user monitoring | tier Free
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-02T10:51:07.144Z (live) | stale on 2026-12-03
- url https://pulsetic.com/pricing
- free tier: Free plan: 10 monitors, heartbeats and domains in total at a 5-minute check interval from 3 regions, 3 months of uptime logs, 3 status pages, 1,000 real user monitoring page views a month, email alerts and 1 webhook per monitor, no API | unit: objects | metered on: object-count | read on: 2026-11-01 | source: [1] | note: The unit counted is the monitor, heartbeat or domain, 10 in total. The Free column also lists 1 webhook per monitor and a custom domain for status pages.
- per-object cap: not applicable: a monitor checks a target; nothing is stored per object
- retention: 3 months of historical uptime logs and 3 months of analytics on Free, with error logs kept 30 days | source: [1]
- egress: not applicable: an outbound checker; the Free plan has no API to read monitor data back | metered: no | source: [1]
- identity: email | detail: The sign-up form offers Google or SSO sign-in, or an email address and a password, behind a Google reCAPTCHA; no payment field appears on it. Whether a later step asks for a card or a phone number is unverified: behind a sign-up.
- interface: unknown
- limits:
  - volume-quota (binding): 10 monitors, heartbeats and domains in total [1]
  - request-rate: 5-minute check interval from 3 regions [1]
  - volume-quota (binding): 1,000 real user monitoring page views a month [1]
  - retention-clamped: 3 months of uptime logs and analytics, 30 days of error logs [1]
- limits note: Free has no API, MCP or n8n access, so monitors are created in the web dashboard, and no Slack, Microsoft Teams or Datadog alerts.
- binding note: The 10-monitor cap fills before the 3 status pages matter, and the missing API means every monitor is set up by hand in the dashboard.
- interface detail: The pricing page lists API, MCP and n8n access as not available on Free and available from the Solo plan, so the Free plan is reached through the web dashboard only; the interface vocabulary has no term for a browser-only service.
- tooling: the web dashboard, email alerts, one webhook per monitor and public status pages; no API on Free
- composes with: External uptime, SSL, port and keyword checks every 5 minutes from 3 regions on up to 10 endpoints of free-hosted services, with 3 public status pages on a custom domain and email alerts.
- reliability: no throttle, ban or data loss is stated on the pages read beyond the 3-month log and analytics retention and the 30-day error log retention
- notes: The first paid plan, Solo, adds API, MCP and n8n access, Slack alerts and 60-second checks.
- evidence note: Every limit is quoted from the first-party pricing page and the sign-up form from the sign-up page. No account was opened, so any step after the form is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: Free has 10 monitors, heartbeats and domains in total | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Monitors/Heartbeats/Domains: Free: 10; Solo: 10+; Team: 50+; Organization: 300+
  - [1] 2026-11-01: Free checks every 5 minutes | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Check Interval: Free: 5 Min.; Solo: 60 Sec.; Team: 30 Sec.; Organization: 30 Sec.
  - [1] 2026-11-01: Free checks from 3 regions | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Region Checks: Free: 3; Solo: 5; Team: 15; Organization: 15
  - [1] 2026-11-01: Free keeps 3 months of uptime logs | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Historical Uptime/Logs: Free: 3 Months; Solo: 1 Year; Team: 1 Year; Organization: 5 Years
  - [1] 2026-11-01: Free includes 1,000 real user monitoring page views a month | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Page Views / mo: Free: 1,000; Solo: 10,000+; Team: 100,000+; Organization: 200,000+
  - [1] 2026-11-01: Free keeps analytics 3 months | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Analytics Retention: Free: 3 Months; Solo: 1 Year; Team: 1 Year; Organization: 5 Years
  - [1] 2026-11-01: Free keeps error logs 30 days | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Error Log Retention: Free: 30 days; Solo: 90 days; Team: 6 months; Organization: 1 Year
  - [1] 2026-11-01: Free includes 3 status pages | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Status Pages: Free: 3; Solo: Unlimited; Team: Unlimited; Organization: Unlimited
  - [1] 2026-11-01: API, MCP and n8n access are not part of Free | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - API/MCP/N8N: Free: no; Solo: yes; Team: yes; Organization: yes
  - [1] 2026-11-01: Free has email alerts | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Email Alerts: Free: yes; Solo: yes; Team: yes; Organization: yes
  - [1] 2026-11-01: Free has no Slack, Microsoft Teams or Datadog alerts | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Slack, MS Teams, Datadog: Free: no; Solo: yes; Team: yes; Organization: yes
  - [1] 2026-11-01: Free has 1 webhook per monitor | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Webhooks (per monitor): Free: 1; Solo: 1; Team: 5; Organization: 10
  - [1] 2026-11-01: Free status pages can use a custom domain | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Custom Domain: Free: yes; Solo: yes; Team: yes; Organization: yes
  - [1] 2026-11-01: the vendor describes the free version as a limited-functionality plan that is often enough | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: Yes, we offer a free version of our service, with limited functionality. In many cases, the free version will be enough to monitor your website.
  - [2] 2026-11-01: the sign-up form offers Google or SSO or an email address and a password | capture: sha256:d953dc73239d51cedf48b52ddad8fc57f11897570c0cb3e097e3d347b809079f | quote: Sign up with Google Sign up with SSO OR Email Password
  - [2] 2026-11-01: the sign-up page is protected by Google reCAPTCHA | capture: sha256:d953dc73239d51cedf48b52ddad8fc57f11897570c0cb3e097e3d347b809079f | quote: This website is protected by Google reCAPTCHA.
  - [1] 2026-11-02: Free includes 1 webhook per monitor | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Webhooks (per monitor): Free: 1; Solo: 1; Team: 5; Organization: 10
  - [3] 2026-11-02: the vendor's own description of the free plan lists email and webhook alerts, 10 monitors and 3 status pages on a custom domain | capture: sha256:fcd4cb9be951ea8b0393d369f656b2eb5c520b022d919fcf8d5fcf8901bfde81 | quote: Pulsetic, on the other hand, gives you lots of functionality for free: 10 monitors, email and webhook alerts, SSL monitoring and 3 status pages on a custom domain you own.
  - [4] 2026-11-02: the monitor count of a plan is one combined total of monitors, heartbeats and domains | capture: sha256:b927197722011a7265bb61a7f5cbfb8c96cc2ee69d8cd854ef1672e67674e676 | quote: - Monitors: The combined total of your active monitors, heartbeats, and domains.
  - [1] 2026-11-02: Free allows 10 monitors, heartbeats and domains | capture: sha256:7e9cbe97cbc291424f516041d618670f4502672b28c33d08b65ddcfe252a183e | quote: - Monitors/Heartbeats/Domains: Free: 10; Solo: 10+; Team: 50+; Organization: 300+
- sources:
  - [1] https://pulsetic.com/pricing
  - [2] https://app.pulsetic.com/signup/
  - [3] https://pulsetic.com/pingdom-alternative/
  - [4] https://help.pulsetic.com/article/256-usage
