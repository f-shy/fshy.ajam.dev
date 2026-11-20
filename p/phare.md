# Phare

> phare.io | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/phare/ | JSON https://fshy.ajam.dev/api/v1/entity/phare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Phare

- `dev-services/phare` | qualifies-with-caveat | evidence documented | binding volume-quota | category uptime monitoring, incidents and status pages (hosted in the European Union) | tier Hobby
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://phare.io/pricing
- free tier: Hobby plan, free and with no credit card: 100,000 monitoring events a month with no additional usage, unlimited projects, organization users and public status pages with custom domains and SSL, and 10 AI incident summaries a month; no SMS or voice alerts and no single sign-on | unit: requests | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The unit is the monitoring event; how many monitors 100,000 events cover depends on the monitoring strategy, and the Scale plan row relates its included events to about 5 monitors. The vocabulary has no events term, so requests is the nearest. Hobby events cannot go past the allowance: it is marked No additional usage.
- per-object cap: not applicable: a monitor checks a target; nothing is stored per object
- retention: unverified: no retention period is stated on the pricing page
- egress: not applicable: an outbound checker; monitor data is read back through the API | metered: no | source: [2]
- identity: email | detail: The pricing page describes the Hobby plan as for people with no credit card; the sign-up form asks for an organization name, a work email address and a password with a confirmation, behind a not-a-robot check.
- interface: rest
- limits:
  - volume-quota (binding): 100,000 monitoring events per month with no additional usage [1]
  - volume-quota (binding): 10 AI incident summaries and postmortems per month [1]
- limits note: Hobby has no SMS or voice alerts and no single sign-on.
- binding note: The 100,000 monitoring events a month cap how many monitors can run at a short interval; the event allowance cannot be raised on Hobby.
- interface detail: An API for most tasks available in the control panel, with organization-scoped or project-scoped API keys created by an Owner or Admin and per-product scopes of no access, read-only or read-write.
- tooling: the web control panel and any HTTP client with an API key; outgoing webhooks to build SMS or voice alerts
- composes with: External monitoring with unlimited projects and alerts on 100,000 events a month, public status pages on custom domains with SSL, and webhooks to chain alerts into other services.
- reliability: no throttle, ban or data loss is stated on the pages read; what happens when the 100,000 events are used up is unverified: not stated on the pricing page beyond No additional usage
- notes: The Scale plan is EUR 5 a month plus usage, with additional events billed at EUR 0.00001 per unit.
- evidence note: Plan limits are quoted from the first-party pricing page, the API access from its documentation and the sign-up fields from the sign-up page. No account was opened.
- evidence:
  - [1] 2026-11-01: the Hobby plan is free and aimed at users with no credit card | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: ## Hobby Free For the hobbyists, bedroom startups and indiehackers with big dreams and no credit card.
  - [1] 2026-11-01: Hobby includes 100,000 monitoring events a month with no additional usage | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: Number of monitoring events you can use each month, usage depends on your monitoring strategy. | 100,000 No additional usage
  - [1] 2026-11-01: Hobby has 10 AI incident summaries a month | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: Number of AI incident summaries and postmortems you can generate each month. | 10 No additional usage
  - [1] 2026-11-01: Hobby has unlimited organization users | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: Number of users you can invite into your organization. | Unlimited | Unlimited
  - [1] 2026-11-01: Hobby has unlimited projects | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: Number of projects you can create in your organization. | Unlimited | Unlimited
  - [1] 2026-11-01: Hobby has unlimited public status pages with custom domains and SSL | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: Number of public status pages you can create in your organization, with custom domains and SSL certificates. | Unlimited | Unlimited
  - [1] 2026-11-01: Hobby has no SMS or voice alerts but outgoing webhooks can build them | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: Not included Build your own SMS or voice alert with outgoing webhooks
  - [1] 2026-11-01: Hobby has no single sign-on and team members log in with their own accounts | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: No single sign-on Team members log in with their own Phare account
  - [1] 2026-11-01: Scale bills additional events at .00001 EUR per unit and relates its included events to about 5 monitors | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: Included Additional events billed at .00001€ per unit only when used ~ 5 monitors
  - [1] 2026-11-01: the Scale plan costs 5 EUR a month plus additional usage | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: 5€/mo + additional usage
  - [1] 2026-11-01: the service is made and hosted in the European Union | capture: sha256:92a9cd9fe60d9dce442816f869bd523514da6b06cd8e6eddcad9f40be34fff94 | quote: Made and hosted in the European Union
  - [2] 2026-11-01: an API covers most tasks available in the control panel | capture: sha256:4f08fac9d10531c6bbe7acddb53c44428cefe08603c97e3522a3f8b63d2f91f1 | quote: This API lets you interact programmatically with the Phare platform, enabling integration and automation for most tasks available in the control panel.
  - [2] 2026-11-01: API keys are created in the control panel by an Owner or Admin | capture: sha256:4f08fac9d10531c6bbe7acddb53c44428cefe08603c97e3522a3f8b63d2f91f1 | quote: Only team members with the Owner or Admin role can create an API key in your organization.
  - [3] 2026-11-01: the sign-up form asks for an organization, a work email, a password and a confirmation behind a not-a-robot check | capture: sha256:22769d26a00b24a9398673edfdc0c3b3c443cef0897fe5a8c87c2cc68602d37b | quote: # Create your account Organization Work email Password Confirm password I'm not a robot
- sources:
  - [1] https://phare.io/pricing
  - [2] https://docs.phare.io/api-reference/introduction
  - [3] https://app.phare.io/register
