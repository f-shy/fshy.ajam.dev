# mail.bg

> mail.bg | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mail-2/ | JSON https://fshy.ajam.dev/api/v1/entity/mail-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mail.bg — 50 GB free mailbox with free IMAP/POP, Bulgarian

- `storage/mail-bg-50-gb-free-mailbox-with-free-imap-pop-bulgarian` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:00.435Z (live) | stale on 2026-12-04
- url https://mail.bg
- disagrees on verdict: `storage/mail-bg` says fails-quota, `storage/mail-bg-50-gb-free-mailbox-with-free-imap-pop-bulgarian` says qualifies-with-caveat
- free tier: 50 GB mailbox | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MB attachments | bytes: 20000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered; mailbox service, no transfer billing. | metered: no
- identity: email | detail: a new email address and password are chosen at registration
- interface: rest
- limits:
  - per-object-cap (binding): 20 MB per attachment [1]
- limits note: Per-object-cap 20 MB per attachment (the binding constraint. 50 GB / 20 MB = ~2,500 messages to fill). No published daily upload meter. IMAP QUOTA extension present so the real byte ceiling is readable before you fill it.
- interface detail: rest
- tooling: IMAP probe-verified live: `imap.mail.bg:993` -> `* OK IMAP4 ready` / `* CAPABILITY IMAP4 IMAP4rev1 QUOTA UIDPLUS MULTIAPPEND BINARY IDLE AUTH=PLAIN`. QUOTA and MULTIAPPEND support is notable. You can read remaining bytes in-band and append several messages per round trip.
- composes with: 50 GB × N free accounts. Also offers free mail hosting on a user-owned domain, which means many mailboxes per domain rather than per signup. The multiplier is domains, not accounts.
- reliability: Small national provider; homepage 302s and the apex signup page 504'd repeatedly through the proxy, so the live signup flow is fragile even though the IMAP server is healthy.
- notes: Signup page, Waybacks capture 2026-02-23: "50 GB пощенска кутия", "20 MB приложения (атачмънти)", "1 GB файл до всяка поща по света". = 50 GB mailbox, 20 MB attachment cap, 1 GB file to any mailbox worldwide.
- evidence:
  - [2] 2026-10-21: 
  - withheld 2026-10-21: probe: openssl s_client -connect imap.mail.bg:993 -> * OK IMAP4 ready + CAPABILITY incl. QUOTA, MULTIAPPEND, BINARY
  - withheld 2026-10-21: probe: GET mail.bg/ -> 302 (0 bytes); GET mail.bg/help -> 200 (17 bytes)
  - [3] 2026-11-09: the archived signup page states a 50 GB mailbox | capture: sha256:04f82417bcc2cb73fabfe7c8fbff94303780382fe3e44eda178259c94e77003e | quote: 50 GB пощенска кутия
  - [3] 2026-11-09: the archived signup page states a 20 MB attachment cap | capture: sha256:04f82417bcc2cb73fabfe7c8fbff94303780382fe3e44eda178259c94e77003e | quote: 20 MB приложения (атачмънти)
  - [3] 2026-11-09: the archived signup page asks for a new email address and password | capture: sha256:04f82417bcc2cb73fabfe7c8fbff94303780382fe3e44eda178259c94e77003e | quote: За регистрация на поща, моля изберете нов имейл адрес и парола.
  - [3] 2026-11-19: the archived first-party signup page confirms a 50 GB mailbox | capture: sha256:04f82417bcc2cb73fabfe7c8fbff94303780382fe3e44eda178259c94e77003e | quote: 50 GB пощенска кутия
  - [3] 2026-11-19: the archived signup page confirms a 20 MB attachment cap | capture: sha256:04f82417bcc2cb73fabfe7c8fbff94303780382fe3e44eda178259c94e77003e | quote: 20 MB приложения (атачмънти)
  - [3] 2026-11-19: the archived signup page confirms registration asks for a new email address and password | capture: sha256:04f82417bcc2cb73fabfe7c8fbff94303780382fe3e44eda178259c94e77003e | quote: За регистрация на поща, моля изберете нов имейл адрес и парола.
- sources:
  - [1] https://mail.bg/signup
  - [2] https://web.archive.org/web/202603/mail.bg/signup
  - [3] https://web.archive.org/web/20260223024603/https://mail.bg/signup?provider=wayback

## mail.bg

- `storage/mail-bg` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:08.542Z (live) | stale on 2026-12-04
- url https://mail.bg/signup
- disagrees on verdict: `storage/mail-bg` says fails-quota, `storage/mail-bg-50-gb-free-mailbox-with-free-imap-pop-bulgarian` says qualifies-with-caveat
- free tier: none reachable: Signup collects a mandatory recovery phone ('Телефон за възстановяване на парола: *', marked required) plus gender and date of birth, and then does not activate automatically: 'Пощенската… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Signup collects a mandatory recovery phone ('Телефон за възстановяване на парола: *', marked required) plus gender and date of birth, and then does not activate automatically: 'Пощенската…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Signup collects a mandatory recovery phone ('Телефон за възстановяване на парола: *', marked required) plus gender and date of birth, and then does not activate automatically: 'Пощенската…
  - [2] 2026-10-21: cited as the basis of the rejection: Signup collects a mandatory recovery phone ('Телефон за възстановяване на парола: *', marked required) plus gender and date of birth, and then does not activate automatically: 'Пощенската ку
  - [1] 2026-11-19: the signup form still marks a recovery phone number as required | capture: sha256:2d2e12c1ef5afb49a73f73c882dcccb258b9eb48cded30f4d3dc80d0977ca1e1 | quote: Телефон за възстановяване на парола: \*
  - [1] 2026-11-19: the mailbox is not activated automatically; the user must contact the provider, so signup is gated | capture: sha256:2d2e12c1ef5afb49a73f73c882dcccb258b9eb48cded30f4d3dc80d0977ca1e1 | quote: За да я активираме, пишете ни!
- sources:
  - [1] https://mail.bg/signup
  - [2] https://mail.bg/
