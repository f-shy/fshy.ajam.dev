# IHC

> ihc.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ihc/ | JSON https://fshy.ajam.dev/api/v1/entity/ihc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IHC

- `compute/ihc` | trial-only | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T10:36:21.696Z (live) | stale on 2026-12-05
- url https://www.ihc.ru/vps-test.html
- free tier: Three days of any VPS tariff free, but activation requires topping up the account by at least RUB 100 first: the page states the money is not spent and does not disappear, that it can be withdrawn or used for another order after the trial, and that the server activates automatically once the balance is funded. Individuals and legal entities both qualify, the second with a scanned application stamped and signed by the company head. The test server is suspended after three days. The cheapest tariff is 1 CPU, 1 GB RAM and 20 GB SSD at RUB 380 a month, or RUB 3,800 a year presented as RUB 317 a month, with extra RAM at RUB 6 per GB a month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: deposit-gated-trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unlimited traffic is included in every tariff under a fair-use policy: the network port is 100 Mbit/s, and once traffic reaches 20 000 GB in a billing month the speed is limited to 10 Mbit/s until the month ends; full speed can be restored for RUB 157.50 per 1000 GB. | metered: yes | free allowance: 20 000 GB per month at 100 Mbit/s, then 10 Mbit/s until the end of the billing month | price per TB: RUB 157.50 per 1000 GB (restores full speed; it is not per-byte billing) | source: [2]
- identity: card
- interface: sftp, ssh, ftp
- limits:
  - volume-quota (binding): Three days and a RUB 100 refundable deposit are the whole offer, so nothing about it reaches the scale; on the paid side the same tariff is RUB 380 a month for 1 vCPU and 1 GiB, which is dearer per core than AdminVPS or WebHOST1 and cheaper only in the RAM add-on at RUB 6 a GB a month. [1]
- limits note: Three days and a RUB 100 refundable deposit are the whole offer, so nothing about it reaches the scale; on the paid side the same tariff is RUB 380 a month for 1 vCPU and 1 GiB, which is dearer per core than AdminVPS or WebHOST1 and cheaper only in the RAM add-on at RUB 6 a GB a month.
- binding note: the same as limits note
- interface detail: SFTP over SSH on port 22 and FTP with the system user's credentials; ispmanager web control panel available
- tooling: an FTP client such as FileZilla, or SFTP; ispmanager control panel; the page names no CLI or SDK
- composes with: A RUB 100 deposit that is withdrawable makes this the cheapest test of a Russian Tier III host found among evaluated providers, and the RUB 6 per GB monthly RAM price composes with the cheapest shape at AdminVPS: adding 8 GB to a RUB 250 plan costs less than buying a bigger plan anywhere in this set.
- reliability: no reliability event recorded
- notes: The trial is honest about its gate, which is unusual in this set: the page says the deposit is refundable before the reader has to ask. Arithmetic: 380 x 12 = 4,560 against the RUB 3,800 annual price, so the annual term is a 17 percent discount; 3,800 / 12 = 316.7. Not established: the accepted payment methods, which the page does not name, and therefore whether a foreign card reaches the deposit.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: deposit-gated-trial
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: 'To activate the trial you need to top up the account by at least RUB 100: the money will not be charged and will not disappear. You will be able to withdraw it after the free test ends', quoted and translated
  - [1] 2026-10-22: after three days the test is suspended, and the funds can be withdrawn or used for any other order; legal entities supply a stamped application, quoted and translated
  - [1] 2026-10-22: cheapest tariff ssdVPS:1 at RUB 380 a month, RUB 3,800 a year or RUB 317 a month annually, with 1 CPU, 1 GB RAM and 20 GB SSD and extra RAM at RUB 6 per GB, quoted
  - [2] 2026-11-04: the page documents SFTP over SSH on port 22 | capture: sha256:a2a56d1f44db7132c5aee6955f0dd82879fd9b337e6be1514a30dbe183759789 | quote: Для большей безопасности рекомендуем использовать SFTP поверх SSH (порт 22).
  - [2] 2026-11-04: the page names FileZilla as the FTP client | capture: sha256:a2a56d1f44db7132c5aee6955f0dd82879fd9b337e6be1514a30dbe183759789 | quote: Вы можете подключиться к серверу по FTP через клиент (например, FileZilla)
  - [2] 2026-11-04: traffic is unmetered to 20 000 GB a month at 100 Mbit/s, then limited to 10 Mbit/s until month end, restorable for RUB 157.50 per 1000 GB | capture: sha256:a2a56d1f44db7132c5aee6955f0dd82879fd9b337e6be1514a30dbe183759789 | quote: Пропускная способность сети на сервере 100 Мбит/с. При достижении объема трафика 20 000 ГБ скорость ограничивается до 10 Мбит/с до конца расчетного месяца. Скорость может быть восстановлена за 157.50 ₽ (1000 ГБ).
  - [2] 2026-11-04: the page documents FTP access with the system user's credentials | capture: sha256:a2a56d1f44db7132c5aee6955f0dd82879fd9b337e6be1514a30dbe183759789 | quote: Вы можете подключиться к серверу по FTP через клиент (например, FileZilla) по IP-адресу вашего VPS, используя учетные данные системного пользователя.
- sources:
  - [1] https://www.ihc.ru/vps-test.html
  - [2] https://www.ihc.ru/vps.html
