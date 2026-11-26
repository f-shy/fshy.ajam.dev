# Migadu

> migadu.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/migadu/ | JSON https://fshy.ajam.dev/api/v1/entity/migadu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Migadu

- `email/migadu` | paid-only | evidence documented | binding request-rate | category custom-domain email hosting | tier Micro
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:33:22.971Z (live) | stale on 2026-12-05
- url https://www.migadu.com/pricing/
- free tier: no free plan: Micro replaced the free plan and costs $19/year, billed yearly only; a time-limited free trial needs no card, its length unverified: behind a sign-up | unit: none | metered on: none | read on: 2026-10-31 | source: [1] | note: Micro: unlimited mailboxes and addresses per account, almost unlimited domains, 200 incoming and 20 outgoing messages per day, 5 GB of soft storage. Mini is $9/month or $90/year with 1000 in/day, 100 out/day and 30 GB. Limits are counted per account across all its domains and mailboxes.
- per-object cap: unverified: no maximum message or attachment size is stated on the captured pages
- retention: no hard storage quota: the 5 GB of Micro is soft and mail never bounces for full storage; an account over quota for seven days is blocked and, uncleared, purged after 30 days | source: [2]
- egress: not applicable: a mailbox; outbound mail is counted in messages, 20 per day on Micro with a 25% tolerance before sends are rejected | metered: yes | free allowance: 20 outgoing messages per day on Micro | source: [1]
- identity: email | detail: signup asks for a full name and an existing email address that receives a confirmation link, with an optional organization name; no card for the trial. The paid plan is paid by card through Stripe, by a PayPal prepayment to the account balance, or in Bitcoin arranged through support. Domains on free TLDs are refused, so a paid domain is needed.
- interface: unknown, rest
- limits:
  - request-rate (binding): 20 outgoing messages per day on Micro, per account, with up to 25% tolerance before sends are rejected [1]
  - request-rate (binding): 200 incoming messages per day on Micro, per account; past the 25% tolerance incoming mail is deferred to the next day [1]
  - volume-quota: 5 GB of soft storage on Micro, per account [1]
