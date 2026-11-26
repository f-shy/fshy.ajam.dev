# Filebit.pl

> filebit.pl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filebit/ | JSON https://fshy.ajam.dev/api/v1/entity/filebit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filebit.pl

- `debrid/filebit-pl` | qualifies-with-caveat | evidence documented | binding volume-quota | category multi-hoster (Polish; time accounts and transfer packs) | tier time and transfer packages
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:52.401Z (live) | stale on 2026-12-26
- url https://filebit.pl/
- free tier: 250 MB free on registration to test the service; the registration page title also advertises a 3-day free test with no card. | unit: MB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: Two free allowances, which do not contradict each other: a one-time 250 MB of transfer on registration (FAQ and terms chapter 4 item 6), and one file per day with no account (terms chapter 5 section 1 item 3). The daily file has no stated size cap, host list or behaviour at the limit; it is unverified how it is enforced.
- per-object cap: unverified: no per-file cap is stated on the offer page or the FAQ | source: [2]
- retention: Generated download links are valid for 24 hours and then become inactive; how long a transferred file itself stays on the server is not stated. | source: [2]
- egress: Time accounts: 30 days 50 GB/24h at 19.49, 60 days at 36.99, 90 days at 52.99; 30 days 100 GB/24h at 38.49, 60 days at 72.99, 90 days at 103.99. Transfer packs: 50 GB at 18.49, 83 GB at 23.69, 165 GB at 40.99, 330 GB at 68.99, 830 GB at 136.99, with no time limit. | metered: yes | free allowance: 250 MB on registration | source: [2]
- identity: email | detail: Registration form asks for a unique login, a current email address needed for contact and password reset, and a password of at least 12 characters with an uppercase letter, a lowercase letter and a digit; referrer login is optional. Terms and marketing consents are required. The former 3-day free test title is no longer on the page.
- interface: browser
- limits:
  - volume-quota (binding): time accounts 50 GB or 100 GB per 24 hours; transfer packs 50 GB to 830 GB with no time limit [2]
  - request-rate: unverified: no per-second or concurrency limit stated [1]
