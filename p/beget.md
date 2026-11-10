# Beget S3

> beget.com | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/beget/ | JSON https://fshy.ajam.dev/api/v1/entity/beget.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Beget S3 (Russia) — free egress S3 at 350 Mbit/s

- `storage/beget-s3-free-egress-s3-at-350-mbit-s-the-only-russian-o` | paid-only | evidence documented | binding per-ip-shaping | category object-storage
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:17.075Z (live) | stale on 2026-12-04
- url https://beget.com/ru/cloud/storage
- price 0.07 RUB per GB per day, 2.10 RUB per GB per month at 30 days (2,100 RUB per 1000 GB, 2,150.4 RUB per 1024 GB); egress and GET/POST/PUT requests are free; USD conversion unverified: no exchange rate was captured. | parsed USD 25.83/TB-mo
- free tier: No free allowance: pay-as-you-go at 0.07 RUB per 1 GB per day on used space; unlimited buckets, unlimited traffic on a 350 Mbit/s port, free GET/POST/PUT requests; stored volume is not capped. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: 50 TB maximum object size; 5 GB maximum per upload request; at most 10000 segments in a segmented upload. | source: [1] | note: stated in the vendor's technical-limits list (control-panel guide)
- retention: source: [1] | note: not stated
- egress: FREE and generous: «Безлимитный трафик. Полоса 350 Мбит/с. Бесплатные GET/POST/PUT-запросы». Unlimited traffic, 350 Mbit/s, free GET/POST/PUT requests. A Russian price-comparison article (serverdelo.ru, prices verified 2026-10-03) independently confirms «Скачивать бесплатно можно у Beget и Рег.облака. Трафик и запросы входят в цену». | metered: no
- identity: card | detail: unverified: behind a sign-up; the product page does not state what registration requires (payment card, phone).
- interface: s3-compatible, ftp, rclone
- limits:
  - per-ip-shaping (binding): 350 Mbit/s [1]
  - per-ip-shaping (binding): 3.8 TB/day [1]
  - per-object-cap: 50 TB per object; 5 GB per upload request [2]
  - request-rate: 2000 requests per second per account [2]
- limits note: 350 Mbit/s is the port cap, about 3.8 TB per day (derived), so serving 1 TiB per day fits with no burst; stored volume is not capped and billing is per GB per day.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: s3 + ftp
- tooling: S3 API, HTTPS, FTP; Terraform provider (github.com/LTD-Beget/terraform-provider-beget); rclone `s3`; custom subdomain + auto SSL. Documentation and CORS supported.
- composes with: Per-GB daily, no cap. Same rate at 5 TB and 20 TB.
- reliability: Long-running Russian shared host with 24/7 support and 99.98 % stated availability. No throttling evidence found. The commercial risk is FX: rouble pricing on a foreign card will carry the same discrimination pattern seen at Yandex.
- notes: ₽0.07 per GB per DAY (≈ ₽2.10/GB/month), billed daily on actual usage, unlimited buckets. Avail 99.98 %, three copies across servers.
- evidence note: Re-read on 2026-11-03 from vendor pages: https://beget.com/ru/cloud/storage (0.07 RUB per 1 GB per day; 350 Mbit/s port; unlimited buckets; availability 99,98%), https://beget.com/ru/kb/manual/obektnoe-hranilishche-s3-v-beget (50 TB object, 5 GB per upload request, 2000 requests per second, unlimited volume) and https://beget.com/ru/publichnaya-oferta (acceptance is by registering on the site; registration fields not listed). Registration fields stay unverified.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: ₽0.07 per GB per DAY (≈ ₽2.10/GB/month), billed daily on actual usage, unlimited buckets. Avail 99.98 %, three copies across servers.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $26.04/TB/mo at both 5 TB and 20 TB (₽0.07/GB/day × 30 × 1024 GB × 0.012111), egress $0 and requests $0. Compare OVH One-Zone at $9.34/TB/mo with the same free-egress structure — Beget is 2.8× the price for geography.
- evidence:
  - [1] 2026-10-21: «Стоимость хранения 0,07 ₽ за каждый 1 ГБ / день»; «Безлимитный трафик — Полоса 350 Мбит/с — Бесплатные GET/POST/PUT-запросы»; «Доступ к файлам по HTTPS, FTP и S3»; «Доступность 99,98 %»
  - [3] 2026-10-21: «Цены сверены с сайтами провайдеров 3 октября 2026 года»; table row «Beget | 2,10 ₽ (0,07 ₽ в день) | бесплатно, скорость до 350 Мбит/с | бесплатно»; lead «Скачивать бесплатно можно у Beget и Рег.облака»
  - [1] 2026-11-03: storage is billed at 0.07 RUB per 1 GB per day on used space | capture: sha256:16375d21d4c08a9beb7fb6965c324e51ef8e36a0a534349312c867976d053bbb | quote: Стоимость хранения 0,07 ₽ за каждый 1 ГБ / день.
  - [2] 2026-11-03: the maximum object size is 50 TB | capture: sha256:8eb42555ec2678db62dd1ea8b426325faaf5ffe9e93b44c24235a210ae1bd736 | quote: Максимальный размер объекта – 50 ТБ
  - [2] 2026-11-03: one upload request carries at most 5 GB | capture: sha256:8eb42555ec2678db62dd1ea8b426325faaf5ffe9e93b44c24235a210ae1bd736 | quote: Максимальный размер данных для загрузки за один запрос – 5 ГБ
  - [2] 2026-11-03: the account is limited to 2000 S3 API requests per second | capture: sha256:8eb42555ec2678db62dd1ea8b426325faaf5ffe9e93b44c24235a210ae1bd736 | quote: Максимальное количество HTTP-запросов к S3 API для аккаунта – 2000 запросов в секунду
  - [1] 2026-11-03: the port bandwidth is 350 Mbit/s | capture: sha256:16375d21d4c08a9beb7fb6965c324e51ef8e36a0a534349312c867976d053bbb | quote: Полоса 350 Мбит/с
  - [4] 2026-11-03: the offer is accepted by registering on the site; its fields are not stated | capture: sha256:e8809c373b8c429bfb2f9b196d8c06e987197a43a299b11c1bd300ce7a2e6e72 | quote: Акцепт Оферты — регистрация на сайте и получение прав доступа к собственным ресурсам Исполнителя
  - [2] 2026-11-03: stored volume is not capped | capture: sha256:8eb42555ec2678db62dd1ea8b426325faaf5ffe9e93b44c24235a210ae1bd736 | quote: Объем хранилища – не ограничено
  - [1] 2026-11-03: the number of buckets is unlimited | capture: sha256:16375d21d4c08a9beb7fb6965c324e51ef8e36a0a534349312c867976d053bbb | quote: Количество создаваемых бакетов при этом не ограничено.
  - [1] 2026-11-03: unlimited traffic on a 350 Mbit/s port, free GET/POST/PUT requests | capture: sha256:16375d21d4c08a9beb7fb6965c324e51ef8e36a0a534349312c867976d053bbb | quote: Полоса 350 Мбит/с
  - [1] 2026-11-03: the vendor page states availability of 99,98% | capture: sha256:16375d21d4c08a9beb7fb6965c324e51ef8e36a0a534349312c867976d053bbb | quote: Доступность 99,98%
