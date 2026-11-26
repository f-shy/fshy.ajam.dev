# Yahoo Mail

> yahoo.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yahoo/ | JSON https://fshy.ajam.dev/api/v1/entity/yahoo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Yahoo Mail (free) — 20 GB, down from 1 TB

- `storage/yahoo-mail-20-gb-down-from-1-tb` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:33.473Z (live) | stale on 2026-12-04
- url https://mail.yahoo.com
- free tier: Yahoo's own help, read live: "Yahoo Mail incluye actualmente 20 GB de almacenamiento gratuito con cada cuenta" = 20 GB free per account. Plans: 100 GB, 1 TB; Mail Plus is 200 GB. The old 1 TB free tier is gone. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap **41,697,280 bytes (39.77 MiB | bytes: 41701867 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered; mailbox service. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap **41,697,280 bytes (39.77 MiB [1]
- limits note: Per-object-cap 41,697,280 bytes (39.77 MiB) advertised as `APPENDLIMIT`. The cleanest, most honest per-message cap of any provider here because it is protocol-advertised rather than buried in docs. SMTP agrees: `250-SIZE 41697280`.
- interface detail: rest
- tooling: IMAP probe-verified: `imap.mail.yahoo.com:993` -> `* OK Welcome! IMAP Server up and ready` / `* CAPABILITY IMAP4rev1 ... APPENDLIMIT=41697280`. That APPENDLIMIT is a live, machine-readable per-message byte cap.
- composes with: Mailbox allowance is 20 GB per account across independently registered email accounts.
- reliability: Quota was cut 1 TB -> 20 GB (Aug 2025) and again to 15 GB for UK/EU from 2026-05. A provider actively shrinking, which makes it a poor archive target structurally.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Yahoo's own help, read live: "Yahoo Mail incluye actualmente 20 GB de almacenamiento gratuito con cada cuenta" = 20 GB free per account. Plans: 100 GB, 1 TB; Mail Plus is 200 GB. The old 1 TB free tier is gone.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: "20 GB de almacenamiento gratuito", 100 GB / 1 TB / Mail Plus 200 GB tiers
  - withheld 2026-10-21: probe: imap.mail.yahoo.com:993 CAPABILITY -> APPENDLIMIT=41697280
  - withheld 2026-10-21: probe: smtp.mail.yahoo.com:587 EHLO -> 250-SIZE 41697280
  - [1] 2026-11-19: Yahoo Mail still includes 20 GB of free storage per account | capture: sha256:4e23a2d764b1e47775d045b8e2b9e61e0a040ad440e87ca7fa9a43018d533e93 | quote: Yahoo Mail incluye actualmente 20 GB de almacenamiento gratuito con cada cuenta
  - [1] 2026-11-19: Mail Plus plus a storage plan reaches at most 1.2 TB total | capture: sha256:4e23a2d764b1e47775d045b8e2b9e61e0a040ad440e87ca7fa9a43018d533e93 | quote: hasta 1.2 TB de almacenamiento total
  - [1] 2026-11-19: messages may be deleted after 12 months of account inactivity | capture: sha256:4e23a2d764b1e47775d045b8e2b9e61e0a040ad440e87ca7fa9a43018d533e93 | quote: Tu cuenta permanece inactiva durante 12 meses
- sources:
  - [1] https://es-us.ayuda.yahoo.com/kb/new-yahoo-mail/SLN37064.html
