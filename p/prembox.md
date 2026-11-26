# Prembox

> prembox.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/prembox/ | JSON https://fshy.ajam.dev/api/v1/entity/prembox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Prembox

- `debrid/prembox` | trial-only | evidence documented | binding volume-quota | category multi-hoster (pay-per-package) | tier Packages
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:53.122Z (live) | stale on 2026-12-26
- url https://prembox.com/
- free tier: Registration gives 300 MB of transfer; confirming the e-mail adds 300 MB, for 600 MB total. Files over 99 MB require a purchased package or a promotional code. | unit: mixed | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: Unit is unknown: the amount of the test transfer is not stated on the pages read.
- per-object cap: A 99 MB maximum applies to users who have not bought a package or received a promotional code. | source: [1]
- retention: unverified: not stated | source: [1]
- egress: Packages are valid throughout the year; pay by online payment, text message or cryptocurrency. | metered: yes | free allowance: a free test transfer of unstated size | source: [1]
- identity: email | detail: Registration requires a login, a password, a repeated password and a Cloudflare Turnstile check; the e-mail address field is optional.
- interface: browser
- limits:
  - volume-quota (binding): package-based transfer valid for a year; sizes unverified [1]
- binding note: Transfer is sold in packages, so the package volume is the metered limit.
- interface detail: Web account; browser plugins and JDownloader integration are listed.
- tooling: Browser, JDownloader.
- composes with: Over 40 hosts under one account; operating since 2011 per the home page.
- reliability: No outage observed on the day read.
- notes: Package prices: unverified, no price page readable. A third-party list says pay-per-package, 40+ hosts. No programmatic path found: Web account; browser plugins and JDownloader integration are listed.
- evidence note: First-party home page only; package prices were not on a readable page.
- evidence:
  - [2] 2026-11-03: registration gives a free test transfer and packages valid for a year | capture: sha256:2196571373d66db1e28bba265276283be2f26a9aa97799c64465deaa709b2d31 | quote: Any registered user gets a free transfer for testing and the opportunity to buy additional packages valid throughout the year, at very attractive prices.
  - [2] 2026-11-03: over 40 hosts under one account | capture: sha256:2196571373d66db1e28bba265276283be2f26a9aa97799c64465deaa709b2d31 | quote: # Over 40 most popular hosts - one account
  - [2] 2026-11-03: payment by online payment, text message or cryptocurrency | capture: sha256:2196571373d66db1e28bba265276283be2f26a9aa97799c64465deaa709b2d31 | quote: We offer online payments as well as more anonymous payments - text messages or cryptocurrencies.
  - [2] 2026-11-03: the service has operated since 2011 | capture: sha256:2196571373d66db1e28bba265276283be2f26a9aa97799c64465deaa709b2d31 | quote: We started in 2011.
  - [3] 2026-11-25: the registered free allowance is 300 MB, or 600 MB after e-mail activation | capture: sha256:153ecb5f8c280afc88903decdd7243195b5ab517b663d37c8e877072221e11d6 | quote: Yes, each user receives 300 MB to start just for registration. After activating the account, you get an additional 300 MB, for a total of 600 MB.
  - [1] 2026-11-25: registration includes a free test transfer and paid packages valid for a year | capture: sha256:2196571373d66db1e28bba265276283be2f26a9aa97799c64465deaa709b2d31 | quote: Any registered user gets a free transfer for testing and the opportunity to buy additional packages valid throughout the year, at very attractive prices.
  - [3] 2026-11-25: the vendor lists JDownloader, FDM, IDM and FlashGet as supported downloaders | capture: sha256:153ecb5f8c280afc88903decdd7243195b5ab517b663d37c8e877072221e11d6 | quote: We support all popular downloaders like JDownloader, FDM, IDM, FlashGet.
  - [3] 2026-11-25: purchased transfer is valid 365 days from top-up | capture: sha256:153ecb5f8c280afc88903decdd7243195b5ab517b663d37c8e877072221e11d6 | quote: The transfer from the transfer packages can be used within 365 days from the moment of top-up, after which the value of the given top-up expires.
  - [3] 2026-11-25: files over 99 MB need a purchased package or a promotional code | capture: sha256:153ecb5f8c280afc88903decdd7243195b5ab517b663d37c8e877072221e11d6 | quote: Larger files are only available to users who have purchased any package or received a promotional code.
  - [4] 2026-11-25: registration marks a login as required | capture: sha256:3b2cfd0dd9d72862e6efff6bb6a9a2bf312e2c77340c0aa1dc831db11ae8596b | quote: <label for="usr_login" class="form-label">Login*</label>
  - [4] 2026-11-25: the e-mail field is not marked as required | capture: sha256:3b2cfd0dd9d72862e6efff6bb6a9a2bf312e2c77340c0aa1dc831db11ae8596b | quote: <div class="mb-3"><label for="usr_email" class="form-label">E-mail</label><input id="usr_email" type="mail" name="usr_email" class="form-control" placeholder="E-mail">
- sources:
  - [1] https://prembox.com/
  - [2] https://prembox.com/pricing.html
  - [3] https://prembox.com/faq.html
  - [4] https://prembox.com/register.html
