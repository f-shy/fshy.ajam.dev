# Outlook.com

> outlook.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/outlook/ | JSON https://fshy.ajam.dev/api/v1/entity/outlook.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Outlook.com (free) — 15 GB mail quota, 150 MiB SMTP SIZE

- `storage/outlook-com-15-gb-mail-quota-150-mib-smtp-size` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://outlook.com
- free tier: 15 GB mail storage, explicitly separate from the 5 GB OneDrive allowance: "You get 15 GB of free Outlook.com email storage which is separate from your Microsoft cloud storage. You have 5 GB of free cloud storage with your Microsoft account shared across your files and photos, attachments in Outlook.com and your Microsoft 365 apps." | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap governed by `250-SIZE 157286400` = 150 MiB | bytes: 157286400 | source: [1] | note: not stated
- retention: Deleted Items counts against quota until emptied or auto-purged at 30 days | days: 30 | source: [1] | note: not stated
- egress: Unmetered; no transfer billing on a mailbox. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap governed by `250-SIZE 157286400` = 150 MiB [1]
- limits note: per-object-cap governed by `250-SIZE 157286400` = 150 MiB per SMTP message, the largest SMTP SIZE probed in this area. Deleted Items counts against quota until emptied or auto-purged at 30 days. No published IMAP/day byte meter equivalent to Gmail's.
- interface detail: rest
- tooling: IMAP probe-verified: `imap-mail.outlook.com:993` -> `* OK Microsoft Exchange IMAP4 service ready` / `* CAPABILITY IMAP4 IMAP4rev1 AUTH=XOAUTH2 LOGINDISABLED SASL-IR UIDPLUS MOVE ID UNSELECT CHILDREN IDLE NAMESPACE LITERAL+`. Note LOGINDISABLED. OAuth2 only. SMTP probe: `smtp-mail.outlook.com:587` -> `250-SIZE 157286400` (150 MiB) and `250-BINARYMIME`.
- composes with: 15 GB × N free Microsoft accounts. Distinct from the A1-education 100 TB tenant offer. This is the consumer path, no tenant needed.
- reliability: LOGINDISABLED means app-password/basic auth is off. An OAuth2 client registration is mandatory, which is the real entry cost.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 15 GB mail storage, explicitly separate from the 5 GB OneDrive allowance: "You get 15 GB of free Outlook.com email storage which is separate from your Microsoft cloud storage. You have 5 GB of free cloud storage with your Microsoft account shared across your files and photos, attachments in Outlook.com and your Microsoft 365 apps."
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: "15 GB of free Outlook.com email storage which is separate from your Microsoft cloud storage"
  - withheld 2026-10-21: probe: smtp-mail.outlook.com:587 STARTTLS EHLO -> 250-SIZE 157286400, 250-BINARYMIME
  - withheld 2026-10-21: probe: imap-mail.outlook.com:993 -> * OK Microsoft Exchange IMAP4 service ready + CAPABILITY with LOGINDISABLED, LITERAL+
- sources:
  - [1] https://support.microsoft.com/en-us/outlook/storage-limits-in-outlook-com
