# JDownloader 2

> jdownloader.org | Debrid; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jdownloader/ | JSON https://fshy.ajam.dev/api/v1/entity/jdownloader.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JDownloader 2

- `debrid/jdownloader` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category open-source multi-hoster download manager and link decrypter (desktop/headless) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://jdownloader.org/download/index
- price USD 0
- free tier: 'JDownloader is a free, open-source download management tool with a huge community that makes downloading as easy and fast as it should be.' The software and its hoster/decrypter plugins are free; what it needs is a machine with Java and disk space. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No hosted first-party instance exists. The vendor offers desktop installers for Windows, Linux and macOS plus a multi-OS JAR, and every remote path points back at a JD installation the caller runs.
- per-object cap: not applicable to the tool: the largest object is whatever the target host serves. JD writes to local disk, so the practical cap is the device's free space. | source: [1]
- retention: not applicable: JD downloads to local storage it does not own. Nothing is retained server-side. | source: [1]
- egress: The transfer runs between the JD host and the file host. JD meters nothing and resells nothing. | metered: no | free allowance: none: no service-side bytes | source: [1]
- identity: anonymous | detail: No account needed to install and use JDownloader. A MyJDownloader account is optional and only needed for remote control. The support FAQ states: 'Do I need to register an account to use JDownloader? No! You only need an account when you use MyJDownloader which is completely optional!'
- interface: cli, rest
- limits:
  - request-rate: core caps simultaneous connections per file at 20; board staff describe raising it with domain rules [2]
  - write-gated: captchas and host wait timers must be solved per download unless a premium account is attached [3]
- limits note: Every cap that matters is imposed by the target host, not by JD. The tool adds a 20-connection ceiling per file and a default concurrency limit.
- binding note: No JD-side quota binds at 1 TiB/month; the host's free-tier limits and the absence of a local machine bind first. Public instances exist but are private containers behind credentials (see evidence), so they are not a route.
- interface detail: GUI and headless (jar) modes; a Click'n'Load listener on port 9666 that accepts container posts from a browser; and a 'Deprecated API' the MyJD docs say can be enabled in Advanced Options to bypass the connection server and reach JD directly.
- tooling: First-party installers and JAR; MyJDownloader for remote control; Docker images by third parties (jlesage/docker-jdownloader-2, junkerderprovinz/jdownloader) that expose the GUI over VNC in a browser. A wrapper needs a machine to install on, which is not available.
- composes with: JD is the decrypter layer of last resort: one tool covers roughly a hundred hosters and several hundred container/decrypter plugins, so it composes with any storage or debrid service that hands it links.
- reliability: Public web instances found in the wild are other people's containers: one answered HTTP 200 with a 'Credentials needed' gate, one answered 530, one 502. They are not a service, they disappear without notice, and using one puts the links on a stranger's disk.
- notes: This is the tool the debrid question is usually answered with, and it fails on the install requirement. The three public instances were found by search and probed as ordinary web pages; no login was attempted on any of them. Their existence shows the pattern (docker + KasmVNC + credentials), not a public service.
- evidence note: The vendor page, the board thread and three probes are in hand. A measured rung needs a JD install downloading a real link, which needs a machine that is not available.
- self hosted: yes
- extras:
  - public_instance_survey: 3 found by search, 1 up behind a credential gate, 2 dead; 0 accepted anonymous input
  - hoster_plugin_count: unverified: the vendor feature page was not readable today; a third-party page claims ~110 hosters and 300+ decrypters
  - probe_records: scratch (removed); scratch (removed); scratch (removed)
- evidence:
  - [1] 2026-10-23: 'JDownloader is a free, open-source download management tool'; installers for Windows/Linux/macOS plus a MULTIOS JAR, i.e. an install, not a hosted service
  - [4] 2026-10-23: the 'Deprecated API' can bypass the MyJD connection server and reach JD directly; JD is the device the API talks to
  - probe:https://wojd.goip.de/ 2026-10-23: a public JDownloader web instance answers HTTP 200, 17403 bytes, sha256 4fb03946a848be39dea877b14593fe69f55a0f54c332de5cc4fca20744a94979, and its body is 'Credentials needed / Please enter the credentials to connect.'
  - probe:https://jdownloader.markodj.com/ 2026-10-23: second public instance is down: HTTP 530, 7660 bytes, sha256 f97e88f5ca4fe49388a454ddfce24f2ed91abda9b6ff29e3e3c6be063086c029, retry-after 120
  - probe:https://jdownloader.stehuenet.selfhost.co/ 2026-10-23: third public instance is down: HTTP 502, 154 bytes, sha256 bf4d0c2fe5252a3e32908499c90a4da5f961c7a7d989c5ef37b406d145929f1b
  - [2] 2026-10-23: third-party board statement that 20 chunks per file is the core limit
- sources:
  - [1] https://jdownloader.org/download/index
  - [2] https://board.jdownloader.org/showthread.php?t=71264
  - [3] https://jdownloader.org/home/features
  - [4] https://my.jdownloader.org/developers/

## MyJDownloader

