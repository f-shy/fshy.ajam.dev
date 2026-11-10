# CT8.PL

> ct8.pl | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ct8/ | JSON https://fshy.ajam.dev/api/v1/entity/ct8.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CT8.PL

- `compute/ct8-pl` | fails-quota | evidence documented | binding write-gated | category shared shell | tier free hosting account
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:24:00.000Z (live) | stale on 2026-11-24
- url https://www.ct8.pl/
- free tier: Quoted from the home page: '3 GB powierzchni dyskowej, nieograniczony transfer, 16 baz danych i 100 stron WWW' (3 GB of disk, unlimited transfer, 16 databases and 100 websites). The offer page adds SSH access, the `devil` account command, crontab, the ability to run your own software, daily backups, and Git/SVN/Hg repositories. | unit: GB | metered on: stored-bytes | read on: 2026-10-24 | source: [1] | note: the vendor writes GB with no binary qualifier; kept as stated. The home page also shows the account counter at '5000 / 5000'
- per-object cap: not applicable: the unit is a hosting account, not an object. The offer page states 'Brak sztucznego limitu wielkości pojedynczego pliku' (no artificial per-file size limit).
- retention: Quoted from the terms, clause 12: 'Konto użytkownika, na które nie było poprawnego zalogowania przez panel DevilWEB lub SSH przez okres 90 dni zostanie automatycznie usunięte z systemu bez możliwości odzyskania danych zgromadzonych na tym koncie.' (an account with no correct DevilWEB panel or SSH login for 90 days is deleted automatically with no recovery). | days: 90 | source: [2] | note: the clock resets on a panel login as well as an SSH login; the news page of 2016 states 3 months, which is the same rule
- egress: 'nieograniczony transfer' (unlimited transfer). The terms then say the operator may block an account whose software 'nadmiernie wykorzystującego zasoby serwerów' (excessively uses server resources), which is a discretionary throttle and not a number. | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: No card, no hold, no phone. The registration page carries no form fields at all on the day read, only the capacity refusal, so what the form would ask could not be read. The terms state accounts are created automatically ('Konto zakładane automatycznie') and the news page says 'konta aktywowane są automatycznie w ciągu kilku minut'. A third-party aggregator reports that CT8 stopped serving non-Polish IPs, which would be a geo gate; that claim is reported, not documented, because no first-party page read states it.
- interface: ssh
- limits:
  - volume-quota: 3 GB of disk, 16 databases, 100 websites per account [1]
  - retention-clamped: deleted after 90 days without a DevilWEB or SSH login [2]
  - write-gated (binding): registration is refused outright while the server is at its account cap: 'Limit użytkowników serwera został osiągnięty, rejestracja nowego konta nie jest aktualnie możliwa.' [3]
  - volume-quota: the operator caps the server at 1000 active accounts per its own 2016 news page, while the home page counter reads 5000 / 5000 today [4]
- binding note: the account cannot be created at all: the registration page returns a capacity refusal rather than a form
- interface detail: SSH plus the DevilWEB panel and a `devil` command for account management; the offer page lists PHP 5.6 through 8.5, Python, Ruby, Perl, Java, Go, C/C++, Node.js, Django, MySQL 8.0, PostgreSQL 16, MongoDB 6.0, Git/SVN/Hg, crontab and mod_rewrite
- tooling: any SSH client; the DevilWEB panel; the `devil` CLI; a full language toolchain on the host
- composes with: 3 GB with SSH, cron and the ability to run your own software is the closest thing to serv00 among evaluated providers, and the account is closed today; it would be a job runner or a small always-on service if it opened.
- reliability: no reliability event observed; the server is at its account cap and published notice directs applicants to a paid sibling product.
- notes: Classified as fails-quota rather than skipped because the offer is real and generous (3 GB, SSH, cron, your own binaries, 16 databases) and every aggregator lists it as available. Two independent blockers: the account cap is reached, so the registration page refuses; and a third-party report says non-Polish IPs are no longer served. The home page counter of 5000/5000 also contradicts published 2016 statement of a 1000-account cap, which is a documented inconsistency in the vendor's own material and is recorded rather than resolved. What could not be established: what the registration form asks, and whether the geo restriction is real.
- evidence note: quota, retention, interfaces and the capacity refusal are all quoted from first-party pages read; the geo restriction is reported from an aggregator and labelled as such
- extras:
  - shape.disk_gib: 3
  - billing_model: free
  - term: perpetual
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: no price: 'Tak jest, nie pobieramy żadnych opłat' (we charge no fees)
  - free_tier_kind: perpetual
  - network_out.allow_outbound: yes
  - network_out.ports: not stated; a hosting account, so HTTP and the listed service ports
  - session_cap.restart_required: no
  - session_cap.note: deleted after 90 days without a DevilWEB or SSH login
  - account_cap.stated_in_2016_news: 1000
  - account_cap.home_page_counter_as_read: 5000 / 5000
  - account_cap.registration_state_as_read: refused: server user limit reached
  - geo_restriction: reported by a third-party aggregator only; no first-party page read states it
- evidence:
  - [1] 2026-10-24: quoted: '3 GB powierzchni dyskowej, nieograniczony transfer, 16 baz danych i 100 stron WWW' and the counter '5000 / 5000 Całkowita liczba kont założonych na serwerze'
  - [3] 2026-10-24: quoted in full: 'Limit użytkowników serwera został osiągnięty, rejestracja nowego konta nie jest aktualnie możliwa.' followed by an advertisement for SMALL.PL at 40 PLN a year
  - [2] 2026-10-24: clause 12 quoted: an account with no correct DevilWEB or SSH login for 90 days is deleted with no recovery; clause 2: 'Wszystkie usługi dostępne w serwisie CT8.PL są darmowe.'
  - [5] 2026-10-24: quoted: 'Dostęp do SSH oraz możliwość zarządznia kontem przy pomocy polecenia devil', 'Zadania crontab', 'Możliwość uruchamiania własnego oprogramowania', 'Codzienne kopie zapasowe', 'Limit wykonywania skryptu PHP wynosi 180 sekund'
  - [4] 2026-10-24: quoted: 'Na serwerze nie może być więcej niż 1000 aktywnych kont jednocześnie' and 'Konta, które nie będą używane przez 3 miesiące będą automatycznie usuwane'
  - [6] 2026-10-24: the operator is named as ADMIN.NET.PL S.C., a Polish civil partnership (spółka cywilna) in Tarnów, with a registered address and NIP, REGON and VAT UE numbers on the contact page
  - [7] 2026-10-24: reported, third party: 'CT8.PL不再支持非波兰IP使用，非波兰用户建议注册 Serv00' (CT8.PL no longer supports non-Polish IPs; non-Polish users are advised to register Serv00). Not confirmed by any first-party page read.
- sources:
  - [1] https://www.ct8.pl/
  - [2] https://www.ct8.pl/tos
  - [3] https://www.ct8.pl/offer/create_new_account
  - [4] https://www.ct8.pl/news
  - [5] https://www.ct8.pl/offer
  - [6] https://www.ct8.pl/contact
  - [7] https://www.aldsd.com/ct8-pl
