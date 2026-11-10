# Yandex

> yandex.com | Email, Storage, Netdisk and pan; 6 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yandex/ | JSON https://fshy.ajam.dev/api/v1/entity/yandex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Yandex 360

- `email/yandex-360` | paid-only | evidence documented | binding write-gated | category mailbox
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T05:33:30.051Z (live) | stale on 2026-12-05
- url https://360.yandex.com/business/tariff/
- free tier: free personal mail at a Yandex address only; the free version of Yandex 360 for Business, which carried mail on a custom domain, is no longer available as of December 8, 2025, except for non-profit organizations and charities | unit: none | metered on: none | read on: 2026-10-31 | source: [1]
- per-object cap: not stated
- retention: not stated | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: any-phone | detail: a Yandex ID: name and surname, a username, a password, and a mobile phone number confirmed by an SMS code; the registration help names no country
- interface: unknown
- limits:
  - write-gated (binding): a custom domain requires a Yandex 360 for Business plan, from USD 3.99 per employee per month on Basic as 360.yandex.com lists it [1]
- limits note: reported by third-party posts that quote a notice sent to organizations without a plan, and stated on no first-party page read: IMAP, SMTP and POP3 become unavailable without a Yandex 360 plan from the date in the notice, June 29 in the first notice quoted and later dates in later notices, leaving webmail and the mobile app; the same posts report that personal mailboxes are not affected, and whether non-profit organizations that keep the services free are affected is unverified
- interface detail: webmail and the mobile apps, and IMAP at imap.yandex.com (port 993, SSL) and SMTP at smtp.yandex.com (port 465, SSL; port 587 for a connection opened without encryption) with an app password, for personal mailboxes and for organization mailboxes where an administrator enables the protocols; the custom-domain feature is a business-plan SKU
- tooling: web mail and the official mobile app; an organization admin can enable IMAP for email clients under Mail settings
- composes with: a mailbox rather than a sender, and the custom-domain feature that would make it useful moved behind the paid tier.
- reliability: an organization that used the free version moves to a paid plan in stages: it keeps the features free until it receives an email 7 days before its first payment, and if it does not pay it stays in view-only mode, where its data is kept and readable and nothing new can be added
- notes: Non-profit organizations and charities keep all Yandex 360 for Business services free of charge, so mail on a custom domain stays free on that institutional route.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: the business tariffs are the ones that carry a custom domain; the personal tier does not
  - [2] 2026-10-30: the free business version that carried domain mail ended on December 8, 2025 | capture: sha256:8783018fcedf787c4122c182fcec3570aaa149c35e59626f0299c70e9de056c3 | quote: As of December 8, 2025, the free version of Yandex 360 for Business is no longer available.
  - [3] 2026-10-30: registration confirms a mobile number by SMS | capture: sha256:33485a7272d44fa4e6fbe26c36663f9d6bfa171b1eadcd9f1b70334e4eb336d2 | quote: Enter the code from the SMS to confirm your phone number.
  - [3] 2026-10-30: the registration step asks for a mobile number without naming a country | capture: sha256:33485a7272d44fa4e6fbe26c36663f9d6bfa171b1eadcd9f1b70334e4eb336d2 | quote: Provide your mobile phone number. You can use this number to restore your password and receive notifications.
  - [3] 2026-10-30: registration asks for a mobile phone number | capture: sha256:33485a7272d44fa4e6fbe26c36663f9d6bfa171b1eadcd9f1b70334e4eb336d2 | quote: Provide your mobile phone number. You can use this number to restore your password and receive notifications.
  - [2] 2026-10-30: unpaid former free organizations drop to view-only mode | capture: sha256:8783018fcedf787c4122c182fcec3570aaa149c35e59626f0299c70e9de056c3 | quote: If you don't pay for Yandex 360 after receiving the email, the services will remain available in view-only mode.
  - [4] 2026-10-30: corporate mail is reached through the web interface, the app, or email clients once protocols are enabled | capture: sha256:7dd7c8616cb939f93d8953fd7178122b6e999e48717bc191a1df97c0966a7308 | quote: If the web interface and application don't meet the requirements of your organization, you can work with corporate mail via email clients.
  - [2] 2026-10-30: non-profit organizations and charities keep the business services free | capture: sha256:8783018fcedf787c4122c182fcec3570aaa149c35e59626f0299c70e9de056c3 | quote: The changes to the terms won't affect non-profit organizations and charities. They can keep using all Yandex 360 for Business services free of charge.
  - [1] 2026-10-30: business plans are prepaid from a balance or a linked bank card | capture: sha256:fa6a0062b4ef0979ed7600ea782804387a1ba750b3424cd586555ac3d7c7e0ba | quote: Yandex 360 for Business is a prepaid service. You can top up your balance manually or link a bank card for automatic top-ups.
  - [5] 2026-10-30: addresses on an own domain need Yandex 360 for Business | capture: sha256:d36496f564632c386f055d33ea4d4846b547a873ab3c87a382197b06b6c08d86 | quote: This option is only available for personal mailboxes. If you have a business and want custom email addresses on your own domain, get Yandex 360 for Business.
  - [2] 2026-10-30: no free business tier remains for a new organization | capture: sha256:8783018fcedf787c4122c182fcec3570aaa149c35e59626f0299c70e9de056c3 | quote: As of December 8, 2025, the free version of Yandex 360 for Business is no longer available.
  - [1] 2026-10-31: Basic, the lowest-priced Yandex 360 for Business plan on the page, costs USD 3.99 per employee per month | capture: sha256:fa6a0062b4ef0979ed7600ea782804387a1ba750b3424cd586555ac3d7c7e0ba | quote: Basic $3.99 /month per employee
  - [1] 2026-10-31: the plan comparison marks Your domain as enabled in its first column, Basic | capture: sha256:68c149751dc8b7eba5788b7f443312e16a82c5cc4d0172da6df4a8e98d3816bb | quote: <span>Your domain</span></div><div class="rowValue_V4JwbeEX3axa06OWx45t"><div class="valueIcon_WuTdmORcmcMx8vjAdhJ7 valueIcon--enabled_XXpI6xgyZTkeGl9FHV35"></div></div>
  - [6] 2026-10-31: a Yandex 360 for Business plan carries mail on an own domain | capture: sha256:f78688867a6d8c5d586752912f423d95fcfab7afe03b2d7344cd0752cc63dc47 | quote: After you buy a Yandex 360 for Business plan, you immediately get everything you need to use email addresses on your own domain and access them on the web, in the iOS and Android apps, and via third-party email clients.
  - [7] 2026-10-31: the Basic plan includes business email on company-branded addresses | capture: sha256:db7d2b06c5781c9e2c549de09bbdfde4a21e81568ed4088893a21dd9c1b7aefb | quote: [Business email](https://yandex.com/support/mail-business/index.html): Create professional email addresses reflecting your company's brand.
  - [1] 2026-10-31: the free tier's source page, read on 2026-10-31, offers the business plans as a prepaid service with no free plan | capture: sha256:fa6a0062b4ef0979ed7600ea782804387a1ba750b3424cd586555ac3d7c7e0ba | quote: Yandex 360 for Business is a prepaid service. You can top up your balance manually or link a bank card for automatic top-ups.
  - [8] 2026-10-31: a personal mailbox at a Yandex address is free | capture: sha256:3f525cc025739c274c87f8827801e32d5b5e6724b7ec3296d5d360feea4a6d20 | quote: Your free mailbox is now all set and ready to go!
  - [1] 2026-10-31: the business offer is three plans for organisations, each carrying corporate email | capture: sha256:fa6a0062b4ef0979ed7600ea782804387a1ba750b3424cd586555ac3d7c7e0ba | quote: Choose one of three available plans for organisations. Each plan includes our corporate email, messenger, calendar, video conferencing, cloud-based file storage, document editor, and newsletter tool.
  - [2] 2026-11-02: organizations move to paid plans in stages, each receiving an email 7 days before its first payment and keeping the features free until then | capture: sha256:2a64021d6546e3fa0ce70461ac6214dcedbb7b4f5f77eb3a31ec25c8d2fdf955 | quote: We're transitioning our clients to paid plans gradually and in stages. Each client receives an email 7 days before the first payment needs to be made. The Yandex 360 features will remain free for you until you receive that email.
  - [2] 2026-11-02: the free version of Yandex 360 for Business has been unavailable since December 8, 2025 | capture: sha256:2a64021d6546e3fa0ce70461ac6214dcedbb7b4f5f77eb3a31ec25c8d2fdf955 | quote: As of December 8, 2025, the free version of Yandex 360 for Business is no longer available.
  - [2] 2026-11-02: an organization that does not pay after the email stays in view-only mode | capture: sha256:2a64021d6546e3fa0ce70461ac6214dcedbb7b4f5f77eb3a31ec25c8d2fdf955 | quote: If you don't pay for Yandex 360 after receiving the email, the services will remain available in view-only mode
  - [2] 2026-11-02: view-only mode reads existing data and adds nothing new | capture: sha256:2a64021d6546e3fa0ce70461ac6214dcedbb7b4f5f77eb3a31ec25c8d2fdf955 | quote: In view-only mode, you can access the services but can't add new data.
  - [9] 2026-11-02: Yandex Mail documents client access over IMAP and SMTP, for which the schema has no term, and the page documents no WebDAV access to mail | capture: sha256:c15d099469261da9921db6beec43121d0de90149eb9c7a9b93d5055b12bd35ee | quote: You can configure any client that supports the IMAP and SMTP protocols to work with Yandex Mail.
  - [9] 2026-11-02:  | capture: sha256:c15d099469261da9921db6beec43121d0de90149eb9c7a9b93d5055b12bd35ee | quote: Port: `465`. If the email client initiates a connection without encryption, port `587` is used.
  - [9] 2026-11-02: IMAP is at imap.yandex.com on port 993 with SSL | capture: sha256:c15d099469261da9921db6beec43121d0de90149eb9c7a9b93d5055b12bd35ee | quote: Mail server address: `imap.yandex.com` (or `imap.ya.ru` if you're not in Russia). - Connection security: `SSL`. - Port: `993`.
  - [10] 2026-11-02: a third-party post quotes the notice: from June 29, IMAP, SMTP and POP3 are unavailable without a Yandex 360 plan to an organization with no plan | capture: sha256:afdce735428b5874fe7aa66445d0900362856a14c72895eba7168ed8fc2d47ad | quote: С 29 июня работа с Яндекс Почтой по протоколам IMAP, SMTP и POP3 будет недоступна без тарифа Яндекс 360 У вашей организации не подключён тариф. Поэтому сотрудники не смогут работать с почтой в Microsoft Outlook, Mozilla Thunderbird и других программах.
  - [10] 2026-11-02: a third-party post reports that the mail client stopped on 3 July 2026 for the domains left unpaid | capture: sha256:afdce735428b5874fe7aa66445d0900362856a14c72895eba7168ed8fc2d47ad | quote: UPD 03.07.2026: Сегодня почтовый клиент отрубился на тех доменах, что я решил не оплачивать.
  - [11] 2026-11-02: a third-party summary reports that the restriction concerns organizations with domains on the free plan and not personal mailboxes, where app-password protocol access keeps working | capture: sha256:6a1e5722e5cc812c5fa3347b2d13d41698534209d6a9ea2b3cd5ea1cb306f0b9 | quote: ограничение касается именно организаций с доменами на бесплатном тарифе — личных ящиков @yandex.ru оно не коснулось, там протокольный доступ по паролю приложения продолжает работать
  - [11] 2026-11-02: a third-party summary reports that the cut-off comes in waves with different dates in different organizations' notices, from late June to August | capture: sha256:6a1e5722e5cc812c5fa3347b2d13d41698534209d6a9ea2b3cd5ea1cb306f0b9 | quote: отключение идёт волнами, и в уведомлениях у разных организаций стоят разные даты — от конца июня до августа
  - [12] 2026-11-02: a third-party author reports that Yandex support confirmed the cut-off only for commercial organizations that have not connected a plan | capture: sha256:0e8344b4ad3b3df4d8fcfdf824d3941793767e3b3fa483852fa4e48095027b43 | quote: после 29 числа сервис действительно отключит возможность использовать протоколы IMAP, SMTP и POP3… но только для тех коммерческих организаций, которые еще не подключили тариф
  - [2] 2026-11-02: the FAQ was captured on 2026-11-02 and still states the free business version ended on December 8, 2025 | capture: sha256:2a64021d6546e3fa0ce70461ac6214dcedbb7b4f5f77eb3a31ec25c8d2fdf955 | quote: As of December 8, 2025, the free version of Yandex 360 for Business is no longer available.
  - [2] 2026-11-02: non-profit organizations and charities keep the business services free | capture: sha256:2a64021d6546e3fa0ce70461ac6214dcedbb7b4f5f77eb3a31ec25c8d2fdf955 | quote: The changes to the terms won't affect non-profit organizations and charities. They can keep using all Yandex 360 for Business services free of charge.
  - [2] 2026-11-04: the free custom-domain version stays withdrawn, unchanged | capture: sha256:8783018fcedf787c4122c182fcec3570aaa149c35e59626f0299c70e9de056c3 | quote: As of December 8, 2025, the free version of Yandex 360 for Business is no longer available.
- sources:
  - [1] https://360.yandex.com/business/tariff/
  - [2] https://yandex.com/support/yandex-360/business/purchase/en/troubleshooting/faq-disable-free-version
  - [3] https://yandex.com/support/yandex-360/customers/mail/en/reg
  - [4] https://yandex.com/support/yandex-360/business/admin/en/mail/email-clients/
  - [5] https://360.yandex.com/premium-plans/
  - [6] https://360.yandex.com/business/domain-mail
  - [7] https://yandex.com/support/yandex-360/business/purchase/en/plans/payment-plans
  - [8] https://360.yandex.com/mail
  - [9] https://yandex.com/support/yandex-360/customers/mail/en/mail-clients/others
  - [10] https://habr.com/ru/news/1042832/
  - [11] https://habr.com/ru/articles/1063226/
  - [12] https://habr.com/ru/articles/1053602/

## Yandex 'unlimited photo storage' (auto-upload)

- `storage/yandex-unlimited-photo-storage` | fails-quota | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://yandex.com/promo/disk/unlim
- free tier: unlimited photos/videos, but only with an active paid Yandex 360 plan; free accounts have those files counted against the 5 GB | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free view/download from the web and app | metered: no
- identity: email
- interface: rest, rclone
- limits note: RAW DNG files are excluded and count against quota; photos in unlimited storage do not sync to desktop; uploads happen only from the mobile client
- interface detail: wrapper-only
- tooling: Yandex Disk REST/API is the same one rclone uses, but the unlimited bucket is only reachable via the mobile auto-upload path, not the upload API
- composes with: Does not multiply. The 'unlimited' is a plan benefit, not a free-tier property; lapses back to metered when the plan ends.
- reliability: Reading it as a free store is a trap: without a paid plan the media occupies quota and over-quota disks get blocked at 44 days and wiped at 90.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: unlimited photos/videos, but only with an active paid Yandex 360 plan; free accounts have those files counted against the 5 GB
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Unlimited photo and video auto-uploads are only available with a Yandex 360 plan'
  - [1] 2026-10-21: 'If you don't have an active Yandex 360 plan, the photos and videos uploaded to Yandex Disk from your phone take up space'
- sources:
  - [1] https://mobi.yandex.com/support/yandex-360/customers/disk/web/en/enlarge/manage-disk-space
  - [2] https://www.yandex.com/support/yandex-360/customers/disk/web/en/media-upload

## Yandex Disk (+ Yandex 360)

- `storage/yandex-disk` | fails-quota | evidence reported | binding retention-clamped | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://disk.yandex.com
- free tier: 5 GB free per account (shared with Yandex Mail attachments); paid 200 GB-2 TB from 319-699 RUB/mo | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Enforcement tightened in 2026: desktop sync became paid on 3 June 2026, over-quota disks are restricted after 44 days and files deleted 90 days after that; data loss risk is real for over-quota free accounts. | days: 44 | source: [1] | note: not stated
- egress: Free. Download links and public share URLs are unmetered, no per-GB egress line in the pricing. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - retention-clamped (binding): deleted 90 days [1]
- limits note: monthly upload limit = 2x plan capacity (3x on Pro); free tier is now browser/mobile only
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: rclone backend 'yandex' (rclone/rclone backend/yandex/yandex.go, in core); REST API at cloud-api.yandex.net/v1/disk; official REST docs
- composes with: 5 GB x unlimited free Yandex accounts = 100 accounts for 500 GB. Weak per-identity yield, and 2026 policy tightening makes mass-account use the failure mode.
- reliability: Enforcement tightened in 2026: desktop sync became paid on 3 June 2026, over-quota disks are restricted after 44 days and files deleted 90 days after that; data loss risk is real for over-quota free accounts.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB free per account (shared with Yandex Mail attachments); paid 200 GB-2 TB from 319-699 RUB/mo
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'By default, users without a plan get 5 GB of storage space'
  - [2] 2026-10-21: 'с 3 июня отключает облачную синхронизацию файлов ... для пользователей версий для компьютеров, использующих сервис бесплатно'; 'через 44 дня он будет заблокирован, а еще через 90 дней все файлы ... удалены'
  - [3] 2026-10-21: probe: GET -> 401 with 'access-control-allow-headers: ... X-Yandex360-Token' (token API live); GET /v1/disk/public/resources?public_key=... -> {"error":"DiskNotFoundError"} (public REST path live)
- sources:
  - [1] https://yandex.com/support/yandex-360/customers/disk/web/en/enlarge/disk-space
  - [2] https://www.fontanka.ru/2026/05/20/76431223/
  - [3] https://cloud-api.yandex.net/v1/disk/

## Yandex Disk (disk.yandex.com)

- `netdisk-pan/yandex-disk` | fails-quota | evidence documented | binding per-object-cap | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T00:21:08.722Z (live) | stale on 2026-11-26
- url https://disk.yandex.com/
- free tier: 5 GB of storage for an account with no plan, shared with Yandex Mail | unit: GB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 1 GB per file without a Yandex 360 plan; 50 GB with any plan | bytes: 1000000000 | source: [2]
- retention: files persist until deleted; deleted files go to Trash for a period, but a file deleted over WebDAV is erased permanently | source: [3]
- egress: no published egress meter; the reader's speed is whatever the service grants, and WebDAV access now requires a paid plan | metered: no | source: [3]
- identity: any-phone
- interface: rest, webdav
- limits:
  - per-object-cap (binding): 1 GB per file on the free tier [2]
  - write-gated: WebDAV access requires a Yandex 360 plan from 2026-06-22 [3]
- binding note: 5 GB total with a 1 GB per-file cap is three orders of magnitude below the working set, and the free WebDAV path that made it mountable closed in June 2026.
- tooling: a documented REST API and a WebDAV endpoint; WebDAV needs an app password rather than the account password, and from 2026-06-22 it needs a Yandex 360 plan
- composes with: a 5 GB tier cannot hold anything at the scale, so its only role is as a small always-available store for the state of a bridge
- reliability: The free WebDAV path closed on 2026-06-22: the help page now states that WebDAV access requires a Yandex 360 plan. The REST API remains documented but the free tier's role is 5 GB.
- notes: The fact that changed is WebDAV: the help page dated the closure to 2026-06-22, so a bridge that mounted Yandex over WebDAV stopped working on a published date rather than silently.
- extras:
  - access_mode: registration-gated
  - webdav_requires_plan_from: 2026-06-22
  - free_webdav: no
- evidence:
  - [2] 2026-10-22: 'Maximum size of a single file for uploading to Yandex Disk: Without a Yandex 360 plan — 1 GB. With any Yandex 360 plan — 50 GB.'
  - [3] 2026-10-22: 'Starting June 22, 2026, WebDAV access requires a Yandex 360 plan', and an app password is required rather than the account password
  - [1] 2026-10-22: 'By default, users without a plan get 5 GB of storage space', and Yandex Mail shares that same pool with Disk
  - [1] 2026-11-03: an account with no plan still gets 5 GB | capture: sha256:f59a9b54726ec036cec2c7d66c377bef2367c6d32d80266d933602416741674e | quote: By default, users without a plan get 5 GB of storage space.
  - [2] 2026-11-03: the per-file upload cap without a Yandex 360 plan is 1 GB | capture: sha256:6daf0e57f31f8c03e10c4d9e7d8fbbe56431f469a9dd962a0c2d01765ad93cb3 | quote: make sure the file size doesn't exceed 1 GB
  - [3] 2026-11-03: WebDAV access requires a Yandex 360 plan from 2026-06-22 | capture: sha256:d904057f23c14258cf3653a5fd0339c792f1485ce3b992138437754c8b19ffc4 | quote: Starting June 22, 2026, WebDAV access requires a
- sources:
  - [1] https://yandex.com/support/yandex-360/customers/disk/web/en/enlarge/disk-space
  - [2] https://yandex.com/support/yandex-360/customers/disk/web/en/uploading.md
  - [3] https://yandex.com/support/yandex-360/customers/disk/web/en/webdav

## yandex disk / yandex photos

- `storage/yandex-disk-yandex-photos` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://disk.yandex.com/
- free tier: none reachable: 5 GB free. The 'unlimited' photo auto-upload is gated behind Yandex 360 paid plans and is not available on free. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 5 GB free. The 'unlimited' photo auto-upload is gated behind Yandex 360 paid plans and is not available on free.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 GB free. The 'unlimited' photo auto-upload is gated behind Yandex 360 paid plans and is not available on free.
  - [2] 2026-10-21: cited as the basis of the rejection: 5 GB free. The 'unlimited' photo auto-upload is gated behind Yandex 360 paid plans and is not available on free.
- sources:
  - [1] https://disk.yandex.com/
  - [2] https://yandex.com/support/yandex-360/customers/disk/app/android/en/autoupload/setup

## Yandex Mail — 5 GB pooled with Disk, 1 GB attachment

- `storage/yandex-mail-5-gb-pooled-with-disk-1-gb-attachment` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://360.yandex.com/mail/
- free tier: Yandex's own docs: "By default, users without a plan get 5 GB of storage space." Mail and Disk now share one pool: "Emails and attachments in Yandex Mail now share storage with files on Yandex Disk." Attachment cap: "The maximum attachment size is 1 GB. You can add larger files to messages only if you have a Yandex 360 plan." | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 1 GB | bytes: 1000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered; mailbox service. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 1 GB [1]
- limits note: Per-object-cap 1 GB attachment (docs) but SMTP SIZE says 51 MiB. The 1 GB path is a Disk-upload link, not an SMTP attachment, so again link-vs-storage. Pool is 5 GB shared with Disk. Hard retention decay ladder documented: full -> attach >25 MB blocked; 44 days -> cannot send/read; 90 days -> Disk may be cleared, files unrecoverable.
- interface detail: rest
- tooling: IMAP probe-verified: `imap.yandex.com:993` -> `* OK Yandex IMAP4rev1 at imap.yandex.ru:993 ready` / `* CAPABILITY IMAP4rev1 CHILDREN UNSELECT LITERAL+ NAMESPACE XLIST UIDPLUS ENABLE ID AUTH=PLAIN AUTH=XOAUTH2 MOVE`. SMTP: `250-SIZE 53477376` = 51 MiB.
- composes with: 5 GB × N accounts. The 1 GB attachment cap makes it look generous per message, but the pool is 5 GB, so one attachment is 20% of the account.
- reliability: The most explicit data-loss ladder of any provider here. 90 days over quota and Disk is wiped. Never use as primary copy.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Yandex's own docs: "By default, users without a plan get 5 GB of storage space." Mail and Disk now share one pool: "Emails and attachments in Yandex Mail now share storage with files on Yandex Disk." Attachment cap: "The maximum attachment size is 1 GB. You can add larger files to messages only if you have a Yandex 360 plan."
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: "users without a plan get 5 GB"
  - [2] 2026-10-21: 1 GB attachment maximum
  - withheld 2026-10-21: probe: smtp.yandex.com:587 -> 250-SIZE 53477376; probe: imap.yandex.com:993 -> * OK Yandex IMAP4rev1 ready
- sources:
  - [1] https://yandex.com/support/yandex-360/customers/disk/web/en/enlarge/disk-space
  - [2] https://yandex.com/support/yandex-360/customers/mail/en/web/letter/attachments
