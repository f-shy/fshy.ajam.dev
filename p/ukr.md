# ukr.net mail

> ukr.net | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ukr/ | JSON https://fshy.ajam.dev/api/v1/entity/ukr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UKR.NET Mail — 100 GB per single message, 1024 attachments/message

- `storage/ukr-net-mail-100-gb-per-single-message-1024-attachments` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.ukr.net
- disagrees on verdict: `storage/ukr-net-mail` says fails-quota, `storage/ukr-net-mail-100-gb-per-single-message-1024-attachments` says qualifies-with-caveat
- free tier: Help wiki states verbatim: "До кожного листа можна прикріпити до 1024 вкладень, однак пам'ятайте, що загальний розмір листа разом з усіма вкладеннями не повинен перевищувати 100 Гб." = up to 1,024 attachments per message, and the total message size including all attachments must not exceed 100 GB. If that figure is real it is the largest per-object cap found anywhere in this niche — 40x Yahoo's APPENDLIMIT and 3x Outlook's SMTP SIZE. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap claimed 100 GB | bytes: 100000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered by provider; mailbox service, no transfer billing. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap claimed 100 GB [1]
- limits note: Per-object-cap claimed 100 GB/message (unverified. No APPENDLIMIT in CAPABILITY, so the server may reject below that). Actual mailbox byte quota not published. IMAP requires a generated app password; the account password is refused.
- interface detail: rest
- tooling: IMAP with app-specific passwords (account password blocked for IMAP since 2020-02-18). probe-verified live: `imap.ukr.net:993` -> `* OK IMAP4 ready` / `* CAPABILITY IMAP4rev1 IDLE ID XLIST NAMESPACE AUTH=PLAIN`. Requires enabling IMAP in settings and generating a per-app password.
- composes with: Byte quota per account is not published at all. Only the per-message cap. If the 100 GB/message figure holds, a handful of accounts covers 10 TiB; if it is a unit typo the real cap is likely 100 MB and the provider collapses to noise. This needs an authenticated test before it is counted.
- reliability: The 100 GB claim is a docs statement with no probe evidence behind it and one plausible unit error (Гб vs Мб); do not size anything against it until an authenticated APPEND succeeds.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: "до 1024 вкладень ... не повинен перевищувати 100 Гб", read live 2026-10-21
  - [2] 2026-10-21: IMAP enabled + app password required since 2020-02-18
  - withheld 2026-10-21: probe: openssl s_client -connect imap.ukr.net:993 -> * OK IMAP4 ready; CAPABILITY has no APPENDLIMIT
- sources:
  - [1] https://wiki.ukr.net/WorkWithMessages
  - [2] https://wiki.ukr.net/ManageIMAPAccess

## ukr.net mail

- `storage/ukr-net-mail` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://accounts.ukr.net/registration
- disagrees on verdict: `storage/ukr-net-mail` says fails-quota, `storage/ukr-net-mail-100-gb-per-single-message-1024-attachments` says qualifies-with-caveat
- free tier: none reachable: Fixed-country dial code on the registration form: the phone field is pre-set to '+380' with the note 'На цей номер ми надішлемо код підтвердження' (we will send a confirmation code to this… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Fixed-country dial code on the registration form: the phone field is pre-set to '+380' with the note 'На цей номер ми надішлемо код підтвердження' (we will send a confirmation code to this…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Fixed-country dial code on the registration form: the phone field is pre-set to '+380' with the note 'На цей номер ми надішлемо код підтвердження' we will send a confirmation code to this n
- sources:
  - [1] https://accounts.ukr.net/registration