- binding note: 20 outgoing messages per day is the first ceiling on Micro; storage is soft and mailboxes and addresses are unlimited.
- interface detail: IMAP at imap.migadu.com (993, TLS), POP at pop.migadu.com (995, TLS) and SMTP at smtp.migadu.com (465, TLS; port 587 also answers); CalDAV and CardDAV; an administration REST API in early beta at https://api.migadu.com/v1/ with HTTP Basic authentication by account email and API key
- endpoint: part of interface detail
- tooling: any IMAP, POP or SMTP client; IMAPSync for migration per the vendor guides; the beta REST API manages domains and mailboxes
- composes with: a flat-priced account with unlimited mailboxes and addresses across many domains; 20 outgoing messages per day bind first on Micro, so it suits receiving on many domains more than sending.
- reliability: a trial account can be limited or ended without notice; an account over quota for seven days is blocked and purged 30 days later
- notes: No free custom-domain mailbox: the cheapest plan is Micro at $19/year, with unlimited mailboxes but 20 outgoing messages per day. The trial needs only an email address. Pricing is per account, not per mailbox.
- evidence note: plans and quotas read from the vendor pages; imap.migadu.com:993 accepted a TCP connection and smtp.migadu.com:587 answered with an ESMTP banner; no login or send was made
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-31: the yearly prices are Maxi $990, Standard $290, Mini $90 and Micro $19 | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: | or$990/year | or$290/year | or$90/year | $19/year |
  - [1] 2026-10-31: Micro has no monthly price; Mini is $9 per month | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: | $99/month | $29/month | $9/month | Not available monthly. |
  - [1] 2026-10-31: Micro accepts 200 incoming messages per day | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: | 10.000 in/day | 3000 in/day | 1000 in/day | 200 in/day |
  - [1] 2026-10-31: Micro sends 20 outgoing messages per day | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: | 2000 out/day | 500 out/day | 100 out/day | 20 out/day |
  - [1] 2026-10-31: Micro includes 5 GB of storage, marked as a soft limit | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: | 500 GB ++ | 100 GB ++ | 30 GB ++ | 5 GB ++ |
  - [1] 2026-10-31: one account holds unlimited mailboxes and addresses at a flat price | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: The plan prices are flat, per Migadu account. An account may have unlimited mailboxes and addresses.
  - [1] 2026-10-31: the free plan is gone and Micro replaced it | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: We have added a new plan, Micro, that is accessible to users in even most undeveloped countries. This plan replaces the free plan.
  - [1] 2026-10-31: Micro enforces no domain count | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: There is no enforced restriction of domains number on the Micro plan.
  - [1] 2026-10-31: outgoing mail past 125% of the plan limit is rejected | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: When reaching outgoing messages limits, we will warn you and allow for some tolerance of up to 25% over the plan limit. After the tolerance we will start rejecting outgoing messages.
  - [1] 2026-10-31: the storage figures are soft limits | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: These storage limits are “soft” and can be crossed without any repercussion.
  - [1] 2026-10-31: mail does not bounce for full storage | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: There are no hard storage quotas. Mails will never bounce back because of full storage regardless of your plan.
  - [1] 2026-10-31: payments run through Stripe or PayPal | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: All processing is done via either Stripe.com or PayPal.com.
  - [1] 2026-10-31: PayPal works as a prepayment to the account balance | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: We do not offer subscriptions via PayPal. However, you can prepay your account using PayPal.
  - [1] 2026-10-31: Bitcoin payment is arranged through support | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: However, if this is your preferred payment method, you can reach out to support and we will give you our wallet address.
  - [3] 2026-10-30: signup needs an existing email address for a confirmation link | capture: sha256:5a01965f042b5895d659b1c78e85764966db367c7004146a6e4e644bfe38a969 | quote: An existing, valid email address is needed to send you a confirmation link.
  - [3] 2026-10-30: the trial needs no card | capture: sha256:5a01965f042b5895d659b1c78e85764966db367c7004146a6e4e644bfe38a969 | quote: To use our basic services you need no credit card. Trying out is free and risk free.
  - [2] 2026-10-30: the free trial is time-limited | capture: sha256:a6f98e6694268c3fb66452e5e2ba7fee56a25173b51078f08f1c7289a09ea666 | quote: We offer a limited, free trial of our services with a time limitation.
  - [2] 2026-10-30: seven days over quota blocks the account | capture: sha256:a6f98e6694268c3fb66452e5e2ba7fee56a25173b51078f08f1c7289a09ea666 | quote: If an account is continuously over quota for seven days, the account will be blocked and if applicable, downgraded forcefully.
  - [2] 2026-10-30: a blocked account is purged after 30 days | capture: sha256:a6f98e6694268c3fb66452e5e2ba7fee56a25173b51078f08f1c7289a09ea666 | quote: Uncleared, blocked accounts will be purged after 30 days regardless of the previous plan.
  - [2] 2026-10-30: a trial can be limited or ended without notice | capture: sha256:a6f98e6694268c3fb66452e5e2ba7fee56a25173b51078f08f1c7289a09ea666 | quote: We may limit or terminate an ongoing trial account at our sole discretion without any previous announcement.
  - [4] 2026-10-30: domains on free TLDs are refused | capture: sha256:cc410c2f3070ccaa5bc583893edbd69650b7526ed87243e27a6577d203b088e0 | quote: We refuse hosting email for free domain names as they are by majority involved in fraud, spamming and phishing.
  - [4] 2026-10-30: basic CalDAV and CardDAV are offered | capture: sha256:cc410c2f3070ccaa5bc583893edbd69650b7526ed87243e27a6577d203b088e0 | quote: We make the basic CalDAV and CarDAV services available, but they are not our focus.
  - [5] 2026-10-30: the vendor guides cover migration with IMAPSync | capture: sha256:d5410ea4b6395f80e05eff450d6493a3337681f8c35c54f56109ee8bb0e803ab | quote: Migrating email data using IMAPSync
  - [5] 2026-10-30: IMAP is served at imap.migadu.com on port 993 over TLS | capture: sha256:d5410ea4b6395f80e05eff450d6493a3337681f8c35c54f56109ee8bb0e803ab | quote: | IMAP | imap.migadu.com | 993 | TLS | Plain password |
  - [5] 2026-10-30: SMTP submission is at smtp.migadu.com on port 465 over TLS | capture: sha256:d5410ea4b6395f80e05eff450d6493a3337681f8c35c54f56109ee8bb0e803ab | quote: | SMTP | smtp.migadu.com | 465 | TLS | Plain password |
  - [5] 2026-10-30: POP is served at pop.migadu.com on port 995 over TLS | capture: sha256:d5410ea4b6395f80e05eff450d6493a3337681f8c35c54f56109ee8bb0e803ab | quote: | POP | pop.migadu.com | 995 | TLS | Plain password |
  - [6] 2026-10-30: an administration API exists and is in early beta | capture: sha256:6f78dd6a03d2f5e9b4da6d4e4fdac472c06ee6de4a388ac445c2f4ceba8224a7 | quote: Migadu provides a simple API intended to integrate with other systems. The API is still in early beta and not all functionalities are exposed.
  - [6] 2026-10-30: the API authenticates with the account email and an API key | capture: sha256:6f78dd6a03d2f5e9b4da6d4e4fdac472c06ee6de4a388ac445c2f4ceba8224a7 | quote: The API uses HTTP Basic authentication over https. Username is the email address of the Migadu account and the password is the API key.
  - probe:smtp.migadu.com:587 2026-10-30: smtp.migadu.com:587 answered with an ESMTP banner | capture: sha256:2b51a200ecfb63ef65918b4edea3cc7e6444b165ba19023cc4554ac1776fdc76 | quote: 220 mta10.migadu.com ESMTP Service Ready
  - probe:imap.migadu.com:993 2026-10-30: imap.migadu.com:993 accepted a TCP connection | capture: sha256:2b51a200ecfb63ef65918b4edea3cc7e6444b165ba19023cc4554ac1776fdc76 | quote: "host": "imap.migadu.com", "port": 993, "ok": true
  - [1] 2026-11-04: Micro is still $19/year, the cheapest plan | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: | or$990/year | or$290/year | or$90/year | $19/year |
  - [1] 2026-11-04: Micro still sends 20 outgoing messages per day | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: | 2000 out/day | 500 out/day | 100 out/day | 20 out/day |
  - [1] 2026-11-04: Micro still includes 5 GB of soft storage | capture: sha256:2783016cfc2cd58d10a82c26d9e2e39cf0e3ce5b447d38c950dafbffff76a44c | quote: | 500 GB ++ | 100 GB ++ | 30 GB ++ | 5 GB ++ |
  - probe:imap.migadu.com:993 2026-11-04: imap.migadu.com:993 accepted a TCP connection on 2026-11-04 | capture: sha256:ae60b7236230281665fed847576d5a23ed6c4945b85373ef973e827bb65e5b47 | quote: "port": 993
- sources:
  - [1] https://www.migadu.com/pricing/
  - [2] https://www.migadu.com/terms/
  - [3] https://admin.migadu.com/public/signup
  - [4] https://www.migadu.com/procon/
  - [5] https://www.migadu.com/guides/
  - [6] https://www.migadu.com/api/
