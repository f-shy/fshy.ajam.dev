# Zoho

> zoho.com | Email, Compute, Storage; 7 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zoho/ | JSON https://fshy.ajam.dev/api/v1/entity/zoho.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZeptoMail (Zoho)

- `email/zeptomail` | qualifies-with-caveat | evidence documented | binding write-gated | category transactional sender
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://www.zoho.com/zeptomail/pricing.html
- free tier: 1 free credit worth 10,000 emails, valid 6 months; 100/day until the account is validated | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: credits expire 6 months after purchase and do not refill | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: email | detail: an account and a validated sending domain
- interface: rest
- limits:
  - write-gated (binding): the 100/day ceiling lifts only after Zoho validates the account [2]
  - request-rate: 10,000 emails in total from the single free credit [1]
- binding note: account validation gates the 100/day ceiling, and then the credit is finite.
- interface detail: the ZeptoMail API and SMTP relay
- tooling: curl, any SMTP client
- composes with: 10,000 emails once, not a rate; it composes with a domain and does not compose with a schedule.
- reliability: the credit is one-time; there is no recurring monthly allowance
- extras:
  - stale_after_days: 90
- evidence:
  - [2] 2026-10-22: the announcement of the free credit and the 100/day pre-validation cap
  - [1] 2026-10-22: the pricing page now redirects to a CPaaS credit model; the credit framing holds
- sources:
  - [1] https://www.zoho.com/zeptomail/pricing.html
  - [2] https://www.zoho.com/blog/cpaas/announcing-quick-transition.html

## Zoho Catalyst