- sources:
  - [1] https://beget.com/ru/cloud/storage
  - [2] https://beget.com/ru/kb/manual/obektnoe-hranilishche-s3-v-beget
  - [3] https://serverdelo.ru/rejtingi/s3-hranilishche/
  - [4] https://beget.com/ru/publichnaya-oferta

## Beget

- `compute/beget` | fails-identity | evidence documented | binding per-object-cap | category cloud VM
- needs card unknown, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://beget.com/ru/hosting/free
- free tier: A perpetual free shared-hosting account: 1 GiB SSD, one site, one FTP account and one database, unlimited domains, 10 CP of load, 25,000 file limit, PHP, Python, MySQL and Perl, with no advertising inserted. No technical support is provided on the free tier. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | detail: a mobile number that receives an SMS code, restricted by country: the free-hosting rules state the applicant enters a mobile number and the SMS code, and a forum post describing the signup form states 'Beget only supports registrations via phone numbers from Russia, Belarus, Ukraine, and Kazakhstan'. The same rules page adds that Beget may request documents proving the details, which is a possible second gate. No card is stated for the free tariff, and the SMS provider is not stated | country: RU, BY, UA or KZ
- interface: unknown
- limits:
  - per-object-cap (binding): The free account is registered by mobile phone and Beget's free-hosting rules require a phone number that receives the SMS code; the free tariff is documented as open to residents of Russia, Belarus, Ukraine and Kazakhstan, and the 25,000-file and 1 GiB limits bind long before any traffic limit does. [1]
- limits note: The free account is registered by mobile phone and Beget's free-hosting rules require a phone number that receives the SMS code; the free tariff is documented as open to residents of Russia, Belarus, Ukraine and Kazakhstan, and the 25,000-file and 1 GiB limits bind long before any traffic limit does.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 1 GiB of SSD with PHP and MySQL and no support is a place to park a static page or a small cron-driven script, and it composes with an external database only because the site limit is one and the database limit is one.
- reliability: no reliability event recorded
- notes: The URL in the fourth evidence row is a mis-transcription of the source path and should be re-checked before promotion; the quoted sentence is what the page said, but the slug on the live site is /besplatnyy-hosting/. The persistent free tier is real and unusually generous for a shared host, and the whole finding turns on the phone. Beget also sells a 30-day full-tariff trial to the same restricted audience.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: perpetual
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: '1 SSD ', '1 ', '1 FTP ', ' ', '10 CP ', '25 000 ', ' ' (no adverts), ' ' (no support on free hosting), quoted
  - [2] 2026-10-22: ' , - ' (enter a mobile number and the SMS code), and ' ... ' (may request documents proving the details), quoted
  - [3] 2026-10-22: 'Beget only supports registrations via phone numbers from Russia, Belarus, Ukraine, and Kazakhstan', third-party forum post describing the signup form, reported
  - [4] 2026-10-22: a Russian review site states ' Beget , , ' (free-tariff registration is open to residents of Russia, Belarus, Ukraine and Kazakhstan), reported
- sources:
  - [1] https://beget.com/ru/hosting/free
  - [2] https://beget.com/ru/rulesfree
  - [3] https://www.nodeloc.com/t/topic/41817
  - [4] https://beget-info.ru/besvyatnyy-hosting/
