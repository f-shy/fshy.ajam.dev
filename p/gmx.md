# GMX

> gmx.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gmx/ | JSON https://fshy.ajam.dev/api/v1/entity/gmx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GMX (free) — 65 GB mailbox, IMAP after opt-in, 135 MiB SMTP SIZE

- `storage/gmx-65-gb-mailbox-imap-after-opt-in-135-mib-smtp-size` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.gmx.com
- free tier: GMX's own storage page: "With GMX, you can store up to 65 GB worth of emails. To put that into perspective, that's around 500,000 emails!" | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 65 GB total is the byte ceiling. Folders can be set to auto-delete on a timer, so retention is user-visible and must be left at 'unlimited'. | source: [1] | note: not stated
- egress: Unmetered; mailbox service. | metered: no
- identity: email
- interface: rest
- limits note: per-object-cap from SMTP: `smtp.gmx.com:587` -> `250 SIZE 141557760` = 135 MiB per message (identical value on mail.com, same platform). 65 GB total is the byte ceiling. Folders can be set to auto-delete on a timer, so retention is user-visible and must be left at 'unlimited'.
- interface detail: rest
- tooling: IMAP probe-verified: `imap.gmx.net:993` -> `* OK [CAPABILITY IMAP4rev1 CHILDREN ENABLE ID IDLE LIST-EXTENDED LIST-STATUS LITERAL- MOVE NAMESPACE SASL-IR SORT SPECIAL-USE THREAD=ORDEREDSUBJECT UIDPLUS UNSELECT WITHIN AUTH=LOGIN AUTH=PLAIN]`. IMAP is OFF by default and must be toggled on in settings (documented, not a paywall). Same server identity as mail.com. The IMAP banner `H migmxus005` is byte-identical in shape to imap.mail.com's.
- composes with: 65 GB × N free accounts. GMX and mail.com are both United Internet properties, but only GMX leaves IMAP open on the free tier. So GMX is the reachable half of that 130 GB pair.
- reliability: Free accounts are deleted for inactivity; IMAP access is auto-revoked "for security reasons" after a long period of non-use, so a dormant archive mailbox can lose its programmatic path.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: GMX's own storage page: "With GMX, you can store up to 65 GB worth of emails. To put that into perspective, that's around 500,000 emails!"
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: "store up to 65 GB worth of emails"
  - withheld 2026-10-21: probe: openssl s_client -connect imap.gmx.net:993 -> * OK [CAPABILITY ...] IMAP server ready H migmx010 32.4
  - withheld 2026-10-21: probe: smtp.gmx.com:587 STARTTLS EHLO -> 250 SIZE 141557760
- sources:
  - [1] https://www.gmx.com/mail/storage/