- `compute/zoho-catalyst` | qualifies-with-caveat | evidence documented | binding request-rate | category serverless runtime
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:35.596Z (live) | stale on 2026-12-05
- url https://catalyst.zoho.com/free-tier/
- free tier: A monthly allowance that renews forever: '25,000 GB-seconds' of Function execution, '900 GB-minutes' of AppSail container runtime, '2 GB-days' of Data Store storage, '1,000,000' LLM input tokens and '500,000' LLM output tokens through QuickML, '1,800 CPU-seconds' of model training, '100,000' API Gateway requests and '300,000' Web Client Hosting requests. The page says: 'your free tier usage limits will be renewed every month forever'. Signing up also gives 'USD 250 in credits' as 'additional runway for 6 months'. | unit: tokens | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-monthly
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - request-rate (binding): The container lane is the real ceiling: 900 GB-minutes a month is 15 GB-hours, so one always-on 1 GiB AppSail container runs about 15 hours a month before the free tier is spent; the per-request counters (1,000 Cache GET, 1,000 queries) bind long before any byte quota does. [1]
- limits note: The container lane is the real ceiling: 900 GB-minutes a month is 15 GB-hours, so one always-on 1 GiB AppSail container runs about 15 hours a month before the free tier is spent; the per-request counters (1,000 Cache GET, 1,000 queries) bind long before any byte quota does.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The perpetual function allowance plus the 6-month USD 250 wallet is the useful pair: the credits can carry a burst build while the monthly free tier keeps a scheduled job alive after the credits end, and QuickML's 1M input tokens a month is a second, separate inference lane that survives the credit expiry.
- reliability: no reliability event recorded
- notes: India's strongest reachable free tier in verification because the door is a Zoho account rather than an Aadhaar or a GST number, and nothing on the free-tier page asks for a card. The catch is arithmetic, not policy: GB-minute and GB-second billing means a 512 MiB container gets twice the wall-clock hours of a 1 GiB one, and the free tier is spent by concurrency, not by month. Not probed: whether an Indian or non-Indian signup is treated differently, and whether the pay-as-you-go model needs a card on file. Both would need a signup.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: perpetual-monthly
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the pricing table row by row: 'Functions | Function execution | $0.000016 / GB-second | 25,000 GB-seconds', 'AppSail | Container runtime | $0.0013 / GB-minute | 900 GB-minutes', 'QuickML | LLM input tokens | $0.20 / million tokens | 1,000,000 tokens', 'Model training: CPU | $0.0004 / vCPU-second | 1,800 CPU-seconds', quoted
  - [1] 2026-10-22: the page description reads 'With a free tier that renews every month and $250 in credits to explore for your first six months'; the body reads 'your free tier usage limits will be renewed every month forever', quoted
  - [2] 2026-10-22: 'the free tier allowance is only available with the pay-as-you-go pricing model', the allowance is account-wide rather than per project, and 'The free tier allowance is refreshed monthly, and is not just a one-time benefit', quoted
  - [3] 2026-10-22: 'Catalyst offers 25k GB-seconds of Serverless Function requests, 2 GB storage in the Data Store, 1000 GET requests in Cache', quoted, matching the pricing table
  - [2] 2026-11-04: Catalyst documents a REST API beside its CLI and SDKs | capture: sha256:2821bce64f6304db782df9079e188885fd908b409b290d85aa838bfd44623b1b | quote: [REST API](https://docs.catalyst.zoho.com/en/api/introduction/overview-and-prerequisites/#OverviewandPrerequisites)
- sources:
  - [1] https://catalyst.zoho.com/free-tier/
  - [2] https://docs.catalyst.zoho.com/en/deployment-and-billing/billing/free-tier/
  - [3] https://docs.catalyst.zoho.com/en/deployment-and-billing/llms-full.md

## Zoho Mail

- `email/zoho-mail` | qualifies-with-caveat | evidence documented | binding retention-clamped | category mailbox
- needs card no, phone no, ID no, institution no | verified 2026-11-02T10:00:29.727Z (live) | stale on 2026-12-03
- url https://www.zoho.com/mail/zohomail-pricing.html
- free tier: 5 users, 5 GB each, 1 custom domain, 25 MB attachment limit | unit: GB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 25 MB attachment limit, 5 GB per mailbox | bytes: 26214400 | source: [1]
- retention: 5 GB per mailbox | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: an account with the domain's MX records pointed at Zoho
- interface: unknown
- limits:
  - retention-clamped (binding): no IMAP, POP or ActiveSync on the free edition, so no programmatic mailbox read [1]
  - per-object-cap: 25 MB per attachment [1]
- limits note: the 5 GB is a mailbox storage volume and not an object size, so no kind in the six-value vocabulary names it. The 25 MB attachment is a per-object cap and stays in limits. What binds the verdict is the removal of IMAP, POP and ActiveSync, which is recorded as retention-clamped because the server withholds the data rather than the bytes
- binding note: a removed feature, not a capped volume; the hard filter is programmatic access.
- interface detail: webmail and the mobile app only on the free edition; no IMAP, POP or ActiveSync
- tooling: none: no IMAP or POP on the free edition
- composes with: a real mailbox with a custom domain for five users, and it breaks the obvious chain because the free edition cannot be read over IMAP.
- reliability: the free edition is region-limited; the page title reads 'Free for 5 Users in select regions'
- notes: This kills the obvious 'free mailbox plus IMAP fetch' chain, which is why it is recorded rather than skipped.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: the free edition is 5 users at 5 GB each with 1 custom domain, and the protocol support table excludes IMAP, POP and ActiveSync from the free edition
  - [1] 2026-11-02: the Mail Free plan is listed as email hosting for one domain, up to 5 users and 5 GB per user with no IMAP, POP or Active Sync, and the page names no WebDAV or other protocol, so no interface term fits its webmail and app access | capture: sha256:d03c095d97ede4a458a5d3e10f18b9f48a7b5e1f887e459f6d06c4077bc2c283 | quote: Email hosting for one domain for up to 5 users 5 GB Mail storage per user IMAP/ POP/ Active Sync not included.
  - [1] 2026-11-02: the pricing page was captured on 2026-11-02 and lists the Mail Free plan without IMAP, POP or Active Sync | capture: sha256:d03c095d97ede4a458a5d3e10f18b9f48a7b5e1f887e459f6d06c4077bc2c283 | quote: Email hosting for one domain for up to 5 users 5 GB Mail storage per user IMAP/ POP/ Active Sync not included.
  - [1] 2026-11-02: the Mail Free plan still excludes IMAP, POP and Active Sync, so the free edition has no programmatic mailbox read | capture: sha256:d03c095d97ede4a458a5d3e10f18b9f48a7b5e1f887e459f6d06c4077bc2c283 | quote: Email hosting for one domain for up to 5 users 5 GB Mail storage per user IMAP/ POP/ Active Sync not included.
- sources:
  - [1] https://www.zoho.com/mail/zohomail-pricing.html

## Zoho Mail Free — 5 GB/user, up to 25 users via referral, live IMAP

- `storage/zoho-mail-free-5-gb-user-up-to-25-users-via-referral-liv` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.zoho.com/mail
- free tier: Zoho's own help: "Each user is allocated 5 GB of storage under the free plan." Headcount: free plan is 5 users in select regions, expandable. Press release "increasing the number of mailboxes offered with the Zoho Mail free email hosting plan, doubling it from five to ten users .. extend the free user limit to 25 users by simply referring other customers". | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 30 MB | bytes: 30000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered; mailbox service. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 30 MB [1]
- limits note: Per-object-cap 30 MB real attachment (the 1 GB 'Huge Attachment' is a link, so it does not consume mailbox quota. It is not storage). 5 GB/user is the byte ceiling. Free plan is geo-restricted: "currently available only in selected data centers and may not be accessible in all regions.".
- interface detail: rest
- tooling: IMAP probe-verified: `imap.zoho.com:993` -> `* OK svwall.zoho.com IMAP4 Server` / `* CAPABILITY IMAP4rev1 ... ESEARCH LIST-EXTENDED LIST-STATUS WITHIN LITERAL- ACL CONDSTORE`. Attachments: 30 MB normal, "Huge Attachment" up to 1 GB (link-based, not stored in the mailbox).
- composes with: 5 GB × 25 users = 125 GB per free organisation, × N organisations. The referral ladder is the multiplier and it is free.
- reliability: Free and paid plans cannot be mixed in one org; upgrading one user can disable the rest. Free plan availability varies by data centre.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Zoho's own help: "Each user is allocated 5 GB of storage under the free plan." Headcount: free plan is 5 users in select regions, expandable — press release "increasing the number of mailboxes offered with the Zoho Mail free email hosting plan, doubling it from five to ten users ... extend the free user limit to 25 users by simply referring other customers".
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: "5 GB of storage under the free plan"
  - [2] 2026-10-21: 5 -> 10 users, extendable to 25 via referrals
  - withheld 2026-10-21: probe: imap.zoho.com:993 -> * OK svwall.zoho.com IMAP4 Server + full CAPABILITY
- sources:
  - [1] https://www.zoho.com/mail/help/mailbox-quota.html
  - [2] https://www.zoho.com/news/zoho-expands-free-email-hosting-plan.html

## zoho wiki / readthedocs / tettra

- `storage/zoho-wiki-readthedocs-tettra` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.zoho.com/wiki/help/faq.html
- free tier: none reachable: Zoho Wiki is free for 3 users but publishes no storage number anywhere in its FAQ; ReadTheDocs Community is free for open-source and publishes no storage quota (only build resources: 7 GB… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Zoho Wiki is free for 3 users but publishes no storage number anywhere in its FAQ; ReadTheDocs Community is free for open-source and publishes no storage quota (only build resources: 7 GB…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Zoho Wiki is free for 3 users but publishes no storage number anywhere in its FAQ; ReadTheDocs Community is free for open-source and publishes no storage quota only build resources: 7 GB RA
  - [2] 2026-10-21: cited as the basis of the rejection: Zoho Wiki is free for 3 users but publishes no storage number anywhere in its FAQ; ReadTheDocs Community is free for open-source and publishes no storage quota only build resources: 7 GB RA
  - [3] 2026-10-21: cited as the basis of the rejection: Zoho Wiki is free for 3 users but publishes no storage number anywhere in its FAQ; ReadTheDocs Community is free for open-source and publishes no storage quota only build resources: 7 GB RA
- sources:
  - [1] https://www.zoho.com/wiki/help/faq.html
  - [2] https://about.readthedocs.com/pricing/
  - [3] https://docs.readthedocs.com/platform/stable/builds.html

## Zoho WorkDrive

- `storage/zoho-workdrive` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.zoho.com/workdrive/
- free tier: 5 GB free forever on the Individual plan | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered on the free individual plan; no CDN story. | metered: yes
- identity: institution
- interface: rest, rclone
- limits note: 5 GB; team plans are 15-day trials, not free; API is throttled per Zoho account.
- interface detail: rest
- tooling: Native rclone backend 'zoho' (Tier 3, added v1.54, rclone.org/zoho/).
- composes with: 5 GB x unlimited free Zoho accounts (one per email address, and Zoho permits many).
- reliability: Stable vendor, tiny quota; the Zoho 'one account per email' rule makes farming cheap but each unit is small.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB free forever on the Individual plan
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Everything you need to get started with 5 GB of free storage... Free / Forever - 5 GB of free storage'
  - [2] 2026-10-21: 'Zoho Workdrive... added in v1.54 [Tier 3]'
- sources:
  - [1] https://www.zoho.com/workdrive/individual-plan.html
  - [2] https://rclone.org/zoho/

## zoho workplace free edition

- `storage/zoho-workplace-free-edition` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.zoho.com/workplace/pricing.html
- free tier: none reachable: The free edition's WorkDrive team-storage number could not be pinned down on the pricing page (the 100 GB / 10 GB-per-user figures are the paid tiers). Not reportable as a quota without a… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The free edition's WorkDrive team-storage number could not be pinned down on the pricing page (the 100 GB / 10 GB-per-user figures are the paid tiers). Not reportable as a quota without a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The free edition's WorkDrive team-storage number could not be pinned down on the pricing page (the 100 GB / 10 GB-per-user figures are the paid tiers). Not reportable as a quota without a…
- sources:
  - [1] https://www.zoho.com/workplace/pricing.html