- binding note: Both account types are metered in bytes: a daily allowance on time accounts and a fixed pack on transfer accounts.
- interface detail: Web form and account panel; the FAQ says a download manager such as JDownloader can be fed the links.
- tooling: Browser or JDownloader; no API is documented on the pages read.
- composes with: A transfer pack (volume, no expiry) covers irregular pulls; a time account covers a daily allowance. Hosts: 46 listed.
- reliability: No outage or removal observed; the site shows live counters (users online, bandwidth load, total downloaded).
- notes: Polish multi-hoster; prices shown without a currency symbol, read as PLN from the list header. HappyHours halves the metered transfer between 02:00 and 10:00 on transfer accounts per the FAQ. No programmatic path found: Web form and account panel; the FAQ says a download manager such as JDownloader can be fed the links.
- evidence note: First-party pages read the same day: FAQ, price list, registration page. Currency read from the price list header (PLN).
- evidence:
  - [1] 2026-11-03: the FAQ states a free 250 MB on registration | capture: sha256:f4aac8998908825a160d3f650053f3025792720ef71fd9b4bb4d72fa25752144 | quote: Przy rejestracji konta dostaniesz za darmo, na start 250 MB, które możesz sobie wykorzystać i sprawdzić, jak działa nasz serwis.
  - [3] 2026-11-03: the registration page advertises a free 3-day test with no card | capture: sha256:12a032055d556b7442ddaeec360fbc06e9ec21e22384b7e56b9d2532021b6eec | quote: Darmowy Test 3 Dni ✓ Bez Karty - Rejestracja | Filebit.pl
  - [2] 2026-11-03: the cheapest transfer pack is 50 GB at 17.99 | capture: sha256:a1827677ff617a46cb42091256292324b1c4eb6feed15e4ece91c4c85da9b4ff | quote: - 50 GB 17.99
  - [2] 2026-11-03: the cheapest time account is 30 days at 50 GB/24h for 18.2 | capture: sha256:a1827677ff617a46cb42091256292324b1c4eb6feed15e4ece91c4c85da9b4ff | quote: - 30 dni 50 GB/24h 18.2
  - [2] 2026-11-03: transfer packs are priced in PLN | capture: sha256:a1827677ff617a46cb42091256292324b1c4eb6feed15e4ece91c4c85da9b4ff | quote: PLN Większy pakiet, mniejsza cena za 1GB!
  - [4] 2026-11-03: the terms text offers one free file per day before account creation, which differs from the FAQ | capture: sha256:498d5a91f34e97f24e3ce41417f1a0f29b0e263abcdd65b37d97049926281b3b | quote: Klient ma możliwość bezpłatnego przetestowania Serwisu przed założeniem Konta Użytkownika - może pobrać jeden plik dziennie bez opłat.
  - [1] 2026-11-03: a download manager can be used with the service | capture: sha256:f4aac8998908825a160d3f650053f3025792720ef71fd9b4bb4d72fa25752144 | quote: Czy mogę używać do pobierania plików programów typu Jdownloader? Tak można.
  - [4] 2026-11-03: the terms (chapter 5, section 1, item 3) offer one free file per day before an account exists, a recurring allowance and not a one-time grant | capture: sha256:498d5a91f34e97f24e3ce41417f1a0f29b0e263abcdd65b37d97049926281b3b | quote: Klient ma możliwość bezpłatnego przetestowania Serwisu przed założeniem Konta Użytkownika - może pobrać jeden plik dziennie bez opłat.
  - [4] 2026-11-03: the terms (chapter 4, item 6) give the same one-time 250 MB on registration that the FAQ states, so the FAQ and the terms agree on it | capture: sha256:498d5a91f34e97f24e3ce41417f1a0f29b0e263abcdd65b37d97049926281b3b | quote: Po zarejestrowaniu Konta Użytkownika, Użytkownik otrzymuje bezpłatnie 250 MB Transferu, które może dowolnie spożytkować.
  - [1] 2026-11-03: the FAQ still states a one-time free 250 MB on registration | capture: sha256:f4aac8998908825a160d3f650053f3025792720ef71fd9b4bb4d72fa25752144 | quote: Przy rejestracji konta dostaniesz za darmo, na start 250 MB, które możesz sobie wykorzystać i sprawdzić, jak działa nasz serwis.
  - [2] 2026-11-25: the cheapest time account now costs 19.49 for 30 days at 50 GB/24h | capture: sha256:1b54f1ffe52569d8f61c0895503231079bc49ae937877d790a996fc79a2ca7a8 | quote: - 30 dni 50 GB/24h 19.49
  - [1] 2026-11-25: the FAQ still grants 250 MB on registration | capture: sha256:f4aac8998908825a160d3f650053f3025792720ef71fd9b4bb4d72fa25752144 | quote: Przy rejestracji konta dostaniesz za darmo, na start 250 MB, które możesz sobie wykorzystać i sprawdzić, jak działa nasz serwis.
  - [1] 2026-11-25: the FAQ still confirms a download manager can be used with the service | capture: sha256:f4aac8998908825a160d3f650053f3025792720ef71fd9b4bb4d72fa25752144 | quote: Czy mogę używać do pobierania plików programów typu Jdownloader? Tak można.
  - [3] 2026-11-25: the registration form now requires an email address | capture: sha256:ae3028b454980e5964e3f7c03eed8d62c6d29bcd171b3387e9e8455043581bd7 | quote: Podaj aktualny adres e-mail – niezbędny do kontaktu i resetu hasła
  - [4] 2026-11-25: the terms still offer one free file per day before an account exists | capture: sha256:498d5a91f34e97f24e3ce41417f1a0f29b0e263abcdd65b37d97049926281b3b | quote: Klient ma możliwość bezpłatnego przetestowania Serwisu przed założeniem Konta Użytkownika - może pobrać jeden plik dziennie bez opłat.
  - [4] 2026-11-25: generated download links expire after 24 hours | capture: sha256:498d5a91f34e97f24e3ce41417f1a0f29b0e263abcdd65b37d97049926281b3b | quote: Wygenerowane linki do plików (danych) są ważne 24 godziny i po tym czasie stają się nieaktywne.
- sources:
  - [1] https://filebit.pl/faq
  - [2] https://filebit.pl/oferta
  - [3] https://filebit.pl/rejestracja
  - [4] https://filebit.pl/regulamin
