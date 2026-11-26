# MultiShare

> mul.ir | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mul/ | JSON https://fshy.ajam.dev/api/v1/entity/mul.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MultiShare (مولتی‌شیر, mul.ir)

- `debrid/multishare-ir` | paid-only | evidence documented | binding volume-quota | category premium-link generator (Iran; pay-per-byte balance, magnet/private-tracker torrent, two-month server copy) | tier prepaid-balance
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:47:00.042Z (live) | stale on 2026-12-26
- url https://www.mul.ir/
- free tier: No free allowance is published on the pages read. The model is a prepaid traffic balance drawn at download time ('کسر حجم'). | unit: bytes | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The balance is topped up from the account panel; the top-up page and its price were not read.
- per-object cap: not stated on the pages read. | source: [1]
- retention: Files can be stored on MultiShare's servers for 30 days ('امکان ذخیره فایل ها برای مدت ۳۰ روز در سرورهای ما وجود دارد'). Converted links themselves do not expire while the source host still holds the file. | source: [2] | note: Two months is stated in months, not days; no day count is published.
- egress: Each download debits the balance by exactly the downloaded amount, multiplied by the host's coefficient where one exists ('برخی از هاست ها دارای ضریب هستند'). Nothing is debited until the download actually starts. | metered: yes | source: [1]
- identity: email | detail: An account is required before download ('برای دانلود نیاز به حساب کاربری دارید'); the registration page was not opened, so email is inferred from the panel.
- interface: unknown
- limits:
  - volume-quota (binding): prepaid byte balance, debited per download and multiplied by the host coefficient [1]
- limits note: The FAQ warns that using a VPN or proxy corrupts the debit ('استفاده از هرگونه میانجی مانند وی پی ان یا پراکسی باعث اختلال در کسر حجم می شود'), so the service assumes an Iranian address.
- binding note: This is a pay-per-byte service: the balance is the only ceiling, and the host coefficient is what makes the real cost per GB differ from the nominal one. 1 TiB/month is priced by top-up, not by a plan.
- interface detail: A web form takes one link per line; an account is required before a download. No API, WebDAV or CLI documentation was found.
- tooling: Browser only on the pages read. No rclone backend, SDK or public API listed.
- composes with: Useful for a one-off foreign file rather than a monthly plan: payment is per downloaded byte, and the fetched copy lives on an Iranian server for two months, which is the part that makes re-download cheap on domestic traffic.
- reliability: Host coefficients drain the balance faster than the byte count, and the FAQ warns that a VPN or proxy breaks the debit calculation, so a client behind any tunnel can be charged wrongly.
- notes: Third native Iranian service and the only one among debrid providers with a pay-per-byte model instead of a monthly plan. Slug carries the -ir suffix because 'multishare' alone is also a generic product name; the vendor's own domain is mul.ir.
- evidence note: The host list, the two-month retention, the debit rule and the coefficient rule were read on mul.ir and its FAQ. The price per byte and the top-up options were not read.
- evidence:
  - [2] 2026-10-23: Supported hosts (FileFactory, Rapidgator, NitroFlare, Icerbox, MediaFire, Mega, Uptobox, Turbobit, Google Drive, Dropbox and more), magnet/private-tracker conversion, and two-month server storage in the page description
  - [1] 2026-10-23: Links do not expire while the source holds the file; the balance is debited only when a download starts, by the downloaded amount, multiplied by the host coefficient; VPN/proxy corrupts the debit
  - [2] 2026-11-25: the home page now states 30 days of server-side file storage | capture: sha256:2597d332825435f45af34cda1c758f1b496083d6df383ab5d996d0e1fbd150a5 | quote: البته امکان ذخیره فایل ها برای مدت ۳۰ روز در سرورهای ما وجود دارد که از بخش مدیریت فایل می توانید اقدام کنید.
  - [1] 2026-11-25: converted links do not expire while the source host holds the file | capture: sha256:e4db2ce290ced0e7b25acbdfe9c169d61c269c3648fd7db99c7b174f514ed64e | quote: این لینک ها مدت اعتبار ندارند و تا هر زمانی که در هاست مبدا وجود داشته باشند می توان از آنها استفاده نمود.
  - [1] 2026-11-25: nothing is debited before download starts, and the debit equals the downloaded amount | capture: sha256:e4db2ce290ced0e7b25acbdfe9c169d61c269c3648fd7db99c7b174f514ed64e | quote: خیر، تا وقتی چیزی دانلود نکنید از حسابتان کم نمی شود و دقیقا به مقدار دانلودی از حسابتان کم می شود.
  - [1] 2026-11-25: the FAQ states a limit of 12 concurrent files and 100 open server connections | capture: sha256:e4db2ce290ced0e7b25acbdfe9c169d61c269c3648fd7db99c7b174f514ed64e | quote: شما در آن واحد می توانید حد اكثر در حال دانلود 12 فایل (100 كانكشن باز به سرور) باشید
  - [2] 2026-11-25: the generator takes one link per line and requires an account to download | capture: sha256:2597d332825435f45af34cda1c758f1b496083d6df383ab5d996d0e1fbd150a5 | quote: در هر خط یک لینک مجزا وارد نمایید و سپس بر روی تبدیل لینک کلیک کنید. برای دانلود نیاز به حساب کابری دارید.
- sources:
  - [1] https://www.mul.ir/faq
  - [2] https://www.mul.ir/
