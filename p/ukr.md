# ukr.net mail

> ukr.net | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ukr/ | JSON https://fshy.ajam.dev/api/v1/entity/ukr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UKR.NET Mail — 100 GB per single message, 1024 attachments/message

- `storage/ukr-net-mail-100-gb-per-single-message-1024-attachments` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:34.761Z (live) | stale on 2026-12-11
- url https://www.ukr.net
- disagrees on verdict: `storage/ukr-net-mail` says fails-quota, `storage/ukr-net-mail-100-gb-per-single-message-1024-attachments` says qualifies-with-caveat
- free tier: До кожного листа можна прикріпити до 1024 вкладень, однак пам'ятайте, що загальний розмір листа разом з усіма вкладеннями не повинен перевищувати 100 Гб. | unit: GB | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: загальний розмір листа разом з усіма вкладеннями не повинен перевищувати 100 Гб | bytes: 100000000000 | source: [1] | note: not stated
- retention: unverified: https://wiki.ukr.net/WorkWithMessages states no retention period and only that mailboxes have no limit on the number of stored messages | source: [1] | note: not stated
- egress: Unmetered by provider; mailbox service, no transfer billing. | metered: no
- identity: email | detail: unverified: the cited help pages state IMAP settings and message limits, not the sign-up requirements
- interface: rest
- limits:
  - per-object-cap (binding): загальний розмір листа разом з усіма вкладеннями не повинен перевищувати 100 Гб [1]
- limits note: З 18.02.2020 пошта @UKR.NET не дозволяє використовувати основний пароль від акаунта для підключення зовнішніх програм до скриньки за протоколом IMAP із міркувань безпеки.
- interface detail: rest
- tooling: IMAP with app-specific passwords (account password blocked for IMAP since 2020-02-18). probe-verified live: `imap.ukr.net:993` -> `* OK IMAP4 ready` / `* CAPABILITY IMAP4rev1 IDLE ID XLIST NAMESPACE AUTH=PLAIN`. Requires enabling IMAP in settings and generating a per-app password.
- composes with: Byte quota per account is not published at all. Only the per-message cap. If the 100 GB/message figure holds, a handful of accounts covers 10 TiB; if it is a unit typo the real cap is likely 100 MB and the provider collapses to noise. This needs an authenticated test before it is counted.
- reliability: The 100 GB claim is a docs statement with no probe evidence behind it and one plausible unit error (Гб vs Мб); do not size anything against it until an authenticated APPEND succeeds.
- notes: Help wiki states verbatim: "До кожного листа можна прикріпити до 1024 вкладень, однак пам'ятайте, що загальний розмір листа разом з усіма вкладеннями не повинен перевищувати 100 Гб." = up to 1,024 attachments per message, and the total message size including all attachments must not exceed 100 GB. If that figure is real it is the largest per-object cap found anywhere in this niche — 40x Yahoo's APPENDLIMIT and 3x Outlook's SMTP SIZE.
- evidence note: the wiki.ukr.net page states up to 1024 attachments and 100 Gb per message
- evidence:
  - [1] 2026-10-21: "до 1024 вкладень ... не повинен перевищувати 100 Гб", read live 2026-10-21
  - [2] 2026-10-21: IMAP enabled + app password required since 2020-02-18
  - withheld 2026-10-21: probe: openssl s_client -connect imap.ukr.net:993 -> * OK IMAP4 ready; CAPABILITY has no APPENDLIMIT
  - [1] 2026-11-09: the wiki states up to 1024 attachments and 100 Gb per message | capture: sha256:af90926661efda81566a3c6321dece0872d0e924b48e6b76b687aae6678ced92 | quote: До кожного листа можна прикріпити до 1024 вкладень, однак пам'ятайте, що загальний розмір листа разом з усіма вкладеннями не повинен перевищувати 100 Гб.
  - [1] 2026-11-09: the wiki states mailboxes have no limit on stored messages | capture: sha256:af90926661efda81566a3c6321dece0872d0e924b48e6b76b687aae6678ced92 | quote: Скриньки @ UKR.NET не мають обмежень на кількість збережених листів.
  - [2] 2026-11-09: the wiki states the account password is refused for IMAP | capture: sha256:1ff79100d1fcf8ead6b4c76bb9ad0aa4508a6e12cdfd13501a9ab9f8f54efe4e | quote: З 18.02.2020 пошта @UKR.NET не дозволяє використовувати основний пароль від акаунта для підключення зовнішніх програм до скриньки за протоколом IMAP із міркувань безпеки.
- sources:
  - [1] https://wiki.ukr.net/WorkWithMessages
  - [2] https://wiki.ukr.net/ManageIMAPAccess

## ukr.net mail

- `storage/ukr-net-mail` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:30.464Z (live) | stale on 2026-12-04
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
  - [2] 2026-11-19: the registration form pre-sets the phone field to +380 and requires an SMS confirmation code | capture: sha256:3c228247c2be68eaa7ff3ee512d5f20fdf2aa587294938a3406c7ad38ba89372 | quote: Mobile phone number +380 The confirmation code will be sent to this number
- sources:
  - [1] https://accounts.ukr.net/registration
  - [2] https://accounts.ukr.net/registration?lang=en