- `debrid/myjdownloader` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category hosted remote-control frontend for a JDownloader instance the user runs | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://my.jdownloader.org/
- price USD 0
- free tier: Registration is free and the free account is usable: 'The Customer is required to register on AppWork's website in order to use the Service. The Customer can use the Service for free after registration, which does not incur a fee. AppWork shall only offer a limited scope of Service to the Customer who uses the website for free.' No device count, call count or byte quota is published anywhere on the site. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The free tier's scope is described only as 'limited' and the paid packages that expand it are not priced on any public page reached today. The unit field says 'unlimited' because nothing is metered in bytes; it does not mean unlimited devices, which is unpublished.
- per-object cap: not applicable: MyJDownloader relays control commands and link lists to a JDownloader installation that the customer runs. No file passes through AppWork's servers. | source: [2] | note: API docs: 'the communication between the frontends and JDownloader is routed through our Connection-Server' for control traffic; downloads are made by the JD device itself.
- retention: not applicable: no file storage. Downloads land on the storage attached to the JDownloader device. | source: [1]
- egress: No file egress: the service carries API calls and link lists between the web UI/apps and the customer's JDownloader device. Terms section 2(1) defines the service as access to 'the computer program JDownloader ... installed on a computer of the Customer'. | metered: no | free allowance: none: no byte path | source: [1]
- identity: email | detail: Self-registration on the website, free. The API document exposes /captcha/getCaptcha and an account-registration route, and lists ERROR_EMAIL_NOT_CONFIRMED and EMAIL_FORBIDDEN as server errors, so a working email address is the gate.
- interface: rest
- limits:
  - request-rate: connection server answers 429 TOO_MANY_REQUESTS, 503 OVERLOAD and 503 MAINTENANCE; no published call budget [2]
  - write-gated: account registration plus email confirmation: 401 ERROR_EMAIL_NOT_CONFIRMED is an API error type [2]
- limits note: The free tier's 'limited scope' is never enumerated. Features for free users can be added, changed or withdrawn at any time ('Ein Anspruch auf die Zusatzfunktionen hat der Kunde jedoch nicht').
- binding note: Nothing in the seven-kind vocabulary fails at 1 TiB/month because no bytes cross this service: a JDownloader device does the transfer on its own connection. What fails first is architectural, not a quota: a running JD instance must be supplied, and the free tier's feature set is unpublished.
- interface detail: REST over HTTPS at https://api.jdownloader.org; the API document states 'The API is REST based, but currently only GET and POST routes are offered'. Every call carries a request id and an HMAC-SHA256 signature built from the AES-CBC session tokens; email must be lower case.
- endpoint: part of interface detail
- tooling: myjdapi (Python), the official Android/iOS apps and browser extensions, and third-party clients over the same API. A wrapper must implement AES128-CBC key exchange plus HMAC-SHA256 per call, so the barrier is the signing handshake, not a missing client.
- composes with: One MyJD account drives any JDownloader device that can be started elsewhere (a free VM), which removes the local machine from the path but not the requirement that some machine runs JD.
- reliability: Free accounts have no availability guarantee (terms: 95% monthly availability is promised only for paid packages). The connection server returns 429/503 under load, and the docs warn that results syntax 'MAY CHANGE'.
- notes: Does not answer the debrid question by itself: it resolves links only through a JDownloader installation the caller provides. The device count the requirements asks for is not published; the only device statement found is that the dashboard lists connected devices and the Android app 'manage multiple JDownloaders'. Two public JDownloader web instances were probed as part of the jdownloader record and neither accepted anonymous input.
- evidence note: Read: the English terms section and the API basics document, both live today, plus a probe of the API host. A measured rung needs a signed /my/connect plus a real device; that was not attempted.
- self hosted: yes
- extras:
  - device_count: unpublished: no page on my.jdownloader.org or the terms names a maximum number of devices; the free tier is described as 'limited scope'
  - cloud_features: no cloud storage is offered; 'cloud' in the sense of remote access means the connection server relays control traffic
  - probe_record: scratch (removed)
- evidence:
  - [1] 2026-10-23: free registration with a 'limited scope of Service' and paid packages that expand it; 95% availability only for paid packages
  - [2] 2026-10-23: 'The API is REST based, but currently only GET and POST routes are offered'; AES128CBC + HMAC-SHA256 signing; /my/connect and /captcha/getCaptcha routes; 429 TOO_MANY_REQUESTS and 503 OVERLOAD error types
  - probe:https://api.jdownloader.org/my/connect?email=probe@example.invalid 2026-10-23: the API host is live and rejects an unsigned call: HTTP 400, 49 bytes, sha256 cfa5193612ce8570c18192a2311ee7d00612dc230092c480a885eba4e29f0ac2, body {"src":"MYJD","type":"BAD_PARAMETERS"}
  - [3] 2026-10-23: the web UI is a login wall: HTTP 200, 39805 bytes, challenge signature login-wall:login
- sources:
  - [1] https://my.jdownloader.org/legal/terms.html
  - [2] https://my.jdownloader.org/developers/
  - [3] https://my.jdownloader.org/login.html
