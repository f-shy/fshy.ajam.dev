# Ploud Storage

> ploud.fr | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ploud/ | JSON https://fshy.ajam.dev/api/v1/entity/ploud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ploud Storage (PSIADE, France)

- `netdisk-pan/ploud-storage` | qualifies-with-caveat | evidence reported | binding write-gated | category hosted Nextcloud, free
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T00:20:59.760Z (inherited) | stale on 2026-11-19
- url https://storage.ploud.fr
- free tier: 1 TB per account free, documented in the provider documentation as '500 Go ou 1 To'. No paid tiers exist, establishing 1 TB as the definitive capacity ceiling. | unit: TiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MiB upload chunk per the login page's oc_appconfig; the per-object ceiling is the Nextcloud default and is not published | source: [2]
- retention: Until deleted. Public link expiry defaults to 7 days unless changed. No retention clock on stored files | source: [1]
- egress: No traffic allotment is published in the wiki or on the portal. The service is presented as free with a donation page and no metering is mentioned | metered: no | source: [3]
- identity: any-phone | detail: the signup form requires prenom, nom, date of birth, sexe, an international phone number and a postcode, plus the reCAPTCHA v3 human-verification widget. The JavaScript has no SMS or code path, so the only gate actually exercised is an email activation link
- interface: webdav, rest, rclone
- limits:
  - per-object-cap: 100 MiB upload chunk; the per-object ceiling is unpublished [2]
  - write-gated (binding): signup needs a name, date of birth, sex, an international phone number, a postcode and the reCAPTCHA v3 human-verification widget token [4]
- binding note: 1 TB free with a working WebDAV endpoint clears the capacity and protocol filters. What binds is the signup: a phone number and an address are collected, and the form is a single-sponsor instance's only gate, so an account that survives is a favour rather than a contract.
- tooling: rclone webdav, davfs2, curl -u, any Nextcloud client. The WebDAV endpoint is /remote.php/webdav/ for the legacy path and /remote.php/dav/ for the modern one, documented by the operator itself
- composes with: A clean 1 TB WebDAV bucket with no payment and no phone, which drops straight into rclone mount or a Cloudflare-fronted origin. Each account is an independent island and the signup form has a phone field, so farming is not free
- reliability: A single-sponsor instance operated by PSIADE in Toulouse. A 2024 help.nextcloud.com thread predicted imminent shutdown and reported stale certificates; the instance now answers status.php as Nextcloud 31.0.6.2 with valid TLS, so that post is stale, but one funding decision still ends it. The .jp mirror is dead
- notes: The best free Nextcloud in Europe by volume and the least durable: one sponsor, one data centre, and a 2024 forum thread that has already predicted its closure once. A reader should use it with a second copy and not as the second copy.
- extras:
  - access_mode: registration-gated
  - free_tier_exists: yes
  - region: France, near Paris
  - nextcloud_version: 31.0.6.2
  - webdav_paths: /remote.php/webdav/; /remote.php/dav/
  - aliases: Ploud Storage (PSIADE, FR); Ploud Storage (PSIADE, Toulouse)
- evidence:
  - probe:https://storage.ploud.fr/status.php 2026-10-21: HTTP 200, {"installed":true,"version":"31.0.6.2","productname":"Nextcloud"}, so a live current server
  - probe:https://storage.ploud.fr/remote.php/dav/ 2026-10-21: HTTP 401 with WWW-Authenticate: Basic realm="Ploud Storage", so the DAV read path exists and is auth-gated
  - probe:https://storage.ploud.fr/remote.php/dav/files/ 2026-10-21: HTTP 401, 584 bytes, real SabreDAV XML with Sabre\DAV\Exception\NotAuthenticated and X-Powered-By: PHP/8.3.8
  - [1] 2026-10-21: 'Vous disposez d'un espace de 500 Go ou 1 To' plus the explicit WebDAV URL https://storage.ploud.fr/remote.php/webdav/
  - [5] 2026-10-21: 'Ploud Storage: 1 espace de stockage securise et crypte de 1 To'
  - [3] 2026-10-21: operated by PSIADE SAS, servers in France near Paris, no ad model, donation page
  - [4] 2026-10-21: signup posts to php/create_userv2.php with name, date of birth, sex, phone, postcode and email plus a grecaptcha token, with no SMS code anywhere in the bundle
  - probe:https://storage.ploud.fr/status.php 2026-11-03: status.php answers the Nextcloud 31.0.6.2 status JSON, installed and not in maintenance | capture: sha256:039272e421cd1c62d07164a8fb7fe40c692b900adcb8d302052b2e8c705541ef | quote: "version":"31.0.6.2"
  - [1] 2026-11-03: the operator's wiki still states a dedicated space of 500 GB or 1 TB | capture: sha256:23153a6b99e58e63495610616e994ba7b33bfa4df16c97a31f5fbf4c9d4b708e | quote: Vous disposez d'un espace de 500 Go ou 1 To qui vous est dédié.
  - probe:https://storage.ploud.fr/remote.php/dav/ 2026-11-03: the WebDAV endpoint answers a SabreDAV NotAuthenticated error, so it is a live auth-gated WebDAV server | capture: sha256:60fb26fe83b9e3679787fd7a4ff5928c72e054b69eb2f29b53566343cb4c61ce | quote: Sabre\DAV\Exception\NotAuthenticated
- sources:
  - [1] https://wiki.ploud.fr/doku.php?id=services%3Aploud_storage
  - [2] https://storage.ploud.fr
  - [3] https://wiki.ploud.fr/doku.php?id=a_propos%3Afrequently_asked_questions
  - [4] https://www.ploud.fr/js/off/ploud-off.js
  - [5] https://www.ploud.fr/
