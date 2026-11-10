# DripFiles

> dripfiles.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dripfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/dripfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DripFiles (@DripFilesBot)

- `debrid/dripfiles` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file transfer service with a Telegram front end: upload, get a link, expire it | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T03:43:39.513Z (live) | stale on 2026-11-23
- url https://dripfiles.com/
- price USD 0
- free tier: "Drop a file -> get a share link. Up to 4 GB." The bot's own description is the free offer; the site terms add that 'Puedes usar partes del servicio sin cuenta' - parts of the service work without an account. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: No byte allowance and no price is published anywhere on the pages read.
- per-object cap: 4 GB per file, from the bot's description. | bytes: 4294967296 | source: [1] | note: 4 x 1024^3. The site's terms page does not restate the figure.
- retention: Not given as a number. The terms say transfers are made 'con opciones de caducidad, contraseña' - expiry and password options chosen by the sender - so retention is set per transfer rather than by a site rule. | source: [2]
- egress: Files are served by the service to whoever holds the link or password; the terms add 'historial o planes de pago' as account features. No bandwidth figure or price is published. | metered: no | source: [2]
- identity: any-phone | detail: Through the bot: a Telegram account, so any phone number. Through the site: 'partes del servicio' work with no account at all, and history or paid plans need registration.
- interface: unknown
- limits:
  - per-object-cap (binding): 4 GB per file [1]
- limits note: One number and nothing else. Transfers can be suspended, and no quota, rate or storage ceiling is published.
- binding note: At 1 TiB a month the 4 GB ceiling is met on the first large file: a 1 TiB archive is 256 transfers. Nothing else in the published terms could bind earlier.
- interface detail: Two front ends: a Telegram bot (@DripFilesBot) and a website with upload, link share and email share. No API is documented on the pages read.
- tooling: Telegram client or browser. No API and no WebDAV, so a script would have to drive one of the two front ends.
- composes with: A handoff tool rather than capacity: 4 GB per transfer with a sender-set expiry is enough to move one file between two people or two machines, and it removes the need to expose a bucket for a one-off.
- reliability: A young service with a Spanish-language terms page last updated on the day of this read and a bot that is its own distribution channel: both are signs of one operator with no published uptime. Files expire by the sender's setting, so the loss is predictable.
- notes: Included because it is a real hosted store-and-forward service and not an account mirror: the file goes into the vendor's storage and comes back as a link.
- evidence note: The bot description and the site's terms were both read and agree that the service stores and re-serves files. The 4 GB figure is reported by the bot only, not measured with an upload.
- extras:
  - front_ends: Telegram bot @DripFilesBot; website dripfiles.com
- evidence:
  - [1] 2026-10-23: the service exists as '@DripFilesBot - The official DripFiles bot' with the cap 'Up to 4 GB'
  - [2] 2026-10-23: the terms describe 'un servicio de envío y compartición de archivos' with upload, link or email sharing, expiry, password and premium features, last updated 23/10/2026
- sources:
  - [1] https://t.me/DripFilesBot
  - [2] https://dripfiles.com/
